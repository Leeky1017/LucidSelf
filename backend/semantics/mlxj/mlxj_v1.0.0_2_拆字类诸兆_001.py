"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.834556
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
    semantic_id="mlxj_v1.0.0_2_拆字类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2拆字类诸兆(SemanticEntry):
    """
    #### 分类汇总

**字形拆解典故**：
- 片犬=状：梁颢梦得犬肉一片，后为状元
- 车中猴=申：谢小娥梦破案
- 弓舆不得=一个得：神祠祈梦
- 高何二姓：都穆典故
- 两人夹木=来：久客将归...
    """
    
    original_text: str = """#### 分类汇总

**字形拆解典故**：
- 片犬=状：梁颢梦得犬肉一片，后为状元
- 车中猴=申：谢小娥梦破案
- 弓舆不得=一个得：神祠祈梦
- 高何二姓：都穆典故
- 两人夹木=来：久客将归
- 木傍人立=休：仕宦罢职
- 鼠戴笠子=窜：逃匿之兆
- 笠飘水畔=泣：父母丧亡
- 火入林中=焚：火烛之惊
- 靴匠倚石=破：家计萧条
- 一木两火=荣：登第贵显
- 三女同居=奸：私奸败露
- 一水四鱼=鳏：孤独之兆
- 人骑牛背=失：失脱之忧
- 人言犬吠=狱：狱囚之系"""
    normalized_text_zh: str = """"""
    subject: str = "2 拆字类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_拆字类诸兆_001_L1",
    )
    version: str = "1.0.0"
