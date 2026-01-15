"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238300
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
    semantic_id="ap_v1.0.0_entry_4__planetary_pattern___f_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4PlanetaryPatternF(SemanticEntry):
    """
    **Source Text** (Lines 13093-13196):
> Here we deal not only with the elementary relationship betwee...
    """
    
    original_text: str = """**Source Text** (Lines 13093-13196):
> Here we deal not only with the elementary relationship between two planets but with relationships that involve the whole personality, that focus the meaning of the whole personality...
>
> The determination of centers of significance, of what Marc Jones calls "focal determinators," is the first and most important factor in the interpretation of a birth-chart...
>
> All planets above the horizon: "The native necessarily lives out in life"... All planets below the horizon: "The native lives within himself or in more subjective realms"...
>
> If nine planets are found in one hemisphere and the tenth in the other... This tenth stands out powerfully... It becomes an absolutely "outstanding" factor... Marc Jones compares this formally isolated planet ("singleton") to an aching tooth which dominates the whole consciousness.

**Key Term Analysis**:
- **Focal determinators**: `centers of significance` / `Marc Jones term` / `most important factor`
- **Above/below horizon**: `extraversion vs introversion` / `outer vs inner focus`
- **East/West meridian**: `free choice vs accepting issues` / `thinking vs feeling`
- **Singleton**: `isolated planet` / `aching tooth` / `irrational accentuation`

**English Paraphrase (Primary Language)**:
"Focal determinators" (Marc Jones) = centers of significance, the most important factor in chart interpretation.

Hemisphere distributions:
- All above horizon: "lives out in life," extraversion
- All below: "lives within himself," introversion
- All East: "makes own choice in every issue"
- All West: "must accept choices placed before him"

Singleton = isolated planet in opposite hemisphere, like "aching tooth dominating whole consciousness." Becomes "autocratic factor."

**Complete Chinese Interpretation (Secondary Language)**:
"焦点决定因子"（Marc Jones） = 意义中心，星盘解读中最重要的因素。

半球分布：
- 全在地平线上：外向，"在生活中活出来"
- 全在地平线下：内向，"活在自己内心"
- 全在东边："在每个问题上做出自己的选择"
- 全在西边："必须接受放在他面前的选择"

单星 = 孤立在对面半球的行星，像"支配整个意识的牙痛"。成为"独裁因素"。

**Narrative Snippets**:
- `[ns_aop_205]` `[trigger: focal_determinators]` `[factor_trigger: astro_focal_det AND astro_focal]` `[role: 主干]` Focal determinators = centers of significance; most important factor in chart interpretation. → L13108-13117
- `[ns_aop_206]` `[trigger: singleton]` `[factor_trigger: astro_singleton_planet AND astro_singleton]` `[role: 主干依赖]` Singleton = isolated planet; like aching tooth; autocratic factor dominating consciousness. → L13185-13196"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: Planetary Pattern - Focal Determinators"
    factor_refs: list = ['focal_det', 'singleton', 'stellium']
    
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
        l1_anchor="ap_v1.0.0_entry_4__planetary_pattern___f_001_L1",
    )
    version: str = "1.0.0"
