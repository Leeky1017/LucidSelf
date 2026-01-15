"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227695
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
    semantic_id="smth_v1.0.0_大林木_戊辰_己巳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大林木戊辰己巳(SemanticEntry):
    """
    - **原文（source_text）**：
  戊辰己巳则气不成量，物已及时，枝叶茂盛，郁然成林，取其木之盛也，故曰大林木。

- 分字分词释义：
  - **气不成量，物已及时**：气机繁多而难以...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊辰己巳则气不成量，物已及时，枝叶茂盛，郁然成林，取其木之盛也，故曰大林木。

- 分字分词释义：
  - **气不成量，物已及时**：气机繁多而难以一一计量，物候已至成熟之时。

- **规范化释义（primary_lang_explained）**：
  戊辰、己巳之木，如成片的大林：枝叶茂密，势成规模，不再是单株之木。象征气势宏大、资源众多，但也容易显得杂而不精、顾此失彼。

- **完整对等诠释（secondary_lang_full）**：

  Wuchen and Jisi form "Forest Wood". Here Wood Qi has multiplied beyond counting: branches and leaves crowd together until individual trees merge into a continuous grove. Attention shifts from the fate of a single trunk to the scale, coverage and atmosphere of the whole stand. In charts this Nayin points to situations where people, projects or resources are numerous enough to create momentum and a living system—teams, networks, communities—yet also warns that without pruning and focus, strength can be scattered and management overwhelmed. Metal and Fire, in the form of clear rules and decisive selection, are needed to turn sheer quantity into a coherent forest rather than a tangle."""
    normalized_text_zh: str = """"""
    subject: str = "大林木（戊辰、己巳）"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_大林木_戊辰_己巳_001_L1",
    )
    version: str = "1.0.0"
