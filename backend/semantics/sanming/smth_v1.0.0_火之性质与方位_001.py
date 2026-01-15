"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227796
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
    semantic_id="smth_v1.0.0_火之性质与方位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 火之性质与方位(SemanticEntry):
    """
    - **原文（source_text）**：
  火主于南，应夏。火之为言化也，毁也。阳在上，阴在下，毁然盛而变化万物也。钻木取火，木所生也。然火无正体，体本木焉，出以应物，尽而复入，乃自然之理也。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  火主于南，应夏。火之为言化也，毁也。阳在上，阴在下，毁然盛而变化万物也。钻木取火，木所生也。然火无正体，体本木焉，出以应物，尽而复入，乃自然之理也。

- **分字分词释义**：
  - **化也，毁也**：变化万物，毁坏旧形。
  - **毁然盛**：炽盛燃烧之貌。
  - **钻木取火**：火从木中生出。
  - **无正体**：火无固定形体。
  - **体本木焉**：火的本体依附于木。

- **规范化释义（primary_lang_explained）**：
  火对应南方，对应夏季。所谓"火"，其本义是"化"和"毁"——阳气在上、阴气在下，炽烈燃烧而变化万物。钻木可以取火，说明火由木所生。但火本身没有固定形体，其本体依附于木，出来应物之后燃尽就复归于木，这是自然的道理。

- **完整对等诠释（secondary_lang_full）**：
  Fire governs the South and corresponds to Summer. Fire's essence means "transformation" and "destruction"—yang above and yin below, blazing intensely to transform all things. Drilling wood produces fire, showing that Wood generates Fire. Fire lacks fixed form; its essence is rooted in Wood, emerging to serve things, exhausting itself and returning to Wood as a natural principle. This depicts Fire's transformative and blazing nature, its dependence on substrate for existence, enabling transformation but requiring wood fuel rather than being sustenance-less. This establishes Fire's dynamic and formless essential nature in destiny analysis.

- **核心要点**：
  - 火对应南方、夏季
  - 火的本义是"化"与"毁"，变化万物
  - 火无正体，依附于木，燃尽复归

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_130]` `[trigger: 火之性质]` `[factor_trigger: element_fire AND direction_south]` `[role: 主干]` 火主于南，应夏。火之为言化也，毁也。阳在上，阴在下，毁然盛而变化万物也。然火无正体，体本木焉。 → 《三命通会》卷一#火之性质与方位

- **详细解说**：
  此条阐明火的基本属性。火主南方、应夏季。火的本质在于"化"与"毁"——通过炽烈燃烧来变化万物、毁坏旧形。木是火的母，钻木可以取火。火的特殊之处在于"无正体"——它没有固定形体，必须依附于燃料（木）才能存在，燃尽之后就复归于木。这种依附性、转化性是火的天然特质。在命理中，火旺之人多具变化、激情、转化之性。

- **校勘与字词辨析（双语）**：
  - **中文**："毁然盛"之"毁"通"炽"，指炽盛燃烧，非毁坏之意。
  - **English**："毁然盛" uses "毁" as variant of "炽" (blazing), not "destroying" in this context."""
    normalized_text_zh: str = """"""
    subject: str = "火之性质与方位"
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
        l1_anchor="smth_v1.0.0_火之性质与方位_001_L1",
    )
    version: str = "1.0.0"
