"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424417
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
    semantic_id="dvd_v1.0.0_basement_地下室_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Basement地下室(SemanticEntry):
    """
    ### Source Text

> Basement = going lower, humbling. **Positive**: Promotion begins at basement (2 C...
    """
    
    original_text: str = """### Source Text

> Basement = going lower, humbling. **Positive**: Promotion begins at basement (2 Chron 18:24). **Negative**: Trapped = bondage, hindered from rising.

### English Paraphrase

Basement = humbling. **Positive**: Promotion starts here. **Negative**: Trapped = bondage.

### Chinese Interpretation（完整对等诠释）

地下室 = 谦卑。**正面**：晋升从这里开始。**负面**：被困 = 捆绑。

### Narrative Snippets

- `[ns_dav_b023]` `[trigger: 梦地下室]` `[factor_trigger: dream_symbol_basement]` `[role: 主干]` Basement = humbling—promotion begins here, or trapped = bondage. → Dreams Dictionary #Basement"""
    normalized_text_zh: str = """"""
    subject: str = "Basement 地下室"
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
        l1_anchor="dvd_v1.0.0_basement_地下室_001_L1",
    )
    version: str = "1.0.0"
