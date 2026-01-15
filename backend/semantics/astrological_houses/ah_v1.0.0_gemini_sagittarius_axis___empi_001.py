"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333869
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
    semantic_id="ah_v1.0.0_gemini_sagittarius_axis___empi_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class GeminiSagittariusAxisEmpi(SemanticEntry):
    """
    #### Source Text

"Gemini is characterized by vivid eagerness to extend the scope of personal experi...
    """
    
    original_text: str = """#### Source Text

"Gemini is characterized by vivid eagerness to extend the scope of personal experiences through many kinds of contacts. It is the most typical symbol of intellectual curiosity and the mind which analytically classifies knowledge for practical use. Sagittarius refers to more abstract and mature knowledge—concerned with integration of distantly related factors, with philosophy, religion, and the quest for basic values. Gemini deals with easily accessible encounters and concrete mind; Sagittarius is haunted by ever larger horizons, by the thirst for great adventures beyond the familiar."

#### English Paraphrase (Primary Language)

The Gemini/Sagittarius axis represents the polarity between empirical data-gathering and philosophical meaning-making. Gemini rising indicates avidity for knowledge—the deep-rooted expectation that through knowledge and multiple contacts one discovers identity. The danger is getting caught in webs of small concerns, well-ordered but empty of larger meaning. Sagittarius Descendant provides abstract frames of reference, dissatisfaction with the near-at-hand, expansion through relationship. When Sagittarius rises, the individual realizes identity through involvement in great causes, social or religious beliefs, truth-seeking. But this requires the polarizing influence of Gemini's more precise, empirical, analytical mind. The axis represents the balance between specialist and generalist, between "how" and "why."

#### Complete Chinese Interpretation (Secondary Language)

双子/射手轴代表经验数据收集与哲学意义建构之间的极性。

**双子上升**：
- 对知识的贪婪——通过知识和多重接触发现身份
- 典型的智识好奇心，分析性地为实用目的分类知识
- 危险：陷入小事务的网中，虽然井井有条但缺乏更大意义
- 需要射手式伴侣提供抽象参照框架

**射手上升**：
- 通过卷入伟大事业、社会或宗教信仰、真理追求来实现身份认同
- 可能以狂热的热情推广或宣传其发现的"真理"
- 需要双子式伴侣的更精确、更经验性、更分析性的头脑来平衡

**轴线的核心张力**：
- 专家vs通才
- "如何"vs"为什么"
- 具体vs抽象
- 近处vs远方

#### Core Points

- **Mutable signs**: Transition, adaptation, distribution
- **Gemini rising**: Knowledge avidity, multiple contacts, practical classification
- **Sagittarius balancing**: Abstract frames, expansion beyond familiar
- **Sagittarius rising**: Identity through great causes, truth-seeking
- **Gemini partner needed**: Precise, empirical, analytical mind
- **Core polarity**: Specialist/empirical vs generalist/philosophical"""
    normalized_text_zh: str = """"""
    subject: str = "Gemini/Sagittarius Axis - Empirical Knowledge vs Philosophical Understanding"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_gemini_sagittarius_axis___empi_001_L1",
    )
    version: str = "1.0.0"
