"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.853838
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
    semantic_id="mlxj_v1.0.0_2_杀斗类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2杀斗类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 杀死他人：大吉，富贵福禄
- 血污衣服：得财利
- 自杀人：中吉，官位荣临
- 持刀杀人有血：吉
- 被他人杀我：利吉之占

**吉类**：
- 见他人杀人...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 杀死他人：大吉，富贵福禄
- 血污衣服：得财利
- 自杀人：中吉，官位荣临
- 持刀杀人有血：吉
- 被他人杀我：利吉之占

**吉类**：
- 见他人杀人：有人送物至
- 持刀斧自杀身死：得大财
- 与人相斫：主喜事
- 被人击：主得势

**凶类**：
- 杀伤不来无血：凶
- 逃避伏藏：反凶
- 被杀而不死：得财复失
- 梦击人不着：失力

#### 杀斗核心原则

| 梦象 | 有血 | 无血 |
|------|------|------|
| 杀人 | 吉 | 凶 |
| 被杀 | 吉 | 凶 |
| 相斫 | 吉 | 凶 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 杀斗类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_杀斗类诸兆_001_L1",
    )
    version: str = "1.0.0"
