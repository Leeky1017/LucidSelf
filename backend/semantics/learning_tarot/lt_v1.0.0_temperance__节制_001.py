"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008105
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
    semantic_id="lt_v1.0.0_temperance__节制_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Temperance节制(SemanticEntry):
    """
    **Source Text** (Lines 4396-4458): Keywords: Temperance • Balance • Health • Combination

**English ...
    """
    
    original_text: str = """**Source Text** (Lines 4396-4458): Keywords: Temperance • Balance • Health • Combination

**English Paraphrase**: **Temperance (Card 14)** represents "quiet composure"—moderation, balance. Its energy is like "the calm of a hurricane's eye"—still center amid swirling change.

**Complete Chinese Interpretation**: **节制（第14号牌）**代表"安静的镇定"——适度、平衡。它的能量像"飓风眼中的平静"——变化旋涡中的静止中心。

**Core Points**: Card 14 = temperance, balance, health, combination; Hurricane's eye calm; Moderation

**Narrative Snippets**:
- `[ns_ltt_055]` `[trigger: temperance_card]` `[factor_trigger: tarot_temperance AND tarot_balance]` `[role: 主干]` Temperance achieves equilibrium not through rigidity but through continuous dynamic adjustment: the angel pours water between cups without spilling—mastery of opposing forces through patient skill, not suppression. → L4443-4450
- `[ns_ltt_056]` `[trigger: temperance_balance]` `[factor_trigger: tarot_temperance AND tarot_integration]` `[role: 主干依赖]` Temperance's synthesis creates something new from apparent opposites: fire and water, conscious and unconscious, spirit and matter combine into unified whole greater than its parts. → L4452-4454"""
    normalized_text_zh: str = """"""
    subject: str = "Temperance (节制)"
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
        l1_anchor="lt_v1.0.0_temperance__节制_001_L1",
    )
    version: str = "1.0.0"
