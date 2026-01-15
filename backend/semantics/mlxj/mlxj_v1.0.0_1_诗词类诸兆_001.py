"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.834548
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
    semantic_id="mlxj_v1.0.0_1_诗词类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1诗词类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 命题属文吉：天意所在（司马相如典故）
- 七步诗：快捷之兆
- 元旦诗吉：气象更新
- 早朝诗大吉：绛帻鸡人报晓

**吉类**：
- 李太白诗：清高富贵
...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 命题属文吉：天意所在（司马相如典故）
- 七步诗：快捷之兆
- 元旦诗吉：气象更新
- 早朝诗大吉：绛帻鸡人报晓

**吉类**：
- 李太白诗：清高富贵
- 杜子美诗吉：魁首词林
- 律诗贞吉：愈加谨慎
- 绝句诗贞吉：勇于为善

**贞吉否凶类**：
- 五噫歌贞吉：百事忧煎
- 除夕诗贞吉：除旧布新

#### 典故

- 白玉楼记：李贺梦人请为天帝白玉楼记，不久卒
- 晓寒歌：萧贯梦至宫殿赋晓寒歌，后登进士"""
    normalized_text_zh: str = """"""
    subject: str = "1 诗词类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_诗词类诸兆_001_L1",
    )
    version: str = "1.0.0"
