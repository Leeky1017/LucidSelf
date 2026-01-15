"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063414
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
    semantic_id="bot_v1.0.0_four_of_disks__power__钱币四_权力_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FourOfDisksPower钱币四权力(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chesed in Earth | Mercy in Earth | Full establishment |
| Sun in Capricorn | Reborn authority | Institutional power |
| Square Disks | Fortress tokens | Law and order |
| Dead Centre | Static point | Risk of rigidity |

**Title**: Lord of Earthly Power (尘世权力之主)
**Qabalistic**: Chesed in Earth (土中之仁慈)
**Astrological**: Sun in Capricorn (太阳入摩羯座)

**Source Text**:
> "The Four, Chesed, shows the establishment of the Universe in three dimensions, that is, below the Abyss. The generating idea is exhibited in its full material sense. The card is ruled by the Sun in Capricornus, the Sign in which he is reborn. The disks are very large and solid; the suggestion of the card is that of a fortress. This represents Law and Order, maintained by constant authority and vigilance. The disks themselves are square; revolution is very opposite to the card; and they contain the signs of the Four Elements... defence is valid only when violently active. So far as it appears stationary, it is the 'dead centre' of the engineer..."

**English Paraphrase**:
**Fortress of Order** – Corresponds to Chesed (Mercy/Structure) in Earth: the **full establishment** of the material universe in three dimensions (below the Abyss). Ruled by **Sun in Capricorn**, the sign of the Sun's rebirth at winter solstice. The disks are large, solid, and **square** – suggesting a **fortress**: Law, Order, and Power maintained by constant authority. Each disk contains a symbol of one of the Four Elements. Though they appear static, they do revolve; defense is only valid when **actively maintained**. This is **Power**: established authority, structure, security, and material dominion, but it requires vigilance or it becomes a "dead center."

**Core**: **Established Authority** – Power, stability, law, order, fortress mentality, material security, but risk of rigidity.

**Chinese Explanation**:
**钱币四（权力）**对应土元素中的**Chesed（仁慈/秩序）**，展示宇宙在三维空间中的**完全建立**（深渊之下的显化）。统治星为**太阳入摩羯座**，这是太阳在冬至**重生**的位置。圆盘非常大且坚固，形状为**方形**，整体给人**堡垒**的感觉：法律、秩序、权力通过持续的权威与警戒来维持。每个方形圆盘上包含四元素之一的符号。虽然看起来静止，它们其实仍在旋转——因为**防御只有在主动行动时才有效**。这张牌代表既定权威与物质保障，但若过于僵化不动，就会成为工程学意义上的"死点"（dead center）。

**In Readings**: Power, authority, stability, security, established structures, law and order, material success, but also rigidity, fortress mentality, control.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Four of Disks shows Chesed establishing Universe below Abyss. Sun in Capricorn reborn. Square disks suggest fortress. Defense valid only when active - or becomes "dead centre".
- **中文**: Crowley的钱币四展示Chesed在深渊之下确立宇宙。太阳入摩羯重生。方形圆盘暗示堡垒。防御只有积极时才有效—否则变成"死点"。

**Narrative Snippets**:
- `[ns_thoth_disks_010]` `[trigger: four_disks_power]` `[factor_trigger: thoth_disks_four]` `[role: 主干]` Four of Disks = Lord of Earthly Power—Chesed in Earth; Law and Order maintained by authority. → Core
- `[ns_thoth_disks_011]` `[trigger: sun_capricorn_reborn]` `[factor_trigger: thoth_disks_four AND planet_sun_capricorn]` `[role: 条件分支]` Sun in Capricorn—reborn at solstice; institutional power; generating idea in full material sense. → Astrological
- `[ns_thoth_disks_012]` `[trigger: fortress_dead_center]` `[factor_trigger: thoth_disks_four AND symbol_fortress]` `[role: 条件分支]` Square disks suggest fortress; defense valid only when active—or becomes "dead centre". → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Four of Disks: Power (钱币四：权力)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_four_001', 'tarot_established_authority', 'rel_disks_four_002', 'tarot_dead_center', 'l1_anchor', 'confidence', 'evi_disks_four_001', 'evi_disks_four_002', 'tarot_dead_center', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_four_001', 'tarot_disks_four', 'astro_sun_capricorn']
    
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
        l1_anchor="bot_v1.0.0_four_of_disks__power__钱币四_权力_001_L1",
    )
    version: str = "1.0.0"
