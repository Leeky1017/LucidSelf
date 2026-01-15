"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424409
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
    semantic_id="dvd_v1.0.0_bars_铁栏_金条_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bars铁栏金条(SemanticEntry):
    """
    ### Source Text

> Bars = context-dependent. Prison bar = bondage. Gold bar = anointing, provision. ...
    """
    
    original_text: str = """### Source Text

> Bars = context-dependent. Prison bar = bondage. Gold bar = anointing, provision. **Positive**: Enemy behind bars = can't touch you. **Negative**: Self behind bars = bondage (Isa 61:1).

### English Paraphrase

Bars = depends on type. Prison = bondage. Gold = provision. Enemy behind = protection.

### Chinese Interpretation（完整对等诠释）

铁栏 = 取决于类型。监狱 = 捆绑。金条 = 供应。仇敌在后 = 保护。

### Narrative Snippets

- `[ns_dav_b022]` `[trigger: 梦铁栏]` `[factor_trigger: dream_symbol_bars]` `[role: 主干]` Bars = bondage or protection depending on who is behind. → Dreams Dictionary #Bars"""
    normalized_text_zh: str = """"""
    subject: str = "Bars 铁栏/金条"
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
        l1_anchor="dvd_v1.0.0_bars_铁栏_金条_001_L1",
    )
    version: str = "1.0.0"
