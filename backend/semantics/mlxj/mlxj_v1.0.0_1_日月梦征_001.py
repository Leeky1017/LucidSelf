"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.783949
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
    semantic_id="mlxj_v1.0.0_1_日月梦征_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1日月梦征(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 汉 | 武帝母 | 神女授日 | 生武帝 |
| 宋 | 太宗母 | ...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 汉 | 武帝母 | 神女授日 | 生武帝 |
| 宋 | 太宗母 | 纳日于襟怀 | 生太宗 |
| 宋 | 真宗母 | 得日于神授 | 生真宗 |
| 宋 | 仁宗母 | 日坠承之以手 | 生仁宗 |
| 齐 | 景公 | 斗日不胜 | 病瘳 |
| 晋 | 明帝 | 日绕军营 | 驾至 |

#### 日月象征

- 日月=极贵之征
- 梦日=帝王之兆
- 月=众阴之长"""
    normalized_text_zh: str = """"""
    subject: str = "1 日月梦征"
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
        l1_anchor="mlxj_v1.0.0_1_日月梦征_001_L1",
    )
    version: str = "1.0.0"
