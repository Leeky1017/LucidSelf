"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008859
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
    semantic_id="lt_v1.0.0_lesson_14__court_cards__宫廷牌_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson14CourtCards宫廷牌(SemanticEntry):
    """
    **Source Text** (Lines 1373-1477): 16 court cards represent personality types. Personality = combina...
    """
    
    original_text: str = """**Source Text** (Lines 1373-1477): 16 court cards represent personality types. Personality = combination of suit + rank.

**English Paraphrase**: The **16 court cards** represent personality types. Each personality is "a combination of its suit and rank." **Kings** are "active and outgoing, want to make impact through force of personality." **Queens** "embody qualities from inside, set tone without imposing." **Knights** are "extremists expressing suit to maximum"—can be positive or negative. **Pages** are "playful children acting out qualities with pleasure and abandon."

**Complete Chinese Interpretation**: **16张宫廷牌**代表人格类型。每种人格是"其花色和等级的组合。"**国王**"积极外向，想通过人格力量产生影响。"**王后**"从内在体现品质，设定基调而不强加。"**骑士**是"将花色发挥到极致的极端主义者"——可以是积极或消极的。**侍从**是"以愉悦和放纵表演品质的顽皮孩子。"

**Four Court Card Ranks**:
1. **Kings** (国王): Active, outgoing, make impact, demonstrate authority/control/mastery
2. **Queens** (王后): Embody from inside, set tone without imposing, relaxed/natural
3. **Knights** (骑士): Extremists, express suit to maximum, positive OR tarot_negative
4. **Pages** (侍从): Playful children, loose/spontaneous, symbol of adventure/possibility

**Three Interpretation Possibilities**:
1. **Side of yourself** being expressed or seeking expression
2. **Another person** in your life
3. **General atmosphere** taking on personality

**Narrative Snippets**:
- `[ns_ltt_145]` `[trigger: court_card_system]` `[factor_trigger: tarot_court_cards]` `[role: 主干]` 16 court cards = personality types, combination of suit + rank. → L1380-1383
- `[ns_ltt_146]` `[trigger: court_interpretation]` `[factor_trigger: tarot_court_cards]` `[role: 主干依赖]` Court card can be: side of you, another person, or general atmosphere. → L1437-1474"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 14: Court Cards (宫廷牌)"
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
        l1_anchor="lt_v1.0.0_lesson_14__court_cards__宫廷牌_001_L1",
    )
    version: str = "1.0.0"
