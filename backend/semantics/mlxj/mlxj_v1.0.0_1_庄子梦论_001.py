"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808916
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
    semantic_id="mlxj_v1.0.0_1_庄子梦论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1庄子梦论(SemanticEntry):
    """
    #### 原文（source_text）

梦饮酒者，旦而哭泣；梦哭泣者，且而田猎。方其梦也，不知其梦也。梦之中又占其梦焉，觉而后知其为梦也。且有大觉而后知此其大梦也。而愚者自以为觉，窃窃然智之。君乎...
    """
    
    original_text: str = """#### 原文（source_text）

梦饮酒者，旦而哭泣；梦哭泣者，且而田猎。方其梦也，不知其梦也。梦之中又占其梦焉，觉而后知其为梦也。且有大觉而后知此其大梦也。而愚者自以为觉，窃窃然智之。君乎牧，固哉！丘与汝皆梦也。予谓汝梦亦梦也。是其言也。其名为吊诡。

汝梦为鸟而厉乎天，梦为鱼而没于渊，不识今之意者，其觉者耶？其梦者耶？其寐也魂交，其觉也形开。

#### 规范化释义（primary_lang_explained）

《庄子》梦论：梦饮酒者，早晨哭泣；梦哭泣者，白天田猎。正在做梦时，不知道是在做梦。梦中又占其梦，醒后才知是梦。且有大觉之人才知这一切都是大梦。愚者自以为觉醒，窃窃自得其智。孔丘与汝都在梦中。我说汝在梦，这话本身也是梦。这种说法叫做「吊诡」。

你梦为鸟而飞于天，梦为鱼而没于渊，不知道现在说话的人是觉者还是梦者。睡眠时魂交游，觉醒时形体开。

#### 核心要点

- 来源：《庄子》
- 核心观点：梦觉难辨，大觉方知大梦
- 名句：其寐也魂交，其觉也形开"""
    normalized_text_zh: str = """"""
    subject: str = "1 庄子梦论"
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
        l1_anchor="mlxj_v1.0.0_1_庄子梦论_001_L1",
    )
    version: str = "1.0.0"
