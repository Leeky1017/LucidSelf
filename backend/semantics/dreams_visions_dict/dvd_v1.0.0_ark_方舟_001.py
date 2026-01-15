"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439702
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
    semantic_id="dvd_v1.0.0_ark_方舟_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ark方舟(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: The ark is symbolic of salvation and the process we undergo ...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: The ark is symbolic of salvation and the process we undergo when entering into the Body of Christ through baptism. It is a picture of the baptism unto death to resurrect in new life.

**Noah's Ark - Positive**: Speaks of change coming—a season of death and tremendous change leading to resurrection and new doors. If things seem to be closing down, the Lord is doing something new. Like Noah shut away in the ark, you might feel shut away—but soon your feet will land on new land with new promises (1 Peter 3:20-21).

**Ark of the Covenant**: In personal experience, speaks of God's manifest glory—where His glory rested in Old Testament. Type and shadow of the anointing we now have as New Testament believers. When born again, Holy Spirit dwells inside you—you are the temple of the Holy Ghost.

**See also**: Baptism, Altar

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Noah's Ark | Salvation through death/resurrection | Change, new beginning |
| Ark of Covenant | God's manifest glory | Anointing presence |
| Incubation | Shut-away season | Preparation for new |

### English Paraphrase

Ark symbolizes salvation through death-to-resurrection process (baptism). **Noah's Ark**: Change is coming—season of death and tremendous change, but leads to resurrection and new doors. Feeling shut away like Noah? Hang in there—soon you'll land on new ground with new promises. **Ark of Covenant**: God's manifest glory. In OT, where glory rested. Now we are the temple—Holy Spirit dwells inside. Both arks speak of transition through death to glory.

### Chinese Interpretation（完整对等诠释）

方舟象征通过死亡到复活过程的救恩（受洗）。**挪亚方舟**：改变将来临——死亡和巨大改变的季节，但导向复活和新门。感觉像挪亚一样被关闭？坚持住——很快你会踏上新土地，有新应许。**约柜**：神显明的荣耀。在旧约，是荣耀安息之处。现在我们是殿——圣灵住在里面。两个方舟都讲述通过死亡到荣耀的过渡。

### Narrative Snippets

- `[ns_dav_a038]` `[trigger: 梦方舟]` `[factor_trigger: dream_symbol_ark]` `[role: 主干]` Ark = salvation through death-to-resurrection process—change and new beginnings. → Dreams Dictionary #Ark
- `[ns_dav_a039]` `[trigger: 挪亚方舟]` `[factor_trigger: dream_symbol_ark AND transition_phase]` `[role: 主干依赖]` Noah's Ark = season of being shut away leading to new land and promises. → Dreams Dictionary #Ark
- `[ns_dav_a040]` `[trigger: 约柜]` `[factor_trigger: dream_symbol_ark AND transition_phase]` `[role: 条件分支]` Ark of Covenant = God's manifest glory; you are now the temple of Holy Spirit. → Dreams Dictionary #Ark"""
    normalized_text_zh: str = """"""
    subject: str = "Ark 方舟"
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
        l1_anchor="dvd_v1.0.0_ark_方舟_001_L1",
    )
    version: str = "1.0.0"
