# Change Delta — cross-book-consistency-conflicts (implement-cross-book-conflicts-and-extraction-gates-v1)

## MODIFIED Requirements

### Requirement: 一致性与冲突（Consistency）
The system SHALL produce an auditable conflict report for cross-book conflicts and SHALL support deterministic blocking via configured thresholds and exception approvals.

#### Scenario: Conflicts are reported with thresholds
- **WHEN** conflict detection is executed
- **THEN** the system MUST produce a machine-readable report with counts by type and severity
- **AND** the report MUST be traceable to `version_id` and `corpus_release_id`

#### Scenario: Exceptions are auditable
- **WHEN** an exception/whitelist is applied to suppress a detected conflict
- **THEN** the applied exception MUST be recorded as a separate auditable artifact

### Requirement: 资产门禁验收（Asset Gate）
The system SHALL provide executable acceptance commands for cross-book conflict detection, and failing thresholds MUST block promotion.

#### Scenario: Threshold breach blocks promotion
- **WHEN** conflict counts exceed configured thresholds after applying approved exceptions
- **THEN** the gate MUST fail deterministically and output actionable evidence paths

