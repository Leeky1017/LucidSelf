"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.816084
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
    semantic_id="mlxj_v1.0.0_1_禳梦诸法_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1禳梦诸法(SemanticEntry):
    """
    #### 禳恶梦法

**东向咒法**：
- 时机：梦恶醒后
- 方向：面向东方
- 咒语：元元上帝，九天真王，护身保命，百鬼潜藏

**书符法**：
- 于黄纸书符
- 焚于卧室四角
- 恶梦不复入...
    """
    
    original_text: str = """#### 禳恶梦法

**东向咒法**：
- 时机：梦恶醒后
- 方向：面向东方
- 咒语：元元上帝，九天真王，护身保命，百鬼潜藏

**书符法**：
- 于黄纸书符
- 焚于卧室四角
- 恶梦不复入

**祭祀法**：
- 设香案
- 供清水鲜花
- 诵经礼拜

#### 禳凶梦法

**转梦法**：
- 梦凶而欲转吉
- 向东三唾
- 念咒三遍
- 不与人言

**解梦法**：
- 以白纸书梦中所见
- 焚于十字路口
- 恶气随烟消散"""
    normalized_text_zh: str = """"""
    subject: str = "1 禳梦诸法"
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
        l1_anchor="mlxj_v1.0.0_1_禳梦诸法_001_L1",
    )
    version: str = "1.0.0"
