"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264316
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
    semantic_id="smth_v1.0.0_小运总论与男女顺逆起法_001",
    book_id="sanming",
    engine_id="bazi"
)
class 小运总论与男女顺逆起法(SemanticEntry):
    """
    - **原文（source_text）**：  
  论小运夫大运司十年之休咎，小运掌一岁之灾祥。是小运者，补大运之不足而立名也。古人以男起丙寅，女起丙申者何？盖元气之所孕，始于子，立于巳，子者字之。...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论小运夫大运司十年之休咎，小运掌一岁之灾祥。是小运者，补大运之不足而立名也。古人以男起丙寅，女起丙申者何？盖元气之所孕，始于子，立于巳，子者字之。始巳者包之始。自子推之，男左行三十而立于巳，女右去，积二十而合之己。巳正阳也，阴实从焉。是故圣人因是而制礼，参天两地，自然之数纪也。自己而壬之，男十月毓于寅，女十月毓于申，申为三阴，寅为三阳，故年运起焉。日生于甲，月生于庚，日月东西，夫妇之象也。甲统于寅，庚统于申，是故阴阳之合以正，将以顺性命之理耳。此小运所以男起丙寅顺行，女起壬申逆行，一定而不可易也。

- **分字分词释义**：
  - **大运司十年，小运掌一岁**：大运主十年大势，小运主每一年的细节灾祥。
  - **男起丙寅、女起丙申**：传统行年起点，男命由寅门顺数，女命由申门逆数。
  - **男左女右**：以子位为起点，男子向左数三十至巳，女子向右数二十至己，比附阳三十、阴二十之数。
  - **寅三阳、申三阴**：以寅、申为三阳三阴之门，承接日月夫妇之象。

- **规范化释义（primary_lang_explained）**：  
  本段首先界定了小运的地位：大运主管十年之休咎，小运则主管一岁之吉凶，是用来“补大运之不足”的精细行年系统。古法规定男命小运起于丙寅、顺行，女命起于丙申、逆行，并非任意，而是把“元气孕于子、成于巳”的象数结构投射到行年路径上：自子位推演，男子向左行三十步至巳，女子向右行二十步至己，以阳三十、阴二十对应成人之龄。巳为纯阳之地，阴从阳后，故以此为起点。又以“男十月毓于寅、女十月毓于申”说明胎成之门：寅为三阳、申为三阴，与“日生于甲、月生于庚，日月东西，夫妇之象”相配合，于是小运起点定在寅、申这对阴阳门户。如此一来，小运男起丙寅顺行、女起壬申逆行，便成为一套有内在数理与礼制根据的固定规则，而非可随意更改的算法。

- **完整对等诠释（secondary_lang_full）**：  
  This passage defines minor luck (xiao yun) as the system that governs yearly fortunes, supplementing the ten‑year major luck cycles. Major luck outlines the decade‑level trend; minor luck refines how each year within that decade unfolds. Classical doctrine states that for men, minor luck begins from Bing‑Yin and moves forward in the zodiac, whereas for women it begins from Bing‑Shen and moves backward. This is grounded in a numerological picture: primordial qi is conceived at Zi and established at Si; counting from Zi, the male path moves left thirty steps to Si, while the female path moves right twenty steps to Ji, corresponding to yang reaching maturity at thirty and yin at twenty. Si is a pure‑Yang place, with yin following behind. The text further links gestation to Yin and Shen as "three‑Yang" and "three‑Yin" gates, and connects "Day born in Jia, Month born in Geng; day and month stand East and West" to the stems Jia and Geng ruling Yin and Shen. Thus, the rule that men start minor luck from Bing‑Yin going forward and women from Ren‑Shen going backward is not arbitrary counting but part of a coherent cosmological framework in which yin‑yang, time, and human maturation are woven together.

- **核心要点**：
  - 小运以“年”为单位，是对大运十年格局的细化补充。
  - 男起丙寅顺行、女起丙申/壬申逆行，源于阴阳数理与胎成比附。
  - 寅申作为三阳三阴之门，与甲、庚及日月夫妇之象相互勾连。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_077]` `[trigger: 大运司十年]` `[factor_trigger: dayun_sishinian AND xiaoyun_zhang_yisui]` `[role: 主干]` 大运司十年之休咎，小运掌一岁之灾祥。 → 《三命通会》卷十#小运总论与男女顺逆起法
  - `[ns_smth_10_078]` `[trigger: 男起丙寅]` `[factor_trigger: nan_qi_bingyin AND nu_qi_bingshen]` `[role: 主干依赖]` 此小运所以男起丙寅顺行，女起壬申逆行，一定而不可易也。 → 《三命通会》卷十#小运总论与男女顺逆起法
  - `[ns_smth_10_079]` `[trigger: 寅为三阳]` `[factor_trigger: yin_wei_sanyang AND shen_wei_sanyin]` `[role: 条件分支]` 申为三阴，寅为三阳，故年运起焉。 → 《三命通会》卷十#小运总论与男女顺逆起法
  - `[ns_smth_10_080]` `[trigger: 参天两地]` `[factor_trigger: cantian_liangdi AND ziran_shuji]` `[role: 总结]` 参天两地，自然之数纪也。 → 《三命通会》卷十#小运总论与男女顺逆起法

- **详细解说**：  
  实务排盘中，许多流派只看大运，不排小运，作者在此明确反对这种简化：若只看十年大势而不看逐年行年，往往难以定位事件的具体发应之年。以“元气孕于子、立于巳”一段来看，其实是用宇宙生成观来为小运起点背书：自子到巳的距离，被编码成阳道三十年、阴道二十年的成熟期，再经寅申之门落实为行年起点。工程化时，可以把“小运起点”和“顺逆方向”单独作为可配置参数，而不要和大运本身混为一谈，既保留传统结构，又便于在不同算法间做对比实验。

- **校勘与字词辨析（双语）**：
  - **中文**：部分抄本对“男起丙寅、女起丙申”之后的起算细节略有出入，但主旨皆以寅、申为阴阳门户，且强调“一定而不可易”。此处据通行本，不逐字考证诸数目，只在释义中突出结构意义。
  - **English**: Some editions offer slightly different numerical schemes for the thirty and twenty steps, but these do not affect the core idea that Yang matures later than Yin and that Yin and Shen serve as the primary gates. The present reading focuses on structural symbolism rather than literal arithmetic."""
    normalized_text_zh: str = """"""
    subject: str = "小运总论与男女顺逆起法"
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
        l1_anchor="smth_v1.0.0_小运总论与男女顺逆起法_001_L1",
    )
    version: str = "1.0.0"
