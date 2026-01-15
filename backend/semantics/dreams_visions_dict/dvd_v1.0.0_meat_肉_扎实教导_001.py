"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396187
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
    semantic_id="dvd_v1.0.0_meat_肉_扎实教导_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Meat肉扎实教导(SemanticEntry):
    """
    ### Source Text

> **Meat**: Universally, meat is a picture of food and having your hunger met. It i...
    """
    
    original_text: str = """### Source Text

> **Meat**: Universally, meat is a picture of food and having your hunger met. It is also a picture of solid doctrine. In vision, meat represents the more complex teachings of the Word—preparing it so it's appealing to others.
> Negative: Eating meat can speak of gluttony and fulfilling the flesh. The Israelites ate quails until they became sick—temporal values turning blessing into sin.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Meat | 肉 | 扎实的教导 |
| Doctrine | 教义 | 神话语的教导 |
| Solid | 扎实 | 成熟的内容 |
| Gluttony | 贪食 | 满足肉体 |

### English Paraphrase

Meat represents food, satisfaction, and solid doctrine. It pictures complex teachings of the Word—preparing it to appeal to others. Negatively, meat can speak of gluttony and flesh. The Israelites ate quails until sick—temporal values turning blessings into sin.

### Chinese Interpretation

肉代表食物、满足和扎实的教义。它象征话语中复杂的教导——使之吸引他人。负面而言，肉可以象征贪食和肉体。以色列人吃鹌鹑直到生病——暂时的价值观使祝福变成罪。

### Core Points

1. **正负皆可**: 吃肉方式决定含义
2. **教义象征**: 扎实的属灵喂养
3. **教导准备**: 使话语吸引人
4. **贪食警告**: 可能是满足肉体

### Narrative Snippets

- `[ns_dav_m005]` `[trigger: meat_doctrine]` `[factor_trigger: dream_meat AND dream_doctrine]` `[role: 主干]` Meat represents the more complex teachings of the Word—solid doctrine for mature believers. → 肉代表话语中更复杂的教导——给成熟信徒的扎实教义。
- `[ns_dav_m006]` `[trigger: meat_gluttony]` `[factor_trigger: dream_meat AND dream_gluttony]` `[role: 警告]` Eating meat can speak of gluttony and fulfilling only the desires of the flesh. → 吃肉可以象征贪食和只满足肉体的欲望。"""
    normalized_text_zh: str = """"""
    subject: str = "Meat 肉/扎实教导"
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
        l1_anchor="dvd_v1.0.0_meat_肉_扎实教导_001_L1",
    )
    version: str = "1.0.0"
