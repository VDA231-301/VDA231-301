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

## Components and materials

**Component master**:
The reusable definition of a component, including its part identification and component-specific requirements, distinct from its material and its physical instances.

**Engineering material**:
In VDA 231-301, EngineeringMaterial generally denotes the technically defined material of a component. Depending on company terminology, it may correspond to a design material or a production material.

**Material class**:
The descriptive category of an engineering material, such as Stainless steel.

**Material name**:
The specific designation of an engineering material, such as 1.4301-X5CrNi18-10, which may combine a material number and an abbreviated designation.

**Design material**:
A material requirement profile used in engineering design, independent of a particular production plant or supplier.

**Production material**:
A narrower, manufacturing-related requirement profile of the same material, used for example for plant-specific or supplier-specific procurement.

**Material source**:
A concrete supplier material with its trade name, supplier and source-specific specification or datasheet.

**Component material assignment**:
The association of a component with an engineering material or layer stack, optionally qualified by material role and geographic scope.
