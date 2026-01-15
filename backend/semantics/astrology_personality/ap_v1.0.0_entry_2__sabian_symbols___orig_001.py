"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238264
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
    semantic_id="ap_v1.0.0_entry_2__sabian_symbols___orig_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2SabianSymbolsOrig(SemanticEntry):
    """
    **Source Text** (Lines 10581-10797):
> From the foregoing it may have become clear that the reality ...
    """
    
    original_text: str = """**Source Text** (Lines 10581-10797):
> From the foregoing it may have become clear that the reality of the Degree, being of such a transcendental nature, can be considered and studied only in terms of a particular symbolical representation attached to it...
>
> In this "Sabian" cycle of symbols we have something similar to the cycle of the Yi King as interpreted by the King Wen some 3000 years ago... The same thing is true today. Therefore the "Sabian" symbols, recorded by Marc Jones, present to us moderns pictures and scenes which are relatively familiar...
>
> The key-number in such a cycle is not 12, but 6. The cycle is one of awareness... Its first division is one which corresponds to the concept of horizon... The concept of meridian, on the other hand, refers to the element of "power."

**Key Term Analysis**:
- **Sabian symbols**: `Marc Jones recording` / `Egyptian sources` / `360 images`
- **Yi King parallel**: `King Wen` / `modern garb` / `familiar scenes`
- **6 as key number**: `awareness cycle` / `6 Rays` / `horizon = consciousness`
- **24 hours/Elders**: `15 degrees per hour` / `span divisions` / `habit/emotional/mental`

**English Paraphrase (Primary Language)**:
Sabian symbols = "something similar to Yi King," recorded by Marc Jones from "ancient Egyptian sources." 360 symbols in modern garb for contemporary understanding.

Key number = 6 (not 12): "cycle of awareness." Six Rays, each crucified into 4 = 24 Elders = 24 hours. Each "hour" = 15 degrees = one span. Each span has three 5-degree sections: habit, emotional, mental realms.

"Symbolical astrology is a living art... symbols are seldom to be taken literally. They are catalytics to higher understanding."

**Complete Chinese Interpretation (Secondary Language)**:
萨比恩符号 = "类似易经的东西"，由Marc Jones从"古埃及来源"记录。360个符号以现代形式呈现，便于当代理解。

关键数字 = 6（不是12）："意识周期"。六射线，每个被钉十字架为4 = 24长老 = 24小时。每"小时" = 15度 = 一个跨度。每个跨度有三个5度部分：习惯、情感、心智领域。

"象征占星学是一门活的艺术……符号很少应被字面理解。它们是激发更高理解的催化剂。"

**Narrative Snippets**:
- `[ns_aop_197]` `[trigger: sabian_origin]` `[factor_trigger: astro_sabian_source]` `[role: 主干]` Sabian symbols: Marc Jones recording from Egyptian sources; 360 images like Yi King. → L10601-10636
- `[ns_aop_198]` `[trigger: span_structure]` `[factor_trigger: astro_span_division AND astro_span]` `[role: 主干依赖]` Cycle key = 6 (not 12); 24 Elders = 24 hours; each span = 15° (habit/emotional/mental). → L10661-10703"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Sabian Symbols - Origin and Method"
    factor_refs: list = ['sabian_symbols', 'span_section', 'elders_24']
    
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
        l1_anchor="ap_v1.0.0_entry_2__sabian_symbols___orig_001_L1",
    )
    version: str = "1.0.0"
