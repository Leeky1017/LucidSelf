# Change Delta – proofreading-workflow-qa (finalize-proofreading-templates-v0-1)

## ADDED Requirements

### Requirement: Proofreading templates are canonicalized to V0.1
The system MUST treat `典籍/精校模板_L1L2.md` and `典籍/texts/Western_Texts_Template.md` as the canonical proofreading templates, and MUST label them with `V0.1` as the only version marker.

#### Scenario: Templates use V0.1 only
- **WHEN** proofreading templates are prepared for release
- **THEN** they MUST NOT contain any `vX.Y` version markers
- **AND** they MUST show `V0.1` as the single version marker

### Requirement: Template references are consistent in docs
The system MUST ensure documentation references to proofreading templates use the canonical paths and refer to `V0.1` consistently.

#### Scenario: Documentation references match canonical templates
- **WHEN** documentation references proofreading templates
- **THEN** references MUST use the canonical file paths
- **AND** references MUST use the `V0.1` label consistently

