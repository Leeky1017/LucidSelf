"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008145
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
    semantic_id="lt_v1.0.0_the_moon__月亮_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheMoon月亮(SemanticEntry):
    """
    **Source Text** (Lines 4654-4719): Keywords: Fear • Illusion • Imagination • Bewilderment

**English...
    """
    
    original_text: str = """**Source Text** (Lines 4654-4719): Keywords: Fear • Illusion • Imagination • Bewilderment

**English Paraphrase**: **The Moon (Card 18)** represents "the world of shadow and night"—fears, illusions, vivid imagination. "Be careful not to let deceptions and false ideas lead you astray."

**Complete Chinese Interpretation**: **月亮（第18号牌）**代表"阴影和夜晚的世界"——恐惧、幻觉、生动的想象力。"小心不要让欺骗和错误观念让你误入歧途。"

**Core Points**: Card 18 = fear, illusion, imagination, bewilderment; World of shadow; Beware deceptions

**Narrative Snippets**:
- `[ns_ltt_063]` `[trigger: moon_card]` `[factor_trigger: tarot_moon AND tarot_shadow]` `[role: 主干]` The Moon illuminates what daylight consciousness cannot see: the realm of shadow, intuition, and the collective unconscious; its light reveals hidden fears and buried memories that shape behavior from below awareness. → L4711-4712
- `[ns_ltt_064]` `[trigger: moon_illusion]` `[factor_trigger: tarot_moon AND tarot_illusion]` `[role: 主干依赖]` The Moon warns against mistaking subjective projections for objective reality: fears may be unfounded, suspicions may be paranoia—distinguish between genuine intuition and anxiety-driven fantasy. → L4717-4718"""
    normalized_text_zh: str = """"""
    subject: str = "The Moon (月亮)"
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_the_moon__月亮_001_L1",
    )
    version: str = "1.0.0"
