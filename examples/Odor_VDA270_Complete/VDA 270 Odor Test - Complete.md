# VDA 270 Odor Test - Complete

## Business Scenario

An interior trim component (a door trim panel) has to fulfil an odor requirement
according to VDA 270. A laboratory performs the odor assessment with a sensory
panel, records the individual assessor grades, consolidates them into a reported
result and compares it against the requirement. All of this is exchanged in a
structured, machine-readable form instead of a PDF laboratory report.

This complete example shows the full test result structure of the VDA 231-301
data model for an odor test, including the laboratory, the tested part instance,
the panel, the individual assessor grades and the consolidated reported result.

## Objective

This example demonstrates how a full odor test according to VDA 270 is
represented, from the individual assessor grades up to the consolidated,
reported result and the comparison against the requirement.

## Background: the VDA 270 odor scale and evaluation

VDA 270 rates the odor of trim materials on a scale from 1 to 6, half grades
allowed, where a lower value is better (1 = not perceptible, 6 = not acceptable).

Per VDA 270 section 9, the reported odor characteristic is the **arithmetic mean
of the individual assessor grades, rounded to half grades**. Both the individual
grades and the mean must always be given in the test report.

The example uses the calculation given in the standard itself:

- individual grades: 3.5, 3.5, 4.0
- arithmetic mean: 11.0 / 3 = 3.67
- rounded to half grades: **3.5**

Per VDA 270 section 8.1, at least three assessors are required. If the individual
grades differ by more than 2 grades, the measurement must be repeated with at
least five assessors. Here the grades differ by only 0.5, so three assessors are
sufficient. The reported grade (3.5) meets the requirement (max 3.5), so the
component passes. All values are illustrative.

## Structure

The example is a `TestingProject` containing:

- order and report metadata (client, laboratory order number, order and report
  date, signatory)
- one `TestingCenter` (the laboratory), referenced as contractor via
  `ContractorID`
- one `ComponentMaster` with one `ComponentInstance` (the specific tested part)
- one `Topic` of type `TestSeries` (the odor test), which carries:
  - the applied standard via `Specification` (VDA 270:2022-05)
  - the test condition via `Conditions` (specimen variant C, storage condition 3)
  - the responsible laboratory via `TestingCenterID`
  - the requirement via `TargetProperties` (odor grade max 3.5)
  - one `TestExecution` with the tester, the start date, the specimen (referring
    to the tested `ComponentInstance`), the measurement system (the sensory
    panel) and the three individual assessor grades via `SingleResults`
  - the consolidated result via `ReportedProperties`, which references the
    individual grades via `SingleResultIDs` and records the evaluation method
    (arithmetic mean, rounded to half grades)
  - the overall verdict via `Assessment` (Passed)

## Relevant Entities

- `TestingProject` - the transmission root
- `TestingCenter`, `Location`, `Person` - the laboratory and its people
- `ComponentMaster` and `ComponentInstance` - the tested component and part
- `Topic` (TestSeries) - the odor test
- `TestExecution` - the concrete execution of the test
- `Specimen` - the tested specimen, linked to the `ComponentInstance`
- `MeasurementSystem` - the sensory panel
- `SingleResultPoint` - an individual assessor grade
- `ConsolidatedCharacteristicValue` - the reported, consolidated result

## Relevant Attributes

- Topic.Specification / Topic.Conditions / Topic.TestingCenterID
- Topic.TargetProperties (requirement)
- Topic.Executions -> TestExecution.Tester / StartTime / Specimen /
  MeasurementSystems / SingleResults
- TestExecution.Specimen.ComponentInstanceID (link to the tested part)
- Topic.ReportedProperties (consolidated result) with Aggregation, Rounding,
  RoundingAccuracy and SingleResultIDs
- Topic.Assessment

## Modelling Decisions

The requirement is expressed as `TargetProperties` (odor grade max 3.5, using a
`Range` with a maximum value). The individual assessor grades are modelled as
`SingleResults` (each a `SingleResultPoint` with an `OdorRating` value).

The reported result is a `ConsolidatedCharacteristicValue` in `ReportedProperties`.
It makes the VDA 270 evaluation rule explicit and traceable:

- `Aggregation` = "Arithmetic mean"
- `RoundingAccuracy` = 0.5 and `Rounding` describing the rounding to half grades
- `Value` = 3.5 (the reported grade)
- `SingleResultIDs` referencing the three individual grades
- a comment stating the unrounded mean (3.67) and the rounded reported grade
  (3.5)

This keeps the full traceability from the individual grades via the arithmetic
mean to the reported half-grade result, as required by VDA 270 (which mandates
that both the individual grades and the mean are reported).

The specimen is linked to the tested `ComponentInstance` via
`ComponentInstanceID`, which connects the test result to a concrete produced
part. The odor grade is a dimensionless value, so no unit is used.

## JSON Example

See `testingProject-vda270-complete.json`.

## Validation Status

Aligned with the generic schema v3.0.0 (`TestingProject`, `TestingCenter`,
`Topic`, `TestExecution`, `Specimen`, `MeasurementSystem`, `SingleResults`,
`ReportedProperties`, `TargetProperties`). Validation against the released schema
version should be performed before productive use.

## Related Examples

- VDA 270 Odor Test - Getting Started
- Component Instance Traceability
- Material with Specification Customization

## Architectural References

- Root: `TestingProject`
- Entity: `Topic` (TestSeries) with `Executions`, `TargetProperties`,
  `ReportedProperties`
- Traceability: `ReportedProperties.SingleResultIDs` -> individual
  `SingleResultPoint` grades
- Evaluation rule: arithmetic mean of individual grades, rounded to half grades
  (VDA 270 section 9), captured via `Aggregation`, `Rounding`, `RoundingAccuracy`
- Link to part: `Specimen.ComponentInstanceID` -> `ComponentInstance`
