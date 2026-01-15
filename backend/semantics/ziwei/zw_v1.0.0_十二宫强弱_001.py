"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654355
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
    semantic_id="zw_v1.0.0_十二宫强弱_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 十二宫强弱(SemanticEntry):
    """
    - 分字分词释义：

  - **强宫**：该性别命理重点关注的宫位。
  - **弱宫**：该性别命理次要关注的宫位。
  - **男命强宫**：财帛、官禄、福德、迁移、田宅。
  - **女命强宫...
    """
    
    original_text: str = """- 分字分词释义：

  - **强宫**：该性别命理重点关注的宫位。
  - **弱宫**：该性别命理次要关注的宫位。
  - **男命强宫**：财帛、官禄、福德、迁移、田宅。
  - **女命强宫**：夫妻、子女、财帛、田宅、福德。
  - **性别差异**：男重事业财富，女重家庭关系。

#### 男命：
- 强宫：财帛、官禄、福德、迁移、田宅
- 弱宫：子女、奴仆、兄弟、父母

#### 女命：
- 强宫：夫妻、子女、财帛、田宅、福德
- 弱宫：其余诸宫

#### 完整对等诠释（secondary_lang_full·38十二宫强弱）：

  The twelve palaces carry different weights depending on gender. For male charts, the strong palaces are Wealth, Career, Fortune, Travel, and Property—these reflect earning capacity, professional achievement, mental well-being, external opportunities, and asset accumulation. Weaker palaces for men include Children, Servants, Siblings, and Parents. For female charts, the strong palaces are Spouse, Children, Wealth, Property, and Fortune—emphasizing relational fulfillment, motherhood, financial security, home stability, and inner contentment. The remaining palaces are considered secondary. This gender-differentiated weighting guides where to focus interpretive energy and which stellar configurations deserve priority attention."""
    normalized_text_zh: str = """"""
    subject: str = "十二宫强弱"
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
        l1_anchor="zw_v1.0.0_十二宫强弱_001_L1",
    )
    version: str = "1.0.0"
