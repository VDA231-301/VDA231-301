# Norm information is aggregated into one embedded Specification entity per material/surface

Status: accepted

## Context and Problem Statement

VDA 231-300 describes a regulation reference (for a material or a surface) as a set of
individual, flat JT attributes: regulation type (`MAT_02`/`SUR_02`), regulation number
(`MAT_03`/`SUR_03`), legal authority (`MAT_04`/`SUR_04`), issue date (`MAT_05`/`SUR_05`),
short name (`MAT_06`/`SUR_06`), features according to the regulation (`MAT_07`/`SUR_07`)
and further applicable regulations (`MAT_11`/`SUR_11`).

In the source systems these values are not stored field by field: the CAD material list
(and the surface database) keep the regulation as a **combined string** in a single column,
e.g. `DIN EN 10263-4` or `OEMSPEC 4104.00`. The issue date and legal authority are usually
not present in these lists at all.

The question arose how this normative information should be represented in the generic
schema v3.0.0: as flat attributes mirroring the JT fields, or aggregated into a dedicated
structure, and where the parsing/derivation of the combined string should happen.

## Decision Drivers

* One material or surface can reference several regulations (a basic standard plus further
  applicable ones, `MAT_11`/`SUR_11`), so the model must support multiplicity.
* The regulation reference must stay machine-readable and queryable (type, number, subnumber),
  not a free-text blob, so downstream systems can resolve and validate it.
* The mapping from a combined source string to the individual fields must be reproducible and
  documented (see parsing rules), not implicit.
* Mandatory VDA 231-300 fields (`_04` authority, `_05` issue date) must have a defined target.
* Definitions should not be duplicated; the same pattern must work for materials and surfaces.

## Considered Options

* Keep the flat JT attributes one-to-one as individual fields on `ComponentMaster`.
* Store the regulation reference as a single free-text string (as in the source list).
* Aggregate all regulation fields into one embedded `Specification` entity and reference it
  from `ComponentMaster` (list of specifications), populated via defined parsing rules.

## Decision Outcome

Chosen option: "Aggregate the norm information into one embedded `Specification` entity per
material/surface", because it is the only option that keeps the reference machine-readable,
supports several regulations per material/surface, and reuses one consistent structure for
both materials and surfaces.

The generic schema v3.0.0 provides the `Specification` entity
(`Type`, `Number`, `Subnumber`, `IssueDate`, `Title`, `FeatureText`, `FeatureList`, `DOI`,
`ReferencedSpecifications`). Norm information is aggregated as follows:

* `MAT_02`/`SUR_02` (regulation type)    -> `Specification.Type`
* `MAT_03`/`SUR_03` (regulation number)  -> `Specification.Number` (+ `Subnumber`)
* `MAT_05`/`SUR_05` (issue date)         -> `Specification.IssueDate`
* `MAT_06`/`SUR_06` (short name)          -> `Specification.Title`
* `MAT_07`/`SUR_07` (features)            -> `Specification.FeatureText` / `FeatureList`
* `MAT_11`/`SUR_11` (further regulations) -> `Specification.ReferencedSpecifications`

The split of the combined source string into `Type` / `Number` / `Subnumber` follows the
documented parsing rules (longest-known-prefix match; `.` = internal execution/issue status,
`-` = part of a DIN/EN standard). The issue date (`_05`) maps directly to the mandatory
`Specification.IssueDate` field.

The legal authority (`_04`) is **not** stored as its own field: it is a function of the
regulation type (`DIN` -> DIN e.V., `DIN EN` -> DIN e.V./CEN, `ISO` -> ISO, ...) and is
derived via a maintained lookup table. This keeps the reference lossless while avoiding a
redundant, denormalized attribute.

The pattern shall be applied consistently: any regulation-like reference (material or surface)
is aggregated into `Specification`, and a material/surface that cites several regul
