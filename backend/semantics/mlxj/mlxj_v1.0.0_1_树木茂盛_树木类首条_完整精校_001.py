"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.802896
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
    semantic_id="mlxj_v1.0.0_1_树木茂盛_树木类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1树木茂盛树木类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

树木茂盛，大吉，家业兴隆，名成利就，根基不薄，得时得气，生机勃勃之兆也。梦此者，文士当主盛名，进取必登巍科。生意利十倍，家计必发达，子姓蕃衍。庆贺螽斯，如梦...
    """
    
    original_text: str = """#### 原文（source_text）

树木茂盛，大吉，家业兴隆，名成利就，根基不薄，得时得气，生机勃勃之兆也。梦此者，文士当主盛名，进取必登巍科。生意利十倍，家计必发达，子姓蕃衍。庆贺螽斯，如梦在家中为幽隐之兆，恐亦非宜。

#### 规范化释义（primary_lang_explained）

梦树木茂盛，大吉。家业兴隆，名成利就，根基不薄，得时得气，生机勃勃之兆。

各类人梦之：
- **文士**：主盛名，进取登巍科
- **商贾**：生意利十倍
- **家居**：家计发达，子姓蕃衍

但若梦在家中，为幽隐之兆，恐亦非宜。

#### 完整对等诠释（secondary_lang_full）

Dreaming of flourishing trees is greatly auspicious. Family enterprise prospers, fame and fortune achieved, foundation solid, timing favorable—a sign of vigorous vitality.

For different dreamers:
- **Scholars**: Renowned reputation, advancing to high examinations
- **Merchants**: Profits tenfold
- **Homemakers**: Family prospers, descendants multiply

However, if dreamed within the home, it signifies hidden matters—perhaps not ideal.

#### 核心要点

- 树木茂盛=家业兴隆=生机勃勃
- 根基不薄，得时得气
- 文士→盛名，商贾→利倍，家居→蕃衍
- 例外：在家中梦→幽隐之兆"""
    normalized_text_zh: str = """"""
    subject: str = "1 树木茂盛（树木类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_树木茂盛_树木类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
