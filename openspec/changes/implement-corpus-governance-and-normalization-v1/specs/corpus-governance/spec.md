# Change Delta — corpus-governance (implement-corpus-governance-and-normalization-v1)

## MODIFIED Requirements

### Requirement: 版本/血缘/许可（Version & License）
The system MUST provide a machine-readable corpus manifest that records inventory, license constraints, provenance, lineage, and version identifiers (`version_id`, `corpus_release_id`) for governed corpus assets.

#### Scenario: Manifest is generated and auditable
- **WHEN** corpus governance artifacts are generated for a gate run
- **THEN** the system MUST emit a compiled manifest containing `version_id` and `corpus_release_id`
- **AND** each asset MUST be traceable to a license constraint and provenance summary

### Requirement: 资产门禁验收（Asset Gate）
The system SHALL provide executable Asset-Gate acceptance commands for corpus governance, and failing checks MUST block promotion.

#### Scenario: Invalid or missing metadata blocks the gate
- **WHEN** the manifest is missing required fields, references unknown licenses, or points to non-resolvable paths
- **THEN** the gate MUST fail deterministically with actionable evidence paths

