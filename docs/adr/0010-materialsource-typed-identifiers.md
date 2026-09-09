# MaterialSource carries its own typed identifiers (concrete-material level), reusing the ADR 0009 pattern

Status: proposed

## Context and Problem Statement

The data model distinguishes two levels of "material": the generic material specification
(manufacturer-independent), identified on the `ComponentMaster` via `MaterialIdentifiers`
(e.g. `OEMMATID` = Mercedes-Benz QEV number), and the concrete supplier material
(manufacturer-dependent), represented as a `MaterialSource` (trade name, supplier, production
location).

A concrete supplier material is typically also registered in a material database with its own
identifier (a material-database ID, and possibly a supplier material code). Currently a
`MaterialSource` has no defined, typed place for such an identifier. `SubjectMaterialSourceID`
seen in approval/listing drafts is a **reference to** a `MaterialSource`, not the source's own
business identifier.

The question arose where the identifier of a concrete supplier material belongs, and whether it
should reuse the identifier structure already decided for the `ComponentMaster` (ADR 0009).

## Decision Drivers

* A concrete supplier material must be traceable to its material-database entry (conformity
  checks, complaint handling, traceability).
* The generic OEMMATID (on the `ComponentMaster`) and the concrete-source identifier are on two
  different levels and must not be conflated.
* The identifier pattern should be uniform across the model, so consumers use one mechanism.
* Not every source records a database ID; the field must be optional and allow several
  identifiers of different provenance.

## Considered Options

* Keep concrete-source identifiers out of the model (rely on trade name + supplier only).
* Reuse `SubjectMaterialSourceID` as the source's identifier.
* Store a single untyped identifier string on `MaterialSource`.
* Add a typed identifier list on `MaterialSource`, reusing the `Generic.MaterialIdentifier` type
  from ADR 0009.

## Decision Outcome

Chosen option: "Typed identifier list on `MaterialSource`, reusing the ADR 0009 type", because it
gives the concrete supplier material a defined, optional home for its identifiers and keeps the
identifier mechanism uniform across `ComponentMaster` and `MaterialSource`.

`MaterialSource` carries an `Identifiers` list of `Generic.MaterialIdentifier` objects. Each entry
holds an `IdentifierType` and a `Value` (and, where applicable, a `DefiningStandard`), exactly as
on the `ComponentMaster`:

```json
"Identifiers": [
  { "IdentifierType": "MaterialDatabaseID",   "Value": "MDB-000123" },
  { "IdentifierType": "SupplierMaterialCode", "Value": "SUP-A-PPGF30-GRADEA" }
]
```

Level separation is explicit:

* The generic OEMMATID / QEV stays on `ComponentMaster.MaterialIdentifiers` (ADR 0009) and is NOT
  duplicated on the source.
* The concrete-source identifiers (material-database ID, supplier material code) live on
  `MaterialSource.Identifiers`.
* `SubjectMaterialSourceID` remains a reference to a `MaterialSource`, not an identifier of it.

Suggested initial `IdentifierType` values for sources: `MaterialDatabaseID`, `SupplierMaterialCode`.
The value is stored once; where a database ID is defined by an external registry, the optional
`DefiningStandard` field captures that registry (single-source-of-truth principle from ADR 0009).

## Consequences

* Good, because a concrete supplier material can be traced to its material-database entry.
* Good, because the identifier pattern is uniform across `ComponentMaster` and `MaterialSource`
  (one type, one mechanism), which is easy to explain and to implement.
* Good, because the two material levels stay clearly separated (generic vs. concrete), avoiding
  the frequent OEMMATID-vs-MaterialSource confusion.
* Neutral, because it is an additive change on `MaterialSource`; sources without `Identifiers`
  remain valid.
* Neutral, because the controlled list of source `IdentifierType` values must be maintained.

## More Information

Related: ADR 0009 (typed `MaterialIdentifiers`; `Generic.MaterialIdentifier`), ADR 0008
(abbreviated designation to `MaterialClass`, incl. its scope on `MaterialSource`), the Material
Identification Concepts document (two-level distinction), and the `multiple-source-material`
example. Field name `Identifiers` and the `IdentifierType` values are proposals; the released
schema takes precedence.
