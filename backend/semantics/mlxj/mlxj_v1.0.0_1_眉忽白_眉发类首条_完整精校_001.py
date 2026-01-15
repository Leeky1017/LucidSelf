"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.817479
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
    semantic_id="mlxj_v1.0.0_1_眉忽白_眉发类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1眉忽白眉发类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

眉忽白，大吉。福寿白眉之兆，诸事得白，子孙有喜，病者梦之，寿增一纪。

#### 规范化释义（primary_lang_explained）

梦见眉毛忽然...
    """
    
    original_text: str = """#### 原文（source_text）

眉忽白，大吉。福寿白眉之兆，诸事得白，子孙有喜，病者梦之，寿增一纪。

#### 规范化释义（primary_lang_explained）

梦见眉毛忽然变白，大吉。这是福寿白眉之兆，诸事都能明白通达，子孙有喜事，病人梦此，可增寿一纪（十二年）。

#### 完整对等诠释（secondary_lang_full）

Dreaming of eyebrows suddenly turning white is greatly auspicious. This is an omen of blessed longevity symbolized by white brows. All matters become clear, descendants will have joyous occasions. If a sick person dreams this, their lifespan extends by one cycle (twelve years).

#### 核心要点

- 眉白=福寿之兆（白眉寿征）
- 诸事得白=万事明白通达
- 子孙有喜=后代吉庆
- 病者寿增一纪=延寿十二年

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v8_001]` `[trigger: 梦眉白]` `[factor_trigger: dream_mei_bai AND dream_meibai AND meifa_zhuangtai]` `[role: 主干]` 眉忽白，大吉。福寿白眉之兆，诸事得白，子孙有喜。 → 《梦林玄解·卷八》#眉忽白
- `[ns_mlxj_v8_002]` `[trigger: 形貌梦象]` `[factor_trigger: qinshu AND chiwei]` `[role: 形貌类]` 亲属、尺尾等形貌梦象。 → 《梦林玄解·卷八》#形貌"""
    normalized_text_zh: str = """"""
    subject: str = "1 眉忽白（眉发类首条·完整精校）"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_眉忽白_眉发类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
