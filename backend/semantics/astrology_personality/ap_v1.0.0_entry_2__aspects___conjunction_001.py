"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238282
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
    semantic_id="ap_v1.0.0_entry_2__aspects___conjunction_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2AspectsConjunction(SemanticEntry):
    """
    **Source Text** (Lines 12914-12994):
> The conjunction is, essentially, the prototype of all particu...
    """
    
    original_text: str = """**Source Text** (Lines 12914-12994):
> The conjunction is, essentially, the prototype of all particular manifestation... The degree, of itself, is one among 360 harmonized and integrated phases of universal being. But when a planet comes to that degree... the degree's quality suddenly becomes vivified, energized, emphasized...
>
> The aspect of opposition is the opposite of, and the antidote to, the conjunction. Two planets in opposition are located... exactly in opposite directions from the Earth-observer. The latter is therefore subjected to two contrary pulls... if the two opposed planets are considered as two poles of a battery, he may be illumined by the spark flowing from pole to pole.

**Key Term Analysis**:
- **Conjunction**: `prototype of particular` / `accent on degree` / `disequilibrium` / `energy release`
- **Opposition**: `antidote to conjunction` / `contrary pulls` / `battery poles` / `reconciliation or pulled apart`
- **Accent concept**: `planets = accents` / `stress, tension` / `colors = sufferings of light`
- **Polarity**: `nirvana or schizophrenia` / `depends on integration power`

**English Paraphrase (Primary Language)**:
Conjunction = "prototype of particular manifestation." Planet on degree = accent, vivification. "Every planet represents a state of disequilibrium of zodiacal wholeness."

Opposition = "antidote to conjunction." Two contrary pulls—either "pulled apart" or "illumined by the spark flowing from pole to pole."

"All depends on whether the individual has the power to reconcile the opposites." Buddha reached nirvana at full Moon (Sun-Moon opposition).

**Complete Chinese Interpretation (Secondary Language)**:
合相 = "特殊显化的原型"。行星在度数上 = 重音、活化。"每颗行星代表黄道整体性的失衡状态。"

对冲 = "合相的解药"。两个相反的拉力——要么"被撕裂"，要么"被从极到极流动的火花照亮"。

"一切取决于个人是否有能力调和对立面。"佛陀在满月时达到涅槃（日月对冲）。

**Narrative Snippets**:
- `[ns_aop_201]` `[trigger: conjunction_meaning]` `[factor_trigger: astro_aspect_conjunction]` `[role: 主干]` Conjunction = prototype of particular; planet = accent; disequilibrium of wholeness. → L12916-12965
- `[ns_aop_202]` `[trigger: opposition_meaning]` `[factor_trigger: astro_aspect_opposition AND astro_opposition]` `[role: 主干]` Opposition = antidote; contrary pulls or battery poles; reconciliation or pulled apart. → L12967-12994"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Aspects - Conjunction and Opposition"
    factor_refs: list = ['aspect_conj', 'aspect_opp']
    
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
        l1_anchor="ap_v1.0.0_entry_2__aspects___conjunction_001_L1",
    )
    version: str = "1.0.0"
