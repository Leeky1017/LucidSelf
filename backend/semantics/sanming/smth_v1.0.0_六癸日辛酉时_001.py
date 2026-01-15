"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339699
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="smth_v1.0.0_六癸日辛酉时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日辛酉时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时辛酉，自身失地更何有。支中明暗被辛伤，无助利名终不就。
  癸日辛酉时，明暗枭神。癸见辛为倒食，酉上辛建旺，癸失地，若无倚托救助者，遇贵生涯；有倚托...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时辛酉，自身失地更何有。支中明暗被辛伤，无助利名终不就。
  癸日辛酉时，明暗枭神。癸见辛为倒食，酉上辛建旺，癸失地，若无倚托救助者，遇贵生涯；有倚托则吉。

- 分字分词释义：
  - **明暗枭神**：辛透，酉藏辛，偏印太旺。
  - **自身失地**：癸水在酉为病地（一说生于酉，但金多水浊，母慈灭子）。
  - **遇贵生涯**：指依靠贵人或从事服务性行业。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于辛酉时，辛金偏印透干且得禄，印绶太旺，有"倒食"之嫌（夺食）。癸水在酉病地，身弱受生太过（金多水浊）。若无倚托救助（如火制金，或木泄水），难成名利。若有倚托，吉。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Xin-You Hour":

  - Self loses ground what more to have—Xin Metal Partial Seal reveals; You hides Xin also; excessive Seal (Owl Spirit).
  - Branch inside bright-dark injured by Xin; no help gain-fame eventually not accomplished.
  - Bright-Dark Owl Spirit; Gui sees Xin as Reversed-Food; Xin builds prosperity at You; Gui loses ground; without support-rescue, encounters noble livelihood.
  - Key: Owl too strong seizes Eating God; needs Fire controlling Seal or Wood draining Water for balance.

- 核心要点：
  - **偏印格**：辛酉枭神旺。
  - **母慈灭子**：金多水浊。
  - **倒食**：夺食神。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_gui_xinyou_001]` `[trigger: 明暗枭神]` `[factor_trigger: gui_xinyou AND mingan_xiaoshen]` `[role: 主干]` 癸日辛酉时，明暗枭神，癸见辛为倒食，酉上辛建旺。 → 《三命通会》卷九#六癸日辛酉时
  - `[ns_smth_09_gui_xinyou_002]` `[trigger: 自身失地]` `[factor_trigger: zishen_shidi AND jin_duo_shui_zhuo]` `[role: 主干依赖]` 自身失地更何有，支中明暗被辛伤。 → 《三命通会》卷九#六癸日辛酉时
  - `[ns_smth_09_gui_xinyou_003]` `[trigger: 有倔托吉]` `[factor_trigger: you_yituo_zeji AND huozhijin_muxieshui]` `[role: 条件分支]` 若无倔托救助者，遇贵生涯；有倔托则吉。 → 《三命通会》卷九#六癸日辛酉时
  - `[ns_smth_09_gui_xinyou_004]` `[trigger: 利名不就]` `[factor_trigger: liming_buzhong AND wuzhu_pingchang]` `[role: 总结]` 无助利名终不就，需火制金或木泄水为平衡。 → 《三命通会》卷九#六癸日辛酉时
- 语义提取（L2）：
  - **主题**：六癸日辛酉时的明暗枭神与金多水浊
  - **自然属性**：象征金多水浊母慈灭子；特性偏印过旺身处病地；元素癸水辛酉时偏印倒食
  - **功能象义**：为偏印格提供判断标准；区分有制得吉与无制埋没；强调倚托救助
  - **条件结构**：必要条件六癸日辛酉时；增强条件有财制印或食伤泄秀；失效条件金多无制身弱
  - **多层解释**：字面层金旺水流；象征层过度庇护（印）导致无能（失地）；实践层审查制印；心理层依赖性强缺乏主见

- L2-术语对齐（Term Glossary）：
| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---|---|---|---|
| 明暗枭神 | Bright-Dark Owl-Spirit | 天干透偏印地支藏偏印 | Heavenly stem reveals Partial Seal earthly branch hides Partial Seal | - | new_candidate |
| 自身失地 | Self Lost-Ground | 日主处于死绝病败之地 | Day Master in dead/extinct/sick/defeated place | - | new_candidate |

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 结构类 | 癸水日主 | day_master_gui | existing | 日主 | 癸 | bazi_semantic | 阴水 |
| 状态类 | 明暗枭神 | bazi_state_factor_323 | existing | 凶象格局 | 辛透酉藏 | bazi_semantic | 印太旺 |
| 关系类 | 母慈灭子 | bazi_relation_zi_4 | existing | 过生状态 | 金多水浊 | bazi_semantic | 身弱泄气 |
| 状态类 | 自身失地 | bazi_state_factor_324 | existing | 凶象 | 酉为病地 | bazi_semantic | 难成名利 |
| 时间类 | 酉时 | hour_branch_you | existing | 时支 | 酉 | bazi_semantic | 金旺水生 |
| 条件类 | 有倚托救助 | bazi_condition_factor_130 | existing | 吉象条件 | 火制木泄 | bazi_semantic | 成格关键 |
<!-- FACTOR_END -->

#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|------------|
| rel_smth_09_172 | structure | mingan_xiaoshen | muci_miezi | 明暗枭神配母慈灭子构成印旺过度身弱失地的不利格局 | 无倚托救助 | 结构关系 | 《三命通会·卷九》#六癸日辛酉时 |
| rel_smth_09_173 | outcome | you_yituo_jiuzhu | huoxiong_weiji | 有倚托救助（火制金或木泄水）则化凶为吉 | 有倚托救助 | 结果关系 | 《三命通会·卷九》#六癸日辛酉时 |
| rel_smth_09_174 | risk | wuzhu_liming | nancheng_mingli | 无助则利名终不就难成名利 | 无倚托救助 | 风险关系 | 《三命通会·卷九》#六癸日辛酉时 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|------------|
| evi_smth_09_172 | "自身失地更何有" | muci_miezi | 癸水在酉病地金多水浊→身弱自身失地 | 格局判定 | 高 | ✅ | rule_zishen_shidi1 |
| evi_smth_09_173 | "有倚托则吉" | huoxiong_weiji | 有火制金或木泄水→化凶为吉 | 结果判定 | 高 | ✅ | rule_youtuo_zeji1 |
| evi_smth_09_174 | "无助利名终不就" | nancheng_mingli | 无救助则利名难成 | 风险判定 | 高 | ✅ | rule_wuzhu_liming1 |

**跨体系概念映射层**：

| 映射ID | 本体系概念 | 目标体系 | 目标概念 | 映射类型 | 映射强度 | 备注 |
|-------|----------|---------|---------|---------|---------|------|
| map_smth_09_115 | mingan_xiaoshen | 心理学 | 过度保护导致的依赖与无能 | 类比映射 | 中 | 明暗枭神对应父母过度庇护导致子女缺乏独立能力 |
| map_smth_09_116 | you_yituo_jiuzhu | 社会学 | 外部支持网络扭转不利局面 | 类比映射 | 中 | 有倚托救助对应通过外部资源弥补自身短板 |

<!-- L2_END -->

---

### 59. 六癸日壬戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日辛酉时"
    factor_refs: list = ['source_ref']
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_六癸日辛酉时_001_L1",
    )
    version: str = "1.0.0"
