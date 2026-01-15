# Change Delta – proofreading-workflow-qa (enforce-full-proofreading-cn-v1)

## ADDED Requirements

### Requirement: CN classics proofreading coverage is full (100%)
The system MUST support a full-coverage proofreading QA workflow for Chinese classics, such that the QA queue covers 100% of in-scope normalized entries for each included book, and MUST exclude `记纂渊海` from the in-scope set.

#### Scenario: Generate a full-coverage QA queue for CN classics
- **WHEN** a proofreading QA queue is generated under a policy that targets Chinese classics
- **THEN** the queue MUST include exactly one task per normalized entry in scope (100% coverage)
- **AND** the queue MUST record the include/exclude scope, per-book counts, and a deterministic digest for auditability

#### Scenario: Missing coverage blocks the asset gate
- **WHEN** the QA workflow detects that coverage is missing for any in-scope CN book (e.g., missing book entries or incomplete task coverage)
- **THEN** the QA verdict MUST be `fail`
- **AND** the failure MUST be attributable to `version_id` + `corpus_release_id` with actionable diagnostics

