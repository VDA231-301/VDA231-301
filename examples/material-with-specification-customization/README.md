# Material with Specification Customization

## Status

Schema-oriented example.

This example is intended to align with the released VDA 231-301 generic schema
v3.0.0. Validation against the referenced schema version should be performed
before productive use.

## Business Scenario

An OEM uses a material that is generally covered by a referenced material
requirement specification.

For a specific application, the OEM needs to document a requirement that
deviates from the corresponding requirement in the referenced specification.

In this example, the referenced OEM requirement specification contains an odor
rating requirement based on VDA 270. The original requirement limits the odor
rating to 4.0. For the specific application represented by this example, the OEM
accepts an odor rating up to 4.5.

The referenced specification remains unchanged. The application-specific
deviation is documented separately so that the original requirement and the
deviating requirement remain traceable.

## Objective

This example demonstrates how an application-specific deviation from a
referenced specification is documented through
`ComponentMaster.SpecificationCustomizations` without changing the referenced
specification itself.

The example also demonstrates how the original requirement value and the
deviating requirement value are maintained together in the customization.

## When to Use This Example

Use this example when:

- a referenced specification remains valid and unchanged
- an application-specific requirement differs from the requirement in the
  referenced specification
- the relationship between the original and the deviating requirement must
  remain explicit and traceable
- the deviation applies only in a defined application context
- the deviation may be more restrictive or less restrictive than the original
  requirement

Do not use this example when:

- the referenced specification itself has been revised
- no application-specific deviation exists
- only a requirement from a specification has to be represented
- a complete test execution and its measured results have to be represented
- the primary concern is a hierarchy of specifications

Use the **VDA 270 Odor Test - Getting Started** example when a test requirement,
a reported result and an assessment have to be represented in a minimal test
project.

Use the **VDA 270 Odor Test - Complete** example when the complete test context,
including individual assessor grades and the consolidated result, has to be
represented.

Use the **Specification Hierarchy** example when the primary concern is the
relationship between a higher-level specification and other independent,
reusable specifications.

## Learning Goals

After reviewing this example, the reader should understand:

- how a specification is referenced by a `ComponentMaster`
- how an application-specific deviation is documented separately through
  `ComponentMaster.SpecificationCustomizations`
- how the customization identifies the specification to which it applies
- how the property affected by the deviation is identified
- how the original and the deviating requirement values are represented
- why the referenced specification remains unchanged
- why a deviation must retain an explicit relationship to the original
  requirement
- how specification customization differs from a test result

## Relevant Entities

### ComponentMaster

The `ComponentMaster` represents the component or material-related object for
which the specification and the application-specific customization apply.

The referenced specifications are maintained in
`ComponentMaster.Specifications`.

The application-specific customizations are maintained separately in
`ComponentMaster.SpecificationCustomizations`.

### Specification

The `Specification` represents the referenced requirement specification that
contains the original requirement.

The referenced `Specification` remains unchanged when an application-specific
deviation is added.

### SpecificationCustomization

A `SpecificationCustomization` represents an application-specific
customization of a referenced specification.

In this example, the customization type is `SpecificationDeviation`.

The customization identifies the specification to which it applies and contains
the properties whose requirements deviate from the referenced specification.

### DeviatingProperty

A `DeviatingProperty` represents a property for which the application-specific
requirement differs from the original requirement in the referenced
specification.

It maintains both the original requirement value and the deviating requirement
value so that the relationship remains traceable.

## Relevant Attributes

This example focuses on the following attributes:

- `ComponentMaster.Designation`
- `ComponentMaster.Version`
- `ComponentMaster.MaterialName`
- `ComponentMaster.MaterialIdentifiers`
- `ComponentMaster.Specifications`
- `ComponentMaster.SpecificationCustomizations`
- `SpecificationCustomization.CustomizationType`
- `SpecificationCustomization.Description`
- `SpecificationCustomization.Specification`
- `SpecificationCustomization.DeviatingProperties`
- `DeviatingProperty.Property`
- `DeviatingProperty.OriginalValue`
- `DeviatingProperty.DeviatingValue`

## Modelling Decisions

The referenced specification remains valid and unchanged.

The application-specific requirement deviation is documented separately through
a `SpecificationCustomization` with the customization type
`SpecificationDeviation`.

This separation preserves two different pieces of information:

- the original requirement defined by the referenced specification
- the application-specific requirement that deviates from the original
  requirement

The customization identifies the specification to which the deviation applies.
The affected property and both requirement values are maintained together in
the customization.

The example uses an odor rating requirement based on VDA 270:

- the original maximum odor rating is 4.0
- the application-specific maximum odor rating is 4.5

The value 4.5 is less restrictive than the original value 4.0. The modelling
pattern is not limited to less restrictive deviations. It can also be used when
the application-specific requirement is more restrictive than the original
requirement.

An application-specific deviation must not overwrite the original requirement
in the referenced specification.

The deviation must also not be represented only as an unrelated additional
requirement if doing so would lose the explicit relationship between the
original and the deviating requirement.

ADR 0007 provides the broader logic for classifying material characteristics
and reading them into typed requirement structures. Within that logic, an
application-specific deviation is represented separately when the explicit
relationship between the original and deviating requirement has to be retained.

The deviation concerns a test-based requirement value. It does not change the
material identity or the referenced specification itself.

The property name `VDA270_OdorRating` makes the underlying test method visible.
The relationship to the applicable specification is maintained through the
customization's `Specification` property.

The `Version` attribute represents the version or change status of the
component definition and should always be provided when describing a component
in the Example Library.

This example intentionally documents only one deviating property to keep the
customization mechanism easy to understand. A customization can contain more
than one deviating property where the schema permits this and the application
requires it.

## Source of Truth and References

- The component or material-related definition is maintained in the
  `ComponentMaster`.
- The version or change status of the component definition is maintained in
  `ComponentMaster.Version`.
- The referenced specifications are maintained in
  `ComponentMaster.Specifications`.
- The original requirement remains part of the referenced `Specification`.
- The referenced `Specification` is the source of the original requirement and
  is not modified by the application-specific deviation.
- The application-specific customization is maintained separately in
  `ComponentMaster.SpecificationCustomizations`.
- The customization identifies the specification to which the deviation
  applies through `SpecificationCustomization.Specification`.
- The affected property is identified through
  `DeviatingProperty.Property`.
- The original requirement value is maintained in
  `DeviatingProperty.OriginalValue`.
- The application-specific requirement value is maintained in
  `DeviatingProperty.DeviatingValue`.
- The deviating value does not replace or overwrite the original value in the
  referenced specification.
- A reported test result is not maintained in the specification customization.
  Test requirements and results are represented in the corresponding test
  project structures.

## JSON Example

See `componentMaster-with-specificationCustomization.json`.

## Validation Status

This example is intended to align with the generic schema v3.0.0, in which the
specification customization structure and the representation of deviating
properties are defined.

Validation against the referenced released schema version should be performed
before productive use.

The exact entity and property names used in the JSON example must remain aligned
with the released generic schema. If the released schema uses names that differ
from terminology used in an ADR, the released schema takes precedence for the
JSON structure and the README field paths.

## Related Examples

- **Simple Material Definition**  
  Use this example for a basic material-related `ComponentMaster` with a
  referenced specification but without an application-specific deviation.

- **Specification Hierarchy**  
  Use this example when a higher-level specification references other
  independent and reusable specifications through
  `Specification.ReferencedSpecifications`.

- **VDA 270 Odor Test - Getting Started**  
  Use this example when a test requirement, a reported result and an assessment
  have to be represented without the complete execution details.

- **VDA 270 Odor Test - Complete**  
  Use this example when individual assessor grades, their consolidation and the
  complete test context have to be represented.

- **Material with Stack**  
  Use this example when the primary concern is a layered material structure
  rather than an application-specific requirement deviation.

## Architectural References

- Entity: `ComponentMaster`
- Referenced specifications: `ComponentMaster.Specifications`
- Application-specific customizations:
  `ComponentMaster.SpecificationCustomizations`
- Customization entity: `SpecificationCustomization`
- Customization type: `SpecificationDeviation`
- Referenced specification:
  `SpecificationCustomization.Specification`
- Deviating properties:
  `SpecificationCustomization.DeviatingProperties`
- Affected property: `DeviatingProperty.Property`
- Original requirement value: `DeviatingProperty.OriginalValue`
- Application-specific requirement value:
  `DeviatingProperty.DeviatingValue`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0007: material characteristics are classified and read out into typed
  requirement structures; application-specific deviations retain the explicit
  relationship between the original and the deviating requirement
