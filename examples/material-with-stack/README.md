# Material with Stack

## Business Scenario

An automotive interior component consists of multiple material layers, for
example a plastic substrate with a primer and a paint layer on top. The supplier
needs to document this layered structure in a transparent and machine-readable
way so that the OEM can understand the composition, the order of the layers and
their mass and thickness.

## Objective

This example demonstrates how a layered material structure is represented using
the `Stack` property of a `ComponentMaster`.

## Learning Goals

After reviewing this example, the reader should understand:

- how a layered material structure is represented using `Stack`
- how the columns of the stack are defined via `ArraySpec`
- how the layer values are provided via `ArrayValue` in the defined column order
- how mass and thickness are documented per layer

## Relevant Entities

### ComponentMaster

The component being described, including its layered material structure.

### Stack

An `InformationSet` describing the layered structure of the material as a table.
`ArraySpec` defines the columns and `ArrayValue` contains one row per layer.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.Version
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.Stack
- Stack.ArraySpec
- Stack.ArrayValue

## Modelling Decisions

The `Stack` is represented as an `InformationSet` with a fixed column structure
defined by the generic schema:

1. `LayerNumber`
2. `Material`
3. `Mass` (with a unit, here grams)
4. `Thickness` (with a unit, here millimetres)

`ArraySpec` defines these columns, and each entry in `ArrayValue` provides the
values of one layer in exactly this order. In this example the layers are
ordered from the substrate (layer 1) to the top coat (layer 3).

The `Version` attribute represents the version / change status of the component
definition (for example the drawing status, known as ZGS at Mercedes-Benz) and
should always be provided when describing a component.

The mass and thickness values are illustrative and only intended to demonstrate
the mechanism, not to describe a specific real product.

## JSON Example

See `componentMaster-with-stack.json`.

## Validation Status

Aligned with the generic schema v3.0.0, in which the `Stack` structure with
`ArraySpec` and `ArrayValue` (LayerNumber, Material, Mass, Thickness) is defined.
Validation against the released schema version should be performed before
productive use.

## Related Examples

- Simple Material Definition
- Color Definition
- Material with Specification Customization

## Architectural References

- Property: `ComponentMaster.Stack`
- Structure: `InformationSet` with `ArraySpec` and `ArrayValue`
- Columns: LayerNumber, Material, Mass, Thickness
