## Release checklist (subschema)
- [ ] Make sure the version number in `$id` of the subschema JSON schema file is updated
- [ ] Make sure all references to the generic schema point to the correct version of the generic schema, e.g. <br>`"$ref": "https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v2.0.0.schema.json"`
- [ ] Make sure the example file validates against the schema file using for example: https://www.jsonschemavalidator.net/
- [ ] Save the working copy of the schema with the file name according to the `$id` property.<br>
    For example: <br>`"$id": "https://vda231-301.github.io/schemas/SubstanceDeclaration/VDA_231_301_Substance_declaration_v2.0.0.schema.json",`<br>
   &rarr; `VDA_231_301_Substance_declaration_v2.0.0.schema.json`
- Also save the example file with the version filename. <br>
    For example:<br>`"$id": "https://vda231-301.github.io/schemas/SubstanceDeclaration/VDA_231_301_Substance_declaration_v2.0.0.schema.json",`<br>
   &rarr; `VDA_231_301_Substance_declaration_v2.0.0.example.json`
- [ ] Create a release in the subschema GitHub repository:
    - Go to the "Releases" section of the GitHub repository
    - Click on "Create a new release"
    - Create a tag for the release, e.g. `v2.0.0` (or use it if it already exists)
    - Title: Release v2.0.0 (or the respective version)
    - Description: Add a description of the release describing the changes made in this version
    - Attach the schema and example files to the release
    - Publish the release
- [ ] Save the schema file with the versioned filename to the respective folder in the schemas repository (folder name is again part of the `$id` path)<br>
    For example:<br>`"$id": "https://vda231-301.github.io/schemas/SubstanceDeclaration/VDA_231_301_Substance_declaration_v2.0.0.schema.json",`<br>
   &rarr; Save the file to `schemas/SubstanceDeclaration/`
- [ ] Push the changes to the schemas repository. A GitHub action will automatically update the GitHub pages of the schemas repository and make the new version available at the URL specified in `$id`.

## Release checklist (generic schema)
- [ ] Make sure the version number in `$id` of the generic schema JSON schema file is updated
- [ ] Make sure the `"_schemaVersion"` property in the generic schema JSON schema file is updated
- [ ] Make sure the example files validate against the schema file using for example: https://www.jsonschemavalidator.net/
- [ ] Save the working copy of the schema with the file name according to the `$id` property.<br>
    For example: <br>`"$id": "https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v2.0.0.schema.json",`<br>
   &rarr; `VDA_231-301_generic_v2.0.0.schema.json`
- [ ] Create a release in the generic schema GitHub repository:
    - Go to the "Releases" section of the GitHub repository
    - Click on "Create a new release"
    - Create a tag for the release, e.g. `v2.0.0` (or use it if it already exists)
    - Title: Release v2.0.0 (or the respective version)
    - Description: Add a description of the release describing the changes made in this version
    - Attach the schema and example files to the release
    - Publish the release
- [ ] Save the schema file with the versioned filename to the `generic` folder in the schemas repository
- [ ] Push the changes to the schemas repository. A GitHub action will automatically update the GitHub pages of the schemas repository and make the new version available at the URL specified in `$id`.