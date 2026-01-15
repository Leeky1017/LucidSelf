"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237755
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
    semantic_id="ap_v1.0.0_entry_4__individual_vs_collect_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4IndividualVsCollect(SemanticEntry):
    """
    **Source Text** (Lines 1886-1914):
> Two basic points must be mentioned, for they have a capital imp...
    """
    
    original_text: str = """**Source Text** (Lines 1886-1914):
> Two basic points must be mentioned, for they have a capital importance in any solid philosophy of astrology. The first is that we shall always find in any type of thought dealing with life a fundamental interpenetration between individual values and collective values. The individual may be free, but that freedom is certainly bound by the magnetic field, or aura, of the collectivity to which he belongs—the "Ring-Pass-Not" of Oriental occultism.
>
> No astrological birth-chart can be judged with accuracy, if the general conditions of the group to which the native belongs as an individual, are unknown. This refers both to the social group (family, race, religion) and to that other grouping in consciousness which creates levels of being. A Chinese coolie may have exactly the same birth-chart as a European nobleman... And it is obvious that no one could infer accurately from the birth-chart alone what the Chinaman's life would be.

**Key Term Analysis**:
- **Individual-collective interpenetration**: `freedom bounded` / `Ring-Pass-Not` / `mutual influence`
- **Group context necessity**: `family, race, religion` / `levels of being` / `chart alone insufficient`
- **Chinese coolie-European nobleman**: `same chart` / `different manifestation` / `group determines expression`

**English Paraphrase (Primary Language)**:
Rudhyar establishes a fundamental principle: individual and collective values interpenetrate. Individual freedom is bounded by the collectivity's "Ring-Pass-Not." No birth-chart can be judged accurately without knowing the native's group context—social (family, race, religion) and consciousness level. The same chart in a Chinese coolie and European nobleman would manifest entirely differently. The chart reveals individual tendencies; the group determines their actual expression.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar确立了一个根本原则：个体与集体价值相互渗透。个体自由受限于集体的"不可逾越之环"。没有了解命主的群体背景——社会的（家庭、种族、宗教）和意识层面的——就无法准确判断出生图。中国苦力与欧洲贵族的同一星图会有完全不同的显化。星图揭示个体倾向；群体决定其实际表达。

**Core Points**:
- Individual-collective values fundamentally interpenetrate
- Individual freedom bounded by collective "Ring-Pass-Not"
- Chart cannot be judged without group context
- Social group: family, race, religion
- Consciousness level also matters
- Same chart, different person = different manifestation
- Chart = individual tendencies; group = actual expression

**Narrative Snippets**:
- `[ns_aop_069]` `[trigger: interpenetration]` `[factor_trigger: collective AND astro_interpen AND astro_ind_coll_struct]` `[role: 主干]` Individual-collective values interpenetrate; freedom bounded by collective Ring-Pass-Not. → L1890-1896
- `[ns_aop_070]` `[trigger: group_context]` `[factor_trigger: group_context AND astro_group_req]` `[role: 主干依赖]` Chart can't be judged without group context—social and consciousness level. → L1900-1904
- `[ns_aop_071]` `[trigger: coolie_nobleman]` `[factor_trigger: astro_same_chart]` `[role: 条件分支]` Chinese coolie and European nobleman with same chart—entirely different lives. → L1906-1910
- `[ns_aop_072]` `[trigger: tendency_expression]` `[factor_trigger: astro_tend_expr AND astro_tend_expr_state]` `[role: 总结]` Chart = individual tendencies; group determines actual expression. → L1911-1914"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: Individual vs Collective Values"
    factor_refs: list = ['astro_ind_coll', 'astro_ring_pass', 'astro_group_context', 'astro_tend_expr']
    
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
        l1_anchor="ap_v1.0.0_entry_4__individual_vs_collect_001_L1",
    )
    version: str = "1.0.0"
