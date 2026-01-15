"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419870
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
    semantic_id="dvd_v1.0.0_colors_颜色_含义_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Colors颜色含义(SemanticEntry):
    """
    ### Source Text

> **Colors**: There are various colors that are relevant in Scripture. Some are uni...
    """
    
    original_text: str = """### Source Text

> **Colors**: There are various colors that are relevant in Scripture. Some are universal while others are cultural.
> In all major cultures, black is negative and speaks of darkness. For the understanding of colors, apply the descriptions to your prophetic dreams.
> See also: Black, Blue, Brown, Gold, Green, Purple, Red, Silver

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Colors | 颜色 | 象征意义的载体 |
| Cultural | 文化的 | 因文化而异 |
| Universal | 普遍的 | 跨文化相同 |
| Symbolism | 象征 | 颜色的属灵含义 |

### English Paraphrase

Colors carry various symbolic meanings in Scripture. Some are universal (black always negative, speaking of darkness) while others vary by culture (red may mean fertility in some cultures, green in others). Apply individual color meanings to interpret your dreams.

### Chinese Interpretation

颜色在圣经中承载各种象征意义。有些是普遍的（黑色始终负面，代表黑暗），而有些因文化而异（红色在某些文化中代表生育力，绿色在其他文化中代表）。应用各颜色的含义来解读你的梦。

### Core Points

1. **参考指引**: 需查看具体颜色条目
2. **文化考量**: 有些颜色因文化而异
3. **普遍规则**: 黑色始终代表黑暗
4. **组合解读**: 多种颜色需综合考虑

### Narrative Snippets

- `[ns_dav_c039]` `[trigger: colors_meaning]` `[factor_trigger: dream_colors AND dream_meaning]` `[role: 指引]` Colors carry symbolic meanings—some universal like black for darkness, others cultural. See individual entries. → 颜色承载象征意义——有些普遍如黑色代表黑暗，有些因文化而异。请查阅具体条目。"""
    normalized_text_zh: str = """"""
    subject: str = "Colors 颜色/含义"
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
        l1_anchor="dvd_v1.0.0_colors_颜色_含义_001_L1",
    )
    version: str = "1.0.0"
