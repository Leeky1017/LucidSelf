"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419784
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
    semantic_id="dvd_v1.0.0_church_教会_属灵家_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Church教会属灵家(SemanticEntry):
    """
    ### Source Text

> **Church**: The body of Christ, the local church, or refers to the church system ...
    """
    
    original_text: str = """### Source Text

> **Church**: The body of Christ, the local church, or refers to the church system as a whole.
> The church in your dreams could represent your spiritual home. If the church is lit up and alive, it speaks of a thriving spiritual community. If it is dark or empty, it speaks of spiritual deadness.
> 1 Corinthians 12:27 "Now you are the body of Christ, and members in particular."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Church | 教会 | 基督的身体 |
| Body of Christ | 基督的身体 | 信徒的集合 |
| Spiritual home | 属灵的家 | 归属的地方 |
| System | 体制 | 宗教组织结构 |

### English Paraphrase

Church represents the body of Christ, your local church, or the church system as a whole. A lit and alive church speaks of thriving spiritual community. A dark or empty church speaks of spiritual deadness or a dead religious system.

### Chinese Interpretation

教会代表基督的身体、你的本地教会或整个教会体制。明亮活泼的教会象征繁荣的属灵团体。黑暗或空荡的教会象征属灵死寂或死掉的宗教体制。

### Core Points

1. **正负皆可**: 教会状态决定含义
2. **归属象征**: 你的属灵家和归属感
3. **体制警告**: 可能代表死掉的宗教体制
4. **生命指标**: 光明vs黑暗显示灵性状态

### Narrative Snippets

- `[ns_dav_c026]` `[trigger: church_alive]` `[factor_trigger: dream_church AND dream_alive]` `[role: 正面]` A church lit up and alive speaks of a thriving spiritual community and healthy spiritual home. → 明亮活泼的教会象征繁荣的属灵团体和健康的属灵家。
- `[ns_dav_c027]` `[trigger: church_dead]` `[factor_trigger: dream_church AND dream_dead]` `[role: 警告]` A dark or empty church speaks of spiritual deadness or a dead religious system. → 黑暗或空荡的教会象征属灵死寂或死掉的宗教体制。"""
    normalized_text_zh: str = """"""
    subject: str = "Church 教会/属灵家"
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
        l1_anchor="dvd_v1.0.0_church_教会_属灵家_001_L1",
    )
    version: str = "1.0.0"
