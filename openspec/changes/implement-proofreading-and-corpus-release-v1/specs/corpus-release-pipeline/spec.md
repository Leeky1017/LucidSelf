# Change Delta — corpus-release-pipeline (implement-proofreading-and-corpus-release-v1)

## MODIFIED Requirements

### Requirement: 数据模型与完整性（Data & Integrity）
The system MUST define a reproducible corpus release package that includes a versioned manifest and content hashes, and MUST bundle or reference the required gate reports, traceable to `version_id` and `corpus_release_id`.

#### Scenario: Release package is self-validating
- **WHEN** a release package is generated
- **THEN** the package MUST include a machine-readable manifest with sha256 hashes for included artifacts
- **AND** a validation command MUST be able to verify integrity deterministically

### Requirement: 门禁验收（Gates & Acceptance）
The system SHALL provide executable Gate-2 acceptance commands for publish/validate/rollback, and failing checks MUST block promotion.

#### Scenario: One-click publish/validate/rollback
- **WHEN** publish/validate/rollback commands are executed
- **THEN** the system MUST emit auditable reports and artifacts for each action
- **AND** failures MUST block deterministically with actionable remediation evidence

