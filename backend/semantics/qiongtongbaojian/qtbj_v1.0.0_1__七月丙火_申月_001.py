"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596775
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
    semantic_id="qtbj_v1.0.0_1__七月丙火_申月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1七月丙火申月(SemanticEntry):
    """
    - **原文（source_text）**：
  七月丙火，太阳转西，阳气衰矣。日近西山，见土皆晦，惟日照湖海，暮夜光天，故仍用壬水，辅映光辉。
  如壬多，取戊制方妙。有壬透干，又见戊土出干，可云科...
    """
    
    original_text: str = """- **原文（source_text）**：
  七月丙火，太阳转西，阳气衰矣。日近西山，见土皆晦，惟日照湖海，暮夜光天，故仍用壬水，辅映光辉。
  如壬多，取戊制方妙。有壬透干，又见戊土出干，可云科甲。如戊藏支内，不过生员。多壬无戊，平常人也。或戊多壬少，亦属常人。或多壬，一戊出制，所谓众杀猖狂，一仁可化，必主显达，有权职。
  一派辛金，又为弃命从才，奇特之造，虽不科甲，亦得恩荣，但多依亲戚而为进身之阶。从才者以水妻木子。

- **分字分词释义**：
  - **太阳转西**：太阳转向西方 / 申月特征 / 火衰
  - **日近西山**：太阳接近西山 / 将落 / 气衰
  - **日照湖海**：太阳照耀湖海 / 壬水功能 / 映辉
  - **暮夜光天**：在暮夜光耀天空 / 壬映丙 / 贵象
  - **众杀猖狂**：众多七杀猖狂 / 壬多 / 凶象
  - **一仁可化**：一个仁德可以化解 / 戊制壬 / 救应
  - **弃命从才**：放弃本命从财格 / 辛多 / 变格
  - **进身之阶**：晋升的阶梯 / 从财 / 靠亲戚

- **规范化释义（primary_lang_explained）**：
  七月（申月）的丙火，太阳转到了西方，阳气衰退了。太阳接近西山，见到土（山）都会遮晦光芒，只有“日照湖海”，在暮夜也能光耀天空，所以仍然用壬水，辅助映照光辉。
  如果壬水太多（杀重），取戊土（食神）制约才妙。有壬水透干，又见戊土透干，可以说是科甲。如果戊土藏在地支内，不过是生员（秀才）。壬水多而没有戊土，是平常人。或者戊土多而壬水少，也属常人。如果壬水多，有一个戊土出干制约，正如所谓的“众杀猖狂，一仁（戊）可化”，必主显达，有权职。
  如果一派辛金（财多），又是“弃命从财”，奇特的造化，虽然不中科甲，也能得到恩荣，但多依靠亲戚作为进身的阶梯。从财格的人，以水（官杀）为妻，木（印）为子（因为从财忌印比，故六亲取法不同，此处原文“水妻木子”疑为从财格通用口诀的特例或传抄差异，通常从财以财为父/妻）。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 7th Month (Monkey Month): The Sun turns West; Yang Qi declines. As the Sun nears the Western Mountains, seeing Earth obscures it. Only "Sun Shining on Lakes and Seas" can light up the sky at dusk; thus, still use Ren Water to reflect its brilliance.
  If Ren is excessive, taking Wu to control it is wondrous. If Ren is revealed and Wu is also revealed, it implies Civil Service. If Wu is hidden in branches, merely a student. Many Ren without Wu implies an ordinary person. Many Wu and few Ren is also ordinary. If there are many Ren and one Wu reveals to control, it is "Massed Killings Rampant, One Benevolence Can Transform", implying prominence and authority.
  If there is a mass of Xin Metal, it is "Abandon Life Follow Wealth", a unique structure. Though not Civil Service, one gains honors, often relying on relatives for advancement. For Follow Wealth, take Water as Wife and Wood as Child.

- **核心要点**：
  - **日近西山**：申月丙火气衰，忌土晦光。
  - **日照湖海**：喜壬水映照，虽在申月亦然。
  - **杀重制杀**：壬多需戊制。
  - **从财**：辛多无根，从财。

- **详细解说**：
  - 申月丙火病地，气势已弱。
  - 此时壬水虽为七杀，但也是“湖海”，能反衬太阳余辉。
  - 若壬水太多，则成"水患"，非"湖海"，需戊土堤坝。
  - "一仁可化"：通常指印化杀，这里指食神（戊）制杀，也借用了"仁"字（或许指戊土厚重之德）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_245]` `[trigger: 申月丙火]` `[factor_trigger: month_shen AND tiangan_bing AND tiangan_ren AND sun_on_lake]` `[role: 主干]` 七月丙火，太阳转西，阳气衰矣。日近西山，见土皆晦，惟日照湖海，暮夜光天。 → 《穷通宝鉴·三秋丙火》#14.1
  - `[ns_qttbj_246]` `[trigger: 众杀猖狂]` `[factor_trigger: month_shen AND tiangan_bing AND ren_multiple AND tiangan_wu AND massed_killings]` `[role: 条件分支]` 多壬，一戊出制，所谓众杀猖狂，一仁可化，必主显达，有权职。 → 《穷通宝鉴·三秋丙火》#14.1
  - `[ns_qttbj_247]` `[trigger: 从才格]` `[factor_trigger: month_shen AND tiangan_bing AND xin_multiple AND pattern_follow_wealth]` `[role: 条件分支]` 一派辛金，又为弃命从才，奇特之造，虽不科甲，亦得恩荣。 → 《穷通宝鉴·三秋丙火》#14.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 七月丙火（申月）"
    factor_refs: list = ['sun_on_lake', 'massed_killings', 'stepping_stone']
    
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
        l1_anchor="qtbj_v1.0.0_1__七月丙火_申月_001_L1",
    )
    version: str = "1.0.0"
