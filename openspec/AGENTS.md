# LucidSelf OpenSpec Instructions (Authoritative)

This file defines how AI assistants MUST use OpenSpec in the LucidSelf (LS) repository.

## Absolute Rules

- Always treat `openspec/project.md` as the top-level constitution.
- Specs are the authoritative definition of behavior and contracts.
- Changes are proposals (planned deltas) and MUST validate strictly before implementation.
- Do not implement new capabilities or behavior changes without an approved change proposal.
- Do not embed implementation details, pseudocode, or interface implementations inside specs.
- Always keep wording normative and testable: SHALL/MUST/SHOULD/MAY.

## Required OpenSpec Format (Strict Mode)

All specs MUST pass:

```bash
openspec validate --specs --strict --no-interactive
```

### Spec structure (mandatory)

- Each spec file MUST be: `openspec/specs/<capability>/spec.md`
- Each `spec.md` MUST contain:
  - `## Purpose`
  - `## Requirements`

### Requirement structure (mandatory)

Under `## Requirements`:

- Each requirement MUST be a level-3 heading: `### Requirement: <name>`
- The first non-empty line under the requirement heading MUST contain `SHALL` or `MUST`
- Each requirement MUST contain at least one scenario section

### Scenario structure (mandatory)

- Each scenario MUST be a level-4 heading: `#### Scenario: <name>`
- Each scenario MUST have non-empty content (bullets recommended)

Recommended scenario format:

```markdown
#### Scenario: Descriptive name
- **WHEN** ...
- **THEN** ...
- **AND** ...
```

## Directory Model (Official)

```
openspec/
├── project.md
├── AGENTS.md
├── specs/
│   └── <capability>/
│       └── spec.md
└── changes/
    ├── <change-id>/
    │   ├── proposal.md
    │   ├── tasks.md
    │   ├── design.md            # optional
    │   └── specs/
    │       └── <capability>/
    │           └── spec.md      # delta format (ADDED/MODIFIED/REMOVED/RENAMED)
    └── archive/
```

## Workflow (Three Stages)

### Stage 1 — Propose (Create a Change)

Create a change proposal when the work:
- Adds new capabilities or user-visible features
- Modifies behavior, contracts, schemas, or outputs
- Changes architecture, security posture, or performance characteristics
- Changes corpus assets, citations, semantic extraction, or KG behavior

Create `openspec/changes/<change-id>/` with:
- `proposal.md`: why, what changes, impact, risks, rollout/rollback
- `tasks.md`: an ordered, checkable implementation plan
- `design.md` (optional): only when decisions must be fixed before coding
- `specs/<capability>/spec.md`: delta specs

Delta spec format (mandatory):

```markdown
## ADDED Requirements
### Requirement: ...
The system SHALL ...

#### Scenario: ...
- **WHEN** ...
- **THEN** ...

## MODIFIED Requirements
### Requirement: ...
The system MUST ...

#### Scenario: ...
- **WHEN** ...
- **THEN** ...

## REMOVED Requirements
- `### Requirement: ...`

## RENAMED Requirements
- FROM: `### Requirement: Old name`
- TO: `### Requirement: New name`
```

Validation (mandatory):

```bash
openspec validate <change-id> --strict --no-interactive
```

### Stage 2 — Implement (Execute the Change)

Implementation MUST follow the validated change proposal:

1. Read `openspec/project.md`
2. Read `openspec/changes/<change-id>/proposal.md`
3. Read `openspec/changes/<change-id>/tasks.md`
4. Implement tasks in order
5. Ensure every task is completed (no partials, no silent skips)
6. Run validations and regressions required by the change

### Stage 3 — Archive (Close the Loop)

After the change is deployed and verified:

- Archive the change under `openspec/changes/archive/` with a date prefix.
- Update `openspec/specs/<capability>/spec.md` to reflect the new truth (what IS built).
- Validate strictly:

```bash
openspec validate --specs --strict --no-interactive
```

## Naming Conventions

### Capability names (`openspec/specs/<capability>/`)

- Use kebab-case
- Single purpose per capability (split if the capability name needs “AND” to make sense)
- Prefer domain nouns for stable areas (e.g., `semantic-layer-core`, `corpus-release-pipeline`)

### Change IDs (`openspec/changes/<change-id>/`)

- Use kebab-case
- Verb-led prefix recommended: `add-`, `update-`, `remove-`, `refactor-`, `fix-`
- Must be unique and descriptive

## LS-Specific Quality Discipline

- Evidence-first: any authoritative output MUST be traceable to citations and evidence_chain.
- Reproducibility-first: outputs MUST be attributable to version identifiers (versions, corpus releases, model/prompt versions).
- Identity-first: all user data writes/reads MUST be scoped by real user identity.
- No default mock paths in production mode.

