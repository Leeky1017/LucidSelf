"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419843
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
    semantic_id="dvd_v1.0.0_cocoon_茧_转变_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cocoon茧转变(SemanticEntry):
    """
    ### Source Text

> **Cocoon**: A picture of transition and transformation. Something beautiful is be...
    """
    
    original_text: str = """### Source Text

> **Cocoon**: A picture of transition and transformation. Something beautiful is being formed within.
> The cocoon is the place where a caterpillar transforms into a butterfly. In dreams and visions, it represents a season of hidden growth and preparation.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cocoon | 茧 | 转变的场所 |
| Transformation | 转变 | 从旧到新 |
| Hidden growth | 隐藏的成长 | 外面看不见的改变 |
| Preparation | 预备 | 为出现做准备 |

### English Paraphrase

A cocoon represents transition and transformation—a place where something beautiful is being formed within. It is a season of hidden growth and preparation, where you may feel restricted but are being transformed for greater things.

### Chinese Interpretation

茧代表过渡和转变——一个美丽事物正在其中形成的地方。这是隐藏成长和预备的季节，你可能感到受限，但正在被转变以迎接更大的事物。

### Core Points

1. **通常正面**: 代表美好的转变
2. **隐藏季节**: 外面看不见内在的改变
3. **受限必要**: 暂时的限制是为了更大的自由
4. **蝴蝶预兆**: 荣耀即将显现

### Narrative Snippets

- `[ns_dav_c036]` `[trigger: cocoon_transform]` `[factor_trigger: dream_cocoon AND dream_transform]` `[role: 主干]` A cocoon represents transition and transformation—something beautiful is being formed within you. → 茧代表过渡和转变——美丽的事物正在你里面形成。"""
    normalized_text_zh: str = """"""
    subject: str = "Cocoon 茧/转变"
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
        l1_anchor="dvd_v1.0.0_cocoon_茧_转变_001_L1",
    )
    version: str = "1.0.0"
