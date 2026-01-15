"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.782254
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
    semantic_id="mlxj_v1.0.0_1_面目诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1面目诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 面大头长与身躯等大吉：天仓满盈，九窍清洁
- 面额忽异平日大吉：神旺色润，学长才高
- 面生三口大吉：贵升一品之象
- 面变如鬼形吉：阳上升神，阴在下鬼

...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 面大头长与身躯等大吉：天仓满盈，九窍清洁
- 面额忽异平日大吉：神旺色润，学长才高
- 面生三口大吉：贵升一品之象
- 面变如鬼形吉：阳上升神，阴在下鬼

**吉类**：
- 面赤吉：喜色，必有喜庆
- 洗去面垢吉：王俊典故

**凶类**：
- 面生黑疵凶：以相法详之，有凶无吉
- 面色青黑黄瘦凶：病恙惊忧
- 面涂垢凶：王俊梦典故

#### 面相与梦象对应

| 面相变化 | 梦象主应 | 原理 |
|---------|---------|------|
| 面大头长 | 天仓满盈 | 相法对应 |
| 面赤 | 喜庆 | 气色对应 |
| 面青黑 | 病忧 | 气色对应 |
| 面生疵 | 凶事 | 相法对应 |
| 面如鬼 | 阴阳转化 | 象征对应 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 面目诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_面目诸兆_001_L1",
    )
    version: str = "1.0.0"
