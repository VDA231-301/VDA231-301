# Multiple Source Material

## Business Scenario

A supplier delivers an interior trim component made of PP-GF30 to an OEM.

The same generic material may be available from more than one material source.
The sources fulfil the same technical requirements for the component, but they
may differ in supplier, trade name, production location and source-specific
material specification.

Two distinct pieces of information have to be captured:

1. Which material sources are **approved and available** for this component,
   relevant for engineering, purchasing and multiple-source strategies, even
   before any part is produced.
2. Which material source was **actually used** for a specific produced part,
   relevant for traceability, complaint handling and root-cause analysis.

## Objective

This example demonstrates how available material sources are defined once at
the `ComponentMaster` level using the `MaterialSource` entity, and how each
produced `ComponentInstance` references its actual material source via
`MaterialSourceID`.

## When to Use This Example

Use this example when:

- more than one material source is available for the same generic material
- the sources differ in supplier, trade name, production location or
  source-specific specification
- the set of available sources must be documented before a part is produced
- the material source actually used for an individual produced part must be
  traceable

Do not use this example as the primary example for:

- documenting the lifecycle of a formal approval or listing decision
- representing approval status, validity periods or approval history
- representing material properties or sustainability information
- assigning a material-database identifier to a concrete material source

Use the **Approval Entry Draft** for a formal approval or listing decision.

Use the **Material Catalog Entry** when material catalog information,
properties or sustainability information are the primary concern.

The assignment of material-database identifiers or supplier material codes to
a concrete `MaterialSource` is a proposed extension described in ADR 0010 and
is not part of this schema-oriented example.

## Learning Goals

After reviewing this example, the reader should understand:

- how a material source is represented using the `MaterialSource` entity
- how available material sources are defined at `ComponentMaster` level via
  `MaterialSources`
- how a produced part references its actual material source via
  `ComponentInstance.MaterialSourceID`
- why material source definitions and the actual source assignment are modelled
  on two levels
- how the generic material identity remains separate from the concrete
  supplier-specific material source
- why the existence of a `MaterialSource` must not be interpreted as a complete
  approval or listing lifecycle

## Relevant Entities

### ComponentMaster

The generic definition of the component and its material.

The `ComponentMaster` holds the list of available `MaterialSources`,
independently of any individually produced part.

The generic material identity is maintained on the `ComponentMaster` and is
not replaced by the supplier-specific information of a `MaterialSource`.

### MaterialSource

An embedded entity describing a concrete supplier-specific material source.

A `MaterialSource` can contain information such as:

- material name
- material class
- trade name
- supplier
- production location
- source-specific specification
- additional information

The `TradeName` identifies the supplier's commercial product name. It is
distinct from the generic material name, the abbreviated material designation
and the generic material identifier.

### ComponentInstance

A specific manufactured instance of the component.

The `ComponentInstance` documents the material source actually used for the
produced part by referencing one of the source definitions maintained on the
related `ComponentMaster` via `MaterialSourceID`.

> **Note:** Within the `ComponentMaster`, the property that holds the material
> sources is named `MaterialSources`, plural in the context of the master.
> Each entry in this list is an object of type `MaterialSource`, indicated by
> its `"_type": "MaterialSource"`.
>
> The same convention applies to `Instances`, with entries of type
> `ComponentInstance`, and to `Colors`, with entries of type `Color`.

## Relevant Attributes

This example focuses on the following attributes:

- `ComponentMaster.Designation`
- `ComponentMaster.Version`
- `ComponentMaster.MaterialGroup`
- `ComponentMaster.MaterialClass`
- `ComponentMaster.MaterialName`
- `ComponentMaster.MaterialIdentifiers`
- `ComponentMaster.MaterialSources`
- `MaterialSource.MaterialName`
- `MaterialSource.MaterialClass`
- `MaterialSource.TradeName`
- `MaterialSource.Supplier`
- `MaterialSource.Specification`
- `MaterialSource.AdditionalInformation`
- `ComponentMaster.Instances`
- `ComponentInstance.SerialNumber`
- `ComponentInstance.ProductionBatchNumber`
- `ComponentInstance.MaterialSourceID`

## Modelling Decisions

The material source information is intentionally modelled on **two levels**:

- The `ComponentMaster` holds the **definition set** of available material
  sources in its `MaterialSources` list.
- The `ComponentInstance` documents the **actual material source** used for a
  produced part by referencing one of the master's source definitions via
  `MaterialSourceID`.

This separation keeps the `ComponentMaster` reusable across all available
sources and avoids duplicating material source definitions on individual
instances.

A produced part does not introduce a new material source. It references one of
the source definitions maintained on the related `ComponentMaster`.

The generic material and the concrete material source must remain separate:

- The generic material is represented on the `ComponentMaster`.
- The generic material identity is maintained in
  `ComponentMaster.MaterialIdentifiers`.
- A concrete supplier-specific material is represented as a `MaterialSource`.
- The supplier's commercial product name is maintained in
  `MaterialSource.TradeName`.
- The source-specific requirement specification is maintained in
  `MaterialSource.Specification`.
- The produced part references the source actually used through
  `ComponentInstance.MaterialSourceID`.

The material description uses distinct fields with non-overlapping meanings:

- `MaterialGroup` holds the material classification group according to
  VDA 231-106, here `Thermoplast`.
- `MaterialClass` holds the abbreviated material designation according to
  ADR 0008, here `PP-GF30`.
- `MaterialName` holds the human-readable material name, here
  `Glass fibre reinforced Polypropylene`.
- `TradeName` holds the commercial product name of a concrete supplier
  material.
- `MaterialIdentifiers` holds the identifying keys of the generic material.

Material identifiers are represented as typed objects according to ADR 0009.
Each entry carries an `IdentifierType` and a `Value`, so that identifiers of
different provenance remain distinguishable.

The `Version` attribute represents the version or change status of the
component definition and should always be provided when describing a component
in the Example Library.

This example describes alternative material sources for the same generic
material. It does not model uncontrolled material substitutions.

The existence of a `MaterialSource` in `ComponentMaster.MaterialSources` does
not represent a complete formal approval or listing lifecycle. Approval status,
status history, approval scope and validity are separate concerns addressed by
the **Approval Entry Draft**.

## Source of Truth and References

- The generic material definition is maintained on the `ComponentMaster`.
- The generic material identity is maintained in
  `ComponentMaster.MaterialIdentifiers`.
- The available material source definitions are maintained in
  `ComponentMaster.MaterialSources`.
- Each entry in `ComponentMaster.MaterialSources` represents a concrete
  supplier-specific material source.
- The supplier's commercial product name is maintained in
  `MaterialSource.TradeName`.
- The supplier and production location are represented through
  `MaterialSource.Supplier`.
- The source-specific specification is maintained in
  `MaterialSource.Specification`.
- `ComponentInstance.MaterialSourceID` references the material source actually
  used for a specific produced part.
- The `ComponentInstance` does not define or duplicate the material source. It
  references one of the source definitions maintained on the related
  `ComponentMaster`.
- The generic `OEMMATID` is not duplicated on the `MaterialSource`.
- Own business identifiers of a concrete material source would be maintained
  in `MaterialSource.Identifiers` according to proposed ADR 0010. This
  proposed field is not used as a released field in this schema-oriented
  example.

## JSON Example

See `componentMaster-with-materialSources.json`.

## Validation Status

This example is intended to align with the generic schema v3.0.0, in which
`ComponentMaster.MaterialSources` and
`ComponentInstance.MaterialSourceID` are defined.

Validation against the referenced released schema version should be performed
before productive use.

The proposed `MaterialSource.Identifiers` structure described in ADR 0010 is
not part of this schema-oriented example.

## Related Examples

- **Simple Material Definition**  
  Use this example for a basic material-related representation without
  supplier-specific material sources.

- **Component Instance Traceability**  
  Use this example for general production traceability information of
  individual produced parts.

- **Color Definition**  
  Use this example for the analogous pattern in which colors are defined in
  `ComponentMaster.Colors` and the actual color is referenced through
  `ComponentInstance.ColorID`.

- **Material Catalog Entry**  
  Use this example when a reusable material catalog entry with colors,
  suppliers, material sources and regional availability is the primary concern.

- **Approval Entry Draft**  
  Use this example when a formal approval or listing decision for a concrete
  material source must be represented, including status, scope and validity.

- **Odor Test with Concrete Material Source**  
  Use this draft example when a concrete material source and its proposed
  material-database identifier must be connected to a complete VDA 270 test.

## Architectural References

- Entity: `MaterialSource`
- Definition set: `ComponentMaster.MaterialSources`
- Reference: `ComponentInstance.MaterialSourceID`
- Generic material identity: `ComponentMaster.MaterialIdentifiers`
- Supplier trade name: `MaterialSource.TradeName`
- Source-specific specification: `MaterialSource.Specification`
- Analogous pattern:
  `ComponentMaster.Colors` /
  `ComponentInstance.ColorID`
- ADR 0001: Definition sets on `ComponentMaster`, concrete assignments on
  `ComponentInstance`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0008: Abbreviated material designation to `MaterialClass`
- ADR 0009: Typed material identifiers without duplication
- ADR 0010: Typed identifiers on `MaterialSource`, proposed
