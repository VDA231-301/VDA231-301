# Approval Entry

## Business Scenario

Material approval and listing information has its own lifecycle and must remain
traceable independently of material master data and product data.

An approval or listing does not necessarily apply to a general material such as
PP-GF30 as a whole. It may apply to a specific trade type from a specific
material source and may be restricted to:

- a material specification or product version
- a geographic region
- a production location
- a specific production line
- a defined validity period

Different material sources for the same general material can therefore have
different approval statuses, scopes and validity periods.

This example illustrates how an independent approval entry could reference a
specific material source from the related
[material-catalog-entry/README.md](material-catalog-entry/README.md).

All names, values, dates, identifiers, suppliers, locations, production lines
and approval information are fictional and fully anonymized.

> **Important:** The structures shown in this example are discussion proposals.
> `ApprovalEntry` and its related attributes are not part of the released
> VDA 231-301 generic schema v3.0.0. The JSON file is intentionally not
> schema-conformant.

## Objective

This example demonstrates how approval and listing information could be
represented as an independent and referencable business object.

The proposed approach separates:

1. the reusable material definition
2. the supplier- and trade-name-specific material source
3. the approval or listing decision
4. the use of the material in a PLM or product context

This separation allows material master data, approval information and product
data to be maintained in separate systems while remaining connected through
stable identifiers.

The example focuses on one anonymized listing scenario. It does not define a
complete approval model for all possible approval types.

## Example Overview

The draft represents a listing entry for:

| Information | Example value |
|---|---|
| Material | PP-GF30 |
| Trade name | Example PP-GF30 Grade A |
| Supplier | Supplier A |
| Approval process | X |
| Approval type | Listing |
| Current status | Listed |
| Applicable specification | OEM-POLYMER-STD-1000, product version 90 |
| Geographic scope | China |
| Production scope | Example Production Site China, Production Line 4 |
| Validity | 2026-01-15 to 2028-01-14 |

The value `X` is an anonymized placeholder for the approval process. It does not
define or disclose a specific company-internal process.

## Referenced Material Source

The approval entry refers to a material source in the related
[material-catalog-entry/componentMaster-catalog-entry.json](material-catalog-entry/componentMaster-catalog-entry.json).

The referenced material source is:

```json
{
  "_id": "b1a00000-1111-4111-8111-000000000001",
  "_type": "MaterialSource",
  "MaterialName": "PP-GF30",
  "TradeName": "Example PP-GF30 Grade A"
}
```

The approval entry references this source through:

```json
"SubjectMaterialSourceID": "b1a00000-1111-4111-8111-000000000001"
```

The approval decision therefore applies to this specific material source and
trade type. It does not automatically apply to:

- every PP-GF30 material
- every trade type
- every supplier
- every production location
- every specification or application

## Relevant Entities

The example proposes the following entities:

- `ApprovalEntry`
  - an independent approval or listing record

- `ApprovalStatusEvent`
  - one documented status change in the approval lifecycle

- `GeographicScope`
  - the geographic applicability of the approval decision

- `ProductionScope`
  - the production-specific applicability of the approval decision

- `Location`
  - the relevant production location

- `DocumentReference`
  - a reference to a supporting approval or listing document

These entities are discussion proposals and are not part of the released generic
schema v3.0.0.

## Relevant Attributes

### Approval Identification

- `ApprovalEntry.Designation`
- `ApprovalEntry.Version`
- `ApprovalEntry.ApprovalProcess`
- `ApprovalEntry.ApprovalType`
- `ApprovalEntry.ListingId`

### Approval Subject

- `ApprovalEntry.Subject`
- `Subject.SubjectMaterialSourceID`
- `Subject.MaterialName`
- `Subject.TradeName`
- `Subject.Supplier`

### Status and Lifecycle

- `ApprovalEntry.CurrentStatus`
- `ApprovalEntry.StatusHistory`
- `ApprovalStatusEvent.Status`
- `ApprovalStatusEvent.EffectiveFrom`
- `ApprovalStatusEvent.Comment`

### Applicability

- `ApprovalEntry.ApplicableSpecification`
- `ApprovalEntry.ApprovalScope`
- `ApprovalScope.GeographicScopes`
- `ApprovalScope.ProductionScopes`
- `ProductionScope.ProductionLocation`
- `ProductionScope.ProductionLine`

### Validity and Traceability

- `ApprovalEntry.ValidityPeriod`
- `ValidityPeriod.ValidFrom`
- `ValidityPeriod.ValidUntil`
- `ApprovalEntry.RelatedApprovalEntries`
- `ApprovalEntry.ReferenceDocuments`

## Modelling Decisions

### Independent Approval Object

The approval entry is modelled as an independent business object rather than as
an embedded attribute of `ComponentMaster` or `MaterialSource`.

This supports separate ownership and lifecycle management for:

- material master data
- approval and listing information
- product and application data

A material database can maintain the material definition and its possible
sources. An approval system can maintain the approval lifecycle. A PLM system
can reference the material source and the applicable approval entry without
owning the complete approval history.

### Approval Refers to a Material Source

The approval entry refers to a specific `MaterialSource`.

This is necessary because different trade types or suppliers for the same
general material can have different:

- approval statuses
- geographic scopes
- production scopes
- validity periods
- applicable specifications

The existence of a `MaterialSource` does not by itself mean that the source is
formally approved or listed.

### Approval Process and Approval Type

The example separates the approval process from the approval type:

```json
"ApprovalProcess": "X",
"ApprovalType": "Listing"
```

`ApprovalProcess` identifies the applicable process using an anonymized value.

`ApprovalType` identifies the kind of approval record represented by the
example.

The example does not decide whether all future approval types should use the
same `ApprovalEntry` entity or specialized entities based on a common approval
concept.

### Complete Status History

The example distinguishes the current status from the complete status history.

The current status is:

```json
"CurrentStatus": "Listed"
```

The path to the current status is documented through:

```text
Submitted
    ↓
UnderEvaluation
    ↓
Listed
```

The proposed status values for discussion include:

- `Draft`
- `Submitted`
- `UnderEvaluation`
- `Listed`
- `Suspended`
- `Expired`
- `Withdrawn`
- `Rejected`

A general value such as `NotListed` is intentionally not used because it does
not explain why no valid listing is available.

These status values are discussion proposals and are not part of the released
generic schema v3.0.0.

### Geographic and Production Scope

Geographic applicability and production-specific applicability are modelled
separately.

The proposed geographic scope can represent, for example:

- a world region
- a country
- another defined geographic area

The proposed production scope can represent:

- a production location
- a production location and a specific production line

A production location or production line is optional. These elements are used
only when the approval decision is restricted to that production context.

A listing can therefore apply:

- to a geographic region without a specific production location
- to one production location
- to one production line at a specific location
- to a combination of geographic and production scopes

### Applicable Specification

The approval entry references the material specification and product version to
which the listing applies.

The example uses:

```text
Standard: OEM-POLYMER-STD-1000
Product version: 90
Issue date: 2026-01
```

The specification reference is aligned with the specification assigned to
`Example PP-GF30 Grade A` in the related material catalog entry.

This prevents the listing from being interpreted as a general approval of the
trade type for every possible requirement profile or application.

### Time-Limited Validity

The example contains a defined validity period:

```json
"ValidityPeriod": {
  "ValidFrom": {
    "Date": "2026-01-15"
  },
  "ValidUntil": {
    "Date": "2028-01-14"
  }
}
```

`ValidUntil` should remain optional because not every approval entry necessarily
has a predefined end date.

The absence of `ValidUntil` does not mean that an approval remains valid under
all circumstances. Approval-relevant changes may require a new approval
decision.

### Versioning

The approval entry can carry its own version:

```json
"Version": "0001"
```

Versioning is proposed as an optional capability.

The version of the approval entry is independent of:

- the version of the material definition
- the version of the applicable material specification
- the version or change status of a component in a PLM system

### Successor Relationships

An existing approval entry is not overwritten when a relevant change requires a
new approval decision.

A later approval entry can refer to the previous entry using:

```json
"RelatedApprovalEntries": [
  {
    "ApprovalEntryID": "previous-approval-entry-id",
    "RelationType": "Supersedes"
  }
]
```

The previous entry remains available with its original:

- status history
- approval scope
- validity period
- specification reference
- supporting documents

### No Evaluating Person

The example does not include an `ApprovedBy`, `Evaluator` or similar
person-related attribute.

The current business scenario does not require the evaluating person to be
documented.

### Reference Documents

The approval entry contains a reference to an illustrative listing document.

The supporting document is referenced rather than embedded in the approval
entry. This allows the approval object and the supporting document to remain
independent while still being traceable.

### Material Properties Remain Outside the Approval Entry

Material properties and sustainability information are not duplicated in the
approval entry.

They remain associated with the related material catalog information. The
approval entry references the applicable material source and specification.

## JSON Example

- approval-entry.draft.json
  - independent approval and listing discussion draft
  - refers to one material source from the related material catalog example
  - uses the anonymized approval process `X`
  - contains status history, approval scope, validity and document references
  - intentionally not schema-conformant

## Validation Status

The file approval-entry.draft.json is intentionally
not schema-conformant.

`ApprovalEntry` and its related entities and attributes are discussion proposals
for a possible future extension of the VDA 231-301 data model.

The example must not be interpreted as:

- an approved schema extension
- a normative definition of an approval process
- a complete model for all approval types
- a declaration of an actual material approval or listing

## Related Examples

- [material-catalog-entry/README.md](material-catalog-entry/README.md)
- [/material-catalog-entry/componentMaster-catalog-entry.json](material-catalog-entry/componentMaster-catalog-entry.json)
- [material-catalog-entry/componentMaster-catalog-entry.draft.json](material-catalog-entry/componentMaster-catalog-entry.draft.json)

## Architectural References

- approval information represented as an independent business object
- material source referenced using `SubjectMaterialSourceID`
- approval lifecycle represented using `CurrentStatus` and `StatusHistory`
- geographic and production scopes represented separately
- time-limited validity represented using `ValidityPeriod`
- previous and subsequent approval entries connected using
  `RelatedApprovalEntries`
- supporting documents referenced using `ReferenceDocuments`
- material properties and sustainability information retained outside the
  approval entry

## Open Points

The example identifies the following questions for further discussion:

- Should `ApprovalEntry` provide a common base concept for different approval
  types?
- Should listings and other approval types use specialized entities?
- Which approval statuses should be standardized?
- Should status events include a reason or reason code?
- Which geographic scope types, codes and code authorities are required?
- How should production locations and production lines be identified?
- Which changes require a new approval entry?
- Should `Version` be optional or mandatory?
- Can one approval entry refer to more than one applicable specification?
- Which metadata are required for supporting reference documents?
- How should another system determine which approval entry applies to a
  particular material source, region and production context?
