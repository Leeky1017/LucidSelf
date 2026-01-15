"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264412
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
    semantic_id="smth_v1.0.0_十干化气与统龙五运总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干化气与统龙五运总论(SemanticEntry):
    """
    - **原文（source_text）**：  
  论十干化气复阳子曰：十干合而化者，阴阳之配，夫妇之道也。遇六则合，遁三则化，以五子余数，至巳上得合，既合，遁虎统龙，龙主阳德，司天而成变化者也。子...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论十干化气复阳子曰：十干合而化者，阴阳之配，夫妇之道也。遇六则合，遁三则化，以五子余数，至巳上得合，既合，遁虎统龙，龙主阳德，司天而成变化者也。子者，坎之位，天一生水，媾精之象，胎娠阳中，故男子从子左行，三十至巳，阳也，故三十而娶；女子从子右行，二十至巳，阴也，故二十而嫁。此人事合五行之造化，讵可过于此期哉？东𡈼子至丁巳六数，故丁与壬合；丁壬化木，甲德统龙。南戊子至癸巳六数，故戊与癸合。戊癸化火，丙德统龙。西。庚子至乙巳六数，故乙与庚合。乙庚化金，庚德统龙。中甲子至己巳六数，故甲与己合。甲己化土，戊德统龙。北丙子至辛巳六数，故丙与辛合。丙辛化水，壬德统龙。甲己之岁，戊德统龙，以土司化黅天土气。乙庚之岁，庚德统龙，以金司化素天金气。丙辛之岁，壬德统龙，以水司化玄天水气。丁壬之岁，甲德统龙，以木司化苍天木气。戊癸之岁，丙德统龙，以火司化丹天火气。统龙天德，上下临御，以成变化，品汇咸亨。

- **规范化释义（primary_lang_explained）**：  
  承接“隔六而合”的数理，本段进一步提出“十干合而化”的观念：当一阴一阳两干不仅在数位上隔六相合，而且符合特定的步进与岁运结构时，就不只是普通的“合”，而会上升为“化气”——成为某一时期的主气与德星。作者以“夫妇之道”“统龙天德”比喻这种高阶结构：在甲己之岁，由戊德统龙，以土司化天地土气；乙庚之岁，由庚德统龙，以金司化金气；丙辛之岁，由壬德统龙，以水司化水气；丁壬之岁，由甲德统龙，以木司化木气；戊癸之岁，由丙德统龙，以火司化火气。所谓“遇六则合，遁三则化，以五子余数至巳上得合”，其实是从历法与遁甲体系中抽取的技术语，说明化气必须兼顾：一是阴阳配偶（夫妇之道），二是间距与步数（遇六、遁三），三是时间节点（以子为起点，经由巳位与“统龙”位置）。这些条件同时满足时，干合才能承担“统御一运之气”的角色，而不只是个体命局里的局部关系。

- **完整对等诠释（secondary_lang_full）**：  
  Building on the six‑step interval principle, this passage introduces the idea of "qi transformation" (hua qi) among the Heavenly Stems. When a Yin‑Yang pair of stems not only combines numerically but also aligns with specific cyclical steps and temporal markers, their interaction rises from ordinary combination to a higher level where it becomes the governing qi of a given period. The text likens this to the union of husband and wife and to a "virtue star commanding the Dragon"—the Dragon being the emblem of Heaven's active power. In years ruled by Jia‑Ji, the "virtue of Wu" commands the Dragon and oversees Earth; in Yi‑Geng years, the "virtue of Geng" presides over Metal; in Bing‑Xin years, the "virtue of Ren" governs Water; in Ding‑Ren years, the "virtue of Jia" governs Wood; and in Wu‑Gui years, the "virtue of Bing" governs Fire. The phrases "meeting at six" and "advancing by three" allude to calendrical stepping rules that start from Zi, pass through Si and reach the Dragon position. Only when the stems fall into this rhythm does the combination gain the authority to "transform" rather than merely coexist. In this sense, hua qi describes a macro‑pattern: it explains why certain years or cycles are dominated by one elemental quality at the level of climate, policy trends or collective mood, beyond the micro‑fortunes of any single chart.

- **核心要点**：
  - “十干合而化”是高于普通干合的一层结构，需要同时满足阴阳配偶、数位间距与岁运节律等条件。
  - 甲己、乙庚、丙辛、丁壬、戊癸五组，分别对应土德、金德、水德、木德、火德轮流“统龙司化”的年份或运段。
  - 化气理论主要用来刻画“大气候”和运势底色，而不是直接判定单个人一年的吉凶祸福。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_121]` `[trigger: 合而化者]` `[factor_trigger: heerhua_zhe AND yinyang_zhipei]` `[role: 主干]` 十干合而化者，阴阳之配，夫妇之道也。遇六则合，遁三则化。 → 《三命通会》卷十#十干化气与统龙五运总论
  - `[ns_smth_10_122]` `[trigger: 统龙天德]` `[factor_trigger: tonglong_tiande AND sihua_bianhua]` `[role: 主干依赖]` 遁虎统龙，龙主阳德，司天而成变化者也。 → 《三命通会》卷十#十干化气与统龙五运总论
  - `[ns_smth_10_123]` `[trigger: 五德轮替]` `[factor_trigger: wude_lunti AND tujin_shuimuhuo]` `[role: 条件分支]` 甲己之岁，戊德统龙；乙庚之岁，庚德统龙；丙辛之岁，壬德统龙。 → 《三命通会》卷十#十干化气与统龙五运总论
  - `[ns_smth_10_124]` `[trigger: 品汇咸亨]` `[factor_trigger: pinhui_xianheng AND shangxia_linyu]` `[role: 总结]` 统龙天德，上下临御，以成变化，品汇咸亨。 → 《三命通会》卷十#十干化气与统龙五运总论

- **详细解说**：  
  若说普通干合更偏向解释个体性格与局部事件，那么化气则是在回答：“这一段时间，哪一行在‘坐庄’？”——是土德当权，强调秩序、制度、土地和现实承载；还是水德当权，强调流动、调整与隐秘力量。工程化时，可以把“五德统龙”抽象为宏观环境因子：将具体年份或运段标记为 Earth‑Dominant / Metal‑Dominant / Water‑Dominant / Wood‑Dominant / Fire‑Dominant 等，然后再与个体命局的用神喜忌相交。这样既保留了传统“土德之世”“水德之世”等说法，又避免把化气直接等同于个人命运的好坏。此外，“夫妇之道”也提示：只有当阴阳配对完整，且有合适的时间与空间承接时，某种趋势才有条件真正“化成时代之气”。

- **校勘与字词辨析（双语）**：
  - **中文**：“遁虎统龙”“统龙天德”皆为古历法与气运术语，此处不作天文实体解，而视作“德星主持一运”的象征说法。
  - **English**: "Hua qi" is translated here as "transformation of qi" rather than "chemical change" to avoid materialist associations; it denotes a shift in dominant symbolic quality rather than a literal physical reaction."""
    normalized_text_zh: str = """"""
    subject: str = "十干化气与统龙五运总论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_十干化气与统龙五运总论_001_L1",
    )
    version: str = "1.0.0"
