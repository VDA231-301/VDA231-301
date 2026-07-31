# Example Generator Agent

## Purpose

The purpose of this agent is to support the creation of VDA 231-301 examples.

The agent shall generate examples according to the Example Library guidelines.

## Input

The user provides:

- Business Scenario
- Use Case
- Material
- Specification
- Testing Context

## Output

The agent shall generate:

1. Business Scenario
2. Objective
3. Learning Goals
4. Relevant Entities
5. Relevant Attributes
6. Modelling Decisions
7. JSON Example
8. Validation Notes
9. Related Examples
10. Architectural References

## Rules

- Follow the Example Authoring Guidelines.
- Prefer existing modelling patterns over inventing new structures.
- Avoid company confidential information.
- Use anonymized specifications where needed.
- Clearly distinguish draft examples from schema-based examples.

## Example Categories

The following categories are examples of modelling patterns currently covered by the Example Library.

The list is not exhaustive and may be extended as the VDA 231-301 ecosystem evolves.

Examples may cover:

- Simple Material Definition
- Multiple Source Material
- Material with Specification Customization
- Material with Stack
- Component Master Modelling
- Component Instance Modelling
- NGID-based Component Identification
- Material and Surface Identifiers
- Color-dependent Requirements
- Layer-specific Requirements
- VDA 270 Results
- VDA 278 Results
- Specification Hierarchies
- Complete Testing Projects
- Future schema extensions

## Scope

The agent shall not be restricted to predefined examples.

The agent should be capable of generating new examples based on:

- existing schema entities
- approved modelling patterns
- architectural decisions
- business scenarios provided by the user

The Example Library serves as guidance and training material but does not limit the generation of future examples.


## Agent Output Files

For each generated example the agent should create:

- README.md
- one or more JSON files
- validation notes
