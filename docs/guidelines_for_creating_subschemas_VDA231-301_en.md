# Instructions: sub-schema Creation according to VDA 231-301 (English)

## 1. Purpose and Goal of a sub-schema

A sub-schema serves to precisely define the contents of a specification and to further restrict the general format of the base schema. This ensures that test results for a specific specification can always be exchanged in the same format. The sub-schema defines:

- Which attribute-value pairs are permitted (nomenclature of the specification)
- Which attributes must be included
- That compatibility with the base schema is maintained. Successful validation against a sub-schema means that the testing project contains data for the specified specification. Documents should still always be validated against the base schema to ensure overall compliance.

---

## 2. Procedure for sub-schema Creation

- **Standard Data Modeling:** Follow best practices, but a compromise must be found between practicality and level of detail.
- **Units:** SI or metric units are recommended, but not mandatory.
- **Tables:** Are mapped as arrays. If arrays are to be validated, the table definition (columns/rows) must be done exactly in the sub-schema. If a precise definition of the properties is required, e.g., a carbon content must always be specified, the results (`SingleResults` & `ConsolidatedCharacteristicValues`) should not be modeled as `InformationSet`, but in the stricter form `SingleResultPoint` or `CharacteristicValuePoint`.
- **Technical properties:** The `_id` and `_type` properties should be included in sub-schemas for all objects that also have them in the base schema. sub-schemas can add relations using pointers to an entities' `_id` property like for example the `ComponentInstanceID` in the base schema.

---

## 3. Naming and Prefixing
### Naming
- Each sub-schema receives a unique identifier, usually related to the standard, e.g., "
VDA278" for results of thermodesorption or "EN10204" for 3.1 test certificates.
- This identifier is used in the file name and URL structure to uniquely identify the sub-schema.

### File names
- The file name of the sub-schema:
  - must include the unique identifier
  - must end with `.schema.json`.
  - can include additional information such as the year of the standard (e.g. EN 10204:2004 ->  `VDA_231-301_EN10204_2004_Certificate_3.1.schema.json`.
  - should use underscores (`_`) instead of spaces.
  - must not contain the version number in the file name (only the files in the delivery repo contain the version).
  - Example: `VDA_231-301_VDA278_Thermodesorption.schema.json`

- The file name of the example JSON file:
  - must have the same base file name as the sub-schema it belongs to
  - must end with  `.example.json` to indicate that it is an example file.
  - Example: `VDA_231-301_VDA278_Thermodesorption.example.json`

### $id Property

Important: The $id property must follow the format:

`https://vda231-301.github.io/schemas/{NAME}/VDA_231-301_{NAME}[_ADDITIONAL_INFO]_v{VERSION}.schema.json`

where:
- `{NAME}` is the unique identifier of the sub-schema (e.g., `VDA278`, `EN10204`).
- `[_ADDITIONAL_INFO]` is optional and can include further details like the year of the standard or specific test series.
- `{VERSION}` is the version number of the sub-schema.

This is important to ensure that each sub-schema can be uniquely identified and accessed.
Released versions of all schemas are stored in the [schemas repository](https://github.com/VDA231-301/schemas) and will always be accessible at the same URL.

```json
{
  "$id": "https://vda231-301.github.io/schemas/VDA_278/VDA_231-301_VDA_278_v0.1.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for VDA 278"
}
```

```json
{
  "$id": "https://vda231-301.github.io/schemas/EN_10204/VDA_231-301_EN_10204_2004_Certificate_3.1_v0.2.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for EN_10204_2004_Certificate_3.1"
}
```

### Prefixing
- Additionally, each sub-schema can use prefixes in the definitions in the JSON schema file to avoid naming conflicts or to clarify affiliation.
- Example:
  - In the schema `VDA278`:
  ```json
  {
    "VDA278.ProcessDataPreconditioningEndDate": {
      "type": "object",
      "properties": {
        "Property": {
          "const": "End date"
        },
        "Value": {
          "$ref": "#/$defs/Generic.Date"
        }
      }
    }
  }
  ```
  - In the schema `EN10204`, different prefixes are used to distinguish the individual test series (tensile test and chemical composition):
  ```json
  {
   "3-1_Certificate.ChangeOfWidth": {
      "properties": {
        "Property": {
          "const": "Change of Width"
        },
        "Unit": {
          "const": "mm"
        }
      },
      "required": [
        "Property",
        "Unit"
      ],
      "type": "object"
    },
     "3-1_Composition_Certificate.SubstanceCAS": {
      "properties": {
        "Property": {
          "const": "Substance CAS"
        }
      },
      "required": [
        "Property"
      ],
      "type": "object"
    },
    "3-1_Tensile_Certificate.TestSeries": {
      ...
    }
  }
  ```
---

## 5. Technical Implementation

### Reference to the Generic Schema
Sub-schemas must reference the generic schema version they are based on using JSON pointers (`$ref`).
The root of the sub-schema must use `allOf` to include the base schema and can then define additional properties or restrictions.

Example:

```json
{
  "$id": "https://vda231-301.github.io/schemas/VDA_278/VDA_231-301_VDA_278_v0.1.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for VDA 278",
  "allOf": [
    {
      "$ref": "https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v0.2.0.schema.json"
    }
  ],
  "type": "object",
  "properties": {
    ...
  }
}
```

### Conditional Logic for applicability of the sub-schema

Goal: The sub-schema should only apply if the test report contains data for the specific standard. That means if a test report JSON is successfully validated against the sub-schema, it contains data for the specified standard.

This will be documented soon.

---

## 6. Publication and Review

- New sub-schemas can be proposed to the project group (PG) in the VDA at any time.
- The submission process is documented in the repository: [Contribution process diagram](./assets/process%20flows/process_flow_release_of_new_specialised_schemas_EN.svg)
- Publication takes place after successful review by the PG.

---

> **Tip:** Take a look at the existing examples and the generic base schema in the GitHub repository to adopt the structure and conventions.