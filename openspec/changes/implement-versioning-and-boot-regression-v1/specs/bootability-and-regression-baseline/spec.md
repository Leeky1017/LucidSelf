# Change Delta — bootability-and-regression-baseline (implement-versioning-and-boot-regression-v1)

## MODIFIED Requirements

### Requirement: 数据模型与完整性（Data & Integrity）
The system MUST define and execute startup checks and regression baselines as machine-readable artifacts, traceable to `version_id`.

#### Scenario: Startup checks are materialized as artifacts
- **WHEN** the service starts or readiness is evaluated
- **THEN** the system MUST produce a startup check list with PASS/FAIL/SKIP
- **AND** failed required checks MUST be explainable via a reason code

#### Scenario: Regression suite baseline is materialized as artifacts
- **WHEN** a regression run is executed for a `version_id`
- **THEN** the system MUST produce a regression suite baseline and a version link report
- **AND** the artifacts MUST be traceable to `version_id`

### Requirement: 门禁验收（Gates & Acceptance）
The system SHALL define hard boot failure conditions and ensure readiness reflects them; failures MUST block Gate-1 promotion.

#### Scenario: Boot fails on invalid configuration
- **WHEN** the service starts with invalid configuration for required dependencies
- **THEN** startup MUST fail or be marked not-ready with reason code `STARTUP_CHECK_FAILED`

#### Scenario: Boot fails when migrations are not applied
- **WHEN** the service starts while required schema migrations are not applied
- **THEN** startup MUST fail or be marked not-ready with reason code `STARTUP_CHECK_FAILED`

#### Scenario: Regression failures block promotion
- **WHEN** regression execution fails or drift exceeds configured thresholds
- **THEN** the system MUST block promotion with reason code `REGRESSION_FAILED`
- **AND** a machine-readable report MUST be produced for remediation

