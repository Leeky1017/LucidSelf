# ISSUE-22
- Issue: #22
- Branch: task/22-cal-mlxj-r11-r20
- PR: <fill-after-created>

## Plan
- 生成《梦林玄解》R11–R20 共 10 张 Deep calibration cards（含 `source_range` 行号引用）
- 更新本 RUN_LOG，并跑最小校验/预检；提交并创建 PR（`Closes #22`，启用 auto-merge）

## Runs
### 2026-01-28 09:59:32 CST setup worktree
- Command: `scripts/agent_controlplane_sync.sh`
- Key output: `OK: control-plane main synced (/home/leeky/work/LucidSelf/.worktrees/control-main) HEAD=1f9d9fe`
- Evidence: see terminal output in this session

- Command: `scripts/agent_worktree_setup.sh 22 cal-mlxj-r11-r20 --no-sync`
- Key output: `OK: .worktrees/issue-22-cal-mlxj-r11-r20 (task/22-cal-mlxj-r11-r20)`
- Evidence: see terminal output in this session

### 2026-01-28 生成 10 张 Deep calibration cards
- 源文件：`典籍/中文典籍/梦林玄解/原文/梦林玄解.md`
- 模板：`典籍/CALIBRATION_TEMPLATE_CN_V3.md` (Deep 级别)
- 输出目录：`典籍/calibrated/cards/mlxj/`
- 生成卡片（共 10 张）：
  - `mlxj_r11_tianxiang_1_001.md` (天象部一：天类/日月星斗，L113-136)
  - `mlxj_r12_tianxiang_2_001.md` (天象部二：风云雷雨等，L138-144)
  - `mlxj_r13_dili_001.md` (地理部一：地土/山水/桥路/坟墓，L146-168)
  - `mlxj_r14_renwu_1_001.md` (人物部一：帝王/圣贤/将相，L169-202)
  - `mlxj_r15_renwu_2_001.md` (人物部二：后妃/节孝/仙佛/神鬼，L203-251)
  - `mlxj_r16_xingmao_001.md` (形貌部一：身体/头额/面目/耳鼻，L261-267)
  - `mlxj_r17_zhengshi_001.md` (政事部：科第/官禄/婚姻/丧葬，L297-331)
  - `mlxj_r18_dongyu_001.md` (栋宇部：殿宫/第宅/仓库/囹圄/神宇，L399-412)
  - `mlxj_r19_yinshi_001.md` (饮食部：泉茗/酒浆/五谷/肴馔，L425-459)
  - `mlxj_r20_feizou_001.md` (飞走部：四灵/百兽/六畜/羽族/昆虫，L460-532)
- Evidence: `glob 典籍/calibrated/cards/mlxj/*.md` 返回 10 个文件

