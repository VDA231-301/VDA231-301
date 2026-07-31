# Material with Stack

## Business Scenario

An automotive interior component consists of multiple material layers.

The supplier needs to document the layered material structure in a transparent and machine-readable way.

The receiving OEM shall be able to understand the composition of the component and identify the materials used in each layer.

## Objective

This example demonstrates how a layered material structure can be represented using the Stack entity.

## Learning Goals

After reviewing this example, the reader should understand:

- how layered structures are represented
- how materials are assigned to layers
- how mass and thickness can be documented per layer
- how the Stack entity is used

## Relevant Entities

### ComponentMaster

The component being described.

### Stack

The layered material structure.

## Relevant Attributes

This example focuses on:

- ComponentMaster.MaterialName
- ComponentMaster.Stack
- Stack.LayerNumber
- Stack.Material
- Stack.Mass
- Stack.Thickness

## Modelling Decisions

This example describes a simplified three-layer structure.

The focus is on demonstrating the Stack mechanism rather than accurately representing a specific product.

## JSON Example

See componentMaster-with-stack.json

## Validation Status

Draft example based on the current generic schema.

## Related Examples

- Simple Material Definition
- Material with Specification Customization
- Multiple Source Material

## Architectural References

To be completed.
