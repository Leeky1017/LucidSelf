"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443943
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
    semantic_id="dvd_v1.0.0_light_光_盼望_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Light光盼望(SemanticEntry):
    """
    ### Source Text

> **Light**: Light in darkness has always been a picture of hope. Light brings life...
    """
    
    original_text: str = """### Source Text

> **Light**: Light in darkness has always been a picture of hope. Light brings life—in Scripture life, light and love are used interchangeably.
> Positive: Light at the end of the tunnel speaks of hope and the end of a hard journey. A dark room dispelled by light means the Lord displacing darkness with His presence.
> Negative: A being coming as bright light should be viewed with caution—Satan disguises himself as an angel of light.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Light | 光 | 盼望和生命 |
| Hope | 盼望 | 艰难旅程的尽头 |
| Darkness | 黑暗 | 被光驱散 |
| Angel of light | 光明天使 | 撒但的伪装 |

### English Paraphrase

Light in darkness represents hope and life. Light at the end of the tunnel speaks of breakthrough coming. Light displacing darkness shows the Lord's presence. Caution: a being coming as bright light may be deception—Satan disguises himself as an angel of light.

### Chinese Interpretation

黑暗中的光代表盼望和生命。隧道尽头的光象征突破即将到来。光驱散黑暗显示主的同在。警惕：作为明光而来的存在可能是迷惑——撒但装作光明的天使。

### Core Points

1. **正负皆可**: 光的来源决定含义
2. **盼望象征**: 艰难旅程的尽头
3. **主的同在**: 驱散黑暗的光
4. **迷惑警告**: 假光的欺骗

### Narrative Snippets

- `[ns_dav_l009]` `[trigger: light_hope]` `[factor_trigger: dream_light AND dream_hope]` `[role: 主干]` Light at the end of the tunnel speaks of hope and the end of a hard and difficult journey. → 隧道尽头的光象征盼望和艰难旅程的结束。
- `[ns_dav_l010]` `[trigger: light_deception]` `[factor_trigger: dream_light AND dream_deception]` `[role: 警告]` Satan disguises himself as an angel of light—a bright being may be deception. → 撒但装作光明的天使——明亮的存在可能是迷惑。"""
    normalized_text_zh: str = """"""
    subject: str = "Light 光/盼望"
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
        l1_anchor="dvd_v1.0.0_light_光_盼望_001_L1",
    )
    version: str = "1.0.0"
