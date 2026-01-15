"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264456
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
    semantic_id="smth_v1.0.0_咸池桃花煞_沐浴之地的情欲与破败_001",
    book_id="sanming",
    engine_id="bazi"
)
class 咸池桃花煞沐浴之地的情欲与破败(SemanticEntry):
    """
    - **原文（source_text）**：  
  特达论咸池按此煞须天干纳音与地同类方是。若只论寅午戌在卯，天干纳音或不属火，非是。此煞亦因三合而取，故附于后。淮南子曰：日出扶桑，入于咸池。故五行...
    """
    
    original_text: str = """- **原文（source_text）**：  
  特达论咸池按此煞须天干纳音与地同类方是。若只论寅午戌在卯，天干纳音或不属火，非是。此煞亦因三合而取，故附于后。淮南子曰：日出扶桑，入于咸池。故五行沐浴之地名咸池，是取日入之义。万物暗昧之时，寅午戌卯、己酉丑午、申子辰、酉亥卯未子，即长生第二位沐浴之宫是也。一名败神，一名桃花煞，其神主奸邪淫鄙。如生旺，则美容仪，躭酒色，疏财好欢，破散家业，惟务贪淫。如死绝，落魄不检，言行狡诈，游荡𫎟赙，忘恩失信，私滥奸淫，靡所不为。与元辰并，更临生旺者，多得匪人为妻。与贵人建禄并，多因油盐酒货得生，或因妇人暗昧之财起家，平生有水厄涝𤹮之疾，累𮞸遗失暗昧之灾。此神入命，有破无成，非为吉兆，妇人尤忌之。

- **规范化释义（primary_lang_explained）**：  
  咸池为五行“沐浴之地”，原义取自“日入于咸池”：光线将尽、万物蒙昧，是一天中既柔软又模糊的时刻。命理上，咸池需同时满足天干纳音与地支同属一行，并依三合局定位在长生之后的第二位——沐浴宫，因此呈现出强烈的桃花、声色与破败特征。生旺时，咸池多表现在外形与气质上：容貌姣好、风姿动人，极易沉迷酒色与享乐，慷慨疏财却不重积蓄，家业易被消耗；落在死绝处，则更偏向行为与价值层面的失序：散漫不检、出入暗昧场所、轻诺寡信。与元辰相并且生旺者，多有“妻非良配”“伴侣出身复杂”的隐忧；与贵人、禄位并者，则往往通过酒色、饮食、交际与异性资源“起家”，但同时伴随水厄、疾病与反复的暗损。总体来说，咸池是一颗“以魅力换资源”的星，福祸同体，关键在于能否以自律与结构化方式承载这股能量。

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph portrays Xianchi, the so‑called Peach Blossom Bath star, as the embodiment of the "bathing" phase in the Five Elements life cycle. Drawing on the image of the Sun sinking into the mythic Xianchi pool, it associates this star with twilight—when forms blur, vigilance relaxes and desires easily slip their leash. Technically, Xianchi is only considered active when the stem's na‑yin element matches that of the branch and when the branch occupies the bathing position within its triad. When strong, it lends beauty, charm and social magnetism, but also inclines people to indulgence in wine, sex and entertainment, spending freely and undermining family wealth. When weak or in dead positions, it correlates more with dissolute habits, shady dealings and breaches of trust. Combined with certain fate‑palace markers, it may signify marriage to an unorthodox or morally compromised partner; with nobles and salary positions, it often describes careers built around hospitality, nightlife or industries revolving around desire. Across scenarios, the refrain is the same: where Xianchi is prominent, there is "breaking without building" unless the person cultivates strong internal discipline and constructive outlets for attraction and pleasure.

- **核心要点**：
  - 咸池源于“沐浴之地”，与日落、昏昧、情欲与审美高度相关。
  - 生旺则多表现为外在魅力与享乐主义；死绝则偏向行为失序与暗昧损耗。
  - 与贵人、禄位同宫时，常以“桃花资源”换取生计或阶层流动，但代价显著。

- **详细解说**：  
  在现代解析中，咸池不宜简单等同“淫荡”或“坏人”，更适合被视为“感官与关系强度过高”的信号：命主在亲密、消费与社交领域有更大的能量通道，若缺乏边界感与价值框架，就容易在这些领域里反复破坏已有结构。工程化时，可以为咸池建立一个“感官—风险”二维因子：一轴是审美与魅力，一轴是自律与边界。生旺且得印、官、正财制约者，往往能把桃花转化为审美职业、人际资源或品牌影响力；落死绝又逢劫耗煞者，则更可能体现为自我消耗与关系动荡。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_145]` `[trigger: 日入咸池]` `[factor_trigger: riru_xianchi AND muyu_zhidi]` `[role: 主干]` 淮南子曰：日出扶桑，入于咸池。故五行沐浴之地名咸池，是取日入之义。 → 《三命通会》卷十#咸池桃花煞
  - `[ns_smth_10_146]` `[trigger: 败神桃花]` `[factor_trigger: baishen_taohua AND jianjian_yinbi]` `[role: 主干依赖]` 一名败神，一名桃花煞，其神主奸邪淫鄙。 → 《三命通会》卷十#咸池桃花煞
  - `[ns_smth_10_147]` `[trigger: 生旺美容]` `[factor_trigger: shengwang_meirong AND danjiu_shucai]` `[role: 条件分支]` 如生旺，则美容仪，躭酒色，疏财好欢，破散家业。 → 《三命通会》卷十#咸池桃花煞
  - `[ns_smth_10_148]` `[trigger: 有破无成]` `[factor_trigger: youpuo_wucheng AND furen_youji]` `[role: 总结]` 此神入命，有破无成，非为吉兆，妇人尤忌之。 → 《三命通会》卷十#咸池桃花煞

- **校勘与字词辨析（双语）**：
  - **中文**：“一名败神，一名桃花煞”强调其“破多立少”的基调，本精校在释义中用“破大于立”“以魅力换资源”来拆解。
  - **English**: The label "Peach Blossom" is culturally loaded; here it is used analytically to denote intensified relational and sensual dynamics, not as a moral condemnation."""
    normalized_text_zh: str = """"""
    subject: str = "咸池桃花煞：沐浴之地的情欲与破败"
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
        l1_anchor="smth_v1.0.0_咸池桃花煞_沐浴之地的情欲与破败_001_L1",
    )
    version: str = "1.0.0"
