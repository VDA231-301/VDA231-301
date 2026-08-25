# NGID Identified Component

## Business Scenario

A component is used within a CAD assembly. To link the material and testing
information to the exact occurrence of the component in the source CAD assembly
structure, a stable reference is required. The Siemens JT Next Generation
Identifier (NGID) provides such a reference through an `NGIDPath`.

This allows the OEM and downstream systems to relate the VDA 231-301 data of a
component to its position within the CAD assembly.

## Objective

This example demonstrates how a `ComponentMaster` is linked to its occurrence in
a CAD assembly structure using `NGIDPath`.

## Learning Goals

After reviewing this example, the reader should understand:

- the purpose of `NGIDPath`
- how an NGID path is structured
- how a component is located within a CAD assembly structure
- how NGID supports traceability between CAD data and material / testing data

## Relevant Entities

### ComponentMaster

The component being described, including its reference to the CAD assembly
occurrence via `NGIDPath`.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.Version
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.NGIDPath

## Understanding the NGID path

The value used in this example is:

```
$$NGID<chain>="JT_PROP_NAME"\0DoorAssembly.asm;0;2:\0DoorTrim.part;0;1:\0\0
```

It is built according to the Siemens "NGID Identifiers" specification:

- `$$NGID<chain>="JT_PROP_NAME"` starts a path tier and selects the identifier
  by which the nodes are named. `JT_PROP_NAME` is a fixed, reserved identifier
  name from the NGID specification and is written literally (it is not a
  placeholder to be replaced).
- `\0` is the delimiter between the components of the path.
- `DoorAssembly.asm;0;2:` and `DoorTrim.part;0;1:` are the node values in CADID
  format: `name.type;version;instanceId`. The version field is optional; the
  instance id is locally unique relative to the parent.
- `\0\0` (a double delimiter) terminates the path.

The node values (the CADID strings) are the parts that describe the actual CAD
structure and are replaced with real values in productive data. The identifier
name in quotes (`"JT_PROP_NAME"`) and the delimiters are part of the fixed
syntax.

## Modelling Decisions

The `NGIDPath` follows the Siemens JT Next Generation Identifier (NGID)
specification. This example uses the `JT_PROP_NAME` identifier with
CADID-formatted node values, which matches the reference example provided by
Siemens for a JT Open Toolkit generated NGID path.

The specific node names, versions and instance ids used here are illustrative
and only intended to demonstrate the structure, not to describe a specific real
CAD assembly.

The `Version` attribute represents the version / change status of the component
definition (for example the drawing status, known as ZGS at Mercedes-Benz) and
should always be provided when describing a component.

## JSON Example

See `componentMaster-with-ngid.json`.

## Validation Status

Aligned with the generic schema v3.0.0, in which `ComponentMaster.NGIDPath` is
defined. The path structure follows the Siemens "NGID Identifiers"
specification. Validation against the released schema version should be
performed before productive use.

## Related Examples

- Simple Material Definition
- Component Instance Traceability
- Color Definition

## Architectural References

- Property: `ComponentMaster.NGIDPath`
- Reference: Siemens JT Next Generation Identifier (NGID) specification
- Path syntax: `$$NGID<chain>="identifier_name"\0<node values>\0\0`
- Node value (CADID) format: `name.type;version;instanceId`

