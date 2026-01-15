"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.853854
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
    semantic_id="mlxj_v1.0.0_2_起居类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2起居类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 贤愚乍会于日下：利用有孚
- 少长咸集于目前：朋来无咎
- 叩首梦人叩请：荣显喜庆
- 笑傲叹赏：直验舒快
- 哭泣涕泪交垂：反为吉兆
- 放声大哭涕泪交垂：...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 贤愚乍会于日下：利用有孚
- 少长咸集于目前：朋来无咎
- 叩首梦人叩请：荣显喜庆
- 笑傲叹赏：直验舒快
- 哭泣涕泪交垂：反为吉兆
- 放声大哭涕泪交垂：必获大吉快乐

**凶类**：
- 乍合乍离：顷聚顷散
- 叩别叩辞叩诀叩告：不祥
- 流泪掩口而走：丧亡
- 悲哀无泪或涕泣流血：大凶
- 呼号叱咤：惊疑愠怒

#### 起居典故

- 羊仲睦：梦坐竹席，次日被邀坐首席
- 林邑王母：梦坐杨迈金席，生儿后为林邑王
- 蔡君谟：梦卧樵疾愈，知大蛇盘鼓上"""
    normalized_text_zh: str = """"""
    subject: str = "2 起居类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_起居类诸兆_001_L1",
    )
    version: str = "1.0.0"
