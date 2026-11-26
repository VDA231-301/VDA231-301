# Toggle Clamp: component hierarchy and material tests

This example shows how to describe a toggle-clamp assembly, link its component
occurrences to CAD data, and associate physical test items with tensile and
hardness tests using VDA 231-301. Names, orders, laboratory details and results
are illustrative data, not a certified test report.

## Files

| File | Role |
|---|---|
| [VDA_231-301_ToggleClamp_SubComponents.example.json](VDA_231-301_ToggleClamp_SubComponents.example.json) | VDA 231-301 testing project with component hierarchy, specimens and test results. |
| [Toggle_Clamp__VDA+all_CAD_.jt](Toggle_Clamp__VDA+all_CAD_.jt) | Binary JT model. |
| [Toggle_Clamp__VDA+all_CAD_.ajt](Toggle_Clamp__VDA+all_CAD_.ajt) | ASCII DirectModel export with assembly occurrence properties. |
| [Toggle_Clamp__VDA+all_CAD_.xml](Toggle_Clamp__VDA+all_CAD_.xml) | JT information report with geometry-node and material properties. |
| [Toggle_Clamp__VDA+all_CAD__properties.csv](Toggle_Clamp__VDA+all_CAD__properties.csv) | Sectioned property export. |
| [validate.py](validate.py) | Local schema and consistency checks. |

## Schema and validation

The example declares `_schemaVersion: "3.0.0"`. The validator checks it against
the [JSON schema in this repository](../../main/VDA_231-301_Schema_Generic.json).

Run from the repository root with Python installed:

```sh
python -m pip install jsonschema==4.26.0
python examples/clamp/validate.py
```

The validator checks:

- Structure and formats defined by the schema (JSON Schema 2020-12).
- Unique UUID v4 identifiers and internal references to the expected object types.
- Topic, specimen and component-instance relationships, execution counts and
  result-table widths.
- Unique CAD occurrence paths, assembly chains in the ASCII JT export, and
  body and material tokens in the XML report.

It also reports whether the XML is well-formed. It does not validate JT geometry
or conformance, resolve NGIDs in a JT viewer, or certify engineering results.

## Component hierarchy

`ComponentMasters` contains one root component. Its `SubComponents` recursively
describe the assembly:

```text
Toggle Clamp
  Bearing Pin (2 root occurrences)
  Clamping Arm Assembly
    Forked Clamping Arm
    Clamping Screw Assembly
      Screw
      Rubber Thrust Pad
    Screw Holder Assembly (2 occurrences)
      Flanged Washer (one per holder)
      Hexagon Nut (one per holder)
  Lever Bar
    Steel body
    Hand Grip
  Toggle Lever
  Mounting Base Assembly
    Base Bracket (2 occurrences)
    Bearing Pin (2 occurrences)
```

The example contains 23 component masters and 22 distinct occurrence paths; the
root has no occurrence path. Repeated CAD occurrences have separate
component-master IDs and paths, even when their supplier part numbers match.
This structure models assembly occurrences rather than a normalized part catalog.

`Instances` separately identifies three physical test items: `FCA-001`,
`FCA-002` and `BP-001`.

## Tests and specimens

`Topics` contains two objects of type `TestSeries`:

- The tensile topic refers to the forked clamping arm and contains two executions
  with separate specimens.
- The hardness topic refers to the first bearing pin and lists the other three
  pin occurrences in `AlsoApplicableComponentMasterIDs`. It contains one
  execution with three raw indentation values. Applicability does not mean
  that each occurrence was tested.

Each topic owns its `Specimens`. Executions reference them through `SpecimenID`,
and each specimen references a physical component instance through
`ComponentInstanceID`. `ReportedProperties` contains consolidated result tables.

## Identifiers and materials

The top-level `EngineeringMaterials` collection defines each material's name,
classification and requirements. Components reference these definitions through
`MaterialAssignments[].EngineeringMaterialID`.

`_id` is the stable internal transmission identifier. `ComponentMasterID`,
`ComponentInstanceID`, `SpecimenID`, `TestingCenterID` and other reference fields
resolve to objects of the corresponding types within the JSON file. These IDs
are independent of CAD node IDs and supplier part numbers.

`MaterialSpecificationIdentifier` maps the CAD property `MAT_01_SPECIFICATION_IDENTIFIER`
to a typed identifier:

```json
{ "IdentifierType": "OEMMATID", "Value": "SDR 221100" }
```

The source property determines this mapping, regardless of the value's prefix;
no norm-defined material number is inferred. `OemIdentifier` is `MB`.
`MaterialClass` holds the descriptive material category; `MaterialName` holds
the specific material designation. For the bearing-pin material:

```json
"MaterialGroup": "Steel",
"MaterialClass": "Stainless steel",
"MaterialName": "1.4301-X5CrNi18-10"
```

`MaterialName` uses the CAD property `MAT_06_SHORT_NAME`. Where
`MAT_08_ADDITIONAL INFORMATION` contains only a material number, the number is
prepended with a hyphen. Both `1.4301` and `X5CrNi18-10` occur in the source.
Other additional-information text is not treated as a material number. The nuts
retain the source designation `19MnB4 Mutter FK 8` as their `MaterialName` and
use `Steel for fasteners` as their `MaterialClass`.

Every engineering material supplies the required `MaterialGroup`, `MaterialClass`
and `MaterialName`. Group and category labels are illustrative descriptions,
not validated VDA classification codes or verbatim classifications supplied by
the CAD export. The source-token check validates the specific material name,
not the descriptive class label.

Each `MaterialAssignments` entry also includes the referenced material's
`MaterialName` for readability. This optional label repeats the definition's name;
`EngineeringMaterialID` remains the reference to the material definition.

## Multiple material sources and colors

The forked clamping arm's engineering material (`AISI 1008`) lists two supplier
products and two colors. Each tested instance records its supplier product in the
`MaterialSourceID` array and its color in `ColorID`.

| Instance serial number | Material source | Color |
|---|---|---|
| FCA-001 | Example clamping-arm sheet A, supplier A plant | Example grey (GREY) |
| FCA-002 | Example clamping-arm sheet B, supplier B plant | Example black (BLACK) |

Both instances use the same component and engineering material definitions.
Supplier sources and colors are illustrative additions, not taken from the CAD
exports or laboratory records. The two selections demonstrate instance traceability;
they do not limit which source/color combinations can be used.

## CAD occurrence paths

`NGIDPath` contains chains using `__CAD_INST_UID` and literal `\0` delimiters
(escaped as `\\0` in JSON). The ASCII export includes assembly occurrence
properties such as `Bearing_Pin.asm;54;492:`. The validator checks assembly
segments in their parent context and matches `.part` segments against XML
name, version and ID tokens.

These paths are **source-derived candidates, not verified viewer-resolvable
NGIDs**. Assembly occurrences expose `__CAD_INST_UID`, while body nodes expose
`__CAD_STABLE_BODY_UID`; matching the exported tokens does not prove that a JT
consumer can resolve the complete chain. Confirm the identifier strategy with
a JT consumer before using this example as an NGID interoperability reference.
Body ID `7046` occurs for two different parts, so a body ID alone does not
identify a unique occurrence.

## Source-data limitations

- `MAT 123456` describes both bearing-pin steel `X5CrNi18-10` and lever-bar steel
  `HX260LAD` in the CAD data. Confirm material keys before using them for identity
  matching.
- No reliable drawing or change revision is supplied. `Revision` is omitted;
  CAD node versions and `Startpart_Version` are not treated as drawing revisions.
- Specifications, dates, titles, assessments and test-method statements are
  illustrative and have not been checked against licensed standards or
  laboratory records. In particular, review the bearing pin's `10088-4` title
  and the characterization of hardness testing as non-destructive before reuse.
- Rubber specification types differ between the JSON (`Company X`) and CAD
  (`ABC`); no equivalence is asserted.
- One designation exceeds the schema's 60-character limit. The designation is
  shortened, with the full source text retained in `Comment`.
