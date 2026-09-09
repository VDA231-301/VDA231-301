# Simple Material Definition

## Status

Schema-oriented example.

This example is intended to align with the released VDA 231-301 generic schema
v3.0.0. Validation against the referenced schema version should be performed
before productive use.

All identifiers, specifications and values are fictional and illustrative.

## Business Scenario

An interior trim component is made of glass-fibre-reinforced polypropylene.

The component has to be described with a small, understandable set of material
information that is suitable as an entry point into the VDA 231-301 data model.

The example includes:

- the component designation
- the supplier part number
- the material classification group
- the abbreviated material designation
- the human-readable material name
- the OEM context
- the version of the component definition
- a typed generic material identifier
- one applicable material specification

## Objective

This example demonstrates a simple material-related `ComponentMaster` and the
basic separation between material classification, material designation,
material identity and material specification.

It is intended as a starting point for readers who are not yet familiar with
more specialized examples such as colors, material sources, component
instances, material stacks or test results.

## When to Use This Example

Use this example when:

- a basic material-related `ComponentMaster` has to be represented
- the minimum introductory structure of a material definition has to be
  explained
- a generic material identifier has to be included
- one applicable material specification has to be referenced
- no produced part, color assignment or material-source assignment is required
- a compact starting point for implementation or onboarding is needed

Do not use this example when:

- approved colors and the actual color of a produced part have to be represented
- several material sources and the source used for production have to be
  represented
- production traceability for an individual part is required
- a component hierarchy or specification hierarchy is required
- a layered material structure is required
- test requirements or test results have to be represented
- material-catalog extensions or approval information have to be discussed

Use the **Color Definition** example for approved color definitions and the
actual color of a produced part.

Use the **Multiple Source Material** example for possible material sources and
the source actually used for a produced part.

Use the **Component Instance Traceability** example for production-related data
of individually manufactured parts.

Use the relevant VDA 270 example for odor-test requirements and results.

## Learning Goals

After reviewing this example, the reader should understand:

- how a basic material-related component is represented by a `ComponentMaster`
- how `MaterialGroup`, `MaterialClass` and `MaterialName` differ
- how a generic material identifier is represented as a typed object
- how an applicable material specification is associated with the component
- why the material identifier and specification are separate concepts
- why `ComponentMaster.Version` is provided in the Example Library

## Relevant Entity

### ComponentMaster

The `ComponentMaster` represents the generic component definition and its
material-related information.

This example contains no `ComponentInstance`. It therefore describes the
generic definition only and does not represent an individually produced part.

## Relevant Attributes

This example uses the following attributes:

- `ComponentMaster.Designation`
- `ComponentMaster.SupplierPartNumber`
- `ComponentMaster.MaterialGroup`
- `ComponentMaster.MaterialClass`
- `ComponentMaster.MaterialName`
- `ComponentMaster.OemIdentifier`
- `ComponentMaster.Version`
- `ComponentMaster.MaterialIdentifiers[]`
- `ComponentMaster.Specifications[]`
- `ComponentMaster.Comment`

## Material Description

The material is described through three distinct attributes:

- `MaterialGroup`: `Thermoplast`
- `MaterialClass`: `PP-GF30`
- `MaterialName`: `Glass fibre reinforced Polypropylene`

These attributes have different meanings and must not be used interchangeably.

`MaterialGroup` contains the material classification group.

`MaterialClass` contains the abbreviated material designation.

`MaterialName` contains the human-readable material name.

## Material Identifier

The generic material identity is maintained in
`ComponentMaster.MaterialIdentifiers[]`.

The example uses one typed material identifier:

- `IdentifierType`: `OEMMATID`
- `Value`: `OEM111ALAHJD`

The typed structure makes the provenance and meaning of the identifier explicit.

The identifier is not duplicated in `MaterialClass`, `MaterialName` or the
specification title.

## Material Specification

The applicable material specification is maintained in
`ComponentMaster.Specifications[]`.

The example uses:

- `Type`: `MaterialSpecification`
- `Number`: `OEM-PP-GF30-SPEC`
- `IssueDate`: `2026-01`
- `Title`: `Example OEM material specification for PP-GF30`

The specification identifies the applicable requirement document. It does not
replace the material identifier or the abbreviated material designation.

## Modelling Decisions

The generic component and material definition is represented by a
`ComponentMaster`.

The material classification group, abbreviated material designation and
human-readable material name are maintained separately:

- `MaterialGroup` classifies the material at group level
- `MaterialClass` carries the abbreviated material designation
- `MaterialName` carries the readable material name

The generic material identifier is represented as a typed object in
`MaterialIdentifiers[]` according to ADR 0009.

The applicable material specification is represented separately in
`Specifications[]`.

`Specification.Title` contains the title of the specification. It is not used as
a substitute for `MaterialClass` or `MaterialName`.

The `Version` attribute represents the version of the component definition,
known as a drawing or change status in an OEM PLM system, and should always be
provided when describing a component.

This example intentionally contains only one material identifier and one
specification to keep the basic modelling pattern easy to understand.

The example does not contain:

- colors
- material sources
- component instances
- component hierarchies
- specification customizations
- material stacks
- test projects or test results
- approval information
- proposed material-property or sustainability structures

## Source of Truth and References

- The generic component definition is maintained in the `ComponentMaster`.
- The component designation is maintained in
  `ComponentMaster.Designation`.
- The supplier part number is maintained in
  `ComponentMaster.SupplierPartNumber`.
- The material classification group is maintained in
  `ComponentMaster.MaterialGroup`.
- The abbreviated material designation is maintained in
  `ComponentMaster.MaterialClass`.
- The human-readable material name is maintained in
  `ComponentMaster.MaterialName`.
- The OEM context is maintained in `ComponentMaster.OemIdentifier`.
- The version or change status of the component definition is maintained in
  `ComponentMaster.Version`.
- The generic material identity is maintained in
  `ComponentMaster.MaterialIdentifiers[]`.
- The applicable material specification is maintained in
  `ComponentMaster.Specifications[]`.
- The specification remains the source of its own type, number, issue date and
  title.
- The comment explains the purpose of the example and is not the source of the
  structured material information.

## JSON Example

See `componentMaster.json`.

## Validation Status

This example is intended to align with the released VDA 231-301 generic schema
v3.0.0.

Validation against the referenced released schema version should be performed
before productive use.

The JSON file is the technical reference for the concrete field paths,
cardinalities and values used by this example.

## Related Examples

- **Color Definition**  
  Use this example when approved colors and the actual color of a produced part
  have to be represented.

- **Component Instance Traceability**  
  Use this example when production-related traceability information for
  individually manufactured parts has to be represented.

- **Multiple Source Material**  
  Use this example when possible material sources and the source actually used
  for a produced part have to be represented.

- **Material with Stack**  
  Use this example when a layered material structure has to be represented.

- **Material with Specification Customization**  
  Use this example when an application-specific requirement deviates from a
  requirement in a referenced specification.

- **Material Catalog Entry**  
  Use this draft example when broader material-catalog information and proposed
  extensions have to be discussed.

## Architectural References

- Primary entity: `ComponentMaster`
- Component designation: `ComponentMaster.Designation`
- Supplier part number: `ComponentMaster.SupplierPartNumber`
- Material classification group: `ComponentMaster.MaterialGroup`
- Abbreviated material designation: `ComponentMaster.MaterialClass`
- Human-readable material name: `ComponentMaster.MaterialName`
- Generic material identity: `ComponentMaster.MaterialIdentifiers[]`
- Applicable specification: `ComponentMaster.Specifications[]`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0008: the abbreviated material designation is maintained in
  `MaterialClass`
- ADR 0009: material identifiers are typed and stored without uncontrolled
  duplication
