"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402052
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
    semantic_id="dvd_v1.0.0_donkey_驴_谦卑_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Donkey驴谦卑(SemanticEntry):
    """
    ### Source Text

> **Donkey**: The donkey is passive and a picture of humility. Used for cargo, to h...
    """
    
    original_text: str = """### Source Text

> **Donkey**: The donkey is passive and a picture of humility. Used for cargo, to have many spoke of wealth. Negatively, a donkey is a picture of stubbornness.
> Jesus seated himself on a donkey instead of a grand horse—presenting a picture of meekness. A war horse brings fear; a donkey does not.
> John 12:15 "Fear not, daughter of Zion: behold, your King is coming, sitting on a donkey's colt."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Donkey | 驴 | 谦卑或固执 |
| Humility | 谦卑 | 耶稣的榜样 |
| Stubbornness | 固执 | 负面的性格 |
| Wealth | 财富 | 作为货运工具 |

### English Paraphrase

A donkey represents humility—Jesus chose a donkey over a horse, presenting meekness. Many donkeys indicated wealth as beasts of burden. Negatively, donkeys represent stubbornness—being deaf to God's voice like Balaam who needed a donkey to speak to him.

### Chinese Interpretation

驴代表谦卑——耶稣选择驴而非马，呈现柔和。许多驴作为货运牲畜代表财富。负面而言，驴代表固执——像巴兰一样对神的声音充耳不闻，需要驴来对他说话。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **谦卑榜样**: 耶稣选择驴而非战马
3. **财务祝福**: 许多驴代表财富
4. **固执警告**: 不听神声音的象征

### Narrative Snippets

- `[ns_dav_d020]` `[trigger: donkey_humility]` `[factor_trigger: dream_donkey AND dream_humility]` `[role: 主干]` Jesus seated on a donkey presented a picture of meekness—not to bring fear but to lead gently. → 耶稣坐在驴上呈现柔和的画面——不是带来恐惧而是温柔地引导。
- `[ns_dav_d021]` `[trigger: donkey_stubborn]` `[factor_trigger: dream_donkey AND dream_stubborn]` `[role: 警告]` A donkey in a negative sense speaks of stubbornness—being deaf to the voice of God. → 负面而言，驴象征固执——对神的声音充耳不闻。"""
    normalized_text_zh: str = """"""
    subject: str = "Donkey 驴/谦卑"
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
        l1_anchor="dvd_v1.0.0_donkey_驴_谦卑_001_L1",
    )
    version: str = "1.0.0"
