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

## Find the Right Example

Use the following navigation guide to identify the example that best matches your use case.

| If you want to... | Start with |
|---|---|
| Understand the basic structure of a material definition | ./simple-material-definition/ |
| Add colour information to a component or material representation | ./color-definition/ |
| Trace individual physical component instances using serial and production information | ./component-instance-traceability/ |
| Represent a component hierarchy with subcomponents | ./component-master-hierarchy/ |
| Apply a customized specification to a material or component | ./material-with-specification-customization/ |
| Represent a multilayer material or coating stack | ./material-with-stack/ |
| Represent material information from multiple sources | [Multiple--source-material/ |
| Identify a component using an NGID path | ./ngid-identified-component/ |
| Represent a hierarchy of referenced specifications | ./specification-hierarchy/ |

## Example Overview

The following matrix provides an overview of the available examples, their purpose and the main modelling concepts demonstrated.

| Example | JSON file | Scenario | Key modelling concepts | Main entity |
|---|---|---|---|---|
| ./simple-material-definition/ | ./simple-material-definition/componentMaster.json | Basic definition of a material-related component | Component master data, material identification and version information | `ComponentMaster` |
| ./color-definition/ | ./color-definition/componentMaster-with-color.json | Representation of colour information | Colour-related information within a component master | `ComponentMaster` |
| ./component-instance-traceability/ | ./component-instance-traceability/componentInstance.json | Traceability of an individual physical component | Component instance, serial number and production traceability | `ComponentInstance` |
| ./component-master-hierarchy/ | ./component-master-hierarchy/componentMaster-with-subComponents.json | Representation of a component structure containing subcomponents | Component hierarchy and subcomponent relationships | `ComponentMaster` |
| ./material-with-specification-customization/ | ./material-with-specification-customization/componentMaster-with-specificationCustomization.json | Representation of a customized specification assignment | Specification customization and component-specific requirements | `ComponentMaster` |
| ./material-with-stack/ | ./material-with-stack/componentMaster-with-stack.json | Representation of a multilayer material or coating system | Stack structure and layer ordering | `ComponentMaster` |
| ./multiple-source-material/ | ./multiple-source-material/componentMaster-with-materialSources.json | Representation of material information from multiple sources | Multiple material sources within one component master | `ComponentMaster` |
| ./ngid-identified-component/ | ./ngid-identified-component/componentMaster-with-ngid.json | Identification of a component within a source CAD assembly structure | NGID identifier and NGID path | `ComponentMaster` |
| ./specification-hierarchy/ | ./specification-hierarchy/componentMaster-with-specificationHierarchy.json | Representation of referenced specifications in a hierarchical structure | Specification references and specification hierarchy | `ComponentMaster` |

Each example folder contains a dedicated README with additional information about the scenario, modelling approach and example data.

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

### component-master-hierarchy

Shows how a component hierarchy is modelled using `ComponentMaster.SubComponents`,
where each subcomponent is itself a `ComponentMaster`. Demonstrates that a
component can be a top-level node or a subcomponent depending on its position in
the tree (containment relationship).

File: `componentMaster-with-subComponents.json`

### specification-hierarchy

Shows how a specification can reference other specifications via
`Specification.ReferencedSpecifications`, so that a higher-level specification
references several sub-specifications (reference relationship). Complements the
component hierarchy example by contrasting "reference" with "containment".

File: `componentMaster-with-specificationHierarchy.json`

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

## Self-referencing structures

Two examples illustrate self-referencing (recursive) structures, which are a
common source of confusion:

- `component-master-hierarchy` uses `ComponentMaster.SubComponents`. This is a
  **containment** relationship: a parent component contains its subcomponents.
- `specification-hierarchy` uses `Specification.ReferencedSpecifications`. This
  is a **reference** relationship: a higher-level specification references other
  specifications that exist in their own right and can be reused by many
  specifications and components.

In both cases the role of an object (top node vs. subordinate) is not a property
of the object itself; it results from its position in the tree.

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

- layer-specific requirements
- Topic-based examples (e.g. VDA 270 / VDA 278 results)
- a complete minimal testing project

