"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402009
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
    semantic_id="dvd_v1.0.0_desert_旷野_分别_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Desert旷野分别(SemanticEntry):
    """
    ### Source Text

> **Desert**: A season of being set apart. Negatively it speaks of being spirituall...
    """
    
    original_text: str = """### Source Text

> **Desert**: A season of being set apart. Negatively it speaks of being spiritually dry.
> Being called to the desert is actually quite positive—you will grow in your relationship with the Lord. Even Jesus withdrew often to the wilderness to be alone with the Father.
> Luke 1:80 "And the child grew, and waxed strong in spirit, and was in the deserts till the day of his showing to Israel."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Desert | 旷野 | 分别的季节 |
| Wilderness | 荒野 | 与主独处 |
| Set apart | 分别 | 为成长而隐退 |
| Dry | 干旱 | 属灵缺乏 |

### English Paraphrase

Desert represents a season of being set apart for growth. Being called to the desert is positive—you will grow in relationship with the Lord. Jesus withdrew to the wilderness to pray. Negatively, a barren wilderness speaks of being cursed or spiritually dry.

### Chinese Interpretation

旷野代表为成长而分别的季节。被呼召到旷野是正面的——你将在与主的关系中成长。耶稣退到旷野祷告。负面而言，荒芜的旷野象征被咒诅或属灵干旱。

### Core Points

1. **正负皆可**: 目的决定含义
2. **分别成长**: 先知训练的必经之路
3. **与主独处**: 最宝贵的亲密时光
4. **干旱警告**: 可能表示属灵缺乏

### Narrative Snippets

- `[ns_dav_d014]` `[trigger: desert_growth]` `[factor_trigger: dream_desert AND dream_growth]` `[role: 主干]` Being called to the desert is positive—you will grow in your relationship with the Lord. → 被呼召到旷野是正面的——你将在与主的关系中成长。
- `[ns_dav_d015]` `[trigger: desert_dry]` `[factor_trigger: dream_desert AND dream_dryness]` `[role: 警告]` A barren wilderness speaks of being spiritually dry and needing the water of the Spirit. → 荒芜的旷野象征属灵干旱，需要圣灵的活水。"""
    normalized_text_zh: str = """"""
    subject: str = "Desert 旷野/分别"
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
        l1_anchor="dvd_v1.0.0_desert_旷野_分别_001_L1",
    )
    version: str = "1.0.0"
