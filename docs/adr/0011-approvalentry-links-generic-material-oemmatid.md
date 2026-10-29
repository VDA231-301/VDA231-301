# ApprovalEntry links to the generic material via OEMMATID by reference (ApprovedForMaterial)

Status: proposed

## Context and Problem Statement

An `ApprovalEntry` (approval / listing) documents that a concrete supplier material
(a `MaterialSource`, described in its `Subject`: trade name, supplier, production site) is
approved. In practice it is necessary to know **for which generic material** this concrete source
is approved, i.e. the manufacturer-independent material specification identified by the OEMMATID
(at OEM01 the PEW number).

Today the `ApprovalEntry` carries the concrete source (`Subject`, `SubjectMaterialSourceID`) but
has no explicit link to the generic material. Without it, an approval cannot be related back to
the generic material it belongs to, which is required in practice (e.g. "which supplier sources
are approved for QEV X?").

## Decision Drivers

* An approval must be relatable to the generic material (OEMMATID / QEV) it approves a source for.
* The two material levels (generic specification vs. concrete source) must stay separate
  (see the Material Identification Concepts document and ADR 0010).
* An `ApprovalEntry` often travels independently between OEM and supplier, without the
  `ComponentMaster` in the same document; the link must work by reference, not by containment.
* The value must not be duplicated in an independently editable way (single source of truth,
  ADR 0009).

## Considered Options

* Do not link the approval to the generic material (rely on the concrete source only).
* Put an OEMMATID onto the `Subject` (concrete-source level).
* Add an explicit reference from the `ApprovalEntry` to the generic material via its OEMMATID.

## Decision Outcome

Chosen option: "Add an explicit reference from the `ApprovalEntry` to the generic material via its
OEMMATID."

The `ApprovalEntry` carries a field `ApprovedForMaterial` that references the generic material by
its OEMMATID business key (not by copying editable fields, and not on the concrete-source
`Subject`):

```json
"ApprovedForMaterial": {
  "IdentifierType": "OEMMATID",
  "Value": "OEM111ALAHJD"
}
```

Level separation is preserved:

* `ApprovedForMaterial` points to the generic material (OEMMATID / PEW, `ComponentMaster` level).
* `Subject` continues to describe the concrete supplier material (trade name, supplier, plant).

The reference uses the OEMMATID value as the business key, consistent with the single-source-of-
truth principle (ADR 0009): the OEMMATID value is owned by the generic material; the
`ApprovalEntry` only references it.

The field name `ApprovedForMaterial` is a first proposal and may change during the ApprovalEntry
work (Issue #37).

## Consequences

* Good, because an approval can be related to the generic material it approves a source for,
  which is needed in practice.
* Good, because the generic and concrete material levels stay clearly separated.
* Good, because the link is a reference (business key), so no editable value is duplicated and the
  approval can travel without the `ComponentMaster`.
* Neutral, because a resolving system must look up the referenced OEMMATID to obtain the full
  generic material.
* Neutral, because `ApprovalEntry` is still a discussion structure (not part of the released
  generic schema v3.0.0); this field is adopted as part of that ongoing work.

## More Information

Related: ADR 0009 (typed identifiers, single source of truth; OEMMATID on the `ComponentMaster`),
ADR 0010 (typed identifiers on `MaterialSource`), the Material Identification Concepts document,
and Issue #37 (ApprovalEntry). The field name `ApprovedForMaterial` is a first proposal; the
released schema takes precedence.
