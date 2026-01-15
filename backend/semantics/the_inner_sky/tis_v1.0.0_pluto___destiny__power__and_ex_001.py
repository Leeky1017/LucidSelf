"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.101007
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
    semantic_id="tis_v1.0.0_pluto___destiny__power__and_ex_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class PlutoDestinyPowerAndEx(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Existential Futility | L...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Existential Futility | Life meaninglessness | What to face |
| Transpersonal Mission | Beyond ego purpose | Goal |
| Death-Rebirth | Transformation cycles | Process |
| Collective Forces | Myths/dreams channeled | Power source |

#### Source Text

"Pluto
Function :
• The realization of one’s destiny
• The recognition of the absurdity of all narrow pursuits
• The development of the capacity to discern truth
Dysfunction :
• Megalomania, grandiosity, violence, preaching, dogmatism, rigidity, dictatorial behavior, hunger for power, a sense of meaninglessness or absurdity, end-justifies-the-means thinking"

"Whirling in the icy black edges of the solar system, minuscule and ominous as a plague virus, tiny Pluto holds the answer. ... From Pluto we actually experience the fact that the sun is nothing special, that the earth is a dust mote, and that we are microbes vainly scratching out a moment’s existence. ... To face Pluto is to face the elemental futility of life. ... To live with that brutal truth we must leap beyond the melodramas of personality. We must identify with something larger, more timeless. In that desperate flight from absurdity there is only one path of escape: we must leave our stamp on eternity. We must change the world."

"Pluto is the planet of vast dreams, of visions, of conquest and transformation. Driven by emptiness, haunted by anonymity, it rips through our safe routines, thrusting into consciousness a sense of mission, a sense of destiny. Mere survival is insufficient. Merely to live is nothing. ... Pluto represents a special wisdom in each of us. A precious gift, it must be found and cultivated, cajoled out of hiding. ... When we speak from our Pluto consciousness, people listen as if it were the voice in the burning bush."

#### English Paraphrase (Primary Language)

**Pluto** represents the **destiny and existential transformation function**—the part of the psyche that confronts the apparent futility of life and demands that we find or create meaning large enough to stand against it. It shrinks our usual self‑importance by placing us at the icy edge of the solar system, where sun, earth, and personal dramas look insignificant. Faced with that perspective, we must either collapse into nihilism or leap beyond personality into a transpersonal sense of mission.

Positively, Pluto calls us to realize a deeper destiny, to recognize the absurdity of narrow, ego‑driven pursuits, and to cultivate the capacity to discern truth that matters. It channels vast, collective forces—myths, dreams, fears—through individuals, sometimes giving them world‑shaping influence when they voice what a group unconsciously feels. At a personal level, Pluto erupts as intense transformations, death‑and‑rebirth processes, and a growing sense that we carry a particular kind of wisdom or power that the world needs.

On the shadow side, Pluto can express as megalomania, abuse of power, ruthless "ends justify the means" thinking, and destructive obsession. It can also manifest as despair and meaninglessness when we feel the weight of cosmic absurdity but refuse the work of transformation. Wherever Pluto lies in the birthchart, Forrest suggests, we meet themes of power, depth, mortality, and destiny—places where we are tempted either to manipulate and dominate or to surrender to a more impersonal, transpersonal calling.

#### Complete Chinese Interpretation

**冥王星**代表**命运与存在性转化功能**——那一部分直面生命表面虚无、却逼迫我们寻找或创造足够宏大的意义的心智力量。它把我们带到太阳系冰冷边缘，让太阳、地球与日常戏码在视角中缩至渺小，从而动摇平常的自我重要感。在这种视角下，我们要么坠入虚无主义，要么跃出人格层面的肥皂剧，进入某种跨个体的使命感。

在正向层面，冥王星召唤我们**实现更深的命运**，看穿狭隘自我追逐的荒诞，并培养**辨别真正重要之真相的能力**。它常常通过个人来传导巨大的集体力量——民族的梦魇、愿景与渴望——因此当某个人说出了一个群体心底的声音时，便可能获得改变世界的影响力。在个体层面，冥王星表现为强烈的转化过程：如同一次次「死亡与重生」，以及一种越来越清晰的感觉：自己承载着某种世界需要的智慧或力量。

在阴影层面，冥王星可能化身为**妄自尊大与权力滥用**：把「目的」绝对化，而无视手段代价；被个人虚荣与恐惧驱动，走向暴力、极端与狂热布道。另一种阴影则是**彻底的无意义感**：当我们感到宇宙荒诞，却拒绝做任何内在转化工作时，冥王星的目光只会让现实显得更加空洞。命盘上冥王星所处之处，是权力、深度、死亡与命运主题反复出现的领域：在那里，我们要么被诱惑去操控与支配，要么学会把自己交托给一个更不依附个人虚荣的、更大的召唤。

#### Core Points

- Pluto = destiny, power, and existential transformation function.
- Confronts the futility of life and demands a leap into transpersonal meaning.
- Positive: sense of mission, capacity to discern deep truth, willingness to transform.
- Shadow: megalomania, abuse of power, nihilism, "ends justify the means".
- Chart position marks arenas where power, death‑rebirth, and collective forces concentrate.

#### Narrative Snippets

- `[ns_innersky_pluto_001]` `[trigger: planet_pluto]` `[factor_trigger: planet_pluto AND transformation_function]` `[role: 主干]` Pluto represents destiny, power, and existential transformation. It takes us to the icy edge of the solar system where sun and earth shrink to insignificance, confronting us with life's apparent futility. → The Inner Sky Ch.6 #Pluto
- `[ns_innersky_pluto_002]` `[trigger: planet_pluto AND astro_function]` `[factor_trigger: astro_planet_pluto]` `[role: 主干依赖]` From this precipice, we either fall into nihilism or make a leap into transpersonal meaning. Pluto demands we realize a deeper destiny, see through narrow ego pursuits, and discern truth that truly matters. → The Inner Sky Ch.6 #Pluto
- `[ns_innersky_pluto_003]` `[trigger: planet_pluto AND astro_shadow]` `[factor_trigger: astro_planet_pluto AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: megalomania (inflated sense of mission), abuse of power (ruthless "ends justify means"), nihilism and despair (refuse transformative work), destructive obsession. → The Inner Sky Ch.6 #Pluto
- `[ns_innersky_pluto_004]` `[trigger: planet_pluto AND astro_chart]` `[factor_trigger: astro_planet_pluto]` `[role: 总结]` Chart position marks arenas where power, death-rebirth, and collective forces concentrate—where we are tempted to manipulate and dominate, or to surrender to a transpersonal calling. → The Inner Sky Ch.6 #Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto – Destiny, Power, and Existential Transformation"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_pluto___destiny__power__and_ex_001_L1",
    )
    version: str = "1.0.0"
