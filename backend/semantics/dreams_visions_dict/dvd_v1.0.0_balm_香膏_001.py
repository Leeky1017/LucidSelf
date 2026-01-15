"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424333
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
    semantic_id="dvd_v1.0.0_balm_香膏_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Balm香膏(SemanticEntry):
    """
    ### Source Text

> Balm = healing ointment. **Positive**: Holy Spirit healing hurts (Jer 51:8). **Ne...
    """
    
    original_text: str = """### Source Text

> Balm = healing ointment. **Positive**: Holy Spirit healing hurts (Jer 51:8). **Negative**: Fly in balm = ruined medicine (Eccl 10:1).

### English Paraphrase

Balm = healing. **Positive**: Spirit healing. **Negative**: Fly = contaminated, brings harm.

### Chinese Interpretation（完整对等诠释）

香膏 = 医治。**正面**：圣灵医治。**负面**：苍蝇 = 污染，反而带来伤害。

### Narrative Snippets

- `[ns_dav_b013]` `[trigger: 梦香膏]` `[factor_trigger: dream_symbol_balm]` `[role: 主干]` Balm = healing ointment—pure = healing, spoiled = contamination. → Dreams Dictionary #Balm"""
    normalized_text_zh: str = """"""
    subject: str = "Balm 香膏"
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
        l1_anchor="dvd_v1.0.0_balm_香膏_001_L1",
    )
    version: str = "1.0.0"
