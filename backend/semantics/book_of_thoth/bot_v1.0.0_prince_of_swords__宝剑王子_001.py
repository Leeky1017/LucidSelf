"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076597
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
    semantic_id="bot_v1.0.0_prince_of_swords__宝剑王子_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrinceOfSwords宝剑王子(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Air of Air | Pure mentality | Mind itself |
| Winged Children | Uncontrolled thoughts | No reins |
| Geometrical Chariot | Abstract structure | Pattern logic |
| Sword + Sickle | Create + destroy | Instant reversal |

**Title**: Prince of the Chariots of the Winds (风之战车的王子)
**Elemental**: The Airy part of Air (气中之气)
**Zodiac**: 21° Capricorn to 20° Aquarius (摩羯座21度至宝瓶座20度)

**Source Text**:
> "This card represents the airy part of Air... it is a picture of the Mind as such. He rules from the 21st degree of Capricornus to the 20th degree of Aquarius. The figure of this Prince is clothed with closely woven armour adorned with definite device, and the chariot which bears him suggests (even more closely) geometrical ideas. This chariot is drawn by winged children... leaping irresponsibly in any direction that takes their fancy... quite unable to progress in any definite direction except by accident. This is a perfect picture of the Mind. ... his logical mental processes have reduced the Air... to many diverse geometrical patterns, but in these there is no real plan... what he creates he instantly destroys."

**English Paraphrase**:
**Restless Mind** – Represents the **Airy part of Air**: pure mentality. The Prince rides a geometrical chariot drawn by winged children who dart about playfully with no reins – symbol of thought moving **in all directions at once**. He wears patterned armour, surrounded by abstract designs: logic breaking Air into many forms. He raises a sword to create and holds a sickle to destroy what he has just formed. This is the **unfocused analytic mind**: brilliant in concept, fast, abstract, but often lacking overall plan or heart.

**Core**: **Abstract Intelligence** – Analysis, ideas, theories, patterns, but risk of detachment and volatility.

**Chinese Explanation**:
**宝剑王子**代表**气中之气**，是“心智本身”的化身。他乘坐几何感极强的战车，由**长着翅膀的孩童**拉动，这些孩子随性跳跃、毫无缰绳控制，象征**思维向一切方向任意驰散**。他身披带有清晰图案的铠甲，周围充满抽象几何形状，显示他的逻辑思维把空气（观念）拆解成**无数模式与结构**。他一手举剑创造，一手持镰刀随即摧毁，这代表**分析心智的双刃性**：能够迅速建立模型，又同样迅速地拆毁，不断推翻自己。正位时，他带来**高度理性、概念创新、抽象推理能力**；失衡时，则成为**冷漠、碎片化、脱离现实的人**，在纯粹思辨中消耗能量而没有落地行动。

**In Readings**: Strong intellect, analysis, strategy, mental agility, scientific or academic focus; or, over‑thinking, inconsistency, argument for its own sake.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Prince of Swords is Air of Air - pure Mind. Winged children pull chariot with no reins. Geometrical patterns everywhere. Sword creates, sickle destroys instantly. "What he creates he instantly destroys."
- **中文**: Crowley的宝剑王子是气中之气—纯粹心智。有翼孩童无缰绳拉车。到处几何图案。剑创造，镰刀即刻毁灭。"他创造的一切立即毁灭"。

**Narrative Snippets**:
- `[ns_thoth_swords_037]` `[trigger: prince_swords_thoth]` `[factor_trigger: thoth_swords_prince]` `[role: 主干]` Prince of Swords = Air of Air—pure Mind; picture of the intellect itself; logical patterns. → Core
- `[ns_thoth_swords_038]` `[trigger: winged_children]` `[factor_trigger: thoth_swords_prince AND symbol_winged_children]` `[role: 条件分支]` Winged children pull geometrical chariot with no reins—thoughts leaping in all directions. → Visual
- `[ns_thoth_swords_039]` `[trigger: create_destroy]` `[factor_trigger: thoth_swords_prince AND state_volatile]` `[role: 条件分支]` Sword creates, sickle instantly destroys—"what he creates he instantly destroys"; no real plan. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Prince of Swords (宝剑王子)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_prince_swords_air', 'air_of_air', 'rel_prince_swords_volatile', 'creation', 'prince_swords_analysis']
    
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
        l1_anchor="bot_v1.0.0_prince_of_swords__宝剑王子_001_L1",
    )
    version: str = "1.0.0"
