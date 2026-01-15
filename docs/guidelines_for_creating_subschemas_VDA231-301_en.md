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

Sub-schemas validate the presence of required test data by checking the `TestSeries` array. There are two primary approaches for this validation:

#### Approach 1: Matching by TestType

When the standard defines specific test types, use the `TestType` property to identify relevant test series:
```json
{
  "allOf": [
    {
      "$ref": "https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v0.2.0.schema.json"
    },
    {
      "properties": {
        "TestSeries": {
          "type": "array",
          "contains": {
            "type": "object",
            "properties": {
              "TestType": {
                "const": "Thermodesorption"
              }
            },
            "required": ["TestType"]
          }
        }
      }
    }
  ]
}
```

For standards requiring multiple test types (e.g., EN 10204 requiring both chemical composition and tensile testing), use `allOf` with multiple `contains`:
```json
{
  "properties": {
    "TestSeries": {
      "type": "array",
      "allOf": [
        {
          "contains": {
            "type": "object",
            "properties": {
              "TestType": {
                "const": "Optical Emission Spectroscopy"
              }
            },
            "required": ["TestType"]
          }
        },
        {
          "contains": {
            "type": "object",
            "properties": {
              "TestType": {
                "const": "Tensile testing"
              }
            },
            "required": ["TestType"]
          }
        }
      ]
    }
  }
}
```

#### Approach 2: Matching by Specification

When test series are identified by the standard specification itself, match against the `Specification` object:
```json
{
  "properties": {
    "TestSeries": {
      "type": "array",
      "contains": {
        "type": "object",
        "properties": {
          "Specification": {
            "type": "object",
            "properties": {
              "Authority": { "const": "VDA" },
              "Number": { "const": "278" }
            },
            "required": ["Authority", "Number"]
          }
        },
        "required": ["Specification"]
      }
    }
  }
}
```

#### Approach 3: Matching by both TestType AND Specification

For stricter validation, require matching on both TestType and Specification properties simultaneously:
```json
{
  "properties": {
    "TestSeries": {
      "type": "array",
      "contains": {
        "type": "object",
        "properties": {
          "TestType": { "const": "Thermodesorption" },
          "Specification": {
            "type": "object",
            "properties": {
              "Authority": { "const": "VDA" },
              "Number": { "const": "278" }
            },
            "required": ["Authority", "Number"]
          }
        },
        "required": ["TestType", "Specification"]
      }
    }
  }
}
```

This approach ensures maximum consistency by requiring both the test type and the standard specification to be explicitly defined and match the expected values.


#### Important Notes:
- The `required` property is essential in each `contains` block to ensure the matched objects actually have the specified properties
- The `contains` keyword ensures at least one array item matches the criteria
- Using `allOf` with multiple `contains` requires all specified test types to be present
- Sub-schemas can combine these conditions with additional property restrictions using `$ref` to reference detailed test series definitions

---

## 6. AI-Assisted Creation of sub-schemas
AI tools can be used to assist in the creation of sub-schemas. They can help with:
- Generating initial drafts based on the standard's documentation.
- Suggesting property names and structures.
- Generating example JSON files.

When using an AI tool, it must be ensured that the contents of the standard are not made publicly available. Therefore, only protected AI tools may be used.
If the underlying standard cannot be read or interpreted, the AI process must be terminated. Do not make assumptions or estimations.

However, it is crucial to have human oversight to ensure accuracy, compliance with the guidelines, and proper representation of the standard.

### Example prompt for AI tools:
```
There is a project based on JSON schema that aims to provide a standard way for digital test results to be represented and exchanged. 
Here's the link to the project:
https://raw.githubusercontent.com/VDA231-301/VDA231-301/refs/heads/main/README.md
Look especially at this guide: https://raw.githubusercontent.com/VDA231-301/VDA231-301/refs/heads/main/docs/guidelines_for_creating_subschemas_VDA231-301_en.md
And this specific sub-schema:
https://vda231-301.github.io/schemas/EN_10204/VDA_231-301_EN_10204_2004_Certificate_3.1_v0.2.0.schema.json
Now I want you to create a new sub-schema for the standard "<Insert name / title of you standard here>".
I will upload the PDF document for this standard.
I will also provide a sample test report PDF document based on the standard to help you create the sub-schema and example files.
Please make sure the sub-schema follows the guidelines provided in the link above and captures all relevant information from the <Insert name of your standard here> standard.
Create a JSON schema document and an example JSON test report file based on the new sub-schema.
The example must validate against the created sub-schema, which also means it must validate against the generic VDA 231-301 schema found here: https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v0.2.0.schema.json (This requirement is crucial and listed in the guidelines, it must be achieved via "allOf" referencing the generic schema).
```

> **Note:** When using this prompt, please replace `<Insert name / title of you standard here>` and `<Insert name of your standard here>` with the actual name of the standard you are working on and attach two PDF documents: one for the standard and one for a sample test report based on that standard.

## 7. Publication and Review

- New sub-schemas can be proposed to the project group (PG) in the VDA at any time.
- The submission process is documented in the repository: [process diagramm](../assets/process%20flows/process_flow_release_of_new_specialised_schemas_DE.svg)
- Publication takes place after successful review by the PG.

---

> **Tip:** Take a look at the existing examples and the generic base schema in the GitHub repository to adopt the structure and conventions.
