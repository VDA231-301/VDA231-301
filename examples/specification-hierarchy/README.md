# Specification Hierarchy

## Business Scenario

Specifications are not always standalone documents. A specification can stand on
its own (for example a single test specification such as VDA 270), and at the
same time it can be one of several sub-specifications referenced by a higher-level
specification.

A typical example is an OEM product requirement specification for an interior
trim component. This product specification does not repeat all requirements
itself; instead it references several other specifications, such as test
specifications (VDA 270, VDA 278) and a material specification.

This example shows how such a specification hierarchy is represented in the data
model.

## Objective

This example demonstrates how a specification hierarchy is modelled using a
specification that references other specifications via `ReferencedSpecifications`.

## Learning Goals

After reviewing this example, the reader should understand:

- that a specification can stand alone or be referenced by a higher-level
  specification
- how a higher-level specification references sub-specifications
- that a referenced specification has exactly the same structure as a
  standalone specification
- the difference between referencing specifications and containing subcomponents

## Relevant Entities

### Specification

A specification (for example a product, test or material specification). Through
its `ReferencedSpecifications` property, a specification can reference further
specifications, forming a hierarchy.

> Note: `ReferencedSpecifications` is a list of `Specification` objects. This is
> a self-reference: the same entity type is used for the higher-level
> specification and for each referenced specification. Whether a specification is
> "standalone" or "referenced" is not a property of the specification itself; it
> results from where it appears in the hierarchy.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Specifications
- Specification.Type
- Specification.Number
- Specification.IssueDate
- Specification.Title
- Specification.ReferencedSpecifications

## Modelling Decisions

A specification hierarchy is modelled as a specification that references other
specifications via `ReferencedSpecifications`. The higher-level specification
(here an OEM product requirement specification) references several
sub-specifications (two test specifications and one material specification).

This is a self-referencing (recursive) structure, similar to the component
hierarchy. However, there is an important semantic difference:

- A component hierarchy (`ComponentMaster.SubComponents`) is a **containment**
  relationship: a parent component contains its subcomponents.
- A specification hierarchy (`Specification.ReferencedSpecifications`) is a
  **reference** relationship: a higher-level specification points to other
  specifications that exist in their own right and are typically reused by many
  specifications and components.

This is why the same test specification (for example VDA 270) can be referenced
by many different product specifications without being duplicated.

## JSON Example

See `componentMaster-with-specificationHierarchy.json`.

## Validation Status

Based on the entity relationship model (ERM), in which a specification can
reference other specifications via `Specification.ReferencedSpecifications`
(shown as a self-reference in the ERM).

Note: The `ReferencedSpecifications` property is defined in the ERM but is not
yet present in the released generic JSON schema. The schema needs to be updated
to add `Specification.ReferencedSpecifications` (a list of `Specification`). This
example already uses the confirmed property name. Validation against the generic
schema should be performed once the schema has been updated accordingly.

## Related Examples

- Material with Specification Customization
- Component Master Hierarchy
- Simple Material Definition

## Architectural References

- Property: `Specification.ReferencedSpecifications`
- Pattern: self-reference (recursive specification hierarchy)
- Relationship type: reference (a higher-level specification references others)
- Contrast: `ComponentMaster.SubComponents` is a containment relationship
