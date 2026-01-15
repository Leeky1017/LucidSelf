"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997205
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
    semantic_id="dts_v1.0.0_支神祇以冲为重_刑与害兮动不动_001",
    book_id="dts",
    engine_id="bazi"
)
class 支神祇以冲为重刑与害兮动不动(SemanticEntry):
    """
    - **原文（source_text）**：
  支神祇以冲为重，刑与害兮动不动.

- 原注（原文注解）：
  　　冲者必是相克，所以必动，至于刑害之间，又有相生相合者存，所以有动不动之异.

- ...
    """
    
    original_text: str = """- **原文（source_text）**：
  支神祇以冲为重，刑与害兮动不动.

- 原注（原文注解）：
  　　冲者必是相克，所以必动，至于刑害之间，又有相生相合者存，所以有动不动之异.

- 分字分词释义：
  - 支神：地支所含诸神（藏干、人元）.
  - 冲为重：以冲的影响力为优先考量.
  - 刑与害：刑为制约伤害，害为损伤不合.

- **规范化释义（primary_lang_explained）**：
  冲多伴随相克，往往直接引动变局；刑与害则多有缓冲空间，其中若夹杂生合或会局，其动象未必立刻爆发，需要结合整体结构细查。

- **次语种完整诠释（secondary_lang_full）**:  
  Clashes usually involve direct overcoming, so they are the first indicator that something will move or change in a chart. Punishments and harms are more ambiguous: they can injure, restrain or irritate, but often contain generating or combining relationships that soften or even redirect their impact. In practice, you look at clashes first to decide whether a pattern is truly set in motion, and only then examine punishments and harms to see how much of that movement is intensified, delayed or absorbed by the surrounding structure.

- **核心要点**：
  - 判动象优先看冲，其力最直接最明显。

- **详细解说**：
  支神之间的冲，多带有明显的克制与对撞，最容易在现实层面引发职位变动、关系破裂、环境突变等"大动"。刑与害虽然也属不良关系，但其内部常混杂生合、会局等结构，使得结果更为暧昧：有时化成内在压力与长期消耗，有时被生合通关而减弱外显冲击。因此，真正判断"动不动"时，不应把冲刑害混为一谈，而是先以冲为首要判动指标，再看刑害在具体局中是否被生合缓冲、被其它结构吸收，最后才给出对整体动象强弱的评价。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_064]` `[trigger: 两支形成明确相冲]` `[factor_trigger: dizhi_clash_relationship EXISTS AND clash_intensity==强直接]` `[role: 主干]` 支神逢冲多主显动，往往伴随职位、关系或格局的明显变更。 → 《滴天髓·地支论》#支神冲刑害
  - `[ns_dts_065]` `[trigger: 刑害关系中夹杂生合]` `[factor_trigger: dizhi_punishment_harm_relationship EXISTS AND xinghai_buffer==有生合缓冲]` `[role: 条件分支]` 刑与害之力不如冲重，若内含生合与会局，常被缓冲为内在压力。 → 《滴天髓·地支论》#支神冲刑害
  - `[ns_dts_066]` `[trigger: 命局兼见冲刑害]` `[factor_trigger: dizhi_clash_relationship EXISTS AND dizhi_punishment_harm_relationship EXISTS AND motion_priority==冲最高]` `[role: 主干依赖]` 冲刑并见之局，断动象须先看冲，再评刑害是否被生合化解。 → 《滴天髓·地支论》#支神冲刑害
  - `[ns_dts_139]` `[trigger: 刑害独见无冲]` `[factor_trigger: dizhi_punishment_harm_relationship EXISTS AND dizhi_clash_relationship NOT EXISTS]` `[role: 条件分支]` 刑害独见而无冲时，动象多成暗伤内耗，而非明显变局。 → 《滴天髓·地支论》#支神冲刑害
  - `[ns_dts_140]` `[trigger: 冲刑害优先序]` `[factor_trigger: motion_priority==冲最高>刑>害]` `[role: 总结]` 断动象按冲→刑→害之序判定，冲为首重，刑害次之。 → 《滴天髓·地支论》#支神冲刑害

- **校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "支神祇以冲为重，刑与害兮动不动."
    factor_refs: list = ['dizhi_chong', 'dizhi_xing', 'dizhi_hai', 'dongbudong', 'shenghe_huanchong', 'dongxiang']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_支神祇以冲为重_刑与害兮动不动_001_L1",
    )
    version: str = "1.0.0"
