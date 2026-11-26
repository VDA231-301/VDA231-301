# Material identification

The [toggle-clamp bearing pin](../examples/clamp/README.md) illustrates four fields on `EngineeringMaterial`.

| Field | Bearing-pin value | Meaning |
|-------|-------------------|---------|
| `MaterialSpecificationIdentifier` | `MAT 123456` (type `OEMMATID`) | OEM specification key from `MAT_01` |
| `MaterialGroup` | `Steel` | Broad material group |
| `MaterialClass` | `Stainless steel` | Descriptive category |
| `MaterialName` | `1.4301-X5CrNi18-10` | Material number `1.4301` and short designation `X5CrNi18-10` from `MAT_06_SHORT_NAME` |

A component assignment references the engineering material's `_id` through `EngineeringMaterialID`.
Several supplier products can meet the same material specification. Each product is a `MaterialSource`
and can carry a `TradeName` and its own `MaterialIdentifiers`. On a component instance,
`MaterialSourceID` references the sources actually used.
