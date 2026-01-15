"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439736
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
    semantic_id="dvd_v1.0.0_arrow_箭_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Arrow箭(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: Arrows speak of spiritual warfare, words being spoken, and y...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: Arrows speak of spiritual warfare, words being spoken, and your strengths.

**Positive - Deliverance** (2 Kings 13:17): "The arrow of the LORD's deliverance"—God working on our behalf. Fiery arrow = word of Lord going forth like lightning, accomplishing its work. Speaking decrees like fire.

**Positive - Children** (Psalm 127:4): "As arrows in the hand of a mighty man, so are the children of one's youth." Our job as parents is to prepare and then send children into the world.

**Negative** (Prov 25:18): Dark arrow = weapons of enemy—destroy and cast down righteous. Negative words and curses spoken over God's people = black arrows that pierce, causing theft, strife, destruction, fear.

**See also**: Armor, Bow, Shield, Sword

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Arrow of Lord | Deliverance, decree | God's word going forth |
| Fiery arrow | Powerful word/decree | Accomplishing God's work |
| Children as arrows | Offspring | Prepared and sent |
| Black arrows | Enemy's words/curses | Attack, destruction |

### English Paraphrase

Arrow = spiritual warfare, words, strengths. **Positive**: Arrow of Lord (2 Kgs 13:17) = deliverance, God working on your behalf. Fiery arrow = word of Lord going forth like lightning, decrees spoken like fire. Also arrows = children (Ps 127:4)—parents prepare and send them into world. **Negative**: Dark/black arrows = enemy's weapons. Negative words and curses over God's people = arrows that pierce, causing theft, strife, destruction, fear.

### Chinese Interpretation（完整对等诠释）

箭 = 属灵争战、话语、力量。**正面**：耶和华的箭（王下13:17）= 拯救，神为你工作。火箭 = 神的话如闪电发出，宣告如火发出。也箭 = 儿女（诗127:4）——父母预备并差遣他们进入世界。**负面**：黑暗/黑色的箭 = 仇敌的武器。对神子民的负面话语和咒诅 = 刺穿的箭，造成偷窃、纷争、毁灭、恐惧。

### Narrative Snippets

- `[ns_dav_a050]` `[trigger: 梦箭]` `[factor_trigger: dream_symbol_arrow]` `[role: 主干]` Arrow = spiritual warfare, words, strengths—deliverance or attack. → Dreams Dictionary #Arrow
- `[ns_dav_a051]` `[trigger: 耶和华的箭]` `[factor_trigger: dream_symbol_arrow AND arrow_nature]` `[role: 条件分支]` Arrow of the Lord = deliverance, fiery decrees going forth like lightning. → Dreams Dictionary #Arrow
- `[ns_dav_a052]` `[trigger: 黑箭]` `[factor_trigger: dream_symbol_arrow AND arrow_nature]` `[role: 条件分支]` Dark arrows = enemy's words and curses—causing theft, strife, destruction. → Dreams Dictionary #Arrow"""
    normalized_text_zh: str = """"""
    subject: str = "Arrow 箭"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_arrow_箭_001_L1",
    )
    version: str = "1.0.0"
