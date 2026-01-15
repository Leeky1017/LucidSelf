"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.836925
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
    semantic_id="mlxj_v1.0.0_1_以刀开心_心胸类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1以刀开心心胸类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

以刀开心，大吉。刀者，肺之气，持刀者，肺之神，肺为心之华盖。梦刀开心，心窍通也。诸难解，百忧去。郑玄师马融三年，将去，过树阴下假寐，忽梦一人以刀开其心，语之...
    """
    
    original_text: str = """#### 原文（source_text）

以刀开心，大吉。刀者，肺之气，持刀者，肺之神，肺为心之华盖。梦刀开心，心窍通也。诸难解，百忧去。郑玄师马融三年，将去，过树阴下假寐，忽梦一人以刀开其心，语之曰：今可学矣。返而复卒业，遂精于典籍，后东归，为名儒。

#### 规范化释义（primary_lang_explained）

梦见用刀打开心，大吉。刀是肺之气，持刀者是肺之神，肺是心的华盖。梦见刀开心，是心窍通达之象。诸难解除，百忧消去。

郑玄师从马融三年，将要离去时，在树荫下小睡，忽然梦见一人用刀打开他的心，对他说：「现在可以学习了。」返回后继续完成学业，遂精通典籍，后来东归，成为名儒。

#### 完整对等诠释（secondary_lang_full）

Dreaming of opening the heart with a knife is greatly auspicious. The knife represents lung qi, the knife-holder is the lung spirit, and the lungs are the canopy of the heart. Dreaming of opening the heart with a knife signifies the opening of heart apertures. All difficulties dissolve, all worries depart.

Zheng Xuan studied under Ma Rong for three years. When about to leave, he napped under a tree and suddenly dreamed of someone opening his heart with a knife, saying: "Now you may learn." He returned to complete his studies, became proficient in the classics, and later returned east to become a renowned scholar.

#### 核心要点

- 刀开心=心窍通=智慧开启
- 刀=肺气，肺=心之华盖（五行金生水、水生木关系）
- 诸难解，百忧去=困难消除
- 郑玄典故：梦后精通典籍，成名儒"""
    normalized_text_zh: str = """"""
    subject: str = "1 以刀开心（心胸类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_以刀开心_心胸类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
