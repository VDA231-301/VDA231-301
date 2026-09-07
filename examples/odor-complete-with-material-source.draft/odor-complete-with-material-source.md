# Odor Test with Concrete Material Source (DRAFT)

## Business Scenario

An interior trim component (`Glass fibre reinforced Polypropylene`, short name `PP-GF30`) is
odor-tested according to VDA 270. In this variant, the test report does not only reference the
**generic material** (identified by the OEMMATID; at OEM01 the PEW number), but also the
**concrete supplier material** actually used — including its entry in the material database
(a material-database ID), its trade name and its supplier.

This connects three levels that are otherwise easy to confuse:

1. the **generic material** (manufacturer-independent specification, OEMMATID),
2. the **concrete supplier material** (manufacturer-dependent source, material-database ID,
   trade name, supplier),
3. the **produced part** (which concrete source it was actually made from).

> **Important:** This example is a DRAFT. `MaterialSources`, `MaterialSource.Identifiers` and
> `ComponentInstance.MaterialSourceID` are discussion proposals (ADR 0010) and are **not** part
> of the released VDA 231-301 generic schema v3.0.0. The JSON file is intentionally not
> schema-conformant. All names, values, dates, identifiers, suppliers and locations are
> fictional and fully anonymized.

## Objective

This example demonstrates how a concrete material source and its material-database reference can
be documented alongside a VDA 270 odor test, without duplicating the generic material identity.

## Relevant Entities

### ComponentMaster

The generic definition of the component and its material. It holds the generic material identity
(`MaterialIdentifiers` with `OEMMATID`) and the set of approved concrete sources
(`MaterialSources`).

### MaterialSource

A concrete, manufacturer-dependent material: a specific supplier product with a trade name, a
supplier and its own identifiers (e.g. a material-database ID). It hangs off the generic material
and does not repeat the OEMMATID.

### ComponentInstance

A produced part. It references the concrete material it was actually made from via
`MaterialSourceID` (analogous to how a part references its color via `ColorID`).

## Relevant Attributes

### Generic material (ComponentMaster)

- `ComponentMaster.MaterialGroup`
- `ComponentMaster.MaterialClass`
- `ComponentMaster.MaterialName`
- `ComponentMaster.MaterialIdentifiers` (with `IdentifierType: "OEMMATID"`)

### Concrete material source

- `ComponentMaster.MaterialSources`
- `MaterialSource.MaterialClass`
- `MaterialSource.MaterialName`
- `MaterialSource.TradeName`
- `MaterialSource.Supplier`
- `MaterialSource.Identifiers` (with `IdentifierType: "MaterialDatabaseID"` and
  `IdentifierType: "SupplierMaterialCode"`)
- `MaterialSource.Specification`

### Produced part

- `ComponentInstance.SerialNumber`
- `ComponentInstance.ProductionBatchNumber`
- `ComponentInstance.MaterialSourceID`

## Modelling Decisions

### Two material levels, connected but separate

The generic material and the concrete material source are two different things and are modelled
on two levels:

```json
"MaterialIdentifiers": [
  { "IdentifierType": "OEMMATID", "Value": "OEM111ALAHJD" }
]
```

```json
"MaterialSources": [
  {
    "_id": "b1a00000-1111-4111-8111-000000000001",
    "_type": "MaterialSource",
    "TradeName": "Example PP-GF30 Grade A",
    "Identifiers": [
      { "IdentifierType": "MaterialDatabaseID",   "Value": "MDB-000123" },
      { "IdentifierType": "SupplierMaterialCode", "Value": "SUP-A-PPGF30-GRADEA" }
    ]
  }
]
```

The OEMMATID (generic) stays on the `ComponentMaster` and is **not** duplicated on the source.
The material-database ID (concrete) lives on the `MaterialSource`. This follows the Material
Identification Concepts document and ADR 0010.

### Produced part references the concrete source

The `ComponentInstance` records which concrete source the part was actually made from:

```json
"MaterialSourceID": "b1a00000-1111-4111-8111-000000000001"
```

This makes the produced part traceable to the exact supplier material and its material-database
entry, not only to the generic material.

### Material name and material class

Following ADR 0008, `MaterialClass` carries the abbreviated designation (`PP-GF30`) and
`MaterialName` the spoken-out name (`Glass fibre reinforced Polypropylene`), both on the
`ComponentMaster` and on the `MaterialSource`. `TradeName` remains the supplier's commercial name
and is distinct from both.

### Test data unchanged

The odor test part (target requirement, single results, consolidated value, assessment) is the
same as in the released odor-complete example. Adding the concrete material source does not change
how the test result is modelled.

## JSON Example

See `odor-complete-with-material-source.draft.json`.

## Validation Status

Intentionally **not** schema-conformant. `MaterialSources`, `MaterialSource.Identifiers` and
`ComponentInstance.MaterialSourceID` are discussion proposals (ADR 0010). The field names
`MaterialDatabaseID`, `SupplierMaterialCode` and `MaterialSourceID` are proposals; the released
schema takes precedence.

## Related Examples

- Odor Complete (released fields only, without material source)
- Color Definition (same master/instance reference pattern via `ColorID`)
- Multiple Source Material (several approved sources for one material)
- Approval Entry (approval of a concrete source, linked to the generic material via
  `ApprovedForMaterial`)

## Architectural References

- generic material identity on `ComponentMaster.MaterialIdentifiers` (OEMMATID) — ADR 0009
- concrete source identity on `MaterialSource.Identifiers` (material-database ID) — ADR 0010
- produced part references the source via `ComponentInstance.MaterialSourceID`
- abbreviated designation in `MaterialClass` — ADR 0008
- Material Identification Concepts document (generic vs. concrete material levels)
