# Change Delta — proofreading-workflow-qa (implement-proofreading-and-corpus-release-v1)

## MODIFIED Requirements

### Requirement: QA与复核（QA & Review）
The system MUST provide a machine-readable proofreading workflow with task queue, state transitions, deterministic sampling policy, review records, and exception approvals, and MUST emit a QA report traceable to `version_id` and `corpus_release_id`.

#### Scenario: QA queue is generated deterministically
- **WHEN** QA sampling is executed for a given `version_id`/`corpus_release_id`
- **THEN** the system MUST output a machine-readable task queue with stable task identifiers
- **AND** each task MUST reference book/item identifiers (at least book_id/entry_id/snippet_ids)

#### Scenario: QA decisions are auditable
- **WHEN** a QA decision (approve/reject/exception) is recorded
- **THEN** the decision MUST be persisted as an auditable artifact
- **AND** the QA report MUST include aggregate metrics and a gate verdict

### Requirement: 资产门禁验收（Asset Gate）
The system SHALL provide executable acceptance commands for proofreading QA, and failing QA thresholds MUST block corpus promotion/release.

#### Scenario: Gate failure blocks release
- **WHEN** required QA thresholds are not met for a release attempt
- **THEN** the gate MUST fail deterministically with actionable evidence paths

