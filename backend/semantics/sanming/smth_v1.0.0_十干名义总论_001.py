"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227920
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
    semantic_id="smth_v1.0.0_十干名义总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干名义总论(SemanticEntry):
    """
    - **原文（source_text）**：
  天气始于甲干，地气始于干支者，乃圣人究乎阴阳重轻之用也。著名以彰其德，立号以表其事，由是于甲相合，然后成纪。远可步于岁而统六十年，近可推于日而明十二时...
    """
    
    original_text: str = """- **原文（source_text）**：
  天气始于甲干，地气始于干支者，乃圣人究乎阴阳重轻之用也。著名以彰其德，立号以表其事，由是于甲相合，然后成纪。远可步于岁而统六十年，近可推于日而明十二时。岁运之盈虚，气令之早晏，万物生死，将今验古，或得而知之。

- **分字分词释义**：
  - **天气始于甲**：天之气始于甲木。
  - **阴阳重轻**：阴阳的轻重程度。
  - **著名以彰其德**：命名以彰显其德性。
  - **立号以表其事**：设立名号以表明其事。
  - **成纪**：形成纪录系统。
  - **步于岁**：推算年岁。
  - **气令之早晏**：节气的早晚。

- **规范化释义（primary_lang_explained）**：
  天之气始于甲干，地之气始于干支配合，这是圣人研究阴阳轻重之用的结果。通过命名来彰显其德性，设立名号来表明其事情，由此天干地支相合，形成纪录系统。远可以推算年岁而统领六十年，近可以推算日期而明确十二时辰。年运的盈虚、节气的早晚、万物的生死，拿今天来验证古代，都可以知晓。

- **完整对等诠释（secondary_lang_full）**：
  Heavenly qi begins with the Jia Stem; earthly qi begins with the combination of Stems and Branches—this is the result of sages investigating the degrees of yin and yang weight. Naming reveals virtue; establishing designations expresses matters. Thus Stems and Branches unite to form a recording system. It can extend to calculate years spanning sixty-year cycles; it can narrow to deduce days clarifying twelve hours. The fullness or depletion of yearly cycles, the earliness or lateness of seasonal qi, the life and death of myriad things—comparing present to past, all can be known.

- **核心要点**：
  - 天干地支体现圣人对阴阳轻重的研究
  - 著名立号以彰德表事
  - 干支相合形成纪录系统
  - 可远推六十年，近推十二时
  - 可知岁运盈虚、气令早晚、万物生死

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_148]` `[trigger: 十干名义总论]` `[factor_trigger: tiangan_meaning AND yinyang_weight]` `[role: 主干]` 天气始于甲干，地气始于干支者，乃圣人究乎阴阳重轻之用也。著名以彰其德，立号以表其事，由是于甲相合，然后成纪。 → 《三命通会》卷一#十干名义总论

- **详细解说**：
  此条为"论十干名字之义"章节的总论，阐述十干命名的深层意义。圣人研究阴阳轻重程度，通过命名（著名）来彰显各干的德性，设立名号（立号）来表明其功用，使天干地支相合形成完整的时间纪录系统。这套体系功能强大：远可推算六十年大周期，近可明确十二时辰；可以预知年运的盈虚（丰歉）、节气的早晚（气候）、万物的生死（物候），用今天的情况验证古代的记录，都可以得知。这说明干支不仅是时间符号，更是包含阴阳轻重、德性功用的完整象数系统。

- **校勘与字词辨析（双语）**：
  - **中文**："阴阳重轻"指阴阳的分量、程度。"盈虚"指丰盈与虚乏。"早晏"指早晚。
  - **English**: "Yin-yang weight" refers to degrees or proportions of yin and yang; "fullness-depletion" refers to abundance and scarcity; "early-late" refers to timing of seasonal changes."""
    normalized_text_zh: str = """"""
    subject: str = "十干名义总论"
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
        l1_anchor="smth_v1.0.0_十干名义总论_001_L1",
    )
    version: str = "1.0.0"
