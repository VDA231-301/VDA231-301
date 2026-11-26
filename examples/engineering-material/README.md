# CR5 design and production materials

The [example](engineering-material.json) defines two CR5 profiles. Both use
`Steel` as the group, `Low-carbon steel` as the class and `CR5` as the name.
The identifiers, specifications, suppliers and measurements are illustrative.

The production profile references the design profile through
`DerivedFromEngineeringMaterialID`. Each profile states its own requirements.
`MaterialDefinitionLevel` accepts `Design` or `Production`. The coating material
omits the optional level and derivation reference.

Two components use the production profile. One also has a two-layer stack.
Its physical instance records the supplier material in the `MaterialSourceID`
array and the colour in `ColorID`.
