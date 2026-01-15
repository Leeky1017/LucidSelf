"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419924
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
    semantic_id="dvd_v1.0.0_cup_杯_器皿_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cup杯器皿(SemanticEntry):
    """
    ### Source Text

> **Cup**: The vessel that you are in the Lord. Also representative of the things w...
    """
    
    original_text: str = """### Source Text

> **Cup**: The vessel that you are in the Lord. Also representative of the things we are called to endure or take care of for the Lord.
> A cup is similar to a clay vessel—it speaks of us believers. Jesus referred to the wine in the cup as his blood and the New Covenant. A cup also represents trials we must endure.
> John 18:11 "The cup which my Father has given me, shall I not drink it?"

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cup | 杯 | 器皿和任务 |
| Vessel | 器皿 | 我们在主里面 |
| Covenant | 约 | 新约的血 |
| Trials | 试炼 | 需要经历的 |

### English Paraphrase

A cup represents the vessel you are in the Lord and the things you are called to endure. Jesus referred to the wine as His blood and the New Covenant. The cup also represents trials we must pass through—difficult but leading to God's perfect will and blessing.

### Chinese Interpretation

杯代表你在主里面的器皿和你被呼召去承受的事物。耶稣称杯中的酒为祂的血和新约。杯也代表我们必须经历的试炼——艰难但通向神完美的旨意和祝福。

### Core Points

1. **正负皆可**: 内容决定含义
2. **器皿象征**: 我们是盛装神荣耀的杯
3. **新约记号**: 杯中的酒象征基督的血
4. **试炼接受**: 接受神所赐的杯

### Narrative Snippets

- `[ns_dav_c049]` `[trigger: cup_vessel]` `[factor_trigger: dream_cup AND dream_vessel]` `[role: 主干]` A cup represents the vessel you are in the Lord—your capacity to contain and share His glory. → 杯代表你在主里面的器皿——你盛装和分享祂荣耀的容量。
- `[ns_dav_c050]` `[trigger: cup_trials]` `[factor_trigger: dream_cup AND dream_trials]` `[role: 主干]` The cup represents trials we must endure—difficult but leading to God's perfect will. → 杯代表我们必须经历的试炼——艰难但通向神完美的旨意。"""
    normalized_text_zh: str = """"""
    subject: str = "Cup 杯/器皿"
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
        l1_anchor="dvd_v1.0.0_cup_杯_器皿_001_L1",
    )
    version: str = "1.0.0"
