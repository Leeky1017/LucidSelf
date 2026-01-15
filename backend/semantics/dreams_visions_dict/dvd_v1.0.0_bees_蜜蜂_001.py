"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424557
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
    semantic_id="dvd_v1.0.0_bees_蜜蜂_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bees蜜蜂(SemanticEntry):
    """
    ### Source Text

> Bees = **Positive**: Blessing, honey, provision (Judg 14:8). **Negative**: Swarm ...
    """
    
    original_text: str = """### Source Text

> Bees = **Positive**: Blessing, honey, provision (Judg 14:8). **Negative**: Swarm = attack, pain from all directions (Ps 118:12; Deut 1:44).

### English Paraphrase

Bees = **Positive**: Honey, provision. **Negative**: Swarm = attack, discouragement.

### Chinese Interpretation（完整对等诠释）

蜜蜂 = **正面**：蜂蜜、供应。**负面**：蜂群 = 攻击、气馁。

### Narrative Snippets

- `[ns_dav_b032]` `[trigger: 梦蜜蜂]` `[factor_trigger: dream_symbol_bees]` `[role: 主干]` Bees = provision or attack—honey = blessing, swarm = pain. → Dreams Dictionary #Bees"""
    normalized_text_zh: str = """"""
    subject: str = "Bees 蜜蜂"
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
        l1_anchor="dvd_v1.0.0_bees_蜜蜂_001_L1",
    )
    version: str = "1.0.0"
