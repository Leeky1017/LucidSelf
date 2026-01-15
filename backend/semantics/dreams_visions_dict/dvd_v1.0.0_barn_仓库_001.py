"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424384
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
    semantic_id="dvd_v1.0.0_barn_仓库_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Barn仓库(SemanticEntry):
    """
    ### Source Text

> Barn = God's storehouse, provision, wealth. **Positive**: Full barn = blessing (D...
    """
    
    original_text: str = """### Source Text

> Barn = God's storehouse, provision, wealth. **Positive**: Full barn = blessing (Deut 28:8; Prov 3:10). Heavenly storehouse overflowing. **Negative**: Empty/robbed = theft, curse (Joel 1:17).

### English Paraphrase

Barn = storehouse. **Positive**: Full = blessing. **Negative**: Empty/robbed = curse.

### Chinese Interpretation（完整对等诠释）

仓库 = 仓房。**正面**：满 = 祝福。**负面**：空/被抢 = 咒诅。

### Narrative Snippets

- `[ns_dav_b019]` `[trigger: 梦仓库]` `[factor_trigger: dream_symbol_barn]` `[role: 主干]` Barn = God's storehouse—full = blessing, empty = curse. → Dreams Dictionary #Barn"""
    normalized_text_zh: str = """"""
    subject: str = "Barn 仓库"
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
        l1_anchor="dvd_v1.0.0_barn_仓库_001_L1",
    )
    version: str = "1.0.0"
