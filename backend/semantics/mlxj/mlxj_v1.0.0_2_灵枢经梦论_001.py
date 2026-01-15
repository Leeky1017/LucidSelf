"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808881
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
    semantic_id="mlxj_v1.0.0_2_灵枢经梦论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2灵枢经梦论(SemanticEntry):
    """
    #### 原文（source_text）

正邪从外袭内，而未有定舍，反淫于藏，不得定处，与荣卫俱行，而与魂魄飞扬，使人卧不得安而喜梦。气淫于府，则有余于外，不足于内；气淫于藏，则有余于内，不足于外。...
    """
    
    original_text: str = """#### 原文（source_text）

正邪从外袭内，而未有定舍，反淫于藏，不得定处，与荣卫俱行，而与魂魄飞扬，使人卧不得安而喜梦。气淫于府，则有余于外，不足于内；气淫于藏，则有余于内，不足于外。

故阴气盛则梦涉大水而恐惧；阳气盛，则梦大火而燔灼。阴阳俱盛，则梦相杀；上盛则梦飞，下盛则梦坠，甚饥则梦取，甚饱则梦予。

肝气盛则梦怒，肺气盛则梦恐惧、哭泣飞扬；心气盛则梦喜笑恐畏；脾气盛则梦歌乐、身体重不举；肾气盛则梦腰脊两解不属。凡此十二盛者，至而写之立已。

#### 规范化释义（primary_lang_explained）

《灵枢经》论梦：正邪从外袭入内部，未有定处，反淫于脏腑，不得安定，与营卫俱行，与魂魄飞扬，使人卧不安而喜梦。气淫于府则有余于外、不足于内；气淫于脏则有余于内、不足于外。

阴阳盛衰与梦象：
- **阴气盛**：梦涉大水而恐惧
- **阳气盛**：梦大火而燔灼
- **阴阳俱盛**：梦相杀
- **上盛**：梦飞
- **下盛**：梦坠
- **甚饥**：梦取
- **甚饱**：梦予

五脏气盛与梦象：
- **肝气盛**：梦怒
- **肺气盛**：梦恐惧、哭泣飞扬
- **心气盛**：梦喜笑恐畏
- **脾气盛**：梦歌乐、身体重不举
- **肾气盛**：梦腰脊两解不属

凡此十二盛者，至而泻之立已。

#### 核心要点

- 来源：《黄帝内经·灵枢》
- 理论：阴阳盛衰、五脏气盛导致特定梦象
- 治法：至而泻之立已"""
    normalized_text_zh: str = """"""
    subject: str = "2 灵枢经梦论"
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
        l1_anchor="mlxj_v1.0.0_2_灵枢经梦论_001_L1",
    )
    version: str = "1.0.0"
