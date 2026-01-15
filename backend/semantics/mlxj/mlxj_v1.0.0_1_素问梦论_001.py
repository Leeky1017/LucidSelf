"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808855
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
    semantic_id="mlxj_v1.0.0_1_素问梦论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1素问梦论(SemanticEntry):
    """
    #### 原文（source_text）

秋刺夏分病不已，令人益嗜卧，又且善梦。少气之厥，令人妄梦。其极至迷，三阳绝，三阴微，是为少气。

是以肺气虚，则使人梦见白物，见人斩血籍籍，得其时则梦见兵战...
    """
    
    original_text: str = """#### 原文（source_text）

秋刺夏分病不已，令人益嗜卧，又且善梦。少气之厥，令人妄梦。其极至迷，三阳绝，三阴微，是为少气。

是以肺气虚，则使人梦见白物，见人斩血籍籍，得其时则梦见兵战；肾气虚，则使人梦见舟船溺人，得其时则梦伏水中，若有畏恐。肝气虚，则梦见菌香生草；得其时，则梦伏树下，不敢起。心气虚，则梦救火阳物，得其时则梦燔灼；脾气虚，则梦饮食不足，得其时则梦筑垣盖屋。

此皆五藏气虚，阳气有余，阴气不足，合之五诊，调之阴阳，以在经脉。

#### 规范化释义（primary_lang_explained）

《素问》论梦：秋季误刺夏分之穴，病不愈者，令人嗜睡且善梦。少气而厥者，令人妄梦。极则迷乱，三阳绝、三阴微，是为少气。

五脏气虚与梦象的对应：
- **肺气虚**：梦见白物、见人斩血籍籍；得其时（秋）则梦见兵战
- **肾气虚**：梦见舟船溺人；得其时（冬）则梦伏水中、若有畏恐
- **肝气虚**：梦见菌香生草；得其时（春）则梦伏树下、不敢起
- **心气虚**：梦救火阳物；得其时（夏）则梦燔灼
- **脾气虚**：梦饮食不足；得其时（长夏/四季）则梦筑垣盖屋

此皆五脏气虚、阳气有余、阴气不足所致，需合五诊、调阴阳、治经脉。

#### 核心要点

- 来源：《黄帝内经·素问》
- 理论：五脏气虚导致特定梦象
- 时令因素：得其时则梦象更显

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v29_001]` `[trigger: 素问梦论]` `[factor_trigger: suwen_dream_theory AND dream_xiang AND wuzang_qixu AND wuzang_qisheng AND yinyang_shengshui]` `[role: 医学基础]` 肺气虚则梦见白物，肾气虚则梦见舟船溺人，肝气虚则梦见菌香生草。五脏气盛衰、阴阳盛衰皆影响梦象。 → 《梦林玄解·卷二十九》#素问
- `[ns_mlxj_v29_core]` `[trigger: 梦原理论]` `[factor_trigger: dream_theory AND dream_category AND liumeng AND meng_benzhi AND dadream]` `[role: 理论框架]` 梦之分类与原理，六梦为正噩思寔喜惧，梦之本质。 → 《梦林玄解·卷二十九》#梦原
- `[ns_mlxj_v29_002]` `[trigger: 三梦占法]` `[factor_trigger: sanmeng_fa AND shimeng AND zhilai_jing]` `[role: 占法]` 大卜三梦之法，十梦分类，致来之精。 → 《梦林玄解·卷二十九》#三梦
- `[ns_mlxj_v29_003]` `[trigger: 魂魄神形]` `[factor_trigger: hunpo AND shenxing AND jueqi_kechu AND dream_jue]` `[role: 理论基础]` 魂魄交接、神形相遇、厥气客处生梦。 → 《梦林玄解·卷二十九》#魂魄"""
    normalized_text_zh: str = """"""
    subject: str = "1 素问梦论"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_素问梦论_001_L1",
    )
    version: str = "1.0.0"
