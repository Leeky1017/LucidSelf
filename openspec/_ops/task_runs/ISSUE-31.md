# ISSUE-31
- Issue: #31
- Branch: task/31-fix-mlxj-r11-r20
- PR: <fill-after-created>

## Plan
- 重新生成 10 张《梦林玄解》Deep calibration cards，严格按 CALIBRATION_TEMPLATE_CN_V3.md 规范
- 修复问题：L4 跨体系桥接层、L5 验证与校准层、L3.3 因子提取
- 提交并创建 PR，启用 auto-merge

## Runs
### 2026-01-28 worktree setup
- Command: `scripts/agent_worktree_setup.sh 31 fix-mlxj-r11-r20`
- Key output: `OK: .worktrees/issue-31-fix-mlxj-r11-r20 (task/31-fix-mlxj-r11-r20)`

### 2026-01-28 卡片重新生成
- 严格按 CALIBRATION_TEMPLATE_CN_V3.md Deep 级别重新生成 10 张卡片
- 修复问题：
  - L4：正确实现「跨体系桥接层」（功能等价分析/文化转译/中立标签）
  - L5：正确实现「验证与校准层」（历史案例/现代测试/文献核验）
  - L3.3：补充「因子提取（语义级）」
  - L1.1：完整原文引用与上下文分析
- 生成文件：
  - mlxj_r11_tianxiang_1_001.md（天象部一：天类日月星斗）
  - mlxj_r12_tianxiang_2_001.md（天象部二：风云雷雨霜雪）
  - mlxj_r13_dili_001.md（地理部一：地土山水桥路坟墓）
  - mlxj_r14_renwu_1_001.md（人物部一：帝王圣贤将相）
  - mlxj_r15_renwu_2_001.md（人物部二：神鬼仙佛）
  - mlxj_r16_xingmao_001.md（形貌部：身体器官容貌）
  - mlxj_r17_zhengshi_001.md（政事部：官职科举政令）
  - mlxj_r18_dongyu_001.md（动与部：飞禽走兽鱼虫）
  - mlxj_r19_yinshi_001.md（饮食部：饮食宴饮酒肉）
  - mlxj_r20_feizou_001.md（占繇总论：梦占原理方法论）
