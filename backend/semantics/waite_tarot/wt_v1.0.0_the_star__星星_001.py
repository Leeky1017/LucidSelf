"""
Auto-generated semantic module for waite_tarot
Generated at: 2025-12-05T13:30:19.952770
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
    semantic_id="wt_v1.0.0_the_star__星星_001",
    book_id="waite_tarot",
    engine_id="tarot"
)
class TheStar星星(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Great Mother Binah | Supernal Understanding | Communicates below |
| Waters of Life Freely | Gifts of Spirit | Poured freely |
| Truth Unveiled | Naked figure | Glorious beauty |
| Eight-Rayed Star | Flamboyante | Masonic symbol |

**Number**: XVII  
**Hebrew Letter**: Tzaddi (צ)  
**Qabalistic Path**: Netzach to Yesod (Victory to Foundation)  
**Element/Planet**: Aquarius / Saturn/Uranus

**Source Text**:
> "A great, radiant star of eight rays, surrounded by seven lesser stars--also of eight rays. The female figure in the foreground is entirely naked. Her left knee is on the land and her right foot upon the water. She pours Water of Life from two great ewers, irrigating sea and land. Behind her is rising ground and on the right a shrub or tree, whereon a bird alights. The figure expresses eternal youth and beauty. The star is l’étoile flamboyante, which appears in Masonic symbolism, but has been confused therein. That which the figure communicates to the living scene is the substance of the heavens and the elements. It has been said truly that the mottoes of this card are 'Waters of Life freely' and 'Gifts of the Spirit.'

> The summary of several tawdry explanations says that it is a card of hope. On other planes it has been certified as immortality and interior light. For the majority of prepared minds, the figure will appear as the type of Truth unveiled, glorious in undying beauty, pouring on the waters of the soul some part and measure of her priceless possession. But she is in reality the Great Mother in the Kabalistic Sephira Binah, which is supernal Understanding, who communicates to the Sephiroth that are below in the measure that they can receive her influx."

**English Paraphrase**:
**Truth Unveiled & Binah the Great Mother** – **8-rayed star** (l’étoile flamboyante) + **seven 8-rayed stars**. **Naked female** (unveiled truth) pours **Water of Life from two ewers**, **irrigating sea and land** – unifying elements. Mottoes: **"Waters of Life freely"** + **"Gifts of the Spirit"**.

Waite rejects shallow **"tawdry explanations"** (mere hope). Higher: **immortality, interior light**. For prepared minds: **"Truth unveiled... pouring on waters of the soul"**.

Esoteric core: **"She is in reality the Great Mother in Binah (supernal Understanding), who communicates to Sephiroth below in the measure they can receive her influx."**

#### Core Points

- **Great Mother Binah**: She is in reality the Great Mother in the Kabalistic Sephira Binah—supernal Understanding.
- **Waters of Life Freely**: The mottoes are "Waters of Life freely" and "Gifts of the Spirit"—grace poured without cost.
- **Truth Unveiled**: The figure will appear as the type of Truth unveiled, glorious in undying beauty.
- **Measured Influx**: She communicates to the Sephiroth that are below in the measure that they can receive her influx.
- **L’étoile Flamboyante**: The 8-rayed star appears in Masonic symbolism but has been confused therein.

#### Detailed Explanation

A great, radiant star of eight rays (l’étoile flamboyante) + seven lesser stars. The naked female figure pours Water of Life from two great ewers, irrigating sea and land—unifying elements. Mottoes: "Waters of Life freely" + "Gifts of the Spirit."

Waite rejects shallow "tawdry explanations" (mere hope). Higher meanings: immortality, interior light. For prepared minds: "Truth unveiled... pouring on the waters of the soul some part and measure of her priceless possession."

Esoteric core: "She is in reality the Great Mother in Binah (supernal Understanding), who communicates to Sephiroth below in the measure they can receive her influx"—revelation according to capacity.

**Narrative Snippets**:
- `[ns_waite_067]` `[trigger: binah_mother]` `[factor_trigger: tarot_star]` `[role: 主干]` She is in reality the Great Mother in the Kabalistic Sephira Binah, which is supernal Understanding. → Source Text
- `[ns_waite_068]` `[trigger: waters_freely]` `[factor_trigger: tarot_star AND tarot_grace]` `[role: 主干依赖]` The mottoes of this card are "Waters of Life freely" and "Gifts of the Spirit"—grace poured without cost. → Source Text
- `[ns_waite_069]` `[trigger: measured_influx]` `[factor_trigger: tarot_star AND tarot_sephiroth]` `[role: 主干依赖]` She communicates to the Sephiroth that are below in the measure that they can receive her influx. → Source Text
- `[ns_waite_070]` `[trigger: truth_unveiled]` `[factor_trigger: tarot_star AND tarot_truth]` `[role: 总结]` For the majority of prepared minds, the figure will appear as the type of Truth unveiled, glorious in undying beauty. → Source Text

**Chinese Explanation**:
**星星（真理揭幕与Binah伟大母亲）**——**八芒星**（炽烈星）+**七小星**。**裸女**（揭幕真理）倾倒**生命之水**，**灌溉海陆**——统一元素。座右铭：**"生命之水白白"**+**"圣灵恩赐"**。

韦特拒绝肤浅**"华而不实解释"**（仅希望）。更高：**不朽、内在之光**。对准备好心智：**"真理揭幕...向灵魂之水倾倒"**。

深奥核心：**"她实际是Binah（至高理解）伟大母亲，按可接受尺度向下方Sephiroth传达其流注"**。

**In Readings**: Hope, renewal, but deeper: Binah's Understanding, Waters freely, graduated revelation.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Waite rejects "tawdry explanations" (mere hope). True meaning: "Great Mother in Binah (supernal Understanding), communicating to Sephiroth below in measure they can receive." Truth unveiled. "Waters of Life freely" + "Gifts of the Spirit."
- **中文**: 韦特拒绝“华而不实解释”(仅希望)。真正含义：“Binah伟大母亲(至高理解)，按可接受尺度向下方Sephiroth传达”。真理揭幕。“生命之水白白”+“圣灵恩赐”。"""
    normalized_text_zh: str = """"""
    subject: str = "The Star (星星)"
    factor_refs: list = ['tarot_star', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tarot_star', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'source_ref', 'rel_waite_049', 'tarot_star', 'downward', 'rel_waite_050', 'tarot_star', 'regulated', 'rel_waite_051', 'tarot_star', 'generous', 'evi_waite_033', 'tarot_star', 'rule_waite_star_binah', 'evi_waite_034', 'tarot_star', 'rule_waite_star_measure', 'concept_supernal_understanding', 'yin_nurture', 'anima_jung', 'concept_graduated_revelation', 'house_11', 'readiness_principle']
    
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
        book_id="waite_tarot",
        chapter="",
        l1_anchor="wt_v1.0.0_the_star__星星_001_L1",
    )
    version: str = "1.0.0"
