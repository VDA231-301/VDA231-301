# Material Catalog Entry

## Business Scenario

An OEM maintains a catalog of approved polymer materials (a "material kit" /
material construction set). For each approved material, the catalog records which
material it is, which suppliers and trade names are approved for it, in which
regions it is available, and which OEM material standard it fulfils. This
information exists and must be documented independently of any specific produced
part, purely at material level.

This example shows how such a catalog entry can be represented with the
VDA 231-301 data model. It uses a glass long fibre reinforced polypropylene
(PP-GLF30) as an example material. All identifiers, suppliers, trade names and
specifications are fictional and fully anonymized.

> Important framing: VDA 231-301 is **not** the material catalog system itself.
> It provides the standardized **data format** in which a catalog can describe
> its materials. The catalog remains the OEM's own system; VDA 231-301 gives it
> a common, machine-readable language.

## Objective

This example demonstrates two things:

1. How much of a real material catalog entry can already be represented with the
   released generic schema v3.0.0 (see `componentMaster-catalog-entry.json`).
2. Which additional attributes a real approval list still requires and are not
   yet part of the schema (see `componentMaster-catalog-entry.draft.json`).

## What the released schema already covers

The schema-conformant file `componentMaster-catalog-entry.json` represents:

- the approved material via `MaterialName`, `MaterialGroup`, `MaterialClass`
- the material identifier (catalog / material ID) via `MaterialIdentifiers`
- the applicable OEM material standard via `Specifications`
- the approved color via `Colors`
- the **approved material sources** via `MaterialSources`, each with its supplier
  (as a `Location` including a DUNS identifier), its trade name and its
  supplier-specific specification
- the **regional availability** per source (production vs. warehouse) via
  `MaterialSource.AdditionalInformation`
- a stable catalog key via `BusinessKeys`

This means the core of a material listing - "material X is approved and can be
sourced from supplier A (trade name, DUNS, region) or alternatively from supplier
B" - maps directly onto the existing `MaterialSources` pattern.

## What is still missing for a real catalog (draft extension)

The draft file `componentMaster-catalog-entry.draft.json` illustrates attributes
that a real approval list uses but that are **not** part of the released generic
schema v3.0.0. It is a discussion basis for possible schema extensions, not a
schema-conformant document:

- **Approval status / listing logic**: whether a material is listed, has a basic
  material approval, or is in a transition period (`ApprovalStatus`,
  `ApprovalProcess`).
- **Listing metadata**: listing identifier and listing date (`ListingId`,
  `ListingDate`).
- **Base material properties**: density and ash content as material properties
  (`MaterialProperties`).
- **Sustainability data**: recyclate shares (mechanical PIR/PCR, chemical,
  biocircular), mass balancing and carbon footprint (`Sustainability`).

These gaps are the actual result of building this example: creating the catalog
entry is at the same time a gap analysis of the schema. The approval status and
the listing identifier in particular are strong candidates for a future schema
extension, because they are central to any material catalog.

## Relevant Entities

- `ComponentMaster` - the material catalog entry
- `MaterialSource` - an approved source (supplier + trade name + specification)
- `Location` - the supplier, including its DUNS identifier
- `Color` - the approved color
- `Specification` - the applicable OEM material standard

## Relevant Attributes

- ComponentMaster.MaterialName
- ComponentMaster.MaterialGroup
- ComponentMaster.MaterialClass
- ComponentMaster.Version
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.Specifications
- ComponentMaster.Colors
- ComponentMaster.MaterialSources
- MaterialSource.TradeName
- MaterialSource.Supplier
- MaterialSource.Specification
- MaterialSource.AdditionalInformation

## Modelling Decisions

The catalog entry is modelled at material level on a `ComponentMaster`, without
any `Instances`, because a catalog describes approved materials independently of
produced parts. Approved sources are held as a definition set in
`MaterialSources`, consistent with the "definition on the master" pattern also
used for colors.

Regional availability is expressed per source via
`MaterialSource.AdditionalInformation` as an `InformationSet`, since the released
schema has no dedicated field for a region matrix.

The `Version` attribute (drawing / change status, ZGS) is included, in line with
the convention that every component example carries its version.

## JSON Example

- `componentMaster-catalog-entry.json` - schema-oriented, aligned with v3.0.0
- `componentMaster-catalog-entry.draft.json` - draft with proposed catalog
  extensions (not schema-conformant)

## Validation Status

The main file is aligned with the generic schema v3.0.0. The draft file is
intentionally not schema-conformant and serves as a discussion basis for
possible catalog-related schema extensions.

## Related Examples

- Multiple Source Material
- Color Definition
- Simple Material Definition

## Architectural References

- Definition set on master: `ComponentMaster.MaterialSources`
- Supplier as `Location` with DUNS identifier
- Open point (proposed): material approval status, listing identifier, listing
  date, base material properties and sustainability data as future schema
  extensions for material catalog use cases
