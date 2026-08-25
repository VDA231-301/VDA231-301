# Material with Specification Customization

## Business Scenario

An OEM uses a material that is generally covered by a referenced material
requirement specification. For a specific application, the OEM needs a deviation
from one of the requirements in that specification.

In this example, the referenced OEM requirement specification contains an odor
rating requirement based on VDA 270. The original requirement limits the odor
rating to 4.0. For this specific application, the OEM accepts an odor rating up
to 4.5. The referenced specification itself remains unchanged; the deviation is
documented separately.

## Objective

This example demonstrates how an OEM-specific deviation from a referenced
specification is documented using `SpecificationCustomizations` and
`DeviatingProperty`, without changing the referenced specification itself.

## Learning Goals

After reviewing this example, the reader should understand:

- how a specification is referenced
- how an OEM-specific deviation is documented via `SpecificationCustomizations`
- how a changed requirement value is expressed via `DeviatingProperty`
- how the original and the deviating value are captured

## Relevant Entities

### ComponentMaster

The component being described, including its referenced specification and the
associated customization.

### Specification

The referenced specification that contains the original requirement.

### SpecificationCustomization

An OEM-specific customization of a referenced specification. In this example the
`CustomizationType` is `SpecificationDeviation`.

### DeviatingProperty

A property whose required value deviates from the original specification,
capturing both the original and the deviating value.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.Version
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.Specifications
- ComponentMaster.SpecificationCustomizations
- SpecificationCustomization.CustomizationType
- SpecificationCustomization.Description
- SpecificationCustomization.Specification
- SpecificationCustomization.DeviatingProperties
- DeviatingProperty.Property
- DeviatingProperty.OriginalValue
- DeviatingProperty.DeviatingValue

## Modelling Decisions

The referenced specification remains valid and unchanged. The OEM-specific
change is documented separately as a `SpecificationCustomization` of type
`SpecificationDeviation`. This keeps the relationship between the original
requirement and the OEM deviation traceable.

The deviation concerns a test-based requirement value (the odor rating based on
VDA 270), not the material definition itself. The property name
`VDA270_OdorRating` makes the underlying test method visible, while the
association to the referenced specification is expressed through the
customization's `Specification`.

The `Version` attribute represents the version / change status of the component
definition (for example the drawing status, known as ZGS at Mercedes-Benz) and
should always be provided when describing a component.

This example intentionally documents only one deviating property in order to
keep the mechanism easy to understand.

## JSON Example

See `componentMaster-with-specificationCustomization.json`.

## Validation Status

Aligned with the generic schema v3.0.0, in which `SpecificationCustomizations`,
`SpecificationCustomization` and `DeviatingProperty` are defined. Validation
against the released schema version should be performed before productive use.

## Related Examples

- Simple Material Definition
- Material with Stack
- Color Definition

## Architectural References

- Property: `ComponentMaster.SpecificationCustomizations`
- Entity: `SpecificationCustomization` (CustomizationType, Specification, DeviatingProperties)
- Entity: `DeviatingProperty` (Property, OriginalValue, DeviatingValue)
