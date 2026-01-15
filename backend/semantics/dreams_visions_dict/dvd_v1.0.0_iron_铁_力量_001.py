"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429265
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
    semantic_id="dvd_v1.0.0_iron_铁_力量_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Iron铁力量(SemanticEntry):
    """
    ### Source Text

> **Iron**: A picture of strength or oppression, depending on context.
> Hot Iron: ...
    """
    
    original_text: str = """### Source Text

> **Iron**: A picture of strength or oppression, depending on context.
> Hot Iron: Being seared means being marked and set in stone.
> Rod of Iron: Leadership that is strict and strong.
> Positive: Iron sharpens iron—those the Lord put in your life to bring pressure to your weaknesses.
> Negative: Iron weapons speak of the attack of the enemy. Chariots of iron represent enemies to fear.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Iron | 铁 | 力量或压迫 |
| Seared | 烙印 | 被标记 |
| Rod | 杖 | 严格的领导 |
| Sharpen | 磨砺 | 彼此造就 |

### English Paraphrase

Iron represents strength or oppression depending on context. Hot iron means being marked. A rod of iron speaks of strict leadership. Iron sharpens iron—people who pressure your weaknesses. Iron weapons speak of enemy attack.

### Chinese Interpretation

铁代表力量或压迫，取决于上下文。热铁意味着被标记。铁杖象征严格的领导。铁磨铁——那些施压于你弱点的人。铁器象征仇敌的攻击。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **力量象征**: 坚强和刚硬
3. **磨砺造就**: 铁磨铁彼此造就
4. **攻击警告**: 铁器是仇敌的武器

### Narrative Snippets

- `[ns_dav_i010]` `[trigger: iron_sharpen]` `[factor_trigger: dream_iron AND dream_sharpen]` `[role: 主干]` Iron sharpens iron—the Lord uses people to bring pressure to your weaknesses for your growth. → 铁磨铁——主使用人施压于你的弱点使你成长。
- `[ns_dav_i011]` `[trigger: iron_weapon]` `[factor_trigger: dream_iron AND dream_attack]` `[role: 警告]` Iron weapons being thrown at you speaks of the attack of the enemy. → 铁器被投向你象征仇敌的攻击。"""
    normalized_text_zh: str = """"""
    subject: str = "Iron 铁/力量"
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
        l1_anchor="dvd_v1.0.0_iron_铁_力量_001_L1",
    )
    version: str = "1.0.0"
