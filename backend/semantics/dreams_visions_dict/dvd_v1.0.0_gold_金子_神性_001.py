"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.390692
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
    semantic_id="dvd_v1.0.0_gold_金子_神性_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Gold金子神性(SemanticEntry):
    """
    ### Source Text

> **Gold**: A picture of God's nature, divinity, and glory. Also represents wealth ...
    """
    
    original_text: str = """### Source Text

> **Gold**: A picture of God's nature, divinity, and glory. Also represents wealth and value.
> Positive: Gold speaks of something refined and pure—God's nature and glory. Receiving gold indicates receiving something of eternal value. The Ark was overlaid with gold.
> Negative: The golden calf was an idol. Love of gold (money) is the root of all evil.
> 1 Peter 1:7 "...your faith, being much more precious than of gold that perishes..."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Gold | 金子 | 神的性情 |
| Divinity | 神性 | 神的荣耀 |
| Refined | 精炼 | 经过火试 |
| Idol | 偶像 | 负面的金崇拜 |

### English Paraphrase

Gold represents God's nature, divinity, and glory—also wealth and value. Gold speaks of something refined and pure. Receiving gold indicates receiving eternal value. The Ark was overlaid with gold. Negatively, the golden calf was an idol; love of gold is the root of all evil.

### Chinese Interpretation

金子代表神的性情、神性和荣耀——也代表财富和价值。金子象征精炼和纯净的事物。接受金子表示接受永恒的价值。约柜用金子包裹。负面而言，金牛犊是偶像；贪财是万恶之根。

### Core Points

1. **正负皆可**: 金子使用决定含义
2. **神性象征**: 代表神的荣耀
3. **精炼价值**: 经过火试的信心
4. **偶像警告**: 可能成为偶像

### Narrative Snippets

- `[ns_dav_g007]` `[trigger: gold_divine]` `[factor_trigger: dream_gold AND dream_divine]` `[role: 主干]` Gold speaks of God's nature and glory—something refined, pure, and of eternal value. → 金子象征神的性情和荣耀——精炼、纯净、有永恒价值的事物。
- `[ns_dav_g008]` `[trigger: gold_idol]` `[factor_trigger: dream_gold AND dream_idol]` `[role: 警告]` The golden calf was an idol—love of gold can become idolatry and the root of evil. → 金牛犊是偶像——爱金子能成为偶像崇拜和万恶之根。"""
    normalized_text_zh: str = """"""
    subject: str = "Gold 金子/神性"
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
        l1_anchor="dvd_v1.0.0_gold_金子_神性_001_L1",
    )
    version: str = "1.0.0"
