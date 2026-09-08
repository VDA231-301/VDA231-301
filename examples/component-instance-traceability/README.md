# Component Instance Traceability

## Business Scenario

A supplier delivers an interior trim component made of PP-GF30 to an OEM.

For quality management, traceability and complaint handling, production-related
information must be available for each individually manufactured part. This
information can include the serial number, production batch, production site,
machine, tool, cavity and production date.

The same component is produced many times. Each produced part is an individual
instance with its own traceability data, even if several parts originate from
the same production batch.

## Objective

This example demonstrates how individually produced parts are represented as
`ComponentInstance` objects within a `ComponentMaster`, and how each instance
carries its own production traceability information.

## When to Use This Example

Use this example when production and traceability information for individual
manufactured parts has to be represented.

The example is appropriate when several produced parts share the same component
definition but require separate instance-specific information, such as:

- serial number
- production batch
- production site
- machine
- tool
- cavity
- production date

Do not use this example as the primary example for:

- defining approved colors
- assigning the actual color of a produced part
- defining approved material sources
- assigning the actual material source of a produced part
- representing test results or technical requirements

The corresponding specialized examples should be used for these purposes.

## Learning Goals

After reviewing this example, the reader should understand:

- the difference between `ComponentMaster` and `ComponentInstance`
- how production-related traceability data is documented at instance level
- how several produced parts of the same component are represented
- how batch, site, machine, tool and cavity information is captured for each
  produced part
- why instance-specific production data is not stored on the
  `ComponentMaster`

## Relevant Entities

### ComponentMaster

The generic definition of the component. It describes the component design and
material independently of any individually produced part.

The `ComponentMaster` contains the `Instances` list with the produced parts
represented as `ComponentInstance` objects.

### ComponentInstance

A specific manufactured instance of the component. It documents the production
and traceability information of one produced part.

Each `ComponentInstance` belongs to the component definition represented by the
containing `ComponentMaster`.

> **Note:** Within the `ComponentMaster`, the property that holds the instances
> is named `Instances`, plural in the context of the master. Each entry in this
> list is an object of type `ComponentInstance`, indicated by its
> `"_type": "ComponentInstance"`.

## Relevant Attributes

This example focuses on the following attributes:

- `ComponentMaster.Designation`
- `ComponentMaster.Version`
- `ComponentMaster.MaterialName`
- `ComponentMaster.MaterialIdentifiers`
- `ComponentMaster.Instances`
- `ComponentInstance.SerialNumber`
- `ComponentInstance.ProductionBatchNumber`
- `ComponentInstance.ProductionSite`
- `ComponentInstance.Machine`
- `ComponentInstance.Tool`
- `ComponentInstance.Cavity`
- `ComponentInstance.ProductionDate`

## Modelling Decisions

Production traceability information is modelled at the level of the
`ComponentInstance` because it applies to a specific produced part and not to
the generic component definition.

The example shows two produced parts of the same component. Both parts
originate from the same production batch but were manufactured in different
cavities.

This demonstrates that each `ComponentInstance` carries its own traceability
information, even where some production-related values are shared by several
parts.

The `ComponentInstance` objects are contained in the `Instances` list of the
related `ComponentMaster`. This keeps the component definition reusable while
allowing any number of individually traceable produced parts to be represented.

The `Version` attribute represents the version or change status of the
component definition and should always be provided when describing a component
in the Example Library.

The `Version` belongs to the `ComponentMaster`. It does not replace the
instance-specific production information of a produced part.

This example focuses exclusively on production traceability. It intentionally
does not include:

- color definitions or color assignments
- material source definitions or material source assignments
- testing results
- technical requirements

These concerns are covered by separate examples.

## Source of Truth and References

- The generic component definition is maintained in the `ComponentMaster`.
- The version or change status of the component definition is maintained in
  `ComponentMaster.Version`.
- The produced parts are maintained as individual entries in
  `ComponentMaster.Instances`.
- The production traceability information of a produced part is maintained on
  the corresponding `ComponentInstance`.
- `ComponentInstance.SerialNumber` identifies the individual produced part
  within the context of this example.
- `ComponentInstance.ProductionBatchNumber` identifies the production batch to
  which the part belongs.
- `ComponentInstance.ProductionSite`, `ComponentInstance.Machine`,
  `ComponentInstance.Tool`, `ComponentInstance.Cavity` and
  `ComponentInstance.ProductionDate` describe the production context of the
  individual part.
- Instance-specific production information is not duplicated on the
  `ComponentMaster`.

## JSON Example

See `componentInstance.json`.

## Validation Status

This example is intended to align with the generic schema v3.0.0, including the
representation of `ComponentInstance` objects in
`ComponentMaster.Instances`.

Validation against the referenced released schema version should be performed
before productive use.

## Related Examples

- **Simple Material Definition**  
  Use this example for the basic material-related description of a
  `ComponentMaster` without detailed instance traceability.

- **Color Definition**  
  Use this example when approved colors and the actual color of a produced part
  have to be represented through `ComponentMaster.Colors` and
  `ComponentInstance.ColorID`.

- **Multiple Source Material**  
  Use this example when approved material sources and the actual material
  source used for a produced part have to be represented through
  `ComponentMaster.MaterialSources` and
  `ComponentInstance.MaterialSourceID`.

- **VDA 270 Odor Test - Complete**  
  Use this example when a concrete produced part must be connected to a
  complete test result through `Specimen.ComponentInstanceID`.

## Architectural References

- Entity: `ComponentMaster`
- Entity: `ComponentInstance`
- Container: `ComponentMaster.Instances`
- Individual part identifier: `ComponentInstance.SerialNumber`
- Batch reference: `ComponentInstance.ProductionBatchNumber`
- Production context:
  `ComponentInstance.ProductionSite`,
  `ComponentInstance.Machine`,
  `ComponentInstance.Tool`,
  `ComponentInstance.Cavity` and
  `ComponentInstance.ProductionDate`
- ADR 0002: `ComponentMaster.Version` is mandatory in component examples
