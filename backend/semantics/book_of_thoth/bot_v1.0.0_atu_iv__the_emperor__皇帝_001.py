"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044585
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
    semantic_id="bot_v1.0.0_atu_iv__the_emperor__皇帝_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuIvTheEmperor皇帝(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Tzaddi (צ) | Hebrew letter (Crowley swap) | Aries attribution |
| Sulphur (Alchemy) | Active fiery principle | Energizes Empress's Salt |
| Aries | Cardinal fire sign | Warrior-king energy |
| Red Eagle | Alchemical Red Tincture | Solar gold, yang |

**Source Text**:
> "This card is attributed to the letter Tzaddi... it refers to the sign of Aries in the Zodiac. This sign is ruled by Mars, and therein the Sun is exalted. The sign is thus a combination of energy in its most material form with the idea of authority... The Emperor is also one of the more important alchemical cards... His arms and head form an upright triangle; below, crossed legs represent the Cross. This figure is the alchemical symbol of Sulphur... Sulphur is the male fiery energy of the Universe... the swift creative energy, the initiative of all Being." (Book of Thoth, The Emperor)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Tzaddi (צ, traditionally) - though Crowley swapped with Heh in attribution
- **Path**: Connects Chokmah (Wisdom) to Tiphareth (Beauty) - The 15th Path
- **Zodiac**: Aries ♈ (Ram)
- **Planet**: Mars (ruler), Sun (exalted)
- **Alchemical**: Sulphur (active fiery principle)

**English Paraphrase**:
The Emperor is the archetype of **Structure**, **Authority**, and **Ordered Will**, embodying Aries as the warrior-king. He is the masculine complement to the Empress, representing **Sulphur** (active fire) to her Salt (passive matter). Where the Empress creates abundantly, the Emperor **organizes** that creation into structure and law. Enthroned with ram-headed capitals (Aries), he wears armor and holds the orb (dominion) and scepter (command). The **Ram** symbolizes both the wild courage of Aries and the domesticated lamb (when tamed, the fierce becomes docile—"the theory of government"). The **Red Eagle** (his heraldic device) corresponds to the alchemical Red Tincture (solar, gold), paired with the Empress's White Eagle. His authority derives from Chokmah (Wisdom/Word) and is exerted upon Tiphareth (the organized human). The Emperor's power is **sudden, violent, but impermanent**—if sustained too long, it burns and destroys.

**完整中文诠释**:
皇帝（The Emperor）是**结构**、**权威**与**有序意志**的原型，体现了白羊座（Aries）作为战士之王的形象。他是皇后的男性互补者，代表着**硫磺**（Sulphur，主动之火）与她的盐（Salt，被动物质）相对应。皇后丰盛地创造，而皇帝则将这些创造**组织**成结构与法律。他端坐于公羊头装饰的王座上（白羊座），身披盔甲，手持宝球（统治权）与权杖（指挥权）。**公羊**象征着白羊座的野性勇气，也象征着被驯服的羔羊（当被驯化时，凶猛变为温顺——"这就是统治的理论"）。**红鹰**（他的纹章符号）对应着炼金术中的红色药剂（太阳性、金质），与皇后的白鹰配对。他的权威源自Chokmah（智慧/道），并施加于Tiphareth（有组织的人类）。皇帝的力量是**突然的、猛烈的，但不持久的**——如果维持太久，就会燃烧并摧毁一切。

**Core Points**:
- **Ordered Structure**: Imposing form and law upon the Empress's creative abundance
- **Alchemical Sulphur**: Active fiery principle energizing passive Salt (Empress)
- **Paternal Authority**: Generalization of fatherly power, command, and governance
- **Swift but Impermanent**: Sudden forceful action that cannot sustain indefinitely

**Detailed Explanation**:
The Emperor's posture forms the alchemical symbol of Sulphur (triangle over cross), identifying him as the Rajas (active energy) of Hindu philosophy. His power is derived from the paternal principle—symbolized by bees and fleur-de-lys on the card. The two-headed Red Eagle represents the perfected solar work, gold, yang power. Unlike the Empress who represents continuous nurturing, the Emperor represents the initiating spark that must then be tempered. His white light descending from above shows his connection to Chokmah (creative Logos).

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: The Emperor is alchemical Sulphur (active fire) to Empress's Salt. Crowley controversially swapped Tzaddi/Heh attributions. His posture forms the Sulphur symbol (triangle over cross). The Ram symbolizes Aries courage; Red Eagle represents solar gold perfection. Harris depicts martial authority with armor and orb/scepter.
- **中文**: 皇帝是炼金术的硫磺（主动火）对应皇后的盐。Crowley有争议地交换了Tzaddi/Heh归属。他的姿势形成硫磺符号（三角形在十字上）。公羊象征白羊座勇气；红鹰代表太阳金完美。Harris通过盔甲和宝球/权杖描绘武威权威。

**Narrative Snippets**:
- `[ns_thoth_043]` `[trigger: emperor_sulphur_fire]` `[factor_trigger: tarot_emperor AND tarot_sulphur]` `[role: 主干]` The Emperor embodies alchemical Sulphur—active fiery principle energizing the Empress's Salt into ordered creation. → English Paraphrase
- `[ns_thoth_044]` `[trigger: aries_warrior_king]` `[factor_trigger: tarot_aries AND tarot_mars]` `[role: 主干依赖]` Attributed to Aries, ruled by Mars with the Sun exalted, he concentrates warrior‑king energy: decisive, initiating, commanding. → English Paraphrase
- `[ns_thoth_045]` `[trigger: red_eagle_tincture]` `[factor_trigger: tarot_red_eagle AND tarot_tincture]` `[role: 主干依赖]` The Red Eagle is the alchemical Red Tincture—solar gold, perfected yang power, paired with the Empress's White Eagle. → English Paraphrase
- `[ns_thoth_046]` `[trigger: swift_impermanent_power]` `[factor_trigger: tarot_power AND tarot_impermanence]` `[role: 例外处理]` Emperor power is sudden and violent but impermanent—if imposed too long, it burns out and destroys what it sought to order. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU IV: The Emperor (皇帝)"
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_atu_iv__the_emperor__皇帝_001_L1",
    )
    version: str = "1.0.0"
