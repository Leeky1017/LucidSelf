"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227426
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
    semantic_id="smth_v1.0.0_五行方位与一至五之配_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行方位与一至五之配(SemanticEntry):
    """
    - **原文（source_text）**：
  一曰水，二曰火，三曰木，四曰金，五曰土者，咸有所自也。水，北方子之位也，子者阳之初，一阳数也，故水曰一。火，南方午之位也，午者阴之初，二阴数也，故火曰...
    """
    
    original_text: str = """- **原文（source_text）**：
  一曰水，二曰火，三曰木，四曰金，五曰土者，咸有所自也。水，北方子之位也，子者阳之初，一阳数也，故水曰一。火，南方午之位也，午者阴之初，二阴数也，故火曰二。木居东方，东阳也，三者奇之数，亦阳也，故木曰三。金居西方，西阴也，四者偶之数，亦阴也，故金曰四。土应西南长夏，五者奇之数，亦阳也，故土曰五。由是论之，则数以阴阳而配者也。

- 分字分词释义：
  - **一曰水……五曰土**：以一至五配水火木金土，非随意命名，而有方位与阴阳之根据。
  - **子者阳之初，一阳数也**：子为阳气初生之地，故配一阳之数。
  - **午者阴之初，二阴数也**：午为阴气初起之处，故配二阴之数。

- **规范化释义（primary_lang_explained）**：
  本段把五行与方位、阴阳之数对应起来：北方子位属水而取一，南方午位属火而取二，东方属木取三，西方属金取四，西南长夏属土取五。所谓「数以阴阳而配」，是说这些数字都是从阴阳与方位关系中自然引出，而不是随意安上的记号。

- **完整对等诠释（secondary_lang_full）**：

  This section aligns each element with a direction and a base number: north and the Zi position belong to Water and take the number one; south and the Wu position belong to Fire and take two; east belongs to Wood and takes three; west to Metal and four; the south‑west and the long late‑summer to Earth and five. The phrase "number matched to Yin and Yang" means that these assignments are drawn from the relation between polarity and direction—odd numbers attached to Yang, even numbers to Yin—rather than being arbitrary labels. In practice, it invites us to read elemental strength together with where and how it is situated in space.

- **核心要点**：
  - 五行与数字、方位的对应，根本在阴阳结构，而非孤立的记忆表；
  - 读命时看「某行之强弱」，需同时兼顾其所居方位和所应之数。

- **详细解说**：
  五行之数非随意命名：水居北方子位，子为阳之初，故配一；火居南方午位，午为阴之初，故配二；木居东方，三为奇数属阳；金居西方，四为偶数属阴；土应西南长夏，五为奇数属阳。此即「数以阴阳而配」之义。论命时，不可只看五行数量多寡，更须看其所居方位与所应之数，方能判断某行之强弱与其发用方向。

- **应用推演（操作顺序）**：
  1) 在判断命局偏向时，不仅看五行数量，还要看其所对应的方位与场域：例如水旺又偏北，则多与北方、水路、流动性职业有关；
  2) 设计规则库时，为五行增加「方位/空间」维度：将人物活动区域、居住环境、行业空间特征与五行方位绑定，使推理能落到具体地理与空间结构；
  3) 在看风水或居住环境与命局配合时，用本节方位配数作为桥梁：判断某人适宜偏向哪一方发展与居住，而不是只从命盘十神抽象推断；
  4) 在数据结构中，可为每一五行节点附上「方位+数」元信息，使后续图算法能利用这些隐含结构做聚类与路径搜索。

- **反例与边界**：
  - 只背「一水二火三木四金五土」的口诀，而完全不理解其背后是子午东西南方与阴阳结构，导致在实际推理中无法用方位解释事件；
  - 将方位机械地套用到现代城市空间，而不考虑高层建筑、虚拟空间等新场景，直接用古代「东西南北」断吉凶，容易失真；
  - 在工程实现中，将方位简化为任意标签或颜色，而不是用作与地图/地理信息系统对接的关键字段，会浪费这层结构信息；
  - 反过来，只用现实方位数据而完全忽略命局中的方位象，使命理退化成普通地理统计，也违背本节「数以阴阳而配」的精神。

- **小例（示意）**：
  - 某命局水气重而在北方有根，长期在南方火旺之地工作频繁水土不服，经调整工作地点或长期出差方向（多往北方/东方），身体与事业皆有改善，这一调整可在系统中作为「方位匹配度」优化的案例；
  - 在业务系统中，将用户的居住/工作经纬度映射到五行方位，再与其命局方位偏好对比，作为推荐迁居、出差方向的一个辅助因子，体现本节「方位与数」在现代场景下的用法。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_033]` `[trigger: 水北方子位]` `[factor_trigger: direction=north AND wuxing_numbers=1]` `[role: 主干]` 水，北方子之位也，子者阳之初，一阳数也，故水曰一。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_034]` `[trigger: 数以阴阳配]` `[factor_trigger: yinyang_number_matching=odd_yang_even_yin]` `[role: 总结]` 由是论之，则数以阴阳而配者也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_035]` `[trigger: 土应西南]` `[factor_trigger: direction=southwest AND wuxing_numbers=5]` `[role: 主干依赖]` 土应西南长夏，五者奇之数，亦阳也，故土曰五。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_725]` `[trigger: 扶身破局风险]` `[factor_trigger: fushen_poju_risk]` `[role: 条件分支]` 扶身破局有风险。 → 《三命通会》卷一
  - `[ns_smth_726]` `[trigger: 扶身助力]` `[factor_trigger: fushen_zhuli]` `[role: 条件分支]` 扶身助力主有力。 → 《三命通会》卷一
  - `[ns_smth_727]` `[trigger: 福寿倾向]` `[factor_trigger: fushou_qingxiang]` `[role: 条件分支]` 福寿倾向定寿命。 → 《三命通会》卷一
  - `[ns_smth_728]` `[trigger: 负向减少]` `[factor_trigger: fuxiang_jianshao]` `[role: 条件分支]` 负向减少主转好。 → 《三命通会》卷一
  - `[ns_smth_729]` `[trigger: 辅星单一]` `[factor_trigger: fuxing_danyi]` `[role: 条件分支]` 辅星单一主单纯。 → 《三命通会》卷一
  - `[ns_smth_730]` `[trigger: 辅星贵人有无]` `[factor_trigger: fuxing_guiren_presence]` `[role: 条件分支]` 辅星贵人有无定贵气。 → 《三命通会》卷一
  - `[ns_smth_731]` `[trigger: 辅星互动]` `[factor_trigger: fuxing_hudong]` `[role: 条件分支]` 辅星互动主多方支持。 → 《三命通会》卷一
  - `[ns_smth_732]` `[trigger: 辅星结构纯度]` `[factor_trigger: fuxing_jiegou_chundu]` `[role: 条件分支]` 辅星结构纯度高主清贵。 → 《三命通会》卷一
  - `[ns_smth_733]` `[trigger: 辅星命主对比]` `[factor_trigger: fuxing_mingzhu_duibi]` `[role: 条件分支]` 辅星命主对比定格局。 → 《三命通会》卷一
  - `[ns_smth_734]` `[trigger: 辅星日主类型]` `[factor_trigger: fuxing_rizhu_leixing]` `[role: 条件分支]` 辅星日主类型定匹配。 → 《三命通会》卷一
  - `[ns_smth_735]` `[trigger: 辅星数量]` `[factor_trigger: fuxing_shuliang]` `[role: 条件分支]` 辅星数量定贵气大小。 → 《三命通会》卷一
  - `[ns_smth_736]` `[trigger: 辅星有效性]` `[factor_trigger: fuxing_youxiaoxing]` `[role: 条件分支]` 辅星有效性定实际作用。 → 《三命通会》卷一
  - `[ns_smth_737]` `[trigger: 辅星组合类型]` `[factor_trigger: fuxing_zuhe_leixing]` `[role: 条件分支]` 辅星组合类型定格局。 → 《三命通会》卷一
  - `[ns_smth_738]` `[trigger: 夫子发展潜力]` `[factor_trigger: fuzi_fazhan_qianli]` `[role: 条件分支]` 夫子发展潜力定前景。 → 《三命通会》卷一
  - `[ns_smth_739]` `[trigger: 夫子福利分配]` `[factor_trigger: fuzi_fuli_fenpei]` `[role: 条件分支]` 夫子福利分配定和谐。 → 《三命通会》卷一
  - `[ns_smth_740]` `[trigger: 夫子福利走向]` `[factor_trigger: fuzi_fuli_zouxiang]` `[role: 条件分支]` 夫子福利走向定变化。 → 《三命通会》卷一
  - `[ns_smth_741]` `[trigger: 夫子受损]` `[factor_trigger: fuzi_shousun]` `[role: 条件分支]` 夫子受损主不顺。 → 《三命通会》卷一
  - `[ns_smth_742]` `[trigger: 夫子同归]` `[factor_trigger: fuzi_tonggui]` `[role: 条件分支]` 夫子同归主和美。 → 《三命通会》卷一
  - `[ns_smth_743]` `[trigger: 夫子相停]` `[factor_trigger: fuzi_xiangting]` `[role: 条件分支]` 夫子相停主平衡。 → 《三命通会》卷一
  - `[ns_smth_744]` `[trigger: 干虚头]` `[factor_trigger: gan_xutou]` `[role: 条件分支]` 干虚头主无力。 → 《三命通会》卷一
  - `[ns_smth_745]` `[trigger: 刚烈性情风险]` `[factor_trigger: ganglie_xingqing_risk]` `[role: 条件分支]` 刚烈性情有风险。 → 《三命通会》卷一
  - `[ns_smth_746]` `[trigger: 刚确]` `[factor_trigger: gangque]` `[role: 条件分支]` 刚确主坚定。 → 《三命通会》卷一
  - `[ns_smth_747]` `[trigger: 刚柔并济]` `[factor_trigger: gangrou_bingji]` `[role: 条件分支]` 刚柔并济主平衡。 → 《三命通会》卷一
  - `[ns_smth_748]` `[trigger: 刚旺宜衰运]` `[factor_trigger: gangwang_yishuaiyun]` `[role: 条件分支]` 刚旺宜衰运主平衡。 → 《三命通会》卷一
  - `[ns_smth_749]` `[trigger: 干克分类]` `[factor_trigger: ganke_fenlei]` `[role: 条件分支]` 干克分类定吉凶。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "五行方位与一至五之配"
    factor_refs: list = ['wuxing_numbers', 'direction', 'yinyang_number_matching', 'yang_beginning']
    
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
        l1_anchor="smth_v1.0.0_五行方位与一至五之配_001_L1",
    )
    version: str = "1.0.0"
