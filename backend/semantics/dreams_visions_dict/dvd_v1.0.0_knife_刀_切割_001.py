"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429333
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
    semantic_id="dvd_v1.0.0_knife_刀_切割_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Knife刀切割(SemanticEntry):
    """
    ### Source Text

> **Knife**: A knife is an implement for dividing or cutting. It can be positive or...
    """
    
    original_text: str = """### Source Text

> **Knife**: A knife is an implement for dividing or cutting. It can be positive or negative depending on context.
> Positive: The Lord taking a knife to an infested wound—applying the cross to rid hindrances, bringing healing. Joshua applied the knife to Israelites before entering the Promised Land.
> Negative: A weapon bringing pain—enemy bringing destruction.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Knife | 刀 | 分开和切割 |
| Cross | 十字架 | 主的对付 |
| Healing | 医治 | 通过切割得医治 |
| Destruction | 毁灭 | 仇敌的武器 |

### English Paraphrase

A knife divides or cuts—positive or negative depending on context. The Lord applying a knife to wounds brings healing by removing hindrances. Joshua circumcised Israel before the Promised Land. Negatively, a knife is a weapon of pain and the enemy's destruction.

### Chinese Interpretation

刀分开或切割——正负取决于上下文。主用刀处理伤口，通过除去阻碍带来医治。约书亚在进入应许之地前给以色列人行割礼。负面而言，刀是痛苦的武器和仇敌的毁灭。

### Core Points

1. **正负皆可**: 使用者决定含义
2. **十架对付**: 主用刀除去阻碍
3. **医治过程**: 虽痛苦但带来医治
4. **攻击警告**: 可能是仇敌的武器

### Narrative Snippets

- `[ns_dav_j007]` `[trigger: knife_cross]` `[factor_trigger: dream_knife AND dream_healing]` `[role: 主干]` The Lord applying a knife to wounds brings healing—removing things that hinder you. → 主用刀处理伤口带来医治——除去阻碍你的事物。
- `[ns_dav_j008]` `[trigger: knife_enemy]` `[factor_trigger: dream_knife AND dream_destruction]` `[role: 警告]` A knife as a weapon speaks of the enemy bringing destruction and pain. → 刀作为武器象征仇敌带来毁灭和痛苦。"""
    normalized_text_zh: str = """"""
    subject: str = "Knife 刀/切割"
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
        l1_anchor="dvd_v1.0.0_knife_刀_切割_001_L1",
    )
    version: str = "1.0.0"
