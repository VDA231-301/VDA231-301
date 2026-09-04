# Material characteristics are read out into typed characteristic requirements via a defined classification logic

Status: accepted

## Context and Problem Statement

In VDA 231-300 a material or surface is pinned down not only by its regulation reference and
short name, but also by additional designation parts carried in
`MAT_07_FEATURES_ACCORDING_TO_REGULATION` / `MAT_08_ADDITIONAL_INFORMATION` (and the `SUR`
equivalents).

In the source data these fields contain highly heterogeneous content, for example:

* `+P`, `+QT`, `+C`, `R600` (standardized treatment/condition symbols)
* `PP-GF30`, `PA6-(MD40+GF20)`, `ABS-I`, `CuSn8` (parts of the standardized short name)
* `OEM01 ZONE 1`, `OEM02.02` (cross-references to a further regulation, plus a zone selector)
* `G-MODUL < 1 MPA`, `65 +/- 10 SHORE OO`, `VST 105 +/-5 °C` (quantitative target values)
* `LIGHT DIFFUSING`, `RADAR ABSORBING`, `REDUCED UV-STABILITY` (qualitative functional properties)

These contents determine the exact material, its requirement profile and the test plan derived
from the specification. As an unstructured string they cannot be evaluated by machine.

## Decision Drivers

* The requirement profile (and the resulting test plan) must be derivable by machine.
* VDA 231-300 shall not be changed; all content must remain expressible in `MAT_07`/`MAT_08`.
* Quantitative targets must carry value, unit and tolerance/range so they are comparable.
* Standardized short-name parts stay interpretable only via their designation system.
* Discriminators that select a requirement level (e.g. zone) must be machine-readable.
* The read-out must be reproducible and auditable, including a defined fallback.

## Considered Options

* Keep `MAT_07`/`MAT_08` as a single free-text field (no read-out).
* Split content into ad-hoc fields per material family.
* Classify each characteristic into a fixed type and read it out into existing structures via
  a defined, ordered logic.

## Decision Outcome

Chosen option: "Classify each characteristic into a fixed type and read it out into the existing
structures", because it keeps VDA 231-300 unchanged, reuses the generic characteristic model,
and produces a machine-evaluable requirement profile that can drive the test plan.

Each characteristic token is classified into exactly one of five types:

| Type | Meaning | Examples | Target in VDA 231-301 |
|------|---------|----------|-----------------------|
| A | Abbreviated material designation (MAT_06 short name), formed per the family-specific designation standard | `PP-GF30`, `CuSn8`, `ABS-I`, `42CrMoS4` | `ComponentMaster.MaterialClass` (see ADR 0008), NOT `Specification.Title` |
| B | Standardized treatment / delivery condition | `+P`, `+QT`, `+C`, `R600` | `Specification.FeatureText` / `FeatureList` |
| C | Cross-reference to a further regulation / zone | `OEM01 ZONE 1`, `OEM02.02` | `Specification.FeatureText` / `FeatureList`; the zone selector goes to `CharacteristicRequirements` (see below) |
| D | Quantitative property target (value/tolerance/range) | `G-MODUL < 1 MPA`, `65 +/- 10 SHORE OO`, `VST 105 +/-5 °C` | `CharacteristicRequirements` entry, `ValueType` = `Range` / `NumberWithTolerance` |
| E | Qualitative functional property | `LIGHT DIFFUSING`, `RADAR ABSORBING` | `CharacteristicRequirements` entry, `ValueType` = `Text` / `List` (controlled vocabulary) |

To hold Type D and E, the `Specification` entity carries a relation `CharacteristicRequirements`
(List of `InformationPoint`). Each `InformationPoint` holds `Property`, `ValueType`
(NumberWithTolerance | Range | Text | Number | List), `Value` and `Unit`. This relation is part
of the generic schema v3.0.0; no new base type is introduced.

Zone selectors (`ZONE 1` / `ZONE 2`): the referenced regulation defines the zones and is kept in
`FeatureText`/`FeatureList` (Type C); the actual zone selection is modelled as a
`CharacteristicRequirements` entry (`Property = "Zone"`, `ValueType = "List"`, `Value = "1"`),
because it selects the applicable requirement level and is therefore test-plan relevant.

The applicable designation system for Type A depends on the material family and is defined in
ADR 0008 (ISO 1043 for plastics, ISO 1629 for elastomers, EN 10027-1 for steel names, etc.).

The read-out logic is applied per token in this fixed order (first match wins):

1. Matches a standardized designation symbol (ISO 1043 / EN 10027 / EN 573 / ISO 1629) -> Type A or B.
2. Matches a regulation/zone pattern -> Type C (regulation to `FeatureText`; zone to `CharacteristicRequirements`).
3. Contains number + unit (optionally with operator or tolerance) -> Type D.
4. Otherwise a pure functional term -> Type E (preferably from a controlled list).
5. Remaining, unclassifiable content -> `MAT_08` / `AdditionalInformation`, flagged as "not classified".

For a requirement narrower than the value range of the product standard, the
`CustomizedPropertyOfObjectSpecification` (OriginalValue / DeviationValue) is used instead of a
plain `CharacteristicRequirements` entry.

## Consequences

* Good, because the requirement profile becomes machine-evaluable and can drive the test plan.
* Good, because VDA 231-300 stays unchanged.
* Good, because quantitative targets and zone selectors are typed and comparable.
* Good, because unclassifiable content is preserved and flagged, keeping the read-out auditable.
* Neutral, because the read-out requires maintained lookup tables and a controlled vocabulary
  for Type E functional properties.
* Neutral, because keeping the zone-defining regulation in `FeatureText` (Type C) makes it a
  string; if it must later be machine-resolved, `ReferencedSpecifications` should be used.
* Bad (effort), because the A-vs-D boundary (short-name part vs. quantitative target) needs
  careful rules and good test coverage to avoid misclassification.

## More Information

Related: ADR 0006 (norm aggregation), ADR 0008 (short name to `MaterialClass`; designation
standards), ADR 0005 (self-reference), the parsing rules, and the classified Example Library
(`Beispielsammlung_Merkmale_Ausleselogik_ADR0007.xlsx`).
