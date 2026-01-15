"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402042
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
    semantic_id="dvd_v1.0.0_dog_狗_攻击_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Dog狗攻击(SemanticEntry):
    """
    ### Source Text

> **Dog**: If negative, a dog speaks of attack coming from the world. It can also s...
    """
    
    original_text: str = """### Source Text

> **Dog**: If negative, a dog speaks of attack coming from the world. It can also speak about a spirit of fear. If positive, it can represent trust and loyalty.
> In dreams, if you dream about your pet dog, look up "Pet." If afraid of dogs, they represent fear. If you love dogs, they speak of joy or blessing.
> Psalms 22:16 "For dogs have surrounded me: the assembly of the wicked have enclosed me."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Dog | 狗 | 攻击或忠诚 |
| Fear | 恐惧 | 负面的灵 |
| Loyalty | 忠诚 | 正面的品质 |
| Attack | 攻击 | 来自世界的敌意 |

### English Paraphrase

Dogs can be positive or negative depending on context. In dreams, your pet dog may represent joy or blessing if you love dogs, or fear if afraid of them. In visions, dogs speak of attack from the world or demonic assault. They do not have positive connotation in Scripture.

### Chinese Interpretation

狗可正可负取决于上下文。在梦中，如果你爱狗，宠物狗可能代表喜乐或祝福；如果害怕狗，则代表恐惧。在异象中，狗象征来自世界的攻击或邪灵的攻击。在圣经中它们没有正面含义。

### Core Points

1. **正负皆可**: 个人经验决定含义
2. **恐惧象征**: 对害怕狗的人代表恐惧
3. **攻击象征**: 在异象中代表仇敌的攻击
4. **宠物例外**: 自己的宠物可能正面

### Narrative Snippets

- `[ns_dav_d018]` `[trigger: dog_attack]` `[factor_trigger: dream_dog AND dream_attack]` `[role: 主干]` Dogs in visions speak of attack from the enemy seeking to devour and destroy you. → 异象中的狗象征仇敌的攻击，企图吞噬和毁灭你。
- `[ns_dav_d019]` `[trigger: dog_fear]` `[factor_trigger: dream_dog AND dream_fear]` `[role: 条件]` If you are afraid of dogs, they represent fear in your dreams. → 如果你害怕狗，它们在你梦中代表恐惧。"""
    normalized_text_zh: str = """"""
    subject: str = "Dog 狗/攻击"
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
        l1_anchor="dvd_v1.0.0_dog_狗_攻击_001_L1",
    )
    version: str = "1.0.0"
