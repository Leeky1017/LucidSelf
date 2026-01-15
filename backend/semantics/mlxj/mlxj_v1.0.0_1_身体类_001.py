"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.804523
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
    semantic_id="mlxj_v1.0.0_1_身体类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1身体类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 秦 | 子婴 | 身长十丈人 | 天下将乱 |
| 齐 | 世祖赜 |...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 秦 | 子婴 | 身长十丈人 | 天下将乱 |
| 齐 | 世祖赜 | 以笔画身为两翅 | 践大位 |
| 唐 | 高祖 | 身死坠床群蛆食 | 得天下 |
| 明 | 万太守 | 裸身称冤 | 破杀人案 |

#### 身死坠床典故（详）

唐高祖将举义师，夜梦身死坠床下，为群蛆所食。诣智满禅师问之。

满贺曰：公得天下矣。
- 死=毙也
- 坠于床=下也
- 群蛆共食=亿兆趋附也
- 人不敢直指天子故曰陛下=至尊之象

后即帝位，命满营寺赐额兴义寺。"""
    normalized_text_zh: str = """"""
    subject: str = "1 身体类"
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
        l1_anchor="mlxj_v1.0.0_1_身体类_001_L1",
    )
    version: str = "1.0.0"
