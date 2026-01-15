"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.819313
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
    semantic_id="mlxj_v1.0.0_1_淫奔名妓类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1淫奔名妓类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 红拂吉：侍儿中之豪杰，贤豪投契
- 卓文君吉：意外有奇缘，科第应高举
- 姑德吉：始邪终正，节烈自居
- 陈妙常吉：学人超出寻常，获息加倍

**贞吉否凶类*...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 红拂吉：侍儿中之豪杰，贤豪投契
- 卓文君吉：意外有奇缘，科第应高举
- 姑德吉：始邪终正，节烈自居
- 陈妙常吉：学人超出寻常，获息加倍

**贞吉否凶类**：
- 步非烟：利弊参半
- 崔莺莺：苟合之缘，美而无终

**名妓类**：
- 小蛮吉：主有美姿侍侧
- 薛涛吉：文翰之祥
- 李师师：倾国之色，但恐后祸

#### 淫奔类占断要点

淫奔名妓类梦象需分辨梦者身份：
- 士人梦之：多主科第、才名
- 商人梦之：主获利或失财
- 女人梦之：主婚姻变故
- 老人梦之：主享福或不祥"""
    normalized_text_zh: str = """"""
    subject: str = "1 淫奔名妓类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_淫奔名妓类诸兆_001_L1",
    )
    version: str = "1.0.0"
