"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412214
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
    semantic_id="dvd_v1.0.0_flying_飞翔_超越_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Flying飞翔超越(SemanticEntry):
    """
    ### Source Text

> **Flying**: A picture of rising above circumstances in the spirit. Also speaks of...
    """
    
    original_text: str = """### Source Text

> **Flying**: A picture of rising above circumstances in the spirit. Also speaks of freedom and the prophetic.
> Positive: Flying speaks of moving in the spirit—above natural limitations. Eagles fly, prophets see from above.
> Negative: Flying that is out of control indicates the enemy's influence or operating in the flesh rather than Spirit.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Flying | 飞翔 | 超越和自由 |
| Spirit | 灵 | 在灵里运行 |
| Freedom | 自由 | 超越限制 |
| Prophetic | 先知的 | 从上面看 |

### English Paraphrase

Flying represents rising above circumstances in the spirit—freedom and the prophetic. Flying speaks of moving above natural limitations. Negative flying that is out of control indicates enemy influence or operating in flesh rather than Spirit.

### Chinese Interpretation

飞翔代表在灵里超越环境——自由和先知性。飞翔象征超越自然限制的运动。负面的失控飞翔表示仇敌的影响或靠肉体而非靠圣灵运作。

### Core Points

1. **正负皆可**: 飞翔方式决定含义
2. **超越环境**: 在灵里高升
3. **先知眼光**: 从上面看全局
4. **失控警告**: 可能表示肉体操作

### Narrative Snippets

- `[ns_dav_f018]` `[trigger: flying_spirit]` `[factor_trigger: dream_flying AND dream_transcendence]` `[role: 主干]` Flying speaks of rising above circumstances in the spirit—moving above natural limitations. → 飞翔象征在灵里超越环境——超越自然的限制运动。"""
    normalized_text_zh: str = """"""
    subject: str = "Flying 飞翔/超越"
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
        l1_anchor="dvd_v1.0.0_flying_飞翔_超越_001_L1",
    )
    version: str = "1.0.0"
