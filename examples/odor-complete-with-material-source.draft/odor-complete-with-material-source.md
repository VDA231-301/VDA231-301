# Odor Test with Concrete Material Source

## Status

Draft example.

The complete odor-test structure is based on the VDA 270 complete example.
This variant additionally uses the proposed `MaterialSource.Identifiers`
structure to identify a concrete supplier material through a material-database
identifier and a supplier material code.

The complete JSON file is intentionally treated as a draft. Proposed field
names and controlled values are subject to change. The released schema takes
precedence.

All names, values, dates, identifiers, suppliers and locations are fictional and
illustrative.

## Business Scenario

An interior trim component made of glass-fibre-reinforced polypropylene is
tested for odor according to VDA 270.

The test report must identify not only the generic material, but also the
concrete supplier material used to manufacture the tested part.

The example connects three levels that must remain distinct:

1. the generic material, identified through `OEMMATID`
2. the concrete supplier material, represented by `MaterialSource`
3. the produced part, represented by `ComponentInstance`

The generic material is represented by:

- `MaterialGroup`: `Thermoplast`
- `MaterialClass`: `PP-GF30`
- `MaterialName`: `Glass fibre reinforced Polypropylene`
- `IdentifierType`: `OEMMATID`
- `Value`: `OEM111ALAHJD`

The concrete supplier material is represented by:

- `TradeName`: `Example PP-GF30 Grade A`
- supplier name: `Supplier A`
- supplier identifier: `111111111`
- supplier identifier type: `DUNS`
- material-database identifier: `MDB-000123`
- supplier material code: `SUP-A-PPGF30-GRADEA`

The produced part references the concrete supplier material through
`ComponentInstance.MaterialSourceID`.

## Objective

This example demonstrates how a complete VDA 270 odor test can be connected to
the concrete supplier material used for the tested produced part.

The example also demonstrates how the generic material identity remains
separate from the concrete material-source identity.

## When to Use This Example

Use this example as a discussion basis when:

- a complete odor test has to be represented
- the concrete tested `ComponentInstance` has to be identified
- the material source actually used for the produced part has to be traceable
- a material-database identifier for the concrete supplier material is required
- a supplier material code has to be represented
- generic material identity and concrete source identity must remain separate
- individual assessor grades and the consolidated odor result must remain
  traceable

Do not use this example as evidence that `MaterialSource.Identifiers` is
available in the released generic schema v3.0.0.

Use the **VDA 270 Odor Test - Complete** example when the complete test context
is required without the proposed material-source identifiers.

Use the **Multiple Source Material** example when the primary concern is the set
of possible material sources and the source actually used for a produced part.

Use the **Approval Entry Draft** when a formal approval or listing decision for
a concrete material source has to be represented.

## Learning Goals

After reviewing this example, the reader should understand:

- how the generic material is represented on `ComponentMaster`
- how a concrete supplier material is represented as `MaterialSource`
- how the generic `OEMMATID` differs from source-specific identifiers
- how a material-database identifier can be proposed on
  `MaterialSource.Identifiers`
- how a supplier material code can be proposed on
  `MaterialSource.Identifiers`
- how `ComponentInstance.MaterialSourceID` identifies the source actually used
- how the test specimen is linked to the produced `ComponentInstance`
- how individual odor grades and the consolidated result remain traceable
- why adding material-source traceability does not change the modelling of the
  odor-test result itself

## Structure

The example is a `TestingProject` containing:

- client and order information
- one `TestingCenter`
- one `ComponentMaster`
- one `MaterialSource`
- one `ComponentInstance`
- one `TestSeries`
- one `TestExecution`
- one `Specimen`
- one sensory-panel `MeasurementSystem`
- three `SingleResultPoint` objects
- one `ConsolidatedCharacteristicValue`
- one overall `Assessment`

## Relevant Entities

### TestingProject

The `TestingProject` is the transmission root.

### ComponentMaster

The `ComponentMaster` contains the generic material description, generic
material identifier, possible material source and produced instance.

### MaterialSource

The `MaterialSource` represents the concrete supplier material.

It contains the material description, trade name, supplier, source-specific
identifiers and source-specific specification.

### ComponentInstance

The `ComponentInstance` represents the produced part.

It references the concrete material source used for production through
`MaterialSourceID`.

### TestSeries

The `TestSeries` contains the specification, conditions, target requirement,
test execution, consolidated reported result and assessment.

### TestExecution

The `TestExecution` contains tester, start time, specimen, measurement system
and individual assessor grades.

### Specimen

The `Specimen` references the concrete tested `ComponentInstance` through
`ComponentInstanceID`.

## Relevant Attributes

This example uses the following paths:

- `TestingProject.TestingCenters[]`
- `TestingProject.ComponentMasters[]`
- `TestingProject.ComponentMasters[].MaterialIdentifiers[]`
- `TestingProject.ComponentMasters[].MaterialSources[]`
- `TestingProject.ComponentMasters[].MaterialSources[].Identifiers[]`
- `TestingProject.ComponentMasters[].MaterialSources[].TradeName`
- `TestingProject.ComponentMasters[].MaterialSources[].Supplier`
- `TestingProject.ComponentMasters[].MaterialSources[].Specification`
- `TestingProject.ComponentMasters[].Instances[]`
- `TestingProject.ComponentMasters[].Instances[].MaterialSourceID`
- `TestingProject.Topics[]`
- `TestingProject.Topics[].ComponentMasterID`
- `TestingProject.Topics[].TestingCenterID`
- `TestingProject.Topics[].Specification`
- `TestingProject.Topics[].Conditions`
- `TestingProject.Topics[].TargetProperties`
- `TestingProject.Topics[].Executions[]`
- `TestingProject.Topics[].Executions[].Specimen.ComponentInstanceID`
- `TestingProject.Topics[].Executions[].MeasurementSystems[]`
- `TestingProject.Topics[].Executions[].SingleResults[]`
- `TestingProject.Topics[].ReportedProperties[]`
- `TestingProject.Topics[].ReportedProperties[].SingleResultIDs[]`
- `TestingProject.Topics[].Assessment`

## Modelling Decisions

### Generic Material Identity

The generic material identity is maintained in
`ComponentMaster.MaterialIdentifiers[]`.

The example uses:

- `IdentifierType`: `OEMMATID`
- `Value`: `OEM111ALAHJD`

The generic `OEMMATID` identifies the generic material and is not duplicated in
`MaterialSource.Identifiers`.

### Concrete Material Source

The concrete supplier material is maintained in
`ComponentMaster.MaterialSources[]`.

The source contains:

- `MaterialClass`: `PP-GF30`
- `MaterialName`: `Glass fibre reinforced Polypropylene`
- `TradeName`: `Example PP-GF30 Grade A`
- supplier identifier: `111111111`
- supplier identifier type: `DUNS`
- supplier name: `Supplier A`

`TradeName` is the supplier's commercial product name and is distinct from both
`MaterialClass` and `MaterialName`.

### Proposed Source-Specific Identifiers

The concrete source contains the proposed `Identifiers[]` list with:

- `MaterialDatabaseID`: `MDB-000123`
- `SupplierMaterialCode`: `SUP-A-PPGF30-GRADEA`

These identifiers belong to the concrete supplier material. They do not replace
the generic `OEMMATID`.

The `MaterialSource.Identifiers` structure and its controlled identifier types
are proposed in ADR 0010. The released schema takes precedence.

### Source Used for the Produced Part

The produced part is maintained in `ComponentMaster.Instances[]`.

Its `MaterialSourceID` value matches the `_id` of the material source contained
in `ComponentMaster.MaterialSources[]`.

This establishes the following reference:

- source `_id`: `b1a00000-1111-4111-8111-000000000001`
- instance `MaterialSourceID`:
  `b1a00000-1111-4111-8111-000000000001`

The produced part therefore references the concrete source actually used.

### Source-Specific Specification

The material source contains the following specification:

- `Type`: `OEMSPEC`
- `Number`: `1232`
- `SubNumber`: `40`
- `IssueDate`: `2026-01`
- `Title`: `Thermoplastic material for interior applications`

This source-specific specification belongs to the concrete `MaterialSource`.

### Test Data Remains Unchanged

The odor-test part follows the complete VDA 270 example.

Adding the concrete material source does not change how the following test data
is represented:

- target requirement
- individual assessor grades
- consolidated reported result
- references from the consolidated result to the individual grades
- overall assessment

The generic material, concrete material source, produced part and test result
remain separate but connected through references.

## Source of Truth and References

- The generic material description is maintained on the `ComponentMaster`.
- The generic material identity is maintained in
  `ComponentMaster.MaterialIdentifiers[]`.
- The possible concrete material sources are maintained in
  `ComponentMaster.MaterialSources[]`.
- The source-specific material-database identifier and supplier material code
  are maintained in the proposed `MaterialSource.Identifiers[]` structure.
- The concrete source's commercial product name is maintained in
  `MaterialSource.TradeName`.
- The source-specific specification is maintained in
  `MaterialSource.Specification`.
- The produced part is maintained in `ComponentMaster.Instances[]`.
- `ComponentInstance.MaterialSourceID` references the concrete source used for
  the produced part.
- The tested part is referenced by
  `TestExecution.Specimen.ComponentInstanceID`.
- The individual assessor grades are maintained in
  `TestExecution.SingleResults[]`.
- The consolidated result is maintained in `TestSeries.ReportedProperties[]`.
- `ConsolidatedCharacteristicValue.SingleResultIDs[]` references the individual
  grades used for the consolidated result.
- The overall verdict is maintained in `TestSeries.Assessment`.

## JSON Example

See `odor-complete-with-material-source.draft.json`.

## Validation Status

This example is intentionally treated as a draft because it contains the
proposed `MaterialSource.Identifiers` structure and proposed controlled values
for concrete source identifiers.

The complete odor-test structure should be validated against the referenced
released schema version.

The released schema remains authoritative for the availability and exact names
of fields. The JSON file is the technical reference for the concrete paths and
values used by this draft.

## Related Examples

- **VDA 270 Odor Test - Complete**  
  Use this example for the complete odor-test structure without the proposed
  material-source identifiers.

- **Multiple Source Material**  
  Use this example for the master/instance pattern of possible material sources
  and the source used for a produced part.

- **Material Catalog Entry**  
  Use this example for material-catalog information, possible sources and
  regional availability.

- **Approval Entry Draft**  
  Use this example for a formal approval or listing proposal linked to the
  concrete source and the generic material.

- **Color Definition**  
  Use this example for the analogous master/instance pattern using `Colors` and
  `ColorID`.

## Architectural References

- Generic material identity: `ComponentMaster.MaterialIdentifiers[]`
- Concrete sources: `ComponentMaster.MaterialSources[]`
- Proposed source identifiers: `MaterialSource.Identifiers[]`
- Material-database identifier type: `MaterialDatabaseID`
- Supplier material identifier type: `SupplierMaterialCode`
- Source used for production: `ComponentInstance.MaterialSourceID`
- Tested-part reference: `Specimen.ComponentInstanceID`
- Individual odor grades: `TestExecution.SingleResults[]`
- Consolidated odor result: `TestSeries.ReportedProperties[]`
- ADR 0001: definition sets on `ComponentMaster` and concrete assignments on
  `ComponentInstance`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0008: the abbreviated material designation is maintained in
  `MaterialClass`
- ADR 0009: the generic `OEMMATID` is maintained on the generic material without
  uncontrolled duplication
- ADR 0010: own typed identifiers of a concrete `MaterialSource` are proposed
