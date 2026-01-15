"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596695
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
    semantic_id="qtbj_v1.0.0_4__三月丙火_辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4三月丙火辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  三月丙火，气渐炎升，用壬水。或成土局，取甲为辅，壬不可离。壬甲两透，科甲定宜，惟忌庚出制甲，则秀才而已。无甲用庚，助壬水泄土气。
  壬透甲藏，富大贵...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月丙火，气渐炎升，用壬水。或成土局，取甲为辅，壬不可离。壬甲两透，科甲定宜，惟忌庚出制甲，则秀才而已。无甲用庚，助壬水泄土气。
  壬透甲藏，富大贵小，有甲无壬，劳碌浊富。壬藏无甲，一介寒儒。壬甲两无，愚贱之辈。乙丁杂乱，定必属凡夫。
  用壬者，金妻水子。用甲者，水妻木子。

- **分字分词释义**：
  - **气渐炎升**：火气逐渐炎热上升 / 辰月特征 / 近夏
  - **壬不可离**：壬水不可离开 / 调候必需 / 核心
  - **科甲定宜**：科举功名适宜 / 壬甲透 / 最贵
  - **富大贵小**：富有大但贵气小 / 壬透甲藏 / 次等
  - **劳碌浊富**：劳碌的浊富 / 有甲无壬 / 次等
  - **一介寒儒**：一个贫寒的书生 / 壬藏无甲 / 清贫
  - **愚贱之辈**：愚蠢贫贱之人 / 壬甲两无 / 凶

- **规范化释义（primary_lang_explained）**：
  三月（辰月）的丙火，火气逐渐炎热上升，用壬水（既济/调候）。如果地支合成土局（晦光/泄气），取甲木（疏土）为辅助，但壬水不可离开（土燥需水润）。壬水和甲木两透，科甲功名适宜。只忌讳庚金透出制约甲木，那样就只是秀才而已。如果没有甲木，就用庚金，帮助壬水并泄土气（土生金，金生水）。
  壬水透出甲木藏支，富大贵小。有甲木无壬水，劳碌的浊富。壬水藏支无甲木，一介寒儒。壬甲全无，愚蠢贫贱之辈。乙木丁火杂乱透出，必定属于凡夫俗子。
  用壬水的人，金为妻水为子。用甲木的人，水为妻木为子。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 3rd Month (Dragon Month): Qi gradually becomes hot and rises; use Ren Water. If branches form an Earth frame, take Jia Wood to assist, but Ren cannot be absent. If Ren and Jia are both revealed, Civil Service is suitable; strictly dread Geng revealing to control Jia, reducing one to merely a Xiucai. Without Jia, use Geng to assist Ren and leak Earth's Qi.
  If Ren is revealed and Jia hidden, wealth is great but nobility small. With Jia but no Ren, one is toiling and turbidly rich. With Ren hidden and no Jia, a poor scholar. With neither Ren nor Jia, a stupid and lowly person. If Yi and Ding are mixed in disorder, one is certainly a commoner.

- **核心要点**：
  - **首要用神**：壬水（调候/映照）。辰月近夏，火气渐炎。
  - **配合用神**：甲木（疏土）。辰为湿土，晦火光，需甲木破土生身。
  - **忌讳**：庚金制甲（破用）。
  - **次选**：无甲用庚（化土生水）。

- **详细解说**：
  - 辰月是丙火冠带位，进气。
  - 关键在于“土重晦光”。丙火最怕土（食伤），尤其是湿土（辰丑），如云遮日。
  - 甲木是破云雾（土）的风，壬水是映照日光的湖。
  - 乙丁杂乱：乙木不能疏土（力弱），丁火助炎燥土，故为凡夫。
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_230]` `[trigger: 辰月丙火]` `[factor_trigger: month_chen AND tiangan_bing AND tiangan_ren AND tiangan_jia]` `[role: 主干]` 三月丙火，气渐炎升，用壬水。或成土局，取甲为辅，壬不可离。 → 《穷通宝鉴·三春丙火》#12.4
  - `[ns_qttbj_231]` `[trigger: 壬甲配合]` `[factor_trigger: month_chen AND tiangan_bing AND tiangan_ren AND tiangan_jia AND NOT tiangan_geng]` `[role: 条件分支]` 壬甲两透，科甲定宜，惟忌庚出制甲，则秀才而已。 → 《穷通宝鉴·三春丙火》#12.4
  - `[ns_qttbj_232]` `[trigger: 壬甲层次]` `[factor_trigger: month_chen AND tiangan_bing AND ren_jia_hierarchy]` `[role: 总结]` 壬透甲藏，富大贵小。有甲无壬，劳碌浊富。壬藏无甲，一介寒儒。壬甲两无，愚贱之辈。 → 《穷通宝鉴·三春丙火》#12.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 三月丙火（辰月）"
    factor_refs: list = ['earth_obscures_fire', 'turbid_wealth']
    
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
        l1_anchor="qtbj_v1.0.0_4__三月丙火_辰月_001_L1",
    )
    version: str = "1.0.0"
