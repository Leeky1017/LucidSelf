"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227839
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
    semantic_id="smth_v1.0.0_朱子论五行序位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 朱子论五行序位(SemanticEntry):
    """
    - **原文（source_text）**：
  朱子曰：五行之序，木为之始，水为之终，而土为之中。以河图、洛书之数言之，则水一木三而土五，皆阳之生数而不可易者也，故得以更迭为主，而为五行之纲。以德言...
    """
    
    original_text: str = """- **原文（source_text）**：
  朱子曰：五行之序，木为之始，水为之终，而土为之中。以河图、洛书之数言之，则水一木三而土五，皆阳之生数而不可易者也，故得以更迭为主，而为五行之纲。以德言之，则木为发生之性，水为贞静之体，而土又包育之母。故水之包五行也，以其流通贯彻而无不在也。木之包五行，以其归根反本而藏于此也。若夫土，则水火之所寄，金木之所资，居中而奠四方，二体而载万类者也。

- **分字分词释义**：
  - **更迭为主**：轮流担任主导。
  - **发生之性**：发生万物的本性。
  - **贞静之体**：坚贞静守的本体。
  - **包育之母**：包容养育的母体。
  - **流通贯彻**：流通贯穿。
  - **归根反本**：回归根本。
  - **二体而载万类**：阴阳二体承载万物。

- **规范化释义（primary_lang_explained）**：
  朱熹说：五行的顺序，木为开始，水为终结，土为中心。从河图洛书的数来说，水一、木三、土五，都是阳的生数而不可改变，所以能够轮流担任主导，成为五行的纲领。从德性来说，木有发生万物的本性，水有坚贞静守的本体，而土又是包容养育的母体。所以水能包含五行，是因为它流通贯穿无所不在；木能包含五行，是因为万物归根反本都藏于此；至于土，则是水火寄托之所、金木资源之地，居中而稳定四方，以阴阳二体承载万物。

- **完整对等诠释（secondary_lang_full）**：
  Zhu Xi discusses the Five Elements sequence: Wood as beginning, Water as ending, Earth as center. From Hetu and Luoshu numbers: Water 1, Wood 3, Earth 5—all yang generating numbers that alternate as masters. By virtue: Wood embodies generating nature, Water embodies steadfast stillness, Earth embodies nurturing motherhood.

- **核心要点**：
  - 引用朱熹论五行序位：木始水终土中
  - 水一木三土五为阳生数，轮流主导
  - 从德性看：木发生、水贞静、土包育
  - 水木土各有包含五行的特殊功能

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_136]` `[trigger: 朱子论五行序位]` `[factor_trigger: zhu_xi_citation AND wuxing_sequence]` `[role: 主干]` 朱子曰：五行之序，木为之始，水为之终，而土为之中。以德言之，则木为发生之性，水为贞静之体，而土又包育之母。 → 《三命通会》卷一#朱子论五行序位

- **详细解说**：
  此条引用宋代理学大师朱熹的论述，从哲学层面阐释五行。朱子指出，五行的顺序是木始水终土中，从德性看，木主发生、水主贞静、土主包育。

- **校勘与字词辨析（双语）**：
  - **中文**："贞静"之"贞"指坚贞守正，非贞节。
  - **English**："贞静" refers to steadfast and still, not chastity."""
    normalized_text_zh: str = """"""
    subject: str = "朱子论五行序位"
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
        l1_anchor="smth_v1.0.0_朱子论五行序位_001_L1",
    )
    version: str = "1.0.0"
