# ISSUE-20
- Issue: #20
- Branch: task/20-tetr-r11-r20
- PR: #26 (https://github.com/Leeky1017/LucidSelf/pull/26)

## Plan
- 执行对话框 C（Tetrabiblos）R11-R20 共 10 轮 Deep 深度校准
- 每轮产出 1 张校准卡，输出到 `典籍/calibrated/cards/tetr/`
- 按 `典籍/CALIBRATION_TEMPLATE_EN_V3.md` 的 Deep 口径完成（卡内 `source_range` 可追溯到 `Tetrabiblos.md` 行号范围）

## Runs
### 2026-01-28 Setup & Calibration

- **Environment setup**:
  - Branch: `task/20-tetr-r11-r20`
  - Worktree: `.worktrees/control-main/.worktrees/issue-20-tetr-r11-r20/`
  - Output directory: `典籍/calibrated/cards/tetr/`

- **Source analysis**:
  - Book I (lines 963-2983): Chapters IV-V (planets), XIV-XVI (signs), XX-XXIV (dignities)
  - Book II (lines 2983-4625): Chapters I-III (geography/climate)
  - Book III (lines 4625-7026): Chapters III-IV (angles, method)
  - Book IV (lines 7026+): Chapters II-V (wealth, rank, marriage)

- **Calibration cards generated** (10 Deep cards):
  | Round | Card ID | Semantic Unit | Source Range |
  |:---|:---|:---|:---|
  | R11 | `tetr_r11_book1_scope_001` | Astrology as second part of prognostication | :971~:1006 |
  | R12 | `tetr_r12_planets_001` | Planetary qualities and benefic/malefic | :1585~:1662 |
  | R13 | `tetr_r13_signs_001` | Sign modalities and aspects | :2097~:2227 |
  | R14 | `tetr_r14_aspects_dignities_001` | Essential dignities system | :2368~:2805 |
  | R15 | `tetr_r15_geography_001` | Mundane astrology geographic framework | :2986~:3176 |
  | R16 | `tetr_r16_nativities_method_001` | Nativity method workflow | :4867~:4965 |
  | R17 | `tetr_r17_angles_001` | Angles and Ascendant importance | :4779~:4863 |
  | R18 | `tetr_r18_wealth_001` | Wealth from Lot of Fortune | :7049~:7102 |
  | R19 | `tetr_r19_rank_001` | Rank from luminaries | :7105~:7176 |
  | R20 | `tetr_r20_domains_001` | Marriage from Venus/Mars | :7400~:7530 |

- **Evidence**: All cards contain traceable `source_range` to `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md` line numbers

