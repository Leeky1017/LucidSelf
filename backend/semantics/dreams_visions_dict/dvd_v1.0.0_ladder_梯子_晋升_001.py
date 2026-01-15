"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443859
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
    semantic_id="dvd_v1.0.0_ladder_梯子_晋升_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ladder梯子晋升(SemanticEntry):
    """
    ### Source Text

> **Ladder**: A ladder speaks of going from one level to another in your life. Goin...
    """
    
    original_text: str = """### Source Text

> **Ladder**: A ladder speaks of going from one level to another in your life. Going up the ladder speaks of a promotion in the spirit. Going down means demotion.
> Jacob's Ladder: The Lord confirming His covenant—access to all the blessings of heaven. As believers, this ladder to heaven is now open to us!
> Negative: Going down may mean the Lord desires to take you through circumstances for full benefit.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Ladder | 梯子 | 层次的转变 |
| Promotion | 晋升 | 属灵的提升 |
| Demotion | 降级 | 失去位置 |
| Jacob's ladder | 雅各的梯子 | 通天的道路 |

### English Paraphrase

A ladder represents going from one level to another. Going up speaks of spiritual promotion; going down means demotion. Jacob's ladder represents covenant access to heaven's blessings—now open to all believers.

### Chinese Interpretation

梯子代表从一个层次到另一个层次。往上代表属灵的晋升；往下意味着降级。雅各的梯子代表约中通往天上祝福的道路——现在向所有信徒敞开。

### Core Points

1. **正负皆可**: 方向决定含义
2. **晋升象征**: 属灵的提升
3. **雅各之梯**: 通往天上的道路
4. **降级警告**: 可能需要经历对付

### Narrative Snippets

- `[ns_dav_l001]` `[trigger: ladder_up]` `[factor_trigger: dream_ladder AND dream_ascend]` `[role: 主干]` Going up the ladder speaks of a promotion in the spirit—reaching new heights. → 上梯子象征属灵的晋升——达到新的高度。
- `[ns_dav_l002]` `[trigger: ladder_jacob]` `[factor_trigger: dream_ladder AND dream_covenant]` `[role: 主干]` Jacob's ladder represents covenant access to all the blessings of heaven—now open to believers. → 雅各的梯子代表约中通往天上一切祝福的道路——现在向信徒敞开。"""
    normalized_text_zh: str = """"""
    subject: str = "Ladder 梯子/晋升"
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
        l1_anchor="dvd_v1.0.0_ladder_梯子_晋升_001_L1",
    )
    version: str = "1.0.0"
