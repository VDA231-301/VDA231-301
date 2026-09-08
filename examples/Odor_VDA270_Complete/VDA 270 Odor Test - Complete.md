# VDA 270 Odor Test - Complete

## Status

Schema-oriented example.

This example is intended to align with the released VDA 231-301 generic schema
v3.0.0. Validation against the referenced schema version should be performed
before productive use.

## Business Scenario

An interior trim component, represented here by a door trim panel, has to fulfil
an odor requirement according to VDA 270.

A laboratory performs the odor assessment with a sensory panel. The laboratory
documents the individual assessor grades, consolidates them into a reported
result and compares the reported result with the target requirement.

The complete test context is exchanged in a structured, machine-readable form
instead of being provided only in a PDF laboratory report.

This complete example includes:

- order and report metadata
- the testing center
- the tested component and produced part
- the applicable test specification
- the test conditions
- the target requirement
- the concrete test execution
- the specimen
- the sensory panel as measurement system
- the individual assessor grades
- the consolidated reported result
- the overall assessment

## Objective

This example demonstrates how a complete odor test according to VDA 270 is
represented in a `TestingProject`.

It shows the complete traceability chain from the tested produced part and the
individual assessor grades to the consolidated reported result and the overall
assessment.

## When to Use This Example

Use this example when:

- the complete context of an odor test has to be represented
- the responsible testing center has to be documented
- the concrete tested part has to be identified
- the test execution and specimen have to be represented
- the sensory panel has to be represented as a measurement system
- individual assessor grades have to be retained
- the consolidated result must reference the individual results from which it
  was derived
- the target requirement, reported result and overall assessment must remain
  distinguishable

Do not use this example when:

- only a minimal introduction to the target and reported result is required
- individual assessor grades and execution details are not needed
- the primary concern is an application-specific deviation from a referenced
  specification
- the primary concern is the identity of a concrete supplier material

Use the **VDA 270 Odor Test - Getting Started** example when only the essential
representation of the target requirement, reported result and assessment is
needed.

Use the **Material with Specification Customization** example when an
application-specific requirement deviates from a requirement in a referenced
specification.

Use the **Odor Test with Concrete Material Source** draft when the complete odor
test must additionally be linked to the concrete supplier material actually
used and to proposed material-source identifiers.

## Learning Goals

After reviewing this example, the reader should understand:

- how a complete odor test is represented in a `TestingProject`
- how a `TestingCenter` is represented and referenced
- how the tested component and produced part are represented
- how the test requirement is represented through `TargetProperties`
- how a concrete test execution is represented
- how the specimen is linked to the tested `ComponentInstance`
- how the sensory panel is represented as a `MeasurementSystem`
- how individual assessor grades are represented through `SingleResults`
- how the consolidated reported result is represented through
  `ReportedProperties`
- how the consolidated result references the individual assessor grades
- how the target requirement, reported result and assessment differ
- how complete result traceability is maintained

## Structure

The example is a `TestingProject` containing:

- order and report metadata
- one `TestingCenter` representing the laboratory
- one `ComponentMaster` representing the tested component
- one `ComponentInstance` representing the concrete tested part
- one test-related topic with the concrete type `TestSeries`
- the applied VDA 270 specification
- the test conditions
- the target odor requirement
- one `TestExecution`
- one `Specimen` linked to the tested `ComponentInstance`
- one `MeasurementSystem` representing the sensory panel
- three individual assessor grades in `SingleResults`
- one consolidated reported result in `ReportedProperties`
- one overall `Assessment`

## Relevant Entities

### TestingProject

The `TestingProject` is the transmission root of the example.

It contains the project metadata, testing center, component data and test-related
topic required for the complete representation.

### TestingCenter

The `TestingCenter` represents the laboratory responsible for the odor test.

The laboratory is referenced from the test-related structures through its
identifier.

### ComponentMaster

The `ComponentMaster` represents the tested component definition.

It contains the `ComponentInstance` representing the concrete produced part
used as the test specimen.

### ComponentInstance

The `ComponentInstance` represents the concrete produced part that was tested.

The specimen refers to this produced part through `ComponentInstanceID`.

### TestSeries

The `TestSeries` represents the odor test.

It contains the applicable specification, conditions, target requirement, test
execution, consolidated reported result and overall assessment.

### TestExecution

The `TestExecution` represents the concrete execution of the odor test.

It identifies the tester, start date, specimen, measurement system and
individual assessor grades.

### Specimen

The `Specimen` represents the tested sample.

It links the test execution to the concrete tested `ComponentInstance` through
`ComponentInstanceID`.

### MeasurementSystem

The `MeasurementSystem` represents the sensory panel used for the odor
assessment.

### SingleResultPoint

Each `SingleResultPoint` represents one individual assessor grade.

### ConsolidatedCharacteristicValue

The `ConsolidatedCharacteristicValue` represents the reported odor result.

It documents the consolidated value, aggregation and rounding information and
references the individual assessor grades through `SingleResultIDs`.

## Relevant Attributes

This example focuses on the following structures and attributes:

- `TestingProject.Client`
- `TestingProject.ContractorID`
- `TestingProject.TestingCenters[]`
- `TestingProject.ComponentMasters[]`
- `TestingProject.ComponentMasters[].Version`
- `TestingProject.ComponentMasters[].Instances[]`
- `TestingProject.Topics[]`
- `TestingProject.Topics[].ComponentMasterID`
- `TestingProject.Topics[].TestingCenterID`
- `TestingProject.Topics[].NumberOfExecutions`
- `TestingProject.Topics[].Specification`
- `TestingProject.Topics[].Conditions`
- `TestingProject.Topics[].TargetProperties`
- `TestingProject.Topics[].Executions[]`
- `TestingProject.Topics[].Executions[].Tester`
- `TestingProject.Topics[].Executions[].StartTime`
- `TestingProject.Topics[].Executions[].Specimen`
- `TestingProject.Topics[].Executions[].Specimen.ComponentInstanceID`
- `TestingProject.Topics[].Executions[].MeasurementSystems[]`
- `TestingProject.Topics[].Executions[].SingleResults[]`
- `TestingProject.Topics[].ReportedProperties[]`
- `TestingProject.Topics[].ReportedProperties[].SingleResultIDs[]`
- `TestingProject.Topics[].ReportedProperties[].Aggregation`
- `TestingProject.Topics[].ReportedProperties[].Rounding`
- `TestingProject.Topics[].ReportedProperties[].RoundingAccuracy`
- `TestingProject.Topics[].Assessment`

## Modelling Decisions

The target requirement, individual assessor grades, consolidated reported result
and overall assessment are represented separately.

The target odor requirement is maintained in `TargetProperties`. It defines the
maximum accepted odor rating for the tested component.

The individual assessor grades are maintained in `SingleResults`. Each grade is
represented as a `SingleResultPoint` with the property `OdorRating`.

The reported odor result is maintained in `ReportedProperties` as a
`ConsolidatedCharacteristicValue`.

The consolidated result makes the evaluation method explicit through:

- `Aggregation`
- `Rounding`
- `RoundingAccuracy`
- the consolidated `Value`
- `SingleResultIDs`

`SingleResultIDs` references the individual assessor grades used to derive the
consolidated result. The consolidated result therefore remains traceable to its
source values.

The example uses three illustrative individual grades:

- 3.5
- 3.5
- 4.0

The arithmetic mean is 3.67. The reported result is 3.5 after rounding to the
nearest half grade according to the rule documented in the example.

The target requirement is a maximum value of 3.5. The reported result is 3.5.
The overall assessment is therefore represented as `Passed` in this example.

The requirement, reported result and assessment must not be conflated:

- `TargetProperties` defines what has to be achieved
- `SingleResults` contains the individual observed values
- `ReportedProperties` contains the consolidated reported result
- `Assessment` contains the overall verdict

The specimen is linked to the concrete tested produced part through
`Specimen.ComponentInstanceID`.

This link establishes traceability between the test result and the relevant
`ComponentInstance`.

The sensory panel is represented as a `MeasurementSystem`. The individual
assessor grades remain separate results and are not replaced by the consolidated
reported value.

The odor rating is represented as a dimensionless value. No unit is used.

All example values are illustrative.

## Source of Truth and References

- The complete transmission is represented by the `TestingProject`.
- The client is maintained in `TestingProject.Client`.
- `TestingProject.ContractorID` references the `_id` of the responsible
  laboratory in `TestingProject.TestingCenters[]`.
- The tested component definition is maintained in
  `TestingProject.ComponentMasters[]`.
- The concrete tested part is maintained in
  `TestingProject.ComponentMasters[].Instances[]`.
- The odor test is maintained in `TestingProject.Topics[]` as an object with
  `"_type": "TestSeries"`.
- `TestingProject.Topics[].ComponentMasterID` references the `_id` of the
  tested component in `TestingProject.ComponentMasters[]`.
- `TestingProject.Topics[].TestingCenterID` references the `_id` of the
  responsible laboratory in `TestingProject.TestingCenters[]`.
- The applied test standard is maintained in
  `TestingProject.Topics[].Specification`.
- The test conditions are maintained in
  `TestingProject.Topics[].Conditions`.
- The target requirement is maintained in
  `TestingProject.Topics[].TargetProperties`.
- The concrete test execution is maintained in
  `TestingProject.Topics[].Executions[]`.
- The specimen links the test execution to the tested part through
  `TestingProject.Topics[].Executions[].Specimen.ComponentInstanceID`.
- The sensory panel is maintained in
  `TestingProject.Topics[].Executions[].MeasurementSystems[]`.
- The individual assessor grades are maintained in
  `TestingProject.Topics[].Executions[].SingleResults[]`.
- The consolidated reported result is maintained in
  `TestingProject.Topics[].ReportedProperties[]`.
- `TestingProject.Topics[].ReportedProperties[].SingleResultIDs[]` references
  the `_id` values of the individual grades used for the consolidated result.
- The aggregation and rounding method is maintained with the consolidated
  result.
- The overall verdict is maintained in
  `TestingProject.Topics[].Assessment`.
- The consolidated result does not replace the individual assessor grades.
- The assessment does not replace either the target requirement or the reported
  result.

## JSON Example

See `testingProject-vda270-complete.json`.

## Validation Status

This example is intended to align with the generic schema v3.0.0, including the
representation of:

- `TestingProject`
- `TestingCenter`
- `ComponentMaster`
- `ComponentInstance`
- `TestSeries`
- `TestExecution`
- `Specimen`
- `MeasurementSystem`
- `SingleResults`
- `ReportedProperties`
- `TargetProperties`
- `Assessment`

Validation against the referenced released schema version should be performed
before productive use.

The README describes the purpose and modelling pattern of the example. The JSON
file remains the technical reference for the concrete object paths, list
cardinalities, identifiers and field values.

## Related Examples

- **VDA 270 Odor Test - Getting Started**  
  Use this example when only the target requirement, reported result and overall
  assessment are needed without the full test execution and individual grades.

- **Odor Test with Concrete Material Source**  
  Use this draft example when the complete odor test must additionally be linked
  to a concrete supplier material and proposed material-source identifiers.

- **Component Instance Traceability**  
  Use this example when the primary concern is the production traceability of an
  individually manufactured part.

- **Material with Specification Customization**  
  Use this example when an application-specific requirement deviates from a
  requirement in a referenced specification.

## Architectural References

- Transmission root: `TestingProject`
- Client: `TestingProject.Client`
- Contractor reference: `TestingProject.ContractorID`
- Laboratories: `TestingProject.TestingCenters[]`
- Tested components: `TestingProject.ComponentMasters[]`
- Tested produced parts: `TestingProject.ComponentMasters[].Instances[]`
- Test topics: `TestingProject.Topics[]`
- Test representation: object with `"_type": "TestSeries"`
- Component reference: `TestingProject.Topics[].ComponentMasterID`
- Testing-center reference: `TestingProject.Topics[].TestingCenterID`
- Applied test standard: `TestingProject.Topics[].Specification`
- Test conditions: `TestingProject.Topics[].Conditions`
- Target requirement: `TestingProject.Topics[].TargetProperties`
- Test executions: `TestingProject.Topics[].Executions[]`
- Tested specimen:
  `TestingProject.Topics[].Executions[].Specimen`
- Link to produced part:
  `TestingProject.Topics[].Executions[].Specimen.ComponentInstanceID`
- Sensory panel:
  `TestingProject.Topics[].Executions[].MeasurementSystems[]`
- Individual assessor grades:
  `TestingProject.Topics[].Executions[].SingleResults[]`
- Consolidated result: `TestingProject.Topics[].ReportedProperties[]`
- Traceability to individual grades:
  `TestingProject.Topics[].ReportedProperties[].SingleResultIDs[]`
- Evaluation method: `Aggregation`, `Rounding` and `RoundingAccuracy`
- Overall verdict: `TestingProject.Topics[].Assessment`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0008: the abbreviated material designation is maintained in
  `MaterialClass`
- ADR 0009: material identifiers are typed and stored without uncontrolled
  duplication

