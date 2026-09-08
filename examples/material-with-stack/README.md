# Material with Stack

## Business Scenario

An automotive interior component consists of several material layers.

A typical layered structure can include:

- a plastic substrate
- a primer
- a paint or top-coat layer

The supplier needs to document this layered structure in a transparent and
machine-readable form.

The representation must show:

- which layers belong to the structure
- in which order the layers are arranged
- which material is assigned to each layer
- which mass is assigned to each layer
- which thickness is assigned to each layer

## Objective

This example demonstrates how a layered material structure is represented using
`ComponentMaster.Stack`.

The stack is represented as a table-like `InformationSet`. Its columns are
defined through `Stack.ArraySpec`, and its layer values are provided through
`Stack.ArrayValue`.

## When to Use This Example

Use this example when:

- a component or material consists of several layers
- the order of the layers must be represented explicitly
- the material of each layer must be documented
- mass or thickness must be documented for individual layers
- a layered structure must be exchanged in a machine-readable form

Typical applications include:

- coated substrates
- painted components
- multilayer films
- laminated structures
- material stacks containing primers, adhesives or functional layers

Do not use this example when:

- only one homogeneous material has to be described
- the primary concern is a component hierarchy
- the primary concern is a specification hierarchy
- a referenced specification contains an application-specific deviation

Use the **Simple Material Definition** example for a basic material description
without a layered structure.

Use the **Component Master Hierarchy** example when a component contains other
components rather than material layers.

Use the **Material with Specification Customization** example when an
application-specific deviation from a referenced specification must be
documented.

## Learning Goals

After reviewing this example, the reader should understand:

- how a layered material structure is represented through
  `ComponentMaster.Stack`
- how the stack columns are defined through `Stack.ArraySpec`
- how the values of each layer are provided through `Stack.ArrayValue`
- why the values in `Stack.ArrayValue` must follow the column order defined in
  `Stack.ArraySpec`
- how the material, mass and thickness of each layer are documented
- how the layer numbering is interpreted
- why layer 1 represents the substrate or bottom layer
- how special structures without an unambiguous substrate must be documented

## Relevant Entities

### ComponentMaster

The `ComponentMaster` represents the component or material-related object whose
layered structure is being described.

Its `Stack` property contains the structured description of the material
layers.

### Stack

The `Stack` is an `InformationSet` that represents the layered structure in a
table-like form.

`Stack.ArraySpec` defines the meaning and sequence of the columns.

`Stack.ArrayValue` contains the rows of the table, with one row for each layer.

> **Note:** The position of a value within an `ArrayValue` row is interpreted
> according to the column sequence defined in `ArraySpec`. The values must
> therefore remain in the defined order.

## Relevant Attributes

This example focuses on the following attributes:

- `ComponentMaster.Designation`
- `ComponentMaster.Version`
- `ComponentMaster.MaterialName`
- `ComponentMaster.MaterialIdentifiers`
- `ComponentMaster.Stack`
- `Stack.ArraySpec`
- `Stack.ArrayValue`

The stack structure uses the following columns:

- `LayerNumber`
- `Material`
- `Mass`
- `Thickness`

## Modelling Decisions

The layered material structure is represented through
`ComponentMaster.Stack`.

The `Stack` uses an `InformationSet` with a fixed column structure.

`Stack.ArraySpec` defines the columns and their order:

1. `LayerNumber`
2. `Material`
3. `Mass`
4. `Thickness`

Each entry in `Stack.ArrayValue` represents one layer.

The values in each layer row must follow exactly the same order as the columns
defined in `Stack.ArraySpec`.

The layer numbering starts at the substrate or bottom of the material stack:

- layer 1 is the substrate or bottom layer
- higher layer numbers proceed outward from the substrate
- the highest layer number represents the top or outer layer

In this example, the layers are ordered from the substrate to the top coat.

The layer order follows ADR 0003 and must be applied consistently so that
different systems interpret the stack in the same direction.

For a typical coated component, the sequence can therefore be interpreted as:

1. substrate
2. primer or intermediate layer
3. paint or top-coat layer

The terms substrate, primer and top coat are illustrative. The actual material
and function of each layer are provided by the corresponding layer data.

In special cases, the structure may not have an unambiguous substrate or
bottom layer. Examples include:

- symmetric structures
- free-standing films
- coating-only stacks
- structures for which either orientation could reasonably be selected

In such cases, the selected orientation and the meaning of layer 1 must be
described in the stack's `Comment` so that the layer order remains
unambiguous.

Mass and thickness are documented separately for each layer.

A unit must be associated with a quantitative mass or thickness value so that
the value can be interpreted correctly. The mass and thickness values used in
this example are illustrative and do not represent a specific productive
component.

The stack represents material layers. It does not represent a hierarchy of
components.

A component tree is modelled separately through
`ComponentMaster.SubComponents`.

The `Version` attribute represents the version or change status of the
component definition and should always be provided when describing a component
in the Example Library.

## Source of Truth and References

- The layered structure is maintained in `ComponentMaster.Stack`.
- The definition and sequence of the stack columns are maintained in
  `Stack.ArraySpec`.
- The individual layer rows are maintained in `Stack.ArrayValue`.
- Each row in `Stack.ArrayValue` represents one layer.
- The position of each value in a layer row is determined by the corresponding
  position of the column definition in `Stack.ArraySpec`.
- `LayerNumber` defines the position of a layer within the material stack.
- Layer 1 represents the substrate or bottom layer.
- Higher layer numbers proceed outward toward the top or outer layer.
- The material assigned to a layer is maintained in the `Material` value of the
  corresponding layer row.
- The mass assigned to a layer is maintained in the `Mass` value of the
  corresponding layer row.
- The thickness assigned to a layer is maintained in the `Thickness` value of
  the corresponding layer row.
- The selected orientation of a special or symmetric structure is maintained
  in the stack's `Comment`.
- Layer-specific information is not duplicated as separate properties on the
  `ComponentMaster`.
- A component hierarchy, if required, is maintained separately through
  `ComponentMaster.SubComponents`.

## JSON Example

See `componentMaster-with-stack.json`.

## Validation Status

This example is intended to align with the generic schema v3.0.0, including the
`Stack` structure with `ArraySpec` and `ArrayValue`.

The documented stack columns are:

- `LayerNumber`
- `Material`
- `Mass`
- `Thickness`

The layer orientation follows ADR 0003:

- layer 1 represents the substrate or bottom layer
- higher layer numbers proceed toward the top or outer layer

Validation against the referenced released schema version should be performed
before productive use.

## Related Examples

- **Simple Material Definition**  
  Use this example for a basic material-related representation without a
  layered material structure.

- **Component Master Hierarchy**  
  Use this example when the structure consists of components contained within
  other components rather than material layers.

- **Material with Specification Customization**  
  Use this example when an application-specific requirement deviates from a
  referenced specification.

- **Color Definition**  
  Use this example when approved colors and the actual color of a produced part
  have to be represented.

## Architectural References

- Entity: `ComponentMaster`
- Layered structure: `ComponentMaster.Stack`
- Stack structure: `InformationSet`
- Column definition: `Stack.ArraySpec`
- Layer rows: `Stack.ArrayValue`
- Stack columns: `LayerNumber`, `Material`, `Mass` and `Thickness`
- Layer orientation: layer 1 is the substrate or bottom layer
- Special-case documentation: stack orientation and the meaning of layer 1 in
  `Stack.Comment`
- Contrasting structure: `ComponentMaster.SubComponents` for a component
  hierarchy
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0003: stack layer ordering starts at the substrate, with layer 1 as the
  bottom layer
