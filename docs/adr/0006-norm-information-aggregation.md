## Norm information is aggregated into one embedded Specification entity per material/surface

Status: accepted

### Context and Problem Statement

VDA 231-300 describes a regulation reference (for a material or a surface) as a set of
individual, flat JT attributes: regulation type (MAT\_02/SUR\_02), regulation number
(MAT\_03/SUR\_03), legal authority (MAT\_04/SUR\_04), issue date (MAT\_05/SUR\_05),
short name (MAT\_06/SUR\_06), features according to the regulation (MAT\_07/SUR\_07)
and further applicable regulations (MAT\_11/SUR\_11).  
In the source systems these values are not stored field by field: the CAD material list
(and the surface database) keep the regulation as a **combined string** in a single column,
e.g. DIN EN 10263-4 or OEMSPEC 4104.00. The issue date and legal authority are usually
not present in these lists at all.  
The question arose how this normative information should be represented in the generic
schema v3.0.0: as flat attributes mirroring the JT fields, or aggregated into a dedicated
structure, and where the parsing/derivation of the combined string should happen.

### Decision Drivers
- One material or surface can reference several regulations (a basic standard plus further
applicable ones, MAT\_11/SUR\_11), so the model must support multiplicity.
- The regulation reference must stay machine-readable and queryable (type, number, subnumber),
not a free-text blob, so downstream systems can resolve and validate it.
- The mapping from a combined source string to the individual fields must be reproducible and
documented (see parsing rules), not implicit.
- Mandatory VDA 231-300 fields (\_04 authority, \_05 issue date) must have a defined target.
- Definitions should not be duplicated; the same pattern must work for materials and surfaces.

### Considered Options
- Keep the flat JT attributes one-to-one as individual fields on ComponentMaster.
- Store the regulation reference as a single free-text string (as in the source list).
- Aggregate all regulation fields into one embedded Specification entity and reference it
from ComponentMaster (list of specifications), populated via defined parsing rules.

### Decision Outcome

Chosen option: "Aggregate the norm information into one embedded Specification entity per
material/surface", because it is the only option that keeps the reference machine-readable,
supports several regulations per material/surface, and reuses one consistent structure for
both materials and surfaces.  
The target schema baseline is the generic schema v3.0.0. The
`Specification` entity aggregates norm information in one consistent,
machine-readable structure. The modelling decision includes the attributes
`Type`, `Number`, `SubNumber`, `IssueDate`, `Title`, `FeatureText`,
`FeatureList`, `CharacteristicRequirements`, `DOI`,
`ReferencedSpecifications`, and `Authority`.

The norm information is aggregated as follows:
- MAT\_02/SUR\_02 (regulation type)    -\> Specification.Type
- MAT\_03/SUR\_03 (regulation number)  -\> Specification.Number (+ SubNumber)
- MAT\_04/SUR\_04 (legal authority)    -\> Specification.Authority (optional; see below)
- MAT\_05/SUR\_05 (issue date)         -\> Specification.IssueDate
- MAT\_06/SUR\_06 (short name)          -\> ComponentMaster.MaterialClass (see ADR 0008);
Specification.Title holds the title of the norm itself, not the material short name
- MAT\_07/SUR\_07 (features)            -\> Specification.FeatureText / FeatureList;
quantitative or qualitative characteristics are read out to
Specification.CharacteristicRequirements (see ADR 0007)
- MAT\_11/SUR\_11 (further regulations) -\> Specification.ReferencedSpecifications  
The MAT\_01/SUR\_01 internal identifier is not part of the Specification; it is held on the
ComponentMaster as a typed identifier (see ADR 0009), together with norm-defined identifiers
such as the steel material number.  
The split of the combined source string into Type / Number / SubNumber follows the
documented parsing rules (longest-known-prefix match; . = internal execution/issue status,
\- = part of a DIN/EN standard). The issue date (\_05) maps directly to the mandatory
Specification.IssueDate field.  
The legal authority (\_04) **is stored as an optional attribute on Specification
(Specification.Authority)**. When a value is present, the explicitly stored value is
authoritative (leading). When it is absent, it may be derived from the regulation type via a
maintained lookup table (DIN -\> DIN e.V., DIN EN -\> DIN e.V./CEN, ISO -\> ISO, ...) as an
**optional fallback**. This keeps the reference lossless, aligns the ADR with the norm-string
parsing rules (LEGAL\_AUTHORITY -\> Specification.Authority) and the reference implementation
that emits this field, and still avoids requiring the (often unavailable) authority in the
source lists.  
The pattern shall be applied consistently: any regulation-like reference (material or surface)
is aggregated into Specification, and a material/surface that cites several regulations is
represented by one primary Specification plus entries in ReferencedSpecifications.

### Consequences
- Good, because the regulation reference stays machine-readable and validatable
(type/number/subnumber/issue date/authority), enabling downstream resolution and completeness checks.
- Good, because several applicable regulations per material/surface are supported through
one reusable structure shared by materials and surfaces.
- Good, because the derivation from the combined source string is reproducible and documented,
and all mandatory VDA 231-300 fields have a defined target.
- Good, because ADR 0006, the norm-string parsing rules (LEGAL\_AUTHORITY -\> Specification.Authority)
and the reference implementation now describe the **same output contract** for the legal authority,
resolving the previously reported inconsistency.
- Neutral, because Specification.Authority is nullable/optional; it is typically populated by the
source or during the sampling (Bemusterung), and the authority lookup remains available as a fallback.
- Neutral, because a parsing/derivation step is still required at import time; unknown prefixes must
be caught and reported rather than silently mapped, and the authority lookup must be maintained
for the fallback case.

### More Information

Related: ADR 0005 (self-reference for ReferencedSpecifications), ADR 0007 (read-out of
characteristics into CharacteristicRequirements), ADR 0008 (short name to MaterialClass),
ADR 0009 (typed identifiers, no duplication), and the norm-string parsing rules
(Parsing-Regeln\_Norm-Strings.md).
