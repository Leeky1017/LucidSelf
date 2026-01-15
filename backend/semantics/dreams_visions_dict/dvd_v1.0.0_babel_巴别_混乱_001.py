"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424228
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
    semantic_id="dvd_v1.0.0_babel_巴别_混乱_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Babel巴别混乱(SemanticEntry):
    """
    ### Source Text

> **Strong's 894**: Babel or Babylon = "confusion (by mixing)"

Babel has no positi...
    """
    
    original_text: str = """### Source Text

> **Strong's 894**: Babel or Babylon = "confusion (by mixing)"

Babel has no positive connotation. It is the tower of confusion—ministries making a name using external strength, not the spirit of God.

### English Paraphrase

Babel = confusion, mixing. **Always negative**. Tower of Babel = status quo church, ministries using external/natural strength rather than Spirit of God.

### Chinese Interpretation（完整对等诠释）

巴别 = 混乱、混杂。**始终负面**。巴别塔 = 墨守成规的教会，用世俗方法而非神的灵兴起的事工。

### Narrative Snippets

- `[ns_dav_b001]` `[trigger: 梦巴别]` `[factor_trigger: dream_symbol_babel]` `[role: 主干]` Babel = confusion, ministries using external strength—always negative. → Dreams Dictionary #Babel"""
    normalized_text_zh: str = """"""
    subject: str = "Babel 巴别/混乱"
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
        l1_anchor="dvd_v1.0.0_babel_巴别_混乱_001_L1",
    )
    version: str = "1.0.0"
