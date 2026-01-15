"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654370
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
    semantic_id="zw_v1.0.0_流禄流羊流陀罗诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 流禄流羊流陀罗诀(SemanticEntry):
    """
    - 分字分词释义：

  - **流禄**：流年禄存，按流年太岁定位。
  - **流羊**：流年擎羊，在流禄后一宫。
  - **流陀**：流年陀罗，在流禄前一宫。
  - **流年太岁**：当年的...
    """
    
    original_text: str = """- 分字分词释义：

  - **流禄**：流年禄存，按流年太岁定位。
  - **流羊**：流年擎羊，在流禄后一宫。
  - **流陀**：流年陀罗，在流禄前一宫。
  - **流年太岁**：当年的流年地支。
  - **三方四正**：宫位三合与对冲的结构关系。
  - **毒祸**：流年煞星与本命煞星重逢之凶。

论流年太岁，如巳丑年流禄在午、流羊在未、流陀在巳。三方四正俱见擎羊、流羊、流陀，又七杀重逢，必遭毒祸。

#### 完整对等诠释（secondary_lang_full·40流禄流羊流陀）：

  The annual flowing stars (Liu Lu, Liu Yang, Liu Tuo) rotate according to the year's Tai Sui. For example, in a Si-Chou year, Liu Lu (Flowing Salary) occupies Wu, Liu Yang (Flowing Ram) occupies Wei, and Liu Tuo (Flowing Hump) occupies Si. When the natal Qingyang and Tuoluo combine with their flowing counterparts in the three-directional or four-opposing positions, and Qisha (Seven Killings) also resurfaces in the same framework, the convergence signals severe danger—potentially poison, violence, or catastrophic loss. This algorithm overlays annual malefic positions onto the natal chart to identify years of heightened risk."""
    normalized_text_zh: str = """"""
    subject: str = "流禄流羊流陀罗诀"
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
        l1_anchor="zw_v1.0.0_流禄流羊流陀罗诀_001_L1",
    )
    version: str = "1.0.0"
