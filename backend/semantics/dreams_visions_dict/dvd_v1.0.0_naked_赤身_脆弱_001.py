"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433348
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
    semantic_id="dvd_v1.0.0_naked_赤身_脆弱_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Naked赤身脆弱(SemanticEntry):
    """
    ### Source Text

> **Naked-Nakedness**: Nakedness in dreams and visions speaks of being vulnerable a...
    """
    
    original_text: str = """### Source Text

> **Naked-Nakedness**: Nakedness in dreams and visions speaks of being vulnerable and exposed. If you are naked and comfortable with it, you are transparent with nothing to hide. If you are uncomfortable, you feel exposed and overwhelmed.
> Positive: The Lord stripping you first before giving you new blessing—allowing yourself to be naked before Him for healing.
> Negative: Nakedness spoke of shame in Scripture—hurts endured that still plague you today.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Naked | 赤身 | 脆弱和暴露 |
| Vulnerable | 脆弱 | 容易受伤的 |
| Transparent | 透明 | 没有隐藏 |
| Shame | 羞耻 | 过去的伤害 |

### English Paraphrase

Nakedness speaks of being vulnerable and exposed. If comfortable, you are transparent with nothing to hide. If uncomfortable, you feel exposed and overwhelmed. The Lord may strip you before giving new blessing. Being naked before Him allows healing. In Scripture, nakedness spoke of shame from past hurts.

### Chinese Interpretation

赤身象征脆弱和暴露。如果舒适，你是透明的没有隐藏。如果不舒适，你感到暴露和不知所措。主可能先剥去你再给新的祝福。在祂面前赤身允许医治。在圣经中，赤身象征过去伤害的羞耻。

### Core Points

1. **正负皆可**: 感受决定含义
2. **脆弱象征**: 暴露和敞开
3. **医治过程**: 在主面前赤露
4. **羞耻警告**: 可能是过去的伤害

### Narrative Snippets

- `[ns_dav_n001]` `[trigger: naked_transparent]` `[factor_trigger: dream_naked AND dream_transparent]` `[role: 主干]` If comfortable being naked, you are transparent with nothing to hide—a positive sign. → 如果赤身时感到舒适，你是透明的没有隐藏——这是正面的迹象。
- `[ns_dav_n002]` `[trigger: naked_shame]` `[factor_trigger: dream_naked AND dream_shame]` `[role: 警告]` Nakedness in Scripture spoke of shame—hurts endured that still plague you today. → 圣经中的赤身象征羞耻——至今仍困扰你的过去伤害。"""
    normalized_text_zh: str = """"""
    subject: str = "Naked 赤身/脆弱"
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
        l1_anchor="dvd_v1.0.0_naked_赤身_脆弱_001_L1",
    )
    version: str = "1.0.0"
