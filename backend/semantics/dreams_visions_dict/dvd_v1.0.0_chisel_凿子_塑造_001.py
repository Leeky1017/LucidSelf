"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419776
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
    semantic_id="dvd_v1.0.0_chisel_凿子_塑造_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Chisel凿子塑造(SemanticEntry):
    """
    ### Source Text

> **Chisel**: A picture of the work of the Holy Spirit in your life, shaping and mo...
    """
    
    original_text: str = """### Source Text

> **Chisel**: A picture of the work of the Holy Spirit in your life, shaping and molding you.
> A chisel is used by a craftsman to shape stone or wood. In dreams and visions, it represents the Lord's work of refining and shaping your character.
> Exodus 20:25 "And if you make me an altar of stone, you shall not build it of hewn stone: for if you lift up your tool upon it, you have polluted it."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Chisel | 凿子 | 塑造的工具 |
| Shaping | 塑造 | 圣灵的工作 |
| Refining | 精炼 | 去除杂质 |
| Character | 品格 | 内在的品质 |

### English Paraphrase

A chisel represents the Holy Spirit's work in shaping and molding you. Like a craftsman shaping stone, the Lord refines your character. Sometimes the chiseling is painful but produces eternal fruit.

### Chinese Interpretation

凿子代表圣灵塑造和雕琢你的工作。就像工匠塑造石头一样，主精炼你的品格。有时凿刻是痛苦的，但会结出永恒的果实。

### Core Points

1. **通常正面**: 代表圣灵的塑造工作
2. **精炼过程**: 去除生命中的杂质
3. **品格建造**: 塑造基督的品格
4. **痛苦必经**: 过程可能艰难但有价值

### Narrative Snippets

- `[ns_dav_c025]` `[trigger: chisel_shaping]` `[factor_trigger: dream_chisel AND dream_shaping]` `[role: 主干]` A chisel represents the Holy Spirit's work in shaping and refining your character. → 凿子代表圣灵塑造和精炼你品格的工作。"""
    normalized_text_zh: str = """"""
    subject: str = "Chisel 凿子/塑造"
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
        l1_anchor="dvd_v1.0.0_chisel_凿子_塑造_001_L1",
    )
    version: str = "1.0.0"
