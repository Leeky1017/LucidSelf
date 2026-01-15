"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619747
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
    semantic_id="qtbj_v1.0.0_2__春季之木_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2春季之木(SemanticEntry):
    """
    - **原文（source_text）**：
  木生于春，余寒犹存。喜火温暖，则无盘屈之患。藉水资扶，而有舒畅之美。春初不宜水盛，阴浓则根损枝枯。春木阳气烦燥，无水则叶藁根枯。是以水火二物，既济方佳...
    """
    
    original_text: str = """- **原文（source_text）**：
  木生于春，余寒犹存。喜火温暖，则无盘屈之患。藉水资扶，而有舒畅之美。春初不宜水盛，阴浓则根损枝枯。春木阳气烦燥，无水则叶藁根枯。是以水火二物，既济方佳。土多而损力，土薄则财丰。忌逢金重伤残克伐，一生不闲。设使木旺，得金则良，终生获福。

- **分字分词释义**：
  - **余寒犹存**：冬天的寒气尚未完全消退 / 初春气候 / 调候需火
  - **盘屈**：盘绕弯曲 / 冻僵无法伸展 / 寒木之象
  - **藉**：借助、依靠 / 水的辅助作用 / 资扶之功
  - **舒畅**：舒展畅达 / 木的理想生长状态 / 水润之美
  - **阴浓**：阴气浓重 / 水多寒重 / 不利春木
  - **阳气烦燥**：阳气过于躁动 / 春末木气过旺 / 需水润
  - **叶藁根枯**：叶片枯萎根部干枯 / 无水之害 / 燥木之患
  - **既济**：水火调和 / 《易经》卦名 / 阴阳平衡之吉象
  - **损力**：消耗木的力量 / 土多耗身 / 财多身弱
  - **伤残克伐**：金克木导致的伤害 / 金重克身 / 一生劳碌

- **规范化释义（primary_lang_explained）**：
  木生在春天，冬天的余寒还存在。喜欢火来温暖，就没有盘结弯曲的祸患。借助水的滋润扶助，就有舒畅条达的美感。初春（寅月）不宜水太盛，水多阴气浓重则会损伤根基导致枝叶枯萎。春末木的阳气烦躁，没有水则叶枯根死。所以水和火这两样东西，要配合得当（既济）才好。土多了会耗损木力，土薄反而财气丰厚。忌讳遇到金太重来进行克伐，会导致一生劳碌不安。如果木非常旺盛，得到金的修剪就是好事，终生都能获福。

- **完整对等诠释（secondary_lang_full）**：
  Wood born in Spring still has residual coldness. It likes Fire for warmth, preventing the trouble of being twisted. Borrowing Water for support brings the beauty of smoothness and expansion. In early Spring, excessive Water is not suitable; heavy Yin damages the roots and withers the branches. Spring Wood has restless Yang energy; without Water, leaves wither and roots dry up. Therefore, Water and Fire, when properly balanced (Ji Ji), are best. Excessive Earth drains its strength; thin Earth brings abundant Wealth. It dreads heavy Metal causing injury and suppression, leading to a life of toil. However, if the Wood is prosperous, obtaining Metal is good, bringing lifelong blessings.

- **核心要点**：
  - 调候：初春余寒，首取火暖（丙火）。
  - 滋润：阳气燥，次取水润（癸水）。
  - 平衡：水火既济为上。
  - 忌讳：土多耗身，金重克身（除非木极旺）。

- **详细解说**：
  春木（寅卯辰月）的特点是“寒”与“燥”的交替。
  - 初春（寅月）：寒气未退，先火后水。
  - 仲春（卯月）：阳气渐盛，水火并用。
  - 暮春（辰月）：阳气燥，先水后火。
  总之，春木是生发之机，最怕“冻”（水多无火）和“伤”（金多无火）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_046]` `[trigger: 春木调候]` `[factor_trigger: season_spring AND element_wood AND element_fire]` `[role: 主干]` 木生于春，余寒犹存，喜火温暖，则无盘屈之患。 → 《穷通宝鉴·论木》#2.2
  - `[ns_qttbj_047]` `[trigger: 春木调候]` `[factor_trigger: season_spring AND element_wood AND element_water]` `[role: 主干依赖]` 藉水资扶，而有舒畅之美。 → 《穷通宝鉴·论木》#2.2
  - `[ns_qttbj_048]` `[trigger: 春木忌水盛]` `[factor_trigger: season_spring AND element_wood AND water_excessive]` `[role: 例外处理]` 春初不宜水盛，阴浓则根损枝枯。 → 《穷通宝鉴·论木》#2.2
  - `[ns_qttbj_049]` `[trigger: 春木需水]` `[factor_trigger: season_spring AND element_wood AND NOT element_water]` `[role: 条件分支]` 春木阳气烦燥，无水则叶藁根枯。 → 《穷通宝鉴·论木》#2.2
  - `[ns_qttbj_050]` `[trigger: 水火既济]` `[factor_trigger: principle_jiji AND element_water AND element_fire]` `[role: 总结]` 水火二物，既济方佳。 → 《穷通宝鉴·论木》#2.2
  - `[ns_qttbj_051]` `[trigger: 春木忌金]` `[factor_trigger: season_spring AND element_wood AND (metal_excessive OR wood_prosperous)]` `[role: 例外处理]` 忌逢金重伤残克伐，一生不闲；木旺得金则良。 → 《穷通宝鉴·论木》#2.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 春季之木"
    factor_refs: list = ['residual_cold', 'twisted_frozen', 'principle_jiji', 'restless_yang_heat']
    
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
        l1_anchor="qtbj_v1.0.0_2__春季之木_001_L1",
    )
    version: str = "1.0.0"
