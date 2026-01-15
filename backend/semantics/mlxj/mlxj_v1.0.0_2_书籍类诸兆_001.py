"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.834528
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
    semantic_id="mlxj_v1.0.0_2_书籍类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2书籍类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 书从天降大吉：殊遇
- 书晒炎日中大吉：文明之象
- 得所未见书大吉：学问长进
- 读书山林间大吉：高贵之品
- 握书登山顶大吉：列三台

**吉类**：
...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 书从天降大吉：殊遇
- 书晒炎日中大吉：文明之象
- 得所未见书大吉：学问长进
- 读书山林间大吉：高贵之品
- 握书登山顶大吉：列三台

**吉类**：
- 月照书史吉：婚姻之喜（韩𢗄典故）
- 云中书贞吉：青云名显达
- 拾地上遗书吉：学日以进
- 秉烛觅书吉：得良师贤友
- 书作枕大吉：作事安稳

**凶类**：
- 风翻书籍凶：心事不宁
- 雨淋书史凶：志不坚学不精
- 焚书凶：弃书不祥
- 架上书崩：老年不吉

#### 典故

- 月照书史：韩𢗄梦月下观后汉书，后娶蔡氏
- 神授文书：萧燧梦神人示文书，后为南宋名公"""
    normalized_text_zh: str = """"""
    subject: str = "2 书籍类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_书籍类诸兆_001_L1",
    )
    version: str = "1.0.0"
