# ISSUE-7
- Issue: #7
- Branch: task/7-calibration-v3-upgrade
- PR: https://github.com/Leeky1017/LucidSelf/pull/8

## Plan
- 新建精校模板 V3.0（中英文）及深度级别定义
- 删除旧版模板文件（V3.0 是全新设计，非旧版优化）
- 删除旧版精校卡（001-020），保留标杆卡（exemplar）

## Runs

### 2026-01-27 精校模板 V3.0 升级
- Command: `git rm` 删除旧版模板和旧版精校卡
- Key output:
  - 删除: `CALIBRATION_TEMPLATE_CN.md`, `CALIBRATION_TEMPLATE_EN.md`
  - 删除: `zpzq_yinyang_shengke_001.md` ~ `020.md`, `zpzq_new_candidates.md`
  - 新增: `CALIBRATION_TEMPLATE_CN_V3.md`, `CALIBRATION_TEMPLATE_EN_V3.md`
  - 新增: `CALIBRATION_DEPTH_LEVELS.md`
  - 新增: `zpzq_yinyang_shengke_exemplar.md` (标杆精校卡)
  - 更新: `CALIBRATION_STRATEGY.md` (V3.0 更新说明)
- Evidence: `git status --short` 输出确认所有文件变更
