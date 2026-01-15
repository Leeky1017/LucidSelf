"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227811
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
    semantic_id="smth_v1.0.0_水之性质与循环_001",
    book_id="sanming",
    engine_id="bazi"
)
class 水之性质与循环(SemanticEntry):
    """
    - **原文（source_text）**：
  水主于北，应冬。水之为言润也。阴气濡润，任养万物也。水西而东，金所生也。水流曲折，顺下而达，乃自然之性也。

- **分字分词释义**：
  - **...
    """
    
    original_text: str = """- **原文（source_text）**：
  水主于北，应冬。水之为言润也。阴气濡润，任养万物也。水西而东，金所生也。水流曲折，顺下而达，乃自然之性也。

- **分字分词释义**：
  - **润**：滋润、濡养之意。
  - **濡润**：湿润滋养。
  - **任养**：任凭其滋养。
  - **水西而东**：水从西向东流动。
  - **顺下而达**：顺应地势向下流通。

- **规范化释义（primary_lang_explained）**：
  水对应北方，对应冬季。所谓"水"，其本义是"润"——阴气湿润，任凭其滋养万物。水从西方向东方流动，说明水由金所生。水流曲折弯转，顺应地势向下流通，这是自然的性质。

- **完整对等诠释（secondary_lang_full）**：
  Water governs the North and corresponds to Winter. Water's essence means "moistening"—yin qi moistens and nourishes all things. Water flows from west to east, as Metal generates Water. Water flows winding and meandering, flowing downward to reach its destination as a natural character. This depicts Water's nourishing and adaptive nature with winding flow, enabling nourishment and requiring metal source rather than flowing upward against nature. This establishes Water's wisdom and adaptation essential nature, completing the Five Elements cycle in destiny analysis, returning to Wood and completing the generation-restriction cycle in completeness.

- **核心要点**：
  - 水对应北方冬季，主滋润养育
  - 水由金生，从西向东流动
  - 水流曲折顺下，体现柔顺适应之性
  - 五行循环完整：水→木→火→土→金→水

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_132]` `[trigger: 水之性质]` `[factor_trigger: element_water AND direction_north]` `[role: 主干]` 水主于北，应冬。水之为言润也，阴气濡润，任养万物也。水西而东，金所生也。水流曲折，顺下而达，乃自然之性也。 → 《三命通会》卷一#水之性质与循环

- **详细解说**：
  此条阐明水的基本属性，并暗示五行循环的完整性。水主北方冬季，本义为"润"——阴气湿润万物，滋养生命。金是水的母，水从西向东流动接受金的滋养。水的自然形态是曲折弯转、顺应地势向下流通，这种柔顺性、适应性是水的天然特质。至此，五行循环完整呈现：水生木、木生火、火生土、土生金、金生水，形成闭环。在命理中，水旺之人多具智慧、柔顺、适应之性。

- **校勘与字词辨析（双语）**：
  - **中文**："濡润"，"濡"音rú，湿润之意，强调水的滋养功能。"任养"指任凭、听任其滋养，非"负责养育"。
  - **English**："濡润" (moistening) and "任养" (allowing to nourish) emphasize water's passive yet essential nurturing quality, not active responsibility."""
    normalized_text_zh: str = """"""
    subject: str = "水之性质与循环"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_水之性质与循环_001_L1",
    )
    version: str = "1.0.0"
