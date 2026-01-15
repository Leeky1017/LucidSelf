"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443922
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
    semantic_id="dvd_v1.0.0_legs_腿_意志_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Legs腿意志(SemanticEntry):
    """
    ### Source Text

> **Legs**: Your ability to sustain and strengthen yourself through your own will—t...
    """
    
    original_text: str = """### Source Text

> **Legs**: Your ability to sustain and strengthen yourself through your own will—to get from one place to another.
> Positive: Legs being strengthened means the Lord will strengthen your ability to get the job done and run the race.
> Negative: Leg-breaking experience—the Lord continually trying to bring an area to death. Lame legs mean giving up on life, a picture of depression.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Legs | 腿 | 意志和能力 |
| Sustain | 支撑 | 自我维持 |
| Leg-breaking | 打断腿 | 主的对付 |
| Lame | 瘸腿 | 放弃生活 |

### English Paraphrase

Legs represent your ability to sustain yourself through will—to move forward. Strengthened legs mean the Lord will help you run the race. Leg-breaking speaks of the Lord bringing an area to death. Lame legs represent giving up on life—depression.

### Chinese Interpretation

腿代表你通过意志支撑自己的能力——向前移动。腿被加强意味着主会帮助你奔跑。打断腿象征主使某个领域死去。瘸腿代表放弃生活——抑郁。

### Core Points

1. **正负皆可**: 腿的状态决定含义
2. **意志象征**: 前进的能力
3. **对付过程**: 打断腿是死的经历
4. **抑郁警告**: 瘸腿是放弃的象征

### Narrative Snippets

- `[ns_dav_l007]` `[trigger: legs_strength]` `[factor_trigger: dream_legs AND dream_strength]` `[role: 主干]` Legs being strengthened means the Lord will strengthen your ability to run the race He has set. → 腿被加强意味着主会加强你奔跑祂所设定赛程的能力。
- `[ns_dav_l008]` `[trigger: legs_break]` `[factor_trigger: dream_legs AND dream_break]` `[role: 警告]` A leg-breaking experience speaks of the Lord bringing your will to complete death. → 打断腿的经历象征主使你的意志完全死去。"""
    normalized_text_zh: str = """"""
    subject: str = "Legs 腿/意志"
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
        l1_anchor="dvd_v1.0.0_legs_腿_意志_001_L1",
    )
    version: str = "1.0.0"
