"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405257
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
    semantic_id="dvd_v1.0.0_perfume_香水_吸引_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Perfume香水吸引(SemanticEntry):
    """
    ### Source Text

> **Perfume**: Our praise to the Lord, being beautified, prepared, honored and clea...
    """
    
    original_text: str = """### Source Text

> **Perfume**: Our praise to the Lord, being beautified, prepared, honored and cleansed. A bride was prepared with perfume for her wedding night—speaking of the Bride of Christ being prepared. We diffuse the perfume of Christ everywhere we go.
> Negative: The perfume of the harlot—being seduced into the world, deceived into sin.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Perfume | 香水 | 赞美和预备 |
| Praise | 赞美 | 对主的敬拜 |
| Bride | 新娘 | 基督的新娘 |
| Harlot | 妓女 | 世界的引诱 |

### English Paraphrase

Perfume represents praise, beautifying, preparation, honor and cleansing. A bride prepared with perfume speaks of the Bride of Christ being made ready. We diffuse Christ's perfume everywhere. The harlot's perfume speaks of worldly seduction into sin.

### Chinese Interpretation

香水代表赞美、美化、预备、尊荣和洁净。用香水预备的新娘象征基督的新娘被预备好。我们到处散发基督的香气。妓女的香水象征被世界引诱陷入罪中。

### Core Points

1. **正负皆可**: 来源决定含义
2. **赞美象征**: 对主的敬拜
3. **新娘预备**: 基督新娘的装扮
4. **引诱警告**: 世界的虚假吸引

### Narrative Snippets

- `[ns_dav_p005]` `[trigger: perfume_bride]` `[factor_trigger: dream_perfume AND dream_bride]` `[role: 主干]` Perfume speaks of the Bride of Christ being prepared—we diffuse Christ's fragrance everywhere. → 香水象征基督的新娘被预备——我们到处散发基督的香气。
- `[ns_dav_p006]` `[trigger: perfume_harlot]` `[factor_trigger: dream_perfume AND dream_seduction]` `[role: 警告]` The harlot's perfume speaks of being seduced into the world—deceived into sin. → 妓女的香水象征被世界引诱——被骗入罪中。"""
    normalized_text_zh: str = """"""
    subject: str = "Perfume 香水/吸引"
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
        l1_anchor="dvd_v1.0.0_perfume_香水_吸引_001_L1",
    )
    version: str = "1.0.0"
