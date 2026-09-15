# Hierarchies are modelled via self-reference (containment for components, reference for specifications)

Status: accepted

## Context and Problem Statement

Some entities in the data model can form hierarchies. A component can be a
top-level node of a part tree or a subcomponent of a larger component. A
specification can stand on its own or be referenced by a higher-level
specification. It had to be decided how such hierarchies are represented in the
data model.

## Decision Drivers

* Hierarchies must support an arbitrary nesting depth.
* An entity should have the same structure regardless of its position in the
  hierarchy (top node or subordinate).
* The model should reflect real part trees / bills of material and real
  specification structures (e.g. a product standard referencing test and
  material standards).

## Considered Options

* Introduce separate entity types for subordinate elements (e.g. a dedicated
  "SubComponentMaster" or "SubSpecification").
* Model hierarchies as flat lists with explicit parent identifiers.
* Model hierarchies via self-reference: an entity references entities of its own
  type.

## Decision Outcome

Chosen option: "Model hierarchies via self-reference", because it keeps the same
attributes at every level, supports arbitrary depth, and matches real part trees
and specification structures. No separate subordinate entity type is required.

The self-reference is applied to two entities, with an important semantic
difference:

* `ComponentMaster.SubComponents` is a **containment** relationship: a parent
  component contains its subcomponents. A subcomponent is simply a
  `ComponentMaster` placed inside another `ComponentMaster`.
* `Specification.ReferencedSpecifications` is a **reference** relationship: a
  higher-level specification references other specifications that exist in their
  own right and are typically reused by many specifications and components.

| Aspect | ComponentMaster.SubComponents | Specification.ReferencedSpecifications |
|--------|-------------------------------|----------------------------------------|
| Pattern | self-reference (recursive tree) | self-reference (recursive tree) |
| Semantics | containment (parent contains child) | reference (parent points to independent specs) |
| Consequence | a subcomponent belongs to its parent | a referenced specification is independent and reusable |

The role of an object (top node vs. subordinate) is not a property of the object
itself; it results from its position in the hierarchy.

### Consequences

* Good, because the same entity structure is reused at every level and no
  additional entity types are needed.
* Good, because it matches part trees / bills of material and specification
  structures, and aligns with the CAD assembly structure (see `NGIDPath`).
* Good, because distinguishing containment from reference prevents a common
  misunderstanding: referenced specifications are shared and not duplicated,
  while subcomponents are contained.
* Neutral, because consuming systems must be able to traverse recursive
  structures.

## More Information

Related examples in the Example Library: `component-master-hierarchy` and
`specification-hierarchy`.
