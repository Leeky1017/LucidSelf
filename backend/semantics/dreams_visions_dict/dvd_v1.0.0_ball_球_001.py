"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424326
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
    semantic_id="dvd_v1.0.0_ball_球_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ball球(SemanticEntry):
    """
    ### Source Text

> Ball = childhood toy. **Positive**: Joy, fun. **Negative**: Tossed to and fro = n...
    """
    
    original_text: str = """### Source Text

> Ball = childhood toy. **Positive**: Joy, fun. **Negative**: Tossed to and fro = no foundation, confusion (Isa 22:18).

### English Paraphrase

Ball = childhood. **Positive**: Joy. **Negative**: Tossed = no foundation, enemy buffeting.

### Chinese Interpretation（完整对等诠释）

球 = 童年。**正面**：快乐。**负面**：被抛 = 无根基，仇敌攻击。

### Narrative Snippets

- `[ns_dav_b012]` `[trigger: 梦球]` `[factor_trigger: dream_symbol_ball]` `[role: 主干]` Ball = childhood joy or being tossed—positive = fun, negative = no foundation. → Dreams Dictionary #Ball"""
    normalized_text_zh: str = """"""
    subject: str = "Ball 球"
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
        l1_anchor="dvd_v1.0.0_ball_球_001_L1",
    )
    version: str = "1.0.0"
