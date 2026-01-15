"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405245
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
    semantic_id="dvd_v1.0.0_pen_笔_表达_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Pen笔表达(SemanticEntry):
    """
    ### Source Text

> **Pen**: To express what is in your heart and spirit through writing. To declare ...
    """
    
    original_text: str = """### Source Text

> **Pen**: To express what is in your heart and spirit through writing. To declare and establish the Word of God for posterity. A golden pen is linked to the Teaching Ministry—the Lord wants you to document what He has given you.
> Negative: A black pen speaks of the enemy's plan and heresy spread in the church.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Pen | 笔 | 书写和表达 |
| Express | 表达 | 心中的东西 |
| Document | 记录 | 留给后人 |
| Teaching | 教导 | 事工的方向 |

### English Paraphrase

A pen represents expressing your heart through writing—declaring and documenting God's Word. A golden pen links to Teaching Ministry—the Lord wants you to write what He has given. A black pen speaks of the enemy's plan and heresy.

### Chinese Interpretation

笔代表通过书写表达你的心——宣告和记录神的话。金笔与教导事工相关——主要你写下祂给你的东西。黑笔象征仇敌的计划和异端。

### Core Points

1. **正负皆可**: 笔的颜色决定含义
2. **表达象征**: 心中话语的出口
3. **教导呼召**: 金笔是教导事工
4. **异端警告**: 黑笔是仇敌的计划

### Narrative Snippets

- `[ns_dav_p003]` `[trigger: pen_teach]` `[factor_trigger: dream_pen AND dream_teaching]` `[role: 主干]` A golden pen is linked to Teaching Ministry—the Lord wants you to document what He has given you. → 金笔与教导事工相关——主要你记录祂给你的东西。
- `[ns_dav_p004]` `[trigger: pen_black]` `[factor_trigger: dream_pen AND dream_heresy]` `[role: 警告]` A black pen speaks of the enemy's plan and heresy spread in the church. → 黑笔象征仇敌的计划和在教会中散布的异端。"""
    normalized_text_zh: str = """"""
    subject: str = "Pen 笔/表达"
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
        l1_anchor="dvd_v1.0.0_pen_笔_表达_001_L1",
    )
    version: str = "1.0.0"
