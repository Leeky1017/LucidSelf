"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.785819
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
    semantic_id="mlxj_v1.0.0_2_金类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2金类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 金光灿烂大吉：功名赫奕
- 金阙金殿大吉：天上玉帝之庭
- 金凤大吉：富贵荣盛
- 金印累累吉：大贵位

**吉类**：
- 金鱼吉：高爵大贵
- 金钗吉：...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 金光灿烂大吉：功名赫奕
- 金阙金殿大吉：天上玉帝之庭
- 金凤大吉：富贵荣盛
- 金印累累吉：大贵位

**吉类**：
- 金鱼吉：高爵大贵
- 金钗吉：夫妇谐老
- 金针吉：奇逢良医
- 金钩利：开心颖慧
- 金甲吉：守志不屈
- 金牛吉：并吞土地

**贞吉否凶类**：
- 金貂：阴长阳消
- 金镮凶：勾连之兆
- 金钿不利：头绪繁多

#### 典故

- 马蹄金：阚喜梦闻树上呼答，获金百余颗
- 紫磨金：范迈母梦铺杨迈金席，生林邑王
- 金龟：刘赞梦吞金龟得文思，吐金龟后卒"""
    normalized_text_zh: str = """"""
    subject: str = "2 金类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_金类诸兆_001_L1",
    )
    version: str = "1.0.0"
