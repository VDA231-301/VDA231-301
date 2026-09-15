# Elastomer Material with Characteristic Requirements

## Business Scenario

An OEM material specification defines multiple possible material variants and
requirement levels. For a specific material definition, additional
characteristics determine the applicable requirement profile.

In this example, an elastomer material is required to have a Shore A hardness
of 70 ± 5 and a minimum tensile strength of 8 MPa. These values are
requirements, not measured test results.

## Objective

This example demonstrates how machine-readable characteristic requirements
are assigned to a `Specification`. The requirements complement the
specification reference and provide the target values from which a test plan
can be derived.

## When to Use This Example

Use this example when a specification reference alone does not fully describe
the applicable requirement profile and additional quantitative or qualitative
requirements must be represented in a structured, machine-readable form.

Do not use this example for measured test results or for an
application-specific deviation from the referenced specification.
