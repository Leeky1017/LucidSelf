"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008154
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
    semantic_id="lt_v1.0.0_the_sun__太阳_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheSun太阳(SemanticEntry):
    """
    **Source Text** (Lines 4720-4781): Keywords: Enlightenment • Vitality • Greatness • Assurance

**Eng...
    """
    
    original_text: str = """**Source Text** (Lines 4720-4781): Keywords: Enlightenment • Vitality • Greatness • Assurance

**English Paraphrase**: **The Sun (Card 19)** represents "vitality and splendor"—total confidence, unlimited energy, radiant health. "Now is the time to let your light shine."

**Complete Chinese Interpretation**: **太阳（第19号牌）**代表"活力和辉煌"——完全的自信、无限的能量、光芒四射的健康。"现在是让你的光芒闪耀的时候。"

**Core Points**: Card 19 = enlightenment, vitality, greatness, assurance; Total confidence; Let your light shine

**Narrative Snippets**:
- `[ns_ltt_065]` `[trigger: sun_card]` `[factor_trigger: tarot_sun AND tarot_vitality]` `[role: 主干]` The Sun represents ego-consciousness at its healthiest: the clear light of day dispels Moon's shadows; confidence flows from genuine self-knowledge rather than denial; energy is abundant because nothing is being repressed. → L4774-4775
- `[ns_ltt_066]` `[trigger: sun_success]` `[factor_trigger: tarot_sun AND tarot_greatness]` `[role: 主干依赖]` The Sun signals that conditions favor authentic self-expression: inner light aligns with outer circumstance; what you genuinely are can now shine without obstruction or apology. → L4780-4781"""
    normalized_text_zh: str = """"""
    subject: str = "The Sun (太阳)"
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
        l1_anchor="lt_v1.0.0_the_sun__太阳_001_L1",
    )
    version: str = "1.0.0"
