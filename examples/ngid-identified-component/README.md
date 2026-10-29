# NGID-identified component

This example shows how a `ComponentMaster` is linked to its occurrence in a
source CAD assembly structure using an `NGIDPath`, following the Siemens NGID
specification.

## Business scenario

A component (here an interior trim part) exists in a CAD assembly. To trace the
component back to its exact position in the source assembly structure, the
`ComponentMaster` carries an `NGIDPath` that encodes the path from the assembly
root down to the specific part occurrence.

File: `componentMaster-with-ngid.json`

## Relevant Attributes

This example focuses on the following attributes:

- `NGIDPath` – locates the component within the source CAD assembly structure.
  It uses the `JT_PROP_NAME` identifier with CADID-formatted node values in the
  form `name.type;version;instanceId` (see ADR-0004).
- `MaterialGroup` – the classification group (here `Thermoplast`).
- `MaterialClass` – the abbreviated material designation (`PP-GF30`), per
  ADR-0008.
- `MaterialName` – the readable material name (`Glass fibre reinforced
  Polypropylene`).
- `MaterialIdentifiers` – the typed material identifier(s); here an `OEMMATID`
  entry, per ADR-0009.
- `Version` – the mandatory drawing / change status (ZGS), included in every
  component example, per ADR-0002.
- `Designation` / `SupplierPartNumber` – human-readable name and supplier part
  number of the component.

## Understanding the NGIDPath

The `NGIDPath` in this example is:

```
$$NGID<chain>="JT_PROP_NAME"\0DoorAssembly.asm;0;2:\0DoorTrim.part;0;1:\0\0
```

It reads as a chain of nodes from the assembly root to the target part:

- `DoorAssembly.asm;0;2` – the assembly node (name `DoorAssembly`, type `.asm`,
  version `0`, instance `2`).
- `DoorTrim.part;0;1` – the part node (name `DoorTrim`, type `.part`, version
  `0`, instance `1`).

Each node value follows the CADID format `name.type;version;instanceId`. The
`JT_PROP_NAME` identifier declares which property carries the node names.

## Modelling decisions

- The link to the CAD structure is expressed via `NGIDPath` on the
  `ComponentMaster`, not by duplicating the assembly structure itself.
- The path is a single, machine-readable string following the NGID / CADID
  conventions, so it can be parsed and resolved by downstream systems.
- Material identity follows the shared conventions: abbreviated designation in
  `MaterialClass` (ADR-0008), typed identifiers in `MaterialIdentifiers`
  (ADR-0009).

## Validation status

Aligned with generic schema v3.0.0.

## Related ADRs

- [ADR-0002: ComponentMaster version mandatory](../../docs/adr/0002-componentmaster-version-mandatory.md)
- [ADR-0004: NGID path representation](../../docs/adr/0004-ngid-path-representation.md)
- [ADR-0008: Abbreviated material designation to MaterialClass](../../docs/adr/0008-abbreviated-material-designation-to-materialclass.md)
- [ADR-0009: Typed material identifiers, no duplication](../../docs/adr/0009-typed-material-identifiers-no-duplication.md)
