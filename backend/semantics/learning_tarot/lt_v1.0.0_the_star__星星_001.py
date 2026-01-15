"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008136
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
    semantic_id="lt_v1.0.0_the_star__星星_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheStar星星(SemanticEntry):
    """
    **Source Text** (Lines 4588-4653): Keywords: Hope • Inspiration • Generosity • Serenity

**English P...
    """
    
    original_text: str = """**Source Text** (Lines 4588-4653): Keywords: Hope • Inspiration • Generosity • Serenity

**English Paraphrase**: **The Star (Card 17)** represents hope—"most welcome when grief and despair have overwhelmed us." It is "the opposite of the Devil who strips us of faith in the future."

**Complete Chinese Interpretation**: **星星（第17号牌）**代表希望——"当悲伤和绝望压倒我们时最受欢迎。"它是"恶魔的对立面，恶魔剥夺了我们对未来的信心。"

**Core Points**: Card 17 = hope, inspiration, generosity, serenity; Opposite of Devil; Light in darkness

**Narrative Snippets**:
- `[ns_ltt_061]` `[trigger: star_card]` `[factor_trigger: tarot_star AND tarot_hope]` `[role: 主干]` The Star appears after Tower's devastation to signal that destruction was not the end: the naked woman pours water freely, unashamed and undefended, having nothing left to hide—vulnerability becomes strength when all pretense has been stripped away. → L4643-4644
- `[ns_ltt_062]` `[trigger: star_healing]` `[factor_trigger: tarot_star AND tarot_inspiration]` `[role: 主干依赖]` The Star's hope is not naive optimism but calm certainty born of having survived the worst: the stars above are distant but their light reaches us—connection to something greater than personal suffering restores meaning. → L4645-4646"""
    normalized_text_zh: str = """"""
    subject: str = "The Star (星星)"
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
        l1_anchor="lt_v1.0.0_the_star__星星_001_L1",
    )
    version: str = "1.0.0"
