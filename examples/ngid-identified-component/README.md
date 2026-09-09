# NGID Identified Component

## Business Scenario

A component is used within a source CAD assembly.

To link material and testing information to the exact occurrence of the
component in that assembly structure, a stable and machine-readable reference
is required.

The Siemens JT Next Generation Identifier, NGID, provides such a reference
through an `NGIDPath`.

The `NGIDPath` enables an OEM and downstream systems to relate the
VDA 231-301 data of a component to its occurrence within the source CAD
assembly structure.

## Objective

This example demonstrates how a `ComponentMaster` is linked to its occurrence
in a source CAD assembly structure using `ComponentMaster.NGIDPath`.

## When to Use This Example

Use this example when:

- a component must be related to its exact occurrence in a source CAD assembly
- material or testing information must be linked to a CAD assembly occurrence
- the same component definition can occur more than once in an assembly
- the position of the component in the CAD structure must remain traceable
- an NGID-compliant reference is available from the source CAD or JT data

Do not use this example as the primary representation of:

- a component hierarchy
- a bill-of-material-like containment structure
- individually produced parts
- production traceability information
- a material source assignment

Use the **Component Master Hierarchy** example when a component structure has
to be represented through `ComponentMaster.SubComponents`.

Use the **Component Instance Traceability** example when production-related
information for an individually manufactured part has to be represented through
a `ComponentInstance`.

An `NGIDPath` identifies an occurrence in the source CAD assembly structure.
It does not replace the component hierarchy or the identity of an individually
produced part.

## Learning Goals

After reviewing this example, the reader should understand:

- the purpose of `ComponentMaster.NGIDPath`
- how an NGID path is structured
- which parts of the NGID path are fixed syntax
- which parts contain values from the actual CAD assembly
- how a component occurrence is located within a source CAD assembly
- how NGID supports traceability between CAD data and VDA 231-301 material or
  testing data
- why `JT_PROP_NAME` is written literally and must not be treated as a
  placeholder

## Relevant Entities

### ComponentMaster

The `ComponentMaster` represents the component being described.

Its `NGIDPath` property contains the reference to the occurrence of the
component within the source CAD assembly structure.

The component identity and the CAD occurrence reference are different pieces
of information:

- the component is described by the `ComponentMaster`
- the component occurrence in the CAD assembly is referenced by
  `ComponentMaster.NGIDPath`

## Relevant Attributes

This example focuses on the following attributes:

- `ComponentMaster.
