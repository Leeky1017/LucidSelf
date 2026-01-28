# Change Delta – corpus-governance (add-zpzq-calibration-cards-p0-b01)

## ADDED Requirements

### Requirement: Calibration cards are governed corpus assets
The system MUST treat `典籍/calibrated/cards/**` as governed corpus assets and MUST require each calibration card to conform to the canonical template `典籍/CALIBRATION_TEMPLATE_CN.md` (flat output).

#### Scenario: A calibration card is structurally valid and traceable
- **WHEN** a calibration card under `典籍/calibrated/cards/<book_abbr>/` is accepted as complete
- **THEN** it MUST include sections `A` through `F` (Entry Metadata / Factor Extraction / Rule Drafts / Narrative Snippets / Cross-System Mapping / Term Alignment)
- **AND** it MUST include a `source_anchor` that can precisely locate the source (at minimum `path:line`)
- **AND** it MUST quote `source_text` verbatim (no character modifications)
- **AND** it MUST include at least:
  - B: 3 factor rows
  - C: 1 rule row
  - D: 1 narrative row
  - E: 1 mapping row
  - F: 1 term alignment row

#### Scenario: Factor IDs are aligned or explicitly proposed
- **WHEN** a factor row is recorded in a calibration card
- **THEN** `factor_id` MUST match an existing ID in `典籍/因子本体/**`
- **OR** it MUST be marked as `new_candidate` and provide a suggested ID that follows the repository naming conventions

