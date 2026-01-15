"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574912
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
    semantic_id="cw_v1.0.0_source_text_004",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "The shadow is a moral problem that challenges the whole ego-personality, for no one can become cons...
    """
    
    original_text: str = """"The shadow is a moral problem that challenges the whole ego-personality, for no one can become conscious of the shadow without considerable moral effort. To become conscious of it involves recognizing the dark aspects of the personality as present and real. This act is the essential condition for any kind of self-knowledge, and it therefore, as a rule, meets with considerable resistance. The shadow is that hidden, repressed, for the most part inferior and guilt-laden personality whose ultimate ramifications reach back into the realm of our animal ancestors."

#### English Paraphrase (Primary Language)

The **Shadow** is Jung's term for everything we've **rejected, repressed, or denied** about ourselves—the parts of psyche deemed unacceptable to ego-consciousness and persona. It's not purely evil but **undeveloped, primitive, and unintegrated**—containing both genuine darkness and unrealized gold.

**Shadow formation**:
- **Early life**: Child has full range of potentials—aggression, sexuality, creativity, softness
- **Socialization**: Family/culture approves certain traits, condemns others
- **Repression**: Condemned traits pushed into unconscious, forming shadow
- **Result**: Persona (acceptable self) + Shadow (rejected self)

**Shadow contents**:
- **Personal shadow**: Individual's repressed qualities—denied anger, forbidden sexuality, unaccepted weakness
- **Collective shadow**: Cultural repressions—racism, scapegoating, projected evil
- **"Gold in the shadow"**: Not just negative—often contains repressed creativity, vitality, authentic emotion society condemned

**How shadow manifests**:
- **Projection**: Seeing in others what we deny in ourselves—"I'm not angry, YOU'RE angry!"
- **Dreams**: Shadow appears as same-sex figure (threatening, inferior, or fascinating)
- **Slips of tongue**: Unconscious breaking through
- **Strong reactions**: Disproportionate emotional response signals shadow projection
- **Scapegoating**: Collective shadow projected onto minorities, enemies

**Integration work**:
1. **Recognition**: Admit these rejected qualities exist in you
2. **Withdrawal of projections**: "This quality I hate in them, where is it in me?"
3. **Moral reckoning**: Face guilt, shame, but without identification (I have darkness, I'm not only darkness)
4. **Assimilation**: Bring shadow qualities into consciousness, integrate appropriately

**Why it's hard**: Recognizing shadow threatens ego-identity and persona. If I've built identity as "nice person," admitting aggression feels like ego-death. Considerable moral courage required.

**Necessity**: **No individuation without shadow integration**. Cannot become whole while rejecting half of self. Shadow work is prerequisite for further development.

**The "dark brother"**: Jung's poetic term—shadow is sibling, not enemy. Rejected part of self seeking recognition and integration, not annihilation.

#### Complete Chinese Interpretation (Secondary Language)

完整中文诠释：阴影指的是我们人格中所有**被拒绝、被压抑、被否认**的部分——那些曾经在童年或成长过程中被家庭、文化、宗教视为“不该有”的冲动、欲望、脆弱、愤怒、贪婪、嫉妒，乃至某些被贬低的天赋（例如被说成“太敏感”“太张扬”的特质）。社会化的过程一方面塑造出一个“可以被看见并被赞许的我”（人格面具/Persona），另一方面也在背面堆积起一个“绝不能承认存在的我”（阴影）。从荣格的角度看，只要有面具，就一定会有与之互补的阴影，它们像硬币的两面一样共同构成自我形象。

阴影最常通过**投射（projection）**的方式表现：我们把自己不愿承认或尚未发展成熟的特质，全部“看见”在别人身上——极度厌恶某类人、动辄指责他人的缺点、对某些行为反应过度激烈，往往都说明那里有自己的阴影被钩住。梦中出现的同性人物、低劣小人、陌生的跟踪者，常常就是阴影的象征化呈现。集体层面上，民族主义狂热、对外群体的妖魔化与替罪羊机制，则是“集体阴影”被倾倒到某一族群或敌人身上的表现。

真正的阴影工作包含几个步骤：首先是**承认**——有勇气说出“这些难堪的品质也确实存在于我之中”；其次是**收回投射**——从“他们都很坏”转向“我为什么如此被这类行为触动”；再往后，是在不认同“我就是这些黑暗”的前提下，**学习与之共处并适度表达**（例如承认愤怒、学会设立界限，而不是要么完全压抑、要么完全爆炸）。荣格称阴影为“黑暗兄弟”（dark brother），强调它是需要被带回家、教育与整合的**手足**，而不是必须被消灭的敌人。没有阴影整合，就不可能谈真正的个体化——因为那意味着你仍然在否认自己的一半，无法成为完整之人。

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Shadow | Repressed/denied personality | Dark brother |
| Projection | See in others what deny in self | Shadow mechanism |
| Gold in Shadow | Repressed positive qualities | Not purely evil |
| Dark Brother | Rejected sibling | Needs integration |

#### Core Points

- **Rejected self**: Everything denied, repressed, deemed unacceptable
- **Formed by socialization**: Family/culture creates persona/shadow split
- **Not purely evil**: Contains both darkness and repressed gold
- **Manifests through projection**: See in others what deny in self
- **Integration essential**: No wholeness without shadow work
- **Moral challenge**: Requires courage to admit darkness
- **Dark brother**: Not enemy but rejected sibling seeking recognition

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Shadow: Repressed/denied personality aspects. Formed by socialization (persona/shadow split). Contains darkness AND jung_gold. Manifests through projection. Essential for individuation. "Dark brother" metaphor—sibling not enemy.
- **中文**: 阴影:被压抑/否认的人格面向。由社会化形成(人格面具/阴影分裂)。包含黑暗与金子。通过投射显现。对个体化至关重要。"黑暗兄弟"隐喻——是手足非敌人。

**Narrative Snippets**:
- `[ns_jung_017]` `[trigger: shadow_moral]` `[factor_trigger: jung_shadow AND jung_moral]` `[role: 主干]` The shadow is a moral problem that challenges the whole ego-personality, for no one can become conscious of the shadow without considerable moral effort. → Source Text
- `[ns_jung_018]` `[trigger: shadow_recognition]` `[factor_trigger: jung_shadow AND jung_recognition]` `[role: 主干依赖]` To become conscious of it involves recognizing the dark aspects of the personality as present and real. → Source Text
- `[ns_jung_019]` `[trigger: shadow_resistance]` `[factor_trigger: jung_shadow AND jung_resistance]` `[role: 条件分支]` This act is the essential condition for any kind of self-knowledge, and it therefore meets with considerable resistance. → Source Text
- `[ns_jung_020]` `[trigger: dark_brother]` `[factor_trigger: jung_shadow AND jung_integration]` `[role: 总结]` Shadow is "dark brother"—rejected sibling seeking recognition and integration, not annihilation. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        book_id="collected_works",
        chapter="",
        l1_anchor="cw_v1.0.0_source_text_004_L1",
    )
    version: str = "1.0.0"
