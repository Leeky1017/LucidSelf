# ISSUE-30

- Issue: #30
- Branch: task/30-qtbj-r21-r30
- PR: <fill-after-created>

## Plan

- 对《穷通宝鉴》执行 R21-R30 精校任务
- 产出 11 张 Deep 级别精校卡（五行总论 + 十天干分论）
- 按 CALIBRATION_TEMPLATE_CN_V3.md 模板执行

## Runs

### 2026-01-28 创建任务环境
- Command: `gh issue create` + `scripts/agent_worktree_setup.sh 30 qtbj-r21-r30`
- Key output: Issue #30 created, worktree at `.worktrees/issue-30-qtbj-r21-r30`
- Evidence: https://github.com/Leeky1017/LucidSelf/issues/30

### 2026-01-28 精校产出
- Command: 按 Deep 模板精校 11 张卡
- Key output:
  - `qtbj_r21_wuxing_001.md` - 五行总论
  - `qtbj_r22_jia_001.md` - 甲木
  - `qtbj_r23_yi_001.md` - 乙木
  - `qtbj_r24_bing_001.md` - 丙火
  - `qtbj_r25_ding_001.md` - 丁火
  - `qtbj_r26_wu_001.md` - 戊土
  - `qtbj_r27_ji_001.md` - 己土
  - `qtbj_r28_geng_001.md` - 庚金
  - `qtbj_r29_xin_001.md` - 辛金
  - `qtbj_r30_ren_001.md` - 壬水
  - `qtbj_r30_gui_001.md` - 癸水
- Evidence: `典籍/calibrated/cards/qtbj/`
