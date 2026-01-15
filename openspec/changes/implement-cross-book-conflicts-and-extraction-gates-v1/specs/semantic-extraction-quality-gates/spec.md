# Change Delta — semantic-extraction-quality-gates (implement-cross-book-conflicts-and-extraction-gates-v1)

## MODIFIED Requirements

### Requirement: 数据模型与完整性（Data & Integrity）
The system MUST version and apply semantic extraction validation rules, and MUST emit a machine-readable quality report traceable to `version_id` and `corpus_release_id`.

#### Scenario: Ruleset is versioned and referenced
- **WHEN** a quality gate run is executed
- **THEN** the run MUST reference a ruleset version identifier
- **AND** the produced report MUST include the ruleset version and the gate verdict

### Requirement: 门禁验收（Gates & Acceptance）
The system SHALL provide executable Gate-1 acceptance commands for semantic extraction quality gates, and failing checks MUST block promotion.

#### Scenario: Minimum blocking set is enforced
- **WHEN** validation produces any ERROR-class finding in the minimum blocking set
- **THEN** the gate MUST fail deterministically with actionable remediation evidence

