# Material Catalog Entry

## Status

Draft example.

This example is intentionally not a schema-conformant document.

The JSON uses a `ComponentMaster` to represent a material catalog entry and
contains the proposed `MaterialProperties` and `Sustainability` structures.
According to the JSON comment, these two structures are not represented by the
released VDA 231-301 generic schema v3.0.0.

All identifiers, suppliers, specifications, material properties and
sustainability values in this example are fictional and illustrative.

## Business Scenario

An organization maintains a reusable material catalog entry for a glass-fibre-
reinforced polypropylene used for an interior component.

The catalog entry combines information about:

- the material definition
- the generic material identifier
- the referenced material standard
- an available color
- two possible supplier-specific material sources
- regional availability of the material sources
- additional material properties
- sustainability information
- a stable material catalog business key

Approval and listing information is intentionally not embedded in the material
catalog entry. Such information is represented separately by a draft
`ApprovalEntry` that references the applicable `MaterialSource` by its
identifier.

## Objective

This example demonstrates how material catalog information can be organized in
a `ComponentMaster` and how generic material information can be distinguished
from concrete supplier-specific material sources.

It also provides a discussion basis for the proposed `MaterialProperties` and
`Sustainability` structures.

## When to Use This Example

Use this example when:

- a reusable material catalog entry has to be described
- a generic material has to be identified independently of a supplier product
- a referenced material standard has to be included
- available colors have to be represented
- several possible supplier-specific material sources have to be listed
- regional availability has to be documented for each material source
- a stable material catalog business key has to be provided
- proposed material-property or sustainability structures have to be discussed

Do not use this example as evidence that `MaterialProperties` or
`Sustainability` are available in the released generic schema v3.0.0.

Do not use this example to embed approval or listing lifecycle information in
the `ComponentMaster`.

Use the separate **Approval Entry Draft** when status, history, scope, validity
or other approval-related information has to be represented.

## Learning Goals

After reviewing this example, the reader should understand:

- how the material catalog entry is represented by a `ComponentMaster`
- how `MaterialGroup`, `MaterialClass` and `MaterialName` are used
- how the generic material is identified through typed
  `MaterialIdentifiers`
- how an applicable material standard is represented through `Specifications`
- how an available color is represented through `Colors`
- how concrete supplier materials are represented through `MaterialSources`
- how `TradeName` distinguishes a supplier product from the generic material
- how supplier identity is represented through a `Location` and a DUNS
  identifier
- how regional availability is represented through
  `MaterialSource.AdditionalInformation`
- how the material catalog entry is identified through `BusinessKeys`
- which structures in this example are explicitly treated as discussion
  structures
- why approval and listing information remains separate from the material
  catalog entry

## Relevant Entities

### ComponentMaster

The `ComponentMaster` represents the material catalog entry.

It contains the generic material description, material identifier, referenced
material standard, available color, possible material sources, proposed
material properties, proposed sustainability information and the material
catalog business key.

### Specification

The `Specification` represents the referenced material standard.

The component-level specification contains the identifying and descriptive
information for the example material standard.

Each `MaterialSource` also contains a source-level `Specification` referring to
the same material standard and product version.

### Color

The `Color` represents an available color for the material catalog entry.

In this example, the available color is black with RAL code 9005.

### MaterialSource

Each `MaterialSource` represents a concrete supplier-specific material source
for the generic material.

The example contains two material sources with different trade names,
suppliers and regional availability information.

### Location

The `Location` embedded in `MaterialSource.Supplier` represents the supplier.

The supplier is identified by a DUNS identifier and a human-readable name.

### InformationSet

The `InformationSet` in `MaterialSource.AdditionalInformation` represents the
regional availability of the corresponding material source.

### BusinessKey

Each entry in `BusinessKeys` contains a `Name` and a `Value` that identify the
material catalog entry in its business context.

## Relevant Attributes

This example uses the following structures and attributes:

- `ComponentMaster.Designation`
- `ComponentMaster.MaterialGroup`
- `ComponentMaster.MaterialClass`
- `ComponentMaster.MaterialName`
- `ComponentMaster.OemIdentifier`
- `ComponentMaster.Version`
- `ComponentMaster.MaterialIdentifiers[]`
- `ComponentMaster.Specifications[]`
- `ComponentMaster.Colors[]`
- `ComponentMaster.MaterialSources[]`
- `ComponentMaster.MaterialProperties`
- `ComponentMaster.Sustainability`
- `ComponentMaster.BusinessKeys[]`
- `MaterialSource.MaterialGroup`
- `MaterialSource.MaterialClass`
- `MaterialSource.MaterialName`
- `MaterialSource.TradeName`
- `MaterialSource.Supplier`
- `MaterialSource.Specification`
- `MaterialSource.AdditionalInformation`
- `Location.Identification[]`
- `InformationSet.Attributes[]`

## Material Definition

The generic material is described through three distinct attributes:

- `MaterialGroup`: `Thermoplast`
- `MaterialClass`: `PP-GF30`
- `MaterialName`: `Glass fibre reinforced Polypropylene`

These values describe different aspects of the material and must not be used
interchangeably.

The generic material identifier is represented as a typed entry in
`ComponentMaster.MaterialIdentifiers[]`:

- `IdentifierType`: `OEMMATID`
- `Value`: `OEM111ALAHJD`

The material catalog entry has version `0001`.

## Referenced Material Standard

The referenced material standard is maintained in
`ComponentMaster.Specifications[]`.

The example uses:

- `Type`: `MaterialStandard`
- `Number`: `OEM-POLYMER-STD-1000`
- `SubNumber`: `90`
- `IssueDate`: `2026-01`
- `Title`: `Example OEM material standard for thermoplastic interior materials,
  product version 90 (glass fibre reinforced PP)`

The two `MaterialSource` objects contain source-level specifications with the
same type, number, subnumber and issue date.

## Available Color

The available color is maintained in `ComponentMaster.Colors[]`.

The example contains:

- `Name`: `Black`
- `Code`: `9005`
- `CodeAuthority`: `RAL`

The color definition is part of the catalog entry. The example does not contain
a `ComponentInstance` and therefore does not assign an actual color to a
produced part.

## Material Sources

The possible supplier-specific material sources are maintained in
`ComponentMaster.MaterialSources[]`.

Both sources describe the same material group, material class and material
name as the generic material definition.

### Material Source A

Material Source A contains:

- `TradeName`: `Example PP-GF30 Grade A`
- supplier identifier: `111111111`
- supplier identifier type: `DUNS`
- supplier name: `Supplier A`

Its regional availability is maintained in
`MaterialSource.AdditionalInformation`:

- `RegionEMEA`: `production`
- `RegionNAFTA`: `warehouse`
- `RegionAPAC`: `warehouse`

### Material Source B

Material Source B contains:

- `TradeName`: `Example PP-GF30 Grade B`
- supplier identifier: `222222222`
- supplier identifier type: `DUNS`
- supplier name: `Supplier B`

Its regional availability is maintained in
`MaterialSource.AdditionalInformation`:

- `RegionAPAC`: `production`

The values `production` and `warehouse` are illustrative values in this draft.

## Proposed Material Properties

The example contains the proposed `MaterialProperties` structure with:

- density: 1.13 g/cm^3
- ash content: 30.0 %

According to the JSON comment, `MaterialProperties` is not represented by the
released generic schema v3.0.0.

The values are fictional and illustrative.

## Proposed Sustainability Information

The example contains the proposed `Sustainability` structure with:

- virgin-material share: 100.0 %
- mechanically recycled PIR share: 0.0 %
- mechanically recycled PCR share: 0.0 %
- chemically recycled share: 0.0 %
- biocircular share: 0.0 %
- carbon footprint: 2.35 kg CO2eq/kg
- calculation method: illustrative cradle-to-gate calculation
- reference year: 2025
- data quality: fictional example value for schema discussion only

According to the JSON comment, `Sustainability` is not represented by the
released generic schema v3.0.0.

All sustainability values are fictional and illustrative.

## Material Catalog Business Key

The stable business identifier for the material catalog entry is maintained in
`ComponentMaster.BusinessKeys[]`.

The example uses:

- `Name`: `MaterialCatalogId`
- `Value`: `CATALOG-PPGF30-0001`

## Modelling Decisions

The generic material definition is maintained on the `ComponentMaster`.

Concrete supplier products are maintained as entries in
`ComponentMaster.MaterialSources[]`.

The generic material identifier remains in
`ComponentMaster.MaterialIdentifiers[]`. It is not duplicated as a supplier
trade name or as a supplier identifier.

The supplier-specific commercial product name is maintained in
`MaterialSource.TradeName`.

The supplier is maintained in `MaterialSource.Supplier` and is identified by a
DUNS identifier.

Regional availability belongs to the corresponding `MaterialSource` because
availability can differ between supplier products.

The material standard is represented both at the generic material level and in
the concrete material sources. The component-level specification includes the
human-readable title, while the source-level specification identifies the same
standard and product version for each material source.

The catalog-level color definition does not identify the actual color of a
produced component because no `ComponentInstance` is included in this example.

Approval and listing information is intentionally not embedded in the material
catalog entry.

The proposed `MaterialProperties` and `Sustainability` structures are included
as a discussion basis. Their presence makes the complete JSON document a draft
and not a schema-conformant document.

## Source of Truth and References

- The material catalog entry is represented by the `ComponentMaster`.
- The generic material description is maintained in
  `ComponentMaster.MaterialGroup`, `ComponentMaster.MaterialClass` and
  `ComponentMaster.MaterialName`.
- The generic material identity is maintained in
  `ComponentMaster.MaterialIdentifiers[]`.
- The applicable material standard is maintained in
  `ComponentMaster.Specifications[]`.
- The available color definition is maintained in
  `ComponentMaster.Colors[]`.
- The possible supplier-specific material sources are maintained in
  `ComponentMaster.MaterialSources[]`.
- The supplier-specific commercial product name is maintained in
  `MaterialSource.TradeName`.
- The supplier identity is maintained in `MaterialSource.Supplier` and
  `MaterialSource.Supplier.Identification[]`.
- The source-specific material standard is maintained in
  `MaterialSource.Specification`.
- Regional availability is maintained in
  `MaterialSource.AdditionalInformation`.
- The catalog business key is maintained in
  `ComponentMaster.BusinessKeys[]`.
- The proposed material properties are maintained in
  `ComponentMaster.MaterialProperties`.
- The proposed sustainability information is maintained in
  `ComponentMaster.Sustainability`.
- Approval and listing information is not maintained in this material catalog
  entry. It belongs to a separate draft `ApprovalEntry`.

## JSON Example

See the material catalog JSON file in this example folder.

The JSON file contains both a schema-oriented material catalog core and the
proposed `MaterialProperties` and `Sustainability` structures. The complete file
is therefore treated as a draft.

## Validation Status

This example is intentionally not a schema-conformant document.

According to the JSON comment:

- `MaterialProperties` is not represented by the released generic schema
  v3.0.0
- `Sustainability` is not represented by the released generic schema v3.0.0

The remaining structures must still be validated against the referenced
released schema version before productive use.

The JSON file is the technical reference for the actual object paths,
cardinalities, identifiers and values.

## Related Examples

- **Simple Material Definition**  
  Use this example for a minimal material-related `ComponentMaster` without the
  material catalog extensions.

- **Color Definition**  
  Use this example when approved color definitions and the actual color of a
  produced part have to be represented.

- **Multiple Source Material**  
  Use this example when the actual material source used for a produced part has
  to be represented through `ComponentInstance.MaterialSourceID`.

- **Approval Entry Draft**  
  Use this draft example when a formal approval or listing decision has to be
  represented separately from the material catalog entry.

- **Odor Test with Concrete Material Source**  
  Use this draft example when a complete odor test must be linked to a concrete
  supplier material and proposed material-source identifiers.

## Architectural References

- Primary catalog representation: `ComponentMaster`
- Generic material description:
  `ComponentMaster.MaterialGroup`, `ComponentMaster.MaterialClass` and
  `ComponentMaster.MaterialName`
- Generic material identity: `ComponentMaster.MaterialIdentifiers[]`
- Applicable material standard: `ComponentMaster.Specifications[]`
- Available color: `ComponentMaster.Colors[]`
- Possible supplier materials: `ComponentMaster.MaterialSources[]`
- Supplier trade name: `MaterialSource.TradeName`
- Supplier: `MaterialSource.Supplier`
- Source-level material standard: `MaterialSource.Specification`
- Regional availability: `MaterialSource.AdditionalInformation`
- Catalog business key: `ComponentMaster.BusinessKeys[]`
- Proposed material properties: `ComponentMaster.MaterialProperties`
- Proposed sustainability information: `ComponentMaster.Sustainability`
- Separate approval concept: `ApprovalEntry`
- ADR 0001: definition sets are maintained on `ComponentMaster`, while concrete
  assignments are maintained on `ComponentInstance`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
- ADR 0008: the abbreviated material designation is maintained in
  `MaterialClass`
- ADR 0009: material identifiers are typed and stored without uncontrolled
  duplication
- ADR 0010: own identifiers of a concrete `MaterialSource` are proposed and are
  not used in this material catalog JSON
- ADR 0011: `ApprovedForMaterial` is proposed as the link from a separate
  `ApprovalEntry` to the generic material
