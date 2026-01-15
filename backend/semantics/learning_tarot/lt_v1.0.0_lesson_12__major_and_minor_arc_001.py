"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008836
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
    semantic_id="lt_v1.0.0_lesson_12__major_and_minor_arc_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson12MajorAndMinorArc(SemanticEntry):
    """
    **Source Text** (Lines 1275-1319): Major arcana = deep, strong, decisive, long-term energy. Minor ar...
    """
    
    original_text: str = """**Source Text** (Lines 1275-1319): Major arcana = deep, strong, decisive, long-term energy. Minor arcana = ups and downs of daily life.

**English Paraphrase**: A **major arcana card** represents "an energy that is deep, strong, decisive, or long-term." The **minor arcana cards** "chart the ups and downs of daily life and register changes in feelings and thoughts." Hermit (major) seeking truth is heartfelt desire; Eight of Cups (minor) seeking is passing fancy.

**Complete Chinese Interpretation**: **大阿卡纳牌**代表"深刻、强烈、决定性或长期的能量。"**小阿卡纳牌**"记录日常生活的起伏，登记感受和思想的变化。"隐士（大阿）寻求真理是内心的渴望；圣杯八（小阿）的寻求是一时兴起。

**Weight Comparison**:
- **Major Arcana**: Deep, strong, decisive, long-term
- **Minor Arcana**: Daily ups and downs, passing concerns

**Example Comparison**:
- **Hermit (Major)**: Strong urge to find answers, major desire lasting long time
- **Eight of Cups (Minor)**: Similar seeking, but not same force, passing fancy

**Narrative Snippets**:
- `[ns_ltt_142]` `[trigger: major_minor_weight]` `[factor_trigger: tarot_arcana_weight]` `[role: 主干]` Major = deep, strong, long-term; Minor = daily ups and downs. → L1280-1287"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 12: Major and Minor Arcana Cards (大小阿卡纳权重)"
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_lesson_12__major_and_minor_arc_001_L1",
    )
    version: str = "1.0.0"
