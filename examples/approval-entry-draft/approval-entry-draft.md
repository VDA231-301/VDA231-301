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
../material-catalog-entry/README.md.

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
[material-catalog-entry/componentMaster-catalog-entry.json](../material-catalog-entry/componentMaster-catalog-entry.json).

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

These status values
