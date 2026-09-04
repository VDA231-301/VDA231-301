# Identifiers are typed and stored once; norm-defined numbers are bound to their norm by reference

Status: accepted

## Context and Problem Statement

A material is designated by several identifiers of different provenance: the internal OEM
material identifier (VDA 231-300 `MAT_01`, here typed as `OEMMATID`) and, for metals, a
norm-defined material number ("Werkstoffnummer", e.g. `1.1302`, `1.8159`) defined by EN 10027-2. 
The material number is not present in the current data model; it exists only inside the standard and, in the CAD material
list, is associated with the material via the `MAT_01` row.

The current `MaterialIdentifiers` is an untyped `array of String`, so consumers cannot tell
whether an entry is an internal OEM key, a material number, or something else. Moreover, the same number
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
  { "IdentifierType": "QEMMATID", "Value": "OEM123ABCR3N" },
  { "IdentifierType": "MaterialNumber", "Value": "1.1302",
    "DefiningStandard": "EN 10027-2" }
]
```

Single source of truth: the identifier value is owned by the material (PLM) and stored exactly
once, here. The `Specification` (e.g. DIN EN 10267) does NOT repeat the number. The fact that a
number is defined/assigned by a norm is expressed as a reference (`DefiningStandard`, and
optionally a pointer to the relevant `Specification`), not as a second copy of the value.

Where a flat export (drawing / JT) cannot carry a reference and the value must physically appear
in two places, the second occurrence is a derived copy, marked as derived and constrained by a
validation rule `derived == source`; it is never independently editable. Two freely editable
fields holding the same value are not allowed.

Ownership split between the norm world and PLM:

* PLM owns the identity (the concrete material IS `1.1302` / this OEMMATID) -> the value lives in
  `MaterialIdentifiers`.
* The norm world owns definitions (EN 10027-2 defines the number system; the product standard
  assigns the number) -> expressed via `Specification` and the `DefiningStandard` reference.

The `OemIdentifier` field on the `ComponentMaster` continues to state the owner of the
identifiers (e.g. which OEM the SRM keys refer to); the typed entries do not repeat this per
item unless an entry has a different owner.

## Consequences

* Good, because every identifier is self-describing (type + provenance) and the metal material
  number finally has a defined, optional home.
* Good, because the value exists exactly once; the norm binding is a reference, so no drift
  between PLM and the norm world is possible.
* Good, because the reference enables later validation (does `1.1302` really belong to this
  material per EN 10027?), which a plain copy could never support.
* Neutral, because there is a slight asymmetry: the short name goes to `MaterialClass` (ADR 0008)
  while numbers/keys go to `MaterialIdentifiers`.
* Bad (breaking), because changing `MaterialIdentifiers` from `array of String` to a typed object
  list is not backward-compatible; it requires a schema change, a PR and a migration note.

## More Information

Related: ADR 0006 (norm aggregation; `MAT_01` not part of `Specification`), ADR 0008 (short name
to `MaterialClass`). Standards: EN 10027-1 (steel names), EN 10027-2 (steel numbers). The field
names `IdentifierType` / `DefiningStandard` are proposals; the released schema takes precedence.
