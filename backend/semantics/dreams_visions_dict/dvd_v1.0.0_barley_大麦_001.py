"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424377
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
    semantic_id="dvd_v1.0.0_barley_大麦_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Barley大麦(SemanticEntry):
    """
    ### Source Text

> Barley = basic needs, daily bread. Cheaper than wheat, more resilient. **Positive...
    """
    
    original_text: str = """### Source Text

> Barley = basic needs, daily bread. Cheaper than wheat, more resilient. **Positive**: Daily needs met (Ruth 3:17). **Negative**: Spoiled/stolen = curse (Exod 9:31).

### English Paraphrase

Barley = basic provision. **Positive**: Daily needs met. **Negative**: Spoiled = financial curse.

### Chinese Interpretation（完整对等诠释）

大麦 = 基本供应。**正面**：日常需求满足。**负面**：变质 = 财务咒诅。

### Narrative Snippets

- `[ns_dav_b018]` `[trigger: 梦大麦]` `[factor_trigger: dream_symbol_barley]` `[role: 主干]` Barley = basic daily needs—receiving = met, spoiled = curse. → Dreams Dictionary #Barley"""
    normalized_text_zh: str = """"""
    subject: str = "Barley 大麦"
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
        l1_anchor="dvd_v1.0.0_barley_大麦_001_L1",
    )
    version: str = "1.0.0"
