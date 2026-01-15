# Change Delta — text-normalization-alignment (implement-corpus-governance-and-normalization-v1)

## MODIFIED Requirements

### Requirement: 一致性与冲突（Consistency）
The system SHALL define normalized text artifacts and alignment reports that are reproducible and traceable to `version_id` and `corpus_release_id`.

#### Scenario: Alignment report is locatable
- **WHEN** an alignment report is produced
- **THEN** each alignment item MUST be locatable to at least `book_id`, `node_id`, and `snippet_ids` (or an equivalent paragraph locator)

### Requirement: 资产门禁验收（Asset Gate）
The system SHALL provide executable Asset-Gate acceptance commands for normalization/alignment, and failing checks MUST block promotion.

#### Scenario: Normalization outputs are validated
- **WHEN** normalized artifacts or alignment reports are missing required fields or cannot be parsed
- **THEN** the gate MUST fail deterministically and output actionable remediation evidence

