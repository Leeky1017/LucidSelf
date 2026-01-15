"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994613
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
    semantic_id="pt_v1.0.0_card_17__the_star_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card17TheStar(SemanticEntry):
    """
    ### Hope, Healing, Direct Experience Behind Veil

#### Key Term Analysis

| Term | Definition | Sign...
    """
    
    original_text: str = """### Hope, Healing, Direct Experience Behind Veil

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 17 | 1+7=8 Strength | Beyond control |
| Eight-pointed Star | Octogram | Matter/spirit midway |
| Behind Veil | Direct experience | Tower's gift |
| Ibis/Thoth | Creativity source | All arts from pool |

**Source Text**: After the storm, peace. The Tower's release ripped away the veil. Here in the Star we are behind the veil. The pool represents the unconscious; that same water concealed behind the High Priestess's pillars. The water poured onto land indicates energy freed by the Tower directed outwards and inwards; it links unconscious with outer reality.

**English Paraphrase**:

**The Star** = **Hope**, **Healing**, **Direct Unconscious** — naked truth, wholeness after storm.

**Core Symbolism**:
- **Number 17**: 1+7=8 (Strength higher), beyond 7 (Chariot control released)
- **Eight-pointed stars**: Octogram halfway between square/circle (matter/spirit)

**Visual**:
- **Naked maiden** kneeling = vulnerability, openness
- **One foot land, one touching water** (not penetrating) = stirring collective unconscious
- **Five streams**: One returns to pool (archetypes blend back), four to land (outward)
- **Ibis** (Thoth) = creativity source, all arts stem from pool
- **No road back** = dwelling in direct experience

**vs. Temperance**: Controlled→Free, Clothed→Naked, Stiff→Relaxed, Conserving→Pouring freely

**完整中文诠释**:
**星星**=**希望**、**治愈**、**直接无意识**——赤裸真理，风暴后完整。**数字17**：1+7=8（力量更高形式），超越7（战车控制被释放）；**八芒星**：八角星在正方与圆之间（物质/灵性）。**图像**（RWS牌）：**裸体少女**跪姿=脆弱、开放；**单足陆地、单足触水**（非穿透）=搅动集体无意识；**五流**：一回归池（原型混回），四至陆地（向外）；**鹮鹳**（透特）=创造力源头，所有艺术源自池；**无归返路**=居于直接经验中。**vs节制**：控制→自由，着衣→赤裸，僵硬→放松，保存→自由倾倒。风暴（塔）后，平安。塔释放撕裂幕帘。此处星星我们在幕帘后。池代表无意识；那同样水藏于女祭司柱后。倾水至陆地显示塔释放之能量向外与向内引导；它连接无意识与外在现实。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Pollack's Star: Number 17=8 higher. Naked maiden. Five streams. No road back. vs Temperance contrast.
- **中文**: Pollack的星星:数字17=8更高。裸体少女。五流。无归返路。vs节制对比。

**Narrative Snippets**:
- `[ns_78deg_155]` `[trigger: star_major]` `[factor_trigger: tarot_major_star AND tarot_number_17 AND symbol_naked_truth AND symbol_octogram AND state_naked_truth]` `[role: 主干]` The Star represents hope and healing after Tower's storm—direct experience behind the veil, naked truth with no road back. → English Paraphrase
- `[ns_78deg_156]` `[trigger: behind_veil]` `[factor_trigger: state_behind_veil]` `[role: 主干]` Behind the veil now—Tower's gift; direct experience of what High Priestess guarded; dwelling in openness, not just visiting. → English Paraphrase
- `[ns_78deg_157]` `[trigger: aquarius_ruler]` `[factor_trigger: sign_aquarius]` `[role: 主干依赖]` Aquarius rules Star—vision, humanity, air element of clear seeing; the Water-Bearer pouring forth streams of consciousness. → English Paraphrase
- `[ns_78deg_158]` `[trigger: celestial_sun_symbol]` `[factor_trigger: celestial_sun]` `[role: 条件分支]` Eight-pointed star surrounded by seven smaller stars—solar principle illuminating planetary influences; light source of hope. → English Paraphrase
- `[ns_78deg_345]` `[trigger: naked_maiden_star]` `[factor_trigger: tarot_major_star AND symbol_nakedness]` `[role: 条件分支]` Naked maiden kneeling—vulnerability, openness; one foot on land, one touching water stirring collective unconscious; no persona, no armor. → Visual Elements
- `[ns_78deg_346]` `[trigger: five_streams]` `[factor_trigger: tarot_major_star AND symbol_water_streams]` `[role: 条件分支]` Five streams: one returns to pool (archetypes blend back), four to land (outward expression)—energy freed by Tower now directed both inward and outward. → Core Symbolism
- `[ns_78deg_347]` `[trigger: ibis_thoth]` `[factor_trigger: tarot_major_star AND symbol_ibis AND deity_thoth]` `[role: 条件分支]` Ibis (Thoth) in tree—creativity's source; all arts stem from this pool; the bird of wisdom watching over the sacred waters. → Visual Elements
- `[ns_78deg_348]` `[trigger: star_vs_temperance]` `[factor_trigger: tarot_major_star AND tarot_major_temperance AND contrast_star_temperance]` `[role: 总结]` Star vs Temperance contrast: controlled→free, clothed→naked, stiff→relaxed, conserving→pouring freely; the liberation that follows integration. → vs. Temperance
- `[ns_78deg_542]` `[trigger: octagram_matter_spirit]` `[factor_trigger: tarot_major_star AND symbol_octagram]` `[role: 条件分支]` Eight-pointed stars (octogram)—halfway between square (matter) and circle (spirit); the integration of material and spiritual achieved after Tower's destruction. → Core Symbolism
- `[ns_78deg_543]` `[trigger: no_road_back]` `[factor_trigger: tarot_major_star AND state_no_return]` `[role: 条件分支]` No road back—dwelling in direct experience, not visiting; the transformation is complete; having crossed, one cannot uncross; permanent opening. → Source Text

---"""
    normalized_text_zh: str = """"""
    subject: str = "Card 17: The Star"
    factor_refs: list = ['tarot_major_star', 'tarot_number_17', 'state_behind_veil', 'state_naked_truth', 'deity_thoth']
    
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
        l1_anchor="pt_v1.0.0_card_17__the_star_001_L1",
    )
    version: str = "1.0.0"
