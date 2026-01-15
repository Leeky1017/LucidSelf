"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439694
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
    semantic_id="dvd_v1.0.0_apple_苹果_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Apple苹果(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: A fruit common to most people. It has both a negative and po...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: A fruit common to most people. It has both a negative and positive connotation.

**Dreams - Positive** (Acts 14:17): An apple can speak of favor or a gift. Also speaks of being fruitful and something that has reached maturity—spiritual maturity.

**Dreams - Negative**: A rotten apple can speak of poison, deception, sin or hidden evil within.

**Visions - Positive** (Psalm 17:8): "Keep me as the apple of the eye." Speaks of favor and position of importance—we are the apple of God's eye. Also Proverbs 7:2—esteem the Word as of great importance.

**Visions - Negative** (Genesis 3:6): The forbidden fruit—temptation and fruits of the flesh. Fruit that looks good outside but bad inside = temptation; don't give in just because it looks good.

**See also**: Fruit

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Apple | Favor, gift, maturity | Positive or temptation |
| Apple of the eye | Position of importance | God's favor |
| Rotten apple | Hidden evil, deception | Corruption |
| Forbidden fruit | Temptation | Genesis 3 fall |

### English Paraphrase

Apple has dual meaning. **Positive**: Favor, gift, fruitfulness, spiritual maturity. "Apple of the eye" (Ps 17:8) = position of importance in God's sight; esteeming God's Word. **Negative**: Rotten apple = hidden evil, deception, sin within. Forbidden fruit (Gen 3:6) = temptation, flesh. If fruit looks good outside but bad inside, it's temptation—discern the spirit, don't judge by appearance.

### Chinese Interpretation（完整对等诠释）

苹果有双重含义。**正面**：恩惠、礼物、结果子、属灵成熟。「眼中的瞳人」（诗17:8）= 在神眼中有重要位置；尊重神的话。**负面**：烂苹果 = 隐藏的邪恶、欺骗、内在的罪。禁果（创3:6）= 试探、肉体。如果果子外表好看但里面坏了，是试探——分辨诸灵，不要以外表判断。

### Narrative Snippets

- `[ns_dav_a035]` `[trigger: 梦苹果]` `[factor_trigger: dream_symbol_apple]` `[role: 主干]` Apple = dual symbol: favor/maturity (positive) or temptation/hidden evil (negative). → Dreams Dictionary #Apple
- `[ns_dav_a036]` `[trigger: 眼中瞳人]` `[factor_trigger: dream_symbol_apple AND fruit_condition]` `[role: 条件分支]` "Apple of the eye" = position of importance, God's favor (Psalm 17:8). → Dreams Dictionary #Apple
- `[ns_dav_a037]` `[trigger: 禁果]` `[factor_trigger: dream_symbol_apple AND dream_forbidden]` `[role: 条件分支]` Forbidden fruit = temptation, flesh—looks good outside, bad inside. → Dreams Dictionary #Apple"""
    normalized_text_zh: str = """"""
    subject: str = "Apple 苹果"
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
        l1_anchor="dvd_v1.0.0_apple_苹果_001_L1",
    )
    version: str = "1.0.0"
