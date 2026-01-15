"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396260
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
    semantic_id="dvd_v1.0.0_mouth_口_言语_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Mouth口言语(SemanticEntry):
    """
    ### Source Text

> **Mouth**: If our eyes are the windows to our souls, our mouths are the doorway! ...
    """
    
    original_text: str = """### Source Text

> **Mouth**: If our eyes are the windows to our souls, our mouths are the doorway! Out of our mouths come both blessing and cursing. What comes out of your mouth under pressure is a direct representation of what is really inside.
> Positive: Fresh water or oil from your mouth speaks of the Lord's words blessing others.
> Negative: Poison, frogs, fire from the mouth speaks of curses and destruction.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Mouth | 口 | 言语的出口 |
| Blessing | 祝福 | 正面的话 |
| Cursing | 咒诅 | 负面的话 |
| Poison | 毒素 | 有害的言语 |

### English Paraphrase

The mouth is the doorway of the soul—both blessing and cursing come from it. What comes out under pressure represents what is inside. Fresh water or oil from your mouth speaks of the Lord's words blessing others. Poison, frogs, fire speak of curses and destruction.

### Chinese Interpretation

口是灵魂的门——祝福和咒诅都从中出来。压力下说出来的代表里面的东西。从口中出来的清水或油象征主的话祝福他人。毒素、青蛙、火象征咒诅和毁灭。

### Core Points

1. **正负皆可**: 言语内容决定含义
2. **言语象征**: 从口而出的话
3. **祝福言语**: 水和油是祝福
4. **咒诅警告**: 毒和火是咒诅

### Narrative Snippets

- `[ns_dav_m019]` `[trigger: mouth_blessing]` `[factor_trigger: dream_mouth AND dream_blessing]` `[role: 主干]` Fresh water or oil from your mouth speaks of the Lord's words blessing everyone around you. → 从你口中出来的清水或油象征主的话祝福你周围的每个人。
- `[ns_dav_m020]` `[trigger: mouth_curse]` `[factor_trigger: dream_mouth AND dream_curse]` `[role: 警告]` Fire coming from the mouth is a picture of speaking curses and destroying others with your words. → 从口中出来的火象征说咒诅的话和用言语毁灭他人。"""
    normalized_text_zh: str = """"""
    subject: str = "Mouth 口/言语"
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
        l1_anchor="dvd_v1.0.0_mouth_口_言语_001_L1",
    )
    version: str = "1.0.0"
