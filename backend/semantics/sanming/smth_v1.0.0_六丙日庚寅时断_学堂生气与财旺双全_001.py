"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157469
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
    semantic_id="smth_v1.0.0_六丙日庚寅时断_学堂生气与财旺双全_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日庚寅时断学堂生气与财旺双全(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日庚寅时断。

  六丙日生时庚寅，学堂生气助其身；运中有合通金局，必是荣华富贵人。丙日庚寅时，生气学堂，丙寅上长生，文章秀气；丙以庚辛为财，寅上庚绝丙...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日庚寅时断。

  六丙日生时庚寅，学堂生气助其身；运中有合通金局，必是荣华富贵人。丙日庚寅时，生气学堂，丙寅上长生，文章秀气；丙以庚辛为财，寅上庚绝丙旺。若通月气金局者财旺，富贵双全，喜西方运；不通局者财薄。

  丙子日庚寅时，生子月，近贵。癸酉月，行水木运，高贵；火木运，五品以上贵。未申、癸午年月，身居武职，大贵，寿浅。

  丙寅日庚寅时，贵不久。生酉申年月，世裔冷职。子丑寅未，贵显。纯寅尤吉。

  丙辰日庚寅时，生寅午戌未年月，妻贤子孝，富贵双全。申子，行北运，大贵。酉丑，富。

  丙午日庚寅时，年月无壬癸子未巳字，飞天禄马，贵。巳酉丑申，主文学，不贵即富。未月，伤官。辰月，先贫后富。亥月，行西运，贵显。

  丙申日庚寅时，亥卯未、申子辰二局，官印两旺，大贵。巳丑财局，吉。寅午戌火局，平。

  丙戌日庚寅时，生亥子月，贵显。申酉年月，行北方运；寅午戌，行官鬼运，俱大贵。若运临死绝，即入黄泉无疑。

  丙庚相合遇寅时，险难消除福自随；运至寒门名将相，时来平步上云梯。丙日庚寅时准，双亲衰旺离乡。妻儿早害晚荣昌，白虎归山正旺。木有成林松柏，生涯广聚财粮。堆金积玉满高堂，共羡人言上样。

- 分字分词释义：

  - **学堂生气**：寅为丙火长生之地，又为学堂位，主文学才华与生命力。
  - **丙庚相合**：丙火与庚金虽为克关系，但在特定条件下可形成合作。
  - **飞天禄马**：特殊格局名，禄马飞腾，主显贵。
  - **白虎归山**：比喻财星（庚金）得位，财运亨通。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，庚寅时」：

  - 丙火在寅为长生，庚金偏财虽在寅为绝地，但丙火身旺可用财；
  - 若月令通金局，财星得用，富贵双全；若不通金局，则财源薄弱；
  - 歌诀以「险难消除福自随」形容此格的转机特点。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Geng-Yin Hour":

  - Bing Fire at Yin reaches Long Life; though Geng Metal (Indirect Wealth) at Yin is at extinction, Bing Fire's strong body can utilize wealth.
  - If monthly pillar connects with Metal formation, wealth star becomes usable, achieving both riches and honor; without Metal formation connection, wealth sources remain thin.
  - The verse uses "dangers eliminated, fortune follows" to describe this pattern's turnaround characteristic.

- 核心要点：

  - 本格以「学堂生气」为核心，强调文学才华与身旺。
  - 身旺方能用财，通金局则财旺。
  - 歌诀强调：运至可平步青云，时来可名将相。

- 详细解说：

  1. **学堂生气的优势**  
     - 寅为丙火长生，日主有力；  
     - 学堂主文学才华，适合从事文职或学术工作。

  2. **财星的运用**  
     - 庚金偏财在寅为绝地，本身力量薄弱；  
     - 但若月令通金局，财星得根，可为用神。

  3. **六丙日的差异**  
     - 各日支因根气不同，吉凶有别；  
     - 身旺者较吉，身弱者财多身弱反凶。

- 校勘与字词辨析：

  - 「寒门名将相」指出身平凡但可达高位。
  - 「堆金积玉满高堂」形容财富丰厚。
  - **English**：
    - Metaphor describing abundant wealth.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_105]` `[trigger: 学堂生气]` `[factor_trigger: xuetang_shengqi AND zhu_qishen]` `[role: 主干]` 六丙日生时庚寅，学堂生气助其身。 → 《三命通会》卷八#六丙日庚寅时
  - `[ns_smth_08_106]` `[trigger: 通金局]` `[factor_trigger: tong_jinju AND ronghua_fugui]` `[role: 主干依赖]` 运中有合通金局，必是荣华富贵人。 → 《三命通会》卷八#六丙日庚寅时
  - `[ns_smth_08_107]` `[trigger: 飞天禄马]` `[factor_trigger: feitian_luma AND gui_xian]` `[role: 条件分支]` 年月无壬癸子未巳字，飞天禄马，贵。 → 《三命通会》卷八#六丙日庚寅时
  - `[ns_smth_08_108]` `[trigger: 堆金积玉]` `[factor_trigger: duijin_jiyu AND man_gaotang]` `[role: 总结]` 堆金积玉满高堂，共羡人言上样。 → 《三命通会》卷八#六丙日庚寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日庚寅时断：学堂生气与财旺双全"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_factor_169', 'bazi_semantic', 'bazi_state_factor_213', 'bazi_semantic', 'bazi_state_factor_170', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_metal_3', 'bazi_semantic', 'source_ref', 'rel_smth_08_079', 'xuetang_shengqi', 'rel_smth_08_080', 'shenwang_yongcai', 'rel_smth_08_081', 'tongjin_ju', 'evi_smth_08_079', 'xuetang_shengqi', 'rule_xuetang', 'evi_smth_08_080', 'shenwang_yongcai', 'rule_yongcai', 'evi_smth_08_081', 'baihu_guishan', 'rule_baihu', 'map_smth_08_053', 'map_smth_08_054']
    
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
        l1_anchor="smth_v1.0.0_六丙日庚寅时断_学堂生气与财旺双全_001_L1",
    )
    version: str = "1.0.0"
