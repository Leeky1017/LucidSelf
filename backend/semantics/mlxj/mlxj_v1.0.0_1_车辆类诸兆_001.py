"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.799594
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
    semantic_id="mlxj_v1.0.0_1_车辆类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1车辆类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 车前后数十乘：特恩封拜
- 车三乘连行大道：捷报喜庆
- 乘轿登云：名登高第

**吉类**：
- 乘轿途中：荣贵
- 坐轿登舟：远行
- 轿入城：家事有喜...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 车前后数十乘：特恩封拜
- 车三乘连行大道：捷报喜庆
- 乘轿登云：名登高第

**吉类**：
- 乘轿途中：荣贵
- 坐轿登舟：远行
- 轿入城：家事有喜

**凶类**：
- 轿无人抬：行事不遂
- 轿出门：分别
- 面前一轿无人：事有阻
- 轿行水中：遁避逃窜

#### 车轿典故

潘择可典故：梦挽车三十辆，弟端甫随后。至政和三年端甫就恩科，相去三十年，乃悟挽车者三十载也。"""
    normalized_text_zh: str = """"""
    subject: str = "1 车辆类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_车辆类诸兆_001_L1",
    )
    version: str = "1.0.0"
