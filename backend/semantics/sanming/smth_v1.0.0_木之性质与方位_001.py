"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227788
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
    semantic_id="smth_v1.0.0_木之性质与方位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 木之性质与方位(SemanticEntry):
    """
    - **原文（source_text）**：
  木主于东，应春。木之为言触也，阳气触动，冒地而生也。水流趋东，以生木也。木上发而覆下，乃自然之质也。

- **分字分词释义**：
  - **木主于...
    """
    
    original_text: str = """- **原文（source_text）**：
  木主于东，应春。木之为言触也，阳气触动，冒地而生也。水流趋东，以生木也。木上发而覆下，乃自然之质也。

- **分字分词释义**：
  - **木主于东，应春**：木对应东方，对应春季。
  - **触**：触动、萌发之意。
  - **冒地而生**：冒出地面生长。
  - **水流趋东**：水向东流动以滋养木。
  - **上发而覆下**：向上生长，枝叶覆盖地面。

- **规范化释义（primary_lang_explained）**：
  木对应东方，对应春季。所谓"木"，其本义是"触动"——阳气触发萌动，冲破地面而生长出来。水向东方流动，滋养木的生长。木的自然属性是向上生发、枝叶向下覆盖，这是其天然的性质。

- **完整对等诠释（secondary_lang_full）**：
  Wood governs the East and corresponds to Spring. The essence of Wood means "touching" or "triggering"—yang qi triggers and sprouts through the earth. Water flows eastward to nourish Wood. Wood naturally grows upward while its branches cover downward, depicting Wood's sprouting nature with upward orientation, nourished by Water. This enables vitality, requiring yang qi activation rather than cold suppression. This establishes Wood's directional, seasonal, and essential attributes in destiny analysis.

- **核心要点**：
  - 木对应东方、春季
  - 木的本义是"触动"，体现生发之性
  - 木需水滋养，向上生长覆盖

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_129]` `[trigger: 木之性质]` `[factor_trigger: element_wood AND direction_east]` `[role: 主干]` 木主于东，应春。木之为言触也，阳气触动，冒地而生也。水流趋东，以生木也。 → 《三命通会》卷一#木之性质与方位

- **详细解说**：
  此条阐明木的基本属性。从方位看，木主东方；从时令看，木应春季。木的本质在于"触动"——当阳气触发时，种子就会冒破地面生长。水是木的母，水向东流动以滋养木的生长。木的自然形态是向上生发、枝叶向外伸展并覆盖地面，这种向上向外的扩张性是木的天然特质。在命理中，木旺之人多具生发、进取、扩张之性。

- **校勘与字词辨析（双语）**：
  - **中文**："触"字在此处指"触动、萌动"，非"触摸"之意，体现木的生发本性。
  - **English**："触" (touching/triggering) here refers to the initiating impulse of wood's sprouting nature, not physical contact."""
    normalized_text_zh: str = """"""
    subject: str = "木之性质与方位"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_木之性质与方位_001_L1",
    )
    version: str = "1.0.0"
