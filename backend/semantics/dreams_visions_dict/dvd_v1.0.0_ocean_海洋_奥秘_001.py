"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433454
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
    semantic_id="dvd_v1.0.0_ocean_海洋_奥秘_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ocean海洋奥秘(SemanticEntry):
    """
    ### Source Text

> **Ocean/Sea**: A picture of mystery and untapped blessing. Floating or swimming w...
    """
    
    original_text: str = """### Source Text

> **Ocean/Sea**: A picture of mystery and untapped blessing. Floating or swimming with control speaks of trusting the Lord. Large waves surfed speak of blessing coming. The Red Sea Situation—facing an impossible direction, needing to take the first step so God can move.
> Negative: Large waves engulfing speaks of overwhelming circumstances. Being tossed around means not having firm conviction in the Word.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Ocean | 海洋 | 奥秘和祝福 |
| Waves | 波浪 | 祝福或压力 |
| Red Sea | 红海 | 不可能的处境 |
| Tossed | 被抛 | 没有扎根 |

### English Paraphrase

The ocean pictures mystery and untapped blessing. Floating or swimming with control speaks of trusting the Lord. Large waves surfed speak of coming blessing. The Red Sea Situation requires taking the first step so God can move. Engulfing waves speak of overwhelming circumstances. Being tossed means lacking firm conviction.

### Chinese Interpretation

海洋象征奥秘和未开发的祝福。受控地漂浮或游泳象征信靠主。冲浪的大浪象征即将来临的祝福。红海处境需要迈出第一步让神动工。吞没的波浪象征压倒性的环境。被抛来抛去意味着缺乏坚定的信念。

### Core Points

1. **正负皆可**: 波浪状态决定含义
2. **奥秘象征**: 未开发的祝福
3. **红海记号**: 需要迈出第一步
4. **摇摆警告**: 没有扎根在话语中

### Narrative Snippets

- `[ns_dav_o001]` `[trigger: ocean_trust]` `[factor_trigger: dream_ocean AND dream_trust]` `[role: 主干]` Floating or swimming with control speaks of trusting the Lord and enjoying His presence. → 受控地漂浮或游泳象征信靠主和享受祂的同在。
- `[ns_dav_o002]` `[trigger: ocean_tossed]` `[factor_trigger: dream_ocean AND dream_doubt]` `[role: 警告]` Being tossed around in the ocean means not having firm conviction in the Word. → 在海中被抛来抛去意味着在话语中没有坚定的信念。"""
    normalized_text_zh: str = """"""
    subject: str = "Ocean 海洋/奥秘"
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
        l1_anchor="dvd_v1.0.0_ocean_海洋_奥秘_001_L1",
    )
    version: str = "1.0.0"
