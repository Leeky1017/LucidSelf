"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.836901
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
    semantic_id="mlxj_v1.0.0_2_肩胁腹背类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2肩胁腹背类诸兆(SemanticEntry):
    """
    #### 肩胁类汇总

**大吉类**：
- 两肩生于耳上大吉：威振边疆
- 荷担肩上吉：任重之象，为蒙宰为元帅
- 立人肩上元吉：大贵之象
- 肩上立人吉：羊琇典故
- 两肩受打痛极大吉：大得人力
...
    """
    
    original_text: str = """#### 肩胁类汇总

**大吉类**：
- 两肩生于耳上大吉：威振边疆
- 荷担肩上吉：任重之象，为蒙宰为元帅
- 立人肩上元吉：大贵之象
- 肩上立人吉：羊琇典故
- 两肩受打痛极大吉：大得人力

**吉类**：
- 斫肩吉：警醒宜守
- 肩生桃枝开一花：得美妾，生美女
- 肩上生痈疽吉：两间气聚

#### 腹背类汇总

**大吉类**：
- 人刺背大吉：唐玄宗典故，后面有良刺史
- 背上生目能视吉：能见后人（独孤后典故）

**吉类**：
- 少腹大于腰吉：后福广厚
- 少腹浸入水中吉：得财物，娶妇得妻财
- 背负重石吉：立功任重
- 背上有虫行吉：多劳多财

**凶类**：
- 少腹开穴凶：阳不足，男变女象
- 背裂凶：国有艰危，家有变异
- 满背生疮痛难忍凶：宋宗泽典故
- 背上缚一木凶：休囚困苦"""
    normalized_text_zh: str = """"""
    subject: str = "2 肩胁腹背类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_肩胁腹背类诸兆_001_L1",
    )
    version: str = "1.0.0"
