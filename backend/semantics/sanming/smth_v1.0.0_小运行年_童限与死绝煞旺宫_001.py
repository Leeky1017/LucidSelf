"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264333
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
    semantic_id="smth_v1.0.0_小运行年_童限与死绝煞旺宫_001",
    book_id="sanming",
    engine_id="bazi"
)
class 小运行年童限与死绝煞旺宫(SemanticEntry):
    """
    - **原文（source_text）**：  
  或者以甲子旬如上起甲申旬，男起丙戍，女起壬辰；甲午旬男起丙申，女起壬寅；甲辰旬男起丙午，女起壬子；甲寅旬男起丙辰，女起壬戍，则非圣人原立起年运之义...
    """
    
    original_text: str = """- **原文（source_text）**：  
  或者以甲子旬如上起甲申旬，男起丙戍，女起壬辰；甲午旬男起丙申，女起壬寅；甲辰旬男起丙午，女起壬子；甲寅旬男起丙辰，女起壬戍，则非圣人原立起年运之义矣。今之谈命者，只以大运为用，殊不知小运亦有紧关。大运虽吉，其小运不通，未可便言吉利。如大运虽凶，其小运却吉，未可便作凶推。此小运又名行年，不可不究。醉醒子以为男女小运皆由时生，而行之逆顺亦以年定。如阳命阳年，甲子时生，堕地即行，乙丑二岁，丙寅一位，一年周而复始。阴命阳年，逆行亦然。尝试用之屡验，亦要与大运及柱中用神日主较量吉凶。童限未交大运，专用此法，行死绝煞旺之宫，必有危难，先详八字衰旺喜忌，然后以此参之，蔑不中矣。

- **规范化释义（primary_lang_explained）**：  
  作者先批评后世另起旬首、改换起点的小运法，认为偏离了圣人原本以寅申门户立起年运的意义。关键在于后半段：今人多只看大运，以为十年吉就十年皆吉，十年凶就十年皆凶，却忽视了小运（行年）在具体年份应验中的关键作用——大运虽吉，若行年不通，则未必能享其福；大运虽凶，若行年有救，也不宜一概作大凶推。醉醒子又提出一套以“时生”和“年之阴阳”来定小运顺逆的法门，说明古来行年系统本就存在多家说法。作者最后点明应用重点：童限未交大运之时，只能依靠小运行年来推断吉凶；若行年至死绝、煞旺之宫，而原局又衰弱或喜忌相反，则必有危难之虞，须先详察八字衰旺喜忌，再以行年参照，几无不验。

- **完整对等诠释（secondary_lang_full）**：  
  The author criticizes later practitioners who modify the starting points of minor luck by旬 segments—such as beginning from different stems in each ten‑stem cycle—arguing that such schemes deviate from the original intent behind establishing the yearly system at Yin and Shen. More importantly, he challenges the habit of treating major luck as sufficient: people often assume that a good decade guarantees good outcomes every year, or that a bad decade means unrelenting misfortune, yet they neglect the crucial role of the annual sequence. A favorable decade with obstructed yearly positions may not yield its promised blessings, while an adverse decade can be mitigated if the行年 runs through supportive palaces. Zui Xingzi's alternative method, which derives the direction of minor luck from the hour of birth and the yin‑yang nature of the birth year, shows that multiple annual systems co‑existed historically. Practically, before the first major luck arrives (during childhood limits), minor luck is almost the only time coordinate available: when the行年 passes through death, extinction or heavily malefic palaces, especially for a weak natal chart with unfavourable喜忌, serious danger is indicated. One must therefore weigh natal strength and preferences first, then use minor luck as a fine‑grained amplifier.

- **核心要点**：
  - 小运/行年与大运相辅相成，不可被大运替代。
  - 童限未交大运时，行年几乎是唯一时间坐标，行至死绝煞旺之宫易出大事。
  - 行年体系历来多家，关键在于与命局衰旺喜忌相参，而非死守某一算法。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_085]` `[trigger: 小运紧关]` `[factor_trigger: xiaoyun_jinguan AND dayun_buzu]` `[role: 主干]` 今之谈命者，只以大运为用，殊不知小运亦有紧关。 → 《三命通会》卷十#小运行年童限与死绝煞旺宫
  - `[ns_smth_10_086]` `[trigger: 童限专用]` `[factor_trigger: tongxian_zhuanyong AND sijue_shawang]` `[role: 主干依赖]` 童限未交大运，专用此法，行死绝煞旺之宫，必有危难。 → 《三命通会》卷十#小运行年童限与死绝煞旺宫
  - `[ns_smth_10_087]` `[trigger: 先详八字]` `[factor_trigger: xianxiang_bazi AND houcanyizhi]` `[role: 条件分支]` 先详八字衰旺喜忌，然后以此参之，今不中矣。 → 《三命通会》卷十#小运行年童限与死绝煞旺宫
  - `[ns_smth_10_088]` `[trigger: 屡验如神]` `[factor_trigger: lvyan_rushen AND dayun_xiaoyun_dieija]` `[role: 总结]` 尝试用之屡验，亦要与大运及柱中用神日主较量吉凶。 → 《三命通会》卷十#小运行年童限与死绝煞旺宫

- **详细解说**：  
  在工程建模中，可将大运视为“十年窗口”，小运与行年则是“窗口内的年度刻度”。本段提供了两个重要启示：一是不要把“十年吉”直接等同于“每年皆吉”，仍须通过行年定位事件发应年份；二是在童年阶段，由于大运尚未介入，行年的位置几乎就是全部时间信息，因此儿童大病、意外、迁徙多与“行年至死绝煞旺宫”高度重合。实作时，可以为童限阶段设计更高的行年权重，并在整体评分中加入“大运×行年×流年”的交互，而非简单线性叠加。

- **校勘与字词辨析（双语）**：
  - **中文**：醉醒子所述行年法与本书原法并列出现，显示古籍本就承认多种系统并存，此处不强行调和，只在释义中强调“以命局衰旺喜忌为先”的总原则。
  - **English**: Zui Xingzi's method is not endorsed or rejected outright; it is presented alongside the canonical system. The key takeaway is that any annual system must be evaluated against natal strength and preferences rather than adopted mechanically."""
    normalized_text_zh: str = """"""
    subject: str = "小运行年、童限与死绝煞旺宫"
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
        l1_anchor="smth_v1.0.0_小运行年_童限与死绝煞旺宫_001_L1",
    )
    version: str = "1.0.0"
