"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237683
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
    semantic_id="ap_v1.0.0_prelude_entry_9__alchemical_as_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry9AlchemicalAs(SemanticEntry):
    """
    **Source Text** (Lines 1404-1537):
> If Kabbalism and the type of astrology used in its magical prac...
    """
    
    original_text: str = """**Source Text** (Lines 1404-1537):
> If Kabbalism and the type of astrology used in its magical practices represent a sort of psychological animism, the true kind of alchemy stands for what we might call "psychological vitalism." Alchemy does not try to renounce nature and to center consciousness, as it were, outside of it, on the high peaks of the soul; nor does it try to command it by compulsion and the exercise of intellectual self-will. It assumes a universal life-substance which fills in the whole universe, physical and spiritual...
>
> [Paracelsus:] "No one needs to care for the course of Saturn: it neither shortens nor lengthens the life of anybody. If Mars is ferocious it does not follow that Nero was his child... It is an old saying that 'a wise man may rule the stars' and I believe in that saying—not in the sense in which you take it, but in my own. The stars force nothing into us that we are not willing to take; they incline us to nothing which we do not desire. They are free for themselves and we are free for ourselves..."
>
> Astrology must be reborn and must perform again for our modern world, made chaotic by an unbridled and false individualism and by the sudden opening of psychological dams, the task of practical integration which has always been its own... The fundamental work of astrology remains the same. It is to reveal the "Harmony of the Spheres" at whatever level man's consciousness is centered. It is to carry the symbol of Order wherever man finds chaos. In modern terminology, it is the algebra of life.

**Key Term Analysis**:
- **Psychological vitalism**: `alchemy's approach` / `vs psychological animism` / `universal life-substance`
- **Paracelsus's position**: `stars don't force` / `wise man rules stars` / `mutual freedom`
- **Microcosm-macrocosm identity**: `same life-substance` / `same principles` / `man as cosmic whole`
- **Astrology's rebirth**: `modern world need` / `practical integration` / `psychological task`
- **Algebra of life**: `fundamental definition` / `Order vs chaos` / `level-independent`
- **Great Work**: `individuation` / `psychological integration` / `building inner cosmos`

**English Paraphrase (Primary Language)**:
Rudhyar distinguishes alchemical astrology from Kabbalistic magic. While Kabbalism represents "psychological animism" (commanding astral forces through magical techniques), true alchemy represents "psychological vitalism"—working with universal life-substance that pervades everything, physical and spiritual.

Paracelsus's revolutionary statement encapsulates humanistic astrology's core: "The stars force nothing into us that we are not willing to take; they incline us to nothing which we do not desire." This isn't fatalistic determinism or magical manipulation, but recognition of mutual freedom and correspondence. Man's soul contains the same elements as stars; wisdom enables ruling the influences circulating within.

The Prelude culminates with astrology's mandate for rebirth: our modern world, chaotic from unbridled individualism and psychological upheaval, needs astrology's integrative function. The fundamental task remains constant across all eras: "to reveal the 'Harmony of the Spheres' at whatever level man's consciousness is centered... to carry the symbol of Order wherever man finds chaos." The definition: "the algebra of life."

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar区分了炼金占星学与卡巴拉魔法。卡巴拉代表"心理泛灵论"（通过魔法技术命令星界力量），而真正的炼金术代表"心理生机论"——与渗透一切（物质和精神）的普遍生命物质合作。

Paracelsus的革命性声明概括了人本占星学的核心："星星不会强迫我们接受任何我们不愿意接受的东西；它们不会使我们倾向于任何我们不渴望的东西。"这不是宿命论决定论或魔法操控，而是承认相互自由和对应。人的灵魂包含与星星相同的元素；智慧使人能够掌控内在循环的影响。

前奏以占星学重生的使命告终：我们的现代世界因不受控制的个人主义和心理动荡而混乱，需要占星学的整合功能。根本任务在所有时代保持不变："在人类意识所在的任何层次揭示'天球和谐'……在人发现混沌的任何地方携带秩序的象征。"定义："生命的代数。"

**Core Points**:
- Alchemy = psychological vitalism (vs Kabbalism = psychological animism)
- Universal life-substance fills physical and spiritual universe
- Paracelsus: "Stars force nothing...they incline us to nothing we don't desire"
- Mutual freedom between stars and humans
- Man's soul contains same elements as stars
- Wisdom enables ruling stellar influences
- Man (post-6th century) as microcosm
- Astrology's task: integration, Order vs chaos
- Fundamental work: reveal Harmony of Spheres at any consciousness level
- Definition: algebra of life

**Narrative Snippets**:
- `[ns_aop_053]` `[trigger: psychological_vitalism]` `[factor_trigger: psych_vitalism]` `[role: 主干]` Alchemy = psychological vitalism: working with universal life-substance pervading physical and spiritual. → Source Text L1406-1414
- `[ns_aop_054]` `[trigger: paracelsus_freedom]` `[factor_trigger: stars AND humans AND astro_freedom AND astro_mutual_freedom AND astro_non_coercive]` `[role: 主干依赖]` Paracelsus: "Stars force nothing into us we're not willing to take...wise man rules stars...they are free and we are free." → Source Text L1454-1461
- `[ns_aop_055]` `[trigger: astrology_rebirth]` `[factor_trigger: astrology_rebirth]` `[role: 条件分支]` Astrology must be reborn for modern world made chaotic—perform again task of practical integration. → Source Text L1526-1530
- `[ns_aop_056]` `[trigger: algebra_definition]` `[factor_trigger: modern_chaos]` `[role: 总结]` Fundamental work: reveal Harmony of Spheres at any level, carry Order where chaos—in modern terminology, algebra of life. → Source Text L1535-1537

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Paracelsus's statement anticipates Rudhyar's humanistic position by four centuries. The "stars incline but don't compel" became a standard formulation, though Rudhyar goes further in emphasizing mutual freedom.
- **中文**: Paracelsus的声明比Rudhyar的人本立场早四个世纪。"星星倾向但不强迫"成为标准表述，尽管Rudhyar在强调相互自由方面走得更远。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 9: Alchemical Astrology and Paracelsus's Vision"
    factor_refs: list = ['astro_psych_vitalism', 'astro_paracelsus_freedom', 'astro_rebirth_mandate', 'astro_great_work']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_prelude_entry_9__alchemical_as_001_L1",
    )
    version: str = "1.0.0"
