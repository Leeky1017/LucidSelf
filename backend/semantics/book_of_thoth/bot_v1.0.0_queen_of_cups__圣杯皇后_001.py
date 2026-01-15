"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027441
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
    semantic_id="bot_v1.0.0_queen_of_cups__圣杯皇后_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class QueenOfCups圣杯皇后(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Water of Water | Pure receptivity | Perfect reflection |
| Still Water Throne | Calm surface | Tranquil seat |
| Lotus of Isis | Great Mother emblem | Spiritual fertility |
| Mirror Nature | Reflects observer | Hard to grasp essence |

**Title**: Queen of the Thrones of the Waters (水之宝座的皇后)
**Elemental**: The Watery part of Water (水中之水)
**Zodiac**: 21° Gemini to 20° Cancer (双子座21度至巨蟹座20度)

**Source Text**:
> "The Queen of Cups represents the watery part of Water, its power of reception and reflection. In the Zodiac it rules from the 21st degree of Gemini to the 20th degree of Cancer. Her image is of extreme purity and beauty, with infinite subtlety; to see the Truth of her is hardly possible, for she reflects the nature of the observer in great perfection. She is represented as enthroned upon still water... she bears a shell-like cup, from which issues a crayfish... and the Lotus of Isis... She is the perfect agent and patient, able to receive and transmit everything without herself being affected thereby. If ill-dignified... everything that passes through her is refracted and distorted."

**English Paraphrase**:
**Pure Reflection** - Represents the **Watery part of Water**: total receptivity and reflection. She sits enthroned upon **still water**, robed and veiled in curving waves of light. She holds a shell-like cup from which a **crayfish** emerges, and the **Lotus of Isis** as emblem of the Great Mother. She mirrors the nature of any observer so perfectly that her own essence is almost impossible to grasp. Positively, she is tranquil, dreamy, intuitive, and the perfect channel—receiving and transmitting without being personally disturbed. Negatively, everything passing through her may become **distorted, illusory or deceptive**, and she can dissolve into passivity and escapism.

**Core**: **Receptive Mirror** - Deep intuition, emotional sensitivity, empathy, reflection, but also illusion and projection.

**Chinese Explanation**:
**圣杯皇后**代表**水中之水**，特别指水的**接受与反射**能力。她的形象极其纯净、美丽而细腻，几乎难以窥见她的真相，因为她**完美地反映观者的本性**。她在**平静的水面**上端坐，身披由光与水纹交织而成的衣袍，手持贝壳形圣杯，其中伸出**小龙虾**，并持有象征大母神的**伊西斯莲花**。她是理想的情感容器与通道：安静、梦幻、直觉敏锐，能接收并传导一切而不被表面波动所扰。逆位或失衡时，所有经过她的东西会被**折射与扭曲**，变成迷幻的镜像与情感幻觉，使人困在投射、理想化与自我欺骗之中。

**In Readings**: Intuitive woman, psychic sensitivity, empathy, emotional support, imagination, spiritual mediumship; or, illusion, projection, emotional dependency.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Queen of Cups is Water of Water - total receptivity. Enthroned on still water, she mirrors observers perfectly. Lotus of Isis shows Great Mother. If ill-dignified: distortion and illusion.
- **中文**: Crowley的圣杯皇后是水中之水—完全接受。在静水上端坐，她完美地反映观察者。伊西斯莲花显示大母神。如果失衡：扳曲和幻觉。

**Narrative Snippets**:
- `[ns_thoth_cups_034]` `[trigger: queen_cups_thoth]` `[factor_trigger: thoth_cups_queen]` `[role: 主干]` Queen of Cups = Water of Water—total receptivity and reflection; mirrors observer's nature perfectly. → Core
- `[ns_thoth_cups_035]` `[trigger: still_water_throne]` `[factor_trigger: thoth_cups_queen AND symbol_still_water]` `[role: 条件分支]` Enthroned on still water—shell cup with crayfish; Lotus of Isis for Great Mother. → Visual
- `[ns_thoth_cups_036]` `[trigger: mirror_distortion]` `[factor_trigger: thoth_cups_queen AND state_ill_dignified]` `[role: 条件分支]` If ill-dignified: everything passing through is refracted and distorted—illusion, projection. → Shadow"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Cups (圣杯皇后)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_thoth_cups_queen', 'thoth_cups_queen', 'expressing', 'evi_thoth_cups_queen', 'thoth_cups_queen', 'rule_thoth_cups_queen', 'concept_thoth_cups_queen', 'decan_zodiac', 'archetype']
    
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
        l1_anchor="bot_v1.0.0_queen_of_cups__圣杯皇后_001_L1",
    )
    version: str = "1.0.0"
