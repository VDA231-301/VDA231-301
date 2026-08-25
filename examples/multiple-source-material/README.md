# Multiple Source Material

## Business Scenario

A supplier delivers an interior trim component made of PP-GF30 to an OEM. The
same material may be procured from more than one approved source. All approved
sources fulfil the same technical requirements, but they may differ in supplier,
trade name and the supplier-specific material specification.

Two distinct pieces of information have to be captured:

1. Which material sources are **approved and available** for this component
   (relevant for engineering, purchasing and multiple-source strategies, even
   before any part is produced).
2. Which material source a **specific produced part** was actually made from
   (relevant for traceability, complaint handling and root-cause analysis).

## Objective

This example demonstrates how approved material sources are defined once at the
`ComponentMaster` level using the `MaterialSource` entity, and how each produced
`ComponentInstance` references its actual material source via `MaterialSourceID`.

## Learning Goals

After reviewing this example, the reader should understand:

- how a material source is represented using the `MaterialSource` entity
- how approved material sources are defined at `ComponentMaster` level via `MaterialSources`
- how a produced part references its actual source via `ComponentInstance.MaterialSourceID`
- why the source definition and the source assignment are modelled on two levels

## Relevant Entities

### ComponentMaster

The generic definition of the component. It holds the list of approved
`MaterialSources` for this component, independent of any produced part.

### MaterialSource

An embedded entity describing a single approved material source, including its
material name, trade name, supplier (as a `Location`) and the supplier-specific
`Specification`.

### ComponentInstance

A specific manufactured instance of the component. It documents the actual
material source of the produced part by referencing one of the master's sources
via `MaterialSourceID`.

> Note: Within the `ComponentMaster`, the property that holds the sources is
> named `MaterialSources` (plural, in the context of the master). Each entry in
> this list is an object of type `MaterialSource`, indicated by its
> `"_type": "MaterialSource"`. The same convention applies to `Instances`
> (property) with entries of type `ComponentInstance`, and to `Colors`
> (property) with entries of type `Color`.

## Relevant Attributes

This example focuses on the following attributes:

- ComponentMaster.Designation
- ComponentMaster.MaterialName
- ComponentMaster.MaterialIdentifiers
- ComponentMaster.MaterialSources
- MaterialSource.MaterialName
- MaterialSource.TradeName
- MaterialSource.Supplier
- MaterialSource.Specification
- ComponentInstance.SerialNumber
- ComponentInstance.ProductionBatchNumber
- ComponentInstance.MaterialSourceID

## Modelling Decisions

The material source information is intentionally modelled on **two levels**, and
the generic schema (v3.0.0) explicitly supports this:

- The `ComponentMaster` holds the **definition set** of approved material
  sources in its `MaterialSources` list. This represents which sources are
  released for the component and can be documented in an engineering or
  purchasing context even before any part has been produced.
- The `ComponentInstance` documents the **actual material source** of a produced
  part by referencing one of the master's sources via `MaterialSourceID`.

This separation keeps the `ComponentMaster` reusable across all approved
sources and avoids duplicating source definitions. A produced part does not
introduce an uncontrolled source; it selects one of the sources that were
defined and approved at master level. This makes the source of every delivered
part consistent with the approved multiple-source set.

The example intentionally describes approved alternative sources for the same
material, not uncontrolled material substitutions.

This example uses the released schema structure. It replaces the earlier draft
version, which represented material sources with a proposed structure before the
`MaterialSources` / `MaterialSourceID` pattern was part of the generic schema.

## JSON Example

See `componentMaster-with-materialSources.json`.

## Validation Status

Aligned with the generic schema v3.0.0, in which `ComponentMaster.MaterialSources`
and `ComponentInstance.MaterialSourceID` are defined. Validation against the
released schema version should be performed before productive use.

## Related Examples

- Simple Material Definition
- Color Definition
- Component Instance Traceability

## Architectural References

- Entity: `MaterialSource` (MaterialName, TradeName, Supplier, Specification, AdditionalInformation)
- Definition set: `ComponentMaster.MaterialSources`
- Reference: `ComponentInstance.MaterialSourceID`
- Analogous pattern: `ComponentMaster.Colors` / `ComponentInstance.ColorID`

