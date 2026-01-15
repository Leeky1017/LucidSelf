"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654292
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
    semantic_id="zw_v1.0.0_安天德月德解神诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安天德月德解神诀(SemanticEntry):
    """
    - 分字分词释义：

  - **天德星**：流年吉星，主化凶为吉，从酉宫起子年顺数。
  - **月德星**：流年吉星，主月内吉祥，从子宫起子年顺数。
  - **解神**：化解凶煞的吉星，从戌宫起...
    """
    
    original_text: str = """- 分字分词释义：

  - **天德星**：流年吉星，主化凶为吉，从酉宫起子年顺数。
  - **月德星**：流年吉星，主月内吉祥，从子宫起子年顺数。
  - **解神**：化解凶煞的吉星，从戌宫起子年逆数。
  - **流年太岁**：当年的流年地支，决定流年吉凶主轴。
  - **顺数**：按地支顺序（子丑寅卯...）向前数。
  - **逆数**：按地支逆序（子亥戌酉...）向后数。

**主题**：流年吉星安放。

#### 安星规则：

- **天德星**：酉宫起子年，顺数至流年太岁
- **月德星**：子宫起子年，顺数至流年太岁
- **解神**：戌宫起子年，逆数至当生年太岁

#### 完整对等诠释（secondary_lang_full·27天德月德解神）：

  Tiande (Heavenly Virtue), Yuede (Monthly Virtue), and Jieshen (Resolving Spirit) form a trio of benevolent stars that protect against calamity in the annual cycle. To place Tiande, begin from the You palace for the Rat year and count forward through the branches until reaching the current year's Tai Sui. For Yuede, start from the Zi palace for the Rat year and again count forward to the year branch. Jieshen operates in reverse: it starts from the Xu palace for the Rat year and counts backward to the native's birth year Tai Sui. When these three stars appear in favorable positions relative to the Life Palace or transit key houses during a given year, they can soften harsh influences, turn potential disasters into manageable setbacks, and signal windows where risky actions may succeed despite apparent obstacles."""
    normalized_text_zh: str = """"""
    subject: str = "安天德月德解神诀"
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
        l1_anchor="zw_v1.0.0_安天德月德解神诀_001_L1",
    )
    version: str = "1.0.0"
