"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654348
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
    semantic_id="zw_v1.0.0_男女竹罗三限_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 男女竹罗三限(SemanticEntry):
    """
    - 分字分词释义：

  - **竹罗三限**：以七杀破军为标志的死限判断法。
  - **死限**：大小限相遇凶星的致命时段。
  - **七杀破军**：破坏力最强的两颗凶星组合。
  - **巨暗...
    """
    
    original_text: str = """- 分字分词释义：

  - **竹罗三限**：以七杀破军为标志的死限判断法。
  - **死限**：大小限相遇凶星的致命时段。
  - **七杀破军**：破坏力最强的两颗凶星组合。
  - **巨暗凶星**：巨门与其他暗暗凶星。
  - **三方四正**：宫位三合与对冲的结构关系。
  - **帝星局例**：紫微星的运行规则。

按帝星局例逆行，以七杀破军为竹罗三限，加巨暗凶星作三方四正定议。大小二限相遇作死限断。

#### 完整对等诠释（secondary_lang_full·37竹罗三限）：

  The Bamboo-Net Three Limits formula identifies potentially fatal periods by tracking Qisha (Seven Killings) and Pojun (Army Breaker). Following the imperial star pattern in reverse, when both Major and Minor Limits converge on positions occupied or aspected by Qisha and Pojun, especially with Jumen (Dark Gate) and other shadowy malefics in the three-directional or four-opposing framework, the confluence is read as a death limit. This is among the most severe timing indicators in Ziwei Doushu and warrants careful verification before any definitive pronouncement."""
    normalized_text_zh: str = """"""
    subject: str = "男女竹罗三限"
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_男女竹罗三限_001_L1",
    )
    version: str = "1.0.0"
