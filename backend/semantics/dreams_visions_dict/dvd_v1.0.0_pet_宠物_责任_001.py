"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405266
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
    semantic_id="dvd_v1.0.0_pet_宠物_责任_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Pet宠物责任(SemanticEntry):
    """
    ### Source Text

> **Pet**: Because pets are different for each person, interpretation changes accor...
    """
    
    original_text: str = """### Source Text

> **Pet**: Because pets are different for each person, interpretation changes according to your relationship with the animal. If you dream of a pet you love, it speaks of responsibilities or dear things. If pets have replaced children, they could represent ministry aspects.
> Negative: Dreaming of someone else's pet or an animal you don't like speaks of irritation or enemy's work.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Pet | 宠物 | 责任和珍爱 |
| Responsibility | 责任 | 需要照顾的 |
| Ministry | 事工 | 属灵的工作 |
| Irritation | 烦扰 | 仇敌的工作 |

### English Paraphrase

Pet interpretation depends on your relationship with the animal. A beloved pet speaks of responsibilities or dear things. If pets replaced children, they may represent ministry. Others' pets or disliked animals speak of irritation or enemy's work.

### Chinese Interpretation

宠物的解释取决于你与动物的关系。心爱的宠物象征责任或珍贵的东西。如果宠物代替了孩子，它们可能代表事工。别人的宠物或不喜欢的动物象征烦扰或仇敌的工作。

### Core Points

1. **正负皆可**: 关系决定含义
2. **责任象征**: 需要照顾的事物
3. **事工代表**: 可能是属灵工作
4. **烦扰警告**: 可能是仇敌工作

### Narrative Snippets

- `[ns_dav_p007]` `[trigger: pet_care]` `[factor_trigger: dream_pet AND dream_responsibility]` `[role: 主干]` A beloved pet speaks of your responsibilities or things that are dear to you. → 心爱的宠物象征你的责任或你珍视的东西。"""
    normalized_text_zh: str = """"""
    subject: str = "Pet 宠物/责任"
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
        l1_anchor="dvd_v1.0.0_pet_宠物_责任_001_L1",
    )
    version: str = "1.0.0"
