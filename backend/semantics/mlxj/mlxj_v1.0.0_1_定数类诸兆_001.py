"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.827657
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
    semantic_id="mlxj_v1.0.0_1_定数类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1定数类诸兆(SemanticEntry):
    """
    #### 科名前定

**吉类**：
- 名当显何年：功名显达数由前定
- 榜中见人姓名：金银榜主台鼎
- 神示科名：有祈必应有感必通

#### 寿数报应

**贞吉否凶类**：
- 三十七之数：杨...
    """
    
    original_text: str = """#### 科名前定

**吉类**：
- 名当显何年：功名显达数由前定
- 榜中见人姓名：金银榜主台鼎
- 神示科名：有祈必应有感必通

#### 寿数报应

**贞吉否凶类**：
- 三十七之数：杨大年典故
- 孔子之年：谯周梦孔子，七十三卒
- 七九之年：李德裕典故，六十三卒于朱崖
- 当食万羊：李德裕平生食万羊
- 四十当贵：裴寂典故
- 一榜二十六人：樊系典故
- 鹿皮之数：吉士瞻梦得十一领鹿皮
- 前后各三年：黄廓无子祈梦

#### 典故

- 杨大年梦怀玉山点字：三十七改为四十七
- 李德裕梦牧羊者：平生所食万羊
- 樊系梦及第榜：人数皆验"""
    normalized_text_zh: str = """"""
    subject: str = "1 定数类诸兆"
    factor_refs: list = []
    
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
        l1_anchor="mlxj_v1.0.0_1_定数类诸兆_001_L1",
    )
    version: str = "1.0.0"
