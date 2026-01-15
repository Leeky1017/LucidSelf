"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994447
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
    semantic_id="pt_v1.0.0_card_6__the_lovers_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card6TheLovers(SemanticEntry):
    """
    ### Union, Choice, and the Reconciliation of Opposites

#### Key Term Analysis

| Term | Definition ...
    """
    
    original_text: str = """### Union, Choice, and the Reconciliation of Opposites

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 6 | Harmony, hexagram | Union of triangles |
| Super-conscious | Angel Raphael | Product of union |
| Passion Liberates | Woman→angel | Not reason controls |
| Sexual Path | Surrender ego | Spiritual union |

**Source Text**: Notice that while the man looks at the woman the woman looks at the angel. If the male is indeed reason, then rationality can only reach beyond its limits through the medium of passion. Our tradition has set the body and the rational mind at odds with each other. The Tarot teaches us that we must unite them and that it is not the controlling power of reason that raises the senses to a higher level, but, rather, the other way around.

**English Paraphrase**:

**The Lovers** = **Union of Opposites**, **Transcendence through Love**, **Conscious Choice** — sexuality as path to super-consciousness.

**Core Symbolism**:
- **Number 6**: Harmony, balance, union of triangles (2×3, perfect balance)
- **Hexagram**: Two triangles interlaced (fire + water, male + female united)

**Visual Elements** (Rider-Waite-Smith):
- **Naked man and woman** (Adam & Eve) = vulnerability, innocence, pre-Fall state
- **Angel Raphael** above = super-conscious, divine blessing, higher self
- **Mountain** between them = single peak, shared goal, unity through ascent
- **Tree of Knowledge** behind woman (with serpent) = consciousness, choice, wisdom
- **Tree of Life** behind man (12 flames) = immortality, divine connection
- **Sun** above angel = enlightenment, consciousness, divine light

**The Transformation from Earlier Decks**:

**Traditional version**: Young man between two women (light/dark)
- **Choice**: Virtue vs. Vice, respectability vs. passion, outer path vs. inner path
- **Adolescent decision**: Breaking from parental expectations

**Waite-Smith version**: Man and woman unified under angel
- **Mature love**: Not choice but union, not conflict but harmony
- **Genesis reversed**: Sexuality as path to paradise, not expulsion from it

**Psychological Meaning**:

**Super-Conscious as Product of Union**:

Paul Foster Case: Angel Raphael = **super-conscious**

**Key insight**: Super-conscious is not separate "third level" above conscious/unconscious, but **product of their union**.

**Triune Mind**:
1. **Conscious** (man, reason, ego)
2. **Unconscious** (woman, passion, instinct)
3. **Super-conscious** (angel) = **conscious + unconscious unified**

**The Pathway**:
- Goes **through the unconscious** (where true life energy resides)
- Super-conscious = **energy of unconscious transformed to higher state**
- Consciousness gives energy **form, direction, meaning**

**The Visual Dynamic**:
- **Man looks at woman** = reason can only transcend through passion
- **Woman looks at angel** = passion connects directly to super-conscious
- **Lesson**: Not reason controlling passion, but **passion liberating reason**

**Sexual Union as Spiritual Path**:

**Surrender of Ego**:
- Most people **bound within ego-masks**
- **Sexual passion allows momentary transcendence** of isolation
- Those who cannot release ego **misuse sex** (becomes power game, never satisfies)
- Rejection of body's desire to release = **depression** (angel denied)

**But passion alone insufficient**:
- Needs **guidance by reason** (direction, meaning)
- Without guidance, thrown from experience to experience without growth
- Union requires **both**: reason freed by passion, passion shaped by reason

**Hermaphroditic Unity**:

**Occult teaching**: All humanity (even Deity) originally **hermaphroditic**
- Male/female separated as consequence of Fall
- Each person = **only half**, seeks unity through love
- Goal of Major Arcana: **Unite male/female principles within self**
- World dancer = hermaphrodite (integration achieved)

**Plato's variation**: Three original types (male-female, male-male, female-female)
- Zeus split all with thunderbolt
- Each seeks "other half"
- **Insight**: Any two lovers can evoke the angel (not limited to heterosexual)
- **What matters**: Reality of union, not social roles

**Narrative Snippets**:
- `[ns_78deg_138]` `[trigger: lovers_major]` `[factor_trigger: tarot_major_lovers AND tarot_number_6 AND symbol_twin_trees]` `[role: 主干]` The Lovers represents union of opposites—transcendence achieved through passion liberating reason; the sacred marriage of conscious and unconscious. → English Paraphrase
- `[ns_78deg_139]` `[trigger: gemini_ruler]` `[factor_trigger: sign_gemini]` `[role: 主干依赖]` Gemini rules the Lovers—twins, communication, choice, duality; the air element that connects and chooses. → English Paraphrase
- `[ns_78deg_140]` `[trigger: superconscious_state]` `[factor_trigger: state_superconscious]` `[role: 主干]` Super-conscious (angel) is not separate third layer but product of conscious/unconscious union—emerges when masculine and feminine unite. → English Paraphrase
- `[ns_78deg_141]` `[trigger: angel_raphael]` `[factor_trigger: symbol_angel_raphael]` `[role: 条件分支]` Angel Raphael above the lovers = super-conscious mind; the higher self that emerges from genuine union; divine blessing on human love. → English Paraphrase
- `[ns_78deg_142]` `[trigger: passion_liberates]` `[factor_trigger: principle_passion_liberates]` `[role: 主干]` Passion liberates reason—man looks at woman (reason through passion), woman looks at angel (passion to divine); not control but liberation. → English Paraphrase
- `[ns_78deg_143]` `[trigger: hermaphrodite_archetype]` `[factor_trigger: archetype_hermaphrodite AND archetype_hieros_gamos]` `[role: 条件分支]` Original hermaphrodite split by Zeus/lightning—each seeks other half; any two lovers can evoke the angel; healing the primordial separation. → English Paraphrase
- `[ns_78deg_144]` `[trigger: conscious_unconscious_polarity]` `[factor_trigger: polarity_conscious_unconscious]` `[role: 总结]` Conscious (man, reason) and unconscious (woman, passion) union produces super-conscious (angel)—the tripartite mind of Tarot psychology. → English Paraphrase
- `[ns_78deg_477]` `[trigger: sexual_path]` `[factor_trigger: tarot_major_lovers AND principle_sexuality]` `[role: 条件分支]` Sexual passion allows momentary transcendence of ego isolation—those who cannot release ego misuse sex (becomes power game, never satisfies); body's desire to release denied becomes depression. → Sexual Path
- `[ns_78deg_548]` `[trigger: man_looks_woman]` `[factor_trigger: tarot_major_lovers AND symbol_gaze_direction]` `[role: 条件分支]` Man looks at woman, woman looks at angel—reason can only transcend through passion's medium; passion connects directly to divine; the pathway runs through feeling, not intellect. → Visual Dynamic
- `[ns_78deg_549]` `[trigger: trees_knowledge_life]` `[factor_trigger: tarot_major_lovers AND symbol_dual_trees]` `[role: 条件分支]` Tree of Knowledge (behind woman, with serpent) = consciousness, wisdom; Tree of Life (behind man, 12 flames) = immortality; together they form complete human potential—both trees needed. → Visual Elements

**完整中文诠释**:
**恋人**=**对立统一**、**通过爱的超越**、**觉知选择**——性作为通往超意识之路。**数字6**：和谐、平衡、三角形结合（2×3，完美平衡）；六芒星：两个三角形交织（火+水，男性+女性统一）。**图像元素**（RWS牌）：**裸体男女**（亚当与夏娃）=脆弱、纯真、堕落前状态；上方**天使拉斐尔**=超意识、神圣祝福、更高自我；他们之间的**山峰**=单一顶点、共享目标、通过攀升的统一；女人身后**知识之树**（带蛇）=意识、选择、智慧；男人身后**生命之树**（12火焰）=不朽、神圣连接；天使上方**太阳**=启蒙、意识、神圣之光。**从早期牌组的转化**：**传统版本**：年轻人站在两女人之间（光明/黑暗）——**选择**：美德vs邪恶、体面vs激情、外在之路vs内在之路；青春期决定：脱离父母期待。**Waite-Smith版本**：男女在天使下统一——**成熟之爱**：非选择而是统一，非冲突而是和谐；**逆转创世记**：性作为通往天堂之路，非从中驱逐。**心理意义**："超意识作为统一产物"：Paul Foster Case：天使拉斐尔=**超意识**。**关键洞见**：超意识不是意识/无意识之上独立的"第三层"，而是**它们统一的产物**。**三位一体心智**：1.**意识**（男人、理性、自我）；2.**无意识**（女人、激情、本能）；3.**超意识**（天使）=**意识+无意识统一**。**路径**：**通过无意识**（真正生命能量所在之处）；超意识=**无意识能量转化至更高状态**；意识给予能量**形式、方向、意义**。**视觉动态**：**男人看女人**=理性只能通过激情超越；**女人看天使**=激情直接连接超意识；**教训**：不是理性控制激情，而是**激情解放理性**。**性统一作为灵性之路**："自我臣服"：多数人**束缚于自我面具**；**性激情允许短暂超越**隔离；那些无法释放自我者**误用性**（成为权力游戏，永不满足）；拒绝身体释放欲望=**抑郁**（天使被拒）。但激情单独不足：需要**理性指引**（方向、意义）；无指引，被从经验抛向经验无成长；统一需要**两者**：被激情解放的理性，被理性塑形的激情。**雌雄同体统一**："神秘学教导"：全人类（甚至神性）原初**雌雄同体**；男/女分离为堕落后果；每人=**仅半个**，通过爱寻求统一；大阿卡纳目标：**统一自我内在男性/女性原则**；世界牌舞者=雌雄同体（达成整合）。**柏拉图变体**：三种原初类型（男-女、男-男、女-女）；宙斯用雷电劈开所有；每人寻求"另一半"；**洞见**：任何两个恋人都能唤起天使（不限于异性恋）；**重要的是**：统一的实在性，非社会角色统一的现实。"""
    normalized_text_zh: str = """"""
    subject: str = "Card 6: The Lovers"
    factor_refs: list = ['tarot_major_lovers', 'tarot_number_6', 'state_superconscious', 'archetype_hieros_gamos', 'archetype_hermaphrodite', 'principle_passion_liberates']
    
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
        l1_anchor="pt_v1.0.0_card_6__the_lovers_001_L1",
    )
    version: str = "1.0.0"
