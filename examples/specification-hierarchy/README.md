# Specification Hierarchy

## Status

ERM-aligned example.

The modelling pattern is defined in the entity relationship model and supported
by ADR 0005.

At the documented state of this example,
`Specification.ReferencedSpecifications` is not yet available in the released
generic JSON schema. The example therefore cannot yet be validated against the
released schema version.

## Business Scenario

Specifications are not always standalone documents.

A specification can be used independently, for example a test specification
such as VDA 270. The same specification can also be referenced by a higher-level
specification.

A typical example is an OEM product requirement specification for an interior
trim component. The product requirement specification does not repeat every
requirement. Instead, it references other specifications, such as:

- test specifications
- material specifications
- other applicable requirement specifications

The referenced specifications continue to exist independently and can be reused
by other specifications and components.

This example shows how such a specification hierarchy is represented in the
VDA 231-301 data model.

## Objective

This example demonstrates how a higher-level `Specification` references other
independent `Specification` objects through
`Specification.ReferencedSpecifications`.

## When to Use This Example

Use this example when:

- a higher-level specification references other specifications
- the referenced specifications remain independent and reusable
- a product specification refers to test, material or other requirement
  specifications
- specification relationships with more than one hierarchy level have to be
  represented
- referenced specifications must not be duplicated in the higher-level
  specification

Do not use this example to represent a component or assembly hierarchy.

A component hierarchy uses `ComponentMaster.SubComponents`. That relationship
is a containment relationship and is demonstrated in the
**Component Master Hierarchy** example.

Use the **Material with Specification Customization** example when an
application-specific deviation from a referenced specification has to be
documented. A customization changes neither the identity nor the content of the
referenced specification.

## Learning Goals

After reviewing this example, the reader should understand:

- that a `Specification` can be used independently or referenced by another
  `Specification`
- how a higher-level specification references other specifications through
  `Specification.ReferencedSpecifications`
- that a referenced specification has the same structure as a higher-level or
  standalone `Specification`
- that the role of a specification results from its position in the hierarchy
- that the specification hierarchy is a recursive self-reference
- that referenced specifications remain independent and reusable
- how specification referencing differs from component containment
- why referenced specifications are not duplicated in the higher-level
  specification

## Relevant Entities

### ComponentMaster

The `ComponentMaster` represents the component to which the higher-level
specification applies.

The applicable specifications are maintained in
`ComponentMaster.Specifications`.

### Specification

A `Specification` represents a product, test, material or other requirement
specification.

Through `ReferencedSpecifications`, a `Specification` can reference further
`Specification` objects and thereby form a recursive reference hierarchy.

The same entity type is used for:

- a specification assigned directly to a `ComponentMaster`
- a higher-level specification
- every specification referenced by another specification
- every specification referenced at a deeper hierarchy level

Whether a specification is used independently, assigned directly to a
component or referenced by another specification is not represented through a
separate entity type. Its role results from its position in the structure.

> **Note:** `ReferencedSpecifications` is a list of `Specification` objects.
> This is a self-reference because the same entity type is used for the
> higher-level specification and for every referenced specification.

## Relevant Attributes

This example focuses on the following attributes:

- `ComponentMaster.Specifications`
- `Specification.Type`
- `Specification.Number`
- `Specification.SubNumber`
- `Specification.IssueDate`
- `Specification.Title`
- `Specification.ReferencedSpecifications`

## Modelling Decisions

A specification hierarchy is modelled through a `Specification` that references
other `Specification` objects using `ReferencedSpecifications`.

In this example, an OEM product requirement specification references:

- test specifications
- a material specification

The referenced specifications are not copied into separate subordinate entity
types. Each referenced entry is represented as a regular `Specification`.

Because every referenced specification is itself a `Specification`, it can
reference further specifications. This creates a recursive structure that can
represent more than one hierarchy level.

The relationship between a higher-level specification and the specifications
it references is a **reference relationship**:

- the referenced specification exists independently
- the referenced specification can be reused
- the same specification can be referenced by different higher-level
  specifications
- the higher-level specification does not own the referenced specification as
  a contained subordinate object
- the requirements of the referenced specification are not duplicated in the
  higher-level specification

This differs from the relationship used in a component hierarchy:

- `ComponentMaster.SubComponents` represents containment
- `Specification.ReferencedSpecifications` represents references to
  independent specifications

The role of a `Specification` is determined by its position in the hierarchy.
A separate entity type such as `SubSpecification` is not required.

`Specification.Title` contains the title of the specification itself. It must
not be used for a material short name. According to ADR 0008, the abbreviated
material designation is maintained in `MaterialClass`.

Where several regulations apply to a material or surface, a primary
`Specification` can reference further applicable specifications through
`ReferencedSpecifications`, following the norm aggregation principle defined
in ADR 0006.

## Source of Truth and References

- The specifications assigned to the component are maintained in
  `ComponentMaster.Specifications`.
- The higher-level specification is represented as a `Specification`.
- Specifications referenced by the higher-level specification are maintained
  in `Specification.ReferencedSpecifications`.
- Each entry in `Specification.ReferencedSpecifications` is itself a complete
  `Specification`.
- The referenced specification remains the source of its own identifying and
  descriptive information, including `Type`, `Number`, `SubNumber`,
  `IssueDate` and `Title`.
- The higher-level specification does not duplicate the content of the
  referenced specification.
- The role of a specification as higher-level, standalone or referenced is
  determined by its position in the hierarchy.
- The role is not maintained as a separate property on the `Specification`.
- `Specification.ReferencedSpecifications` expresses a reference relationship.
  It does not express containment.
- Component containment is maintained separately through
  `ComponentMaster.SubComponents`.
- An application-specific deviation from a referenced specification is
  maintained separately through `SpecificationCustomizations`. The referenced
  specification itself remains unchanged.

## JSON Example

See `componentMaster-with-specificationHierarchy.json`.

## Validation Status

This example is aligned with the entity relationship model, in which a
`Specification` can reference other `Specification` objects through
`Specification.ReferencedSpecifications`.

The self-reference and its reference semantics are supported by ADR 0005.

At the documented state of this example,
`Specification.ReferencedSpecifications` is not yet present in the released
generic JSON schema. The example therefore cannot yet be validated against the
released generic schema version.

Validation against the generic JSON schema should be performed after
`Specification.ReferencedSpecifications` has been added to the released schema.

This example must not be described as schema-conformant until that validation
has been completed successfully.

## Related Examples

- **Component Master Hierarchy**  
  Use this example for a recursive component tree based on the containment
  relationship `ComponentMaster.SubComponents`.

- **Material with Specification Customization**  
  Use this example when a requirement from a referenced specification remains
  identifiable but an application-specific deviation must be documented
  separately.

- **Simple Material Definition**  
  Use this example for a basic material-related `ComponentMaster` with
  specification references but without a specification hierarchy.

- **Material with Stack**  
  Use this example when the primary concern is a layered material structure
  rather than relationships between specifications.

## Architectural References

- Entity: `Specification`
- Specifications assigned to a component:
  `ComponentMaster.Specifications`
- Hierarchy property:
  `Specification.ReferencedSpecifications`
- Pattern: self-reference
- Structure: recursive specification reference hierarchy
- Relationship type: reference
- Role of an object: determined by its position in the specification hierarchy
- Contrasting relationship:
  `ComponentMaster.SubComponents` as a containment relationship
- Related customization:
  `ComponentMaster.SpecificationCustomizations`
- ADR 0005: Hierarchies are modelled through self-reference, with containment
  for components and references for specifications
- ADR 0006: Norm information is aggregated into `Specification`, with further
  applicable regulations represented through `ReferencedSpecifications`
- ADR 0008: The abbreviated material designation is maintained in
  `MaterialClass`, not in `Specification.Title`
