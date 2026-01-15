## 1. Implementation
- [x] 1.1 Create OpenSpec change + validate (`openspec validate enforce-full-proofreading-cn-v1 --strict --no-interactive`)
- [x] 1.2 Implement CN full coverage: asset gate + QA workflow + Gate-2 wiring

## 2. Testing
- [x] 2.1 Verify OpenSpec strict validation (`openspec validate --specs --strict --no-interactive`)
- [x] 2.2 Verify Gate-2 script runs end-to-end (`bash scripts/gates/gate2_proofreading_and_corpus_release.sh --skip-openspec`)
- [ ] 2.3 `pytest -q` (known collection errors; see OpenSpec evidence)

## 3. Documentation
- [x] 3.1 Update `openspec/specs/proofreading-workflow-qa/acceptance.md` to reference v2 policy
- [x] 3.2 Record evidence under `openspec/changes/enforce-full-proofreading-cn-v1/evidence/`
