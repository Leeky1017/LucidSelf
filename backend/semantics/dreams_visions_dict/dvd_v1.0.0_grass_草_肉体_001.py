"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.390711
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
    semantic_id="dvd_v1.0.0_grass_草_肉体_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Grass草肉体(SemanticEntry):
    """
    ### Source Text

> **Grass**: A picture of the frailty of flesh and the temporary nature of life.
> ...
    """
    
    original_text: str = """### Source Text

> **Grass**: A picture of the frailty of flesh and the temporary nature of life.
> Isaiah 40:6 "All flesh is grass, and all the goodliness thereof is as the flower of the field."
> Positive: Green grass can speak of provision (lying in green pastures). Negative: Dried grass speaks of frailty and death. Grass being burned indicates flesh being dealt with.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Grass | 草 | 肉体和短暂 |
| Flesh | 肉体 | 人的软弱 |
| Frailty | 脆弱 | 生命的短暂 |
| Pasture | 草场 | 神的供应 |

### English Paraphrase

Grass represents the frailty of flesh and temporary nature of life. All flesh is grass—here today, gone tomorrow. Green grass can speak of provision (green pastures). Dried grass speaks of frailty and death. Grass being burned indicates flesh being dealt with.

### Chinese Interpretation

草代表肉体的脆弱和生命的短暂。凡有血气的尽都如草——今天在，明天不在。青草可以象征供应（青草地）。干草象征脆弱和死亡。草被焚烧表示肉体正在被对付。

### Core Points

1. **正负皆可**: 草的状态决定含义
2. **肉体象征**: 凡有血气的尽都如草
3. **供应记号**: 青草地是安息
4. **对付肉体**: 草被烧代表洁净

### Narrative Snippets

- `[ns_dav_g011]` `[trigger: grass_flesh]` `[factor_trigger: dream_grass AND dream_flesh]` `[role: 主干]` All flesh is grass—the frailty and temporary nature of human life. → 凡有血气的尽都如草——人生命的脆弱和短暂。
- `[ns_dav_g012]` `[trigger: grass_pasture]` `[factor_trigger: dream_grass AND dream_pasture]` `[role: 主干]` He makes me lie down in green pastures—green grass speaks of rest and provision. → 祂使我躺卧在青草地上——青草象征安息和供应。"""
    normalized_text_zh: str = """"""
    subject: str = "Grass 草/肉体"
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
        l1_anchor="dvd_v1.0.0_grass_草_肉体_001_L1",
    )
    version: str = "1.0.0"
