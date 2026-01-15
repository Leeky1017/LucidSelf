"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439727
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
    semantic_id="dvd_v1.0.0_army_军队_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Army军队(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: The collective work of the enemy or the Lord in your life. C...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: The collective work of the enemy or the Lord in your life. Can also represent a season of training for the work God has called you to.

**Dreams - Positive**: Dreaming of army positively = strengthened, equipped. Being enlisted = going through spiritual training. Army speaks of training, being equipped, force of strength, unity, protection.

**Dreams - Negative**: Being captured, chased, oppressed = captive to desires and flesh not of Lord. Controlling/dominating others. Recurring "prisoner" dreams where you're fighting out = spiritual attack or conflict. Solution: rise up in Jesus' name OR dream_stop running, rest, let God take control. Jesus has already won the battle!

**Visions - Positive** (Joel 2:11): Body of Christ = army of God—powerful, enabled, overcoming obstacles. Apostle pictured as "General," Prophet as watchman/warrior.

**Visions - Negative**: Dark army = forces of Satan, pharaoh of this world—destruction, fear, theft, strife. Lord's army in disarray = disunity in body. Wounded soldiers = those attacked in Christian walk.

**See also**: Ambush, War

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Army of God | Body of Christ | Unity, strength |
| Dark army | Forces of Satan | Enemy attack |
| Enlisted | Spiritual training | Preparation |
| Prisoner dreams | Spiritual conflict | Need victory |

### English Paraphrase

Army = collective work of Lord or enemy; training season. **Positive**: Being enlisted = spiritual training, equipping. Army = strength, unity, protection. Body of Christ as God's army (Joel 2:11)—powerful, overcoming. **Negative**: Captured/chased = captive to flesh or oppression. Prisoner dreams = spiritual attack—solution: rise in Jesus' name or stop striving and let God take control (He's already won). Dark army = Satan's forces. Disarrayed Lord's army = body's disunity. Wounded soldiers = attacked believers.

### Chinese Interpretation（完整对等诠释）

军队 = 主或仇敌的集体工作；训练季节。**正面**：被征召 = 属灵训练、装备。军队 = 力量、合一、保护。基督的身体作为神的军队（珥2:11）——有能力、得胜。**负面**：被俘/追赶 = 被肉体或压制捆绑。囚犯的梦 = 属灵争战——解决方案：奉耶稣的名起来，或停止挣扎让神掌管（祂已得胜）。黑暗军队 = 撒但的势力。混乱的主军队 = 身体不合一。受伤士兵 = 受攻击的信徒。

### Narrative Snippets

- `[ns_dav_a047]` `[trigger: 梦军队]` `[factor_trigger: dream_symbol_army]` `[role: 主干]` Army = collective work of Lord (positive) or enemy (negative); training and warfare. → Dreams Dictionary #Army
- `[ns_dav_a048]` `[trigger: 被征召]` `[factor_trigger: dream_symbol_army AND army_role]` `[role: 条件分支]` Being enlisted = spiritual training, equipping, strengthening. → Dreams Dictionary #Army
- `[ns_dav_a049]` `[trigger: 囚犯梦]` `[factor_trigger: dream_symbol_army AND army_role]` `[role: 条件分支]` Prisoner/captured dreams = spiritual conflict—rise in Jesus' name or let God take control. → Dreams Dictionary #Army"""
    normalized_text_zh: str = """"""
    subject: str = "Army 军队"
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
        l1_anchor="dvd_v1.0.0_army_军队_001_L1",
    )
    version: str = "1.0.0"
