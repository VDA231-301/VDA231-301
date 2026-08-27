# VDA 270 Odor Test - Getting Started


## Business Scenario

An interior trim component has to fulfil an odor requirement according to
VDA 270. A laboratory determines the odor characteristics of the material, and
the result is exchanged in a structured, machine-readable form instead of a PDF
laboratory report.

This getting started example shows the essence of a test result in the
VDA 231-301 data model: a requirement and the corresponding reported result,
embedded in a minimal but complete `TestingProject`.

## Objective

This example demonstrates, in the simplest possible form, how a test requirement
(`TargetProperties`) and a test result (`ReportedProperties`) are represented for
an odor test according to VDA 270.

## Background: the VDA 270 odor scale

VDA 270 rates the odor of trim materials on a scale from 1 to 6, with half steps
allowed, where a lower value is better:

- 1 - not perceptible
- 2 - perceptible, not disturbing
- 3 - clearly perceptible, not disturbing
- 4 - disturbing
- 5 - strongly disturbing
- 6 - not acceptable

In this example the requirement is a maximum odor rating of 3.5, and the reported
result is 3.0, so the component passes. All values are illustrative.

## Structure

The example is a `TestingProject` containing:

- one `ComponentMaster` (the tested interior trim component)
- one `Topic` of type `TestSeries` (the odor test), which references the
  component via `ComponentMasterID` and carries:
  - the applied standard via `Specification` (VDA 270)
  - the test condition via `Conditions` (test variant)
  - the requirement via `TargetProperties` (odor rating max 3.5)
  - the result via `ReportedProperties` (odor rating 3.0)
  - the overall verdict via `Assessment` (Passed)

## Relevant Entities

- `TestingProject` - the transmission root
- `ComponentMaster` - the tested component
- `Topic` (TestSeries) - the odor test
- `Specification` - the applied standard (VDA 270)

## Relevant Attributes

- Topic.TestType
- Topic.ComponentMasterID
- Topic.Specification
- Topic.Conditions
- Topic.TargetProperties (requirement)
- Topic.ReportedProperties (result)
- Topic.Assessment

## Modelling Decisions

The requirement is expressed as a `TargetProperties` information set with an
`OdorRating` property of value type `Range` and a maximum value of 3.5, which
represents "at most 3.5".

The result is expressed as a `ReportedProperties` consolidated characteristic
value with an `OdorRating` of 3.0. In this getting started example the result is
given directly, without individual assessor ratings or laboratory details. The
complete version of this example (`vda270-odor-complete`) adds the laboratory,
the panel and the individual assessor ratings.

The odor rating is a dimensionless grade, so no unit is used.

## JSON Example

See `testingProject-vda270-getting-started.json`.

## Validation Status

Aligned with the generic schema v3.0.0 (root type `TestingProject`, `Topic`,
`TargetProperties`, `ReportedProperties`). Validation against the released schema
version should be performed before productive use.

## Related Examples

- VDA 270 Odor Test - Complete
- Material with Specification Customization

## Architectural References

- Root: `TestingProject`
- Entity: `Topic` (TestSeries) with `TargetProperties` and `ReportedProperties`
- Requirement vs. result: `TargetProperties` vs. `ReportedProperties`
