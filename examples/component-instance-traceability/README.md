# Component Instance Traceability

## Business Scenario

A supplier delivers an interior trim component made of PP-GF30 to an OEM. For
quality management, traceability and complaint handling, the OEM requires
production-related information for each individually manufactured part, such as
serial number, production batch, production site, machine, tool and cavity.

The same component is produced many times. Each produced part is an individual
instance with its own traceability data, even if several parts come from the
same production batch.

## Objective

This example demonstrates how individually produced parts are represented as
`ComponentInstance` objects within a `ComponentMaster`, and how each instance
carries its own production traceability information.

## Learning Goals

After reviewing this example, the reader should understand:

- the difference between `ComponentMaster` and `ComponentInstance`
- how production-related traceability data is documented on instance level
- how several produced parts of the same component are represented
- how batch, site, machine, tool and cavity information is captured per part

## Relevant Entities

### ComponentMaster

The generic definition of the component. It describes the component design and
material, independent of any individual produced part.

### ComponentInstance

A specific manufactured instance of the component. It documents the production
traceability information of one produced part.

> Note: Within the `ComponentMaster`, the property that holds the instances is
> named `Instances` (plural, in the context of the master). Each entry in this
> list is an object of type `ComponentInstance`, indicated by its
> `"_type": "ComponentInstance"`.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentInstance.SerialNumber
- ComponentInstance.ProductionBatchNumber
- ComponentInstance.ProductionSite
- ComponentInstance.Machine
- ComponentInstance.Tool
- ComponentInstance.Cavity
- ComponentInstance.ProductionDate

## Modelling Decisions

Traceability information is modelled at the level of the `ComponentInstance`,
because it applies to a specific produced part and not to the generic component
definition.

The example shows two produced parts of the same component. Both originate from
the same production batch but were manufactured in different cavities. This
demonstrates that each instance carries individual traceability information even
when other production data is shared.

The `ComponentInstance` objects are placed inside the `Instances` list of a
`ComponentMaster`. This keeps the component definition reusable while allowing
an arbitrary number of individually traceable produced parts.

The focus of this example is production traceability. It intentionally does not
include colors, material sources, testing results or requirements.

## JSON Example

See `componentInstance.json`.

## Validation Status

Aligned with the generic schema v3.0.0. Validation against the released schema
version should be performed before productive use.

## Related Examples

- Simple Material Definition
- Color Definition
- Multiple Source Material

## Architectural References

- Entity: `ComponentInstance` (SerialNumber, ProductionBatchNumber, ProductionSite, Machine, Tool, Cavity, ProductionDate)
- Container: `ComponentMaster.Instances`

