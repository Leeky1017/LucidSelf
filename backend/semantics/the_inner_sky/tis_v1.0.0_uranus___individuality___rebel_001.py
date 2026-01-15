"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.100980
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
    semantic_id="tis_v1.0.0_uranus___individuality___rebel_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class UranusIndividualityRebel(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Invisible Planet | Requi...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Invisible Planet | Requires conscious work | Nature |
| Individuality | Beyond personality | Core function |
| Cultural Programming | Internalized rules | What to transcend |
| Beyond Saturn | Past ordinary limits | Realm |

#### Source Text

"Uranus, Neptune, and Pluto represent only possibilities. They signify transcendent, unnatural qualities attainable only through intentional work on the self unlike the classical planets, no positive manifestation of their functions can ever be triggered automatically. Until we purposefully move to transform our being, we see only their shadows. Without effort, these three mysterious symbols remain to the spirit exactly as they are to the eye: invisible."

"Uranus
Function:
• The development of individuality
• The development of the capacity to question authority
• The transcendence of cultural and social programming
Dysfunction:
• Contrariness, stubbornness, inflexibility, touchiness, quirkishness, unreliability, irresponsibility, selfishness, insensitivity to others’ feelings, inability to learn from others, eccentricity for its own sake"

"The astrological label for that untamable quality is Uranus. This is the planet of individuality, of freedom. Nothing is more delightful to it than the prospect of mutiny. It is independent, rebellious, headstrong and colorful... Uranus challenges us to be free. Where it lies on the birth-chart the high drama of rebellion crackles in our mental circuitry. It symbolizes an area in which our essence makes war on the constraints imposed on us by our culture. To be true to ourselves, we must break the rules."

#### English Paraphrase (Primary Language)

**Uranus** represents the **individuality and rebellion function**—the part of the psyche that refuses to be flattened by culture, rules, or expectations. It belongs to the family of "invisible planets": forces that cannot express constructively on their own, but become available only through conscious, intentional work on the self. Before that work, we mostly meet their shadow forms.

On the positive side, Uranus develops individuality, the capacity to question authority, and the ability to step outside cultural and social programming. It is the inner outlaw that will not accept being steamrollered by "Miss Manners"—the drive to live one’s own truth even when it offends convention. It delights in freedom, mutiny, and creative nonconformity, and often coincides with flashes of insight and original thinking.

On the shadow side, the same energy can collapse into contrariness for its own sake: stubbornness, unreliability, quirkiness that ignores other people’s feelings, and rebellion that serves only ego. Where Uranus lies in the birthchart, Forrest suggests, we face an ongoing drama between our essence and our culture. To be true to ourselves there, we must learn to break dead rules without simply destroying healthy structures.

#### Complete Chinese Interpretation

**天王星**代表**个体性与反叛功能**——那一部分拒绝被文化、规则和期待压扁的心灵力量。它属于所谓「不可见行星」家族：这些力量本身无法自动以正向方式表达，只有在我们有意识地进行自我工作时，它们才会以建设性的形式出现；在此之前，我们更多遇见的是它们的阴影。

在正向层面，天王星推动**个体性的展开**、**质疑权威的能力**，以及**超越社会与文化编程的自由**。它是内在的「亡命之徒」：不肯被礼节和成规碾平，坚持活出自己的真实，即便这会冒犯惯例。它热爱自由、叛逆与非传统，经常伴随灵感闪现和原创思维。

在阴影层面，同一股能量会蜕变为纯粹的「唱反调」：固执、难以合作、古怪而不顾他人感受，只为反对而反对的行为模式。Forrest 认为，天王星在命盘中所落之处，是自我本质与所在文化持续「交战」的领域：在那里，要忠于自己，就必须学会打破僵死的规则，但同时避免把真正有生命力的结构一并摧毁。

#### Core Points

- Uranus = individuality, rebellion, freedom beyond Saturn's structures.
- Belongs to the "invisible planets"—requires conscious work for constructive expression.
- Positive: questioning authority, breaking dead rules, transcending cultural programming.
- Shadow: contrariness, unreliability, egoic rebellion that harms relationships.
- Chart position shows where essence and culture are in ongoing tension.

#### Narrative Snippets

- `[ns_innersky_uranus_001]` `[trigger: planet_uranus]` `[factor_trigger: planet_uranus AND individuality]` `[role: 主干]` Uranus is the planet of individuality, rebellion, and freedom beyond Saturn's structures. It belongs to the "invisible planets"—requiring conscious work for constructive expression. → The Inner Sky Ch.6 #Uranus
- `[ns_innersky_uranus_002]` `[trigger: planet_uranus AND astro_function]` `[factor_trigger: astro_planet_uranus]` `[role: 主干依赖]` Uranus questions authority, breaks dead rules, transcends cultural programming. It develops individuality distinct from personality masks. → The Inner Sky Ch.6 #Uranus
- `[ns_innersky_uranus_003]` `[trigger: planet_uranus AND astro_shadow]` `[factor_trigger: astro_planet_uranus AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: contrariness (opposing just to oppose), unreliability, egoic rebellion that harms relationships—rebellion without purpose. → The Inner Sky Ch.6 #Uranus
- `[ns_innersky_uranus_004]` `[trigger: planet_uranus AND astro_chart]` `[factor_trigger: astro_planet_uranus]` `[role: 总结]` Chart position shows where essence and culture are in ongoing tension—where being true to self requires breaking free from collective programming. → The Inner Sky Ch.6 #Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus - Individuality & Rebellion Beyond Saturn"
    factor_refs: list = ['individuality']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_uranus___individuality___rebel_001_L1",
    )
    version: str = "1.0.0"
