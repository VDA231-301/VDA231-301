# Map the abbreviated material designation to EngineeringMaterial.MaterialName

Status: accepted

## Context and Problem Statement

VDA 231-300 supplies the abbreviated material designation (Werkstoffkurzbezeichnung)
in `MAT_06_SHORT_NAME`. The earlier ComponentMaster-based model mapped this value
to `MaterialClass` and proposed the same mapping for a referenced material source.
Several grades belong to the class `Stainless steel`, while the short name
`X5CrNi18-10` designates a particular grade within that class.

## Decision Outcome

Map `MAT_06_SHORT_NAME` to `EngineeringMaterial.MaterialName`. The short name
can stand alone. When the source also provides a material number, the name may
combine the number and the short name.

The three required fields on `EngineeringMaterial` have distinct meanings.
The bearing pin in the [toggle-clamp example](../../examples/clamp/README.md)
illustrates all three.

| Field | Meaning | Bearing-pin material |
|-------|---------|----------------------|
| `MaterialGroup` | Broad classification group, for example according to VDA 231-106 | `Steel` |
| `MaterialClass` | Descriptive category within the group | `Stainless steel` |
| `MaterialName` | Specific material designation | `1.4301-X5CrNi18-10` |

In this example, `X5CrNi18-10` comes from `MAT_06_SHORT_NAME` and `1.4301`
comes from `MAT_08_ADDITIONAL INFORMATION`, which contains only the material
number for the bearing pin. The group and class are descriptive labels supplied
in the example. The [CR5 example](../../examples/engineering-material/engineering-material.json)
shows a short name used on its own, with `MaterialClass` set to `Low-carbon steel`
and `MaterialName` set to `CR5`.

## Consequences

* When migrating an older record that used `MaterialClass` for the short name,
  carry the designation into `EngineeringMaterial.MaterialName` and supply the
  descriptive class separately.
* Several material definitions can share a designation. A component assignment
  references the definition by `EngineeringMaterialID`. Its optional
  `MaterialName` is a readable copy of the referenced name.
* `MaterialSpecificationIdentifier` carries the material specification key
  (for example the OEM key from `MAT_01`). `Specification.Title` carries the
  title of the specification. A supplier's commercial product name belongs in
  `MaterialSource.TradeName`.

## Designation standards

The short name follows the designation system of its material family.

| Material family | Designation standard | Examples |
|-----------------|----------------------|----------|
| Plastics | ISO 1043-1 (basic polymers), ISO 1043-2 (fillers and reinforcements), ISO 1043-3/-4 (plasticizers and flame retardants) | `ABS`, `PP-GF30` |
| Rubber and elastomers | ISO 1629 | `FKM`, `VMQ`, `EPDM` |
| Thermoplastic elastomers | ISO 18064 | `TPE-O`, `TPE-U` |
| Steel | EN 10027-1 | `X5CrNi18-10`, `42CrMoS4` |
| Aluminium | EN 573 series | `AlMg2Mn0,8` |
| Copper and copper alloys | EN chemical-symbol designations | `CuSn8`, `CuZn37Mn3Al2PbSi` |
| Japanese steels | JIS designation standards | `SCr420H` |
