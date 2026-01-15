"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.829255
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
    semantic_id="mlxj_v1.0.0_2_冠冕类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2冠冕类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 冕旒大吉：大喜庆事
- 冲天冠吉：缙绅得宠任，青衿得显荣
- 皮弁吉：必得官爵

**吉类**：
- 紫金冠：逢凶化吉，遇难生祥
- 鱼尾冠贞吉：羽士服饰
...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 冕旒大吉：大喜庆事
- 冲天冠吉：缙绅得宠任，青衿得显荣
- 皮弁吉：必得官爵

**吉类**：
- 紫金冠：逢凶化吉，遇难生祥
- 鱼尾冠贞吉：羽士服饰

**凶类**：
- 戴网巾凶：囹圄之兆
- 戴破帻贞吉：解灾散祸

#### 典故

- 梁武帝敕贺革：梦湘东王脱冠授之，后膺归运
- 铁冠宋熙宁：徐熙春遇方士铁冠道服"""
    normalized_text_zh: str = """"""
    subject: str = "2 冠冕类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_冠冕类诸兆_001_L1",
    )
    version: str = "1.0.0"
