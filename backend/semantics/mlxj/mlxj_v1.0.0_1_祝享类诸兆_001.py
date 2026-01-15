"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.853846
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
    semantic_id="mlxj_v1.0.0_1_祝享类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1祝享类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 行郊社之礼：建功勋如反掌
- 作五祀之仪：树恒产以荣身
- 焚香焚帛行祼：大吉
- 受福送服：大吉
- 鸣钟击鼓设乐：大吉
- 饮福受胙大吉：人君梦之万民安...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 行郊社之礼：建功勋如反掌
- 作五祀之仪：树恒产以荣身
- 焚香焚帛行祼：大吉
- 受福送服：大吉
- 鸣钟击鼓设乐：大吉
- 饮福受胙大吉：人君梦之万民安泰

**吉类**：
- 奠祖考：人子之孝心
- 奠亲邻：人友之大事
- 摆设楮帛刍狗高烛：阿睹中物不期而至

#### 典故

周宣解梦刍狗三梦：
1. 第一梦：得美食
2. 第二梦：堕车折脚
3. 第三梦：家中天火

刍狗为祭神之物，三次梦应不同：祭前→饮食，祭后→车铄，樵后→火灾。"""
    normalized_text_zh: str = """"""
    subject: str = "1 祝享类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_祝享类诸兆_001_L1",
    )
    version: str = "1.0.0"
