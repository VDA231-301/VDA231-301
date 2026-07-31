# NGID Identified Component

## Business Scenario

A component is used within a CAD assembly and needs to be uniquely referenced.

The NGIDPath provides a stable reference from the material and testing information to the corresponding occurrence within the CAD structure.

## Objective

This example demonstrates how a ComponentMaster can be linked to a CAD assembly occurrence using NGIDPath.

## Learning Goals

After reviewing this example, the reader should understand:

- the purpose of NGIDPath
- how a component can be linked to a CAD occurrence
- how NGID supports traceability between CAD and material information

## Relevant Entities

### ComponentMaster

The component being described.

## Relevant Attributes

This example focuses on:

- ComponentMaster.Designation
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.NGIDPath

## Modelling Decisions

This example uses a simplified NGID path.

The objective is to demonstrate the modelling principle rather than a complete CAD structure.

## JSON Example

See componentMaster-with-ngid.json

## Validation Status

Draft example based on the current generic schema draft.

## Related Examples

- Simple Material Definition
- Component Instance Traceability

## Architectural References

To be completed.
