"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.798231
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
    semantic_id="mlxj_v1.0.0_1_肴馔类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1肴馔类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 天仓肴馔：天赐饮食
- 食羊头大吉：解元、和解
- 食天鹅肉吉：生儿贵

**吉类**：
- 伊蒲馔吉：佛门法供，行善修福
- 食鸭吉：登科甲，披甲胄
- ...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 天仓肴馔：天赐饮食
- 食羊头大吉：解元、和解
- 食天鹅肉吉：生儿贵

**吉类**：
- 伊蒲馔吉：佛门法供，行善修福
- 食鸭吉：登科甲，披甲胄
- 杀鸡为黍吉：成德之士
- 食雁吉：既饱以德
- 食黄雀吉：进爵
- 食蛋吉：多子
- 食鱼头吉：参政，淑女

**凶类**：
- 啖鹅头贞吉否凶：呕吐、死亡
- 食腥肉贞吉否凶：学未纯熟"""
    normalized_text_zh: str = """"""
    subject: str = "1 肴馔类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_肴馔类诸兆_001_L1",
    )
    version: str = "1.0.0"
