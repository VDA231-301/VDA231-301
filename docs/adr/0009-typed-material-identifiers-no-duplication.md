# Identifiers are typed and stored once; norm-defined numbers are bound to their norm by reference

Status: accepted

## Context and Problem Statement

A material is designated by several identifiers of different provenance: the internal SRM
identifier (VDA 231-300 `MAT_01`) and, for metals, a norm-defined material number
("Werkstoffnummer", e.g. `1.1302`, `1.8159`) defined by EN 10027-2. The material number is not
present in the current data model; it exists only inside the standard and, in the CAD material
list, is associated with the material via the `MAT_01` row.

The current `MaterialIdentifiers` is an untyped `array of String`, so consumers cannot tell
whether an entry is an SRM key, a material number, or something else. Moreover, the same number
could be documented both as an identifier and inside the `Specification`, raising the question
how to avoid contradictory duplicates between the "norm world" and PLM.

## Decision Drivers

* Every identifier must be attributable to its type and provenance (internal vs. norm-defined).
* The metal material number needs a defined home; it must be optional (polymers have none).
* A value must have a single source of truth; the same value must not live in two independently
  editable places.
* The relationship "this number is defined by norm X" must be machine-readable.
* Materials without a norm number (e.g. plastics) must not require empty or dummy fields.

## Considered Options

* Keep `MaterialIdentifiers` as an untyped `array of String`.
* Store the material number inside the `Specification` (e.g. as an `ObjectNumber`).
* Store the material number as a characteristic requirement.
* Make `MaterialIdentifiers` a typed list; hold the value once and bind it to its defining norm
  by reference.

## Decision Outcome

Chosen option: "Typed `MaterialIdentifiers`; value stored once; norm binding by reference."

`MaterialIdentifiers` becomes a list of typed identifier objects. Each entry carries at least an
`IdentifierType` and a `Value`; norm-defined identifiers additionally carry the defining
standard:

```json
"MaterialIdentifiers": [
  { "IdentifierType": "SRM", "Value": "OEM123ABCR3N" },
  { "IdentifierType": "MaterialNumber", "Value": "1.1302",
    "DefiningStandard": "EN 10027-2" }
]
