# ComponentMaster.Version (drawing / change status) is mandatory in component examples

Status: accepted

## Context and Problem Statement

A component definition is only unambiguous together with its version / change
status. The same part number can exist in several versions (for example the
drawing status, known as ZGS at Mercedes-Benz, and generally maintained by every
PLM system). It had to be decided whether the version should be an optional
detail or a mandatory part of describing a component in the Example Library.

## Decision Drivers

* A part number without a version is not unambiguous.
* Every PLM system maintains a version / change status for a component.
* Examples should reflect realistic, production-relevant component descriptions.

## Considered Options

* Treat `ComponentMaster.Version` as an optional detail and omit it in examples.
* Include `ComponentMaster.Version` in every component example.

## Decision Outcome

Chosen option: "Include `ComponentMaster.Version` in every component example",
because a component definition is only unambiguous together with its version and
because every PLM system maintains this value.

`ComponentMaster.Version` shall be present in all component examples of the
Example Library.

### Consequences

* Good, because examples reflect unambiguous, production-relevant component
  descriptions.
* Good, because it aligns the examples with real PLM usage.
* Neutral, because the field remains optional in the generic schema; the
  requirement applies to the Example Library, not to the schema itself.

## More Information

The generic schema defines `ComponentMaster.Version` as a string, with the
drawing status (ZGS) given as an example value (e.g. "0001", "0002").
