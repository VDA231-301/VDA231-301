# VDA 231-301 JSON Schema

Welcome to the **VDA 231-301 JSON Schema Repository**, the official home for the JSON schema recommendation for the digital exchange of material test results. This repository is maintained as part of the VDA initiative to enable an open, collaborative recommendation that supports various industry needs.
Developed jointly by the German Association of the Automotive Industry (www.vda.de), as well as the Institute for Engineering Design and Industrial Design (IKTD) at the University of Stuttgart (www.iktd.uni-stuttgart.de) and many contributors from the automotive industry.

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
