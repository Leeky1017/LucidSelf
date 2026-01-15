"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492388
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
    semantic_id="zpzq_v1.0.0_伤官格在行运中的放大与节制_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 伤官格在行运中的放大与节制(SemanticEntry):
    """
    - **原文（source_text）**：
  四十二、论伤官取运.
  伤官取运，即以伤官所成之局，分而配之。伤官用财，财旺身轻，则利印比；身强财浅，则喜财运，伤官亦宜.

  伤官佩印，运行官煞...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十二、论伤官取运.
  伤官取运，即以伤官所成之局，分而配之。伤官用财，财旺身轻，则利印比；身强财浅，则喜财运，伤官亦宜.

  伤官佩印，运行官煞为宜，印运亦吉，伤食不碍，财地则凶.

  伤官而兼用财印者，其财多而带印者，运喜助印，印多而带财者，运喜助财.

  伤官而用煞印者，印运最利，伤食亦亨，杂官非吉，逢财即危.

  伤官带煞，喜印忌财，然伤重煞轻，运喜印而财亦吉。惟七根重，则运喜伤食，印绶身旺亦吉，而逢财为凶矣.

  伤官用官，运喜财印，不利食伤，若局中官露而财印两旺，则比劫伤官，未绐非吉矣.

- 原注（原文注解）：
  　本章承三十九、四十、四十一诸章之后，专从“时间维度”说明：不同形态的伤官格，在行运中应如何配合财、官、印、煞与比劫.

  1) **伤官用财之取运**：
  - “伤官用财，财旺身轻，则利印比；身强财浅，则喜财运，伤官亦宜”：
    - 若财旺而身轻 → 先行印绶、比劫之运：
      - 印比帮身承财，使“伤→财→官”的链条可负荷；
    - 若身强而财浅 → 反宜多行财运、伤官运：
      - 以扩张“伤生财”的能力.

  2) **伤官佩印之取运**：
  - “伤官佩印，运行官煞为宜，印运亦吉，伤食不碍，财地则凶”：
    - 命局已以印制伤：
      - 行官煞运可使“官来得印护”，以秩序收束伤官锋芒；
      - 行印运亦吉，可增印力，稳住结构；
      - 伤食运反不碍，因印足以制伤；
      - 财地则凶，因为财破印、党伤，使“伤官见官”的凶象被放大.

  3) **伤官兼用财印之取运**：
  - “其财多而带印者，运喜助印，印多而带财者，运喜助财”：
    - 若命局财多带印 → 行运宜助印：
      - 以印护身、护官，使财不过度泛滥；
    - 若命局印多带财 → 行运宜助财：
      - 以财引伤生官，使印不过于沉重；
    - 核心是“补轻不补重”，使财伤印三者保持中和.

  4) **伤官用煞印之取运**：
  - “伤官而用煞印，印运最利，伤食亦亨，杂官非吉，逢财即危”：
    - 以煞生印、印制伤官为主轴：
      - 印运为最利 → 强化护身与制伤之力；
      - 伤食运亦可亨 → 伤得其用，为才华成果；
      - 杂官则不吉 → 官煞混杂、夺印之专用；
      - 逢财即危 → 财破印、党煞，使体系瓦解.

  5) **伤官带煞之取运**：
  - “伤官带煞，喜印忌财，然伤重煞轻，运喜印而财亦吉。惟七根重，则运喜伤食，印绶身旺亦吉，而逢财为凶矣”：
    - 伤官与七煞并存：
      - 通则为“喜印忌财”：印护身、制伤制煞，财则党煞破印；
      - 若伤重煞轻 → 运喜印，财亦可略吉（财助煞以平衡过重之伤）；
      - 若煞根重（“七根重”） → 运喜伤食与印，比重在“以伤制煞、以印护身”；
      - 但无论何种情况，重财之运多为凶.

  6) **伤官用官之取运**：
  - “伤官用官，运喜财印，不利食伤，若局中官露而财印两旺，则比劫伤官，未绐非吉矣”：
    - 以官星为用、伤官为辅时：
      - 行财运、印运为宜 → 财生官、印护官身；
      - 不利再行重食伤运，以免“伤官见官”过度；
      - 若局中官露而财印两旺，则比劫与伤官难以破局，虽不至全凶，亦难大吉.

 - 分字分词释义：
  - 伤官取运：围绕伤官主格，选择合宜行运的原则与方法；
  - 伤官用财：以伤官生财，再由财生官的链条构成主格；
  - 伤官佩印：以印绶制伤护身，使伤官不致破格；
  - 伤官用煞印：借七煞生印、印制伤官的复合结构；

- **规范化释义（primary_lang_explained）**：
  若把四十一章看作“伤官静态结构图”，本章就是“伤官在时间轴上的调度说明书”：
  - 当伤官主要生财时 → 行运重点在“补身与补财”；
  - 当伤官主要受印制时 → 行运重点在“强化印与官煞”；
  - 当伤官与煞、印交织时 → 行运要同时考虑“风险（煞）”“制衡（印）”“输出（伤）”；
  - 当伤官用官时 → 行运要防止“伤官见官”被放大.

- **完整对等诠释（secondary_lang_full）**：  
  Luck for Hurting‑Officer charts must be read from the way output is already wired in the natal pattern. In structures where Hurting Officer is paired with Printing, good periods are those that strengthen Officer and Ink, giving talent a formal channel while avoiding Wealth that would cut away the very support that restrains excess. Where Hurting Officer uses Wealth, we prefer periods that boost both Wealth and output while keeping Officer from becoming entangled, so that criticism and creativity turn into tangible results instead of open conflict.

  In patterns that ride on Killing or abandon Officer altogether, the focus of luck is different again: some years need strong Killing and Wealth so that the sharpness can be spent in high‑risk arenas rather than attacking institutions; others need more Printing and body strength so that the native can carry both pressure and expression without collapse. What all good Hurting‑Officer luck shares is that it channels surplus output into recognised roles, projects or battlefields, instead of letting it collide head‑on with Proper Officer. Treating every Hurting‑Officer period as inherently disastrous ignores the structural救应 that can turn this star into a powerful, if dangerous, asset.

  - 伤官带煞：伤官与七煞并见，锋芒极锐，风险极高；
  - 伤官用官：以官为主、伤为辅的金水特例格局.

- 详细解说：
  - 伤官的行运问题，本质上是：
    - 如何在不同阶段“开闸”或“关闸”伤官的表达力量；
    - 何时让才华转换为财富、权力，何时控制才华避免冲突；
  - 从工程化角度：
    - 不能抽象地说“伤官喜财/喜印/喜官”，必须把“静态格局 + 行运输入”作为组合特征考虑.

- **核心要点**：
  - 伤官取运，以伤官所成之局分而配之
  - 伤官用印，运喜官印，身旺之方
  - 伤官用财，运喜财食，身旺之地
  - 伤官用煞，运喜印绶，制伤护煞

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_565]` `[trigger: 伤官格在行运中的放大]` `[role: 主干]` `[factor_trigger: shangguan_quyun AND yi_shangguan_suocheng_zhiju_fen_er_pei]` 伤官取运，以伤官所成之局分而配之 → 《子平真诠》#下卷
  - `[ns_zpzy_566]` `[trigger: 伤官格在行运中的放大]` `[role: 条件分支]` `[factor_trigger: shangguan_yongyin AND yunxi_guanyin AND shenwang_zhifang]` 伤官用印，运喜官印，身旺之方 → 《子平真诠》#下卷
  - `[ns_zpzy_567]` `[trigger: 伤官格在行运中的放大]` `[role: 条件分支]` `[factor_trigger: shangguan_yongcai AND yunxi_caishi AND shenwang_zhidi]` 伤官用财，运喜财食，身旺之地 → 《子平真诠》#下卷
  - `[ns_zpzy_568]` `[trigger: 伤官格在行运中的放大]` `[role: 条件分支]` `[factor_trigger: shangguan_yongsha AND yunxi_yinshou AND zhishang_husha]` 伤官用煞，运喜印绶，制伤护煞 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 伤官格用神类型     |        | new_candidate | 分型轴     | shang_yong_cai / shang_pei_yin / shang_cai_yin / shang_yong_sha_yin / shang_dai_sha / shang_yong_guan | 概括本章行运讨论的几类结构 |"""
    normalized_text_zh: str = """"""
    subject: str = "伤官格在行运中的放大与节制"
    factor_refs: list = ['shangguan_quyun', 'shangguan_yongcai', 'shangguan_peiyin_quyun', 'shangguan_yong_shayin_quyun', 'shangguan_daisha', 'engine_id', 'shangge_leixing', 'bazi_rule_engine', 'caishen_qingzhong', 'bazi_rule_engine', 'shangge_xiyun', 'bazi_rule_engine', 'shangge_jiyun', 'bazi_rule_engine', 'shangsha_qingzhong', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_42_01', 'caishen_qingzhong', 'rel_zpzq_42_02', 'caishen_qingzhong', 'rel_zpzq_42_03', 'shangguan_peiyin_quyun', 'rel_zpzq_42_04', 'shangguan_peiyin_quyun', 'rel_zpzq_42_05', 'shangguan_yong_shayin_quyun', 'rel_zpzq_42_06', 'shangguan_yong_shayin_quyun', 'rel_zpzq_42_07', 'shangsha_qingzhong', 'rel_zpzq_42_08', 'shangsha_qingzhong', 'evi_zpzq_42_01', 'shangge_leixing', 'rule_shangge_quyun_fenxing', 'evi_zpzq_42_02', 'caishen_qingzhong', 'rule_shangyongcai_quyun', 'evi_zpzq_42_03', 'shangguan_peiyin_quyun', 'rule_shangpeiyin_quyun', 'evi_zpzq_42_04', 'shangguan_yong_shayin_quyun', 'rule_shangyongshayin_quyun', 'evi_zpzq_42_05', 'shangsha_qingzhong', 'rule_shangdaisha_quyun', 'concept_output_regulation', 'concept_capacity_load', 'concept_control_expression']
    
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
        l1_anchor="zpzq_v1.0.0_伤官格在行运中的放大与节制_001_L1",
    )
    version: str = "1.0.0"
