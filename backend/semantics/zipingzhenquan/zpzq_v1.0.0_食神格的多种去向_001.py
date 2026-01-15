"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492322
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
    semantic_id="zpzq_v1.0.0_食神格的多种去向_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 食神格的多种去向(SemanticEntry):
    """
    - **原文（source_text）**：
  三十七、论食神。
  食神本属泄气，以其能生正财，所以喜之。故食神生财，美格也。财要有根，不必偏正叠出，如身强食旺而财透，大贵之格。

  若丁未、癸...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十七、论食神。
  食神本属泄气，以其能生正财，所以喜之。故食神生财，美格也。财要有根，不必偏正叠出，如身强食旺而财透，大贵之格。

  若丁未、癸卯、癸亥、癸丑，梁丞相之命是也；己未、壬申、戊子、庚申，谢阁老之命是也。

  藏食露伤，主人性刚。如丁亥、癸卯、癸卯、甲寅，沈路分命是也。偏正叠出，富贵不巨。如甲午、丁卯、癸丑、丙辰，龚知县命是也。

  夏木用财，火炎土燥，贵多就武。如己未、己巳、甲寅、丙寅，黄都督之命是也。

  若不用财而就煞印，最为威权显赫。如辛卯、辛卯、癸酉、己未，常国公命是也。若无印绶而单露偏官，只要无财，亦为贵格。如戊戌、壬戌、丙子、戊戌，胡会元命是也。

  若金水食神而用煞，贵而且秀。如丁亥、壬子、辛巳、丁酉，舒尚书命是也。至于食神忌印，夏火太炎而木焦，透印不碍。如丙午、癸巳、甲子、丙寅，钱参政命是也。食神忌官，金水不忌，即金水伤官可见官之谓。

  至若单用食神，作食神有气，有财运则富，无财运则贫。

  更有印来夺食，透财以解，亦有富贵，须就其全局之势而断之。至于食神而官煞竞出，亦可成局，但不甚贵耳。

  更有食神合煞存财，最为贵格。

  至若食神透煞，本忌见财，而财先、煞后，食以间之，而财不能党煞，亦可就贵。如刘提台命，癸酉、辛酉、己卯、乙亥是也。

  其余变化，不能尽述，类而推之可也。

- 原注（原文注解）：
  　本章专论“食神格”的多种演化路径，主轴是：食神本属“泄气之神”，却因能生正财而转为可喜之用。
  - 首句点明：食神之所以喜用，在于“能生正财”，不是因为它泄气本身；
  - 但要构成美格，必须同时满足：
    - 身强 → 能承受食神泄气；
    - 食旺 → 有足够“产出”生财；
    - 财有根、有透 → 所生之财有落点。

  文中依次展开数类格局：
  - **一、身强食旺而财透之格**：
    - 食生财，财有根，日主有力，是典型的“才能转化为资源”的结构；
    - 梁丞相、谢阁老两例，即身强食旺而财透的大贵之象.
  - **二、藏食露伤与偏正叠出**：
    - “藏食露伤” → 内在有稳定产出（食），外在见锋芒（伤），主性刚；
    - 偏正食神叠出，则泄气过多而不聚，故“富贵不巨”；
  - **三、夏木用财、贵多就武**：
    - 夏令木火旺、土燥，以财（多指土）为用，多见武职、实干型人物；
  - **四、食神不用财而就煞印**：
    - 不以财为主，而借煞印体系转化食神之力；
    - 常国公、胡会元诸例，说明“无财而贵”，关键在煞印得当；
  - **五、金水食神用煞**：
    - 金水伤食本属秀气，若配合七煞，反成“贵而且秀”；
    - 同时提示：食神一般忌印、忌官，但在金水格局中，有例外与变通.
  - **六、单用食神与食神合煞存财**：
    - 单用食神，有财运则富、无财运则贫，体现对行运的高度依赖；
    - 合煞存财，则是将煞之力与食、生财体系整合，形成高级贵格.

- 分字分词释义：
  - 食神：十神之一，多主温和之才、产出、享受、子女等，属“我生之神”。
  - 泄气：日主之气外泄，用于生食、财、官等.
  - 藏食露伤：地支藏食神、天干露伤官，内敛与外刚并存.
  - 偏正叠出：正食、偏食（即伤官）多重透出，泄气过度.
  - 就煞印：舍财不用而用七煞、印绶构成煞印体系.
  - 金水食神：以金生水、水为食之格局，主思维、文采之秀.
  - 合煞存财：以合化方式约束七煞，保留财星.

- **规范化释义（primary_lang_explained）**：
  可把食神理解为“长期、温和输出”的功能：
  - 对个人而言，是持续的才能发挥、作品产出、口福享受；
  - 对结构而言，是日主之气柔性外泄.

  本章强调：
  - 若身强，则可承受食神泄气，反能借食生财、生官，成“以才致富”的路径；
  - 若身弱，则过多食神反成耗损；
  - 是否富贵，在于：食生的“财、煞、印”被接住还是流失.

- 详细解说：
  - 食神格善用时，是一种“可持续发展模式”：不断产出、逐步累积；
  - 但若只泄不收（偏正叠出而无财根），则变成“耗能、空谈才华”；
  - 与伤官相比：
    - 食神偏温和、守成；
    - 伤官偏锋利、突破；
    - 本章多次比较二者与财、煞、印的搭配，实际上是在搭建一个“才华与权力/资源如何互动”的谱系.

- **完整对等诠释（secondary_lang_full）**：  
  The Food God describes a style of output that is steady, gentle and sustainable. When well used, it is like a long, slow project that keeps producing fruit year after year: talent is expressed in concrete work, that work generates Wealth, and Wealth in turn can support Officer or Printing. But if Food only leaks气 without being received—endless talking, performing or giving with no roots in Wealth or authority—then the same configuration becomes an engine that drains the self while leaving nothing stored.

  Compared with Hurting Officer, Food is more inclined to preserve and nurture rather than to break and overturn. This chapter repeatedly compares how Food and Hurting Officer pair with Wealth, Killing and Printing, sketching a spectrum of ways in which talent can interact with power and resources. At one end are charts where Food gently feeds Wealth and Officer, building stable prosperity; at the other are patterns where output pours into conflicts or gets scattered. Whether Food God becomes a symbol of "slow, compounding growth" or of "wasted effort" depends on body strength and on whether its products are properly caught by Wealth, Killing or Printing.

- **核心要点**：
  - 食神本属泄气，而以能生财为美
  - 财厚食旺而身强，此食神之贵也
  - 食神生财而佩印，运宜身旺印绶之乡
  - 食神而用煞印，运喜印绶，而煞运不忌
  - 食神带煞，喜行食神制煞，身旺之运

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_548]` `[trigger: 食神格的多种去向]` `[role: 主干]` `[factor_trigger: shishen_benshu_xieqi AND yi_neng_shengcai_weimei]` 食神本属泄气，而以能生财为美 → 《子平真诠》#下卷
  - `[ns_zpzy_549]` `[trigger: 食神格的多种去向]` `[role: 条件分支]` `[factor_trigger: caihou_shiwang_shenqiang AND shishen_zhi_gui]` 财厚食旺而身强，此食神之贵也 → 《子平真诠》#下卷
  - `[ns_zpzy_550]` `[trigger: 食神格的多种去向]` `[role: 条件分支]` `[factor_trigger: shishen_shengcai_peiyin AND yunyi_shenwang_yinshou]` 食神生财而佩印，运宜身旺印绶之乡 → 《子平真诠》#下卷
  - `[ns_zpzy_551]` `[trigger: 食神格的多种去向]` `[role: 条件分支]` `[factor_trigger: shishen_yong_shayin AND yunxi_yinshou AND shayun_buji]` 食神而用煞印，运喜印绶，而煞运不忌 → 《子平真诠》#下卷
  - `[ns_zpzy_552]` `[trigger: 食神格的多种去向]` `[role: 条件分支]` `[factor_trigger: shishen_daisha AND xi_xing_shishen_zhisha AND shenwang_zhiyun]` 食神带煞，喜行食神制煞，身旺之运 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | 备注 |"""
    normalized_text_zh: str = """"""
    subject: str = "食神格的多种去向"
    factor_refs: list = ['shishen', 'shishen_shengcai', 'cangshi_lushang', 'pianzheng_diechu', 'jiu_shayin', 'jinshui_shishen', 'shishen_hesha_cuncai', 'engine_id', 'shishen', 'bazi_rule_engine', 'shishen_shengcai_ge', 'bazi_rule_engine', 'shishen_jiu_shayin_ge', 'bazi_rule_engine', 'jinshui_shishen_ge', 'bazi_rule_engine', 'shishen_hesha_cuncai_ge', 'bazi_rule_engine', 'cangshi_lushang', 'bazi_rule_engine', 'pianzheng_diechu', 'bazi_rule_engine', 'shishen_jiyin', 'bazi_rule_engine', 'shishen_jiguan', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_37_01', 'shishen', 'rel_zpzq_37_02', 'shenwang_chengdu', 'rel_zpzq_37_03', 'cangshi_lushang', 'rel_zpzq_37_04', 'pianzheng_diechu', 'rel_zpzq_37_05', 'jiu_shayin', 'rel_zpzq_37_06', 'jinshui_shishen_ge', 'rel_zpzq_37_07', 'shishen_jiyin', 'rel_zpzq_37_08', 'shishen_jiguan', 'evi_zpzq_37_01', 'rule_shishen_xi_shengcai', 'evi_zpzq_37_02', 'shishen_shengcai_ge', 'rule_shishen_shengcai_dagui', 'evi_zpzq_37_03', 'cangshi_lushang', 'rule_cangshi_lushang_xinggang', 'evi_zpzq_37_04', 'jiu_shayin', 'rule_shishen_jiu_shayin_weiquan', 'evi_zpzq_37_05', 'shishen_hesha_cuncai_ge', 'rule_shishen_hesha_cuncai_zuigui', 'evi_zpzq_37_06', 'shishen', 'rule_danyong_shishen_yilai_caiyun', 'concept_steady_output', 'concept_talent_conversion', 'concept_authority_path', 'concept_elegance_intellect']
    
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
        l1_anchor="zpzq_v1.0.0_食神格的多种去向_001_L1",
    )
    version: str = "1.0.0"
