# Definition sets on ComponentMaster, concrete assignments on ComponentInstance

## Context and Problem Statement

Some information exists both as a set of approved options for a component and as
a concrete value of an individually produced part. Colors and material sources
are typical examples. The question arose whether such information should be
modelled on the `ComponentMaster` (the generic component definition) or on the
`ComponentInstance` (a specific produced part).

## Decision Drivers

* PLM and engineering must be able to document approved colors and approved
  material sources before any part is produced.
* Traceability and complaint handling must be able to document the actual color
  and actual source of a specific produced part.
* Definitions should not be duplicated across instances.
* Produced parts must not introduce uncontrolled or unapproved variants.

## Considered Options

* Model the information only on the `ComponentInstance`.
* Model the information only on the `ComponentMaster`.
* Model the definition set on the `ComponentMaster` and the concrete assignment
  on the `ComponentInstance` via a reference.

## Decision Outcome

Chosen option: "Definition set on the `ComponentMaster`, concrete assignment on
the `ComponentInstance` via a reference", because it is the only option that
supports both the PLM definition use case (before production) and the
traceability use case (per produced part) without duplicating definitions.

The generic schema v3.0.0 already implements this pattern:

* `ComponentMaster.Colors` (definition set) and `ComponentInstance.ColorID` (reference)
* `ComponentMaster.MaterialSources` (definition set) and `ComponentInstance.MaterialSourceID` (reference)

The pattern shall be applied consistently to any future "variant-like"
attribute: the definition set is held on the master, and the instance references
one entry of that set via its identifier.

### Consequences

* Good, because approved colors and material sources can be documented in a PLM
  context without any produced part.
* Good, because each produced part is traceable to a specific, approved color
  and source.
* Good, because the `ComponentMaster` stays reusable across all variants and
  definitions are not duplicated.
* Neutral, because instances rely on the referenced definition existing on the
  master; consuming systems must resolve the reference.

## More Information

Related examples in the Example Library: `color-definition`,
`multiple-source-material`, `component-instance-traceability`.
