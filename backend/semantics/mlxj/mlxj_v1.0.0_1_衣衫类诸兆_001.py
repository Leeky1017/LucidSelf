"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.829265
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
    semantic_id="mlxj_v1.0.0_1_衣衫类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1衣衫类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 衮衣大吉：至尊至贵盛服
- 衮衣升座：姚襄梦弟苌服衮衣，后称秦王
- 帝脱御衣：康王梦，后践位为宋高宗

**吉类**：
- 朱衣贞吉否凶：朱衣点头，绯衣挂...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 衮衣大吉：至尊至贵盛服
- 衮衣升座：姚襄梦弟苌服衮衣，后称秦王
- 帝脱御衣：康王梦，后践位为宋高宗

**吉类**：
- 朱衣贞吉否凶：朱衣点头，绯衣挂体
- 锦衣贴月飞：沈彬典故
- 鼠入衣下吉：娄太后典故

**凶类**：
- 衮衣倚槐凶：元渊典故，槐=木傍鬼
- 衣倒着凶：颠倒乱常
- 裳飞起凶：河间国典故

#### 衣色与吉凶

| 衣色 | 吉应 | 凶应 |
|------|------|------|
| 朱/红 | 朱衣点头、天神降福 | 诛斩、赤族 |
| 锦 | 文章华丽 | - |
| 素/白 | 清高 | 丧服 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 衣衫类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_衣衫类诸兆_001_L1",
    )
    version: str = "1.0.0"
