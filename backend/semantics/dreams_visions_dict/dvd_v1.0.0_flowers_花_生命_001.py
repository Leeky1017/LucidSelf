"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412206
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
    semantic_id="dvd_v1.0.0_flowers_花_生命_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Flowers花生命(SemanticEntry):
    """
    ### Source Text

> **Flowers**: A picture of life, beauty, and blessing. Can also represent the frag...
    """
    
    original_text: str = """### Source Text

> **Flowers**: A picture of life, beauty, and blessing. Can also represent the fragility of life.
> Positive: Flowers speak of blooming and flourishing—new life and hope. Receiving flowers indicates being blessed.
> Negative: Wilted flowers speak of death, sickness, or fading beauty. Life that is withering.
> Song of Solomon 2:12 "The flowers appear on the earth; the time of the singing is come."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Flowers | 花 | 生命和美丽 |
| Bloom | 绽放 | 生命力和希望 |
| Beauty | 美丽 | 神创造的荣美 |
| Wilted | 枯萎 | 生命衰退 |

### English Paraphrase

Flowers represent life, beauty, and blessing—also the fragility of life. Blooming flowers speak of flourishing and new hope. Receiving flowers indicates blessing. Wilted flowers speak of death, sickness, or fading beauty.

### Chinese Interpretation

花代表生命、美丽和祝福——也代表生命的脆弱。绽放的花象征繁荣和新希望。收到花表示被祝福。枯萎的花象征死亡、疾病或衰退的美丽。

### Core Points

1. **正负皆可**: 花的状态决定含义
2. **生命象征**: 绽放代表繁荣
3. **祝福记号**: 收到花是祝福
4. **枯萎警告**: 可能表示生命衰退

### Narrative Snippets

- `[ns_dav_f017]` `[trigger: flowers_bloom]` `[factor_trigger: dream_flowers AND dream_bloom]` `[role: 主干]` Flowers appearing on the earth—the time of singing and new life has come. → 花开在地上——歌唱和新生命的时候到了。"""
    normalized_text_zh: str = """"""
    subject: str = "Flowers 花/生命"
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
        l1_anchor="dvd_v1.0.0_flowers_花_生命_001_L1",
    )
    version: str = "1.0.0"
