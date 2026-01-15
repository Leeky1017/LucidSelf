# Proposal: issue-1-ls-github-bootstrap

## Why
LucidSelf needs a complete initial GitHub delivery: upload source-of-truth content, and align collaboration to the SS-style three-system workflow (OpenSpec + Rulebook + GitHub) so future changes are enforceable, auditable, and reproducible.

## What Changes
- Add LS delivery hard gates (Issue → Branch → PR → Checks → Auto-merge) and the required GitHub checks.
- Add agent delivery scripts (worktree isolation, PR preflight, auto-merge + sync, sync audit).
- Optimize `AGENTS.md` to match SS “spec-first + delivery gates” conventions.
- Upload repository contents required for LS to be built/audited (excluding local secrets/caches/artifacts).

## Impact
- Affected specs: `openspec/specs/ls-delivery-workflow/spec.md`
- Affected code: `scripts/agent_*.sh`, `scripts/agent_pr_preflight.py`, `.github/workflows/*.yml`
- Breaking change: NO
- User benefit: deterministic, enforceable delivery workflow + GitHub-hosted source-of-truth
