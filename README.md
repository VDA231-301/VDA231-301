# VDA 231-301 JSON Schema

Welcome to the **VDA 231-301 JSON Schema Repository**, the official home for the JSON schema recommendation for the digital exchange of material test results. This repository is maintained as part of the VDA initiative to enable an open, collaborative recommendation that supports various industry needs.
## Disclaimer

⚠️ **Important notice**

We are constantly working to improve the VDA 231‑301 recommendation.

The **current official version** of the VDA 231‑301 document is published exclusively by the VDA and is available via the **VDA Webshop**  (**German / English**).

The official document contains **additional information** that is **not part of this GitHub repository**.

---

## Language Requirement

English is the preferred language for all content.  
German content may be added where appropriate.

---

## Contents

- How to contribute  
- Disclaimer on standard copyright  
- Main repository  
- Sub‑schemas  
- Versioning  
- Branching  
- Using and generating IDs  

---

## 1. How to Contribute

See the **"How to contribute  section"** (https://github.com/VDA231-301/VDA231-301/tree/main#how-to-contribute) in the main `README.md` file of the repository.

---

## 2. Disclaimer on Standard Copyright

The content and references in this repository are based on standards whose copyrights belong to the respective standardization organizations  
(e.g. **DIN, ISO, VDA**).

⚠️ **Full standard texts must not be reproduced or published without permission.**  
Please ensure that you have the appropriate licenses when working with standard documents.

---

## 3. Main Repository

The main repository of the VDA 231‑301 JSON Schema is available here:

**VDA231‑301**  
https://github.com/VDA231-301/VDA231-301

---

## 4. Sub‑Schemas

### 4.1 General Information

This section describes the **subschema workflow repository** and the **lifecycle of subschemas** from conception to official publication.

#### Phase 1: Draft and Discussion (GitHub Repository)

Each subschema begins its lifecycle as an **independent GitHub repository**.

These repositories:
- serve as publicly accessible working drafts,
- invite discussion and collaborative development,
- collect feedback via GitHub Issues and Discussions.

Subschemas in this phase are **not yet officially versioned**.

#### Phase 2: Official Publication (Schema Repository)

Once a subschema has been reviewed and approved by the responsible **VDA Project Group (PG)**, it enters the official publication phase.

This includes:
- official versioning of the subschema,
- publication in the **central schema repository**,
- availability via a dedicated HTTPS endpoint.

✅ **Only subschemas published in the schema repository are considered officially released and versioned.**

---

### 4.1.1 Officially Released Sub‑Schemas

Currently, the following sub‑schemas are officially released:

- **EN 10204**  
  https://vda231-301.github.io/schemas/EN_10204/VDA_231-301_EN_10204_2004_Certificate_3.1_v0.2.0.schema.json
- **VDA 275**
  https://vda231-301.github.io/schemas/VDA_275/VDA_231-301_VDA_275_2021_Formaldehyde_v1.0.0.schema.json

---

### 4.1.2 Sub‑Schemas Under Review

The following sub‑schemas are currently under review:

- VDA 270  https://github.com/VDA231-301/VDA_231-301__VDA_270
- VDA 278  https://github.com/VDA231-301/VDA_231-301__VDA_278
- SEP 1240 https://github.com/VDA231-301/VDA_231-301__SEP_1240
- Substance Declaration https://github.com/VDA231-301/VDA_231-301__SubstanceDeclaration

---

### 4.2 Creating New Sub‑Schemas

Guidelines for creating new sub‑schemas are available in:
- [English](https://github.com/VDA231-301/VDA231-301/blob/main/docs/guidelines_for_creating_subschemas_VDA231-301_en.md)
- [German](https://github.com/VDA231-301/VDA231-301/blob/main/docs/guidelines_for_creating_subschemas_VDA231-301_de.md)

---

### 4.3 Level of Detail for Standards

The level of detail in a subschema may vary:

- **Must**  
  Mandatory requirements according to the standard.
- **Can**  
  Optional requirements, often defined by internal factory standards.

The JSON Schema supports **both variants** and enables flexible implementation.

---

## 5. Versioning of Schemas

Each schema must have **clear versioning**.

- Semantic versioning is used (e.g. `v1.0.0`)
- Changes must be documented in a changelog
- Schema changes are made via **pull requests** only

This ensures **consistency, traceability, and transparency**.

---

## 6. Branching

All examples must:
- include the appropriate `if` condition to represent correct logic,
- ensure that `$ref` is present for references.

---

## 7. Using and Generating IDs

IDs must be **unique and stable**.They are generated according to the pattern `<prefix>-<sequential-number>`. 

### Requirements

- Every referable object **MUST** carry an internal data ID in `_id`
- Type: `string`
- Format: **UUID v4** (RFC 4122)
- Representation: lowercase, hyphenated UUID  
  (e.g. `123e4567-e89b-12d3-a456-426655440000`)

### Stability and Uniqueness

- `_id` **MUST** be unique within a test report
- `_id` **MUST NOT** be mutated after assignment

### References

- Reference fields (e.g. `refId`, `instrumentRef`, `sampleRef`)
  **MUST** use the same type and format as `_id`

### Validation

- JSON Schema validates structure and format
- Referential integrity must be ensured via **build / CI checks**






**DISCLAIMER**: We are constantly working to improve the VDA 231-301. 
The current version of the official VDA 231-301 document can be found in the VDA Webshop ([German](https://webshop.vda.de/VDA/de/vda-231-301-022025) / [English](https://webshop.vda.de/VDA/en/vda-231-301-022025)). It contains additional information about the recommendation that is not part of this repository. 

This repository contains the generic schema and tracks changes and issues. All official releases of the generic schema and the sub-schemas are available in the [schemas repository](https://github.com/VDA231-301/schemas).

## Scope and Relation to the Official VDA Recommendation

This GitHub repository provides the **technical JSON Schema implementation** of the VDA 231-301 **recommendation** for the digital exchange of material sampling test results.  
It supports software vendors, laboratories, suppliers, and OEMs in implementing, validating, and exchanging test data in a structured and machine-readable format.

> [!IMPORTANT]
> ⚠️ **Important note:**  
This repository **does not replace and does not compete with** the official VDA 231-301 recommendation.  
The **normative and legally binding content** is published exclusively by the VDA and is available via the **VDA Webshop**.

The purpose of this repository is to provide an **open and collaborative technical reference**, including the generic schema and its evolution.  
Any changes intended to become part of the official VDA recommendation must follow the formal VDA committee and release process.

# Getting Started

## Contributing

This repository follows the organization-wide contribution and governance rules:  
https://github.com/VDA231-301/.github/blob/main/CONTRIBUTING.md

## Using the Schema

You can use the schema to:
- Validate your material test data.
- Integrate it into existing software tools.
- Develop converters, editors, or validators for the standard.

## Creating new sub-schemas
See the **guidelines  for creating sub-schemas**:
- [English](./docs/guidelines_for_creating_subschemas_VDA231-301_en.md)
- [German](./docs/guidelines_for_creating_subschemas_VDA231-301_de.md)

# Goals and Structure of the VDA 231-301 JSON Schema
The main goal of the VDA 231-301 JSON schema is to provide a standardized format for the digital exchange of material test results. The schema is designed to be generic and extensible, allowing for the representation of various test results across different standards and recommendations. 

The **generic schema** defines the basic structure of the data that all digital test reports should follow. 

Specific **sub-schemas** can be created for individual standards or recommendations, further restricting the general format to ensure that test results for the same standard can always be exchanged in the same format.

### Schemas
 
**Generic schema**
- Repository: [VDA231-301](https://github.com/VDA231-301/VDA231-301) (this repository)
- Latest version: 1.0.0
- Downloads: [schemas repository](https://vda231-301.github.io/schemas/#/generic)

### Sub-schemas
Currently, the following sub-schemas are available:

- **EN 10204** 
  - Title: "Metallic products - Types of inspection documents" 
  - Repository: [VDA_231-301__EN_10204](https://github.com/VDA231-301/VDA_231-301__EN_10204)
  - Standard source: https://webshop.vda.de/VDA/de/vda-270-052022
  - Latest version: not released yet
- **VDA 270** 
  - Title: "Determination of the odour characteristics of trim materials in motor vehicles" 
  - Repository: [VDA_231-301__VDA_270](https://github.com/VDA231-301/VDA_231-301__VDA_270)
  - Standard source: https://webshop.vda.de/VDA/de/vda-270-052022
  - Latest version: not released yet
- **VDA 278** 
  - Title: "Thermal Desorption Analysis of Organic Emissions for the Characterization of Non-Metallic Materials for Automobiles"
  - Repository: [VDA_231-301__VDA_278](https://github.com/VDA231-301/VDA_231-301__VDA_278)
  - Standard source: https://webshop.vda.de/VDA/de/vda-278-05-2016
  - Latest version: not released yet
- **SEP 1240**
  - Title: "Testing and Documentation Guideline for the Experimental Determination of Mechanical Properties of Steel Sheets for CAE-Calculations"
  - Repository: [VDA_231-301__SEP_1240](https://github.com/VDA231-301/VDA_231-301__SEP_1240)
  - Standard source: https://matplus.shop/product/sep-1240?lang=en
  - Latest version: not released yet


## Goals

The VDA 231-301 recommendation defines a generic and extensible data model for representing test results in a digital, machine-readable format. Its goals include:

- **Interoperability:** Ensure seamless data exchange across OEMs, suppliers, laboratories, and vendors.
- **Flexibility:** Allow specific norms and test protocols to define their extensions through sub-schemas.
- **Validation:** Provide a robust framework for validating test data using the JSON Schema format.

The schema and its sub-schemas are versioned and collaboratively developed here on GitHub, ensuring a transparent and open improvement process.


### Entity relationship diagram

<img src="./assets/ERM/ERM_EntitiesWithAttributes_EN.svg" alt="Entity Relationship Model (English, entities with attributes)">


### Reuse

The base schema provides `$defs` for `UuidV4` and `UuidV4Ref`. Subschemas include them via `$ref`.

**Example Base Schema Definition:**
```json
"$defs": {
  "UuidV4": {
    "type": "string",
    "format": "uuid",
    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
  }
}



{
  "_id": "123e4567-e89b-12d3-a456-426655440000",
  "instrumentRef": "987e6543-e21b-43d3-a456-426655440999"
}
