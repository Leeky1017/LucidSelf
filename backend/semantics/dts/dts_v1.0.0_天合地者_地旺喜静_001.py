"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997271
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
    semantic_id="dts_v1.0.0_天合地者_地旺喜静_001",
    book_id="dts",
    engine_id="bazi"
)
class 天合地者地旺喜静(SemanticEntry):
    """
    - **原文（source_text）**：
  天合地者，地旺喜静。

- 原注（原文注解）：
  　　如戊子（戊子癸水财），己亥（己亥甲木官，壬水财），壬午（壬午丁火财，己土官），癸巳（癸巳戊土官...
    """
    
    original_text: str = """- **原文（source_text）**：
  天合地者，地旺喜静。

- 原注（原文注解）：
  　　如戊子（戊子癸水财），己亥（己亥甲木官，壬水财），壬午（壬午丁火财，己土官），癸巳（癸巳戊土官，丙火财）之类，皆支中人元与天干相合，此乃下财官，旺则得其用矣，不直冲坏。
  　　甲申（申中庚生壬，壬生甲）戊寅（寅中甲生丙，丙生戊），是为煞印相生。
  　　庚寅（寅中丙生戊，戊生庚）癸丑（丑中巳生辛，辛生癸），亦是煞印两旺。

- 分字分词释义：
  - 天合地：天干与地支中人元成合。
  - 地旺喜静：地支旺时，不宜冲动其合局。

- **规范化释义（primary_lang_explained）**：
  天干与地支成合，多为下财官之象；旺时当静以成用，不可轻冲破。其间又有"煞印相生""煞印两旺"之格，皆须随局裁取。

- **次语种完整诠释（secondary_lang_full）**:  
  When a heavenly stem combines with a hidden stem inside the earth branch, forming a heaven–earth union, the branch often carries wealth or office on behalf of the stem. When the branch is strong, this combined structure prefers stillness: it works best when allowed to remain settled, consolidating resources and authority, and is damaged by clashes or violent movement that break the union apart. In such charts, repeated shocks to the branch can dissolve what the union has patiently woven, whereas quiet, stable circumstances let the lower forces ripen and be used. This also includes Sha–Yin patterns where Killing and Resource support one another beneath the surface: as long as the earth side is vigorous and undisturbed, the joined power can be harnessed; if the base is shaken, the very strength of the union turns into a point of vulnerability.

- **核心要点**：
  - 天合地多主下财官或隐伏之力，关键在地支是否真旺、能否安静守成；
  - 地旺之时合局宜静不宜动，尤忌运岁频频冲破、拆散合局根基；
  - 煞印相生、煞印两旺等格局，要在“守合”与“避冲”之间细致拿捏取用。

- **详细解说**：
  所谓“天合地”，是指天干与地支中的藏干成合，如戊子、己亥、壬午、癸巳等，往往在地支中隐藏着财官或煞印等用神。当地支本身旺盛得令，这种合局就像地下已经搭好的结构：财官之力、煞印之力都在其中酝酿，只待时机成熟而上用。此时最忌的不是静，而是乱；越去冲动、拆解、折腾，越容易把本可成就的局面打碎。

  因此古书说“地旺喜静”：地支为根、为承载，旺极之时更要保持环境的稳定与和合，使下财官或煞印之力能在不受冲击的前提下慢慢成形。断此条时，一要看天合地之结构是否成立，二要看地支是否真旺，三要看运岁是助其守静，还是来冲破合局；同时，对“煞印相生”“煞印两旺”等格局，也要在此原则下衡量取用，而非一味好高务动。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_091]` `[trigger: 命局形成天合地且地支旺盛]` `[factor_trigger: tiangan_dizhi_he_pattern=有 & dizhi_vigor_level=旺 & combination_stability=静守]` `[role: 主干]` 天合地而地旺，多主下财官或格局力量已在根部成形，宜以守静养成，不宜频繁折腾。 → 《滴天髓·地支论》#天合地者地旺喜静
  - `[ns_dts_092]` `[trigger: 天合地局遇岁运频繁冲克合支]` `[factor_trigger: combination_stability=冲破 & combination_protection=无]` `[role: 主干依赖]` 合局本宜静守，若岁运再三冲克合支，多应已成之事被拆散、既定的资源与关系被打乱。 → 《滴天髓·地支论》#天合地者地旺喜静
  - `[ns_dts_093]` `[trigger: 命局见煞印相生或煞印两旺兼有天合地]` `[factor_trigger: shayin_pattern_type=煞印相生/两旺 & combination_protection=守静]` `[role: 条件分支]` 煞印相生、两旺而又天合地者，往往格局有成，但更需环境安稳以护其合，不可好高务动。 → 《滴天髓·地支论》#天合地者地旺喜静
  - `[ns_dts_157]` `[trigger: 合局被冲破]` `[factor_trigger: combination_stability=冲破]` `[role: 例外处理]` 天合地而合支被冲破，原本潜成之局一朝散尽，静守之功毁于一旦。 → 《滴天髓·地支论》#天合地者地旺喜静
  - `[ns_dts_158]` `[trigger: 守合避冲总则]` `[factor_trigger: combination_protection=守静]` `[role: 总结]` 天合地而地旺，守合避冲为第一要务，合稳则局成，合破则功散。 → 《滴天髓·地支论》#天合地者地旺喜静

 - **校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "天合地者，地旺喜静。"
    factor_refs: list = ['tianhedi', 'diwang', 'xijing', 'hehua', 'wangchong', 'qingxie']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_天合地者_地旺喜静_001_L1",
    )
    version: str = "1.0.0"
