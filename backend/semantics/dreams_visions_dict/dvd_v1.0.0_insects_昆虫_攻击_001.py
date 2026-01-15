"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429226
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
    semantic_id="dvd_v1.0.0_insects_昆虫_攻击_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Insects昆虫攻击(SemanticEntry):
    """
    ### Source Text

> **Insects**: In prophetic dreams or visions with negative connotation, insects sp...
    """
    
    original_text: str = """### Source Text

> **Insects**: In prophetic dreams or visions with negative connotation, insects speak of: Destruction, attack from enemy, negative words, things that annoy, things that bring fear, a spirit of destruction, the presence of Satan (Lord of the Flies).
> Positive: Crushing insects means overcoming something negative. A lady bug pollinates fruit and assists fruitfulness.
> Negative: Cockroaches represent small sins that crept into your life.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Insects | 昆虫 | 攻击和破坏 |
| Destruction | 毁灭 | 仇敌的工作 |
| Flies | 苍蝇 | 撒但的象征 |
| Cockroaches | 蟑螂 | 小罪的象征 |

### English Paraphrase

Insects in negative contexts speak of destruction, enemy attack, negative words, annoyances, fear, and Satan's presence. Crushing insects means overcoming negativity. Cockroaches represent small sins. Flies are tied to Beelzebub, Lord of the Flies.

### Chinese Interpretation

昆虫在负面语境中象征毁灭、仇敌攻击、负面话语、烦扰、恐惧和撒但的同在。压碎昆虫意味着克服负面事物。蟑螂代表小罪。苍蝇与别西卜（苍蝇之主）相关。

### Core Points

1. **正负皆可**: 行动决定含义
2. **攻击象征**: 仇敌的工作
3. **小罪警告**: 蟑螂代表小罪
4. **克服胜利**: 压碎昆虫是得胜

### Narrative Snippets

- `[ns_dav_i004]` `[trigger: insects_attack]` `[factor_trigger: dream_insects AND dream_attack]` `[role: 警告]` Insects in negative contexts speak of destruction, enemy attack, and the presence of Satan. → 昆虫在负面语境中象征毁灭、仇敌攻击和撒但的同在。
- `[ns_dav_i005]` `[trigger: insects_overcome]` `[factor_trigger: dream_insects AND dream_overcome]` `[role: 主干]` Crushing insects means you are overcoming something negative in your life. → 压碎昆虫意味着你正在克服生命中的负面事物。"""
    normalized_text_zh: str = """"""
    subject: str = "Insects 昆虫/攻击"
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
        l1_anchor="dvd_v1.0.0_insects_昆虫_攻击_001_L1",
    )
    version: str = "1.0.0"
