# ISSUE-23
- Issue: #23
- Branch: task/23-smth-r11-r20
- PR: <fill-after-created>

## Plan
- 产出《三命通会》R11-R20（10 张 Deep 精校卡），落盘到 `典籍/calibrated/cards/smth/`（文件名按批次清单）。
- 新增/更新 rulebook task `rulebook/tasks/issue-23-smth-r11-r20/`，并在本文件记录关键执行证据。
- 通过 PR 交付并启用 auto-merge，required checks 全绿后确认实际合并。

## Runs
### 2026-01-28 init
- Command: `gh auth status && git remote -v`
- Key output: GitHub CLI authenticated
- Evidence: issue `#23`

### 2026-01-28 cards-generation
- Command: 生成 10 张 Deep 精校卡
- Key output:
  ```
  smth_r11_wuxing_zonglun_001.md   (9385 bytes)
  smth_r12_ganzhi_zonglun_001.md   (9823 bytes)
  smth_r13_nayin_zonglun_001.md    (10757 bytes)
  smth_r14_liushijiazi_001.md      (11110 bytes)
  smth_r15_tiangan_shengsi_001.md  (9533 bytes)
  smth_r16_sishi_jieqi_001.md      (8452 bytes)
  smth_r17_wangxiang_xiuxiu_001.md (9850 bytes)
  smth_r18_suiyun_shijian_001.md   (9498 bytes)
  smth_r19_luma_tianyi_001.md      (8784 bytes)
  smth_r20_shensha_zonglun_001.md  (9519 bytes)
  ```
- Evidence: `ls -la 典籍/calibrated/cards/smth/` 显示 10 个文件

### 2026-01-28 validation
- Command: `openspec validate --specs --strict --no-interactive`
- Key output: `Totals: 27 passed, 0 failed (27 items)`
- Evidence: openspec 验证全绿
