"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492459
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
    semantic_id="zpzq_v1.0.0_杂格与从格的行运原则_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 杂格与从格的行运原则(SemanticEntry):
    """
    - **原文（source_text）**：
  四十八(附)、论杂格取运.
  杂格不一，大都气势偏旺，出于五行常理之外。昔人评命，泥于财官之说，四柱无财可取，则不惜遥合倒冲，牵强附会，以期合于财官...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十八(附)、论杂格取运.
  杂格不一，大都气势偏旺，出于五行常理之外。昔人评命，泥于财官之说，四柱无财可取，则不惜遥合倒冲，牵强附会，以期合于财官，未免可嗤。命理不外乎五行，气势虽为偏旺，而偏旺之中，仍有正理可取，详《滴天髓征义》.偏旺之格，取运大都须顺其气势，虽干支喜忌，须察四柱之配合，而顺势取运，大致有定.

  兹就本篇所引各造，约略言之：
  - 曲直仁寿格，气势偏旺于木，宜行水木火运，官煞运最忌，财运亦不宜；
  - 炎上格，火气偏旺，宜行土运泄火之气，水运适度为佳；
  - 稼穑格，土气偏旺，宜行金运泄土之秀，水运亦可，木火忌；
  - 从革格，金气偏旺，宜行水运化金之秀，木火忌；
  - 润下格，水气偏旺，宜行木运疏水，火运适度为佳，土运忌塞.

- 原注（原文注解）：
  　本附篇虽篇幅不长，却给出了一个总的“杂格取运原则”：
  - **一切以“顺其气势”为基本前提**：
    - 杂格、从格之所以成格，在于某一五行气势偏旺甚至极旺；
    - 取运若逆其大势，多成激烈冲突与折损；
    - 取运若顺其大势，再辅以适度的泄、制、护，方为上策.
  - 同时点出：
    - 不可为了迎合“财官之说”，强以遥合倒冲去凑财官格；
    - 真正的杂格，从始至终应围绕自己的主气势来取运，而不是被“财官名目”牵着走.

- 分字分词释义：
  - 曲直仁寿格：木一方秀气之格，主仁、主伸展；
  - 炎上格：火一方秀气之格，主明、主上升；
  - 稼穑格：土一方秀气之格，主成就、主承载；
  - 从革格：金一方秀气之格，主肃杀、主变革；
  - 润下格：水一方秀气之格，主润泽、主流动；
  - 顺势取运：在保持主气势不被摧毁的前提下，选择方向相顺、且适度泄制之运.

- **规范化释义（primary_lang_explained）**：
  若用现代语言概括本篇：
  - 杂格、从格好比“极端配置”的系统：
    - 某一资源极多，其他资源相对较少；
    - 若行运方向完全对立，就像用强制限电去压制发电站的本能输出，容易引发系统震荡；
    - 若行运方向顺其大势，再用适度泄制，就像在高压水道上加装调压阀，使之既能大流量，又不致爆裂.

  因此：
  - 曲直仁寿格 → 木强，宜水木火，忌金官、重财；
  - 炎上格 → 火盛，宜土、水调剂，忌再加木火；
  - 从革格 → 金旺，宜水，忌火木；
  - 润下格 → 水旺，宜木火适度，忌土塞；
  - 从财、从煞等从格 → 主气一方，行运以顺主气之方位为本，再视身、印、官等轻重调整细节.

- 详细解说：
  - 本附篇和四十七章合看，有两个要害：
    1) 反对“格名崇拜”与“财官崇拜”；
    2) 强调“气势偏旺仍有其内在正理”，应顺势而为，不违其性.
  - 对现代建模：
    - 杂格、从格不宜当作神秘标签；
    - 更像是“偏态样本”“极端参数区域”：
      - 需要特别的正则与调参策略，而不是简单丢弃或强行归类.

- **完整对等诠释（secondary_lang_full）**：  
  Luck for miscellaneous and from‑patterns is governed by one guiding principle: follow the dominant current rather than fighting it with conventional formulas. When Wood is overwhelmingly strong as in the Curved-Straight Benevolence pattern, suitable periods feed it with Water and Fire while avoiding heavy Metal Officer or over‑weight Wealth that would stiffen or distort it. When Fire blazes in the Blazing Upward pattern, we prefer Earth and a measured amount of Water, not more Wood‑Fire piled on top. In the Harvest-Planting pattern, strong Earth needs Metal and Water to become fruitful rather than being choked by additional Wood; in the Following-Reform pattern, powerful Metal responds best to Water with a touch of Earth, not to Wood‑Fire that tries to reverse its nature; in the Moistening Downward pattern, abundant Water calls for some Wood and Fire but dislikes being dammed by heavy Earth.

  For patterns that truly follow Wealth or follow Killing, the same idea holds: one should walk in the direction of the dominant qi, not attempt to drag the chart back toward a conventional "balanced" model that no longer applies. These extreme, biased configurations still contain an inner logic; good luck periods are those that respect and extend that logic, while bad ones are those that try to impose normal expectations and end up wrecking the structure. In modelling terms, miscellaneous patterns and following patterns are skewed samples that demand careful regularisation and tuning, not brute‑force correction against their native flow.

- **核心要点**：
  - 杂格取运，以杂格所成之局分而配之
  - 从格喜行所从之运，忌生扶日主
  - 化格喜行化神之运，忌破格之运

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_588]` `[trigger: 杂格与从格的行运原则]` `[role: 主干]` `[factor_trigger: zage_quyun AND yi_zage_suocheng_zhiju_fen_er_pei]` 杂格取运，以杂格所成之局分而配之 → 《子平真诠》#下卷
  - `[ns_zpzy_589]` `[trigger: 杂格与从格的行运原则]` `[role: 条件分支]` `[factor_trigger: congge_xi_xing_suocong_zhiyun AND ji_shengfu_rizhu]` 从格喜行所从之运，忌生扶日主 → 《子平真诠》#下卷
  - `[ns_zpzy_590]` `[trigger: 杂格与从格的行运原则]` `[role: 条件分支]` `[factor_trigger: huage_xi_xing_huashen_zhiyun AND ji_poge_zhiyun]` 化格喜行化神之运，忌破格之运 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 杂格主气类型       | zage_qishi_leixing | new_candidate | 分型轴     | qu_zhi_ren_shou / yan_shang / jia_se / cong_ge / run_xia / cong_cai / cong_sha | bazi_rule_engine | 概括本篇主要格局类型       |"""
    normalized_text_zh: str = """"""
    subject: str = "杂格与从格的行运原则"
    factor_refs: list = ['zage', 'shunshi_quyun', 'quzhi_renshou', 'yanshang_ge', 'jiase_ge', 'congge_ge', 'runxia_ge', 'engine_id', 'zage_leixing', 'bazi_rule_engine', 'zhuqi_fangxiang', 'bazi_rule_engine', 'zage_xiyun', 'bazi_rule_engine', 'zage_jiyun', 'bazi_rule_engine', 'shunshi_yuanze', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_48_01', 'shunshi_yuanze', 'rel_zpzq_48_02', 'quzhi_renshou', 'rel_zpzq_48_03', 'yanshang_ge', 'rel_zpzq_48_04', 'jiase_ge', 'rel_zpzq_48_05', 'congge_ge', 'rel_zpzq_48_06', 'runxia_ge', 'evi_zpzq_48_01', 'zage_leixing', 'rule_zage_texing', 'evi_zpzq_48_02', 'shunshi_yuanze', 'rule_shunshi_quyun_yuanze', 'evi_zpzq_48_03', 'quzhi_renshou', 'rule_quzhi_quyun', 'evi_zpzq_48_04', 'yanshang_ge', 'rule_yanshang_quyun', 'evi_zpzq_48_05', 'jiase_ge', 'rule_jiase_quyun', 'concept_extreme_configuration', 'concept_flow_direction', 'concept_regulate_excess']
    
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
        l1_anchor="zpzq_v1.0.0_杂格与从格的行运原则_001_L1",
    )
    version: str = "1.0.0"
