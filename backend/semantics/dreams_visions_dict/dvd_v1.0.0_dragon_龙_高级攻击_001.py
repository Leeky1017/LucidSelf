"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402090
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
    semantic_id="dvd_v1.0.0_dragon_龙_高级攻击_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Dragon龙高级攻击(SemanticEntry):
    """
    ### Source Text

> **Dragon**: A picture of high level demonic attack.
> Because Dragons are mytholo...
    """
    
    original_text: str = """### Source Text

> **Dragon**: A picture of high level demonic attack.
> Because Dragons are mythological in nature, if you keep dreaming of dragons, it could mean you have been getting into writings of this nature.
> The devil is mentioned as a dragon in Scripture. If you see a vision of a dragon, this speaks of high level demonic attack.
> Revelation 12:9 "And the great dragon was cast out, that old serpent, called the devil, and Satan, who deceives the whole world."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Dragon | 龙 | 高级邪灵攻击 |
| Devil | 魔鬼 | 撒但的称号 |
| Mythological | 神话的 | 与虚假教导相关 |
| Deception | 迷惑 | 迷惑全世界的 |

### English Paraphrase

A dragon represents high level demonic attack. In Scripture, the devil is called a dragon. If you always have visions of dragons and folklore, you may have opened your heart to teachings not of the Lord, contaminating your spirit.

### Chinese Interpretation

龙代表高级邪灵攻击。在圣经中，魔鬼被称为龙。如果你总是看见龙和民间传说的异象，你可能向不属于主的教导敞开了心，污染了你的灵。

### Core Points

1. **始终负面**: 龙代表撒但和高级攻击
2. **邪灵等级**: 最高级别的邪灵攻击
3. **污染警告**: 可能表示接受了错误教导
4. **迷惑全地**: 龙迷惑全世界

### Narrative Snippets

- `[ns_dav_d028]` `[trigger: dragon_attack]` `[factor_trigger: dream_dragon AND dream_attack]` `[role: 主干]` A dragon speaks of high level demonic attack—the devil is called a dragon in Scripture. → 龙象征高级邪灵攻击——在圣经中魔鬼被称为龙。
- `[ns_dav_d029]` `[trigger: dragon_contaminate]` `[factor_trigger: dream_dragon AND dream_contamination]` `[role: 警告]` If you always have visions of dragons, you may have contaminated your spirit with wrong teachings. → 如果你总是看见龙的异象，你可能用错误的教导污染了你的灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Dragon 龙/高级攻击"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="dvd_v1.0.0_dragon_龙_高级攻击_001_L1",
    )
    version: str = "1.0.0"
