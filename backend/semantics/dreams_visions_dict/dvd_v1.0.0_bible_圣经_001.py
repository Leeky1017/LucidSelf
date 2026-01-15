"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424569
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
    semantic_id="dvd_v1.0.0_bible_圣经_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bible圣经(SemanticEntry):
    """
    ### Source Text

> Bible = Word and Covenant. **Positive**: Foundation, eat the Word. **Negative**: ...
    """
    
    original_text: str = """### Source Text

> Bible = Word and Covenant. **Positive**: Foundation, eat the Word. **Negative**: Old family bible = generational curse, ungodly religious spirit (Gal 3:10).

### English Paraphrase

Bible = Word, covenant. **Positive**: Foundation. **Negative**: Old family bible = generational curse.

### Chinese Interpretation（完整对等诠释）

圣经 = 话语、盟约。**正面**：根基。**负面**：旧家庭圣经 = 世代咒诅。

### Narrative Snippets

- `[ns_dav_b033]` `[trigger: 梦圣经]` `[factor_trigger: dream_symbol_bible]` `[role: 主干]` Bible = Word/covenant—foundation or generational curse. → Dreams Dictionary #Bible"""
    normalized_text_zh: str = """"""
    subject: str = "Bible 圣经"
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
        l1_anchor="dvd_v1.0.0_bible_圣经_001_L1",
    )
    version: str = "1.0.0"
