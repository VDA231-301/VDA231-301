# Metal Material with Characteristic Requirements

## Status

Schema-oriented example for VDA 231-301 generic schema v3.0.0.
The values and the OEM material requirement specification used in this example
are illustrative and do not reproduce a normative material standard.

## Business Scenario

An OEM uses a cold-rolled steel sheet material. The material is identified by
its material class and by an OEM material identifier. A specification reference
alone does not fully describe the requirement profile that applies to this
material definition.

The specification therefore carries machine-readable characteristic
requirements for:

- a permitted yield-strength range
- a nominal Vickers hardness with tolerances
- a qualitative surface condition selected from a controlled list

These entries are requirements. They are neither measured test results nor
application-specific deviations from another requirement.

## Objective

This example demonstrates how quantitative and qualitative requirements imposed
by a material specification are represented in
`Specification.CharacteristicRequirements`.

The example shows the three value patterns:

- `Range`
- `NumberWithTolerance`
- `List`

## When to Use This Example

Use this pattern when:

- a specification reference alone is not sufficient to describe the applicable
  material requirement profile
- additional target values, permitted ranges or qualitative selections must be
  machine-readable
- the requirements belong to the specification itself
- the data may later be used to derive a test plan or compare requirements with
  reported results

Do not use this pattern for:

- measured values or test results
- a component-specific deviation from a referenced specification
- a material supplier product or production batch
- characteristics that are only part of the standardized material designation

## Learning Goals

After reviewing the example, the reader should understand:

- where characteristic requirements are placed in a `Specification`
- how `Range`, `NumberWithTolerance` and `List` values are structured
- the difference between a requirement and a reported result
- the difference between a characteristic requirement and a specification
  customization
- why the material identity remains on `ComponentMaster`

## Relevant Entities

### ComponentMaster

Represents the reusable metal material definition. It contains the material
identity, material class, version and associated specification.

### Specification

Represents the requirement specification applicable to the material. The
machine-readable requirement profile is carried in
`CharacteristicRequirements`.

### CharacteristicRequirement

Represents a required value, a permitted value range or a qualitative selection
for a material or component characteristic.

## Modelling Decisions

### Material identity

`MaterialClass` contains the abbreviated material designation. It is not
repeated as a characteristic requirement.

### Requirement profile

The requirements are nested directly in the specification because they explain
what the specification requires for this material definition.

### No test results

The values in this example are target requirements. A measured yield strength,
hardness value or assessment would be represented in the test structures, not
in `Specification.CharacteristicRequirements`.

### No specification customization

The example does not change an original requirement for a specific application.
If an original and a deviating requirement must be retained together, use
`ComponentMaster.SpecificationCustomizations` instead.

### Illustrative values

`OEM01 M-STEEL-001`, the identifier `PEW000000001`, and all requirement values
are synthetic example data. They must not be interpreted as requirements from
an actual OEM, EN, ISO or VDA standard.

## JSON Walkthrough

- `ComponentMaster.MaterialClass`: identifies the metal grade designation used
  by this illustrative material definition.
- `ComponentMaster.Specifications[]`: links the applicable specification.
- `Specification.CharacteristicRequirements[]`: holds the structured
  requirement profile.
- `Yield strength`: uses `ValueType: Range` with `minValue` and `maxValue`.
- `Vickers hardness`: uses `ValueType: NumberWithTolerance` with a nominal value
  and lower and upper tolerances.
- `Surface condition`: uses `ValueType: List` for a controlled qualitative
  selection.

## Validation Status

The JSON structure was checked against the field definitions inspected in
VDA 231-301 generic schema v3.0.0. Before merge, run the repository's
regular validation against the exact schema file used by the target branch.

## Files

- `material-with-characteristic-requirements-metal.json`
- `README.md`

## Related Examples

- Material with Specification Customization
- Simple Material Definition
- VDA 270 Odor Test - Getting Started

## Architectural References

- `ComponentMaster.Specifications`
- `Specification.CharacteristicRequirements`
- `Generic.CharacteristicRequirement`
- `Generic.InformationPoint`
- ADR 0007: material characteristics are read out into typed characteristic
  requirements via a defined classification logic
