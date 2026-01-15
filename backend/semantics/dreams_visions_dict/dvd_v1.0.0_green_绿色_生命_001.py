"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.390720
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
    semantic_id="dvd_v1.0.0_green_绿色_生命_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Green绿色生命(SemanticEntry):
    """
    ### Source Text

> **Green**: A picture of life, growth, and prosperity. Also speaks of envy negativ...
    """
    
    original_text: str = """### Source Text

> **Green**: A picture of life, growth, and prosperity. Also speaks of envy negatively.
> Positive: Green speaks of life and vitality—things growing and flourishing. Evergreen represents eternal life. Green light means "go."
> Negative: Green with envy speaks of jealousy. Sickly green indicates disease or decay.
> Psalms 92:14 "They shall still bring forth fruit in old age; they shall be fat and flourishing."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Green | 绿色 | 生命和成长 |
| Life | 生命 | 活力和繁荣 |
| Growth | 成长 | 生长和发展 |
| Envy | 嫉妒 | 负面的绿 |

### English Paraphrase

Green represents life, growth, and prosperity—also envy negatively. Green speaks of vitality and flourishing. Evergreen represents eternal life. Green light means "go." Green with envy speaks of jealousy. Sickly green indicates disease.

### Chinese Interpretation

绿色代表生命、成长和繁荣——负面也代表嫉妒。绿色象征活力和茂盛。常青代表永生。绿灯意味着"可以走"。嫉妒的绿象征妒忌。病态的绿表示疾病。

### Core Points

1. **正负皆可**: 绿色状态决定含义
2. **生命象征**: 活力和繁荣
3. **永生记号**: 常青树代表永生
4. **嫉妒警告**: 嫉妒的绿是负面

### Narrative Snippets

- `[ns_dav_g013]` `[trigger: green_life]` `[factor_trigger: dream_green AND dream_life]` `[role: 主干]` Green speaks of life and vitality—things growing, flourishing, and prospering. → 绿色象征生命和活力——事物生长、茂盛和繁荣。
- `[ns_dav_g014]` `[trigger: green_envy]` `[factor_trigger: dream_green AND dream_envy]` `[role: 警告]` Green with envy speaks of jealousy—a negative spiritual condition that needs to be addressed. → 嫉妒的绿象征妒忌——需要处理的负面属灵状态。"""
    normalized_text_zh: str = """"""
    subject: str = "Green 绿色/生命"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="dvd_v1.0.0_green_绿色_生命_001_L1",
    )
    version: str = "1.0.0"
