"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008869
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
    semantic_id="lt_v1.0.0_lesson_15__card_pairs__牌卡配对_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson15CardPairs牌卡配对(SemanticEntry):
    """
    **Source Text** (Lines 1478-1571): Card pairs show balance issues. Law of Opposition - any quality i...
    """
    
    original_text: str = """**Source Text** (Lines 1478-1571): Card pairs show balance issues. Law of Opposition - any quality implies its opposite.

**English Paraphrase**: **Card pairs** reveal balance issues through the **Law of Opposition**: "any quality, once identified, implies its opposite." Three types: **Permanent pairs** (clear permanent opposites like Magician/High Priestess), **Court card/Ace pairs** (contrast suits or ranks), **Occasional pairs** (arise by chance, last for one instance). **Reinforcing pairs** can also strengthen same energy.

**Complete Chinese Interpretation**: **牌卡配对**通过**对立法则**揭示平衡问题："任何品质一旦被识别，就暗示其对立面。"三种类型：**永久配对**（如魔术师/女祭司等明确的永久对立）、**宫廷牌/王牌配对**（对比花色或等级）、**临时配对**（偶然产生，只持续一次）。**强化配对**也可以加强相同的能量。

**Law of Opposition**: "Any quality, once identified, implies its opposite"

**Three Types of Card Pairs**:
1. **Permanent Pairs** (永久配对): Clear, obvious permanent opposites
   - Eight of Swords (restriction) ↔ Four of Wands (freedom)
   - Magician (action/conscious) ↔ High Priestess (nonaction/unconscious)
2. **Court Card/Ace Pairs** (宫廷牌/王牌配对): Contrast suits or ranks
3. **Occasional Pairs** (临时配对): Arise by chance, useful comparisons

**Reinforcing Pairs**: Two cards strengthen same energy (e.g., Empress + Nine of Cups = pleasure/sensuality)

**Narrative Snippets**:
- `[ns_ltt_147]` `[trigger: law_opposition]` `[factor_trigger: tarot_pairs AND tarot_polarity]` `[role: 主干]` Law of Opposition: every quality contains and implies its shadow; strength implies vulnerability, giving implies receiving; when one card appears, consider what its polar opposite would mean—often both are operating.
- `[ns_ltt_148]` `[trigger: pair_types]` `[factor_trigger: tarot_pairs]` `[role: 主干依赖]` Three types: permanent, court/ace, occasional. Plus reinforcing pairs. → L1515-1569"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 15: Card Pairs (牌卡配对)"
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
        l1_anchor="lt_v1.0.0_lesson_15__card_pairs__牌卡配对_001_L1",
    )
    version: str = "1.0.0"
