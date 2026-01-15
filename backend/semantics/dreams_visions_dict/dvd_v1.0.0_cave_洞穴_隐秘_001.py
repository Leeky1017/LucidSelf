"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419742
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
    semantic_id="dvd_v1.0.0_cave_洞穴_隐秘_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cave洞穴隐秘(SemanticEntry):
    """
    ### Source Text

> **Cave**: A season of obscurity but also of intimacy with the Lord. In a negative...
    """
    
    original_text: str = """### Source Text

> **Cave**: A season of obscurity but also of intimacy with the Lord. In a negative sense, a cave is a picture of trying to escape the pressures of life.
> Positive: Being drawn to a cave speaks of a time of seclusion that is temporary—a time of much growth where you will know the Lord face to face.
> 1 Kings 19:9 "And he came there to a cave, and lodged there; and, behold, the word of the LORD came to him."
> Negative: Being tied to a cave wall indicates hiding away from the real world because of past hurts.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cave | 洞穴 | 隐秘和亲密的场所 |
| Seclusion | 隐退 | 暂时的分别 |
| Intimacy | 亲密 | 与主面对面 |
| Hiding | 躲藏 | 逃避现实压力 |

### English Paraphrase

A cave represents a season of obscurity but also intimacy with the Lord. Being drawn to a cave speaks of temporary seclusion for growth and knowing the Lord face to face. Negatively, being tied to a cave wall indicates hiding from reality because of past hurts, refusing to step out.

### Chinese Interpretation

洞穴代表隐秘的季节，但也象征与主的亲密。被引到洞穴象征暂时的隐退，用于成长和面对面认识主。负面而言，被绑在洞壁上表示因过去的伤害而躲避现实，拒绝走出来。

### Core Points

1. **正负皆可**: 动机决定含义
2. **先知训练**: 这是先知训练的必经阶段
3. **亲密时光**: 最宝贵的与主相遇时刻
4. **逃避警告**: 可能表示躲避生活压力

### Narrative Snippets

- `[ns_dav_c018]` `[trigger: cave_intimacy]` `[factor_trigger: dream_cave AND dream_intimacy]` `[role: 主干]` Being drawn to a cave speaks of a time of seclusion for growth—knowing the Lord face to face. → 被引到洞穴象征隐退成长的时刻，与主面对面相遇。
- `[ns_dav_c019]` `[trigger: cave_hiding]` `[factor_trigger: dream_cave AND dream_hiding]` `[role: 警告]` Being tied to a cave wall indicates hiding from the real world because of past hurts. → 被绑在洞壁上表示因过去伤害而躲避现实世界。"""
    normalized_text_zh: str = """"""
    subject: str = "Cave 洞穴/隐秘"
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
        l1_anchor="dvd_v1.0.0_cave_洞穴_隐秘_001_L1",
    )
    version: str = "1.0.0"
