# NGIDPath examples use JT_PROP_NAME with CADID-formatted node values

Status: accepted

## Context and Problem Statement

`ComponentMaster.NGIDPath` references the occurrence of a component within a
source CAD assembly structure, following the Siemens "NGID Identifiers"
specification. It had to be decided how an NGID path is represented in the
Example Library, because the generic schema only provides a free-text example
in the field description and the exact meaning of its parts was initially
unclear (in particular whether `__CAD_INST_UID` is a placeholder or a fixed
identifier name).

## Decision Drivers

* Examples must be correct with respect to the Siemens NGID specification.
* The representation should match a verifiable Siemens reference example.
* Readers must understand which parts are fixed syntax and which parts are
  replaced with real CAD values.

## Considered Options

* Use `__CAD_INST_UID` as the identifier name with CADID-formatted node values
  (as shown in the schema field description).
* Use `JT_PROP_NAME` as the identifier name with CADID-formatted node values
  (as shown in the Siemens JT Open Toolkit reference example).

## Decision Outcome

Chosen option: "Use `JT_PROP_NAME` with CADID-formatted node values", because it
matches the verifiable Siemens reference example
(`$$NGID<chain>="JT_PROP_NAME"\0wheels.asm;0;5:\0Tire.part;0;1:\0\0`) and is
consistent with the NGID specification: CADID-formatted node values
(`name.type;version;instanceId`) correspond to the `JT_PROP_NAME` identifier.

Key facts established from the Siemens "NGID Identifiers" specification:

* Identifier names such as `JT_PROP_NAME` and `__CAD_INST_UID` are fixed,
  reserved names written literally in quotes; they are not placeholders.
* An NGID path tier has the form `$$NGID<chain>="identifier_name"` followed by
  `\0`-delimited node values, terminated by a double delimiter `\0\0`.
* A CADID node value has the format `name.type;version;instanceId`, where the
  version is optional and the instance id is locally unique relative to the
  parent.

### Consequences

* Good, because the example is backed by a verifiable Siemens reference and the
  NGID specification, not by assumption.
* Good, because the README explains which parts are fixed syntax and which are
  replaced with real CAD values.
* Neutral, because the generic schema field description currently shows
  `__CAD_INST_UID` together with CADID-formatted values, which is inconsistent
  with the specification. This should be raised for correction of the schema
  description (see open point below).

## More Information

Open point: The `NGIDPath` description in the generic schema uses the identifier
name `__CAD_INST_UID` together with CADID-formatted node values. According to
the Siemens specification, CADID-formatted values correspond to `JT_PROP_NAME`,
whereas `__CAD_INST_UID` values are CAD instance ids. The schema field
description should be reviewed and corrected accordingly.

Related example in the Example Library: `ngid-identified-component`.
Source documents: Siemens "NGID Identifiers_July2024" and "Referenceable JT
data" (JT Open Program).
