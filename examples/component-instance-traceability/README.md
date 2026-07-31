# Component Instance Traceability

## Business Scenario

A supplier provides an interior trim component made from PP-GF30.

The OEM requires traceability information for the tested component instance.

The supplier therefore documents production-specific information such as batch number, tool, cavity and production date.

## Objective

This example demonstrates how a specific physical component instance can be represented using the ComponentInstance entity.

## Learning Goals

After reviewing this example, the reader should understand:

- the difference between ComponentMaster and ComponentInstance
- how production-related information is documented
- how batch-related traceability data can be represented
- how individual manufactured parts can be identified

## Relevant Entities

### ComponentMaster

Definition of the component.

### ComponentInstance

Representation of a specific manufactured instance of the component.

## Relevant Attributes

This example focuses on:

- ComponentInstance.ProductionBatchNumber
- ComponentInstance.ProductionDate
- ComponentInstance.Tool
- ComponentInstance.Cavity
- ComponentInstance.SerialNumber

## Modelling Decisions

This example represents a single manufactured instance of a PP-GF30 interior trim component.

The focus is on traceability information and not on testing results.

## JSON Example

See componentInstance.json

## Validation Status

Draft example based on the current generic schema.

## Related Examples

- Simple Material Definition
- Material with Stack

## Architectural References

To be completed.
