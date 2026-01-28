# ISSUE-36
- Issue: #36
- Branch: task/36-astro-houses-cal
- PR: https://github.com/Leeky1017/LucidSelf/pull/41

## Plan
- 精校 The Astrological Houses R21-R30（10轮，约15张卡片）
- 按英文模板 (CALIBRATION_TEMPLATE_EN_V3.md) 产出 Deep 级别卡片
- 输出到 `典籍/calibrated/cards/astro_houses/`

## Runs
### 2026-01-28 初始化
- Command: `scripts/agent_worktree_setup.sh 36 astro-houses-cal`
- Key output: `OK: .worktrees/issue-36-astro-houses-cal (task/36-astro-houses-cal)`
- Evidence: worktree 创建成功

### 2026-01-28 精校卡片产出
- Command: 读取源文件 `典籍/texts/The Astrological Houses/原文/The Astrological Houses.MD`，按模板产出 15 张 Deep 级别卡片
- Key output: 
  - R21: `astro_houses_r21_why_houses_001.md` (WHY HOUSES? 章节)
  - R22: `astro_houses_r22_house01_001.md`, `astro_houses_r22_house02_001.md` (第一、二宫)
  - R23: `astro_houses_r23_house03_001.md`, `astro_houses_r23_house04_001.md` (第三、四宫)
  - R24: `astro_houses_r24_house05_001.md`, `astro_houses_r24_house06_001.md` (第五、六宫)
  - R25: `astro_houses_r25_house07_001.md`, `astro_houses_r25_house08_001.md` (第七、八宫)
  - R26: `astro_houses_r26_house09_001.md`, `astro_houses_r26_house10_001.md` (第九、十宫)
  - R27: `astro_houses_r27_house11_001.md`, `astro_houses_r27_house12_001.md` (第十一、十二宫)
  - R28: `astro_houses_r28_cusp_sign_method_001.md` (cusp signs 方法)
  - R29: `astro_houses_r29_house_structure_001.md` (angular/succeedent/cadent 结构)
  - R30: `astro_houses_r30_synthesis_001.md` (综合解读)
- Evidence: `典籍/calibrated/cards/astro_houses/` 目录下 15 个 .md 文件
