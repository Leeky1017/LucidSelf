"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994414
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
    semantic_id="pt_v1.0.0_card_4__the_emperor_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card4TheEmperor(SemanticEntry):
    """
    ### Authority, Structure, and Patriarchal Order

#### Key Term Analysis

| Term | Definition | Signi...
    """
    
    original_text: str = """### Authority, Structure, and Patriarchal Order

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 4 | Stability, structure | Material reality |
| Father Archetype | Remote authority | Judge/punisher |
| Society Construct | Human overlay | vs Nature |
| Controlled River | Channeled passion | Order vs vitality |

**Source Text**: For each child its parents are archetypes. Not just mother and father, but Mother and Father. The Father, especially in traditional times when sex roles were stricter, remained more remote, and therefore a figure of severity. It was the father who bore the authority and thus became the judge, the father who punished and the father who taught us the rules of society and then demanded obedience. To the child the father is in many ways indistinguishable from society as a whole, just as the mother is nature itself.

**English Paraphrase**:

**The Emperor** = **Authority**, **Society**, **Structure** — the patriarchal principle of order, law, and civilization.

**Core Symbolism**:
- **Number 4**: Stability, structure, material reality, completion
  - Four elements, four directions, four seasons
  - Square = solid foundation (vs. triangle's dynamism)
  - **Earthly manifestation** (after 1-2-3's creative process)

**Visual Elements** (Rider-Waite-Smith):
- **Armored figure** on stone throne = protection, defense, solidity
- **Red robe** under armor = passion controlled by discipline
- **Rams' heads** on throne = Aries (cardinal fire, initiative, leadership, Mars rulership)
- **Ankh scepter** = Egyptian symbol of life (authority over life/death)
- **Orb** in left hand = world dominion, sovereignty
- **Crown** = temporal power (vs. spiritual power)
- **Barren rocky mountains** behind = harsh, unforgiving landscape (vs. Empress's lush nature)
- **Small stream** visible = remnant of Empress's river, now controlled/channeled
- **Rigid posture** = immobility, fixed authority

**Psychological Meaning**:

**Father as Archetype**:
- **Remote figure** (vs. mother's intimacy) = severity, judgment
- **Authority bearer**: Sets rules, demands obedience, punishes transgressions
- **Society's representative**: Father indistinguishable from social order itself
- **Painful maturity moment**: Discovering parents' limited humanity (they're not archetypal gods)

**Freudian Development** (male psyche):
- **Infant psyche**: Demands constant satisfaction, desires mother's physical pleasure
- **Father's intervention**: Represents **reality principle** (vs. pleasure principle)
- Child must **internalize father's rules** (superego formation)
- **Oedipus complex**: Must renounce mother, identify with father, accept society's laws
- Failure = neurosis; success = **adult ego** capable of functioning in civilization

**Society as Human Construct**:

The "Worldly Sequence" triad (cards 3-5):
1. **Empress**: Nature (underlying reality)
2. **Emperor**: Society (human construct)
3. **Hierophant**: Religion/Education (human construct)

**Egyptian trinity**: Female supreme + two male consorts
- Nature (Empress) = primary reality
- Society (Emperor) and Church (Hierophant) = **constructs overlaid on nature**

**The Necessity of Structure**:

Despite the Emperor's harshness, **civilization requires order**:
- Without rules, **chaos** (return to pre-civilized state)
- **Authority enables**: Security, cooperation, large-scale organization
- **Laws protect** individuals from stronger individuals' tyranny
- **Stability allows**: Art, science, philosophy, spiritual development

**But also warns**:
- **Rigidity suppresses** natural instincts (alienation from Empress's vitality)
- **Authoritarian excess**: Tyranny, oppression, patriarchal domination
- **Control vs. life**: Barren mountains vs. lush forest (what's lost when nature is tamed)

**The Controlled River**:
- Empress's flowing river now **channeled** into small stream
- **Civilization** = harnessing nature's wildness for human purposes
- Necessary for survival, but **at cost of spontaneity**

**Complementarity with Empress**:
- Empress = **thesis** (nature, emotion, spontaneity)
- Emperor = **antithesis** (culture, reason, control)
- Neither complete without the other
- **Integration** (card 21, The World) holds both

**Narrative Snippets**:
- `[ns_78deg_093]` `[trigger: emperor_major]` `[factor_trigger: tarot_major_emperor AND tarot_number_4 AND psych_reality_principle AND symbol_stone_throne AND symbol_barren_mountains]` `[role: 主干]` The Emperor represents authority, society, structure—the patriarchal principle of order, law, and civilization; the Father archetype who is indistinguishable from society itself. → English Paraphrase
- `[ns_78deg_094]` `[trigger: father_archetype]` `[factor_trigger: archetype_father]` `[role: 主干]` Father as archetype: remote figure of severity and judgment; authority bearer who sets rules, demands obedience, and punishes transgressions. → Source Text
- `[ns_78deg_095]` `[trigger: superego_formation]` `[factor_trigger: psych_superego]` `[role: 主干依赖]` Child must internalize father's rules (superego formation)—Oedipal resolution creating adult ego capable of functioning in civilization. → English Paraphrase
- `[ns_78deg_096]` `[trigger: mars_aries_ruler]` `[factor_trigger: planet_mars]` `[role: 主干依赖]` Mars/Aries rules the Emperor—rams' heads on throne symbolizing cardinal fire, initiative, leadership, active masculine force. → English Paraphrase
- `[ns_78deg_097]` `[trigger: sign_aries]` `[factor_trigger: sign_aries]` `[role: 主干依赖]` Aries attribution: rams' heads on Emperor's throne represent cardinal fire sign—initiative, leadership, the active masculine force. → English Paraphrase
- `[ns_78deg_098]` `[trigger: controlled_river]` `[factor_trigger: symbol_controlled_river]` `[role: 条件分支]` Small stream visible behind Emperor—Empress's flowing river now channeled and controlled; civilization harnessing nature's wildness. → English Paraphrase
- `[ns_78deg_099]` `[trigger: worldly_sequence]` `[factor_trigger: framework_worldly_sequence]` `[role: 条件分支]` Worldly Sequence triad (cards 3-5): Empress (Nature), Emperor (Society), Hierophant (Religion)—nature as primary reality, others as human constructs. → English Paraphrase
- `[ns_78deg_392]` `[trigger: barren_mountains]` `[factor_trigger: tarot_major_emperor AND symbol_barren_landscape]` `[role: 条件分支]` Barren rocky mountains behind Emperor—harsh, unforgiving landscape vs. Empress's lush nature; what's lost when spontaneity is tamed. → Visual Elements
- `[ns_78deg_393]` `[trigger: emperor_empress_polarity]` `[factor_trigger: tarot_major_emperor AND tarot_major_empress]` `[role: 总结]` Emperor vs Empress polarity: thesis (nature/emotion/spontaneity) vs antithesis (culture/reason/control); neither complete without other; integration in World. → Complementarity
- `[ns_78deg_554]` `[trigger: ankh_scepter]` `[factor_trigger: tarot_major_emperor AND symbol_ankh]` `[role: 条件分支]` Ankh scepter in hand—Egyptian symbol of life; authority over life and death; the power to give or withhold; temporal rule claiming eternal sanction. → Visual Elements

**完整中文诠释**:
**皇帝**=**权威**、**社会**、**结构**——秩序、法律和文明的父权原则。**数字4**：稳定、结构、物质现实、完成——四元素、四方位、四季节；正方形=坚固基础（vs三角形的动态性）；**尘世显化**（在1-2-3的创造过程之后）。**图像元素**（RWS牌）：石座上的**铠甲人物**=保护、防御、坚固；铠甲下**红袍**=激情受纪律控制；座上**白羊头**=白羊座（开创火象、主动性、领导力、火星统治）；**安卡权杖**=埃及生命符号（对生死的权威）；左手**宝珠**=世界统治、主权；**王冠**=世俗权力（vs灵性权力）；背后**荒芜岩石山**=严酷、无情景观（vs皇后茂密自然）；可见**小溪流**=皇后河流的残留，现被控制/导引；**僵硬姿态**=不动性、固定权威。**心理意义**："父亲作为原型"：**遥远人物**（vs母亲亲密）=严厉、裁判；**权威承载者**：设立规则、要求服从、惩罚违背；**社会代表**：父亲与社会秩序本身无法区分；**痛苦成熟时刻**：发现父母有限的人性（他们非原型神祗）。**弗洛伊德发展**（男性心理）：**婴儿心理**：要求持续满足，渴望母亲身体愉悦；**父亲介入**：代表**现实原则**（vs快乐原则）；孩子必须**内化父亲规则**（超我形成）；**俄狄浦斯情结**：必须放弃母亲，认同父亲，接受社会法律；失败=神经症；成功=能在文明中运作的**成人自我**。**社会为人类构造**："世俗序列"三位一体（牌3-5）：1.**皇后**：自然（底层现实）；2.**皇帝**：社会（人类构造）；3.**教皇**：宗教/教育（人类构造）。**埃及三位一体**：女性至高+两个男性配偶——自然（皇后）=首要现实；社会（皇帝）和教会（教皇）=**叠加于自然的构造**。**结构的必要性**：尽管皇帝严酷，**文明需要秩序**：无规则，**混乱**（返回前文明状态）；**权威使能**：安全、合作、大规模组织；**法律保护**个体免于更强个体的暴政；**稳定允许**：艺术、科学、哲学、灵性发展。但也警告：**僵化压抑**自然本能（从皇后活力异化）；**独裁过度**：暴政、压迫、父权统治；**控制vs生命**：荒山vs茂密森林（当自然被驯服时失去什么）。**受控河流**：皇后流淌的河流现**导引**成小溪；**文明**=为人类目的驾驭自然野性；生存必需，但**以自发性为代价**。**与皇后互补**：皇后=**正题**（自然、情感、自发性）；皇帝=**反题**（文化、理性、控制）；无对方皆不完整；**整合**（牌21，世界）持有两者。"""
    normalized_text_zh: str = """"""
    subject: str = "Card 4: The Emperor"
    factor_refs: list = ['tarot_major_emperor', 'tarot_number_4', 'archetype_father', 'psych_reality_principle', 'psych_superego', 'symbol_controlled_river', 'framework_worldly_sequence']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_card_4__the_emperor_001_L1",
    )
    version: str = "1.0.0"
