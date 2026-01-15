"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424318
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
    semantic_id="dvd_v1.0.0_baldness_秃头_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Baldness秃头(SemanticEntry):
    """
    ### Source Text

> Baldness = seldom positive. Humiliation, exposure. Woman bald = not under coverin...
    """
    
    original_text: str = """### Source Text

> Baldness = seldom positive. Humiliation, exposure. Woman bald = not under covering (1 Cor 11:15). Man bald = exposed, vulnerable.

### English Paraphrase

Baldness = humiliation. **Negative**: Woman = no covering. Man = exposed, vulnerable.

### Chinese Interpretation（完整对等诠释）

秃头 = 羞辱。**负面**：女人 = 无遮盖。男人 = 暴露、脆弱。

### Narrative Snippets

- `[ns_dav_b011]` `[trigger: 梦秃头]` `[factor_trigger: dream_symbol_baldness]` `[role: 主干]` Baldness = humiliation and exposure—seldom positive. → Dreams Dictionary #Baldness"""
    normalized_text_zh: str = """"""
    subject: str = "Baldness 秃头"
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
        l1_anchor="dvd_v1.0.0_baldness_秃头_001_L1",
    )
    version: str = "1.0.0"
