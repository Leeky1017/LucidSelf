"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288059
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
    semantic_id="pit_v1.0.0_mars_in_the_tenth_house__火星过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheTenthHouse火星过境第(SemanticEntry):
    """
    **Source Text** (Lines 8516-8540):
> Mars at home in house of highest ego expression. Arouses ambiti...
    """
    
    original_text: str = """**Source Text** (Lines 8516-8540):
> Mars at home in house of highest ego expression. Arouses ambition to achieve. Identify with project, work extremely hard. Need independent project, individual initiative. Not tolerant of others' authority—prefer to be own boss. Energy makes impression on those who can help. Problem: conflict with authority figures. Conflicts with coworkers if they feel threatened. Play down conflicts, remain conscious of others' interests.

**English Paraphrase**: Ambition aroused. Work hard on independent projects. Prefer to be own boss. May conflict with authorities. Play down conflicts, consider others' interests.

**Complete Chinese Interpretation**: 雄心被激发。在独立项目上努力工作。喜欢当自己的老板。可能与权威冲突。淡化冲突，考虑他人利益。

**Narrative Snippets**:
- `[ns_pit_ma010]` `[trigger: mars_transit_house_10]` `[factor_trigger: astro_transit_mars AND astro_house_10]` `[role: 主干]` Ambition aroused. Independent projects. May conflict with authorities. Consider others' interests. → PIT Ch8 Mars-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Tenth House (火星过境第十宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_tenth_house__火星过境第_001_L1",
    )
    version: str = "1.0.0"
