# Change Delta — observability-slos (implement-security-and-observability-v1)

## MODIFIED Requirements

### Requirement: 可观测与审计（Observability）
The system MUST provide end-to-end correlation across logs/metrics/traces using `request_id` and `trace_id`, and MUST make core service health and SLO signals executable and observable.

#### Scenario: Request correlation identifiers are present and propagated
- **WHEN** an API request is processed
- **THEN** logs MUST include `request_id` and `trace_id` (and `user_id/org_id/engine_id/version_id` when applicable)
- **AND** the response MUST include `X-Request-ID` and `X-Trace-ID` for client-side correlation

#### Scenario: Core request metrics are exportable without high-cardinality labels
- **WHEN** metrics are scraped for Gate-0 validation
- **THEN** the service MUST export core metrics including `ls_requests_total` and `ls_request_duration_ms`
- **AND** metrics MUST NOT include high-cardinality identifiers (`user_id/org_id/request_id/trace_id/version_id`) as default labels

#### Scenario: Readiness checks can block on missing dependencies
- **WHEN** `/ready` is queried while a required dependency is unavailable or misconfigured
- **THEN** the service MUST return a deterministic not-ready result with actionable reasons
- **AND** the block MUST be observable via logs/metrics and recorded as an audit event when applicable

