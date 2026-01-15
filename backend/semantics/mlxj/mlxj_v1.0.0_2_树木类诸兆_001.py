"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.802928
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
    semantic_id="mlxj_v1.0.0_2_树木类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2树木类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 树木茂盛大吉：家业兴隆
- 树木成林大吉：方兴未艾
- 树木火烧大吉：昌明之象，培植阴德
- 木现五色大吉：祥瑞异常

**吉类**：
- 大树荫体吉：贵人...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 树木茂盛大吉：家业兴隆
- 树木成林大吉：方兴未艾
- 树木火烧大吉：昌明之象，培植阴德
- 木现五色大吉：祥瑞异常

**吉类**：
- 大树荫体吉：贵人护庇
- 身立大木吉：登三台八座

**凶类**：
- 树木凋零枯死凶：剥落之象
- 风吹树木落叶拔根凶：不测之祸
- 身入木中凶：身危之象
- 大树落屋上凶：木克土

#### 树木位置象征

| 位置 | 主应 |
|------|------|
| 家中 | 幽隐之兆 |
| 山顶 | 高位 |
| 水边 | 清雅 |
| 路旁 | 行旅 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 树木类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_树木类诸兆_001_L1",
    )
    version: str = "1.0.0"
