"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793436
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
    semantic_id="mlxj_v1.0.0_5_天开大吉_001",
    book_id="mlxj",
    engine_id="dream"
)
class 5天开大吉(SemanticEntry):
    """
    #### 原文（source_text）

天开大吉。乾象弗闭，俄然划开，游魂所遘，奇瑞天来。此为贵人遇时之象，主得大财，逢大贵，兆应重新，事无不泰也。梦天开放彩者，富贵之象，万倍寻常，大吉。

##...
    """
    
    original_text: str = """#### 原文（source_text）

天开大吉。乾象弗闭，俄然划开，游魂所遘，奇瑞天来。此为贵人遇时之象，主得大财，逢大贵，兆应重新，事无不泰也。梦天开放彩者，富贵之象，万倍寻常，大吉。

#### 规范化释义（primary_lang_explained）

梦见天门开启，大吉。乾象不闭塞，忽然划开，游魂所遇，奇瑞从天而来。此为贵人遇时之象，主得大财、逢大贵，兆应重新开始，事无不泰。若梦天开且放射彩光，为富贵之象，万倍于寻常吉兆，大吉。

#### 核心要点

- **梦象**：天开
- **吉凶**：大吉
- **象义**：乾象开启、奇瑞天来
- **主应**：得大财、逢大贵、事无不泰
- **加强象**：天开放彩，富贵万倍"""
    normalized_text_zh: str = """"""
    subject: str = "5 天开大吉"
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
        l1_anchor="mlxj_v1.0.0_5_天开大吉_001_L1",
    )
    version: str = "1.0.0"
