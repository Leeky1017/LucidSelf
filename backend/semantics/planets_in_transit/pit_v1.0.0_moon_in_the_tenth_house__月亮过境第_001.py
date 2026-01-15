"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301082
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
    semantic_id="pit_v1.0.0_moon_in_the_tenth_house__月亮过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheTenthHouse月亮过境第(SemanticEntry):
    """
    **Source Text** (Lines 3745-3762):
> Professional and business concerns in focus, but in a way that ...
    """
    
    original_text: str = """**Source Text** (Lines 3745-3762):
> Professional and business concerns in focus, but in a way that tests you. Your most intimate and personal life is on public display more than usual—may be difficult to hide certain facts. Even if you usually have reservations about emotional display in public, you're likely to indulge now (public argument with spouse, public emotional outburst). This can be advantageous in career—more emotional sensitivity and empathy toward coworkers. Be careful about blurring professional/personal distinctions. Good for public relations and sales work.

**English Paraphrase**: Professional concerns in focus—tested. Intimate life on public display—hard to hide facts. May have public emotional displays despite reservations. Can be career advantage—sensitivity to coworkers. Careful not to blur professional/personal. Good for PR and sales.

**Complete Chinese Interpretation**: 职业关注成为焦点——受到测试。私密生活公开展示——难以隐藏事实。可能有公开情感表达尽管有顾虑。可以是职业优势——对同事的敏感度。小心不要模糊职业/个人界限。适合公关和销售。

**Narrative Snippets**:
- `[ns_pit_m019]` `[trigger: moon_transit_house_10]` `[factor_trigger: astro_transit_moon AND astro_house_10]` `[role: 主干]` Professional concerns in focus—intimate life on public display. May have public emotional displays. → PIT Ch5 Moon-10H
- `[ns_pit_m020]` `[trigger: moon_transit_house_10]` `[factor_trigger: astro_transit_moon AND astro_house_10 AND emotional_sensitivity AND career_success]` `[role: 条件分支]` Can be career advantage—emotional sensitivity to coworkers. Good for PR and sales. → PIT Ch5 Moon-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Tenth House (月亮过境第十宫)"
    factor_refs: list = ['state_public_emotional', 'state_professional_personal_blur', 'state_empathy_advantage']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_tenth_house__月亮过境第_001_L1",
    )
    version: str = "1.0.0"
