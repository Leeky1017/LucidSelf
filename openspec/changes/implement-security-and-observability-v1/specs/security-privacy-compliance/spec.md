# Change Delta — security-privacy-compliance (implement-security-and-observability-v1)

## MODIFIED Requirements

### Requirement: 可观测与审计（Observability）
The system MUST emit auditable security/compliance signals (logs/metrics/audit records) that can be correlated by `request_id/trace_id` and scoped by `user_id/org_id` without leaking unnecessary sensitive content.

#### Scenario: Sensitive content is minimized in logs and audit summaries
- **WHEN** the system logs security/compliance events (including auth failures and blocking decisions)
- **THEN** logs and audit summaries MUST NOT include unnecessary sensitive raw content (e.g., emails, tokens, secrets, or free-form user text)
- **AND** correlation identifiers (`request_id/trace_id`) MUST be present when available

#### Scenario: Audit records are exportable as NDJSON with required fields
- **WHEN** Gate-0 acceptance exports audit records
- **THEN** the export MUST be NDJSON where each line is valid JSON
- **AND** each record MUST include required fields (`audit_id`, `created_at`, `event_type`, `result`)

