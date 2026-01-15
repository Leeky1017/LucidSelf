"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997279
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
    semantic_id="dts_v1.0.0_上下贵乎情协_001",
    book_id="dts",
    engine_id="bazi"
)
class 上下贵乎情协(SemanticEntry):
    """
    - **原文（source_text）**：
  上下贵乎情协.

- 原注（原文注解）：
  　　天干地支，虽非相生，郤有情而不悖.

- 分字分词释义：
  - 上下：天干与地支.
  - 情协：...
    """
    
    original_text: str = """- **原文（source_text）**：
  上下贵乎情协.

- 原注（原文注解）：
  　　天干地支，虽非相生，郤有情而不悖.

- 分字分词释义：
  - 上下：天干与地支.
  - 情协：上下情义协调.

- **规范化释义（primary_lang_explained）**：
  干支上下，纵非相生，但若情协（有情），亦不相悖.

- **次语种完整诠释（secondary_lang_full）**:
  Even when the heavenly stems above and the earthly branches below do not form a textbook generating relationship, the chart can still be harmonious if they move in the same spirit and do not attack one another. What matters here is "affectionate coordination": intent, direction and momentum that fit together rather than collide. In such cases, lack of mutual birth does not equal hostility; the stems and branches may simply coexist, support the same purposes and avoid mutual harm. This principle asks us to look beyond a mechanical sheng–ke calculus and include relational harmony as a higher criterion: are the upper and lower parts of the chart working with each other in feeling and tendency, or are they secretly at odds?

- **核心要点**：
  - 评断干支关系，不可只看五行生克，更要看上下是否情协、不相悖；
  - 虽非相生，但若方向一致、气势相和而无冲刑克害，亦可为美局；
  - “情协”是高于单一生克打分的判据，应作为格局优劣的重要判断维度。

- **详细解说**：
  此条提出“上下贵乎情协”，是要命理师跳出只看生克的机械框架.干支之间固然有五行生克，但现实人生中，很多关系既非典型“相生”，也不至于构成明显“相克”，更多是一种方向相近、互不妨碍的并行.若只按五行生克判吉凶，容易把这类“有情不悖”的组合误判为平庸甚至不利.

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_094]` `[trigger: 干支之间无明显生克亦无冲害刑破]` `[factor_trigger: sheng_ke_relationship_type=中性/平 & qingxie_indicator=有情]` `[role: 主干]` 上下虽无明显相生，但若彼此不相冲克、不互拆台，多主关系平和稳定，可视为"情协". → 《滴天髓·地支论》#上下贵乎情协
  - `[ns_dts_095]` `[trigger: 命局生克一般但上下象意方向一致]` `[factor_trigger: qingxie_indicator=有情 & beyond_shengke_harmony=on]` `[role: 主干依赖]` 干支生克平平，却在象意与方向上同向而行，常见团队或家庭中"志同道合、各守本分"的格局. → 《滴天髓·地支论》#上下贵乎情协
  - `[ns_dts_096]` `[trigger: 五行上不相生却明显存在冲害刑破]` `[factor_trigger: qingxie_conflict_detector=有 & qingxie_indicator=相悖]` `[role: 条件分支]` 若干支既不相生、又多冲害刑破，则属"情义相悖"，不可勉强以"情协"美化之. → 《滴天髓·地支论》#上下贵乎情协
  - `[ns_dts_159]` `[trigger: 情悖而强合]` `[factor_trigger: qingxie_conflict_detector=有 & qingxie_indicator=相悖]` `[role: 例外处理]` 上下情悖而强行合作，终生暗耗，不如坦然分道. → 《滴天髓·地支论》#上下贵乎情协
  - `[ns_dts_160]` `[trigger: 情协总则]` `[factor_trigger: qingxie_indicator]` `[role: 总结]` 上下贵乎情协，情协则和顺，情悖则暗耗，判局须先辨情. → 《滴天髓·地支论》#上下贵乎情协

 - **校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "上下贵乎情协."
    factor_refs: list = ['shangxia', 'qingxie', 'guihu', 'tiandi_peihe', 'xiangsheng_xianghe', 'qingyi']
    
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
        l1_anchor="dts_v1.0.0_上下贵乎情协_001_L1",
    )
    version: str = "1.0.0"
