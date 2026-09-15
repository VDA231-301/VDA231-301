# VDA 231-301 Example Library

This folder contains example files illustrating typical modelling patterns for
the VDA 231-301 data model.

The examples are intended to support:

- onboarding of new users
- discussion of modelling approaches
- documentation of recommended usage patterns
- preparation of validation and tooling examples

## Purpose

The examples are not meant to replace the JSON Schema documentation. Instead,
they show how selected parts of the data model can be applied in realistic
business scenarios.

Each example contains:

- a `README.md` explaining the business scenario and modelling decisions
- one or more JSON files illustrating the corresponding data structure

Examples have different validation statuses; consult each example's README
before using it against a released generic schema version. Some examples
(catalog, approval and other drafts) intentionally use structures that are not
part of the released generic schema v3.0.0 and are marked accordingly.

Schema-oriented examples currently target generic schema **v3.0.0**. The exact target
version is stated per example in the "Validation status" column and in each
example's README.

## Find the Right Example

Use the following navigation guide to identify the example that best matches
your use case.

| If you want to... | Start with |
|---|---|
| Understand the basic structure of a material definition | [Simple material definition](./simple-material-definition/) |
| Add color information to a component or material representation | [Color definition](./color-definition/) |
| Trace individual physical component instances using serial and production information | [Component instance traceability](./component-instance-traceability/) |
| Represent a component hierarchy with subcomponents | [Component master hierarchy](./component-master-hierarchy/) |
| Apply a customized specification to a material or component | [Material with specification customization](./material-with-specification-customization/) |
| Represent a multilayer material or coating stack | [Material with stack](./material-with-stack/) |
| Represent material information from multiple sources | [Multiple-source material](./multiple-source-material/) |
| Represent characteristic requirements for a metal material | [Material with characteristic requirements (metal)](./material-with-characteristic-requirements-metal/) |
| Represent characteristic requirements for an elastomer material | [Material with characteristic requirements (elastomer)](./material-with-characteristic-requirements-elastomer/) |
| Identify a component using an NGID path | [NGID-identified component](./ngid-identified-component/) |
| Represent a hierarchy of referenced specifications | [Specification hierarchy](./specification-hierarchy/) |
| Represent a generic material catalog entry (draft) | [Material catalog entry](./material-catalog-entry/) |
| Represent an independent approval / listing decision (draft) | [Approval entry (draft)](./approval-entry-draft/) |
| Model a minimal VDA 270 odor test | [Odor VDA 270 – getting started](./odor-vda270-simple/) |
| Model a complete VDA 270 odor test | [Odor VDA 270 – complete](./odor-vda270-complete/) |
| Model a complete VDA 270 odor test with a material source (draft) | [Odor complete with material source (draft)](./odor-complete-with-material-source-draft/) |

## Example Overview

The following matrix provides an overview of the available examples, their
scenario, demonstrated modelling concept, main entities, validation status and
related Architectural Decision Records.

| Example | Scenario | Demonstrated modelling concept | Main entities used | Validation status | Related ADRs |
|---|---|---|---|---|---|
| [Simple material definition](./simple-material-definition/) | Define a basic material-related component. | Material identification and specification references on a reusable component definition. | `ComponentMaster`, `Specification`, `MaterialIdentifier` | Aligned with generic schema v3.0.0 | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) |
| [Color definition](./color-definition/) | Add approved colors and record the color used by a produced part. | Definition sets on the master and concrete assignments on instances. | `ComponentMaster`, `ComponentInstance`, `Color` | Aligned with generic schema v3.0.0 | [ADR-0001](../docs/adr/0001-definition-set-on-master-assignment-on-instance.md) <br> [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) <br> [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0009](../docs/adr/0009-typed-material-identifiers-no-duplication.md) |
| [Component instance traceability](./component-instance-traceability/) | Trace physical parts using serial and production information. | Separation of a reusable component definition from individually produced instances. | `ComponentMaster`, `ComponentInstance`, `Location` | Aligned with generic schema v3.0.0 | [ADR-0001](../docs/adr/0001-definition-set-on-master-assignment-on-instance.md) |
| [Component master hierarchy](./component-master-hierarchy/) | Represent a component structure containing subcomponents. | Recursive containment of component definitions. | `ComponentMaster` | Aligned with generic schema v3.0.0 | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) <br> [ADR-0005](../docs/adr/0005-hierarchies-via-self-reference.md) |
| [Material with specification customization](./material-with-specification-customization/) | Apply OEM-specific requirements that differ from a referenced specification. | Explicit representation of original and application-specific requirement values. | `ComponentMaster`, `Specification`, `SpecificationCustomization`, `DeviatingProperty` | Aligned with generic schema v3.0.0 | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) |
| [Material with stack](./material-with-stack/) | Represent a multilayer material or coating system. | Ordered layers with material, mass and thickness values. | `ComponentMaster`, `Stack` | Aligned with generic schema v3.0.0 | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) <br> [ADR-0003](../docs/adr/0003-stack-layer-ordering.md) |
| [Multiple-source material](./multiple-source-material/) | Represent alternative supplier-specific sources for one material. | Separation of a generic material definition from concrete sources and instance assignments. | `ComponentMaster`, `ComponentInstance`, `MaterialSource`, `Specification`, `Location` | Aligned with generic schema v3.0.0 | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) <br> [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0010](../docs/adr/0010-materialsource-typed-identifiers.md) |
| [Material with characteristic requirements (metal)](./material-with-characteristic-requirements-metal/) | Express target characteristics for a metal material. | Machine-readable characteristic requirements attached to a specification. | `TestingProject`, `ComponentMaster`, `Specification`, `CharacteristicRequirement` | Aligned with generic schema v3.0.0 | [ADR-0007](../docs/adr/0007-material-characteristics-read-out-logic.md) <br> [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0009](../docs/adr/0009-typed-material-identifiers-no-duplication.md) |
| [Material with characteristic requirements (elastomer)](./material-with-characteristic-requirements-elastomer/) | Express target characteristics for an elastomer material. | Machine-readable characteristic requirements attached to a specification. | `TestingProject`, `ComponentMaster`, `Specification`, `CharacteristicRequirement` | Aligned with generic schema v3.0.0 | [ADR-0007](../docs/adr/0007-material-characteristics-read-out-logic.md) <br> [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0009](../docs/adr/0009-typed-material-identifiers-no-duplication.md) |
| [NGID-identified component](./ngid-identified-component/) | Link material and test information to a CAD assembly occurrence. | Stable CAD occurrence identification through `NGIDPath`. | `ComponentMaster` | Aligned with generic schema v3.0.0 | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) <br> [ADR-0004](../docs/adr/0004-ngid-path-representation.md) |
| [Specification hierarchy](./specification-hierarchy/) | Reference reusable specifications from a higher-level specification. | Recursive specification references rather than containment. | `ComponentMaster`, `Specification` | Schema-oriented example (see README) | [ADR-0005](../docs/adr/0005-hierarchies-via-self-reference.md) <br> [ADR-0006](../docs/adr/0006-norm-information-aggregation.md) <br> [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) |
| [Material catalog entry](./material-catalog-entry/) | Represent a generic material with supplier-specific sources. | Separation of material identity, concrete sources and approval information. | `ComponentMaster`, `MaterialSource`, `Specification`, `Location` | Draft – not schema-conformant | [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0009](../docs/adr/0009-typed-material-identifiers-no-duplication.md) <br> [ADR-0010](../docs/adr/0010-materialsource-typed-identifiers.md) <br> [ADR-0011](../docs/adr/0011-approvalentry-links-generic-material-oemmatid.md) |
| [Approval entry (draft)](./approval-entry-draft/) | Represent an approval or listing decision independently from material data. | Approval as a separate referenceable business object. | `ApprovalEntry`, `MaterialSource` | Draft – intentionally not part of generic schema v3.0.0 | [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0009](../docs/adr/0009-typed-material-identifiers-no-duplication.md) <br> [ADR-0010](../docs/adr/0010-materialsource-typed-identifiers.md) <br> [ADR-0011](../docs/adr/0011-approvalentry-links-generic-material-oemmatid.md) |
| [Odor VDA 270 – getting started](./odor-vda270-simple/) | Model a minimal VDA 270 odor test. | Separation of target properties, reported properties and assessment. | `TestingProject`, `ComponentMaster`, `Topic` | Schema-oriented example (see README) | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) <br> [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0009](../docs/adr/0009-typed-material-identifiers-no-duplication.md) |
| [Odor VDA 270 – complete](./odor-vda270-complete/) | Model a VDA 270 odor test with executions and individual grades. | Traceability from individual results to a consolidated result and assessment. | `TestingProject`, `ComponentMaster`, `ComponentInstance`, `Topic`, `TestExecution` | Schema-oriented example (see README) | [ADR-0002](../docs/adr/0002-componentmaster-version-mandatory.md) <br> [ADR-0008](../docs/adr/0008-abbreviated-material-designation-to-materialclass.md) <br> [ADR-0009](../docs/adr/0009-typed-material-identifiers-no-duplication.md) |
| [Odor complete with material source (draft)](./odor-complete-with-material-source-draft/) | Extend the complete odor test with a concrete supplier material source. | Assignment of a concrete material source to the tested component instance. | `TestingProject`, `ComponentMaster`, `ComponentInstance`, `MaterialSource`, `Topic` | Draft (see README) | [ADR-0001](../docs/adr/0001-definition-set-on-master-assignment-on-instance.md) <br> [ADR-0010](../docs/adr/0010-materialsource-typed-identifiers.md) |

Each example folder contains a dedicated README and the corresponding JSON
example.

## Example Details

### simple-material-definition

The minimal "hello world" example. Describes a component and its material using
a `ComponentMaster` with a referenced specification.

File: `componentMaster.json`

### color-definition

Shows how approved colors are defined at `ComponentMaster` level via `Colors`
and how each produced `ComponentInstance` references its actual color via
`ColorID`.

File: `componentMaster-with-color.json`

### multiple-source-material

Shows how approved material sources are defined at `ComponentMaster` level via
`MaterialSources` and how each produced `ComponentInstance` references its
actual source via `MaterialSourceID`. Following ADR 0008, `MaterialClass` holds
the abbreviated material designation and `MaterialName` the readable name,
consistently on master and sources.

File: `componentMaster-with-materialSources.json`

### component-instance-traceability

Shows how individually produced parts are represented as `ComponentInstance`
objects within a `ComponentMaster`, each carrying its own production
traceability information (batch, site, machine, tool, cavity).

File: `componentInstance.json`

### material-with-stack

Shows how a layered material structure is represented using the `Stack`
property with `ArraySpec` and `ArrayValue` (LayerNumber, Material, Mass,
Thickness).

File: `componentMaster-with-stack.json`

### material-with-specification-customization

Shows how an OEM-specific deviation from a referenced specification is
documented using `SpecificationCustomizations` and `DeviatingProperty`, without
changing the referenced specification itself.

File: `componentMaster-with-specificationCustomization.json`

### material-with-characteristic-requirements-metal

Shows how characteristic requirements for a metal material are read out into
`Specification.CharacteristicRequirements` following the classification logic of
ADR 0007. `MaterialClass` carries the abbreviated designation (e.g. a steel
name per EN 10027-1, ADR 0008) and `MaterialIdentifiers` uses the typed form
(ADR 0009). The values and the OEM material requirement specification are
illustrative and do not reproduce a normative material standard.

File: `material-with-characteristic-requirements-metal.json`

### material-with-characteristic-requirements-elastomer

Shows how characteristic requirements for an elastomer material are read out
into `Specification.CharacteristicRequirements` following the classification
logic of ADR 0007. `MaterialClass` carries the abbreviated designation
(e.g. an elastomer symbol per ISO 1629, ADR 0008) and `MaterialIdentifiers`
uses the typed form (ADR 0009). The values and the OEM material requirement
specification are illustrative and do not reproduce a normative material
standard.

File: `material-with-characteristic-requirements-elastomer.json`

### ngid-identified-component

Shows how a `ComponentMaster` is linked to its occurrence in a CAD assembly
structure using `NGIDPath`, following the Siemens NGID specification.

File: `componentMaster-with-ngid.json`

### component-master-hierarchy

Shows how a component hierarchy is modelled using
`ComponentMaster.SubComponents`, where each subcomponent is itself a
`ComponentMaster`. Demonstrates that a component can be a top-level node or a
subcomponent depending on its position in the tree (containment relationship).

File: `componentMaster-with-subComponents.json`

### specification-hierarchy

Shows how a specification can reference other specifications via
`Specification.ReferencedSpecifications`, so that a higher-level specification
references several sub-specifications (reference relationship). Complements the
component hierarchy example by contrasting "reference" with "containment".

File: `componentMaster-with-specificationHierarchy.json`

### material-catalog-entry

Shows how a generic material catalog entry is represented and how supplier-
specific sources relate to it, keeping generic material and concrete sources
separate (ADR 0008/0010) and referencing approvals as separate `ApprovalEntry`
objects (ADR 0011). Draft example: it uses structures that are not part of the
released generic schema v3.0.0. Consult the folder README before use.

### approval-entry-draft

Shows how an approval or listing decision can be represented as an independent,
referenceable `ApprovalEntry` business object, separated from the generic
material definition, the concrete supplier `MaterialSource`, and the product /
PLM context. `ApprovedForMaterial` references the generic material by its
OEMMATID business key (ADR 0011), while `Subject` describes the concrete source
(ADR 0008/0010) and identifiers follow the single-source-of-truth principle of
ADR 0009. Draft example: `ApprovalEntry` and all approval-related structures are
intentionally not part of the released generic schema v3.0.0.

### odor-vda270-simple

Minimal VDA 270 odor test represented as a `TestingProject` (getting-started
scenario).

File: `testingProject-vda270-getting-started.json`

### odor-vda270-complete

Complete VDA 270 odor test represented as a `TestingProject`.

File: `testingProject-vda270-complete.json`

### odor-complete-with-material-source-draft

Complete VDA 270 odor test that also references a material source. Draft
example; consult the folder README before use.

## Conventions

The examples follow a set of shared conventions. Key architectural decisions are
documented as Architectural Decision Records (ADRs) in `docs/adr`:

- Definition sets are held on the `ComponentMaster`, concrete assignments on the
  `ComponentInstance` (e.g. `Colors` / `ColorID`, `MaterialSources` /
  `MaterialSourceID`).
- `ComponentMaster.Version` (drawing / change status, ZGS) is included in every
  component example.
- Stack layers are numbered starting with 1 for the bottom (substrate) layer.
- `NGIDPath` examples use the `JT_PROP_NAME` identifier with CADID-formatted
  node values.
- The abbreviated material designation is held in `MaterialClass`, the readable
  name in `MaterialName` (ADR 0008).
- Material identifiers are modelled as typed objects and stored once (ADR 0009,
  and ADR 0010 for `MaterialSource`).

## Self-referencing structures

Two examples illustrate self-referencing (recursive) structures, which are a
common source of confusion:

- `component-master-hierarchy` uses `ComponentMaster.SubComponents`. This is a
  **containment** relationship: a parent component contains its subcomponents.
- `specification-hierarchy` uses `Specification.ReferencedSpecifications`. This
  is a **reference** relationship: a higher-level specification references other
  specifications that exist in their own right and can be reused by many
  specifications and components.

In both cases the role of an object (top node vs. subordinate) is not a property
of the object itself; it results from its position in the tree.

## Naming Conventions

- Example folders use lower-case names with hyphens.
- JSON files use descriptive names, for example `componentMaster.json` or
  `componentMaster-with-color.json`.

## Modelling Principles

- Focus on one modelling topic per example.
- Keep examples as simple as possible while preserving the learning objective.
- Use anonymized identifiers and fictional specifications.
- Avoid company-specific confidential information.
- Explain important modelling decisions in the example's README.

## Future Examples

Potential future examples include:

- layer-specific requirements
- additional topic-based examples (e.g. further VDA 278 results)
- a complete minimal testing project
