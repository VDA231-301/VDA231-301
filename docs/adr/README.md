# Architectural Decision Records (ADR)

This folder contains the Architectural Decision Records (ADRs) for the
VDA 231-301 project. ADRs document important architectural and modelling
decisions together with their context, the considered options and their
consequences.

The records follow the MADR (Markdown Architectural Decision Records) format.

## How to use

- Each decision is stored in its own file, named `NNNN-short-title.md`.
- New decisions receive the next free sequential number.
- ADRs are not deleted. If a decision changes, a new ADR is added and the
  superseded one is marked accordingly.

## Index

| ID | Title | Status |
|----|-------|--------|
| 0001 | [Definition sets on ComponentMaster, concrete assignments on ComponentInstance](0001-definition-set-on-master-assignment-on-instance.md) | accepted |
| 0002 | [ComponentMaster.Version (drawing / change status) is mandatory in component examples](0002-componentmaster-version-mandatory.md) | accepted |
| 0003 | [Stack layer ordering starts at the substrate (layer 1 = bottom)](0003-stack-layer-ordering.md) | accepted |
| 0004 | [NGIDPath examples use JT_PROP_NAME with CADID-formatted node values](0004-ngid-path-representation.md) | accepted |
| 0005 | [Hierarchies are modelled via self-reference (containment for components, reference for specifications)](0005-hierarchies-via-self-reference.md) | accepted |
| 0006 | [norm-information-aggregation](0006-norm-information-aggregation.md) | accepted | 
| 0007 | [material-characteristics-read-out-logic](0007-material-characteristics-read-out-logic.md) | accepted | 
| 0008 | [abbreviated-material-designation-to-materialclass](0008-abbreviated-material-designation-to-materialclass.md) | accepted | 
| 0009 | [typed-material-identifiers-no-duplication](0009-typed-material-identifiers-no-duplication.md) | accepted |
