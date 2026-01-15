"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436607
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
    semantic_id="smth_v1.0.0_妇人孕生男女的古法推算_001",
    book_id="sanming",
    engine_id="bazi"
)
class 妇人孕生男女的古法推算(SemanticEntry):
    """
    - 原文（source_text）：

  定妇人孕生男女.

  诀曰：父母岁数两头安，受胎之月中心取；干、坎、艮、震为男儿，巽、离、坤、兑总属女.假父母年双为折，受胎月只为单，成坎卦，定男；父母年...
    """
    
    original_text: str = """- 原文（source_text）：

  定妇人孕生男女.

  诀曰：父母岁数两头安，受胎之月中心取；干、坎、艮、震为男儿，巽、离、坤、兑总属女.假父母年双为折，受胎月只为单，成坎卦，定男；父母年只为单，受胎月双为拆，成离卦，定女.父年上，母年下，胎月中，余准此推.又一法：以大衍之数推之.诀曰：七七四十九，问娘何月有；除却母生年，单奇双是偶，奇偶若不常，寿命不长久.假先下四十九数于算盘，乃加上母受胎月数，总得若干数.若值正月胎，是五十数，其母三十一除去，止余十九数，九则为单，单则男.若单生女，双生男，主夭折.

- 分字分词释义：

  - **父母岁数两头安，受胎之月中心取**：以父母年龄为上下两端、受胎月份为中间，构成一组卦象的三要素.
  - **干坎艮震 / 巽离坤兑**：以八卦方位区分男卦与女卦，用于推测胎儿性别.
  - **大衍之数四十九**：出自《易经》蓍草占筮之法，以 7×7 的数目为推算基础.
  - **单奇双偶**：以奇偶判断男女，并附带对母亲寿命的说法，带有浓厚宿命色彩.

- **规范化释义（primary_lang_explained）**：

  本节收录的是两种古法，用来推算妇人怀孕所生胎儿的性别，皆以《易经》卦象与奇偶之数为依据：

  - 第一法：用父年、母年与受胎月构成卦象，落在“干坎艮震”则判为男，落在“巽离坤兑”则判为女；
  - 第二法：以“大衍之数四十九”为基数，加上受胎月份，经过简单加减之后，以奇偶来推断男女，甚至附会母亲寿命的长短.

  这些方法体现了古人将生育视为“天命”与“卦象”相连的观念，但从现代医学角度看，并无科学依据.

- **完整对等诠释（secondary_lang_full）**：

  This section records two classical methods for guessing the sex of an unborn child, both built on the symbolic language of the Yijing. One takes the ages of the parents and the month of conception as three lines of a trigram and then divides the eight trigrams into a "male" group and a "female" group. The other starts from the Great Expansion number forty‑nine, adds the conception month and subtracts the mother's age, and then uses the odd or even remainder to judge boy or girl, even extending the logic to comments about the mother's lifespan.

  Read today, these formulas are best understood as expressions of imagistic–numerical thinking and of cultural expectations around sons and daughters, not as tools for medical prediction. They show how earlier generations tried to make the unknown more graspable by tying it to number, omen and fate. For a contemporary reader, they can be appreciated as cultural texts, while real decisions about pregnancy and childbirth are grounded in modern medicine, ethics and respect for all genders.

- 核心要点：

  - 本节主要是传统卜筮文化在生育问题上的应用示例，而非可验证的预测方法；
  - 通过父母年龄、受胎月份与卦象奇偶来推断胎儿性别，是象数思维的典型运用；
  - 与其照单全收，不如将其视为古代生育观念与性别文化的文本材料.

- 详细解说：

  1. **象数思维的特点**  
     - 不追求生理机制，而重在“数”“卦”“阴阳”之间寻找对应关系；  
     - 在农业社会中，为难以掌控的生育结果提供一种“可理解的解释框架”。

  2. **性别与价值判断**  
     - 古代社会往往将男丁与家族延续绑定，这类预测法也常被用来满足对“生男生女”的期待；  
     - 现代阅读时需要意识到其中可能隐含的性别偏见，避免以此强化对性别的价值差别。

  3. **现代立场下的使用边界**  
     - 胎儿性别由生物学机制决定，这些占法仅具文化与象征意义；  
     - 若要实际处理孕期与生育问题，应以现代医学与伦理为依据，不宜以古书断人生育与亲子关系。

- 校勘与字词辨析：

  - 文中“单生女、双生男，主夭折”等说法，带有浓厚宿命与恐吓意味，本稿在白话与解说中不予承接，只视为古代观念的记录。
  - “大衍之数四十九”“干坎艮震”等术语，统一按《易经》象数体系理解，不再展开技术细节。
  - **English**：
    - Relational understanding; technical details not expanded.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_081]` `[trigger: 孕生男女]` `[factor_trigger: furen_yunsheng_nannv]` `[role: 主干]` 定妇人孕生男女。 → 《三命通会》卷七#妇人孕生
  - `[ns_smth_07_082]` `[trigger: 三爻构卦]` `[factor_trigger: fumu_suishu AND shoutai_yue]` `[role: 主干依赖]` 父母岁数两头安，受胎之月中心取。 → 《三命通会》卷七#妇人孕生
  - `[ns_smth_07_083]` `[trigger: 八卦分性]` `[factor_trigger: gan_kan_gen_zhen_nan OR xun_li_kun_dui_nv]` `[role: 条件分支]` 干、坎、艮、震为男儿，巽、离、坤、兑总属女。 → 《三命通会》卷七#妇人孕生
  - `[ns_smth_07_084]` `[trigger: 大衍奇偶]` `[factor_trigger: dayan_zhishu_sishijiu]` `[role: 总结]` 七七四十九，问娘何月有；除却母生年，单奇双是偶。 → 《三命通会》卷七#妇人孕生
  - `[ns_smth_07_jiaogan]` `[trigger: 交感] [factor_trigger: jiaogan]` `[role: 命理]` 交感者，阴阳交感。 → `《三命通会·卷七》#论妇人`
  - `[ns_smth_07_qise]` `[trigger: 气色] [factor_trigger: qise]` `[role: 命理]` 气色者，面部气色。 → `《三命通会·卷七》#论妇人`
  - `[ns_smth_07_wuchang]` `[trigger: 五常] [factor_trigger: wuchang]` `[role: 命理]` 五常者，仁义礼智信。 → `《三命通会·卷七》#论妇人`
  - `[ns_smth_07_xingqing]` `[trigger: 性情] [factor_trigger: xingqing]` `[role: 命理]` 性情者，性格情志。 → `《三命通会·卷七》#论妇人`"""
    normalized_text_zh: str = """"""
    subject: str = "妇人孕生男女的古法推算"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_state_strength_12', 'bazi_semantic', 'bazi_state_degree_43', 'bazi_semantic', 'bazi_state_factor_360', 'bazi_semantic', 'bazi_strength', 'bazi_semantic', 'source_ref', 'rel_smth_07_058', 'xingbie_qidai', 'rel_smth_07_059', 'xiandai_yixue', 'rel_smth_07_060', 'xingbie_pingdeng', 'evi_smth_07_058', 'xingbie_qidai', 'rule_guaxiang', 'evi_smth_07_059', 'gufa_yilai', 'rule_xiangshuu', 'evi_smth_07_060', 'xingbie_pingdeng', 'rule_jiou', 'map_smth_07_039', 'map_smth_07_040']
    
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
        l1_anchor="smth_v1.0.0_妇人孕生男女的古法推算_001_L1",
    )
    version: str = "1.0.0"
