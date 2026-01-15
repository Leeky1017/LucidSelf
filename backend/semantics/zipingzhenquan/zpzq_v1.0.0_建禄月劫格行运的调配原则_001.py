"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492441
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
    semantic_id="zpzq_v1.0.0_建禄月劫格行运的调配原则_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 建禄月劫格行运的调配原则(SemanticEntry):
    """
    - **原文（source_text）**：
  四十六、论建禄月劫取运.
  禄劫取运，即以禄劫所成之局，分而配之。禄劫用官，印护者喜财，怕官星之逢合，畏七煞之相乘。伤食不能为害，劫比未即为凶.

...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十六、论建禄月劫取运.
  禄劫取运，即以禄劫所成之局，分而配之。禄劫用官，印护者喜财，怕官星之逢合，畏七煞之相乘。伤食不能为害，劫比未即为凶.

  财生喜印，宜官星之植根，畏伤食之相侮，逢财愈见其功，杂煞岂能无碍？

  禄劫用财而带伤食，财食重则喜印绶，而不喜比肩；财食轻则宜助财，而不喜印比。逢煞无伤，遇官非福.

  禄劫用煞食制，食重煞轻，则运宜助煞；食轻煞重，则运喜助食.

  若用煞而带财，命中合煞存财，则伤食为宜，财运不忌，透官无虑，身旺亦亨.若命中合财存煞，而用食制，煞轻则助煞，食轻则助食则已.

  禄劫而用伤食，财运最宜，煞亦不忌，行印非吉，透官不美.若命中伤食太重，则财运固利，而印亦不忌矣.禄劫而官煞并出，不论合煞留官，存官制煞，运喜伤食，比肩亦宜，印绶未为良图，财官亦非福运.

- 原注（原文注解）：
  　本章承接“四十五．论建禄月劫”，从时间与行运的角度说明：
  - 比劫极旺的建禄月劫格，在不同用神结构下，行运应如何配合官、财、印、煞、伤食与比劫；
  - 核心仍在“把过旺的自我能量，引导到合适的出口”。

  1) **禄劫用官、有印护者**：
  - “禄劫用官，印护者喜财，怕官星之逢合，畏七煞之相乘.伤食不能为害，劫比未即为凶”：
    - 用官制劫，印为护官之神：
      - 行财运可喜 → 财生官、财养印，使官印得力；
      - 忌官星逢合 → 官被合去则失其制劫之用；
      - 畏七煞相乘 → 煞多则官力受挤，变身危局；
      - 伤食不足为害 → 因官印在位，伤食不易破局；
      - 劫比并非一概为凶，需看是否过重、是否争官.

  2) **“财生喜印”之取运**：
  - “财生喜印，宜官星之植根，畏伤食之相侮，逢财愈见其功，杂煞岂能无碍？”：
    - 财生印、印护身官之局：
      - 行官运有利于“官星植根”；
      - 伤食若来“相侮”，易冲击印与官之链条，故需谨慎；
      - 财运叠加，使“财生印”的作用更明显；
      - 杂煞则打乱官印之序，易生波折.

  3) **禄劫用财而带伤食之取运**：
  - “禄劫用财而带伤食，财食重则喜印绶，而不喜比肩；财食轻则宜助财，而不喜印比.逢煞无伤，遇官非福”：
    - 若财食已重：
      - 行印运最佳，可化解“比劫争财”的风险；
      - 忌再行比肩之运，以免劫财更甚；
    - 若财食尚轻：
      - 行财运更佳，可使“劫生财”的结构真正发挥；
      - 印比运则不宜过多，以免压制财势；
    - 煞运不必过度忌讳，官运则需谨慎：官来过多，恐与伤食相冲，引发“伤官见官”之象.

  4) **禄劫用煞食制之取运**：
  - “禄劫用煞食制，食重煞轻，则运宜助煞；食轻煞重，则运喜助食”：
    - 以煞为用、以食制煞：
      - 若食重煞轻 → 利于助煞，使食有可制之对象；
      - 若煞重食轻 → 利于助食，使“以食制煞”的机制更明晰；
    - 这条强调了“制与被制”的相对强弱，不能偏废一端.

  5) **用煞而带财、合煞存财/合财存煞之取运**：
  - “若用煞而带财，命中合煞存财，则伤食为宜，财运不忌，透官无虑，身旺亦亨.若命中合财存煞，而用食制，煞轻则助煞，食轻则助食则已”：
    - 若命局以“合煞存财”为主：
      - 行运以伤食最宜，可进一步调节煞与财之度；
      - 财运亦不必忌，反可成就存财之用；
      - 官透亦无大忧，只要整体结构未破；
    - 若命局以“合财存煞，用食制煞”为主：
      - 则应视“煞轻/煞重”“食轻/食重”而分别助煞或助食.

  6) **禄劫用伤食与官煞并出之取运**：
  - “禄劫而用伤食，财运最宜，煞亦不忌，行印非吉，透官不美.若命中伤食太重，则财运固利，而印亦不忌矣.禄劫而官煞并出，不论合煞留官，存官制煞，运喜伤食，比肩亦宜，印绶未为良图，财官亦非福运”：
    - 用伤食泄劫时：
      - 财运最宜，可使“劫生伤、伤生财”形成正向循环；
      - 煞运亦可承受，但印运反而不佳，官透亦不美；
      - 若伤食本已过重，则印运亦可略许（帮助收束），但须谨慎.
    - 官煞并出且禄劫旺时：
      - 行运宜伤食、比肩，以泄旺气、稳住结构；
      - 印、财官之运不宜过重，以免权力与资源压力叠加.

- 分字分词释义：
  - 禄劫取运：围绕建禄月劫格，选择合宜行运的原则；
  - 印护者喜财：指在官印格架构中，以财生官、财生印的局面；
  - 相侮：五行相互侮辱、反克的复杂关系；
  - 合煞存财 / 合财存煞：通过合化的方式保留财或保留煞；
  - 存官制煞：保留官星，用以制伏七煞.

- **规范化释义（primary_lang_explained）**：
  若把四十五章看作“建禄月劫的静态格局说明”，本章就是“如何在时间轴上调节比劫与其用神”：
  - 比劫旺如同系统中大量并发线程：
    - 需要官/煞来调度、协调；
    - 需要财来设定目标、印来维持规则、伤食来输出成果；
  - 行运就是不断调整这些线程的“优先级与配给”：
    - 有时加官、有时加印、有时加财、有时加伤食.

- 详细解说：
  - 建禄月劫的取运，强调“高能系统的风险管理”：
- **完整对等诠释（secondary_lang_full）**：  
  Luck for Build‑Lu and Month‑Rob charts is essentially the art of risk‑managing a high‑energy system. Periods that only add more Peers or raw power usually intensify contention and resource grabs; what is needed are periods that emphasise clear focal points and outputs. When Officer is the chosen pivot, good luck strengthens both Officer and the Wealth that feeds it, so that the many "threads" of Robbing stars work under a unified command. When Wealth and output are central, good luck encourages Food and Hurting to generate Wealth while keeping Peers from crowding in to fight over it.

  In structures that rely on Killing‑and‑Printing, suitable periods bring strong Killing and Ink so that excess strength is turned into protective, duty‑bearing roles rather than chaotic rebellion. Across all variants, the criterion is not "how much more energy is added" but "where the energy is flowing". Good periods channel the already‑abundant body strength outward—into authority, production or service—while bad periods simply pile pressure on an already overloaded self, pushing the system past its safe operating range.

    - 不能只看“再加多少能量”，而要看“能量往哪里流”；
    - 适度伤食与财运，往往有助于释放比劫之压；
    - 过重官煞与财官叠加，则可能使系统进入“超压状态”。

- **核心要点**：
  - 建禄月劫取运，以所成之局分而配之
  - 禄劫用官，运喜财印，官煞之地
  - 禄劫用财，运喜食伤，财官之地

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_579]` `[trigger: 建禄月劫格行运的调配]` `[role: 主干]` `[factor_trigger: jianlu_yuejie_quyun AND yi_suocheng_zhiju_fen_er_pei]` 建禄月劫取运，以所成之局分而配之 → 《子平真诠》#下卷
  - `[ns_zpzy_580]` `[trigger: 建禄月劫格行运的调配]` `[role: 条件分支]` `[factor_trigger: lujie_yongguan AND yunxi_caiyin AND guansha_zhidi]` 禄劫用官，运喜财印，官煞之地 → 《子平真诠》#下卷
  - `[ns_zpzy_581]` `[trigger: 建禄月劫格行运的调配]` `[role: 条件分支]` `[factor_trigger: lujie_yongcai AND yunxi_shishang AND caiguan_zhidi]` 禄劫用财，运喜食伤，财官之地 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 建禄月劫用神类型   |        | new_candidate | 分型轴     | lu_ge_yong_guan / shen_qiang_san_qi / lu_jie_yong_cai / lu_jie_yong_sha / lu_jie_yong_shang | 概括本章几类主要用法       |
| 关系类   | 比劫与财官印强弱   |        | new_candidate | 载荷与统御 | bi_jie_guo_wang / shen_qiang_bi_zhong / cai_guan_yin_qiang_bi_jie_zhong    | 判断是“劫多财少”还是“身强值三奇”等 |
| 关系类   | 化劫路径存在与否   |        | new_candidate | 变化通道  | wu_hua_jie / hua_jie_wei_cai / hua_jie_wei_sheng                          | 标记是否有化劫为财/为生的高阶变化 |
| 关系类   | 官煞清浊与取向     |        | new_candidate | 贵贱枢纽  | he_sha_liu_guan / zhi_sha_liu_guan / guan_sha_hun_za                       | 对应合煞留官、制煞留官或官煞杂乱 |
| 态势类   | 建禄月劫现实表现型 |        | new_candidate | 结果轮廓  | tuan_dui_ling_xiu_xing / nei_hao_tu_hao_xing / zi_wo_zeng_chang_xing       | 概括偏向领袖、内耗或自我成长 |
| 边界类   | 是否需转入比劫专题 |        | new_candidate | 使用边界  | ke_du_ben_zhang / ying_he_bi_jie_ti_xi_tong_pan                            | 提醒何时需并入比劫专题综合分析 |
- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_582]` `[trigger: 喜忌干支]` `[factor_trigger: xiji_zaigan_yunyi_tou AND xiji_zaizhi_yunyi_hui]` `[role: 主干]` 喜忌在干运宜透，在支运宜会。 → 《子平真诠·论喜忌干支有别》#干支
  - `[ns_zpzy_583]` `[trigger: 干支应速]` `[factor_trigger: gan_zhudong_yingsu AND zhi_zhujing_yinghuan]` `[role: 主干]` 干主动应速，支主静应缓。 → 《子平真诠·论喜忌干支有别》#快慢
  - `[ns_zpzy_584]` `[trigger: 格成格破]` `[factor_trigger: ge_cheng_ze_ji AND ge_po_ze_xiong]` `[role: 条件分支]` 格成则吉，格破则凶。 → 《子平真诠》#下卷"""
    normalized_text_zh: str = """"""
    subject: str = "建禄月劫格行运的调配原则"
    factor_refs: list = []
    
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
        l1_anchor="zpzq_v1.0.0_建禄月劫格行运的调配原则_001_L1",
    )
    version: str = "1.0.0"
