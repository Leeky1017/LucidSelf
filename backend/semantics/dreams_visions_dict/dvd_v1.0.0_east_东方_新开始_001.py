"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.409502
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
    semantic_id="dvd_v1.0.0_east_东方_新开始_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class East东方新开始(SemanticEntry):
    """
    ### Source Text

> **East**: The place of new beginnings. The sun rises in the east—a new start to l...
    """
    
    original_text: str = """### Source Text

> **East**: The place of new beginnings. The sun rises in the east—a new start to life.
> Genesis 2:8 "And the LORD God planted a garden eastward in Eden; and there he put the man whom he had formed."
> Matthew 2:1 "...there came wise men from the east to Jerusalem."
> Negative: The east is also the direction of the enemy's attack—the nations that attacked Israel came from the east.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| East | 东方 | 新开始 |
| Sunrise | 日出 | 新的一天 |
| Eden | 伊甸 | 神的起初计划 |
| Attack | 攻击 | 仇敌的方向 |

### English Paraphrase

East represents new beginnings—the sun rises there, starting a new day. The garden of Eden was planted in the east. The wise men came from the east seeking Jesus. Negatively, attacking nations came from the east, so it can represent enemy attack.

### Chinese Interpretation

东方代表新的开始——太阳从那里升起，开始新的一天。伊甸园种在东方。博士从东方来寻找耶稣。负面而言，攻击的列国从东方来，所以它可能代表仇敌的攻击。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **新开始**: 太阳升起的方向
3. **伊甸记号**: 神起初的计划
4. **攻击方向**: 仇敌可能从东方来

### Narrative Snippets

- `[ns_dav_e009]` `[trigger: east_newbeginning]` `[factor_trigger: dream_east AND dream_beginning]` `[role: 主干]` East represents the place of new beginnings—the sun rises there, starting a new day and season. → 东方代表新开始的地方——太阳从那里升起，开始新的一天和季节。
- `[ns_dav_e010]` `[trigger: east_attack]` `[factor_trigger: dream_east AND dream_attack]` `[role: 警告]` The east is also the direction of enemy attack—nations that attacked Israel came from the east. → 东方也是仇敌攻击的方向——攻击以色列的列国从东方来。"""
    normalized_text_zh: str = """"""
    subject: str = "East 东方/新开始"
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
        l1_anchor="dvd_v1.0.0_east_东方_新开始_001_L1",
    )
    version: str = "1.0.0"
