"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405275
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
    semantic_id="dvd_v1.0.0_pig_猪_不洁_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Pig猪不洁(SemanticEntry):
    """
    ### Source Text

> **Pig**: Universally associated with filth and something unclean. There is no pos...
    """
    
    original_text: str = """### Source Text

> **Pig**: Universally associated with filth and something unclean. There is no positive interpretation for a pig in Scripture. Pigs were unclean animals the Israelites were forbidden to eat. A jewel in a pig's snout speaks of a woman without discretion. A vision of a pig speaks of an unclean spirit.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Pig | 猪 | 不洁和污秽 |
| Unclean | 不洁 | 禁止吃的 |
| Discretion | 谨慎 | 缺乏判断力 |
| Spirit | 灵 | 污秽的灵 |

### English Paraphrase

A pig is universally associated with filth and uncleanness. Scripture has no positive interpretation for a pig—they were forbidden food. A jewel in a pig's snout represents a woman without discretion. A vision of a pig speaks of an unclean spirit.

### Chinese Interpretation

猪普遍与污秽和不洁相关。圣经中猪没有正面解释——它们是禁止的食物。猪鼻子上的珠宝代表没有谨慎的女人。看见猪象征污秽的灵。

### Core Points

1. **始终负面**: 猪是不洁的象征
2. **污秽象征**: 圣经中禁止的
3. **缺乏判断**: 没有谨慎
4. **邪灵警告**: 污秽的灵

### Narrative Snippets

- `[ns_dav_p008]` `[trigger: pig_unclean]` `[factor_trigger: dream_pig AND dream_unclean]` `[role: 警告]` A pig is universally unclean—in Scripture there is no positive interpretation. A vision speaks of an unclean spirit. → 猪普遍是不洁的——圣经中没有正面解释。看见猪象征污秽的灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Pig 猪/不洁"
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
        l1_anchor="dvd_v1.0.0_pig_猪_不洁_001_L1",
    )
    version: str = "1.0.0"
