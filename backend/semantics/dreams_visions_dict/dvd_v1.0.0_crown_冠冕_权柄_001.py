"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419916
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
    semantic_id="dvd_v1.0.0_crown_冠冕_权柄_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Crown冠冕权柄(SemanticEntry):
    """
    ### Source Text

> **Crown**: Receiving a crown speaks of being given a position of honor and favor....
    """
    
    original_text: str = """### Source Text

> **Crown**: Receiving a crown speaks of being given a position of honor and favor. To have run the race faithfully and won.
> Positive: If you see the Lord giving you a crown, it speaks of being given honor and authority. A laurel wreath indicates you have run a good race and won.
> Negative: To dream of losing your crown or having it stolen speaks of letting go of the authority God has given you.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Crown | 冠冕 | 荣耀和权柄 |
| Honor | 尊荣 | 被高举的地位 |
| Authority | 权柄 | 神所赐的能力 |
| Victory | 得胜 | 完成赛程 |

### English Paraphrase

A crown speaks of being given honor, favor, and authority. The Lord giving you a crown means honor and authority for faithful service. A laurel wreath means you have won your race. Losing your crown speaks of letting go of God-given authority.

### Chinese Interpretation

冠冕象征被赋予尊荣、恩宠和权柄。主给你冠冕意味着因忠心服事而得尊荣和权柄。月桂花冠表示你赢得了赛程。失去冠冕象征放弃神所赐的权柄。

### Core Points

1. **正负皆可**: 得到或失去决定含义
2. **荣耀赏赐**: 忠心的奖赏
3. **权柄象征**: 代表属灵职分
4. **需要持守**: 要持守所得的

### Narrative Snippets

- `[ns_dav_c047]` `[trigger: crown_honor]` `[factor_trigger: dream_crown AND dream_honor]` `[role: 主干]` Receiving a crown speaks of being given honor and authority—faithful service rewarded. → 接受冠冕象征被赋予尊荣和权柄——忠心服事得到奖赏。
- `[ns_dav_c048]` `[trigger: crown_lost]` `[factor_trigger: dream_crown AND dream_lost]` `[role: 警告]` Losing your crown speaks of letting go of the authority God has given you—hold fast! → 失去冠冕象征放弃神所赐的权柄——要持守！"""
    normalized_text_zh: str = """"""
    subject: str = "Crown 冠冕/权柄"
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
        l1_anchor="dvd_v1.0.0_crown_冠冕_权柄_001_L1",
    )
    version: str = "1.0.0"
