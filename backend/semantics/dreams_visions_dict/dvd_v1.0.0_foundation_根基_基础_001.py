"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412231
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
    semantic_id="dvd_v1.0.0_foundation_根基_基础_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Foundation根基基础(SemanticEntry):
    """
    ### Source Text

> **Foundation**: A picture of what your life or ministry is built upon.
> Positive...
    """
    
    original_text: str = """### Source Text

> **Foundation**: A picture of what your life or ministry is built upon.
> Positive: A solid foundation speaks of being built on Christ and His Word. Foundation being laid indicates new beginnings.
> Negative: A cracked foundation indicates problems at the core. Building without foundation leads to collapse.
> 1 Corinthians 3:11 "For other foundation can no man lay than that is laid, which is Jesus Christ."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Foundation | 根基 | 生命的基础 |
| Solid | 坚固 | 建在磐石上 |
| Christ | 基督 | 唯一的根基 |
| Crack | 裂缝 | 核心问题 |

### English Paraphrase

Foundation represents what your life or ministry is built upon. A solid foundation speaks of being built on Christ and His Word. Foundation being laid indicates new beginnings. A cracked foundation indicates core problems. Building without foundation leads to collapse.

### Chinese Interpretation

根基代表你的生命或事工建立在什么之上。坚固的根基象征建立在基督和祂的话语上。根基被奠定表示新的开始。有裂缝的根基表示核心问题。没有根基的建造导致倒塌。

### Core Points

1. **正负皆可**: 根基状态决定含义
2. **基督唯一**: 没有别的根基
3. **新开始**: 奠基代表新事物
4. **裂缝警告**: 核心问题需要处理

### Narrative Snippets

- `[ns_dav_f020]` `[trigger: foundation_christ]` `[factor_trigger: dream_foundation AND dream_christ]` `[role: 主干]` No other foundation can be laid than Jesus Christ—build your life on Him alone. → 那已经立好的根基就是耶稣基督——单单将你的生命建立在祂上面。"""
    normalized_text_zh: str = """"""
    subject: str = "Foundation 根基/基础"
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
        l1_anchor="dvd_v1.0.0_foundation_根基_基础_001_L1",
    )
    version: str = "1.0.0"
