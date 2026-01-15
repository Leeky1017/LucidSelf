# Change Delta — engine-id-governance (implement-engine-id-and-identity-foundation-v1)

## MODIFIED Requirements

### Requirement: 契约与标识符（Contract & IDs）
The system MUST enforce `engine_id` presence, format validity, and registry membership whenever runtime inputs reference an engine.

#### Scenario: Missing engine_id is deterministically rejected
- **WHEN** a request/job is processed without an `engine_id` where it is required
- **THEN** the system MUST reject with a deterministic reason code `MISSING_ENGINE_ID`
- **AND** the rejection MUST be recorded in an auditable form (including `version_id` and correlation identifiers when available)

#### Scenario: Unregistered engine_id is deterministically rejected
- **WHEN** a request/job is processed with an `engine_id` not present in the registry
- **THEN** the system MUST reject with a deterministic reason code `ENGINE_ID_NOT_FOUND`
- **AND** the rejection MUST be recorded in an auditable form (including `engine_id` and `version_id`)

### Requirement: 可观测与审计（Observability）
The system MUST make gate failures and runtime validations traceable by `engine_id` via logs/traces/audit records.

#### Scenario: Gate failures are traceable by engine_id
- **WHEN** validation or gate checks fail
- **THEN** logs/traces/audit records MUST include `engine_id` and `version_id` (and `user_id` when applicable)

