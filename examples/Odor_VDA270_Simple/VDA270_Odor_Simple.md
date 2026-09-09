# VDA 270 Odor Test - Getting Started

## Status

Schema-oriented example.

This example is intended to align with the released VDA 231-301 generic schema
v3.0.0. Validation against the referenced schema version should be performed
before productive use.

## Business Scenario

An interior trim component, represented here by a door trim panel, has to fulfil
an odor requirement according to VDA 270.

A laboratory determines the odor characteristic of the material. The
requirement and the reported result are exchanged in a structured,
machine-readable form instead of being provided only in a PDF laboratory
report.

This getting-started example shows the essential representation of an odor test
result in the VDA 231-301 data model:

- the applicable test specification
- the test conditions
- the target requirement
- the reported result
- the overall assessment

The information is embedded in a minimal `TestingProject`.

## Objective

This example demonstrates, in a minimal form, how an odor test requirement is
represented through `Topic.TargetProperties` and how the corresponding reported
result is represented through `Topic.ReportedProperties`.

The example also shows how the overall verdict is represented through
`Topic.Assessment`.

## When to Use This Example

Use this example when:

- a minimal introduction to the VDA 231-301 test result structure is required
- an odor test requirement and its reported result have to be represented
- the difference between target and reported properties has to be explained
- the complete laboratory and execution context is not required
- individual assessor grades do not have to be included
- a compact example is preferable for onboarding or initial implementation

Do not use this example when:

- individual assessor grades have to be represented
- the reported result must be traceable to individual results
- a laboratory, tester, specimen or measurement system has to be represented
- the complete test execution has to be documented
- a concrete material source and its material-database identifier have to be
  included

Use the **VDA 270 Odor Test - Complete** example when the full test context,
individual assessor grades and the derivation of the consolidated result have
to be represented.

Use the **Odor Test with Concrete Material Source** draft when the test result
must additionally be linked to a concrete supplier material and its proposed
material-source identifiers.

Use the **Material with Specification Customization** example when the primary
concern is an application-specific deviation from a requirement in a referenced
specification rather than the representation of a test result.

## Learning Goals

After reviewing this example, the reader should understand:

- how a minimal odor test is represented within a `TestingProject`
- how the tested component is represented by a `ComponentMaster`
- how the odor test is represented by a `Topic` of type `TestSeries`
- how the applied test specification is represented
- how the test conditions are represented
- how the target requirement is separated from the reported result
- how `TargetProperties` represents the requirement
- how `ReportedProperties` represents the reported result
- how `Assessment` represents the overall verdict
- why the individual assessor grades are intentionally omitted from this
  getting-started example

## Structure

The example is a `TestingProject` containing:

- one `ComponentMaster` representing the tested component
- one `Topic` of type `TestSeries` representing the odor test
- a reference from the `Topic` to the tested component through
  `ComponentMasterID`
- the applied test standard through `Specification`
- the test conditions through `Conditions`
- the target requirement through `TargetProperties`
- the reported test result through `ReportedProperties`
- the overall verdict through `Assessment`

## Relevant Entities

### TestingProject

The `TestingProject` is the transmission root of the example.

It contains the component and the test-related topic required for the minimal
representation.

### ComponentMaster

The `ComponentMaster` represents the tested component.

The `Topic` refers to the component through `ComponentMasterID`.

### Topic

The `Topic` represents the odor test and has the type `TestSeries`.

It contains the applicable specification, test conditions, target requirement,
reported result and overall assessment.

### Specification

The `Specification` identifies the applied test standard.

In this example, the applicable test standard is VDA 270 with the issue date
used in the JSON example.

## Relevant Attributes

This example focuses on the following attributes:

- `TestingProject.ComponentMasters[]`
- `TestingProject.ComponentMasters[]._id`
- `TestingProject.ComponentMasters[].Version`
- `TestingProject.Topics[]`
- `TestingProject.Topics[].TestType`
- `TestingProject.Topics[].ComponentMasterID`
- `TestingProject.Topics[].Specification`
- `TestingProject.Topics[].Conditions`
- `TestingProject.Topics[].TargetProperties`
- `TestingProject.Topics[].ReportedProperties[]`
- `TestingProject.Topics[].Assessment`

## Modelling Decisions

The example separates the requirement from the reported result.

The requirement is represented in `Topic.TargetProperties`.

The reported result is represented in `Topic.ReportedProperties`.

This separation is essential because a target requirement and a measured or
reported result have different meanings and different data ownership.

The target odor requirement is represented as an `OdorRating` property with the
value type `Range` and a maximum value of 3.5. The maximum value expresses that
the accepted odor rating must not exceed 3.5.

The reported odor result is represented as a consolidated characteristic value
in `Topic.ReportedProperties`, with an `OdorRating` value of 3.5.

The evaluation method is made explicit in the reported result:

- `Aggregation` is set to `Arithmetic mean`
- `RoundingAccuracy` is set to 0.5
- the reported value is 3.5

The overall verdict is represented separately in `Topic.Assessment` and is set
to `Passed` in this example.

The test requirement, the reported value and the overall assessment are related
but must not be conflated:

- `TargetProperties` defines what has to be achieved
- `ReportedProperties` records the reported result
- `Assessment` records the verdict derived from comparing the result with the
  requirement

The individual assessor grades are intentionally not shown in this
getting-started example.

The complete example adds:

- a `TestingCenter`
- a concrete tested `ComponentInstance`
- a `TestExecution`
- a `Specimen`
- a `MeasurementSystem`
- individual assessor grades in `SingleResults`
- references from the consolidated result to the individual results

The odor rating is represented as a dimensionless value. No unit is used.

The values in this example are illustrative.

## Source of Truth and References

- The complete transmission is represented by the `TestingProject`.
- The tested component definition is maintained in
  `TestingProject.ComponentMasters[]`.
- The odor test is maintained in `TestingProject.Topics[]` as an object with
  `"_type": "TestSeries"`.
- `TestingProject.Topics[].ComponentMasterID` references the `_id` of the
  tested component in `TestingProject.ComponentMasters[]`.
- The applied test standard is maintained in
  `TestingProject.Topics[].Specification`.
- The test conditions are maintained in
  `TestingProject.Topics[].Conditions`.
- The target requirement is maintained in
  `TestingProject.Topics[].TargetProperties`.
- The reported result is maintained in
  `TestingProject.Topics[].ReportedProperties[]`.
- The overall verdict is maintained in
  `TestingProject.Topics[].Assessment`.
- The reported result does not replace or redefine the target requirement.
- The assessment does not replace either the target requirement or the reported
  result.
- Individual assessor grades are not included in this getting-started example.
  If individual grades and their traceability are required, the complete odor
  test example is the relevant source.

## JSON Example

See `testingProject-vda270-getting-started.json`.

## Validation Status

This example is intended to align with the generic schema v3.0.0, including the
root type `TestingProject` and the use of `Topic.TargetProperties`,
`Topic.ReportedProperties` and `Topic.Assessment`.

Validation against the referenced released schema version should be performed
before productive use.

The README describes the purpose and modelling pattern of the example. The JSON
file remains the technical reference for the concrete object structure and
field values.

## Related Examples

- **VDA 270 Odor Test - Complete**  
  Use this example when the complete test context, individual assessor grades,
  their consolidation and the link to a concrete tested part have to be
  represented.

- **Odor Test with Concrete Material Source**  
  Use this draft example when a complete odor test must additionally be linked
  to a concrete supplier material and proposed material-source identifiers.

- **Material with Specification Customization**  
  Use this example when an application-specific requirement deviates from the
  requirement in a referenced specification.

- **Component Instance Traceability**  
  Use this example when the primary concern is production traceability for an
  individually manufactured part rather than the representation of a test
  result.

## Architectural References

- Transmission root: `TestingProject`
- Tested components: `TestingProject.ComponentMasters[]`
- Test topics: `TestingProject.Topics[]`
- Test representation: object with `"_type": "TestSeries"`
- Component reference: `TestingProject.Topics[].ComponentMasterID`
- Applied test standard: `TestingProject.Topics[].Specification`
- Test conditions: `TestingProject.Topics[].Conditions`
- Target requirement: `TestingProject.Topics[].TargetProperties`
- Reported results: `TestingProject.Topics[].ReportedProperties[]`
- Overall verdict: `TestingProject.Topics[].Assessment`
- Requirement/result separation:
  `TargetProperties` versus `ReportedProperties`
- Evaluation information in the reported result:
  `Aggregation`, `Rounding` and `RoundingAccuracy`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0008: the abbreviated material designation is maintained in
  `MaterialClass`
- ADR 0009: material identifiers are typed and stored without uncontrolled
  duplication
