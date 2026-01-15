"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.390682
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
    semantic_id="dvd_v1.0.0_glasses_眼镜_洞察_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Glasses眼镜洞察(SemanticEntry):
    """
    ### Source Text

> **Glasses**: A picture of spiritual sight and discernment—the ability to see clea...
    """
    
    original_text: str = """### Source Text

> **Glasses**: A picture of spiritual sight and discernment—the ability to see clearly.
> Positive: Putting on glasses speaks of receiving spiritual insight—seeing what was blurry before. Reading glasses indicate understanding the Word. Sunglasses can indicate protection.
> Negative: Broken glasses speak of impaired vision. Rose-colored glasses indicate deception—seeing things as you want rather than as they are.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Glasses | 眼镜 | 属灵的看见 |
| Sight | 视力 | 清晰地看 |
| Discernment | 洞察 | 辨别能力 |
| Deception | 迷惑 | 看事物不真实 |

### English Paraphrase

Glasses represent spiritual sight and discernment—the ability to see clearly. Putting on glasses speaks of receiving spiritual insight. Reading glasses indicate understanding the Word. Broken glasses speak of impaired vision. Rose-colored glasses indicate deception.

### Chinese Interpretation

眼镜代表属灵的看见和洞察——清晰看事物的能力。戴上眼镜象征接受属灵的洞见。阅读眼镜表示理解神的话语。破损的眼镜象征受损的视力。玫瑰色眼镜表示迷惑。

### Core Points

1. **正负皆可**: 眼镜状态决定含义
2. **洞察恩赐**: 看见隐藏的事物
3. **话语理解**: 阅读眼镜理解圣经
4. **迷惑警告**: 玫瑰色眼镜不真实

### Narrative Snippets

- `[ns_dav_g005]` `[trigger: glasses_insight]` `[factor_trigger: dream_glasses AND dream_insight]` `[role: 主干]` Putting on glasses speaks of receiving spiritual insight—seeing what was blurry before. → 戴上眼镜象征接受属灵的洞见——看清之前模糊的事物。
- `[ns_dav_g006]` `[trigger: glasses_deception]` `[factor_trigger: dream_glasses AND dream_deception]` `[role: 警告]` Rose-colored glasses indicate deception—seeing things as you want rather than as they are. → 玫瑰色眼镜表示迷惑——按你想要的而非真实的方式看事物。"""
    normalized_text_zh: str = """"""
    subject: str = "Glasses 眼镜/洞察"
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
        l1_anchor="dvd_v1.0.0_glasses_眼镜_洞察_001_L1",
    )
    version: str = "1.0.0"
