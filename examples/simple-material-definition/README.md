# Simple Material Definition

## Business Scenario

An automotive supplier wants to exchange information about a material with an OEM using the VDA 231-301 data model.

The material shall be uniquely identified and linked to the applicable material specification.

## Objective

This example demonstrates the minimum structure required to describe a material using VDA 231-301.

## Learning Goals

After reviewing this example, the reader should understand:

- how a material is represented
- how material identifiers are used
- how specifications are referenced
- how a simple VDA 231-301 example is structured

## Relevant Entities

### ComponentMaster

The central entity used to describe the material and its associated metadata.

### Specification

Reference to the applicable material specification.

### Material Identifier

Identifier used to uniquely identify the material within the business context.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.SupplierPartNumber
- ComponentMaster.SpecificationS

## Modelling Decisions

This example intentionally represents a simple material without:

- coating systems
- composite materials
- multiple-source scenarios
- customized requirements
- subcomponents

The objective is to provide the simplest possible example for new users.

## JSON Example

Draft example based on the current generic schema draft for the upcoming release.

## Validation Status

To be completed.

## Related Examples

Future related examples:

- Composite Material
- Multiple Source Material
- Material with Customized Requirements
- Multi-Layer Coating System

## Architectural References

To be completed.
