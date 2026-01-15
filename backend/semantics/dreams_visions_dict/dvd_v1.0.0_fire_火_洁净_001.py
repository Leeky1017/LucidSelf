"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412164
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
    semantic_id="dvd_v1.0.0_fire_火_洁净_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Fire火洁净(SemanticEntry):
    """
    ### Source Text

> **Fire**: A picture of the Holy Spirit, purification, and the presence of God. Ca...
    """
    
    original_text: str = """### Source Text

> **Fire**: A picture of the Holy Spirit, purification, and the presence of God. Can also represent judgment or destruction.
> Positive: Fire refines and purifies. The Holy Spirit came as tongues of fire. Fire consumes the sacrifice.
> Negative: Fire of judgment destroys. Hell is described as fire. Passion burning out of control.
> Hebrews 12:29 "For our God is a consuming fire."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Fire | 火 | 圣灵和洁净 |
| Holy Spirit | 圣灵 | 火焰舌头 |
| Purification | 洁净 | 精炼的过程 |
| Judgment | 审判 | 毁灭性的火 |

### English Paraphrase

Fire represents the Holy Spirit, purification, and God's presence. Fire refines and purifies—the Holy Spirit came as tongues of fire. Fire consumes the sacrifice. Negatively, fire of judgment destroys, hell is fire, and uncontrolled passion burns destructively.

### Chinese Interpretation

火代表圣灵、洁净和神的同在。火精炼和洁净——圣灵如火焰舌头降临。火焚烧祭物。负面而言，审判的火毁灭，地狱是火，失控的激情毁灭性地燃烧。

### Core Points

1. **正负皆可**: 火的来源和目的决定含义
2. **圣灵象征**: 火焰舌头的恩膏
3. **洁净工具**: 除去杂质
4. **审判警告**: 神是烈火

### Narrative Snippets

- `[ns_dav_f010]` `[trigger: fire_spirit]` `[factor_trigger: dream_fire AND dream_spirit]` `[role: 主干]` Fire represents the Holy Spirit and purification—refining and purifying you for God's purposes. → 火代表圣灵和洁净——为神的目的精炼和洁净你。
- `[ns_dav_f011]` `[trigger: fire_judgment]` `[factor_trigger: dream_fire AND dream_judgment]` `[role: 警告]` Our God is a consuming fire—fire of judgment destroys what is not of Him. → 我们的神是烈火——审判的火毁灭不属于祂的一切。"""
    normalized_text_zh: str = """"""
    subject: str = "Fire 火/洁净"
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
        l1_anchor="dvd_v1.0.0_fire_火_洁净_001_L1",
    )
    version: str = "1.0.0"
