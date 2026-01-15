"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619956
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
    semantic_id="qtbj_v1.0.0_6__九月甲木_戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 6九月甲木戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  九月甲木，木星凋零，独爱丁火，壬癸滋扶。丁壬癸透，戊己亦透，此命配得中和，可许一榜。庚金得所，科甲定然。
  或见一二比肩，无庚金制之，平常人也。倘运...
    """
    
    original_text: str = """- **原文（source_text）**：
  九月甲木，木星凋零，独爱丁火，壬癸滋扶。丁壬癸透，戊己亦透，此命配得中和，可许一榜。庚金得所，科甲定然。
  或见一二比肩，无庚金制之，平常人也。倘运不得用，贫无立锥。
  一命，甲辰、甲戌、甲辰、甲戌、身伴明君，富贵寿考，此为天元一气，又名一才一用。遇比用才，专取季土。
  或见庚丙，可许入泮，白手成家。用火者，木妻火子，子肖妻贤。

- **分字分词释义**：
  - **木星凋零**：木气凋谢零落 / 戌月特征 / 木衰
  - **独爱丁火**：唯独喜爱丁火 / 暖木炼金 / 首要用神
  - **壬癸滋扶**：壬癸水滋润扶持 / 润燥 / 次要用神
  - **配得中和**：配合达到中和 / 调候得宜 / 吉格
  - **可许一榜**：可以许诺考中一榜 / 举人功名 / 贵象
  - **贫无立锥**：穷得没有立锥之地 / 极贫 / 无庚制比之害
  - **天元一气**：天干全是一种五行 / 特殊格局 / 四甲
  - **一才一用**：一个财一个用神 / 身财两停 / 贵格
  - **入泮**：进入学堂 / 考中秀才 / 功名起步
  - **木妻火子**：以木为妻、以火为子 / 六亲配置 / 子肖妻贤

- **规范化释义（primary_lang_explained）**：
  九月（戌月）的甲木，木气凋零，独爱丁火（暖局/炼金），以及壬癸水滋润扶持（润燥）。如果丁火、壬水、癸水都透出，戊己土也透出，这命造配合得中和，可以许诺中一榜（举人）。如果庚金得地（有力），科甲功名是一定的。
  如果见到一两个比肩（甲木），没有庚金来制约它们，只是普通人。如果大运也不得用，会贫穷到无立锥之地。
  有一个命造：甲辰年、甲戌月、甲辰日、甲戌时，身伴明君，富贵长寿，这是“天元一气”格，又叫“一财一用”。遇到比肩多而用财星，专取季土（辰戌丑未）为财。
  或者见到庚金丙火，可以许诺入泮（考中秀才），白手起家。用火的人，以木为妻，火为子，且子孙肖似自己，妻子贤惠。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 9th Month (Dog Month) is withered; it exclusively loves Ding Fire, supported by Ren/Gui Water. If Ding, Ren, Gui, and Wu/Ji are all revealed, the configuration is balanced, promising a degree. If Geng Metal is well-placed, Civil Service success is certain.
  If one or two Parallel Shoulders appear without Geng Metal to control them, one is an ordinary person. If Luck is not useful, one will be poor without a place to stand.
  One destiny: Jia-Chen, Jia-Xu, Jia-Chen, Jia-Xu. This person accompanied a wise ruler, enjoying wealth, nobility, and longevity. This is "Heavenly Origin One Qi", also called "One Wealth One Use". When meeting Parallel Shoulders and using Wealth, focus on Seasonal Earth.
  Or if Geng and Bing are seen, one may enter the academy (become a Xiucai) and build a family from scratch. Those using Fire take Wood as Wife and Fire as Child; the child resembles the father and the wife is virtuous.

- **核心要点**：
  - **首要用神**：丁火（暖/炼）。
  - **次要用神**：壬癸（润）、庚（制比）。
  - **天元一气**：四甲透干，地支辰戌冲（财旺），身财两停，大贵。
  - **比劫争财**：无庚制比，贫穷。

- **详细解说**：
  戌月土燥木枯。
  - 丁火是关键，既暖木又炼库中辛金。
  - 壬癸水不可缺，因为戌土燥，无水不能养木。
  - 比劫多（如四甲）必须有财（四库土）或杀（庚金）。文中所举“甲辰甲戌”例，是特殊格局（天元一气/仓龙出海），地支辰戌冲开财库，甲木以土为财，身旺财旺，故贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_147]` `[trigger: 戌月甲木]` `[factor_trigger: month_xu AND tiangan_jia AND tiangan_ding AND (tiangan_ren OR tiangan_gui)]` `[role: 主干]` 九月甲木，木星凋零，独爱丁火，壬癸滋扶。 → 《穷通宝鉴·三秋甲木》#5.6
  - `[ns_qttbj_148]` `[trigger: 戌月中和]` `[factor_trigger: month_xu AND tiangan_jia AND ding_revealed AND ren_revealed AND gui_revealed AND (tiangan_wu OR tiangan_ji)]` `[role: 主干依赖]` 丁壬癸透，戊己亦透，此命配得中和，可许一榜。 → 《穷通宝鉴·三秋甲木》#5.6
  - `[ns_qttbj_149]` `[trigger: 天元一气]` `[factor_trigger: pattern_heavenly_origin_one_qi AND tiangan_jia AND (dizhi_chen OR dizhi_xu)]` `[role: 条件分支]` 甲辰、甲戌、甲辰、甲戌，身伴明君，富贵寿考，此为天元一气。 → 《穷通宝鉴·三秋甲木》#5.6
  - `[ns_qttbj_150]` `[trigger: 比劫争财]` `[factor_trigger: month_xu AND tiangan_jia AND shishen_parallel AND NOT tiangan_geng]` `[role: 例外处理]` 或见一二比肩，无庚金制之，平常人也，倘运不得用，贫无立锥。 → 《穷通宝鉴·三秋甲木》#5.6"""
    normalized_text_zh: str = """"""
    subject: str = "6. 九月甲木（戌月）"
    factor_refs: list = ['pattern_heavenly_origin_one_qi', 'poor_without_place', 'enter_the_academy']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_6__九月甲木_戌月_001_L1",
    )
    version: str = "1.0.0"
