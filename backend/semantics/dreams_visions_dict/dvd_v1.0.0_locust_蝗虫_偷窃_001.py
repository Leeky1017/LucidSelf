"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443981
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
    semantic_id="dvd_v1.0.0_locust_蝗虫_偷窃_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Locust蝗虫偷窃(SemanticEntry):
    """
    ### Source Text

> **Locust**: If positive, a picture of your basic needs being provided for (Israel...
    """
    
    original_text: str = """### Source Text

> **Locust**: If positive, a picture of your basic needs being provided for (Israelites could eat locusts). Negatively, they speak of a spirit of theft—devouring crops and leaving only dust.
> Negative: If you have seen the Lord provide, only to see provision eaten up by circumstances, this is a clear indication of a curse in your life.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Locust | 蝗虫 | 偷窃或供应 |
| Provision | 供应 | 基本需要 |
| Theft | 偷窃 | 仇敌的工作 |
| Devour | 吞噬 | 吃光一切 |

### English Paraphrase

Locusts can positively represent basic needs being met (as food for Israelites). Negatively, they represent a spirit of theft—devouring provision and leaving dust. If provision is eaten up by unexpected circumstances, it indicates a curse.

### Chinese Interpretation

蝗虫可以正面代表基本需要被供应（作为以色列人的食物）。负面而言，它们代表偷窃的灵——吞噬供应只留下灰尘。如果供应被意外情况吃掉，表明有咒诅。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **供应象征**: 可代表基本需要
3. **偷窃的灵**: 吞噬祝福的仇敌
4. **咒诅警告**: 供应被吃掉是咒诅

### Narrative Snippets

- `[ns_dav_l013]` `[trigger: locust_theft]` `[factor_trigger: dream_locust AND dream_theft]` `[role: 警告]` Locusts represent a spirit of theft—devouring provision and leaving only dust behind. → 蝗虫代表偷窃的灵——吞噬供应只留下灰尘。
- `[ns_dav_l014]` `[trigger: locust_curse]` `[factor_trigger: dream_locust AND dream_curse]` `[role: 警告]` If provision is eaten up by unexpected circumstances, it indicates a curse in your life. → 如果供应被意外情况吃掉，表明你生命中有咒诅。"""
    normalized_text_zh: str = """"""
    subject: str = "Locust 蝗虫/偷窃"
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
        l1_anchor="dvd_v1.0.0_locust_蝗虫_偷窃_001_L1",
    )
    version: str = "1.0.0"
