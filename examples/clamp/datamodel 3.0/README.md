# so far

1. Carried out generalization (according to issue [#17](https://github.com/VDA231-301/VDA231-301/issues/17)): 
    - Renamed TestingProject -> Project
    - Split TestSeries into RequirementSet and TestSeries
    - Added Layer between TestSeries and RequirementSet to capture "Conditions" (e.g. preconditioning, test environment, etc.) TODO: find a better name, currently called "CharacteristicValues"
    - This allows documentation only projects without TestSeries to exist (e.g. Substance Declaration)

Next steps:
- Adjust generic schema / data model to reflect the changes above

Still todo before releasing the next major version 3.0:
- Color information
- VDA 210-300: Multiple source logic