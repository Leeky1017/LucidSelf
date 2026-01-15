"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439743
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
    semantic_id="dvd_v1.0.0_axe_斧头_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Axe斧头(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: A weapon of spiritual warfare as well. Also refers to destru...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: A weapon of spiritual warfare as well. Also refers to destruction or humiliation.

**Positive** (Jer 51:20): "You are my battle axe and weapons of war"—we as the church are an axe in the Lord's hand, His weapon against the enemy. Represents strength and destruction against Satan's works. Powerful but crude instrument—brute strength rather than precision.

**Negative** (Matt 3:10): "The axe is laid at the root of the trees"—separation and destruction. Separates good fruit from bad. When axe brings division, Lord is dividing those who mean business with God from those who don't. Axe to root = Lord removing entirely an aspect from person's life, bringing flesh to death. May require a prophet to send decree.

**See also**: Armor, Sword, Trees

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Battle axe | Church as God's weapon | Warfare against Satan |
| Axe at root | Judgment, removal | Separation of good/bad |
| Brute strength | Crude but powerful | Not precision |

### English Paraphrase

Axe = spiritual warfare weapon; destruction or humiliation. **Positive** (Jer 51:20): Church is God's battle axe—His weapon against enemy, strength against Satan's works. Powerful but crude (brute strength, not precision). **Negative** (Matt 3:10): Axe at root of trees = separation and judgment. Removes entirely an aspect from life, brings flesh to death. Division between those serious with God and those who aren't. Prophet may send decree for such divine axe work.

### Chinese Interpretation（完整对等诠释）

斧头 = 属灵争战武器；毁灭或羞辱。**正面**（耶51:20）：教会是神的战斧——祂对付仇敌的武器，对抗撒但工作的力量。有力但粗犷（蛮力，非精确）。**负面**（太3:10）：斧头已放在树根上 = 分离和审判。完全从生命中移除某方面，使肉体死。分别认真对待神的和不认真的。先知可能发出诏令进行这神圣的斧头工作。

### Narrative Snippets

- `[ns_dav_a053]` `[trigger: 梦斧头]` `[factor_trigger: dream_symbol_axe]` `[role: 主干]` Axe = spiritual warfare weapon—church as God's battle axe or judgment/separation tool. → Dreams Dictionary #Axe
- `[ns_dav_a054]` `[trigger: 战斧]` `[factor_trigger: dream_symbol_axe AND axe_use]` `[role: 条件分支]` Battle axe (Jer 51:20) = church is God's weapon against Satan—brute strength. → Dreams Dictionary #Axe
- `[ns_dav_a055]` `[trigger: 斧在树根]` `[factor_trigger: dream_symbol_axe AND axe_use]` `[role: 条件分支]` Axe at root (Matt 3:10) = judgment, separation, removing flesh—division of serious vs casual. → Dreams Dictionary #Axe"""
    normalized_text_zh: str = """"""
    subject: str = "Axe 斧头"
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
        l1_anchor="dvd_v1.0.0_axe_斧头_001_L1",
    )
    version: str = "1.0.0"
