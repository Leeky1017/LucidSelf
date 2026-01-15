"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997687
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
    semantic_id="dts_v1.0.0_德胜才者_局全君子之风_才胜德者_用显多能之象_001",
    book_id="dts",
    engine_id="bazi"
)
class 德胜才者局全君子之风才胜德者用显多能之象(SemanticEntry):
    """
    - **原文（source_text）**：
  德胜才者，局全君子之风，才胜德者，用显多能之象。

- 原注（原文注解）：
  　　清顺中和，主辅得宜……此君子之风也。财官不向日主，而日主贪合强求…...
    """
    
    original_text: str = """- **原文（source_text）**：
  德胜才者，局全君子之风，才胜德者，用显多能之象。

- 原注（原文注解）：
  　　清顺中和，主辅得宜……此君子之风也。财官不向日主，而日主贪合强求……此多能之象。阳内阴外，多为德胜；阳外阴内，多为才胜（举例略）。

- **规范化释义（primary_lang_explained）**：
  才德之衡，以清顺中和为本；德胜贵恒，才胜多变，皆需“主辅得宜”。

- 分字分词释义：
  - 德胜：秩序中和为德，胜于才技。
  - 才胜：功能技艺显于表。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 才德 | Talent-Virtue (Cai-De) | 才干与德行 | Ability and morality | caide | existing |
| 德胜才 | Virtue Exceeds Talent | 君子之风 | Gentleman style | deshengcai | new_candidate |
| 才胜德 | Talent Exceeds Virtue | 多能之象 | Versatile image | caishengde | new_candidate |
| 君子 | Gentleman (Jun-Zi) | 有德之人 | Virtuous person | junzi | new_candidate |
| 多能 | Versatile/Many Skills | 多才多艺 | Multi-talented | duoneng | new_candidate |
| 阳内阴外 | Yang Inside Yin Outside | 内刚外柔 | Inner strength, outer softness | yangnei_yinwai | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Cai-De (Talent-Virtue) theory: "Virtue Exceeds Talent" (De-Sheng-Cai) shows the style of a Gentleman (Jun-Zi). "Talent Exceeds Virtue" (Cai-Sheng-De) shows versatility (Duo-Neng). Yang Inside Yin Outside is Virtue; Yang Outside Yin Inside is Talent. Balance is key."""
    normalized_text_zh: str = """"""
    subject: str = "德胜才者，局全君子之风，才胜德者，用显多能之象。"
    factor_refs: list = []
    
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
        l1_anchor="dts_v1.0.0_德胜才者_局全君子之风_才胜德者_用显多能之象_001_L1",
    )
    version: str = "1.0.0"
