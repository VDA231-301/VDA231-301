# Material Catalog Entry

## Business Scenario

An OEM maintains a catalog of standardized polymer materials, sometimes described
as a material kit or material construction set. For each material definition, the
catalog records the material identity, applicable material standard, available
colors, possible material sources, supplier trade names and regional availability.

The catalog information can be reused across applications and systems. The example
uses an application-oriented designation but does not represent a specific produced
component instance, serial number or production batch.

This example shows how such a catalog entry can be represented using the
VDA 231-301 data model. It uses glass fibre reinforced polypropylene
(PP-GF30) in the context of a door trim panel. All identifiers, suppliers,
trade names, specifications, properties and sustainability values are fictional
and fully anonymized.

> Important framing: VDA 231-301 is **not** the material catalog system itself.
> It provides a standardized, machine-readable data structure that can be used
> to describe and exchange material, source and related technical information.
> The material catalog and its business rules remain within the responsible OEM
> systems.

## Objective

This example demonstrates three aspects:

1. Which elements of a material catalog entry can already be represented using
   the released generic schema v3.0.0
   (see `componentMaster-catalog-entry.json`).
2. Which additional material property and sustainability information may be
   relevant for a material catalog but is not yet represented by the released
   generic schema v3.0.0
   (see `componentMaster-catalog-entry.draft.json`).
3. Why formal approval and listing information should be represented as a
   separate, referencable business object rather than embedded directly in the
   material definition
   (see `approval-entry.draft.json`).

## What the released schema already covers

The schema-oriented file `componentMaster-catalog-entry.json` represents:

- the material definition via `MaterialName`, `MaterialGroup` and
  `MaterialClass`
- the material identifier via `MaterialIdentifiers`
- the version or change status via `Version`
- the applicable OEM material standard via `Specifications`
- the color definition via `Colors`
- potential material sources via `MaterialSources`
- the supplier of each material source as a `Location`, including a DUNS
  identifier
- the supplier trade name and source-specific specification
- regional availability information per material source via
  `MaterialSource.AdditionalInformation`
- a stable catalog key via `BusinessKeys`

The existing `MaterialSources` pattern can therefore describe that one material
definition is available from multiple suppliers under different trade names.

The existing schema elements do **not** state that a material, color, supplier or
material source is formally approved or listed. Formal approval and listing
information is handled separately in the discussion draft described below.

## Material Properties and Sustainability Data

The draft file `componentMaster-catalog-entry.draft.json` adds information that
may be relevant for a real material catalog but is not represented by the
released generic schema v3.0.0.

The discussion fields include:

- base material properties such as density and ash content via
  `MaterialProperties`
- virgin material share
- mechanical pre-consumer recyclate share
- mechanical post-consumer recyclate share
- chemically recycled material share
- biocircular material share
- carbon footprint information via `Sustainability`

The carbon footprint in the draft includes:

- a value and unit
- an illustrative calculation scope
- a reference year
- a data-quality statement

All material property and sustainability values are fictional and are included
only to support the schema discussion.

## Approval and Listing Information

Formal approval and listing information is intentionally not embedded in the
material catalog entry.

The discussion draft `approval-entry.draft.json` introduces an independent and
referencable `ApprovalEntry`. The entry refers to a specific `MaterialSource`
using its identifier.

The approval draft illustrates:

- an anonymized approval process via `ApprovalProcess: "X"`
- the approval type, for example `Listing`
- an optional version or change status
- a listing identifier
- the current status
- a complete status history
- a reference to the applicable material specification
- geographic scopes such as a world region
- production-specific scopes such as a production location
- an optional production line
- a time-limited validity period
- references to supporting documents
- relationships to previous or subsequent approval entries

The separation between `MaterialSource` and `ApprovalEntry` allows material
master data and approval information to be maintained independently.

A material source can exist without a corresponding listing entry. Different
material sources for the same general material can also have different approval
statuses, scopes and validity periods.

## Status History

The approval draft demonstrates that a single value such as `Listed` or
`NotListed` is not sufficient for complete documentation.

The proposed status history can distinguish states such as:

- `Draft`
- `Submitted`
- `UnderEvaluation`
- `Listed`
- `Suspended`
- `Expired`
- `Withdrawn`
- `Rejected`

These values are discussion proposals and are not part of the released generic
schema v3.0.0.

Existing approval entries should not be overwritten when the relevant trade
type, production process, production location or production line changes.

A subsequent approval entry can refer to the previous entry using a relationship
such as:

```json
{
  "ApprovalEntryID": "previous-approval-entry-id",
  "RelationType": "Supersedes"
}
