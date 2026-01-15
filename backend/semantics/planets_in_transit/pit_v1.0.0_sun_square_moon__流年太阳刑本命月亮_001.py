"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224172
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
    semantic_id="pit_v1.0.0_sun_square_moon__流年太阳刑本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquareMoon流年太阳刑本命月亮(SemanticEntry):
    """
    **Source Text** (Lines 2196-2234):
> This can be a rather tense time. If you have been bottling up p...
    """
    
    original_text: str = """**Source Text** (Lines 2196-2234):
> This can be a rather tense time. If you have been bottling up pressures, they will become very difficult to bear now. Your conscious actions may be impulsive and ill-thought-out, as your emotions come into conflict with your conscious will.
> 
> You may feel split into two personalities working at cross-purposes. The Sun rules your conscious personality; the Moon rules your unconscious compulsions and habits. The square is expressed as irritability, proneness to upset, or excessive emotionalism. However, if you are in good emotional shape, this can be an energizing transit.

**English Paraphrase**: Rather tense time; bottled pressures become unbearable. Impulsive, ill-thought actions as emotions conflict with conscious will. Feel split into two cross-purpose personalities. Sun=conscious; Moon=unconscious compulsions/habits. Square=irritability, upset, excessive emotionalism. But if emotionally healthy, can be energizing.

**Complete Chinese Interpretation**: 相当紧张的时期；压抑的压力变得难以承受。情感与有意识意志冲突时行动冲动、考虑不周。感觉分裂成两个目的相悖的人格。太阳=有意识；月亮=无意识强迫/习惯。刑相=易怒、不安、过度情绪化。但如果情感健康，可以是激励性的。

**Narrative Snippets**:
- `[ns_pit_059]` `[trigger: transit_sun_square_natal_moon]` `[factor_trigger: astro_transit_sun SQUARE natal_moon]` `[role: 主干]` Tense time—bottled pressures become difficult; emotions conflict with conscious will. → PIT Ch4 Sun□Moon
- `[ns_pit_060]` `[trigger: transit_sun_square_natal_moon]` `[factor_trigger: astro_transit_sun SQUARE natal_moon]` `[role: 条件分支]` May feel split into two cross-purpose personalities. Can be irritability and emotionalism—or energizing if emotionally healthy. → PIT Ch4 Sun□Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Moon (流年太阳刑本命月亮)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_sun_square_moon__流年太阳刑本命月亮_001_L1",
    )
    version: str = "1.0.0"
