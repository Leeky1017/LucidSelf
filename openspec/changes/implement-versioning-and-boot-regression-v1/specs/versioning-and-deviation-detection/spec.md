# Change Delta — versioning-and-deviation-detection (implement-versioning-and-boot-regression-v1)

## MODIFIED Requirements

### Requirement: 契约与标识符（Contract & IDs）
The system MUST enforce `version_id` presence and validity for versioned outputs and gate artifacts, and MUST provide a minimal `corpus_release_id` scheme for traceability where corpus assets apply.

#### Scenario: Missing version_id is deterministically rejected
- **WHEN** a request/job/gate run is processed without a `version_id` where it is required
- **THEN** the system MUST reject with a deterministic reason code `MISSING_VERSION_ID`
- **AND** the rejection MUST be recorded in an auditable form

#### Scenario: Invalid version_id is deterministically rejected
- **WHEN** a request/job/gate run is processed with an invalid `version_id`
- **THEN** the system MUST reject with a deterministic reason code `INVALID_VERSION_ID`
- **AND** the rejection MUST be recorded in an auditable form

#### Scenario: corpus_release_id is captured for regression artifacts
- **WHEN** a regression/deviation artifact is produced for corpus-dependent behavior
- **THEN** the artifact MUST be traceable to `corpus_release_id` and `version_id`

### Requirement: 数据模型与完整性（Data & Integrity）
The system MUST produce machine-readable artifacts for version manifests and deviation reports, and MUST validate baseline resolvability for deviation detection.

#### Scenario: Baseline not found blocks deviation detection
- **WHEN** deviation detection is executed with a missing/unresolvable baseline reference
- **THEN** the system MUST fail deterministically with reason code `BASELINE_NOT_FOUND`
- **AND** the failure MUST be recorded in an auditable form

### Requirement: 门禁验收（Gates & Acceptance）
The system SHALL provide executable Gate-0 acceptance commands for versioning/deviation detection, and failing checks MUST block promotion.

#### Scenario: Gate-0 provides executable checks
- **WHEN** Gate-0 acceptance is executed
- **THEN** it MUST produce a pass/fail verdict and machine-readable artifacts
- **AND** failures MUST block promotion with actionable evidence
