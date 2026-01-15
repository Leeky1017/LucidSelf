## 1. Implementation
- [ ] 1.1 Create run log `openspec/_ops/task_runs/ISSUE-1.md` and keep appending evidence
- [ ] 1.2 Add LS delivery OpenSpec: `openspec/specs/ls-delivery-workflow/spec.md`
- [ ] 1.3 Add agent delivery scripts: worktree + preflight + auto-merge + sync audit
- [ ] 1.4 Optimize root `AGENTS.md` to match SS delivery gates and code discipline
- [ ] 1.5 Fix `.gitignore` to exclude local secrets/caches/artifacts; ensure no secrets are committed
- [ ] 1.6 Upload LS source-of-truth content to GitHub via PR (exclude `.env`, `.venv`, `node_modules`, etc.)

## 2. Testing
- [ ] 2.1 `openspec validate --specs --strict --no-interactive`
- [ ] 2.2 Run minimal CI-equivalent checks locally: gate scripts + unit tests

## 3. Documentation
- [ ] 3.1 Ensure `README.md` and `AGENTS.md` point to OpenSpec + Rulebook + GitHub workflow
- [ ] 3.2 PR includes `Closes #1` + run log, and required checks are green
