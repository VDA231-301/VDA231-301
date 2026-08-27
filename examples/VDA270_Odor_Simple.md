# VDA 270 Odor Test - Getting Started

## Business Scenario

An interior trim component (a door trim panel) has to fulfil an odor requirement
according to VDA 270. A laboratory determines the odor characteristics of the
material, and the result is exchanged in a structured, machine-readable form
instead of a PDF laboratory report.

This getting started example shows the essence of a test result in the
VDA 231-301 data model: a requirement and the corresponding reported result,
embedded in a minimal but complete `TestingProject`.

## Objective

This example demonstrates, in the simplest possible form, how a test requirement
(`TargetProperties`) and a reported test result (`ReportedProperties`) are
represented for an odor test according to VDA 270.

## Background: the VDA 270 odor scale and evaluation

VDA 270 rates the odor of trim materials on a scale from 1 to 6, half grades
allowed, where a lower value is better (1 = not perceptible, 6 = not acceptable).

Per VDA 270 section 9, the reported odor characteristic is the **arithmetic mean
of the individual assessor grades, rounded to half grades**. Both the individual
grades and the mean are always given in the test report.

In this getting started example the requirement is a maximum odor grade of 3.5,
and the reported grade is 3.5, so the component passes. All values are
illustrative. The complete version of this example
(`vda270-odor-complete`) shows the underlying individual assessor grades and how
the reported grade is derived.

## Structure

The example is a `TestingProject` containing:

- one `ComponentMaster` (the tested door trim panel)
- one `Topic` of type `TestSeries` (the odor test), which references the
  component via `ComponentMasterID` and carries:
  - the applied standard via `Specification` (VDA 270:2022-05)
  - the test condition via `Conditions` (specimen variant C, storage condition 3)
  - the requirement via `TargetProperties` (odor grade max 3.5)
  - the reported result via `ReportedProperties` (odor grade 3.5, arithmetic mean
    rounded to half grades)
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
- Topic.ReportedProperties (reported result, with Aggregation and Rounding)
- Topic.Assessment

## Modelling Decisions

The requirement is expressed as a `TargetProperties` information set with an
`OdorRating` property of value type `Range` and a maximum value of 3.5, which
represents "at most 3.5".

The reported result is expressed as a `ReportedProperties` consolidated
characteristic value with an `OdorRating` of 3.5. The evaluation method is made
explicit: `Aggregation` is set to "Arithmetic mean" and `RoundingAccuracy` to
0.5, reflecting the VDA 270 rule of rounding the arithmetic mean to half grades.
In this getting started example the individual assessor grades are not shown; the
complete version adds them.

The odor grade is a dimensionless value, so no unit is used.

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
- Evaluation rule: arithmetic mean of individual grades, rounded to half grades
  (VDA 270 section 9)
