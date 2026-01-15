"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419825
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
    semantic_id="dvd_v1.0.0_coals_炭火_洁净_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Coals炭火洁净(SemanticEntry):
    """
    ### Source Text

> **Coals**: A picture of the refining fire of God or the passion within you.
> Coa...
    """
    
    original_text: str = """### Source Text

> **Coals**: A picture of the refining fire of God or the passion within you.
> Coals from the altar touched Isaiah's lips to cleanse him. Coals speak of the purifying fire of God. Burning coals can also speak of passion—on fire for the Lord.
> Isaiah 6:6 "Then flew one of the seraphims to me, having a live coal in his hand, which he had taken with the tongs from off the altar."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Coals | 炭火 | 洁净和热情 |
| Refining | 精炼 | 神的洁净工作 |
| Purifying | 洁净 | 除去不洁 |
| Passion | 热情 | 为主火热 |

### English Paraphrase

Coals represent the refining fire of God or passion within you. The coal from the altar touched Isaiah's lips to cleanse him. Burning coals speak of being on fire for the Lord, while also representing purification.

### Chinese Interpretation

炭火代表神的精炼之火或你里面的热情。从祭坛取的炭沾了以赛亚的嘴唇来洁净他。燃烧的炭象征为主火热，同时也代表洁净。

### Core Points

1. **通常正面**: 代表洁净和热情
2. **洁净工具**: 神用炭火洁净先知
3. **热情象征**: 为主火热燃烧
4. **祭坛关联**: 来自祭坛的神圣之火

### Narrative Snippets

- `[ns_dav_c034]` `[trigger: coals_purify]` `[factor_trigger: dream_coals AND dream_purify]` `[role: 主干]` Coals from the altar speak of the purifying fire of God—touching your lips to cleanse and prepare you. → 祭坛的炭火象征神洁净的火——沾你的嘴唇来洁净和预备你。
- `[ns_dav_c035]` `[trigger: coals_passion]` `[factor_trigger: dream_coals AND dream_passion]` `[role: 主干]` Burning coals speak of passion—being on fire for the Lord and His purposes. → 燃烧的炭象征热情——为主和祂的旨意火热。"""
    normalized_text_zh: str = """"""
    subject: str = "Coals 炭火/洁净"
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
        l1_anchor="dvd_v1.0.0_coals_炭火_洁净_001_L1",
    )
    version: str = "1.0.0"
