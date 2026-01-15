"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492229
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
    semantic_id="zpzq_v1.0.0_正官之_尊__从克身到分所当尊_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 正官之尊从克身到分所当尊(SemanticEntry):
    """
    - **原文（source_text）**：
  三十一、论正官。
  官以克身，虽与七煞有别，终受彼制，何以切忌刑冲破害，尊之若是乎？岂知人生天地间，必无矫焉自尊之理，虽贵极天子，亦有天祖临之。正官...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十一、论正官。
  官以克身，虽与七煞有别，终受彼制，何以切忌刑冲破害，尊之若是乎？岂知人生天地间，必无矫焉自尊之理，虽贵极天子，亦有天祖临之。正官者分所当尊，如在国有君，在家有亲，刑冲破害，以下犯上，乌乎可乎？

  以刑冲破害为忌，则以生之护之为喜矣。存其喜而去其忌则贵，而贵之中又有高低者，何也？以财印并透者论之，两不相碍，其贵也大。如薛相公命，甲申、壬申、乙巳、戊寅，壬印戊财，以乙隔之，水与土不相碍，故为大贵。若壬戌、丁未、戊午、乙卯，杂气正官，透干会支，最为贵格，而壬财丁印，二者相合，仍以孤官无辅论，所以不上七品。

  若财印不以两用，则单用印不若单用财，以印能护官，亦能泄官，而财生官也。若化官为印而透财，则又为甚秀，大贵之格也。如金状元命，乙卯、丁亥、丁未、庚戌，此并用财印，无伤官而不杂煞，所谓去其忌而存其喜者也。

  然而遇伤在于佩印，混煞贵乎取清。如宣参国命，己卯、辛未、壬寅、辛亥，未中己官透干用清，支会水局，两辛解之，是遇伤而佩印也。李参政命，庚寅、乙酉、甲子、戊辰，甲用酉官，庚金混杂，乙以合之，合煞留官，是杂煞而取清也。

  至于官格透伤用印者，又忌见财，以财能去印，未能生官，而适以护伤故也。然亦有逢财而反大贵者，如范太傅命，丁丑、壬寅、己巳、丙寅，支具巳丑，会金伤官，丙丁解之，透壬岂非破格？却不知丙丁并透，用一而足，以丁合壬而财去，以丙制伤而官清，无情而愈有情。此正造化之妙，变幻无穷，焉得不贵？

  至若地支刑冲，会合可解，已见前篇，不必再述，而以后诸格，亦不谈及矣。

- 原注（原文注解）：
  　　本章由“正官为何可贵”入手，说明：
  - 正官虽本质上也是“克身之神”，却象征“分所当尊”的秩序与位分；
  - 因而忌刑冲破害，是在维护上下秩序，而非单纯怕克身。

  首句提出疑问：
  - 官既以克身，与七煞同属“克我”一类，为什么又要“切忌刑冲破害”，反而“尊之若是”？
  - 作者以“人生天地间，必无矫焉自尊之理”作答：
    - 人无论多贵，必有更高的“规范与约束”在上；
    - 正官所代表的，便是在国有君、在家有亲等“应当尊奉之位”。
  - 因此：
    - 刑冲破害正官，就像以下犯上，扰乱纲常，自然为大忌；
    - 相反，“生之护之”的财、印，则是对秩序的维护，故为喜。

  接下来论“贵之高低”：
  - 若财印并透而“两不相碍”，则官星得财生、得印护：
    - 如薛相公命：壬为印、戊为财，中间以乙隔开，使水土不相战；
    - 官星居中受生受护，故为“大贵”。
  - 若财印相合互损，则虽为杂气正官、高格之局，仍以“孤官无辅”论之：
    - 如壬戌、丁未、戊午、乙卯一例；
    - 财印相合，反令官失去真正的“左右辅弼”。

  再论“财印偏重”的取舍：
  - 单用印不如单用财：
    - 印既能护官，亦能泄官，终究有一“耗官”之侧面；
    - 财则纯以生官，更符合“尊官”的核心逻辑。
  - 若“化官为印而透财”：
    - 官气化入印绶以生身，财再来生官印之气；
    - 这种结构既有护身之印，又有生官之财，故为“甚秀、大贵”。

  然后讨论“遇伤佩印、杂煞取清”的情况：
  - 正官遇伤官时：
    - 佩印可以护官制伤，使“伤不坏官”；
    - 宣参国命例中，己官透干用清，水局之伤由两辛来化解。
  - 正官兼七煞时：
    - 通过“合煞留官”的方式，去其混杂，取其清纯；
    - 李参政命中，乙合庚以去煞留官，正体现“杂煞而取清”的妙用。

  最后，作者以范太傅一例，展示“似破实不破”的高阶变化：
  - 表面看：透壬财而又会伤官局，似乎“财去印而护伤”，为破格；
  - 实则：
    - 丙丁并透，仅用其一即可；
    - 以丁合壬，使“财去而不伤官印系统”；
    - 以丙来制伤，使“官星反而更清”；
    - 表面“无情”，而内部结构更有情，故反成大贵。

- 分字分词释义：
  - 正官：十神之一，以克身而有序的官星，主名位、规范与权威。
  - 七煞：偏官，以克身而无节制者，主险峻、压力与风险。
  - 刑冲破害：刑、冲、破、害等对官星的破坏性作用，总称官星受损。
  - 分所当尊：各安其位，各有其应当被尊重的角色与层级。
  - 孤官无辅：有官而无财印比劫之辅助与调剂，官势孤立。
  - 并透：同一类或相应类神同时明现于天干。
  - 佩印：以印绶护官、护身，有“佩戴印绶以示名份”之意。
  - 合煞留官：通过合化方式，使煞气被合去而官气得以保留。
  - 去其忌而存其喜：去掉不利因素，保留有利因素，是格局优化的核心原则。

- **规范化释义（primary_lang_explained）**：
  若从结构上讲，正官好比一个体系中的“正当权威”：
  - 它必须有“上位”属性：能约束日主，代表规则与秩序；
  - 但又不能乱来：一旦被刑冲破害，或被伤煞所坏，则规则失效，秩序崩解。

  本章最重要的观念有两点：
  1) 正官不是因为“克身”就可怕，而是因为它代表“上位者”：
     - 官被刑冲破害，其象就像“臣犯君、子犯父”；
     - 故“忌刑冲破害”是对秩序的维护，而非怕克身本身。
  2) 真正的好官格，一定要有“生之护之”的体系：
     - 财来生官，使官有源；
     - 印来护官、护身，使克身有节；
     - 若刑冲破害、伤官混煞，则是对秩序的破坏。

  在操作层面，可以这样理解：
  - 判断一个命局“官格贵不贵”：
    - 先看：正官是否清纯，不混七煞、不被刑冲破害；
    - 再看：是否有财印比劫等“辅弼体系”围绕官星运转；
    - 最后看：是否存在“去其忌而存其喜”的合化、制伏结构。

- 详细解说：
  - 正官格的精华，不在于“有无官星”，而在于：
    - 官是否代表一个稳定、被认可的规范系统；
    - 这个系统是否获得足够的资源（财）和正当性（印）。
  - 从社会学意义看：
    - 正官格的高低，对应着一个人如何与“制度、权威”打交道：
      - 官清而有辅 → 多见循规而能上达之人；
      - 官弱而混煞 → 易陷于权力斗争与秩序崩坏之中.

- **完整对等诠释（secondary_lang_full）**：  
  Proper Officer represents a recognised framework of law and order, something that deserves respect rather than casual violation. Even when it restrains the Day Master, it does so in an orderly, rule‑based way, very different from the raw pressure of Killing. It detests being battered by clashes, punishments and harms that amount to rebellion against the system, and thrives when supported by clear Wealth and Printing: Wealth supplies resources for the office to function, Printing grants legitimacy, credentials and backing.

  A chart is not noble simply because an Officer star is present on the surface. True nobility appears when the Officer is clean, unentangled with Killing, protected from severe冲刑, and surrounded by appropriate Wealth, Printing and Peers so that the burden of responsibility is actually bearable. Configurations such as Hurting Officer with Printing, or combinations that remove Killing while preserving Officer, all work to resolve conflicts while keeping the underlying order intact. In this sense, Officer symbolises a functioning institutional structure, and the question is always whether that structure is truly upheld and resourced, not merely whether a character labelled "Officer" happens to be written in the chart.

- **核心要点**：
  - 正官虽克身，却代表"分所当尊"的秩序与权威
  - 刑冲破害正官，等同于以下犯上，乱其纲常
  - 财印并透而两不相碍，官格大贵
  - 财印相合互损，虽格局高亦沦为"孤官无辅"
  - 单用印不若单用财，印护官亦泄官，财纯以生官
  - 化官为印而透财，既有护身之印又有生官之财，为甚秀大贵
  - 遇伤在于佩印，混煞贵乎取清
  - 合煞留官：以合化方式去煞存官
  - 去其忌而存其喜，是格局优化的核心原则

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_494]` `[trigger: 正官格]` `[role: 主干]` `[factor_trigger: zhengguan_fen_suo_dang_zun AND xingchong_pohai_yi_xia_fan_shang]` 正官者分所当尊，如在国有君，在家有亲，刑冲破害，以下犯上，乌乎可乎？ → 《子平真诠》#下卷
  - `[ns_zpzy_495]` `[trigger: 正官格 AND 财印并透]` `[role: 条件分支]` `[factor_trigger: caiyin_bingtou AND liang_bu_xiang_ai AND qi_gui_ye_da]` 以财印并透者论之，两不相碇，其贵也大。 → 《子平真诠》#下卷
  - `[ns_zpzy_496]` `[trigger: 正官格 AND 财印相合]` `[role: 条件分支]` `[factor_trigger: caiyin_xianghe AND yi_guguan_wufu_lun]` 财印二者相合，仍以孤官无辅论。 → 《子平真诠》#下卷
  - `[ns_zpzy_497]` `[trigger: 正官格 AND 单用财印]` `[role: 条件分支]` `[factor_trigger: dan_yong_yin_bu_ru_dan_yong_cai AND yin_neng_hu_guan_yi_neng_xie_guan AND cai_sheng_guan]` 单用印不若单用财，以印能护官，亦能泄官，而财生官也。 → 《子平真诠》#下卷
  - `[ns_zpzy_498]` `[trigger: 正官格 AND 化官为印]` `[role: 条件分支]` `[factor_trigger: hua_guan_wei_yin_er_tou_cai AND you_hu_yu_ye_da_gui]` 若化官为印而透财，则又为甚秀，大贵之格也。 → 《子平真诠》#下卷
  - `[ns_zpzy_499]` `[trigger: 正官格 AND 遇伤官]` `[role: 例外处理]` `[factor_trigger: yu_shang_guan_zai_pei_yin AND hun_sha_gui_qu_qing]` 遇伤在于佩印，混煞贵乎取清。 → 《子平真诠》#下卷
  - `[ns_zpzy_500]` `[trigger: 正官格 AND 杂煞]` `[role: 例外处理]` `[factor_trigger: he_sha_liu_guan AND za_sha_qu_qing]` 合煞留官，是杂煞而取清也。 → 《子平真诠》#下卷
  - `[ns_zpzy_501]` `[trigger: 变格大贵]` `[role: 例外处理]` `[factor_trigger: wu_qing_er_yu_yu_qing AND zhao_hua_zhi_miao_bian_hua_wu_qiong]` 无情而愈有情，此正造化之妙，变幻无穷，焉得不贵？ → 《子平真诠》#下卷
  - `[ns_zpzy_502]` `[trigger: 正官之贵]` `[role: 总结]` `[factor_trigger: cun_qi_xi_er_qu_ji]` 存其喜而去其忌则贵。 → 《子平真诠》#下卷
  - `[ns_zpzy_503]` `[trigger: 正官格取运]` `[role: 主干]` `[factor_trigger: qu_yun_zhi_dao_yi_ba_zi_jiu_you_yi_ba_zi_zhi_lun]` 取运之道，一八字则有一八字之论，其理甚精，其法甚活。 → 《子平真诠》#下卷
  - `[ns_zpzy_504]` `[trigger: 正官用财印]` `[role: 条件分支]` `[factor_trigger: zheng_guan_yong_cai_yin AND shen_qing_zhong_yu_zhu_shen]` 正官而用财印，身稍轻则取助身，官稍轻则助官。 → 《子平真诠》#下卷
  - `[ns_zpzy_505]` `[trigger: 官露]` `[role: 条件分支]` `[factor_trigger: guan_lu_bu_ke_feng_he AND bu_ke_za_sha AND bu_ke_zhong_guan]` 若官露而不可逢合，不可杂煞，不可重官。 → 《子平真诠》#下卷
  - `[ns_zpzy_506]` `[trigger: 正官用财]` `[role: 条件分支]` `[factor_trigger: zheng_guan_yong_cai AND yun_xi_yin_jia_sheng_di]` 正官用财，运喜印绶身旺之地，切忌食伤。 → 《子平真诠》#下卷
  - `[ns_zpzy_507]` `[trigger: 正官佩印]` `[role: 条件分支]` `[factor_trigger: zheng_guan_pei_yin AND yun_xi_cai_xiang]` 正官佩印，运喜财乡，伤食反吉。 → 《子平真诠》#下卷
  - `[ns_zpzy_508]` `[trigger: 正官带伤用印]` `[role: 条件分支]` `[factor_trigger: zheng_guan_dai_shang_yong_yin AND yun_xi_guan_wang_yin_wang]` 正官带伤食而用印制，运喜官旺印旺之乡，财运切忌。 → 《子平真诠》#下卷
  - `[ns_zpzy_509]` `[trigger: 正官带煞]` `[role: 条件分支]` `[factor_trigger: zheng_guan_dai_sha AND shang_shi_fan_wu_ai]` 正官而带煞，伤食反为不碍。 → 《子平真诠》#下卷
  - `[ns_zpzy_510]` `[trigger: 取运总则]` `[role: 总结]` `[factor_trigger: yun_zhong_mei_yu_yi_zi_ge_you_yan_jiu]` 运中每遇一字，各有研究，随时取用，不可言形。凡格皆然。 → 《子平真诠》#下卷
  - `[ns_zpzy_511]` `[trigger: 正官格取运]` `[role: 总结]` `[factor_trigger: zheng_guan_qu_yun_zhi_dao]` 正官格取运之道，强调一八字则有一八字之论。 → 《子平真诠》#下卷
  - `[ns_zpzy_512]` `[trigger: 变格大贵]` `[role: 例外处理]` `[factor_trigger: wuqing_er_yu_youqing AND zaohua_zhi_miao]` 无情而愈有情，此正造化之妙，变幻无穷，焉得不贵？ → 《子平真诠》#下卷
  - `[ns_zpzy_513]` `[trigger: 正官之贵]` `[role: 总结]` `[factor_trigger: cun_qi_xi_qu_qi_ji_ze_gui]` 存其喜而去其忌则贵。 → 《子平真诠》#下卷

<!-- FACTOR_BEGIN -->
#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 官星清浊度         | guanxing_qingzhuo                    | existing | 质量指标       | 清纯 / 杂煞 / 被刑冲                        | bazi_rule_engine | 评估正官是否可作贵格之体 |
| 关系类   | 财印配官模式       | caiyin_peiguan                    | existing | 辅弼体系       | 财印并见不相碍 / 财破印 / 印泄官           | bazi_rule_engine | 决定官格高低与稳固程度   |
| 关系类   | 官与身强弱比例     | guanshen_qiangruo_bili                    | existing | 承受关系       | 身轻官重 / 身官平衡 / 身重官轻             | bazi_rule_engine | 影响能否承受官克之压力   |
| 态势类   | 官星受伤类型       | guanxing_shoushang_leixing                    | new_candidate | 风险标记       | 伤官直克 / 刑冲破害 / 合煞留官             | bazi_rule_engine | 区分可救与难救的破格情形 |
| 边界类   | "去忌存喜"结构有无 | quji_cunxi_jiegou                    | existing | 优化开关       | 有 / 无                                    | bazi_rule_engine | 是否存在合化制伏以升级格局 |
- **功能象义**：
  - 命理上，用来界定“正官格何以为贵”：不在有无官星，而在官体是否清、辅弼是否全
  - 实务上，用于判断命主如何与制度、权威互动，是循规上达还是陷入权力斗争
- **条件结构**：
  - 必要条件：命局中有可作正官用的克身之神，且不混杂七煞与重刑冲破害
  - 增强条件：财印并透而两不相碍，比劫适度分担压力，使官能克而不至过严
  - 失效条件：官星被杂煞混合、重刑冲破害，或孤官无辅、身弱不胜官
  - 时间层次（勾选适用项）：
    - [x] 原局层（natal）：正官清浊与辅弼是否完整，主要由原局结构决定
    - [x] 大运层（luck_cycle）：大运可加强或破坏官格结构，如再添杂煞或助清官
    - [x] 流年层（annual）：流年具体呈现“升迁、受阻或失序”等官格事件
- **多层解释**：
  - 字面层：说明正官如何由“克身之神”提升为“分所当尊”的名位象
  - 象征层：对应社会中的合法权威与制度框架，强调“清、稳、有辅弼”的秩序
  - 现实层：指示命主在现实中如何经历职位、责任与评价体系的考验
  - 心理层：提醒在面对权威与规则时，既不一味抗拒，也不盲目迎合，而是学会与之合作

**L2-术语对齐（Term Glossary）**
| 术语（中文） | 术语（英文） | 简明释义 |
|---|---|---|
| 正官 | 正官 | 十神之一，以克身而有序的官星，主名位、规范与权威。 |
| 七煞 | 七煞 | 偏官，以克身而无节制者，主险峻、压力与风险。 |
| 刑冲破害 | 刑冲破害 | 刑、冲、破、害等对官星的破坏性作用，总称官星受损。 |
| 分所当尊 | 分所当尊 | 各安其位，各有其应当被尊重的角色与层级。 |
| 孤官无辅 | 孤官无辅 | 有官而无财印比劫之辅助与调剂，官势孤立。 |
| 并透 | 并透 | 同一类或相应类神同时明现于天干。 |


<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|------------|
| rel_zpzq_zhengguan_01 | depend | guanxing_qingzhuo | zhengguan_zunwei | 官星清浊度决定正官能否承担“分所当尊”的角色 | 官清而不混煞、少刑冲 | 决定 | 《子平真诠》#论正官 |
| rel_zpzq_zhengguan_02 | support | caiyin_peiguan | zhengguan_zunwei | 财印配官体系为正官提供资源与正当性 | 财印并见而不相碍 | 增强 | 《子平真诠》#论正官 |
| rel_zpzq_zhengguan_03 | refine | quji_cunxi_jiegou | guanxing_shoushang | “去忌存喜”的合化结构可化解官星受伤 | 合煞留官或化官为印透财 | 优化 | 《子平真诠》#论正官 |

**证据链层**：

| 证据ID | 证据类型 | 支持命题 | 来源片段 | 可信度 | source_ref |
|-------|---------|---------|---------|--------|------------|
| evi_zpzq_zhengguan_01 | 原文直接 | 正官象征“分所当尊”的秩序 | 正官者分所当尊，如在国有君，在家有亲 | 高 | 《子平真诠》#论正官 |
| evi_zpzq_zhengguan_02 | 原文直接 | 财印并透且不相碍则官格大贵 | 以财印并透者论之，两不相碇，其贵也大 | 高 | 《子平真诠》#论正官 |
| evi_zpzq_zhengguan_03 | 原文直接 | 合煞留官与存其喜去其忌是格局优化原则 | 合煞留官，是杂煞而取清也……存其喜而去其忌则贵 | 高 | 《子平真诠》#论正官 |

**跨体系映射层**：

| 映射ID | 本体系概念 | 目标体系 | 目标概念 | 映射性质 | 备注 |
|-------|-----------|---------|---------|---------|------|
| map_zpzq_zhengguan_01 | 正官与秩序系统 | 社会学 | 合法权威与制度信任 | 结构类比 | 清纯正官对应稳定而被承认的制度框架 |
| map_zpzq_zhengguan_02 | 去忌存喜结构 | 心理学 | 风险管理与边界设定 | 功能类比 | 通过清理破坏性因素来保存有益约束 |

<!-- L2.5_END -->

---

## 三十二．论正官取运

### 1. 正官格成后，如何借行运而显其用"""
    normalized_text_zh: str = """"""
    subject: str = "正官之“尊”：从克身到分所当尊"
    factor_refs: list = ['source_ref']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_正官之_尊__从克身到分所当尊_001_L1",
    )
    version: str = "1.0.0"
