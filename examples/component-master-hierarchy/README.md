# Component Master Hierarchy

## Business Scenario

Components are not always standalone parts.

A component can be the top-level node of a part tree, for example a complete
door module. Other components, such as a door trim panel or a loudspeaker
grille, can be contained as parts of that component.

The same component structure can therefore appear in two different positions:

- as the top-level component of a component tree
- as a subcomponent within a larger component

This example shows how a component hierarchy is represented in the
VDA 231-301 data model.

## Objective

This example demonstrates how a component hierarchy is modelled using
`ComponentMaster.SubComponents`, where each subcomponent is itself represented
as a `ComponentMaster`.

## When to Use This Example

Use this example when:

- a component consists of other components
- a part tree or bill-of-material-like structure has to be represented
- the same component structure is required at every hierarchy level
- more than one level of component nesting may be needed
- the relationship between a component and its subcomponents is a containment
  relationship

Do not use this example to represent a hierarchy of specifications.

A specification hierarchy uses
`Specification.ReferencedSpecifications`. That relationship is a reference
relationship rather than a containment relationship and is demonstrated in the
**Specification Hierarchy** example.

Do not introduce a separate entity type such as `SubComponentMaster`.
A subcomponent is represented as a regular `ComponentMaster` contained in the
`SubComponents` list of its parent.

## Learning Goals

After reviewing this example, the reader should understand:

- that a `ComponentMaster` can appear as either a top-level component or a
  subcomponent
- how a component tree is built using
  `ComponentMaster.SubComponents`
- that every subcomponent has the same structure as a top-level
  `ComponentMaster`
- that the role of a component results from its position in the tree
- that the component hierarchy is a recursive structure
- that the relationship between a parent component and its subcomponents is a
  containment relationship
- how component containment differs from specification referencing

## Relevant Entities

### ComponentMaster

A `ComponentMaster` represents a component definition.

Through its `SubComponents` property, a `ComponentMaster` can contain further
`ComponentMaster` objects and thereby form a recursive component tree.

The same entity type is used for:

- the top-level component
- every directly contained subcomponent
- every subcomponent contained at a deeper hierarchy level

The role of a component as either a top-level component or a subcomponent is
not stored as a separate attribute. The role results from the position of the
`ComponentMaster` within the component tree.

> **Note:** `SubComponents` is a list of `ComponentMaster` objects. This is a
> self-reference because the same entity type is used for the parent component
> and for every contained subcomponent.

## Relevant Attributes

This example focuses on the following attributes:

- `ComponentMaster.Designation`
- `ComponentMaster.Version`
- `ComponentMaster.SupplierPartNumber`
- `ComponentMaster.MaterialName`
- `ComponentMaster.MaterialIdentifiers`
- `ComponentMaster.SubComponents`

## Modelling Decisions

A component hierarchy is modelled as a recursive tree of `ComponentMaster`
objects.

The top-level component is represented as a `ComponentMaster`. Each of its
subcomponents is represented as another `ComponentMaster` contained in the
parent's `SubComponents` list.

Because each subcomponent is again a `ComponentMaster`, it can contain its own
`SubComponents`. This allows component hierarchies with an arbitrary nesting
depth.

A separate entity type for subcomponents is not required. The same attributes
and structures are available at every hierarchy level.

The relationship between a parent component and its subcomponents is a
**containment relationship**:

- the parent component contains its subcomponents
- the subcomponents form part of the component structure represented by the
  parent
- the hierarchy corresponds to a part tree or bill-of-material-like structure

This containment relationship differs from the relationship used in a
specification hierarchy.

`Specification.ReferencedSpecifications` represents references to independent
and reusable specifications. By contrast,
`ComponentMaster.SubComponents` represents components contained within a
parent component.

In this example, the top-level door module does not carry material information
itself because it represents an assembly. Its subcomponents, such as the door
trim panel and the loudspeaker grille, carry the relevant material information.

This is a modelling decision of this example. It does not mean that a
top-level `ComponentMaster` is generally prohibited from carrying material
information.

The `Version` attribute represents the version or change status of each
component definition and should be provided for every `ComponentMaster` in the
Example Library, including both the top-level component and its subcomponents.

## Source of Truth and References

- The top-level component is represented by the outer
  `ComponentMaster`.
- The directly contained subcomponents are maintained in
  `ComponentMaster.SubComponents`.
- Each entry in `ComponentMaster.SubComponents` is itself a complete
  `ComponentMaster`.
- A contained `ComponentMaster` can maintain its own
  `SubComponents`, creating further hierarchy levels.
- The role of a component as a top-level component or a subcomponent is
  determined by its position in the tree.
- The role is not maintained as a separate property on the
  `ComponentMaster`.
- Component-specific information, such as `Designation`, `Version`,
  `SupplierPartNumber`, `MaterialName` and `MaterialIdentifiers`, is maintained
  on the `ComponentMaster` to which the information applies.
- Information belonging to a subcomponent is not duplicated on the parent
  component.
- `ComponentMaster.SubComponents` expresses containment and does not represent
  a reference to an independent specification.
- A CAD occurrence reference, if required, is maintained separately through
  `ComponentMaster.NGIDPath`.

## JSON Example

See `componentMaster-with-subComponents.json`.

## Validation Status

This example is intended to align with the generic schema v3.0.0, in which
`ComponentMaster.SubComponents` is defined as a list of
`ComponentMaster` objects.

Validation against the referenced released schema version should be performed
before productive use.

## Related Examples

- **Simple Material Definition**  
  Use this example for the basic representation of a standalone material-related
  `ComponentMaster` without a component hierarchy.

- **Specification Hierarchy**  
  Use this example when a higher-level specification references independent
  and reusable specifications through
  `Specification.ReferencedSpecifications`.

- **NGID Identified Component**  
  Use this example when a component must be linked to its occurrence in a
  source CAD assembly through `ComponentMaster.NGIDPath`.

- **Component Instance Traceability**  
  Use this example when individually produced parts and their production
  traceability information must be represented as `ComponentInstance`
  objects.

## Architectural References

- Entity: `ComponentMaster`
- Hierarchy property: `ComponentMaster.SubComponents`
- Pattern: self-reference
- Structure: recursive component tree
- Relationship type: containment
- Role of an object: determined by its position in the component tree
- Contrasting relationship:
  `Specification.ReferencedSpecifications` as a reference relationship
- Related CAD reference: `ComponentMaster.NGIDPath`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0005: Hierarchies are modelled via self-reference, with containment for
  components and references for specifications
