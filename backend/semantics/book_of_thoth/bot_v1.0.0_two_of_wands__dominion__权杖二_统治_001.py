"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088781
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
    semantic_id="bot_v1.0.0_two_of_wands__dominion__权杖二_统治_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TwoOfWandsDominion权杖二统治(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chokmah in Fire | Wisdom in Fire | Exalted Will |
| Mars in Aries | Planet in home sign | Maximum initiative |
| Dorje | Tibetan thunderbolt | Destroy to create |
| Pure Will | Objectless intention | Thelemic ideal |

**Title**: Lord of Dominion (统治之主)
**Qabalistic**: Chokmah in Fire (火中之智慧)
**Astrological**: Mars in Aries (火星入白羊座)

**Source Text**:
> "This card, pertaining to Chokmah in the suit of Fire, represents the Will in its most exalted form. It is an ideal Will, independent of any given object. ... The background of this card shows the power of the planet Mars in his own sign Aries... initiating a Current of Force. The pictorial representation is two Dorjes crossed. The Dorje is the Tibetan symbol of the thunderbolt... Destruction may be regarded as the first step in the creative process."

**English Paraphrase**:
**Exalted Will** - Corresponding to Chokmah (Wisdom/Force) in Fire, this card symbolizes **Will in its highest, most ideal form**—pure purpose independent of a specific target. Ruled by **Mars in Aries** (its home sign), it represents energy initiating a current of force. The symbol is two crossed **Dorjes** (Tibetan thunderbolts), representing celestial power in its destructive/creative aspect. Destruction here is the necessary first step of creation ("The virgin ovum must be broken").

**Core**: **Pure Will** - Authority, boldness, and the energy to initiate. Will unassuaged of purpose.

**Chinese Explanation**:
**权杖二（统治）**对应火元素中的Chokmah（智慧），代表**最高形式的意志**。这是一种理想的意志，独立于任何具体对象。背景显示**火星在白羊座**（其本位星座）的力量，代表启动一股力量流。图像是两个交叉的**金刚杵**（Dorje，西藏雷电符号），象征天界力量，兼具破坏与创造性。在此，破坏被视为创造过程的第一步（如打破卵子以受精）。它代表纯粹的、无所畏惧的启动力量。

**In Readings**: Authority, boldness, taking initiative, exerting will, conquering, destruction as creation, fierce independence.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Two of Wands shows "pure Will unassuaged of purpose" (Thelemic formula). Mars in Aries gives maximum aggressive initiative. Crossed Dorjes symbolize destruction as creation's first step. Chokmah provides ideal Will.
- **中文**: Crowley的权杖二展示"纯粹意志不受目的约束"（泰勒玛公式）。火星入白羊赋予最大攻击性主动。交叉金刚杵象征破坏作为创造的第一步。Chokmah提供理想意志。

**Narrative Snippets**:
- `[ns_thoth_wands_004]` `[trigger: two_wands_dominion]` `[factor_trigger: thoth_wands_two]` `[role: 主干]` Two of Wands = Lord of Dominion—Will in most exalted form; pure, ideal, independent of any object. → Core
- `[ns_thoth_wands_005]` `[trigger: crossed_dorjes]` `[factor_trigger: thoth_wands_two AND symbol_dorje]` `[role: 条件分支]` Two crossed Dorjes (Tibetan thunderbolts)—celestial power; destruction as first step of creation. → Visual
- `[ns_thoth_wands_006]` `[trigger: mars_aries_home]` `[factor_trigger: thoth_wands_two AND planet_mars_aries]` `[role: 条件分支]` Mars in Aries (home sign)—initiating current of force; maximum aggressive initiative. → Astrological"""
    normalized_text_zh: str = """"""
    subject: str = "Two of Wands: Dominion (权杖二：统治)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_two_001', 'tarot_exalted_will', 'rel_wands_two_002', 'tarot_creation_first_step', 'l1_anchor', 'confidence', 'evi_wands_two_001', 'evi_wands_two_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_two_001', 'tarot_wands_two', 'astro_mars_aries']
    
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
        l1_anchor="bot_v1.0.0_two_of_wands__dominion__权杖二_统治_001_L1",
    )
    version: str = "1.0.0"
