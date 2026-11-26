# ERM Guide: Components, Engineering Materials and Material Approvals

## 1. Purpose and document status

This guide explains the material and component area of the VDA 231-301 entity-relationship model (ERM). It complements the [glossary](CONTEXT.md) and the [JSON schema](../main/VDA_231-301_Schema_Generic.json).

**Status: Initial ERM-oriented working draft for review.**

**Target branch:** `feat/44-engineering-material` (FEAT44).



## 2. The model in plain language

The material and component area answers different questions:

| Question | Concept |
| --- | --- |
| Which component is being described? | `ComponentMaster` |
| Which technically defined material is assigned to the component? | `EngineeringMaterial`, through `ComponentMaterialAssignment` |
| Which concrete supplier material is being considered? | `MaterialSource` |
| What is the approval status of that supplier material for a particular material definition? | `MaterialApproval` |
| Which physical component was produced or received? | `ComponentInstance` |
| Which supplier materials and colour are recorded for that physical component? | `ComponentInstance.MaterialSourceID` (array) and `ComponentInstance.ColorID` in JSON |

These questions must remain separate. A material definition is not a supplier product. A supplier product is not an approval. A reusable component definition is not a physical component.

## 3. Components and their material assignments

### 3.1 ComponentMaster: the reusable component definition

**Purpose.** `ComponentMaster` describes a component independently of a particular physical instance. It holds component identification and component-specific requirements.

**Boundary.** It is neither the material definition nor the record of an individual produced component.

**Relationships.** The supplied ERM connects the component definition with material assignments and physical component instances. It also shows a `SubComponents` self-relationship for component structures.

**Example.** A housing definition describes which housing is meant and which component-specific requirements apply. The actual housing produced on a particular date is represented separately as a `ComponentInstance`.

### 3.2 ComponentMaterialAssignment: how a material is used in a component

**Purpose.** `ComponentMaterialAssignment` describes the association of a component with an engineering material or a layer stack.

**Important information shown in the ERM:**

- `EngineeringMaterialID`: reference to an engineering material.
- `MaterialRole`: the role of the material, for example base material, coating, adhesive or insert.
- `Stack`: a layer-stack description.
- `GeographicScope`: geographic qualification of the assignment.

The listed material roles are examples, not a closed code list.

**Why a separate assignment?** The material definition describes the material itself. The assignment describes its use in a particular component. This allows the same material definition to be used in different component contexts without treating those contexts as new material definitions.

**Example.** A housing uses one engineering material as its base material and another as a coating. The assignments distinguish these roles.

The permitted combinations of `EngineeringMaterialID` and `Stack`, including whether either or both must be present, are not established by this guide.

### 3.3 Stack and StackLayer: a layered material structure

The supplied ERM shows `Stack` with a `Layers` structure. `StackLayer` includes `LayerNumber`, `EngineeringMaterialID`, `Thickness`, `Mass` and `Comment`.

A layer stack describes a layered structure; a component hierarchy describes components and subcomponents. These are different modelling concepts.

**Example.** A coated structure can be described through its individual material layers. A component assembly can instead contain separate subcomponents. The choice depends on what is being represented.

This guide does not prescribe JSON containment or derive additional cardinalities from the screenshot.

## 4. EngineeringMaterial: the technical material definition

### 4.1 Purpose and boundary

`EngineeringMaterial` describes the technically defined material of a component. Depending on company terminology, this can be a design material or a production material.

It is distinct from a concrete supplier product, trade name, physical component or production batch.

The supplied ERM includes material classification and naming, material identifiers, specifications, a definition level, possible material sources and additional information.

### 4.2 Design material and production material

The supplied Context.md distinguishes:

- **Design material:** a material requirement profile used in engineering design, independent of a particular production plant or supplier.
- **Production material:** a narrower, manufacturing-related requirement profile of the same material, for example for plant-specific or supplier-specific procurement.

A production material remains a requirement profile. It must not be confused with the concrete supplier material described by `MaterialSource`.

The ERM shows `MaterialDefinitionLevel` and a self-reference named `DerivedFromEngineeringMaterialID`. The latter identifies the engineering material from which another definition is derived.

**Illustrative use.** A manufacturing-related material definition may refer back to the design material from which it was derived.

The reference alone does not establish automatic inheritance, requirement merging, version propagation or transfer of approvals.

### 4.3 Names, classes and identifiers

An engineering material has three required descriptive fields.

| Field | Bearing-pin example |
|-------|---------------------|
| `MaterialGroup` | `Steel` |
| `MaterialClass` | `Stainless steel` |
| `MaterialName` | `1.4301-X5CrNi18-10` |

The OEM specification key belongs in `MaterialSpecificationIdentifier`. See the [material identification guide](<Material Identification Concepts_VDA 231-301.md>).

## 5. MaterialSource: the concrete supplier material

**Purpose.** `MaterialSource` describes a concrete supplier material with its trade name, supplier and source-specific specification or datasheet.

The supplied ERM also shows source identifiers, production site, business keys and additional information.

**Boundary.** A material source is not the engineering requirement profile. Its existence or association with an engineering material does not by itself establish approval.

**Relationship to EngineeringMaterial.** One material definition can be associated with different supplier materials. Conversely, the same supplier material can be associated with different engineering-material definitions. The approval status must therefore be evaluated for the relevant combination, not for the source alone.

**Example.** Supplier material A can be considered for material definitions X and Y. Whether it is approved for X says nothing by itself about its approval for Y.

## 6. MaterialApproval: approval for a particular material definition

### 6.1 Purpose

`MaterialApproval` records the approval-process status of a concrete supplier material for a particular engineering-material definition.

The ERM records `EngineeringMaterialID` and shows the supplier product through an association to `MaterialSource`. It also shows the approval type, status, scope, validity dates and status history.

An approval record can describe an ongoing process. The presence of a record does not mean approval has already been granted.

### 6.2 Why both references are needed

Consider the same supplier material associated with two engineering-material definitions:

| Approval record | MaterialSource | EngineeringMaterial | Business status |
| --- | --- | --- | --- |
| Approval A-X | Supplier material A | Material definition X | Approved |
| Approval A-Y | Supplier material A | Material definition Y | Under evaluation |

These are fictional labels and plain-language statuses, not JSON payloads or prescribed status codes.

A statement such as “Supplier material A is approved” would be incomplete. It would not identify which material definition the approval applies to.

A source-specific approval in the ERM concerns both the supplier product and the engineering material. The repository JSON schema does not define `MaterialApproval`.

### 6.3 Assignment, approval and actual use are different

- **Association:** a supplier material is associated with a material definition.
- **Approval:** a record documents its approval-process status for that definition.
- **Actual use:** a physical component records the supplier material or materials used.

None of these statements automatically proves the other two. In particular, recording actual use does not by itself prove a valid approval for the relevant context and date.

## 7. ComponentInstance and Color: the physical component context

### 7.1 ComponentInstance

`ComponentInstance` represents a physical component separately from its reusable definition. The supplied ERM includes production and traceability information such as production site, machine, tool, cavity, serial number, batch number and dates.

The diagram labels the source list `MaterialSourceIDs`. The JSON property is `MaterialSourceID`, an array of `MaterialSource` identifiers, even when only one source was used. `ColorID` holds a single colour identifier.

**Example.** A produced housing records the supplier material actually used and its colour, while its `ComponentMaster` describes the reusable housing definition.

A list of material-source references does not, by itself, explain which source belongs to which material assignment, role or layer in a multi-material component. This guide does not invent an additional mapping. Any mapping rule must be confirmed from the branch or documented separately.

### 7.2 Color

The supplied ERM shows `Color` with `ID`, `Name`, `Code`, `CodeAuthority` and additional information. `ComponentInstance.ColorID` refers to a colour record.

The colour reference identifies the recorded colour; it is not a material-approval record.

## 8. A connected example

All names in this example are fictional. The example explains relationships and is not a schema-valid JSON example.

1. **Define the component.** A `ComponentMaster` describes a housing.
2. **Assign the material.** A `ComponentMaterialAssignment` associates the housing with engineering-material definition X as its base material.
3. **Describe the supplier product.** `MaterialSource` A describes a concrete supplier material.
4. **Record the approval context.** Approval A-X records that source A is approved for definition X.
5. **Keep a second context separate.** Approval A-Y records that the same source A is still under evaluation for definition Y.
6. **Record the physical component.** A `ComponentInstance` represents a produced housing and records source A in its material-source references, together with the relevant production information.

The example keeps the component definition, material definition, supplier product, approval status and physical component distinct.

## 9. Common misunderstandings

| Misunderstanding | Clarification |
| --- | --- |
| EngineeringMaterial is the supplier's trade product. | The technical material definition and the concrete supplier material are separate concepts. |
| Production material and MaterialSource mean the same thing. | A production material is a manufacturing-related requirement profile; MaterialSource describes the concrete supplier material. |
| A source listed for a material is automatically approved. | Association and approval status are separate. |
| A supplier material has one approval status for every use. | Its status can differ between engineering-material definitions. |
| A derived material automatically inherits approval. | The derivation reference alone establishes no approval-transfer rule. |
| A source recorded on a physical component proves approval. | Actual use and valid approval must be considered separately. |
| A relationship in the ERM proves a JSON Schema implementation. | Technical availability and validation rules require schema evidence. |




