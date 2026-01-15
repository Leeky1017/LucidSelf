"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.827647
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
    semantic_id="mlxj_v1.0.0_2_名姓类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2名姓类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 天神命名吉：上帝所使
- 神赐姓吉：家计日丰
- 神命字吉：运必亨通
- 神圣令更名吉：诚感所致
- 人与己同名姓吉：同心断金

**贞吉否凶类**：
- 神...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 天神命名吉：上帝所使
- 神赐姓吉：家计日丰
- 神命字吉：运必亨通
- 神圣令更名吉：诚感所致
- 人与己同名姓吉：同心断金

**贞吉否凶类**：
- 神呼姓名：呵责平日之谴
- 死者称名：鬼求食或求度

**凶类**：
- 易不祥名凶：财散疾病死亡
- 忽易姓名：迁移变产

#### 典故

- 周武王梦天命子虞：后封唐为晋
- 晋简文帝梦神命昌明：武帝字昌明，应谶"晋祚尽昌明"
- 衢州刘署梦神示改名：二十年后果为刺史
- 曹熙梦官府见名：改名颖叔，后进士及第
- 欧阳程改名：梦童子报榜，改名程后登第"""
    normalized_text_zh: str = """"""
    subject: str = "2 名姓类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_名姓类诸兆_001_L1",
    )
    version: str = "1.0.0"
