"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237971
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
    semantic_id="ap_v1.0.0_entry_1__signatures_and_signif_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1SignaturesAndSignif(SemanticEntry):
    """
    **Source Text** (Lines 5797-5864):
> "To make significant" is to visualize each and all situations o...
    """
    
    original_text: str = """**Source Text** (Lines 5797-5864):
> "To make significant" is to visualize each and all situations or entities which one meets as signs of the workings of Spirit. In each of the smallest details of the world-pattern one may see at work the Wholeness of the whole... The whole is active everywhere.
>
> The alchemist was supposed to be an expert graphologist deciphering at once the Signature; from the Sign going straight to the life; from symbol, to reality...
>
> An astrological birth-chart is a true Signature—and must be read as such. One must find in it the individual and the collective names—plus the sign of the creative.

**Key Term Analysis**:
- **Signature**: `sign of indwelling spirit` / `form revealing inner reality` / `medieval alchemical concept`
- **Significant facts**: `facts seen as signs of life` / `not superficial but life-revealing`
- **Birth-chart as Signature**: `individual name + collective name + creative sign` / `to be deciphered`
- **Clair-seeing (holistic perception)**: `conscious intuition` / `power to see universal patterns in particular`

**English Paraphrase (Primary Language)**:
Rudhyar introduces the concept of "Signature"—the alchemical/medieval idea that form reveals inner spirit. "To make significant" means seeing every situation as a sign of Spirit's workings. The birth-chart IS a true Signature containing individual name, collective name, and creative sign—to be deciphered like a graphologist reads handwriting.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar引入"签名"概念——中世纪炼金术思想，形式揭示内在精神。"使之有意义"意味着将每种情境视为精神运作的符号。出生图是真正的签名，包含个体名、集体名和创造性符号——需要像笔迹学家解读笔迹那样解读。

**Narrative Snippets**:
- `[ns_aop_133]` `[trigger: signature]` `[factor_trigger: astro_signature AND astro_signature_concept]` `[role: 主干]` Signature: form as revelation of indwelling spirit, from symbol to reality. → L5834-5839
- `[ns_aop_134]` `[trigger: birth_chart_signature]` `[factor_trigger: astro_chart_as_signature AND astro_signature_concept]` `[role: 总结]` Birth-chart as Signature: individual name + collective name + creative sign. → L5862-5864"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Signatures and Significant Facts"
    factor_refs: list = ['astro_signature', 'astro_clairseeing']
    
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
        l1_anchor="ap_v1.0.0_entry_1__signatures_and_signif_001_L1",
    )
    version: str = "1.0.0"
