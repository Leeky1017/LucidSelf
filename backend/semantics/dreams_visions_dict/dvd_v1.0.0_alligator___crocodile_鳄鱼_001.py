"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439617
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
    semantic_id="dvd_v1.0.0_alligator___crocodile_鳄鱼_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class AlligatorCrocodile鳄鱼(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: A spirit of destruction. I have never interpreted a dream or...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: A spirit of destruction. I have never interpreted a dream or vision where an alligator is seen as a positive picture. In most cases it is seen as an agent of destruction and theft.

It resembles the work of the enemy, and if I see it in vision I class it as a power demon. The teeth of the animal represent a tearing and a violent attack.

**Scripture**: Daniel 7:19 - "Then I would know the truth of the fourth beast, which was diverse from all the others, exceeding dreadful, whose teeth were of iron, and his nails of brass; which devoured, broke in pieces, and stamped the residue with his feet."

**See also**: Animal, Bear, Demons

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Alligator/Crocodile | Spirit of destruction | Always negative |
| Teeth | Tearing, violent attack | Destructive power |
| Power demon | High-level demonic entity | Serious spiritual threat |

### English Paraphrase

Alligator/Crocodile is **always negative**—a spirit of destruction. Toach has never interpreted it positively. It represents the enemy's work, classified as a power demon when seen in visions. The teeth symbolize tearing and violent attack—destructive, devouring force. Biblical parallel: Daniel 7:19's beast with iron teeth that devours, breaks in pieces, and tramples. This is a serious spiritual threat requiring warfare response.

### Chinese Interpretation（完整对等诠释）

鳄鱼**始终是负面的**——毁灭之灵。Toach从未将其解释为正面。它代表仇敌的工作，在异象中被归类为权势魔鬼。牙齿象征撕裂和暴力攻击——毁灭性、吞噬的力量。圣经对应：但以理书7:19中铁牙兽，吞吃、打碎、用脚践踏。这是严重的属灵威胁，需要争战回应。

### Core Points

- 鳄鱼 = 毁灭之灵（**始终负面**）
- 代表仇敌工作，权势魔鬼
- 牙齿 = 撕裂、暴力攻击
- 圣经对应：但以理书铁牙兽
- 需要属灵争战回应

### Narrative Snippets

- `[ns_dav_a011]` `[trigger: 梦鳄鱼]` `[factor_trigger: dream_symbol_alligator]` `[role: 主干]` Alligator/Crocodile = spirit of destruction, always negative, never positive interpretation. → Dreams Dictionary #Alligator
- `[ns_dav_a012]` `[trigger: 鳄鱼牙齿]` `[factor_trigger: dream_symbol_alligator AND outcome_jiong AND demon_level]` `[role: 主干依赖]` Teeth represent tearing and violent attack—classified as power demon. → Dreams Dictionary #Alligator"""
    normalized_text_zh: str = """"""
    subject: str = "Alligator / Crocodile 鳄鱼"
    factor_refs: list = ['dream_symbol_alligator', 'demon_power', 'symbol_teeth']
    
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
        l1_anchor="dvd_v1.0.0_alligator___crocodile_鳄鱼_001_L1",
    )
    version: str = "1.0.0"
