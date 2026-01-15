"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419684
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
    semantic_id="dvd_v1.0.0_camel_骆驼_财富_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Camel骆驼财富(SemanticEntry):
    """
    ### Source Text

> **Camel**: A carrier of blessing and a picture of wealth.
> The camel was respons...
    """
    
    original_text: str = """### Source Text

> **Camel**: A carrier of blessing and a picture of wealth.
> The camel was responsible for carrying the trade of the merchants—a carrier of blessing. Wearing camel's hair is a picture of walking in humility.
> Negative: The camel speaks of a place of stumbling. "It is easier for a camel to go through a needle's eye, than for a rich man to enter into the kingdom of God." (Luke 18:25)

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Camel | 骆驼 | 财富和祝福的载体 |
| Carrier | 载体 | 承载祝福的工具 |
| Humility | 谦卑 | 穿骆驼毛衣的象征 |
| Stumbling | 绊脚石 | 财富可能成为障碍 |

### English Paraphrase

A camel is a carrier of blessing and a picture of wealth. The camel carried the trade of merchants, symbolizing provision from afar. Wearing camel's hair represents humility. Negatively, the camel speaks of stumbling over wealth or insignificant things.

### Chinese Interpretation

骆驼是祝福的载体和财富的象征。骆驼承载商人的贸易，象征从远方来的供应。穿骆驼毛代表谦卑。负面而言，骆驼象征财富可能成为绊脚石，或在小事上跌倒却忽略大错。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **财富载体**: 象征从各地而来的供应
3. **谦卑象征**: 骆驼毛衣代表放下骄傲
4. **绊脚石**: 财富可能阻碍进入天国

### Narrative Snippets

- `[ns_dav_c006]` `[trigger: camel_blessing]` `[factor_trigger: dream_camel AND dream_provision]` `[role: 主干]` A camel is a carrier of blessing—speaking of provision from afar and the blessing of the Lord. → 骆驼是祝福的载体，象征从远方而来的供应。
- `[ns_dav_c007]` `[trigger: camel_stumbling]` `[factor_trigger: dream_camel AND dream_stumbling]` `[role: 警告]` The camel speaks of a place of stumbling—straining out a gnat but swallowing a camel. → 骆驼象征绊脚石，提醒勿因小失大。"""
    normalized_text_zh: str = """"""
    subject: str = "Camel 骆驼/财富"
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
        l1_anchor="dvd_v1.0.0_camel_骆驼_财富_001_L1",
    )
    version: str = "1.0.0"
