"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.791077
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
    semantic_id="mlxj_v1.0.0_1_昆虫类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1昆虫类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 虺蛇吉：女子之祥，生女必贤
- 黄蛇亘天：上帝之征（秦文公典故）
- 天诛大蛇：晋文修德成霸
- 脚踏蛇吉：随侯珠典故
- 蛇绕于身吉：李雄生而称帝

**凶...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 虺蛇吉：女子之祥，生女必贤
- 黄蛇亘天：上帝之征（秦文公典故）
- 天诛大蛇：晋文修德成霸
- 脚踏蛇吉：随侯珠典故
- 蛇绕于身吉：李雄生而称帝

**凶类**：
- 蛇生足凶：杀女子作贼者（刘桢典故）
- 群蛇缘城四出凶：寇乱
- 猬攻穴破城凶：寇盗作乱

#### 鼠类汇总

**吉类**：
- 白鼠吉：积财致富
- 田鼠入室：福将至
- 鼠化成人形吉：生男之兆
- 鼠窜吉：灾消祸解

**凶类**：
- 鼠忽死凶：子亡
- 髫鼠大如犬凶：位不当

#### 蝶虫类汇总

**吉类**：
- 身化蝴蝶：庄周梦蝶，物化
- 蝴蝶飞来扑杀之吉：得外财
- 飞虫遍体入肤复出：大贵人之梦（马皇后典故）

**凶类**：
- 一飞虫入目凶：匪人将有大凶
- 飞虫自耳中出：病人不祥"""
    normalized_text_zh: str = """"""
    subject: str = "1 昆虫类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_昆虫类诸兆_001_L1",
    )
    version: str = "1.0.0"
