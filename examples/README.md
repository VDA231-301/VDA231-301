# VDA 231-301 Example Library

This folder contains example files illustrating typical modelling patterns for the VDA 231-301 data model.

The examples are intended to support:

- onboarding of new users
- discussion of modelling approaches
- documentation of recommended usage patterns
- preparation of validation and tooling examples
- future AI-assisted example generation

## Purpose

The examples are not meant to replace the JSON Schema documentation.

Instead, they show how selected parts of the data model can be applied in realistic business scenarios.

Each example contains:

- a `README.md` explaining the business scenario and modelling decisions
- one or more JSON files illustrating the corresponding data structure

## Available Examples

### Simple Material Definition

Folder:

`simple-material-definition`

This example demonstrates how a simple material can be represented using a `ComponentMaster`.

It focuses on:

- material name
- material identifiers
- supplier part number
- specification references

Status:

Schema-oriented reference example.

### Multiple Source Material

Folder:

`multiple-source-material`

This example illustrates a proposed modelling approach for documenting multiple approved material sources.

It focuses on:

- alternative approved material sources
- supplier-specific material information
- trade names
- source-specific specifications

Status:

Draft example.

The `MaterialSources` structure is currently shown as a proposed modelling approach and is not yet part of the officially released generic schema.

### Material with Specification Customization

Folder:

`material-with-specification-customization`

This example demonstrates how an OEM-specific customization of a referenced specification can be represented.

It focuses on:

- `SpecificationCustomizations`
- `SpecificationDeviation`
- `DeviatingProperty`
- original and deviating requirement values

The example uses an odor rating requirement based on VDA 270 as an illustrative use case.

Status:

Draft example based on the current generic schema draft.

## Example Status

Examples may have different maturity levels:

### Reference example

The example follows the current schema structure and is intended as a recommended usage pattern.

### Draft example

The example illustrates a modelling proposal or a structure that is still under discussion.

Draft examples are useful for discussion but may not validate against the currently released schema.

### Future example

The example describes a planned use case that has not yet been modelled in detail.

## Naming Conventions

Example folders use lower-case names with hyphens.

Example JSON files should use descriptive names, such as:

- `componentMaster.json`
- `componentMaster-with-materialSources.draft.json`
- `componentMaster-with-specificationCustomization.json`

The suffix `.draft.json` should be used when the example contains structures that are not yet part of the officially released schema.

## Modelling Principles

The examples follow these general principles:

- focus on one modelling topic per example
- keep examples as simple as possible
- avoid company-specific confidential information
- use anonymized identifiers and specifications
- explain important modelling decisions in the README
- distinguish clearly between schema-based examples and draft modelling proposals

## Future Examples

Potential future examples may include:

- coating system with stack information
- composite material
- VDA 270 result
- VDA 278 result
- complete minimal TestingProject
- test series with consolidated characteristic values
- specification hierarchy and test method references


## How to Create a VDA 231-301 Example

Every example should contain the following sections:

1. Business Scenario
2. Objective
3. Learning Goals
4. Relevant Entities
5. Relevant Attributes
6. Modelling Decisions
7. JSON Example
8. Validation Status
9. Related Examples
10. Architectural References

### General Principles

Examples should:

- focus on one modelling topic
- be technically plausible
- use anonymized information
- avoid company confidential information
- explain modelling decisions
- distinguish clearly between released schema examples and draft proposals
- use realistic automotive use cases where possible


### Recommended File Structure

```text
example-name/
├── README.md
└── example.json
```

Example:

```text
simple-material-definition/
├── README.md
└── componentMaster.json
```

### Naming Conventions

Folder names:

- lower-case-with-hyphens

JSON files:

- componentMaster.json
- componentMaster-with-materialSources.draft.json
- componentMaster-with-specificationCustomization.json

Draft examples should use the suffix:

- .draft.json

