"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008096
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
    semantic_id="lt_v1.0.0_death__死神_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Death死神(SemanticEntry):
    """
    **Source Text** (Lines 4329-4395): Keywords: Ending • Transition • Elimination • Inexorable Forces

...
    """
    
    original_text: str = """**Source Text** (Lines 4329-4395): Keywords: Ending • Transition • Elimination • Inexorable Forces

**English Paraphrase**: **Death (Card 13)**: "In tarot, Death is not permanent end but transition to new state. To grow, to move, to live—we must 'die' to the old to give birth to the new."

**Complete Chinese Interpretation**: **死神（第13号牌）**："在塔罗中，死亡不是永久终结而是向新状态的过渡。要成长、移动、活着——我们必须'死于'旧事物以诞生新事物。"

**Core Points**: Card 13 = ending, transition, elimination; Not physical death; Transition to new state

**Narrative Snippets**:
- `[ns_ltt_053]` `[trigger: death_card]` `[factor_trigger: tarot_death AND tarot_transition]` `[role: 主干]` Death initiates necessary endings that clear space for new growth: what is exhausted, outworn, or no longer serving must be released; resistance to this natural cycle creates stagnation and suffering. → L4379-4382
- `[ns_ltt_054]` `[trigger: death_transformation]` `[factor_trigger: tarot_death AND tarot_transformation]` `[role: 主干依赖]` Death's transformation is not cosmetic but fundamental: the caterpillar does not get wings added—it dissolves entirely before the butterfly emerges; ego-death precedes spiritual rebirth. → L4388-4390"""
    normalized_text_zh: str = """"""
    subject: str = "Death (死神)"
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
        l1_anchor="lt_v1.0.0_death__死神_001_L1",
    )
    version: str = "1.0.0"
