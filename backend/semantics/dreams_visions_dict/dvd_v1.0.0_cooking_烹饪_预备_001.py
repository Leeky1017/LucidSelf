"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419881
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
    semantic_id="dvd_v1.0.0_cooking_烹饪_预备_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cooking烹饪预备(SemanticEntry):
    """
    ### Source Text

> **Cooking**: The Lord has often given me dreams and visions where I see myself pr...
    """
    
    original_text: str = """### Source Text

> **Cooking**: The Lord has often given me dreams and visions where I see myself preparing food and handing it out.
> This speaks of not only ministering out to others what I have, but also training and mentoring them. To give them both the teaching and the training they need to rise up.
> See also: Bake, Bread, Cake

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cooking | 烹饪 | 预备和分享 |
| Preparing | 预备 | 为他人准备 |
| Ministering | 服事 | 将所有的分享出去 |
| Training | 培训 | 帮助他人成长 |

### English Paraphrase

Cooking represents preparing spiritual food and handing it out to others. It speaks of ministering what you have, training and mentoring others. To give them both the teaching and the training they need to rise up in their calling.

### Chinese Interpretation

烹饪代表预备属灵食物并分发给他人。它象征将你所拥有的服事出去，培训和指导他人。给他们所需的教导和训练，使他们在呼召中成长起来。

### Core Points

1. **通常正面**: 代表服事和培训
2. **双重功能**: 既教导又训练
3. **预备阶段**: 在分发前先预备
4. **门徒造就**: 帮助他人成长

### Narrative Snippets

- `[ns_dav_c040]` `[trigger: cooking_ministry]` `[factor_trigger: dream_cooking AND dream_ministry]` `[role: 主干]` Cooking speaks of preparing spiritual food and ministering it out—training and mentoring others. → 烹饪象征预备属灵食物并服事出去——培训和指导他人。"""
    normalized_text_zh: str = """"""
    subject: str = "Cooking 烹饪/预备"
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
        l1_anchor="dvd_v1.0.0_cooking_烹饪_预备_001_L1",
    )
    version: str = "1.0.0"
