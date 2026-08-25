# VDA 231-301 Example Library

This folder contains example files illustrating typical modelling patterns for
the VDA 231-301 data model.

The examples are intended to support:

- onboarding of new users
- discussion of modelling approaches
- documentation of recommended usage patterns
- preparation of validation and tooling examples

## Purpose

The examples are not meant to replace the JSON Schema documentation. Instead,
they show how selected parts of the data model can be applied in realistic
business scenarios.

Each example contains:

- a `README.md` explaining the business scenario and modelling decisions
- one or more JSON files illustrating the corresponding data structure

All examples are aligned with the generic schema v3.0.0.

## Available Examples

### simple-material-definition

The minimal "hello world" example. Describes a component and its material using
a `ComponentMaster` with a referenced specification.

File: `componentMaster.json`

### color-definition

Shows how approved colors are defined at `ComponentMaster` level via `Colors`
and how each produced `ComponentInstance` references its actual color via
`ColorID`.

File: `componentMaster-with-color.json`

### multiple-source-material

Shows how approved material sources are defined at `ComponentMaster` level via
`MaterialSources` and how each produced `ComponentInstance` references its actual
source via `MaterialSourceID`.

File: `componentMaster-with-materialSources.json`

### component-instance-traceability

Shows how individually produced parts are represented as `ComponentInstance`
objects within a `ComponentMaster`, each carrying its own production traceability
information (batch, site, machine, tool, cavity).

File: `componentInstance.json`

### material-with-stack

Shows how a layered material structure is represented using the `Stack` property
with `ArraySpec` and `ArrayValue` (LayerNumber, Material, Mass, Thickness).

File: `componentMaster-with-stack.json`

### material-with-specification-customization

Shows how an OEM-specific deviation from a referenced specification is documented
using `SpecificationCustomizations` and `DeviatingProperty`, without changing the
referenced specification itself.

File: `componentMaster-with-specificationCustomization.json`

### ngid-identified-component

Shows how a `ComponentMaster` is linked to its occurrence in a CAD assembly
structure using `NGIDPath`, following the Siemens NGID specification.

File: `componentMaster-with-ngid.json`

## Conventions

The examples follow a set of shared conventions. Key architectural decisions are
documented as Architectural Decision Records (ADRs) in `docs/adr`:

- Definition sets are held on the `ComponentMaster`, concrete assignments on the
  `ComponentInstance` (e.g. `Colors` / `ColorID`, `MaterialSources` /
  `MaterialSourceID`).
- `ComponentMaster.Version` (drawing / change status, ZGS) is included in every
  component example.
- Stack layers are numbered starting with 1 for the bottom (substrate) layer.
- `NGIDPath` examples use the `JT_PROP_NAME` identifier with CADID-formatted node
  values.

## Naming Conventions

- Example folders use lower-case names with hyphens.
- JSON files use descriptive names, for example `componentMaster.json` or
  `componentMaster-with-color.json`.

## Modelling Principles

- Focus on one modelling topic per example.
- Keep examples as simple as possible while preserving the learning objective.
- Use anonymized identifiers and fictional specifications.
- Avoid company-specific confidential information.
- Explain important modelling decisions in the example's README.

## Future Examples

Potential future examples include:

- specification hierarchies
- layer-specific requirements
- Topic-based examples (e.g. VDA 270 / VDA 278 results)
- a complete minimal testing project
