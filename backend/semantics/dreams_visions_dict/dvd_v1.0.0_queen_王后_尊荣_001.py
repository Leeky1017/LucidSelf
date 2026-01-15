"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405377
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
    semantic_id="dvd_v1.0.0_queen_王后_尊荣_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Queen王后尊荣(SemanticEntry):
    """
    ### Source Text

> **Queen**: Royalty and favor. As believers we are all kings and queens in the Lor...
    """
    
    original_text: str = """### Source Text

> **Queen**: Royalty and favor. As believers we are all kings and queens in the Lord—speaking of our position and authority in Christ. Queen Esther is a lovely illustration—when ministering to a woman, seeing Esther means she should see herself as a queen, lifting up her head instead of groveling like a beggar.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Queen | 王后 | 王权和恩宠 |
| Royalty | 王权 | 在基督里的位置 |
| Authority | 权柄 | 信徒的身份 |
| Esther | 以斯帖 | 王后的榜样 |

### English Paraphrase

A queen represents royalty and favor—our position and authority in Christ. We are all kings and queens in the Lord. Queen Esther illustrates this—seeing Esther means seeing yourself as royalty, lifting your head instead of groveling.

### Chinese Interpretation

王后代表王权和恩宠——我们在基督里的位置和权柄。我们在主里都是君王和王后。以斯帖王后说明这一点——看见以斯帖意味着把自己看作王室，抬起头而不是卑躬屈膝。

### Core Points

1. **通常正面**: 王后代表尊荣
2. **位置象征**: 在基督里的身份
3. **以斯帖榜样**: 王后的典范
4. **自我认识**: 要抬起头

### Narrative Snippets

- `[ns_dav_q002]` `[trigger: queen_royal]` `[factor_trigger: dream_queen AND dream_royalty]` `[role: 主干]` A queen represents royalty and favor—our position and authority in Christ. See yourself as royalty! → 王后代表王权和恩宠——我们在基督里的位置和权柄。把自己看作王室！"""
    normalized_text_zh: str = """"""
    subject: str = "Queen 王后/尊荣"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="dvd_v1.0.0_queen_王后_尊荣_001_L1",
    )
    version: str = "1.0.0"
