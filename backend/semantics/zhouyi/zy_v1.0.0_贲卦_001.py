"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899898
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
    semantic_id="zy_v1.0.0_贲卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 贲卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  贲：亨，小利有攸往。

  【彖传】
  《彖》曰：“贲，亨。柔来而文刚，故亨；分刚上而文柔，故小利有攸往。天文也；文明以止，人文也。...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  贲：亨，小利有攸往。

  【彖传】
  《彖》曰：“贲，亨。柔来而文刚，故亨；分刚上而文柔，故小利有攸往。天文也；文明以止，人文也。观乎天文，以察时变；观乎人文，以化成天下。”

  【象传】
  《象》曰：山下有火，贲；君子以明庶政，无敢折狱。

  【爻辞】
  初九，贲其趾，舍车而徒。
  六二，贲其须。
  九三，贲如，濡如，永贞吉。
  六四，贲如，皤如，白马翰如；匪寇，婚媾。
  六五，贲于丘园，束帛戋戋；吝，终吉。
  上九，白贲，无咎。

- 分字分词释义：

  - **贲**：文彩、装饰之意，引申为礼仪、文明、审美与文化制度的修饰作用。
  - **柔来而文刚 / 分刚上而文柔**：阴柔之质来润饰阳刚，使刚不粗暴；又将阳刚之德上移，用以规范柔顺，使柔不至软烂。
  - **天文 / 人文**：天文是日月星辰、节气运行的自然纹理；人文是礼乐制度、文化风俗的人间纹理。
  - **明庶政，无敢折狱**：以明察之智治理众多政务，却不轻易决断刑狱，强调在用刑问题上要慎之又慎。
  - **贲其趾 / 贲其须**：从脚趾到胡须的修饰，比喻从细节礼节开始的装饰。
  - **贲如，濡如 / 皤如 / 白贲**：有润泽之饰、有素白之饰，象征适度润饰、质朴素雅与回归简素。
  - **束帛戋戋**：成束的细帛，数量不多，象征“礼不在厚贵，在乎有节”。

- **规范化释义（primary_lang_explained）**：

  贲卦谈“文饰与文明”：如何在不损害本质的前提下，以合宜的装饰、礼仪与文化制度来润色刚柔，使人与社会更可亲、更可久。卦辞“贲：亨，小利有攸往”指出：适度的修饰与文化建设可以带来通达，但过度追求外饰则不宜大举进取，只适合“小利有攸往”。

  彖传把贲分成“天文”与“人文”：观天文，用以察觉时序与气候的变迁；观人文，用以化成天下，使人心趋于和谐。象传“山下有火，贲；君子以明庶政，无敢折狱”提醒：火在山下，光明藏于厚重之内，象征内在光明、外在稳重——君子应以此光明处理众务，却不轻率用刑，以防“文饰”堕为“苛刻之法”。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Bi, "Adornment" or "Grace", explores the role of beauty, culture, and refinement in human life. The Judgment, "Bi: success; in small matters it is favorable to have somewhere to go", suggests that while adornment and culture are valuable, they should not overshadow substance. True grace comes from balancing inner reality with outward form.

- 核心要点：

  - 贲卦强调**内外相称的修饰**：文饰不应掩盖本质，而是让刚柔更可亲、可久。
  - “天文 / 人文”的区分，将自然纹理与文化纹理置于同一框架，有利于从时间因子与文化因子两端建模。
  - 爻辞提示：从细节礼节到整体风格，装饰可以渐渐丰富，但最高处仍以“白贲”之素朴为归结。

- 详细解说：

  从卦象看，艮为山在上，离为火在下，火光照亮山体之下，山体为火光提供依托。此象既有光明之用，又有止息之能：装饰与规范同在。与噬嗑相比，噬嗑偏重“雷火断案”，贲偏重“火山润物”：前者基于是非断决，后者基于礼文之饰。

  贲卦的难点在于“度”：太少则粗野，太多则虚饰。九三“贲如，濡如，永贞吉”提供了一种平衡：润饰得宜、内外相称，并能长期坚持，才会有久远之吉；上九“白贲，无咎”则提醒：修饰的高境界是在素白中见文彩，而非倚赖繁缛色彩与形式堆砌。

  在个人与组织层面，贲卦适合作为“风格与文化设计”的参照：在制度、仪式、界面、语言等方面适度引入“文彩”，但始终保留“山下之火”的根本——真实与稳重。若过度追求形式，就会偏离“无敢折狱”的谨慎原则，容易在关键时刻因形式主义而误判。"""
    normalized_text_zh: str = """"""
    subject: str = "贲卦（䷕）"
    factor_refs: list = ['zhouyi_gua_bi']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_贲卦_001_L1",
    )
    version: str = "1.0.0"
