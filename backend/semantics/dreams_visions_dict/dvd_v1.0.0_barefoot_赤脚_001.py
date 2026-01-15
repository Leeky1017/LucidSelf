"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424368
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
    semantic_id="dvd_v1.0.0_barefoot_赤脚_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Barefoot赤脚(SemanticEntry):
    """
    ### Source Text

> Barefoot = vulnerability, servanthood. **Positive**: Humility, transparency, serv...
    """
    
    original_text: str = """### Source Text

> Barefoot = vulnerability, servanthood. **Positive**: Humility, transparency, servant. **Negative**: Exposed, unprotected, lacking spiritual armor (Eph 6:15).

### English Paraphrase

Barefoot = vulnerability. **Positive**: Humility. **Negative**: Unprotected, lacking gospel of peace.

### Chinese Interpretation（完整对等诠释）

赤脚 = 脆弱。**正面**：谦卑。**负面**：无保护，缺乏平安福音。

### Narrative Snippets

- `[ns_dav_b017]` `[trigger: 梦赤脚]` `[factor_trigger: dream_symbol_barefoot]` `[role: 主干]` Barefoot = vulnerability—humility or lacking armor. → Dreams Dictionary #Barefoot"""
    normalized_text_zh: str = """"""
    subject: str = "Barefoot 赤脚"
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
        l1_anchor="dvd_v1.0.0_barefoot_赤脚_001_L1",
    )
    version: str = "1.0.0"
