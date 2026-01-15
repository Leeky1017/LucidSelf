"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405316
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
    semantic_id="dvd_v1.0.0_precious_stones_宝石_价值_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class PreciousStones宝石价值(SemanticEntry):
    """
    ### Source Text

> **Precious Stones**: A depiction of your value and status in the eyes of God. The...
    """
    
    original_text: str = """### Source Text

> **Precious Stones**: A depiction of your value and status in the eyes of God. The High Priest's Ephod had 12 stones representing the tribes. Team members are gemstones rubbing off hard edges. The Lord may set you as a precious stone in His crown. For a stone to shine, it takes chiseling and buffing.
> Negative: A tarnished gemstone means you have let what God wrought in you go to waste.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Precious Stones | 宝石 | 价值和地位 |
| Value | 价值 | 在神眼中的 |
| Chiseling | 凿刻 | 需要对付的 |
| Crown | 冠冕 | 神的装饰 |

### English Paraphrase

Precious stones depict your value in God's eyes. The High Priest's Ephod had 12 stones for tribes. Team members are gemstones rubbing off edges. The Lord sets you in His crown. Shining requires chiseling and buffing. A tarnished gem means wasted what God did in you.

### Chinese Interpretation

宝石描绘你在神眼中的价值。大祭司的以弗得有12颗代表支派的宝石。团队成员是彼此磨去棱角的宝石。主把你镶嵌在祂的冠冕上。发光需要凿刻和打磨。失去光泽的宝石意味着浪费了神在你身上所做的。

### Core Points

1. **正负皆可**: 宝石状态决定含义
2. **价值象征**: 在神眼中的地位
3. **打磨过程**: 需要经历对付
4. **浪费警告**: 可能失去光泽

### Narrative Snippets

- `[ns_dav_p013]` `[trigger: stones_value]` `[factor_trigger: dream_stones AND dream_value]` `[role: 主干]` Precious stones depict your value in God's eyes—He may set you in His crown. → 宝石描绘你在神眼中的价值——祂可能把你镶嵌在祂的冠冕上。
- `[ns_dav_p014]` `[trigger: stones_tarnish]` `[factor_trigger: dream_stones AND dream_waste]` `[role: 警告]` A tarnished gemstone means you have let what God wrought in you go to waste. → 失去光泽的宝石意味着你让神在你身上所做的白费了。"""
    normalized_text_zh: str = """"""
    subject: str = "Precious Stones 宝石/价值"
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
        l1_anchor="dvd_v1.0.0_precious_stones_宝石_价值_001_L1",
    )
    version: str = "1.0.0"
