"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227473
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
    semantic_id="smth_v1.0.0_金主西方与禁收之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 金主西方与禁收之象(SemanticEntry):
    """
    - **原文（source_text）**：
  金主于西，应秋。金之为言禁也，阴气始禁止万物而收敛，披沙拣金，土所生也。生于土而别于土，乃自然之形也。

- 分字分词释义：
  - **禁**：禁止...
    """
    
    original_text: str = """- **原文（source_text）**：
  金主于西，应秋。金之为言禁也，阴气始禁止万物而收敛，披沙拣金，土所生也。生于土而别于土，乃自然之形也。

- 分字分词释义：
  - **禁**：禁止、收束之意，象征收敛、裁断、节制。
  - **生于土而别于土**：金从土中出，却有独立于土的坚刚形质。

- **规范化释义（primary_lang_explained）**：
  金属西方，对应秋季。「禁」表阴气开始收束万物，令其停息与收成。金自土中生出，却与土的质地不同，成为可裁可断的坚硬之物，这是金的自然形态。

- **完整对等诠释（secondary_lang_full）**：

  Metal rules the West and corresponds to autumn. The key idea in "jin" here is restraint and prohibition: as Yin Qi gathers, it curbs and closes down growth so that things can be harvested and brought to completion. Metal is born from Earth—sifted out of sand and rock—yet has a distinct, hard, cutting quality. In charts, Metal signifies contraction, judgment, rules, decisions and the power to sever. Well‑formed Metal has been both produced by Earth and tempered by Fire; without Earth it lacks a proper base, and without Fire it is either too crude or too brittle. Overly strong, untempered Metal becomes harsh and violent; too little Metal becomes softness that cannot uphold necessary boundaries.

- **核心要点**：
  - 命局之金，多主收敛、裁决、刚毅、决断，也可表刑伐斩断；
  - 金须有土生、有火炼，过刚无制则为暴戾，太弱无根则为柔金。

- **详细解说**：
  本节阐述金的西方属性与禁收机能。金主西方应秋，其义为「禁」——收敛、裁断与定规。金自土中生出，却与土的质地不同，成为可裁可断的坚硬之物。论命时，金旺而有土生、有火炼，则为秩序与公义之器；过刚无制则为暴戾，太弱无根则为柔金。在职业与事件分析中，金主「规则与收成」，对应决策、法务、风控、审核、评审等环节。

- **应用推演（操作顺序）**：
  1) 在人格与职业分析中，将金视作「规则与裁剪」的力量：适合承担决策、法务、风控、审核等角色，但需视其强弱与配伍来判断是「守正之金」还是「刻薄之金」；
  2) 在命局运行中，观金行何时：秋令与土厚之时行金，多主收成与定型；若在春木旺、水泛滥而土虚之时行金，则多为强硬介入带来的阵痛或割裂；
  3) 在系统建模中，为与规则、合规、边界控制相关的逻辑标注「金象」，使它们在解释层面能与这一节的象意对接；
  4) 调整策略时，以「金需土生火炼」为纲：在现实决策中，为刚性制度配以适当的文化与奖惩设计，以免变为冷酷之金。

- **反例与边界**：
  - 见金重便断为「暴戾、刑伤」，忽视若有适当土生与火炼，金也可成为秩序与公义之器；
  - 将「缺金」简单解释为「缺义气、缺良心」，过度道德化象意，而不看具体局中金的功能位；
  - 在工程实现中，不加区分地把所有约束和条件判断都归入金，使解释层面失去细度；
  - 反过来，只关注软性文化而完全不设硬性规则，会使系统与现实都缺乏必要的金之刃。

- **小例（示意）**：
  - 某命局金旺而有土生、火炼，适合在司法、审计、风控岗位上用其断事之能；系统可在职业推荐中将这类高金权重映射到规则型职位；
  - 在团队命盘分析中，若整体金弱而木火偏盛，则建议通过流程制度与检查点来「补金」，在项目管理系统中体现为增加必要的审批和复盘环节。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_047]` `[trigger: 金主西方]` `[factor_trigger: direction=west AND wuxing=metal]` `[role: 主干]` 金主于西，应秋。金之为言禁也，阴气始禁止万物而收敛。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_048]` `[trigger: 土生金]` `[factor_trigger: wuxing_shengke=earth_generates_metal]` `[role: 主干依赖]` 披沙拣金，土所生也。生于土而别于土，乃自然之形也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_850]` `[trigger: 甲庚辛金]` `[factor_trigger: jiangengxin_jin]` `[role: 条件分支]` 甲庚辛金主金气。 → 《三命通会》卷一
  - `[ns_smth_851]` `[trigger: 建官风险]` `[factor_trigger: jianguan_risk]` `[role: 条件分支]` 建官有风险。 → 《三命通会》卷一
  - `[ns_smth_852]` `[trigger: 建禄格有无]` `[factor_trigger: jianlu_ge_presence]` `[role: 条件分支]` 建禄格有无定格局。 → 《三命通会》卷一
  - `[ns_smth_853]` `[trigger: 建禄日月类型]` `[factor_trigger: jianlu_riyue_leixing]` `[role: 条件分支]` 建禄日月类型定位置。 → 《三命通会》卷一
  - `[ns_smth_854]` `[trigger: 交印入局]` `[factor_trigger: jiaoyin_rujiem]` `[role: 条件分支]` 交印入局主有力。 → 《三命通会》卷一
  - `[ns_smth_855]` `[trigger: 交运延续]` `[factor_trigger: jiaoyun_yanxu]` `[role: 条件分支]` 交运延续主持续。 → 《三命通会》卷一
  - `[ns_smth_856]` `[trigger: 甲色格有无]` `[factor_trigger: jiase_ge_presence]` `[role: 条件分支]` 甲色格有无定格局。 → 《三命通会》卷一
  - `[ns_smth_857]` `[trigger: 夹杀心商风险]` `[factor_trigger: jiasha_xinshang_risk]` `[role: 条件分支]` 夹杀心商有风险。 → 《三命通会》卷一
  - `[ns_smth_858]` `[trigger: 家庭压力]` `[factor_trigger: jiating_yali]` `[role: 条件分支]` 家庭压力主不顺。 → 《三命通会》卷一
  - `[ns_smth_859]` `[trigger: 家族连结]` `[factor_trigger: jiazu_lianjie]` `[role: 条件分支]` 家族连结主有缘。 → 《三命通会》卷一
  - `[ns_smth_860]` `[trigger: 羁绊贪合风险]` `[factor_trigger: jiban_tanhe_risk]` `[role: 条件分支]` 羁绊贪合有风险。 → 《三命通会》卷一
  - `[ns_smth_861]` `[trigger: 截马元]` `[factor_trigger: jie_mayuan]` `[role: 条件分支]` 截马元主有力。 → 《三命通会》卷一
  - `[ns_smth_862]` `[trigger: 劫财天时风险]` `[factor_trigger: jiecai_tianshi_risk]` `[role: 条件分支]` 劫财天时有风险。 → 《三命通会》卷一
  - `[ns_smth_863]` `[trigger: 劫财同宫]` `[factor_trigger: jiecai_tonggong]` `[role: 条件分支]` 劫财同宫主竞争。 → 《三命通会》卷一
  - `[ns_smth_864]` `[trigger: 结构清浊]` `[factor_trigger: jiegou_qingzhuo]` `[role: 条件分支]` 结构清浊定格局。 → 《三命通会》卷一
  - `[ns_smth_865]` `[trigger: 结构中和]` `[factor_trigger: jiegou_zhonghe]` `[role: 条件分支]` 结构中和主平衡。 → 《三命通会》卷一
  - `[ns_smth_866]` `[trigger: 解释起源]` `[factor_trigger: jieshi_qiyuan]` `[role: 条件分支]` 解释起源主根源。 → 《三命通会》卷一
  - `[ns_smth_867]` `[trigger: 稽贵铭造]` `[factor_trigger: jigui_mingzao]` `[role: 条件分支]` 稽贵铭造主有贵。 → 《三命通会》卷一
  - `[ns_smth_868]` `[trigger: 井栏叉格]` `[factor_trigger: jinglancha_ge]` `[role: 条件分支]` 井栏叉格主格局。 → 《三命通会》卷一
  - `[ns_smth_869]` `[trigger: 金寒水冷]` `[factor_trigger: jinhan_shuileng]` `[role: 条件分支]` 金寒水冷主不利。 → 《三命通会》卷一
  - `[ns_smth_870]` `[trigger: 金火持争]` `[factor_trigger: jinhua_chizheng]` `[role: 条件分支]` 金火持争主相战。 → 《三命通会》卷一
  - `[ns_smth_871]` `[trigger: 金火配置]` `[factor_trigger: jinhuo_peizhi]` `[role: 条件分支]` 金火配置定格局。 → 《三命通会》卷一
  - `[ns_smth_872]` `[trigger: 金火偏废风险]` `[factor_trigger: jinhuo_pianfei_risk]` `[role: 条件分支]` 金火偏废有风险。 → 《三命通会》卷一
  - `[ns_smth_873]` `[trigger: 金火平衡评分]` `[factor_trigger: jinhuo_pingheng_score]` `[role: 条件分支]` 金火平衡评分定强度。 → 《三命通会》卷一
  - `[ns_smth_874]` `[trigger: 金火数量配置]` `[factor_trigger: jinhuo_shuliang_config]` `[role: 条件分支]` 金火数量配置定比例。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "金主西方与禁收之象"
    factor_refs: list = ['metal', 'restriction', 'sifting_essence', 'born_from_earth_distinct']
    
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
        l1_anchor="smth_v1.0.0_金主西方与禁收之象_001_L1",
    )
    version: str = "1.0.0"
