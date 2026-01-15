"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.814377
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
    semantic_id="mlxj_v1.0.0_1_第宅类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1第宅类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 门楣生五色芝：文章之兆（王祎典故）
- 店门高耸品物充盈大吉：年丰家富
- 会饮肆中吉：获财之兆

**凶类**：
- 四顾无人舍凶：疾病死亡
- 高墙坚壁：...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 门楣生五色芝：文章之兆（王祎典故）
- 店门高耸品物充盈大吉：年丰家富
- 会饮肆中吉：获财之兆

**凶类**：
- 四顾无人舍凶：疾病死亡
- 高墙坚壁：将有囹圄
- 屋坏凶：赵王伦典故，祸患将至
- 堂下开店舍否凶：胸有贪私

#### 典故

- 王德亨梦邻屋颓：邻家水客被杀，后得廉州巡检
- 赵王伦梦屋坏：是夜难作，华遂被害"""
    normalized_text_zh: str = """"""
    subject: str = "1 第宅类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_第宅类诸兆_001_L1",
    )
    version: str = "1.0.0"
