"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.840354
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
    semantic_id="mlxj_v1.0.0_2_老幼男女类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2老幼男女类诸兆(SemanticEntry):
    """
    #### 老幼类汇总

**吉类**：
- 见老人大吉：寿年绵永，财帛丰盈
- 见童子吉：天真无邪，主有喜事

**凶类**：
- 自身忽老：男子中年兆之主长寿；幼者非祥
- 见小儿死：主有口舌灾殃
...
    """
    
    original_text: str = """#### 老幼类汇总

**吉类**：
- 见老人大吉：寿年绵永，财帛丰盈
- 见童子吉：天真无邪，主有喜事

**凶类**：
- 自身忽老：男子中年兆之主长寿；幼者非祥
- 见小儿死：主有口舌灾殃

**贞吉否凶类**：
- 老人变少：返老还童，吉；病者不祥
- 小儿变老：早慧之兆，但恐夭折

#### 男女类汇总

**男子梦象**：
- 男人梦见男子：平常兆
- 女子梦见男子：主情私
- 男子化女凶：阴祸临身

**女子梦象**：
- 男子梦见女人：情意所通，或疾病鬼物
- 女人梦寻丈夫：主丈夫死亡
- 女子化男吉：阴转阳，凶化吉

#### 核心占断原则

| 梦者 | 所梦 | 吉凶 | 主应 |
|------|------|------|------|
| 男子 | 男子 | 平 | 常兆 |
| 男子 | 女子 | 凶 | 情扰/病侵 |
| 女子 | 男子 | 凶 | 情私 |
| 女子 | 女子 | 平 | 常兆 |
| 任何 | 老人 | 吉 | 寿增财丰 |
| 任何 | 童子 | 吉 | 喜事至 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 老幼男女类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_老幼男女类诸兆_001_L1",
    )
    version: str = "1.0.0"
