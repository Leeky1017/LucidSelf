"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412222
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
    semantic_id="dvd_v1.0.0_food_食物_供应_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Food食物供应(SemanticEntry):
    """
    ### Source Text

> **Food**: A picture of spiritual nourishment and provision.
> Positive: Eating go...
    """
    
    original_text: str = """### Source Text

> **Food**: A picture of spiritual nourishment and provision.
> Positive: Eating good food speaks of receiving spiritual nourishment—the Word of God. Preparing food speaks of ministering to others.
> Negative: Rotten food speaks of contaminated teaching. Being hungry indicates spiritual lack.
> John 6:35 "I am the bread of life: he that comes to me shall never hunger."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Food | 食物 | 属灵供应 |
| Nourishment | 滋养 | 灵里的喂养 |
| Word | 话语 | 神的话语 |
| Hunger | 饥饿 | 属灵缺乏 |

### English Paraphrase

Food represents spiritual nourishment and provision. Eating good food speaks of receiving the Word of God. Preparing food speaks of ministering to others. Rotten food indicates contaminated teaching. Being hungry indicates spiritual lack.

### Chinese Interpretation

食物代表属灵的滋养和供应。吃好食物象征接受神的话语。预备食物象征服事他人。腐烂的食物表示污染的教导。饥饿表示属灵缺乏。

### Core Points

1. **正负皆可**: 食物状态决定含义
2. **话语供应**: 神的话是生命粮
3. **服事他人**: 预备食物是服事
4. **污染警告**: 腐烂食物是假教导

### Narrative Snippets

- `[ns_dav_f019]` `[trigger: food_word]` `[factor_trigger: dream_food AND dream_word]` `[role: 主干]` I am the bread of life—good food represents receiving the Word of God for spiritual nourishment. → 我是生命的粮——好食物代表接受神的话语得属灵滋养。"""
    normalized_text_zh: str = """"""
    subject: str = "Food 食物/供应"
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
        l1_anchor="dvd_v1.0.0_food_食物_供应_001_L1",
    )
    version: str = "1.0.0"
