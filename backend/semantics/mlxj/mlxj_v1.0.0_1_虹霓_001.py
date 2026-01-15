"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831773
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
    semantic_id="mlxj_v1.0.0_1_虹霓_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1虹霓(SemanticEntry):
    """
    #### 原文摘要

虹者，阴阳交接之气也。雄曰虹，雌曰霓。梦见虹霓，主有私情暗约之事。若五色分明者吉，混浊不清者凶。

#### 分类汇总

- 虹横天上：五色分明者吉，混浊者凶
- 霓虹下饮水：主...
    """
    
    original_text: str = """#### 原文摘要

虹者，阴阳交接之气也。雄曰虹，雌曰霓。梦见虹霓，主有私情暗约之事。若五色分明者吉，混浊不清者凶。

#### 分类汇总

- 虹横天上：五色分明者吉，混浊者凶
- 霓虹下饮水：主有婚姻之喜
- 白虹贯日：兵革之象（荆轲刺秦典故）"""
    normalized_text_zh: str = """"""
    subject: str = "1 虹霓"
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
        l1_anchor="mlxj_v1.0.0_1_虹霓_001_L1",
    )
    version: str = "1.0.0"
