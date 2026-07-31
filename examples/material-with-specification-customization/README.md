# Material with Specification Customization

## Business Scenario

An OEM uses a material that is generally covered by a material specification.

However, the OEM requires a deviation from the original specification, introduces an additional requirement, or makes an optional requirement mandatory.

The receiving supplier and testing laboratory need to understand both the original specification and the associated customization.

## Objective

This example demonstrates how OEM-specific deviations, additional requirements, or mandatory normative options can be represented using SpecificationCustomizations.

## Learning Goals

After reviewing this example, the reader should understand:

- how specifications are referenced
- how OEM-specific requirements are represented
- how deviations from an existing specification are documented
- how SpecificationCustomizations are linked to a ComponentMaster

## Relevant Entities

### ComponentMaster

The material or component being described.

### Specification

The original specification applicable to the component.

### SpecificationCustomization

An OEM-specific customization of the referenced specification.

### DeviatingProperty

A property that differs from the original specification.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Specifications
- ComponentMaster.SpecificationCustomizations
- SpecificationCustomization.CustomizationType
- SpecificationCustomization.Specification
- SpecificationCustomization.DeviatingProperties
- DeviatingProperty.Property
- DeviatingProperty.OriginalValue
- DeviatingProperty.DeviatingValue

## Modelling Decisions

This example assumes that the referenced specification remains valid.

Only specific requirements are modified or added by the OEM.

The example does not replace the original specification but documents the customization separately.

## JSON Example

See componentMaster-with-specificationCustomization.json

## Validation Status

Draft example based on the current generic schema.

## Related Examples

- Simple Material Definition
- Multiple Source Material

## Architectural References

To be completed.
