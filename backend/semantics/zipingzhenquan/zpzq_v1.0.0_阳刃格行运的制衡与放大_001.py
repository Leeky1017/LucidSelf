"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492415
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
    semantic_id="zpzq_v1.0.0_阳刃格行运的制衡与放大_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 阳刃格行运的制衡与放大(SemanticEntry):
    """
    - **原文（source_text）**：
  四十四、论阳刃取运.
  阳刃用官，则运喜助官，然命中官星根深，则印绶比劫之方，反为美运，但不喜伤食合官耳.

  阳刃用煞，煞不甚旺，则运喜助煞；煞...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十四、论阳刃取运.
  阳刃用官，则运喜助官，然命中官星根深，则印绶比劫之方，反为美运，但不喜伤食合官耳.

  阳刃用煞，煞不甚旺，则运喜助煞；煞若太重，则运喜身旺印绶，伤食亦不为忌.

  阳刃而官煞并出，不论去官去煞，运喜制伏，身旺亦利，财地官乡反为不吉也.

- 原注（原文注解）：
  　本章是在“四十三．论阳刃”的静态格局基础上，专门讨论：在不同类型阳刃格中，行运如何选择官、煞、印、比劫、财、伤食，才能“驾刃而不被刃所伤”。

  1) **阳刃用官之取运**：
  - “阳刃用官，则运喜助官，然命中官星根深，则印绶比劫之方，反为美运，但不喜伤食合官耳”：
    - 以官制刃为主格：
      - 行运可助官，使制刃之力更稳固；
      - 若命中官星根深，则行印运、比劫运反而是“美运”：
        - 印护官、护身；
        - 比劫帮身承官与刃；
      - 唯独忌“伤食合官”：
        - 伤食合去官气，使“制刃之神”失力.

  2) **阳刃用煞之取运**：
  - “阳刃用煞，煞不甚旺，则运喜助煞；煞若太重，则运喜身旺印绶，伤食亦不为忌”：
    - 若煞略轻而刃重：
      - 行运宜助煞，使“煞制刃”之力足够；
    - 若煞已太重：
      - 行运宜助身、助印，使日主不被煞、刃双重压制；
      - 伤食运亦不为忌，可泄身而不至完全破局.

  3) **阳刃而官煞并出之取运**：
  - “阳刃而官煞并出，不论去官去煞，运喜制伏，身旺亦利，财地官乡反为不吉也”：
    - 官煞并见且皆有制刃之意：
      - 行运宜“制伏”二者中的一部分，使结构取清；
      - 同时补强日主，使其有力负担官煞与刃；
      - 财地、官乡反为不利：
        - 财助官煞、劫财，易使局面失衡；
        - 官乡再重，恐成“官煞太重而身危”。

- 分字分词释义：
  - 阳刃用官：以正官制伏阳刃，为阳刃格中最常见的高阶用法；
  - 阳刃用煞：以七煞制刃，比正官更偏锋利，需印与身配合；
  - 助官、助煞：在大运、流年上增加官煞之力，使制刃更有效；
  - 助身、助印：以比劫、印绶增强日主根气与制度护持；
  - 制伏：通过印、伤食、财等综合结构，使官煞不过重不过轻.

- **规范化释义（primary_lang_explained）**：
  从系统视角看，阳刃取运并非“逢官逢煞必好”或“逢官逢煞必凶”，而是要看：
  - 当前系统里，阳刃、官、煞、身、印、财、伤食各自的“占比分布”；
  - 行运来的是“继续加码强项”还是“补上缺项”。

  本章给出的原则可以简化为：
  - 若“制刃之神”（官或煞）不足 → 适度助之；
  - 若“制刃之神”已过重 → 转而扶身、扶印；
  - 对于官煞并出的局 → 一定要借行运“取清”，而非再添官煞.

- 详细解说：
  - 阳刃行运的核心，是保持在“能量可控”的区间：
    - 阳刃象征强烈进取心、行动力与竞争；
    - 官、煞象征秩序与压力；
    - 印象征制度、契约与身份；
    - 财象征资源与诱因；
- **完整对等诠释（secondary_lang_full）**：  
  Luck for Yang‑Blade charts is about keeping an extremely powerful drive within a controllable band. When periods strengthen Officer or pure Killing that is already acting as "the god that restrains the Blade", they help turn raw aggression into disciplined advance: the person rushes ahead, but within clear lines of command. When periods instead over‑stimulate Blade itself or add confused, mixed powers, the same energy spills over into conflict, burnout and "charging until everything breaks".

  Good Blade luck therefore does not mean "more pressure is always better". It means years in which the controlling forces are just strong enough, muddied 官煞 are clarified, the body and Printing are solid enough to bear the strain, and Wealth and Food give the Blade constructive targets. Dangerous luck is that which piles on more pressure or more Blade without adding structure, or which strips away Printing and support so that the native has only naked force and nowhere safe to place it. From a systems view, we must always ask not only how much energy is being added, but where that energy is being channelled.

  - 若行运只是一味加压（官煞、财），而少有调节（印、身、伤），则阳刃局很容易从“冲锋陷阵”走向“自毁之路”。

- **核心要点**：
  - 阳刃取运，以阳刃所成之局分而配之
  - 阳刃用官，运喜财印，官煞之地
  - 阳刃用煞，运喜食伤，身旺之方

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_573]` `[trigger: 阳刃格行运的制衡与放]` `[role: 主干]` `[factor_trigger: yangren_quyun AND yi_yangren_suocheng_zhiju_fen_er_pei]` 阳刃取运，以阳刃所成之局分而配之 → 《子平真诠》#下卷
  - `[ns_zpzy_574]` `[trigger: 阳刃格行运的制衡与放]` `[role: 条件分支]` `[factor_trigger: yangren_yongguan AND yunxi_caiyin AND guansha_zhidi]` 阳刃用官，运喜财印，官煞之地 → 《子平真诠》#下卷
  - `[ns_zpzy_575]` `[trigger: 阳刃格行运的制衡与放]` `[role: 条件分支]` `[factor_trigger: yangren_yongsha AND yunxi_shishang AND shenwang_zhifang]` 阳刃用煞，运喜食伤，身旺之方 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 阳刃取运格局类型   |        | new_candidate | 分型轴     | ren_yong_guan / ren_yong_sha / ren_guan_sha_bing_chu                    | 概括本章三类核心结构       |"""
    normalized_text_zh: str = """"""
    subject: str = "阳刃格行运的制衡与放大"
    factor_refs: list = ['yangren_quyun', 'yangren_yongguan_quyun', 'yangren_yongsha_quyun', 'zhuguan', 'guansha_bingchu', 'engine_id', 'yangrenge_leixing', 'bazi_rule_engine', 'guanxing_genshenqian', 'bazi_rule_engine', 'shawang_chengdu', 'bazi_rule_engine', 'yangrenge_xiyun', 'bazi_rule_engine', 'yangrenge_jiyun', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_44_01', 'yangren_yongguan_quyun', 'rel_zpzq_44_02', 'guanxing_genshenqian', 'rel_zpzq_44_03', 'yangren_yongguan_quyun', 'rel_zpzq_44_04', 'shawang_chengdu', 'rel_zpzq_44_05', 'shawang_chengdu', 'rel_zpzq_44_06', 'guansha_bingchu', 'rel_zpzq_44_07', 'guansha_bingchu', 'evi_zpzq_44_01', 'rule_yangren_yongguan_quyun', 'evi_zpzq_44_02', 'shawang_chengdu', 'rule_yangren_yongsha_quyun', 'evi_zpzq_44_03', 'guansha_bingchu', 'rule_yangren_guansha_bingchu_quyun', 'concept_control_calibration', 'concept_pressure_balance', 'concept_clarity_seeking']
    
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
        l1_anchor="zpzq_v1.0.0_阳刃格行运的制衡与放大_001_L1",
    )
    version: str = "1.0.0"
