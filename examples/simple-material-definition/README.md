# Simple Material Definition

## Business Scenario

An automotive supplier exchanges information about a material with an OEM using
the VDA 231-301 data model. The material shall be uniquely identified and linked
to the applicable material specification.

This is the most basic example of the Example Library and serves as the starting
point for understanding how a component and its material are represented.

## Objective

This example demonstrates the minimum structure required to describe a component
and its material using a `ComponentMaster`.

## Learning Goals

After reviewing this example, the reader should understand:

- how a component and its material are represented using a `ComponentMaster`
- how material identifiers are used
- how a material specification is referenced
- how a simple, valid VDA 231-301 example is structured

## Relevant Entities

### ComponentMaster

The central entity used to describe the component, its material and the
associated specification.

### Specification

A reference to the applicable material specification.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.SupplierPartNumber
- ComponentMaster.OemIdentifier
- ComponentMaster.Specifications
- Specification.Type
- Specification.Number
- Specification.IssueDate

## Modelling Decisions

This example intentionally represents a simple material without:

- colors
- material sources
- stacks
- specification customizations
- subcomponents
- instances

The objective is to provide the simplest possible valid example for new users.

The `Specifications` property references the applicable specification. Each
specification requires at least a `Type`, a `Number` and an `IssueDate`.

## JSON Example

See `componentMaster.json`.

## Validation Status

Aligned with the generic schema v3.0.0. Validation against the released schema
version should be performed before productive use.

## Related Examples

- Color Definition
- Multiple Source Material
- Material with Specification Customization
- Component Instance Traceability

## Architectural References

- Entity: `ComponentMaster`
- Referenced entity: `Specification` (Type, Number, IssueDate)

