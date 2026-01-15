"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808891
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
    semantic_id="mlxj_v1.0.0_3_灵枢厥气客梦论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3灵枢厥气客梦论(SemanticEntry):
    """
    #### 原文（source_text）

厥气客于心，则梦见丘山烟火；客于肺，则梦飞扬，见金铁之奇物；客于肝则梦山林树木；客于脾则梦见丘陵大泽、坏屋风雨；客于肾，则梦临渊没，居水中；客于膀胱则梦游行...
    """
    
    original_text: str = """#### 原文（source_text）

厥气客于心，则梦见丘山烟火；客于肺，则梦飞扬，见金铁之奇物；客于肝则梦山林树木；客于脾则梦见丘陵大泽、坏屋风雨；客于肾，则梦临渊没，居水中；客于膀胱则梦游行；客于胃则梦饮食；客于大肠则梦田野；客于小肠则梦聚邑冲衢；客于胆则梦斗讼自刳；客于阴器则梦接内；客于项则梦斩首；客于胫则梦行走而不能前，及居深地茆苑中；客于股肱则梦礼节拜起；客于胞络则梦溲便。

凡此十五不足者，至而补之，立已也。

#### 规范化释义（primary_lang_explained）

《灵枢经》厥气客梦论：邪气（厥气）客于不同部位产生不同梦象：

| 客于部位 | 梦象 |
|---------|------|
| 心 | 丘山烟火 |
| 肺 | 飞扬，见金铁之奇物 |
| 肝 | 山林树木 |
| 脾 | 丘陵大泽、坏屋风雨 |
| 肾 | 临渊没，居水中 |
| 膀胱 | 游行 |
| 胃 | 饮食 |
| 大肠 | 田野 |
| 小肠 | 聚邑冲衢 |
| 胆 | 斗讼自刳 |
| 阴器 | 接内（房事） |
| 项 | 斩首 |
| 胫 | 行走不能前，居深地茆苑中 |
| 股肱 | 礼节拜起 |
| 胞络 | 溲便 |

凡此十五不足者，至而补之，立已。"""
    normalized_text_zh: str = """"""
    subject: str = "3 灵枢厥气客梦论"
    factor_refs: list = ['wuzang_qixu_meng', 'jueqi_ke_meng']
    
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
        l1_anchor="mlxj_v1.0.0_3_灵枢厥气客梦论_001_L1",
    )
    version: str = "1.0.0"
