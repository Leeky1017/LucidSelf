"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439755
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
    semantic_id="dvd_v1.0.0_animals__general__动物_总论_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class AnimalsGeneral动物总论(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: Depending on the animal, the interpretation for your dream w...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: Depending on the animal, the interpretation for your dream will change. In a dream it is important to identify your view or relationship with the animal. If the animal is a pet, then it could speak of your responsibilities.

In visions or prophetic dreams, animals have quite clear interpretations in the Scriptures. Some are a source of blessing and others a picture of the attack of the enemy.

**See also**: Alligator, Badger, Bat, Bear, Calf, Camel, Horse, Lamb, Lion

### English Paraphrase

Animals in dreams require identifying your relationship with them. Pets = responsibilities. In prophetic dreams/visions, animals have clear biblical interpretations—some represent blessing, others enemy attack. Consult specific animal entries for detailed meanings.

### Chinese Interpretation（完整对等诠释）

梦中的动物需要辨别你与它们的关系。宠物 = 责任。在先知性梦境/异象中，动物有明确的圣经解释——有些代表祝福，有些代表仇敌攻击。查阅具体动物条目获取详细含义。

### Narrative Snippets

- `[ns_dav_a056]` `[trigger: 梦动物]` `[factor_trigger: dream_symbol_animals]` `[role: 主干]` Animals depend on your relationship with them and biblical symbolism—blessing or enemy attack. → Dreams Dictionary #Animals"""
    normalized_text_zh: str = """"""
    subject: str = "Animals (General) 动物（总论）"
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
        l1_anchor="dvd_v1.0.0_animals__general__动物_总论_001_L1",
    )
    version: str = "1.0.0"
