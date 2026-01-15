"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429211
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
    semantic_id="dvd_v1.0.0_idol_偶像_敬拜对象_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Idol偶像敬拜对象(SemanticEntry):
    """
    ### Source Text

> **Idol**: The object of your worship. Things that have the place of honor in your...
    """
    
    original_text: str = """### Source Text

> **Idol**: The object of your worship. Things that have the place of honor in your life. There is no place for a positive interpretation for an idol. An idol in a dream or vision represents something taking your time, affection and worship that should go to God.
> Golden Calf: Speaks of heresy and doctrine not of God.
> Work of Your Hands: Things accomplished becoming more important than what God wants.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Idol | 偶像 | 敬拜的对象 |
| Worship | 敬拜 | 应归给神的 |
| Golden calf | 金牛犊 | 异端和错误教义 |
| Works | 工作 | 自己成就的 |

### English Paraphrase

An idol represents the object of your worship—things taking the place of honor that belongs to God. There is no positive interpretation for an idol. A golden calf speaks of heresy. The work of your hands becoming an idol means accomplishments becoming more important than God's will.

### Chinese Interpretation

偶像代表你敬拜的对象——占据了本属于神的尊荣位置的事物。偶像没有正面解释。金牛犊象征异端。你手所做的工作成为偶像意味着成就变得比神的旨意更重要。

### Core Points

1. **始终负面**: 偶像没有正面含义
2. **敬拜错位**: 把敬拜给了不是神的
3. **异端象征**: 金牛犊代表错误教义
4. **工作偶像**: 成就可能成为偶像

### Narrative Snippets

- `[ns_dav_i002]` `[trigger: idol_worship]` `[factor_trigger: dream_idol AND dream_worship]` `[role: 警告]` An idol represents something taking your time, affection and worship that should go to God. → 偶像代表某些东西占据了你应该给神的时间、感情和敬拜。
- `[ns_dav_i003]` `[trigger: idol_calf]` `[factor_trigger: dream_idol AND dream_heresy]` `[role: 警告]` A golden calf speaks of heresy and doctrine that is not of God. → 金牛犊象征异端和不属于神的教义。"""
    normalized_text_zh: str = """"""
    subject: str = "Idol 偶像/敬拜对象"
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
        l1_anchor="dvd_v1.0.0_idol_偶像_敬拜对象_001_L1",
    )
    version: str = "1.0.0"
