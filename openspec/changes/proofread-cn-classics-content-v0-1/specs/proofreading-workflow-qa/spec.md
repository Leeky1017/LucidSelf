# Change Delta – proofreading-workflow-qa (proofread-cn-classics-content-v0-1)

## ADDED Requirements

### Requirement: CN proofreading markdown assets conform to the canonical template
The system MUST treat `典籍/精校模板_L1L2.md` (V0.1) as the canonical proofreading template for Chinese classics, and MUST ensure each in-scope CN proofreading markdown asset contains L1 + L2 + factor-layer structures (including required markers) before it is considered complete for release.

#### Scenario: A CN proofreading file is structurally complete
- **WHEN** a CN proofreading markdown file under `典籍/中文典籍/<book>/编辑/` is accepted as “complete”
- **THEN** it MUST contain `<!-- L1_BEGIN -->` and `<!-- L1_END -->`
- **AND** it MUST contain `<!-- L2_BEGIN -->` and `<!-- L2_END -->`
- **AND** it MUST contain `<!-- FACTOR_BEGIN -->` and `<!-- FACTOR_END -->`

#### Scenario: Template references are canonical
- **WHEN** a CN proofreading markdown file references its proofreading template or version
- **THEN** it MUST reference `典籍/精校模板_L1L2.md` as the canonical template
- **AND** it MUST use `V0.1` as the version marker (no `v2.x` markers)

