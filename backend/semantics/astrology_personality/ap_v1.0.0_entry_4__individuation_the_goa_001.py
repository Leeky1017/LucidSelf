"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237896
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
    semantic_id="ap_v1.0.0_entry_4__individuation_the_goa_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4IndividuationTheGoa(SemanticEntry):
    """
    **Source Text** (Lines 3815-3875):
> Individuation... This consummation (which, in a sense, is never...
    """
    
    original_text: str = """**Source Text** (Lines 3815-3875):
> Individuation... This consummation (which, in a sense, is never final, for the existence of spheres within spheres of collective unconscious can be conceived or postulated) is individuation: the "making whole," or "making perfect" of older systems of spiritual development—yet with a difference due to the new mental level reached by mankind.
>
> Jung: "Individuation means to become a single, discrete being, and, inasmuch as the concept individuality embraces that innermost, last and incomparable uniqueness of our being, it also includes the idea of becoming one's own real self. Hence individuation could also be translated as 'coming to selfhood' or 'self-realization.' ... Individualism is a purposeful attempt to stress and make conspicuous some ostensible peculiarity, in opposition to collective considerations and obligations. But individuation means precisely a better and more complete fulfillment of the collective dispositions of mankind..."

**Key Term Analysis**:
- **Individuation**: `making whole` / `becoming real self` / `self-realization` / `coming to selfhood`
- **vs Individualism**: `not opposing collective` / `better fulfillment of collective` / `not strangeness`
- **Process**: `conscious assimilates unconscious` / `ego becomes Self` / `never final`

**English Paraphrase (Primary Language)**:
Individuation = "making whole"—the ego grows beyond itself to become "the fully integrated Self—the center of the totality of man's fully developed being." Not to be confused with individualism (opposing collective); individuation means "a better and more complete fulfillment of the collective dispositions of mankind."

Jung: individuation = "becoming one's own real self," "coming to selfhood," "self-realization." It fulfills the individual's particular nature, which is "vastly different from egoism or individualism." The individual is "made up of universal factors," so "wholly collective" yet uniquely combined.

**Complete Chinese Interpretation (Secondary Language)**:
个体化="使完整"——自我超越自身成为"完全整合的自性——人完全发展的存在之整体的中心"。不要与个人主义（对抗集体）混淆；个体化意味着"对人类集体倾向更好、更完整的实现"。

Jung：个体化="成为真正的自我"、"达到自性"、"自我实现"。它实现个体的特殊本性，这"与自我主义或个人主义截然不同"。个体"由普遍因素构成"，因此"完全集体性"但独特组合。

**Narrative Snippets**:
- `[ns_aop_117]` `[trigger: individuation_def]` `[factor_trigger: astro_individ AND astro_indiv_process]` `[role: 主干]` Individuation: making whole, becoming real self, ego→Self, never final. → L3839-3841
- `[ns_aop_118]` `[trigger: vs_individualism]` `[factor_trigger: astro_vs_indivism]` `[role: 总结]` Individuation ≠ individualism; better fulfillment of collective, uniqueness from universal factors. → L3851-3873"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: Individuation—The Goal"
    factor_refs: list = ['astro_individuation', 'astro_self_center']
    
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
        l1_anchor="ap_v1.0.0_entry_4__individuation_the_goa_001_L1",
    )
    version: str = "1.0.0"
