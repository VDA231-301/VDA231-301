# Color Definition

## Business Scenario

An automotive supplier produces an interior trim component that is delivered
to an OEM in several color variants. The component design, the material and the
technical requirements are identical for all variants, but each variant has a
specific, agreed color.

Two distinct pieces of information have to be captured:

1. Which colors are **approved and available** for this component (relevant for
   engineering, PLM and the sampling scope, even before any part is produced).
2. Which color a **specific produced part** actually has (relevant for
   conformity checks, complaint handling and traceability).

## Objective

This example demonstrates how approved colors are defined once at the
`ComponentMaster` level using the `Color` entity, and how each produced
`ComponentInstance` references its actual color via `ColorID`.

## Learning Goals

After reviewing this example, the reader should understand:

- how a color is represented using the `Color` entity (Name, Code, CodeAuthority)
- how approved colors are defined at `ComponentMaster` level via `Colors`
- how a produced part references its actual color via `ComponentInstance.ColorID`
- why the color definition and the color assignment are modelled on two levels

## Relevant Entities

### ComponentMaster

The generic definition of the component. It holds the list of approved
`Colors` for this component, independent of any produced part.

### Color

An embedded entity describing a single color, including its name, its code and
the code authority (color system such as RAL, Pantone or NCS) the code refers to.

### ComponentInstance

A specific manufactured instance of the component. It documents the actual
color of the produced part by referencing one of the master's colors via
`ColorID`.

> Note: Within the `ComponentMaster`, the property that holds the instances is
> named `Instances` (plural, in the context of the master). Each entry in this
> list is an object of type `ComponentInstance`, indicated by its
> `"_type": "ComponentInstance"`. The same convention applies to `Colors`
> (property) with entries of type `Color`, and to `MaterialSources` (property)
> with entries of type `MaterialSource`.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.Version
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.Colors
- Color.Name
- Color.Code
- Color.CodeAuthority
- ComponentInstance.SerialNumber
- ComponentInstance.ProductionBatchNumber
- ComponentInstance.ColorID

## Modelling Decisions

The color information is intentionally modelled on **two levels**, and the
generic schema (v3.0.0) explicitly supports this:

- The `ComponentMaster` holds the **definition set** of approved colors in its
  `Colors` list. This represents which colors are released for the component and
  can be documented in a PLM context even before any part has been produced.
- The `ComponentInstance` documents the **actual color** of a produced part by
  referencing one of the master's colors via `ColorID`.

This separation keeps the `ComponentMaster` reusable across all color variants
and avoids duplicating color definitions. A produced part does not invent a new
color; it selects one of the colors that were defined and approved at master
level. This makes the color of every delivered part consistent with the
approved variant set.

The `Version` attribute represents the version / change status of the component
definition (for example the drawing status, known as ZGS) and
should always be provided when describing a component.

The color code is described together with its `CodeAuthority`, so that a code
such as a RAL number can be interpreted unambiguously. The color name is
provided as a human-readable label.

This example intentionally does not model color-dependent requirements. Its
only purpose is the unambiguous definition and identification of colors.

## JSON Example

See `componentMaster-with-color.json`.

## Validation Status

Aligned with the generic schema v3.0.0, in which `ComponentMaster.Colors` and
`ComponentInstance.ColorID` are defined. Validation against the released schema
version should be performed before productive use.

## Related Examples

- Simple Material Definition
- Component Instance Traceability
- Multiple Source Material

## Architectural References

- Entity: `Color` (Name, Code, CodeAuthority, AdditionalInformation)
- Definition set: `ComponentMaster.Colors`
- Reference: `ComponentInstance.ColorID`
- Analogous pattern: `ComponentMaster.MaterialSources` / `ComponentInstance.MaterialSourceID`


