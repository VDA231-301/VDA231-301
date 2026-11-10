# Engineering materials: design and production profiles

This example targets the repository-main **development schema (ERM Arbeitsstand 8)**,
not a published v3.0.0 release. See the [migration notes](../../docs/engineering-material-migration.md).

The CR5 designation comes from the proposed VW scenario. All identifiers,
requirements, suppliers, classifications, dimensions and masses are illustrative.
The Scholz slides were not available when preparing this example; it is not a
transcription of VW's CR5 data or a statement of normative material properties.

- Every EngineeringMaterial includes the required MaterialGroup, MaterialClass
  and MaterialName, including the coating that omits the optional VW fields.
- EngineeringMaterials declares a Design profile and a Production profile for
  the same material. DerivedFromMaterialID points from Production to Design.
- Two component definitions reuse the production profile through MaterialAssignments.
- An additional coating material omits both optional VW fields.
- A Stack contains explicit StackLayers referencing reusable materials.
- Material sources, a source-specific datasheet and colors belong to the material;
  the physical instance selects its MaterialSourceID and ColorID.
- Component classifications support a parent and nested subclassifications.
- A material-level topic uses EngineeringMaterialID without requiring ComponentMasterID.

Specifications are explicit on each profile. DerivedFromMaterialID does not inherit
requirements, classifications, colors or supplier sources. Both optional fields
can also occur on their own. Unspecified is accepted as an explicit level;
omission is the usual representation when the distinction is not made.

Validate structure, reference targets, instance selections and acyclicity with:

```sh
python scripts/validate_materials.py examples/engineering-material/engineering-material.json
```
