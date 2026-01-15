"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831758
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
    semantic_id="mlxj_v1.0.0_1_雷象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1雷象(SemanticEntry):
    """
    #### 原文摘要

雷霆震响，大吉。占曰：雷者，令也，天之号令。梦者政教宣布，大权在握，凡作事举动，如发千钧之弩也。

#### 分类汇总

**大吉类**：
- 雷霆震响大吉：令也，天之号令，大权...
    """
    
    original_text: str = """#### 原文摘要

雷霆震响，大吉。占曰：雷者，令也，天之号令。梦者政教宣布，大权在握，凡作事举动，如发千钧之弩也。

#### 分类汇总

**大吉类**：
- 雷霆震响大吉：令也，天之号令，大权在握
- 雷震子大吉：子受皇恩，未得子者产麒麟，已得子者登科第
- 雷火烧身上衣：脱白挂绿，功名遂志
- 雷起龙门大吉：登科得子之象

**凶类**：
- 雷掩耳：春夏作事退怯，秋冬外侮不侵
- 鬼驱雷电凶：魁名不能遂志（汉献帝典故）
- 人与纸丸作雷响：虚惊不实，多说少成

**贞吉否凶类**：
- 雷震殿宇：迁官起宅大吉，动成田，垦辟田园

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 鬼驱雷电 | 汉献帝 | 为曹操所害 | 汉 |
| 神告当死雷斧 | 顾德称妻张氏 | 立门外待，帝赦其孝 | 绍兴间 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 雷象"
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
        l1_anchor="mlxj_v1.0.0_1_雷象_001_L1",
    )
    version: str = "1.0.0"
