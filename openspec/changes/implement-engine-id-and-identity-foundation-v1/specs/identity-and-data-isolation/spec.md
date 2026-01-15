# Change Delta — identity-and-data-isolation (implement-engine-id-and-identity-foundation-v1)

## MODIFIED Requirements

### Requirement: 契约与标识符（Contract & IDs）
The system MUST derive `user_id` and `org_id` from authentication for protected operations and MUST NOT rely on client-supplied identity for authorization decisions.

#### Scenario: Auth-derived identity claim is used
- **WHEN** an authenticated request is processed
- **THEN** the request context MUST include `user_id` and `org_id`
- **AND** all data access MUST be scoped to that `user_id` and `org_id`

#### Scenario: Cross-tenant access is blocked and auditable
- **WHEN** a request attempts to access a resource outside its `org_id` scope
- **THEN** the system MUST deny with a deterministic reason code `CROSS_TENANT_ACCESS`
- **AND** the system MUST emit an auditable isolation-violation event

