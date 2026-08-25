# Component Master Hierarchy

## Business Scenario

Components are not always standalone parts. A component can be the top node of a
part tree (for example a complete door module), and at the same time other
components can be parts of it (for example a door trim panel and a loudspeaker
grille inside that door module).

The same component definition can therefore play two roles:

- it can be the top-level component of a structure, or
- it can be a subcomponent within a larger component.

This example shows how such a component hierarchy is represented in the data
model.

## Objective

This example demonstrates how a component hierarchy is modelled using
`ComponentMaster.SubComponents`, where each subcomponent is itself a
`ComponentMaster`.

## Learning Goals

After reviewing this example, the reader should understand:

- that a `ComponentMaster` can be either a top-level component or a subcomponent
- how a component tree is built using the `SubComponents` property
- that a subcomponent has exactly the same structure as a top-level component
- that the role (top node vs. subcomponent) results from the position in the
  tree, not from a different entity type

## Relevant Entities

### ComponentMaster

The component being described. Through its `SubComponents` property, a
`ComponentMaster` can contain further `ComponentMaster` objects, forming a tree.

> Note: `SubComponents` is a list of `ComponentMaster` objects. This is a
> self-reference: the same entity type is used for the parent component and for
> each subcomponent. The role of a component (top node or subcomponent) is not a
> property of the component itself; it results from where the component sits in
> the tree.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.Version
- ComponentMaster.SupplierPartNumber
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.SubComponents

## Modelling Decisions

A component hierarchy is modelled as a tree of `ComponentMaster` objects. The
top-level component is a `ComponentMaster`, and each of its subcomponents is
again a `ComponentMaster` placed in the parent's `SubComponents` list.

This is a self-referencing (recursive) structure. It allows an arbitrary depth
of nesting and uses the same set of attributes at every level. There is no
separate "subcomponent" entity; a subcomponent is simply a `ComponentMaster`
that is contained in another `ComponentMaster`.

This relationship is a containment relationship: the parent component contains
its subcomponents. This matches the logic of a part tree or bill of materials,
and it corresponds to the CAD assembly structure that can also be referenced via
`NGIDPath`.

In this example the top-level `Door Module` does not carry material information
itself, because it represents an assembly. Its subcomponents (`Door Trim Panel`,
`Loudspeaker Grille`) carry the material information.

## JSON Example

See `componentMaster-with-subComponents.json`.

## Validation Status

Aligned with the generic schema v3.0.0, in which `ComponentMaster.SubComponents`
is defined as a list of `ComponentMaster`. Validation against the released schema
version should be performed before productive use.

## Related Examples

- Simple Material Definition
- NGID Identified Component
- Component Instance Traceability

## Architectural References

- Property: `ComponentMaster.SubComponents`
- Pattern: self-reference (recursive component tree)
- Relationship type: containment (parent contains subcomponents)
