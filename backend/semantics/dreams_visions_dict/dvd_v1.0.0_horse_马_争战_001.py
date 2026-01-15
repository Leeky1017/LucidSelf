"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450583
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
    semantic_id="dvd_v1.0.0_horse_马_争战_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Horse马争战(SemanticEntry):
    """
    ### Source Text

> **Horse**: Horses are a picture of strength, especially related to spiritual warf...
    """
    
    original_text: str = """### Source Text

> **Horse**: Horses are a picture of strength, especially related to spiritual warfare. In OT times, the number of horses indicated army strength.
> Positive: An army of horses and riders on your side pictures the Lord's army fighting for you. Jesus on a white horse represents His power as King.
> Negative: Relying on horses instead of God speaks of works and striving. Black horses speak of the enemy's army.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Horse | 马 | 力量和争战 |
| Warfare | 争战 | 属灵争战 |
| Army | 军队 | 神或仇敌的军队 |
| White horse | 白马 | 主的得胜 |

### English Paraphrase

Horses represent strength, especially in spiritual warfare. An army of horses on your side pictures God's army fighting for you. Jesus on a white horse shows His power as King. Relying on horses instead of God speaks of works and striving. Black horses represent the enemy's army.

### Chinese Interpretation

马代表力量，尤其在属灵争战中。站在你这边的马军象征神的军队为你争战。耶稣骑白马显示祂作为王的权能。倚靠马而非神象征靠行为努力。黑马代表仇敌的军队。

### Core Points

1. **正负皆可**: 马的颜色和阵营决定含义
2. **争战象征**: 属灵争战的能力
3. **白马得胜**: 主的权能和得胜
4. **靠己警告**: 倚靠马是倚靠自己

### Narrative Snippets

- `[ns_dav_h014]` `[trigger: horse_warfare]` `[factor_trigger: dream_horse AND dream_warfare]` `[role: 主干]` Horses are a picture of strength in spiritual warfare—the Lord's army fighting on your behalf. → 马是属灵争战中力量的象征——主的军队为你争战。
- `[ns_dav_h015]` `[trigger: horse_works]` `[factor_trigger: dream_horse AND dream_flesh]` `[role: 警告]` Relying on the strength of horses instead of the Lord speaks of works and striving in the flesh. → 倚靠马的力量而非主象征靠肉体行事和努力。"""
    normalized_text_zh: str = """"""
    subject: str = "Horse 马/争战"
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
        l1_anchor="dvd_v1.0.0_horse_马_争战_001_L1",
    )
    version: str = "1.0.0"
