"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596760
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
    semantic_id="qtbj_v1.0.0_4__六月丙火_未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4六月丙火未月(SemanticEntry):
    """
    - **原文（source_text）**：
  六月丙火退气，三伏生寒，壬水为用，取庚辅佐。
  庚壬两透，贴身相生，可云科甲名宦。若无庚有壬，不见戊出，小富小贵。见戊制壬，则为乡贤而已。
  或己...
    """
    
    original_text: str = """- **原文（source_text）**：
  六月丙火退气，三伏生寒，壬水为用，取庚辅佐。
  庚壬两透，贴身相生，可云科甲名宦。若无庚有壬，不见戊出，小富小贵。见戊制壬，则为乡贤而已。
  或己土出干混杂，此必庸夫俗子。或壬水浅，己土出干，其人贫困。无壬下格，贱而且顽，男女一理。
  或天干一派丙火，阳极生阴，干支两见庚壬，登科及第。
  总之六月丙火用壬，不同余月用壬，喜运行西北，六月用壬，喜运行西南。

- **分字分词释义**：
  - **退气**：火气退缩、势力减弱 / 未月特点 / 用神变化
  - **三伏生寒**：大暑后极热生寒意 / 物极必反 / 调候关键
  - **贴身相生**：庚壬紧邻相生 / 金生水 / 格局配合
  - **科甲名宦**：科举取士为官 / 显贵 / 吉象
  - **乡贤**：乡里贤人 / 次等贵格 / 中吉
  - **庸夫俗子**：平庸之人 / 己土混壬 / 凶象
  - **阳极生阴**：阳气极盛转生阴气 / 物极必反 / 自然规律

- **规范化释义（primary_lang_explained）**：
  六月（未月）的丙火，火气退缩，三伏天生起寒气，用壬水为用神，取庚金辅佐（生水）。
  庚金和壬水都透出，贴身相生（金生水），可以说是科甲名臣。如果无庚金只有壬水，不见戊土透出，是小富小贵。见到戊土制壬水，只是乡下的贤人而已。
  如果己土出干混杂（浊壬），这必是庸夫俗子。如果壬水浅（弱），己土出干，这人贫困。没有壬水是下格，贫贱而且顽固，男女都是这个道理。
  如果天干一派丙火，阳极生阴（火土燥需水），干支两处见到庚壬，登科及第。
  总之六月丙火用壬水，不同于其他月份用壬水。其他月份喜运行西北（金水），六月用壬水，喜运行西南（火金/申金长生位，此处原文可能有深意或传抄异同，通常六月火土旺喜金水，西南申位为壬水长生，故喜）。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 6th Month (Goat Month): Qi retreats; Three Fu Days generate cold. Use Ren Water, taking Geng to assist.
  If Geng and Ren are both revealed, generating each other closely, it implies Civil Service and fame. If there is Ren without Geng, and Wu does not appear, it is small wealth and nobility. Seeing Wu control Ren makes one merely a village worthy.
  If Ji Earth reveals and mixes, one is certainly a mediocrity. If Ren is shallow and Ji reveals, the person is poor. Without Ren, it is a lower pattern, lowly and stubborn; same for both sexes.
  If there is a mass of Bing Fire on stems, "Extreme Yang generates Yin", seeing Geng/Ren in both stems and branches leads to passing exams.
  In summary, using Ren for Bing in the 6th Month is different from other months. Usually, it likes Northwest; in the 6th Month, it likes Southwest (Shen, source of Water).

- **核心要点**：
  - **首要用神**：壬水（润土/映照）。未月土燥晦光，非壬不可。
  - **配合**：庚金（生壬）。
  - **忌讳**：己土（混壬/浊水）。
  - **运势**：喜西南（申金长生水之地）。

- **详细解说**：
  - 未月火气犹存但已退，土气最旺。
  - 己土透干最忌，因为己土是“沙土”，能混浊壬水，使“江湖”变成“泥塘”，丙火失辉。
  - “阳极生阴”：指物极必反，大暑之后阴气生。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_242]` `[trigger: 未月丙火]` `[factor_trigger: month_wei AND tiangan_bing AND tiangan_ren AND tiangan_geng]` `[role: 主干]` 六月丙火退气，三伏生寒，壬水为用，取庚辅佐。 → 《穷通宝鉴·三夏丙火》#13.4
  - `[ns_qttbj_243]` `[trigger: 己土混杂]` `[factor_trigger: month_wei AND tiangan_bing AND tiangan_ji AND fears_ji_mixing_ren]` `[role: 例外处理]` 己土出干混杂，此必庸夫俗子。壬水浅，己土出干，其人贫困。 → 《穷通宝鉴·三夏丙火》#13.4
  - `[ns_qttbj_244]` `[trigger: 阳极生阴]` `[factor_trigger: month_wei AND tiangan_bing_multiple AND tiangan_geng AND tiangan_ren AND extreme_yang_yin]` `[role: 条件分支]` 天干一派丙火，阳极生阴，干支两见庚壬，登科及第。 → 《穷通宝鉴·三夏丙火》#13.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 六月丙火（未月）"
    factor_refs: list = ['village_worthy', 'mediocrity']
    
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
        l1_anchor="qtbj_v1.0.0_4__六月丙火_未月_001_L1",
    )
    version: str = "1.0.0"
