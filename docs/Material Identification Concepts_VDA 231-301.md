# Material Identification Concepts (VDA 231-301)

This document clarifies the different material-related identifiers and levels in the
VDA 231-301 data model. It exists because two fundamentally different concepts are easily
confused: the **generic material specification** and the **concrete supplier material**.

---

## The two levels at a glance

| | Material specification (generic) | Material source (concrete) |
|---|---|---|
| **What it is** | "A PP-GF30 according to standard X" — a target profile | "Grade A from supplier Y, plant Z" — a real product |
| **Manufacturer-dependent?** | No (several suppliers may fulfil it) | Yes (exactly one supplier product) |
| **Who owns / assigns it** | The OEM | Exists at the supplier; the OEM lists/approves it |
| **Model location** | `ComponentMaster.MaterialIdentifiers` | `ComponentMaster.MaterialSources` (entries of type `MaterialSource`) |
| **Typical identifier** | OEM material key (e.g. OEM0001 PQW number) | Trade name + supplier + production location (and, if needed, a source id) |

Key point: the generic specification is the **anchor**; the concrete supplier materials **hang
off** it. One generic material can have several approved sources.

---

## Concepts in detail

### 1. OEMMATID — the OEM material identifier (generic, manufacturer-independent)

- `OEMMATID` is the **generic field name** for the internal material key that a given OEM assigns
  to a material specification.
- It identifies the **generic material** (the target profile), not a specific supplier product.
- It is **manufacturer-independent**: several supplier materials can satisfy the same OEMMATID.
- **At OEM0001, the concrete value of the OEMMATID is the PQW number** (from the CAD
  material list).
- Model location: an entry in `ComponentMaster.MaterialIdentifiers` with
  `IdentifierType = "OEMMATID"` (see ADR 0009).

```json
"MaterialIdentifiers": [
  { "IdentifierType": "OEMMATID", "Value": "PQW222ACRR1N" }
]
```

### 2. Norm-defined material number (generic, standard-assigned)

- For metals, a standard assigns a material number (e.g. `1.1302` per EN 10027-2).
- Also an identifier of the **generic material**, but defined by a norm, not by the OEM.
- Model location: another entry in `MaterialIdentifiers` with `IdentifierType = "MaterialNumber"`
  and a `DefiningStandard` (see ADR 0009). Optional; polymers have none.

### 3. MaterialClass — the abbreviated material designation (generic)

- The standardized short name of the material (e.g. `PP-GF30`, `42CrMoS4`), formed per the
  family-specific designation standard (ISO 1043, EN 10027, ...).
- It **describes/designates**, it does not **identify** (many materials share `ABS`).
- Model location: `ComponentMaster.MaterialClass` (see ADR 0008). Not an identifier.

### 4. MaterialName — the human-readable name (generic)

- The spoken-out material name (e.g. `Glass fibre reinforced Polypropylene`).
- Model location: `ComponentMaster.MaterialName`.

### 5. MaterialSource — the concrete supplier material (manufacturer-dependent)

- Represents a **real, approved material source**: a specific supplier product, identified by its
  trade name, its supplier and (optionally) its production location.
- This is the "material database" idea: manufacturer-dependent concrete materials with trade
  names and production sites, hanging off the generic OEMMATID.
- It is **NOT** the OEMMATID. The OEMMATID is the anchor; the MaterialSource is a concrete
  instance approved for that anchor.
- Model location: entries of type `MaterialSource` in `ComponentMaster.MaterialSources`
  (currently a proposed structure, see the multiple-source-material example).
- Typical attributes: `TradeName`, `Supplier`, `MaterialName`, `MaterialClass`, `Specification`,
  and production location (see approval / listing structures).

---

## How they relate

```
ComponentMaster  (generic material specification)
  ├─ MaterialIdentifiers: [
  │     { IdentifierType: "OEMMATID",       Value: "PQW222ACRR1N" },   // manufacturer-independent
  │     { IdentifierType: "MaterialNumber", Value: "1.1302",           // norm-defined (metals)
  │       DefiningStandard: "EN 10027-2" }
  │  ]
  ├─ MaterialClass: "PP-GF30"                        // abbreviated designation (ADR 0008)
  ├─ MaterialName:  "Glass fibre reinforced Polypropylene"
  └─ MaterialSources: [                              // manufacturer-dependent concrete materials
        { TradeName: "...", Supplier: {...}, ProductionLocation: {...} },
        { TradeName: "...", Supplier: {...}, ProductionLocation: {...} }
     ]
```

One OEMMATID (one generic material) may reference several MaterialSources (several approved
supplier products / plants). This is exactly the multiple-source scenario.

---

## Quick disambiguation for the project group

- **OEMMATID / PQW** answers: *Which material (per specification)?* — identity of the target profile.
- **MaterialClass** answers: *What is it called (standardized short name)?* — designation.
- **MaterialSource** answers: *From whom, under which trade name, from which plant?* — identity of
  the real source.

The material-database idea (concrete supplier materials) belongs to the **MaterialSource** level,
not to the OEMMATID.

---

## Related decisions

- ADR 0008 — abbreviated material designation to `MaterialClass`.
- ADR 0009 — typed `MaterialIdentifiers` (OEMMATID, norm-defined numbers), stored once.
- Example: `multiple-source-material` (several approved sources for one material).
