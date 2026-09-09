# VDA 231-301

This context defines the terminology used to exchange material-related specifications, requirements, and test data.

## Language

**Property**:
A named aspect of a material or component to which a value can be assigned, such as G-modulus or Shore hardness.
_Avoid_: Characteristic name, attribute name

**Characteristic requirement**:
The value, permitted range, or tolerance that a specification imposes on a property. It is not an actual measured or reported value.
_Avoid_: Property detail, specification property

**Characteristic value**:
An actual reported, measured, or consolidated value of a property.
_Avoid_: Requirement, target value

## Specimen ownership and reuse

**Specimen**:
A physical sample extracted or prepared from a component instance for testing. A specimen belongs to a topic and is declared once in that topic's `Specimens` collection.

**Specimen reference**:
Each test execution identifies the specimen it uses through `SpecimenID`. More than one execution may reference the same specimen, for example when sequential analyses are performed on one physical sample. Embedding or duplicating a specimen inside a test execution is not supported.
