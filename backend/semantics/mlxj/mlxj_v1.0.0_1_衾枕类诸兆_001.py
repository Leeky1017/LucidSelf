"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.829275
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
    semantic_id="mlxj_v1.0.0_1_衾枕类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1衾枕类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 锦衾吉：朱长文母典故，生子必能文
- 睡红锦被吉：喜事临身，满门吉庆
- 鸳鸯枕大吉：家庭和，子孙兴

**吉类**：
- 座褥吉：焚香诵经，功业进
- 芦...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 锦衾吉：朱长文母典故，生子必能文
- 睡红锦被吉：喜事临身，满门吉庆
- 鸳鸯枕大吉：家庭和，子孙兴

**吉类**：
- 座褥吉：焚香诵经，功业进
- 芦花毯贞吉：始难终易

**凶类**：
- 虎皮褥否凶：贵者失贵，勇者失勇"""
    normalized_text_zh: str = """"""
    subject: str = "1 衾枕类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_衾枕类诸兆_001_L1",
    )
    version: str = "1.0.0"
