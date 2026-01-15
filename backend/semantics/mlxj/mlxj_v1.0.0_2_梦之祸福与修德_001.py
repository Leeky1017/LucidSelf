"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.845097
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
    semantic_id="mlxj_v1.0.0_2_梦之祸福与修德_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2梦之祸福与修德(SemanticEntry):
    """
    #### 原文（source_text）

人之梦兆，祸福形焉。负天之梦，叔孙信之而肇家祸；琼瑰之梦，不齐信之而遽亡身。梦登台者以忧死，梦身执者以反诛。升天折翼之梦，启史臣之疑；乘龙授鼎之梦，来谗人之...
    """
    
    original_text: str = """#### 原文（source_text）

人之梦兆，祸福形焉。负天之梦，叔孙信之而肇家祸；琼瑰之梦，不齐信之而遽亡身。梦登台者以忧死，梦身执者以反诛。升天折翼之梦，启史臣之疑；乘龙授鼎之梦，来谗人之口。祸福固不可测，圣人岂设虚文？人当敬信其言，以图转凶而回吉也。

#### 规范化释义（primary_lang_explained）

人的梦兆蕴含祸福。历史上：叔孙因信「负天」之梦而招致家祸；不齐因信「琼瑰」之梦而遽然亡身；梦登台者因忧而死；梦身被执者因谋反被诛；升天折翼之梦引起史臣疑虑；乘龙授鼎之梦招来谗人口舌。

祸福固然不可测，但圣人设立占梦制度岂是虚文？人应当敬信这些教诲，以图转凶为吉。"""
    normalized_text_zh: str = """"""
    subject: str = "2 梦之祸福与修德"
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
        l1_anchor="mlxj_v1.0.0_2_梦之祸福与修德_001_L1",
    )
    version: str = "1.0.0"
