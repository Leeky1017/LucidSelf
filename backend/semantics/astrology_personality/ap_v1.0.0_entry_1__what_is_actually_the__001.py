"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238121
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
    semantic_id="ap_v1.0.0_entry_1__what_is_actually_the__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1WhatIsActuallyThe(SemanticEntry):
    """
    **Source Text** (Lines 7863-7970):
> We could easily proceed with our study of the significance attr...
    """
    
    original_text: str = """**Source Text** (Lines 7863-7970):
> We could easily proceed with our study of the significance attributed to the signs of the zodiac... but to do so would be taking things for granted and shrinking, in fact, from facing serious problems concerning the zodiac...
>
> This fact of the public discovery of the Earth's rotation around the polar axis and of its revolution around the Sun upset completely the basis of astrological symbolism... the sphericity of the Earth and the fact of its rotation introduced an utterly new sense of space, which necessitated a revaluation of the zodiac...
>
> From our standpoint we find in the twelve-fold pattern of the dial of houses a basic formula of individual unfoldment... The zodiac remains, of course, the pattern of collective development and universal life-functioning.

**Key Term Analysis**:
- **Zodiac revaluation**: `Ptolemaic unity broken` / `dualism of motion` / `axial vs orbital`
- **Houses vs Zodiac**: `houses = individual unfoldment` / `zodiac = collective development`
- **Earth rotation significance**: `enables individuation` / `dial of houses becomes basic`

**English Paraphrase (Primary Language)**:
The discovery of Earth's rotation and revolution "upset completely the basis of astrological symbolism." The Ptolemaic zodiac's unity was broken—now there's a dualism: axial rotation (individual) vs orbital revolution (collective).

Rudhyar proposes: **Houses** = basic formula of individual unfoldment; **Zodiac** = pattern of collective development. "The dial of houses can be considered now as the basic factor, instead of the solar zodiac."

**Complete Chinese Interpretation (Secondary Language)**:
地球自转和公转的发现"彻底颠覆了占星符号学的基础。"托勒密黄道的统一性被打破——现在存在二元性：轴向旋转（个体）vs轨道公转（集体）。

Rudhyar提出：**宫位** = 个体展开的基本公式；**黄道** = 集体发展的模式。"宫位表盘现在可以被视为基本因素，而非太阳黄道。"

**Narrative Snippets**:
- `[ns_aop_165]` `[trigger: zodiac_revaluation]` `[factor_trigger: astro_zodiac_modern AND astro_zodiac_houses]` `[role: 主干]` Earth's rotation discovery necessitated zodiac revaluation: houses (individual) vs zodiac (collective). → L7917-7946
- `[ns_aop_166]` `[trigger: houses_basic]` `[factor_trigger: astro_houses_primary AND astro_zodiac_houses]` `[role: 总结]` Houses now basic formula of individual unfoldment; zodiac remains collective pattern. → L7966-7970"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: What Is Actually the Zodiac?"
    factor_refs: list = ['zodiac_reeval', 'houses_basic']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_1__what_is_actually_the__001_L1",
    )
    version: str = "1.0.0"
