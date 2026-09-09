# Approval Entry

## Status

Discussion proposal.

`ApprovalEntry` and all approval-related structures used in this example are
not part of the released VDA 231-301 generic schema v3.0.0. The JSON file is
intentionally not schema-conformant.

All names, values, dates, identifiers, suppliers, locations, production lines
and approval information are fictional and illustrative.

## Business Scenario

Material approval and listing information has its own lifecycle and must remain
traceable independently of material master data and product data.

An approval does not necessarily apply to PP-GF30 as a whole. It can apply to a
specific supplier material and can be restricted by:

- the applicable specification and product version
- geographic scope
- production location and production line
- validity period

The example represents one listing decision for `Example PP-GF30 Grade A` from
`Supplier A`.

## Objective

This example demonstrates how approval information could be represented as an
independent and referencable business object.

The proposal separates:

- the generic material definition
- the concrete supplier-specific `MaterialSource`
- the approval or listing decision
- the use of the material in a product or PLM context

## When to Use This Example

Use this example as a discussion basis when:

- an approval or listing decision requires its own lifecycle
- a decision applies to a concrete supplier material
- the generic material must remain identifiable
- current status and status history must be distinguished
- geographic and production restrictions must be represented separately
- a validity period and supporting documents are required

Do not use this example as evidence that the proposed fields are available in
the released generic schema v3.0.0.

Use the **Material Catalog Entry** example for the generic material definition
and its possible supplier-specific sources.

Use the **Multiple Source Material** example when the primary concern is the
source actually used for a produced part.

## Example Overview

The draft JSON represents:

- approval type: `Listing`
- approval process: `X`
- current status: `Listed`
- generic material reference: `OEMMATID` with value `OEM111ALAHJD`
- concrete source reference: `b1a00000-1111-4111-8111-000000000001`
- material class: `PP-GF30`
- material name: `Glass fibre reinforced Polypropylene`
- trade name: `Example PP-GF30 Grade A`
- supplier: `Supplier A`, identified by DUNS `111111111`
- applicable specification: `OEM-POLYMER-STD-1000`, product version `90`
- geographic scope: China
- production scope: Example Production Site China, Production Line 4
- validity: 2026-01-15 to 2028-01-14
- one supporting listing document

The value `X` is an anonymized placeholder. It does not define a specific
company-internal approval process.

## Relevant Entities

### ApprovalEntry

The independent approval or listing record and root object of the example.

### ApprovalStatusEvent

One event in the proposed approval lifecycle. The example contains three status
events: `Submitted`, `UnderEvaluation` and `Listed`.

### GeographicScope

The geographic applicability of the approval. The example contains one scope of
type `WorldRegion` with code `CHINA`.

### ProductionScope

The production-specific applicability of the approval. The example contains one
production location and one production line.

### Location

The production location to which the approval applies.

### DocumentReference

A reference to a supporting listing document.

## Relevant Attributes

### Approval Identification

- `ApprovalEntry.Designation`
- `ApprovalEntry.Version`
- `ApprovalEntry.ApprovalProcess`
- `ApprovalEntry.ApprovalType`
- `ApprovalEntry.ListingId`

### Generic Material Reference

- `ApprovalEntry.ApprovedForMaterial`
- `ApprovalEntry.ApprovedForMaterial.IdentifierType`
- `ApprovalEntry.ApprovedForMaterial.Value`

### Concrete Approval Subject

- `ApprovalEntry.Subject`
- `ApprovalEntry.Subject.SubjectMaterialSourceID`
- `ApprovalEntry.Subject.MaterialName`
- `ApprovalEntry.Subject.MaterialClass`
- `ApprovalEntry.Subject.TradeName`
- `ApprovalEntry.Subject.Supplier.Identifier`
- `ApprovalEntry.Subject.Supplier.IdentifierType`
- `ApprovalEntry.Subject.Supplier.Name`

### Status and Lifecycle

- `ApprovalEntry.CurrentStatus`
- `ApprovalEntry.StatusHistory[]`
- `ApprovalEntry.StatusHistory[].Status`
- `ApprovalEntry.StatusHistory[].EffectiveFrom`
- `ApprovalEntry.StatusHistory[].Comment`

### Applicability

- `ApprovalEntry.ApplicableSpecification`
- `ApprovalEntry.ApprovalScope`
- `ApprovalEntry.ApprovalScope.GeographicScopes[]`
- `ApprovalEntry.ApprovalScope.GeographicScopes[].ScopeType`
- `ApprovalEntry.ApprovalScope.GeographicScopes[].Code`
- `ApprovalEntry.ApprovalScope.GeographicScopes[].Designation`
- `ApprovalEntry.ApprovalScope.GeographicScopes[].CodeAuthority`
- `ApprovalEntry.ApprovalScope.ProductionScopes[]`
- `ApprovalEntry.ApprovalScope.ProductionScopes[].ProductionLocation`
- `ApprovalEntry.ApprovalScope.ProductionScopes[].ProductionLine`

### Validity and Traceability

- `ApprovalEntry.ValidityPeriod`
- `ApprovalEntry.ValidityPeriod.ValidFrom`
- `ApprovalEntry.ValidityPeriod.ValidUntil`
- `ApprovalEntry.RelatedApprovalEntries[]`
- `ApprovalEntry.ReferenceDocuments[]`

## JSON Structure Confirmed by This Example

The JSON contains:

- one `ApprovedForMaterial` object
- one `Subject` object
- three entries in `StatusHistory[]`
- one `ApplicableSpecification`
- one entry in `GeographicScopes[]`
- one entry in `ProductionScopes[]`
- one `ValidityPeriod`
- an empty `RelatedApprovalEntries[]` list
- one entry in `ReferenceDocuments[]`

The empty `RelatedApprovalEntries[]` list demonstrates the proposed property,
but not a concrete predecessor or successor relationship.

## Modelling Decisions

### Independent Approval Object

The approval is represented as an independent `ApprovalEntry`, not as approval
fields embedded in `ComponentMaster` or `MaterialSource`.

This allows material master data, approval lifecycle data and product data to be
maintained independently.

### Generic Material and Concrete Source Remain Separate

`ApprovalEntry.ApprovedForMaterial` references the generic material through its
`OEMMATID` business key.

The example uses:

- `IdentifierType`: `OEMMATID`
- `Value`: `OEM111ALAHJD`

The `OEMMATID` is owned by the generic material on `ComponentMaster`. The
`ApprovalEntry` references it and does not become a second editable source.

`ApprovalEntry.Subject.SubjectMaterialSourceID` references the concrete
supplier-specific material source.

The proposal therefore preserves two levels:

- generic material: referenced by `ApprovedForMaterial`
- concrete supplier material: referenced by `SubjectMaterialSourceID`

At OEM01, the `OEMMATID` is called the PEW number.

The field name and structure of `ApprovedForMaterial` are first proposals and
can change. A future released schema takes precedence.

### Material Name, Material Class and Trade Name

Following ADR 0008:

- `MaterialClass` contains `PP-GF30`
- `MaterialName` contains `Glass fibre reinforced Polypropylene`
- `TradeName` contains `Example PP-GF30 Grade A`

These concepts must not be used interchangeably.

### Current Status and Status History

`ApprovalEntry.CurrentStatus` contains the current status `Listed`.

`ApprovalEntry.StatusHistory[]` contains the sequence:

1. `Submitted`, effective 2025-11-10
2. `UnderEvaluation`, effective 2025-12-01
3. `Listed`, effective 2026-01-15

The listed status values are discussion values, not a released controlled
vocabulary.

### Applicable Specification

The approval applies to:

- type: `MaterialStandard`
- number: `OEM-POLYMER-STD-1000`
- subnumber: `90`
- issue date: `2026-01`

This prevents the listing from being interpreted as approval for every possible
specification or application.

### Geographic and Production Scope

The geographic scope is modelled separately from the production scope.

The current JSON contains:

- geographic scope type: `WorldRegion`
- geographic code: `CHINA`
- geographic designation: `China`
- code authority: `OEM`
- production location: `Example Production Site China`
- production line identifier: `LINE-04`
- production line designation: `Production Line 4`

### Time-Limited Validity

The validity period contains:

- `ValidFrom`: 2026-01-15
- `ValidUntil`: 2028-01-14

The example does not decide whether `ValidUntil` must be mandatory in a future
schema.

### Versioning

The `ApprovalEntry` has its own proposed version, `0001`.

This version is independent of:

- the version of the generic material definition
- the version of the applicable specification
- the version or change status of a component in a PLM system

### Related Approval Entries

`ApprovalEntry.RelatedApprovalEntries` is empty in the current JSON.

The property is intended to support predecessor or successor relationships, but
this JSON does not demonstrate such a relationship.

### Reference Document

The current JSON contains one `DocumentReference`:

- document type: `ListingDocument`
- document identifier: `LIST-DOC-PPGF30-2026-001`
- title: `Listing for PP-GF30 Grade A`
- issue date: 2026-01-15

The document is referenced rather than embedded.

### Material Properties Remain Outside the Approval Entry

The JSON does not duplicate material properties or sustainability information
in the `ApprovalEntry`.

Those data remain associated with the related material catalog information.

## Source of Truth and References

- The generic material definition and its `OEMMATID` are maintained on the
  related `ComponentMaster`.
- `ApprovalEntry.ApprovedForMaterial` references the generic material through
  its `OEMMATID`.
- The concrete supplier material is maintained as a `MaterialSource` in the
  related material catalog information.
- `ApprovalEntry.Subject.SubjectMaterialSourceID` references the concrete
  `MaterialSource` to which the approval applies.
- `ApprovalEntry.Subject` contains the descriptive subject data used by this
  draft.
- The independent approval decision is maintained in `ApprovalEntry`.
- The current state is maintained in `ApprovalEntry.CurrentStatus`.
- The lifecycle history is maintained in `ApprovalEntry.StatusHistory[]`.
- The applicable requirement profile is maintained in
  `ApprovalEntry.ApplicableSpecification`.
- Geographic and production applicability are maintained in
  `ApprovalEntry.ApprovalScope`.
- Temporal applicability is maintained in `ApprovalEntry.ValidityPeriod`.
- Supporting document references are maintained in
  `ApprovalEntry.ReferenceDocuments[]`.
- Material properties and sustainability information remain outside the
  `ApprovalEntry`.

## JSON Example

See `approval-entry.draft.json`.

## Validation Status

`approval-entry.draft.json` is syntactically well-formed JSON, based on the
content provided for this review.

It is intentionally not schema-conformant because `ApprovalEntry` and its
related entities and attributes are discussion proposals outside the released
VDA 231-301 generic schema v3.0.0.

The example must not be interpreted as:

- an approved schema extension
- a normative definition of an approval process
- a complete model for all approval types
- a declaration of an actual material approval or listing

The JSON file remains the technical reference for the proposed field paths,
cardinalities and values.

## Related Examples

- **Material Catalog Entry**  
  Use this example for the generic material definition, possible material
  sources, regional availability and material catalog business key.

- **Multiple Source Material**  
  Use this example when possible material sources and the source actually used
  for a produced part have to be represented.

- **Odor Test with Concrete Material Source**  
  Use this draft example when a complete odor test must be linked to a concrete
  supplier material and proposed material-source identifiers.

## Architectural References

- Independent approval object: `ApprovalEntry`
- Generic material reference: `ApprovalEntry.ApprovedForMaterial`
- Generic material identifier type: `OEMMATID`
- Concrete source reference:
  `ApprovalEntry.Subject.SubjectMaterialSourceID`
- Current state: `ApprovalEntry.CurrentStatus`
- Complete lifecycle: `ApprovalEntry.StatusHistory[]`
- Applicable specification: `ApprovalEntry.ApplicableSpecification`
- Geographic and production scopes: `ApprovalEntry.ApprovalScope`
- Time-limited validity: `ApprovalEntry.ValidityPeriod`
- Proposed successor relationships: `ApprovalEntry.RelatedApprovalEntries[]`
- Supporting documents: `ApprovalEntry.ReferenceDocuments[]`
- ADR 0008: the abbreviated material designation is maintained in
  `MaterialClass`
- ADR 0009: the generic `OEMMATID` is owned by the generic material and is
  referenced without creating a second editable source
- ADR 0010: own identifiers of a concrete `MaterialSource` are a separate
  proposed concept
- ADR 0011: `ApprovedForMaterial` is proposed as the reference from an
  `ApprovalEntry` to the generic material through `OEMMATID`

## Open Points

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
- Is `ApprovedForMaterial` the right name and structure for the link to the
  generic material through `OEMMATID`?
