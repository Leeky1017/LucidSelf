"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251421
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
    semantic_id="pit_v1.0.0_transits_as_intentions__行运作为意图_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class TransitsAsIntentions行运作为意图(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Transits symbolize original intentions manifesting, not ...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Transits symbolize original intentions manifesting, not external fate. The horoscope is a map of intentions, not a prediction of events. Character is destiny. The person unconsciously intends certain experiences; transits show when those intentions naturally ripen into manifestation."

**English Paraphrase (Primary Language)**:
Hand's deepest philosophy reframes transits entirely: they are not **external fate** imposed by planets but **manifestations of original intentions**. Before birth or in early childhood, the soul/psyche forms intentions—patterns of what it needs to learn, experience, and become. The natal chart maps these intentions. Transits then show **when those intentions naturally ripen into external expression**. This radically shifts responsibility: you are not a victim of planetary forces but a conscious participant in your own unfolding. The phrase "character is destiny" captures this: your deep character (intentions) creates your life circumstances through synchronistic timing. When Saturn transits your Sun, you're not being punished by Saturn; you're meeting the maturation challenge you originally intended to face.

**Complete Chinese Interpretation (Secondary Language)**:
汉德最深层的哲学是对行运的彻底重构：行运不是行星强加的**外部命运**，而是**原始意图的显化**。在出生前或幼年，灵魂/心理形成了意图——需要学什么、经历什么、成为什么的模式。本命盘映射这些意图。行运则显示**这些意图何时自然成熟为外部表达**。这从根本上转移了责任：你不是行星力量的受害者，而是自己展开过程中的有意识参与者。"性格即命运"这句话抓住了核心：你的深层性格（意图）通过同步性时机创造你的人生环境。当土星行运到你的太阳，你不是被土星惩罚，而是在遇见你原本打算面对的成熟挑战。

**Key Term Analysis**:
- **Original Intentions**: `pre-birth or early childhood` / `soul's curriculum` / `deep character pattern`
- **Manifestation not Fate**: `intention ripens` / `synchronistic timing` / `not external imposition`
- **Character is Destiny**: `deep character creates circumstances` / `responsibility shift` / `conscious participation`

**Core Points** (decomposed, no upper limit):
- Transits symbolize original intentions manifesting, not external fate
- Horoscope = map of intentions, not prediction of events
- Character is destiny: deep character creates life circumstances
- Person unconsciously intends certain experiences
- Transits show when intentions naturally ripen into manifestation
- Shifts responsibility from victim to conscious participant
- Raises consciousness through recognizing own intention

**Detailed Explanation**:
This philosophy transforms astrology from a fatalistic prediction system into a consciousness-raising tool. Instead of asking "What will happen to me?" the question becomes "What am I intending to learn through this transit?" This is profoundly empowering because it returns agency to the person. Even difficult transits (Saturn, Pluto) become understood as chosen learning experiences rather than cosmic punishments. The astrologer's role shifts from fortune-teller to guide helping the person recognize and cooperate with their own deeper intentions.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_005]` `[trigger: original_intentions]` `[factor_trigger: astro_original_intentions]` `[role: 主干]` Transits symbolize original intentions manifesting, not external fate. → Source Text
- `[ns_hand_pit_006]` `[trigger: character_destiny]` `[factor_trigger: astro_character_destiny]` `[role: 主干依赖]` Character is destiny—deep character creates life circumstances through synchronistic timing. → Source Text
- `[ns_hand_pit_007]` `[trigger: consciousness_raising]` `[factor_trigger: astro_consciousness_raising]` `[role: 总结]` Recognizing transits as own intentions raises consciousness and returns responsibility. → English Paraphrase
- `[ns_pit_pc]` `[trigger: past_conditioning]` `[factor_trigger: past_conditioning]` `[role: 条件分支]` Past conditioning refers to behavioral and emotional patterns developed in childhood that influence current responses. → PIT Foundation
- `[ns_pit_pp]` `[trigger: past_patterns]` `[factor_trigger: past_patterns]` `[role: 条件分支]` Past patterns are repetitive life themes rooted in early experience that transits may activate for conscious examination. → PIT Foundation
- `[ns_pit_us]` `[trigger: unconscious_self]` `[factor_trigger: unconscious_self]` `[role: 条件分支]` Unconscious self contains repressed material, shadow contents, and unintegrated aspects that transits bring to awareness. → PIT Foundation
- `[ns_pit_sc]` `[trigger: self_control]` `[factor_trigger: self_control]` `[role: 效果]` Self-control is the capacity to manage impulses and direct energy consciously—challenged or strengthened by transits. → PIT Foundation
- `[ns_pit_att]` `[trigger: attachment]` `[factor_trigger: attachment]` `[role: 条件分支]` Attachment patterns from early bonding affect how transits are experienced in relationships. → PIT Foundation
- `[ns_pit_er]` `[trigger: emotional_repression]` `[factor_trigger: emotional_repression]` `[role: 条件分支]` Emotional repression is the suppression of feelings that may surface during emotionally activating transits. → PIT Foundation
- `[ns_pit_hf]` `[trigger: hidden_feelings]` `[factor_trigger: hidden_feelings]` `[role: 条件分支]` Hidden feelings are emotions kept from consciousness that transits may expose for integration. → PIT Foundation
- `[ns_pit_lr]` `[trigger: love_relationship]` `[factor_trigger: love_relationship]` `[role: 条件分支]` Love relationship dynamics are activated by Venus, 7th house, and relationship-focused transits. → PIT Foundation
- `[ns_pit_fr]` `[trigger: friendship]` `[factor_trigger: friendship]` `[role: 条件分支]` Friendship patterns relate to 11th house themes and are activated by relevant transits. → PIT Foundation
- `[ns_pit_cf]` `[trigger: confrontation]` `[factor_trigger: confrontation]` `[role: 效果]` Confrontation may arise during Mars or Pluto transits challenging established patterns. → PIT Foundation
- `[ns_pit_vs]` `[trigger: value_system]` `[factor_trigger: value_system]` `[role: 条件分支]` Value system represents core beliefs about worth—examined during 2nd house and Venus transits. → PIT Foundation

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Hand's intention framework is his distinctive contribution to modern astrology, moving beyond mechanical prediction toward psychological and spiritual interpretation.
- **中文**: Hand的意图框架是他对现代占星的独特贡献，超越了机械预测，走向心理与灵性解读。"""
    normalized_text_zh: str = """"""
    subject: str = "Transits as Intentions (行运作为意图)"
    factor_refs: list = ['astro_original_intentions', 'astro_character_destiny', 'astro_consciousness_raising', 'astro_soul_curriculum']
    
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
        l1_anchor="pit_v1.0.0_transits_as_intentions__行运作为意图_001_L1",
    )
    version: str = "1.0.0"
