"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.826009
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
    semantic_id="mlxj_v1.0.0_1_桥路诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1桥路诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 造新桥吉：桥成事济，往来和合
- 金银造成桥：利之聚，济之功
- 群鹊聚成桥大吉：鹊桥，婚姻大吉

**吉类**：
- 渡过高桥：久病遇良医
- 桥上呼唤吉...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 造新桥吉：桥成事济，往来和合
- 金银造成桥：利之聚，济之功
- 群鹊聚成桥大吉：鹊桥，婚姻大吉

**吉类**：
- 渡过高桥：久病遇良医
- 桥上呼唤吉：忧疑得清理，佳期乐就
- 桥下过吉：光彩明亮，诸事大吉
- 持𬬰立桥吉：乘高有威，得势之兆

**凶类**：
- 桥坏折凶：口舌相争，官讼相连
- 桥柱折毁大凶：老者损子孙，少者丧父母
- 桥生草：凶年之象，病危者之占

**贞吉否凶类**：
- 桥上饮食：下虚上险，家业飘零
- 桥上有亭楼否凶：虹形蜃气，虚浮无实
- 桥被火烧：通行阻塞（吴人菜佣得盐致富典故）

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 渡过高桥 | 杨骢 | 病愈/接引渡桥 | 宋 |
| 桥被火烧 | 吴人菜佣 | 至火烧桥地，得盐致富 | 古 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 桥路诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_桥路诸兆_001_L1",
    )
    version: str = "1.0.0"
