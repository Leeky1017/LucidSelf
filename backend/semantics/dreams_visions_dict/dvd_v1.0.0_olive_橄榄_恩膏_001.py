"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433481
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
    semantic_id="dvd_v1.0.0_olive_橄榄_恩膏_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Olive橄榄恩膏(SemanticEntry):
    """
    ### Source Text

> **Olive**: Olive oil is a picture of the anointing and healing. Olive crushed let...
    """
    
    original_text: str = """### Source Text

> **Olive**: Olive oil is a picture of the anointing and healing. Olive crushed letting out oil speaks of when pressures come, what comes out is the anointing. An olive tree is a picture of abundance and reproducing blessing.
> Negative: A branch being severed and new one grafted speaks of God removing a person and bringing someone new. Olive bearing fruit other than olives means things are not what they seem.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Olive | 橄榄 | 恩膏和医治 |
| Crushed | 压榨 | 压力下出油 |
| Tree | 树 | 丰盛和繁衍 |
| Grafted | 嫁接 | 新的取代旧的 |

### English Paraphrase

Olive oil pictures anointing and healing. Olive crushed speaks of what comes out under pressure—the anointing. An olive tree represents abundance and reproducing blessing. A severed branch with new one grafted speaks of God removing someone and bringing another. Olive bearing other fruit means things are not what they seem.

### Chinese Interpretation

橄榄油象征恩膏和医治。橄榄被压榨象征压力下出来的东西——恩膏。橄榄树代表丰盛和繁衍的祝福。被砍断的枝子和嫁接的新枝象征神移除一个人带来另一个人。橄榄结出其他果子意味着事情不是看起来那样。

### Core Points

1. **正负皆可**: 橄榄状态决定含义
2. **恩膏象征**: 压力下出油
3. **丰盛记号**: 繁衍的祝福
4. **嫁接警告**: 可能有人被替换

### Narrative Snippets

- `[ns_dav_o006]` `[trigger: olive_anointing]` `[factor_trigger: dream_olive AND dream_anointing]` `[role: 主干]` Olive crushed speaks of what comes out under pressure—the anointing flows from you. → 橄榄被压榨象征压力下出来的东西——恩膏从你流出。
- `[ns_dav_o007]` `[trigger: olive_graft]` `[factor_trigger: dream_olive AND dream_graft]` `[role: 警告]` A branch severed and new one grafted speaks of God removing someone and bringing another. → 被砍断的枝子和嫁接的新枝象征神移除一个人带来另一个人。"""
    normalized_text_zh: str = """"""
    subject: str = "Olive 橄榄/恩膏"
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
        l1_anchor="dvd_v1.0.0_olive_橄榄_恩膏_001_L1",
    )
    version: str = "1.0.0"
