"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405304
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
    semantic_id="dvd_v1.0.0_potter_s_wheel_窑匠轮_塑造_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class PotterSWheel窑匠轮塑造(SemanticEntry):
    """
    ### Source Text

> **Potter's Wheel**: A season of shaping that the Lord is about to do in your life...
    """
    
    original_text: str = """### Source Text

> **Potter's Wheel**: A season of shaping that the Lord is about to do in your life. When the Lord calls you to do His work, you need to become the kind of person to fulfill that work—this requires change on the potter's wheel. He will apply pressures through circumstances and mentors—not to destroy you, but to make you a vessel of honor!

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Potter's Wheel | 窑匠轮 | 塑造的过程 |
| Shaping | 塑造 | 改变的季节 |
| Vessel | 器皿 | 被使用的人 |
| Honor | 尊荣 | 最终的目标 |

### English Paraphrase

The potter's wheel represents a season of shaping. When called to God's work, you need to become the right person—requiring change. He applies pressure through circumstances and mentors—not to destroy, but to make you a vessel of honor!

### Chinese Interpretation

窑匠轮代表塑造的季节。当被呼召做神的工作时，你需要成为对的人——需要改变。祂通过环境和导师施加压力——不是要毁灭你，而是要使你成为尊贵的器皿！

### Core Points

1. **通常正面**: 塑造是为了荣耀
2. **改变象征**: 需要经历的过程
3. **压力目的**: 不是毁灭而是塑造
4. **尊荣记号**: 最终成为尊贵器皿

### Narrative Snippets

- `[ns_dav_p012]` `[trigger: potter_shape]` `[factor_trigger: dream_potter AND dream_shaping]` `[role: 主干]` The potter's wheel speaks of the Lord shaping you—not to destroy, but to make you a vessel of honor! → 窑匠轮象征主塑造你——不是要毁灭你，而是要使你成为尊贵的器皿！"""
    normalized_text_zh: str = """"""
    subject: str = "Potter's Wheel 窑匠轮/塑造"
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
        l1_anchor="dvd_v1.0.0_potter_s_wheel_窑匠轮_塑造_001_L1",
    )
    version: str = "1.0.0"
