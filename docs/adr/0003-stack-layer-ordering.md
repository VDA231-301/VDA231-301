# Stack layer ordering starts at the substrate (layer 1 = bottom)

Status: accepted

## Context and Problem Statement

A material stack describes a layered structure (for example a substrate with a
primer and a paint layer). The layers are numbered via `LayerNumber` in the
`Stack` structure. It had to be decided in which direction the layers are
counted, so that stack examples and stack data are interpreted consistently.

## Decision Drivers

* Layer numbering must be unambiguous and consistent across all examples and data.
* The convention should match the generic schema, which describes layer 1 as the
  bottom layer.
* The convention should be intuitive for typical component structures.

## Considered Options

* Count layers from the substrate outward (layer 1 = substrate / bottom).
* Count layers from the outer surface inward (layer 1 = top / outer layer).

## Decision Outcome

Chosen option: "Count layers from the substrate outward", so that layer 1 is the
substrate (bottom layer) and the highest layer number is the top / outer layer.
This matches the generic schema, which defines layer 1 as the bottom layer.

In special cases where a stack cannot be clearly oriented from a substrate (for
example a symmetric structure, a free-standing film or a coating-only stack), the
chosen orientation and the meaning of layer 1 shall be described in the stack's
`Comment` so that the ordering remains unambiguous.

### Consequences

* Good, because the layer ordering is consistent with the generic schema.
* Good, because typical component stacks are described intuitively from the
  substrate outward.
* Neutral, because special or symmetric structures require an explicit note about
  the chosen orientation.

## More Information

Related example in the Example Library: `material-with-stack`.
