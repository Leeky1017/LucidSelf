"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318507
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
    semantic_id="pit_v1.0.0_saturn_in_the_eleventh_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheEleventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 12546-12572):
> Principal task: integrate individual self with group expressi...
    """
    
    original_text: str = """**Source Text** (Lines 12546-12572):
> Principal task: integrate individual self with group expression. Groups demand integration. After 10H individual shine, now join others, be less of a star. Continuation of high period if answer challenges. If difficult to work with others, may feel coworkers and friends getting in your way. They give responsibilities you don't want. Try to come to terms rather than avoid. House of hopes, wishes, ideals, objectives. Find out if worked effectively to attain ideals. Saturn brings results if prepared well. If not, expectations disappointed—clear that not getting what you want. Then 12H will be breakdown and clearing for next cycle. First transit often not as successful as second—comes too early. Usually need two transits for experience and maturity.

**English Paraphrase**: Integrate self with groups. Less individual star, more team. Continuation of high period if handle challenges. Friends and groups make demands. Find out if ideals achieved. If prepared, results come. If not, disappointment—clearing for next cycle.

**Complete Chinese Interpretation**: 将自我与群体整合。不那么个人明星，更多团队。如果处理好挑战，高峰期延续。朋友和群体提出要求。发现理想是否实现。如果准备好了，结果来临。如果没有，失望——为下一周期清理。

**Narrative Snippets**:
- `[ns_pit_sa011]` `[trigger: saturn_transit_house_11]` `[factor_trigger: astro_transit_saturn AND astro_house_11]` `[role: 主干]` Integrate with groups. Less individual, more team. Results of ideals tested. → PIT Ch10 Saturn-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Eleventh House (土星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_eleventh_house___001_L1",
    )
    version: str = "1.0.0"
