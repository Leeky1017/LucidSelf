"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.401969
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
    semantic_id="dvd_v1.0.0_darts_飞镖_攻击_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Darts飞镖攻击(SemanticEntry):
    """
    ### Source Text

> **Darts**: A picture of spiritual attack usually coming through words spoken agai...
    """
    
    original_text: str = """### Source Text

> **Darts**: A picture of spiritual attack usually coming through words spoken against you.
> The dart comes from the enemy and destroys. Darts usually contained poison—although small, the poison caused death. Darts to the heart can speak of hurts inflicted by others in your past. The poison of rejection remains, unhealed.
> Ephesians 6:16 "...taking the shield of faith, with which you shall be able to quench all the fiery darts of the wicked one."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Darts | 飞镖 | 属灵攻击 |
| Poison | 毒素 | 留在心中的伤害 |
| Attack | 攻击 | 通过言语来的 |
| Shield | 盾牌 | 信心的保护 |

### English Paraphrase

Darts represent spiritual attack, usually through negative words spoken against you. Like the dagger, darts are deadly—the poison causes harm. Darts to the heart speak of past hurts and rejection. The shield of faith quenches these fiery darts.

### Chinese Interpretation

飞镖代表属灵攻击，通常通过针对你的负面言语。像匕首一样，飞镖是致命的——毒素造成伤害。刺入心脏的飞镖象征过去的伤害和拒绝。信心的盾牌能熄灭这些火箭。

### Core Points

1. **始终负面**: 飞镖代表仇敌的攻击
2. **言语攻击**: 通过话语来的咒诅
3. **过去伤害**: 未愈合的拒绝之伤
4. **信心防护**: 用信心盾牌抵挡

### Narrative Snippets

- `[ns_dav_d006]` `[trigger: darts_attack]` `[factor_trigger: dream_darts AND dream_attack]` `[role: 主干]` Darts represent spiritual attack through negative words—the poison of rejection remains unhealed. → 飞镖象征通过负面言语的属灵攻击——拒绝的毒素留下未愈的伤。
- `[ns_dav_d007]` `[trigger: darts_defense]` `[factor_trigger: dream_darts AND dream_shield]` `[role: 解决]` The shield of faith quenches all the fiery darts of the wicked one. → 信心的盾牌熄灭恶者一切的火箭。"""
    normalized_text_zh: str = """"""
    subject: str = "Darts 飞镖/攻击"
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
        l1_anchor="dvd_v1.0.0_darts_飞镖_攻击_001_L1",
    )
    version: str = "1.0.0"
