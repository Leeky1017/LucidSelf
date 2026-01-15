"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237842
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
    semantic_id="ap_v1.0.0_entry_12__symbols_representati_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry12SymbolsRepresentati(SemanticEntry):
    """
    **Source Text** (Lines 2755-2902):
> What are symbols? They are representations of qualities which p...
    """
    
    original_text: str = """**Source Text** (Lines 2755-2902):
> What are symbols? They are representations of qualities which pertain to wholes. In contradistinction to symbols, enumerations and categories pertain to parts...
>
> Time-values, soul-values, whole-values—all similar terms—cannot be communicated directly. Intellectual analysis and its related mental operations are of no use whatsoever to convey the wholeness of a whole...
>
> Intuition is thus the power to read every whole as a symbol of a basic quality of life. This actually means to see the soul in every thing, the wholeness (quality) in every whole...
>
> Cosmically speaking, every moment of the universe can thus be realized as a cosmic symbol revealing the quality of the moment, and the soul of the Cosmos... The wholeness of the celestial pattern at birth and the wholeness of the selfhood and destiny of the native are identical; and both are expressions of the wholeness of the moment.

**Key Term Analysis**:
- **Symbols**: `representations of whole-qualities` / `vs enumerations/categories` / `communicate soul`
- **Intuition = symbol-reading**: `see soul in everything` / `wholeness in every whole` / `basic life-quality`
- **Moment as cosmic symbol**: `quality of moment` / `soul of Cosmos` / `birthing wholes`
- **Birth-chart identity**: `celestial pattern wholeness = native's wholeness` / `both = moment's wholeness`

**English Paraphrase (Primary Language)**:
Symbols are "representations of qualities which pertain to wholes"—opposed to enumerations/categories (which pertain to parts). Time-values, soul-values cannot be communicated by intellectual analysis; only symbols convey wholeness.

Intuition = "power to read every whole as a symbol of a basic quality of life"—seeing soul in everything. Cosmically, every moment is a "cosmic symbol revealing the quality of the moment, and the soul of the Cosmos."

The crucial identity: "The wholeness of the celestial pattern at birth and the wholeness of the selfhood and destiny of the native are identical; and both are expressions of the wholeness of the moment." This is holistic logic's genetic (not merely mathematical) equality.

**Complete Chinese Interpretation (Secondary Language)**:
符号是"属于整体的品质的表征"——与列举/分类（属于部分）相对。时间价值、灵魂价值无法通过知性分析传达；只有符号传达整体性。

直觉="将每个整体解读为生命基本品质的符号的能力"——在一切中看到灵魂。宇宙性地，每一刻都是"揭示时刻品质和宇宙灵魂的宇宙符号"。

关键的同一性："出生时天体模式的整体性与命主的自我和命运的整体性是同一的；两者都是时刻整体性的表达。"这是整体论逻辑的发生性（而非仅数学的）等式。

**Narrative Snippets**:
- `[ns_aop_101]` `[trigger: symbols_defined]` `[factor_trigger: astro_symbols_def]` `[role: 主干]` Symbols = representations of whole-qualities; vs enumerations/categories for parts. → L2755-2763
- `[ns_aop_102]` `[trigger: intuition_symbol]` `[factor_trigger: astro_intuit_sym]` `[role: 主干依赖]` Intuition = power to read wholes as symbols of basic life-qualities—see soul in everything. → L2871-2876
- `[ns_aop_103]` `[trigger: moment_cosmic_symbol]` `[factor_trigger: astro_moment_sym]` `[role: 条件分支]` Every moment = cosmic symbol revealing moment's quality and Cosmos's soul. → L2881-2884
- `[ns_aop_104]` `[trigger: birth_identity]` `[factor_trigger: astro_birth_id]` `[role: 总结]` Celestial pattern wholeness = native's wholeness = moment's wholeness—identity through holistic logic. → L2897-2902"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 12: Symbols—Representations of Wholeness Qualities"
    factor_refs: list = ['astro_symbols', 'astro_intuit_symbol', 'astro_birth_identity']
    
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
        l1_anchor="ap_v1.0.0_entry_12__symbols_representati_001_L1",
    )
    version: str = "1.0.0"
