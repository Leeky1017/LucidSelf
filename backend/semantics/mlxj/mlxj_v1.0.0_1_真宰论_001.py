"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808945
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
    semantic_id="mlxj_v1.0.0_1_真宰论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1真宰论(SemanticEntry):
    """
    #### 原文（source_text）

真宰窈冥，无象无形。𭱊蒙浑穆，气数斯涵。气判阴阳，数苞终始，天旋地凝，两间定位，而人物生矣。人葆冲和，肖乎天地，精神融贯，无相盭也。天气为魂，地气为魄，气清...
    """
    
    original_text: str = """#### 原文（source_text）

真宰窈冥，无象无形。𭱊蒙浑穆，气数斯涵。气判阴阳，数苞终始，天旋地凝，两间定位，而人物生矣。人葆冲和，肖乎天地，精神融贯，无相盭也。天气为魂，地气为魄，气清者魄从魂，气浊者魂从魄，从魂为贵，从魄为贱。清魂为贤，浊魄为愚。此寿妖祸福之阃也。

魂能知来，魄能藏往。人之昼兴也，魂丽于目；夜寐也，魄宿于肝。魂丽于目，故能见焉；魄宿于肝，故能梦焉。梦者，神之游，知来之镜也。

#### 规范化释义（primary_lang_explained）

真宰（造化主宰）窈冥无形。混沌之气，涵容气数。气分阴阳，数包终始，天旋地凝，两间定位，人物乃生。人葆冲和之气，肖似天地，精神融贯无相悖。

天气为魂，地气为魄。气清者魄从魂，气浊者魂从魄。从魂为贵，从魄为贱；清魂为贤，浊魄为愚。此乃寿夭祸福之关键。

魂能知来，魄能藏往。人白天醒来，魂附丽于目；夜晚睡眠，魄宿于肝。魂丽于目故能视，魄宿于肝故能梦。梦者，神之游，知来之镜也。

#### 核心要点

- **宇宙论**：真宰无形 → 气判阴阳 → 天旋地凝 → 人物生
- **魂魄论**：天气为魂，地气为魄
- **梦之本质**：梦者，神之游，知来之镜"""
    normalized_text_zh: str = """"""
    subject: str = "1 真宰论"
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
        l1_anchor="mlxj_v1.0.0_1_真宰论_001_L1",
    )
    version: str = "1.0.0"
