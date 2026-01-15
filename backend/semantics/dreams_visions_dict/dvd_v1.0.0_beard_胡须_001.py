"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424517
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
    semantic_id="dvd_v1.0.0_beard_胡须_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Beard胡须(SemanticEntry):
    """
    ### Source Text

> Beard = appearance to others. **Positive**: Long beard = strength, favor. Shaved ...
    """
    
    original_text: str = """### Source Text

> Beard = appearance to others. **Positive**: Long beard = strength, favor. Shaved = new face. **Negative**: Woman with beard = losing femininity. Beard shaved off = disgrace (2 Sam 10:5).

### English Paraphrase

Beard = public image. **Positive**: Long = favor. **Negative**: Shaved = disgrace. Woman = wrong identity.

### Chinese Interpretation（完整对等诠释）

胡须 = 公众形象。**正面**：长 = 恩惠。**负面**：剃光 = 羞辱。女人 = 错误身份。

### Narrative Snippets

- `[ns_dav_b029]` `[trigger: 梦胡须]` `[factor_trigger: dream_symbol_beard]` `[role: 主干]` Beard = public image—long = favor, shaved = disgrace or new face. → Dreams Dictionary #Beard"""
    normalized_text_zh: str = """"""
    subject: str = "Beard 胡须"
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
        l1_anchor="dvd_v1.0.0_beard_胡须_001_L1",
    )
    version: str = "1.0.0"
