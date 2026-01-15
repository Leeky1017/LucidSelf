"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419801
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
    semantic_id="dvd_v1.0.0_clay_泥土_器皿_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Clay泥土器皿(SemanticEntry):
    """
    ### Source Text

> **Clay**: A picture of being molded and shaped in God's hands. Also speaks of our...
    """
    
    original_text: str = """### Source Text

> **Clay**: A picture of being molded and shaped in God's hands. Also speaks of our mortality.
> We are clay vessels in the hands of the Potter. The Lord shapes and molds us for His purposes. Clay also reminds us of our humble origins—from dust we came.
> Jeremiah 18:6 "O house of Israel, cannot I do with you as this potter? says the LORD. Behold, as the clay is in the potter's hand, so are you in my hand."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Clay | 泥土 | 被塑造的材料 |
| Potter | 窑匠 | 塑造者（神） |
| Vessel | 器皿 | 被使用的容器 |
| Mortality | 必死性 | 人的有限性 |

### English Paraphrase

Clay represents being molded and shaped in God's hands. We are clay vessels in the Potter's hands, shaped for His purposes. Clay also reminds us of our humble origins and mortality—from dust we came and to dust we return.

### Chinese Interpretation

泥土代表在神手中被塑造。我们是窑匠手中的泥土器皿，被塑造以成就祂的目的。泥土也提醒我们卑微的起源和必死性——我们从尘土而来。

### Core Points

1. **通常正面**: 代表神的塑造工作
2. **顺服呼召**: 愿意在神手中被塑造
3. **谦卑提醒**: 我们不过是尘土
4. **目的导向**: 神按祂的旨意塑造我们

### Narrative Snippets

- `[ns_dav_c029]` `[trigger: clay_potter]` `[factor_trigger: dream_clay AND dream_potter]` `[role: 主干]` We are clay vessels in the Potter's hands—the Lord shapes and molds us for His purposes. → 我们是窑匠手中的泥土器皿，主按祂的目的塑造我们。
- `[ns_dav_c030]` `[trigger: clay_mortality]` `[factor_trigger: dream_clay AND dream_mortality]` `[role: 提醒]` Clay reminds us of our humble origins—from dust we came and to dust we return. → 泥土提醒我们卑微的起源——我们从尘土而来，也要归于尘土。"""
    normalized_text_zh: str = """"""
    subject: str = "Clay 泥土/器皿"
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
        l1_anchor="dvd_v1.0.0_clay_泥土_器皿_001_L1",
    )
    version: str = "1.0.0"
