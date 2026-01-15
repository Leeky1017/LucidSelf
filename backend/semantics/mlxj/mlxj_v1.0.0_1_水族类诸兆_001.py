"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.791068
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
    semantic_id="mlxj_v1.0.0_1_水族类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1水族类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 腾蛟大吉：变化飞腾
- 蛟龙入怀吉：学贯天人（董仲舒典故）
- 蛇化蛟大吉：平地升天
- 鼋曝日大吉：面君之象
- 鲤鱼大吉：化龙鱼（六六鱼）
- 鳣鲔吉：...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 腾蛟大吉：变化飞腾
- 蛟龙入怀吉：学贯天人（董仲舒典故）
- 蛇化蛟大吉：平地升天
- 鼋曝日大吉：面君之象
- 鲤鱼大吉：化龙鱼（六六鱼）
- 鳣鲔吉：嫁娶佳兆

**吉类**：
- 蜃贞吉：韬光养晦
- 大龟吉：静信寺典故
- 蟹去足吉：解元（解字）
- 蚌吉：和合婚姻
- 蛤蜊：合本多利
- 鳗吉：柔腻滑泽
- 鳅跃水中吉：秋试之捷

**贞吉否凶类**：
- 鳌鱼：登科/煎熬
- 鲸鱼：好音/不善终
- 黄甲蟹：科甲/解散

**凶类**：
- 鼋啮足：涉险遇伤
- 鱼啮人凶：柳沂典故
- 蟛蚏凶：不义之财

#### 典故

- 董仲舒梦蛟龙入怀：作春秋繁露
- 胡寅母梦大鱼跃水盆：生宋名儒"""
    normalized_text_zh: str = """"""
    subject: str = "1 水族类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_水族类诸兆_001_L1",
    )
    version: str = "1.0.0"
