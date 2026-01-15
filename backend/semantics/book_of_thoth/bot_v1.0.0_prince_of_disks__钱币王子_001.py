"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063796
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
    semantic_id="bot_v1.0.0_prince_of_disks__钱币王子_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrinceOfDisks钱币王子(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Air of Earth | Intelligible matter | Practical thought |
| Bull Helmet | Taurus emblem | Stubborn endurance |
| Mathematical Orb | Planning globe | Measured cultivation |
| Implacable Temper | Relentless once provoked | Hidden strength |

**Title**: Prince of the Chariot of Earth (土之战车的王子)
**Elemental**: The Airy part of Earth (土中之气)
**Zodiac**: 21° Aries to 20° Taurus (白羊座21度至金牛座20度)

**Source Text**:
> "The Prince of Disks represents the airy part of Earth, indicating the florescence and fructification of that element... The figure of this Prince is meditative. He is the element of Earth become intelligible. Clothed in light armour, his helmet is crowned with the head of a bull; and his chariot is drawn by an ox... In his left hand he holds his disk, which is an orb resembling a globe, marked with mathematical symbols as if to imply the planning involved in agriculture. In his right hand he bears an orbed sceptre surmounted by a cross, a symbol of the Great Work accomplished... The character denoted by this card is that of great energy brought to bear upon the most solid of practical matters. He is energetic and enduring, a capable manager... He is lacking almost entirely in emotion... slow to anger, but, if driven, becomes implacable."

**English Paraphrase**:
**Intelligent Cultivation** – **Air of Earth**: Earth become **intelligible**, florescence and fruiting. Meditative, light armor, bull-head helmet, ox-drawn chariot. Holds **mathematical orb** (agricultural planning) and cross-scepter (Great Work accomplished). Brings **great energy to solid practical matters**: capable manager, steadfast, ingenious, trustworthy, patient. Seeks new uses for common things. Lacks emotion, somewhat insensitive, may seem dull but is not. Slow to anger but implacable if provoked.

**Core**: **Practical Intelligence** – Management, engineering, steady improvement, emotionally limited, resistant to abstract.

**Chinese Explanation**:
**钱币王子**代表**土中之气**：土变得**可理解**，开花结果。沉思，轻甲，**公牛头**盔，**公牛**拉车。持**数学球**（农业规划）与十字权杖（大工作已完成）。将**巨大能量施于最坚实实际事务**：能干管理者、坚定、富创造力、值得信赖、耐心。寻找日常物新用途。缺乏情感，有些迟钝，但其实不笨。不易怒，但一旦被逼就**无情**。

**In Readings**: Capable manager, engineer, practical problem-solver, steady worker, but emotionally limited, resentful of spiritual types, implacable when provoked.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Prince of Disks is Air of Earth - Earth become intelligible. Bull helmet, ox-drawn chariot. Mathematical orb for agricultural planning. Cross scepter shows Great Work accomplished. Slow to anger but implacable.
- **中文**: Crowley的钱币王子是土中之气—大地变得可理解。公牛头盔，公牛拉车。数学球用于农业规划。十字权杖显示大工作已完成。不易怒但无情。

**Narrative Snippets**:
- `[ns_thoth_disks_037]` `[trigger: prince_disks_thoth]` `[factor_trigger: thoth_disks_prince]` `[role: 主干]` Prince of Disks = Air of Earth—Earth become intelligible; florescence and fructification. → Core
- `[ns_thoth_disks_038]` `[trigger: bull_helmet_orb]` `[factor_trigger: thoth_disks_prince AND symbol_bull]` `[role: 条件分支]` Bull-head helmet, ox chariot; mathematical orb for planning; cross scepter (Great Work). → Visual
- `[ns_thoth_disks_039]` `[trigger: implacable_manager]` `[factor_trigger: thoth_disks_prince AND state_character]` `[role: 条件分支]` Capable manager, ingenious, trustworthy; lacking emotion; slow to anger but implacable. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Prince of Disks (钱币王子)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_prince_disks_air', 'air_of_earth', 'rel_prince_disks_manage', 'planning', 'prince_disks_plan']
    
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
        l1_anchor="bot_v1.0.0_prince_of_disks__钱币王子_001_L1",
    )
    version: str = "1.0.0"
