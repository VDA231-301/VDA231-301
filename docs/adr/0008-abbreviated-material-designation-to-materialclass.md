# The abbreviated material designation is mapped to MaterialClass (ComponentMaster and MaterialSource)

Status: accepted

## Context and Problem Statement

VDA 231-300 carries the abbreviated material designation ("Werkstoffkurzbezeichnung",
`MAT_06_SHORT_NAME`), e.g. `ABS`, `ABS-I`, `PP-GF30`, `42CrMoS4`, `CuZn37Mn3Al2PbSi`,
`AlMg2Mn0,8`. In the CAD material list this is a dedicated column ("Werkstoffkurzbezeichnung").

This designation is not the title of the norm, and it is not a unique key: many different
materials (with different identifiers) share the same short designation (e.g. several materials
named `ABS`). It therefore does not belong to `Specification.Title` and is not, on its own, an
identifier.

The abbreviated designation is needed not only on the `ComponentMaster` (the material being
described) but also wherever a material is referenced as a source, e.g. in a `Subject` /
`MaterialSource` structure (approval / listing / multiple-source scenarios). A single, consistent
target field is required across these places.

## Decision Drivers

* The abbreviated designation must have exactly one defined target field, used consistently
  wherever a material is described or referenced (component master and material source).
* The same field must carry both coarse (`ABS`) and fine (`CuZn37Mn3Al2PbSi`) designations.
* The field definition must reference the family-specific designation standards so the value
  stays interpretable.
* `Specification.Title` must remain reserved for the norm's own title.
* Identifiers (internal OEM key, material number, see ADR 0009) must not be conflated with the
  designation, nor with the commercial `TradeName`.

## Considered Options

* Map the abbreviated designation to `Specification.Title`.
* Map it to `MaterialIdentifiers`.
* Map it to `MaterialName`.
* Map it to `MaterialClass`, and use the same field on both `ComponentMaster` and
  `Subject`/`MaterialSource`.

## Decision Outcome

Chosen option: "Map the abbreviated material designation (`MAT_06_SHORT_NAME`) to `MaterialClass`,
consistently on `ComponentMaster` and on `Subject`/`MaterialSource`".

The field `MaterialClass` is hereby defined to contain exactly the abbreviated material
designation as carried in VDA 231-300 `MAT_06_SHORT_NAME`. It applies wherever a material is
described or referenced:

* `ComponentMaster.MaterialClass` — the material being described.
* `Subject.MaterialClass` / `MaterialSource.MaterialClass` — a referenced/approved material
  source (approval, listing, multiple-source scenarios).

The previous reference to VDA 231-200 on this field is removed: the content of `MaterialClass`
is defined by this ADR, not by VDA 231-200.

The abbreviated designation is formed according to a family-specific designation standard:

| Material family | Designation standard | Examples |
|-----------------|----------------------|----------|
| Plastics - basic polymers | ISO 1043-1 | `ABS`, `PP`, `PC`, `PMMA`, `PA6` |
| Plastics - fillers / reinforcements | ISO 1043-2 | `GF30`, `MD40` (in `PP-GF30`, `PA6-(MD40+GF20)`) |
| Plastics - plasticizers / flame retardants | ISO 1043-3 / ISO 1043-4 | additive symbols |
| Rubber / elastomers | ISO 1629 | `FKM`, `VMQ`, `EPDM` |
| Thermoplastic elastomers (TPE) | ISO 18064 | `TPE-O`, `TPE-U` |
| Steel - names (Kurznamen) | EN 10027-1 | `42CrMoS4`, `X46Cr13`, `10B21` |
| Aluminium | EN 573 (-1..-4) | `AlMg2Mn0,8`, `EN AW-...` |
| Copper and copper alloys | chemical symbol per EN; numbers per EN 1412 | `CuSn8`, `CuZn37Mn3Al2PbSi`, `CW453K` |
| Japanese steels (special case) | JIS (e.g. JIS G 4053) | `SCr420H` |

Distinction from neighbouring fields:

* `MaterialGroup` (VDA 231-106) holds the classification group (e.g. steel, thermoplast).
* `MaterialName` holds the descriptive, human-readable material name
  (e.g. "Glass fibre reinforced Polypropylene").
* `MaterialIdentifiers` holds the identifying keys (internal OEM key, and norm-defined numbers
  such as the steel material number per EN 10027-2); see ADR 0009.
* `TradeName` (on a material source) holds the commercial product name of a specific supplier
  grade; it is not the abbreviated designation.
* `Specification.Title` holds the title of the norm.
* `MaterialClass` holds the abbreviated material designation as defined here.

## Consequences

* Good, because the abbreviated designation has one defined target that works for both coarse
  and fine values, and is identical on `ComponentMaster` and `MaterialSource`.
* Good, because the designation standards are named explicitly, so the value stays interpretable
  and parseable per family (the family is available via `MaterialGroup`).
* Good, because `MaterialName`, `TradeName`, `MaterialIdentifiers` and `Specification.Title` keep
  clean, non-overlapping semantics.
* Neutral, because `MaterialClass` no longer refers to VDA 231-200; its content is defined solely
  by this ADR. Consuming systems that expected a VDA 231-200 classification here must be adjusted.
* Neutral, because adding `MaterialClass` to `Subject`/`MaterialSource` is a schema addition on
  those structures; where they are still discussion drafts (e.g. approval entries), the field is
  adopted as part of that ongoing work.

## More Information

Related: ADR 0006 (norm aggregation; `MAT_06` therefore not on `Specification.Title`), ADR 0007
(Type A short-name parts), ADR 0009 (identifiers). Designation standards: ISO 1043-1/-2/-3/-4,
ISO 1629, ISO 18064, EN 10027-1, EN 573, EN 1412, JIS.
