# Approval Entry

## Business Scenario

Material approval and listing information has its own lifecycle and must remain
traceable independently of the material master data.

An approval or listing does not necessarily apply to a general material such as
PP-GF30 as a whole. It may apply to a specific trade type from a specific
material source and may be restricted to:

- a material specification or product version
- a geographic region
- a production location
- a specific production line
- a defined validity period

Different material sources for the same general material can therefore have
different approval statuses, scopes and validity periods.

This example illustrates how an independent approval entry could reference a
specific material source from the related
../material-catalog-entry/README.md.

All names, values, dates, identifiers, suppliers, locations, production lines
and approval information are fictional and fully anonymized.

> Important framing: The structures shown in this example are discussion
> proposals. `ApprovalEntry` and its related attributes are not part of the
> released VDA 231-301 generic schema v3.0.0. The JSON file is intentionally not
> schema-conformant.

## Objective

This example demonstrates how approval and listing information could be
represented as an independent and referencable business object.

The proposed approach separates:

1. the reusable material definition
2. the supplier- and trade-name-specific material source
3. the approval or listing decision
4. the application of the material in a PLM or product context

This separation allows material master data, approval information and product
data to be maintained in separate systems while remaining connected through
stable identifiers.

## Referenced Material Source

The approval entry refers to the following material source in the related
../material-catalog-entry/componentMaster-catalog-entry.json:

```json
{
  "_id": "b1a00000-1111-4111-8111-000000000001",
  "_type": "MaterialSource",
  "MaterialName": "PP-GF30",
  "TradeName": "Example PP-GF30 Grade A"
}
