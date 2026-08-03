# Current Data Model Release 3.0

Status: Development Version

This document describes the current development status of the VDA 231-301 data model.

This model is not yet part of the officially released documentation.

For architecture, entities, relationships, Generic Schema and Subschemas this document supersedes older ERM diagrams contained in published documentation.

## Release 3.0 Changes

### Component

The current Release 3.0 data model defines the following ComponentMaster attributes:

- ID*
- Designation
- CustomerPartNumber
- SupplierPartNumber
- MaterialGroup (VDA 231-106)
- MaterialClass (VDA 231-200)
- MaterialName
- OemIdentifier
- MaterialIdentifiers (VDA 231-300)
- SurfaceIdentifiers (VDA 231-300)
- Specifications [List of Specification]
- Stack [Stack]
- SpecificationCustomizations [SpecificationCustomizations]
- Attachment [Attachment]
- Comment
- BusinessKeys [BusinessKey]
- Mass [Mass]
- NumberOfParts
- NGIDPath
 
The Release 3.0 model additionally supports:

- Colors
- MaterialSources
- ComponentInstances
- SubComponents

### Colors

Attributes:

- ID
- ColorName
- ColorCode
- ColorCodeAuthority
- AdditionalProperties [InformationSet]

### MaterialSources

Attributes:

- ID
- MaterialName
- TradeName
- Supplier [Location]
- Specification [Specification]
- AdditionalProperties [InformationSet]

### ComponentInstance

Attributes:

- ID*
- ProductionSite [Location]
- Machine
- Tool
- Cavity
- SerialNumber
- ProductionLotNumber
- ProductionDate [Date]
- DateOfReceipt [Date]
- Attachment [Attachment]
- Comment
- BusinessKeys [BusinessKey]
- MaterialSourceID
- ColorID

## Current ERM Diagram

The current ERM Diagram is available here:

(https://github.com/VDA231-301/VDA231-301/blob/feat/22-add-a-complete-example-including-ngid-and-3d-data/assets/ERM/ERM_EntitiesWithAttributes_EN.png)

## Usage

Use this model for all questions related to:

- Entities
- Relationships
- Generic Schema
- Subschemas
- Business Keys
- Material IDs
- Architecture decisions

The current model includes:

- Material
- MaterialSpecification
- Requirement
- TestRequirement
- TestResult
- ComponentInstance
- NGIDPath

Compared to the published documentation, the Release 3.0 model contains additional entities, relationships and modeling concepts, including support for multiple material sources and enhanced color information.

This document represents the latest available Release 3.0 development status and should be preferred for technical modeling questions if differences exist compared to older published documentation.

For technical modeling questions, this document shall be considered the authoritative source for the current Release 3.0 development status.
