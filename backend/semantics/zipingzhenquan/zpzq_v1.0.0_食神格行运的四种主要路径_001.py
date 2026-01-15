"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492336
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
    semantic_id="zpzq_v1.0.0_食神格行运的四种主要路径_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 食神格行运的四种主要路径(SemanticEntry):
    """
    - **原文（source_text）**：
  三十八、论食神取运.
  食神取运，即以食神所成之局，分而配之.食神生财，财重食轻，则行财食；财食重则喜帮身.官煞之方，俱为不美.

  食用煞印，运...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十八、论食神取运.
  食神取运，即以食神所成之局，分而配之.食神生财，财重食轻，则行财食；财食重则喜帮身.官煞之方，俱为不美.

  食用煞印，运喜印旺，切忌财乡.身旺，食伤亦为福运，行官行煞，亦为吉也.

  食伤带煞，喜行印绶，身旺，食伤亦为美运，财则最忌.若食太重而煞轻，印运最利，逢财反吉矣.

  食神太旺而带印，运最利财，食伤亦吉，印则最忌，官煞皆不吉也.

  若食神带印，透财以解，运喜财旺，食伤亦吉，印与官煞皆忌也.

- 原注（原文注解）：
  　本章是“三十七．论食神”的行运篇，从时间维度说明：不同形态的食神格，在行运中如何取舍财、官、煞、印.
  - 开首总则：“食神取运，即以食神所成之局，分而配之” ：
    - 先判断命局中食神是“生财型、煞印型、带煞型、带印型”等；
    - 再按类型选择对应行运，而非“一见食神就喜财运”。

  关于“食神生财”之取运：
  - “财重食轻，则行财食；财食重则喜帮身” ：
    - 若财已重而食略轻 → 仍可行财、食之运，以放大“食生财”的效应；
    - 若财、食两者皆重 → 则先行比劫、印绶之运，以帮身承受泄气与财压；
    - 官煞之方总体不佳：
      - 易引发“食伤见官”或“食制煞度失衡”的问题.

  关于“食用煞印”之取运：
  - “运喜印旺，切忌财乡.身旺，食伤亦为福运，行官行煞，亦为吉也” ：
    - 以煞印体系为主轴，印为药、煞为病；
    - 行印旺之运，印得其力，能护身护食；
    - 此时财运反而破印、党煞，易致失衡；
    - 若身旺，则食伤运、官煞运皆可成“负荷高但能驾驭”的局面.

  关于“食伤带煞”之取运：
  - “喜行印绶，身旺，食伤亦为美运，财则最忌.若食太重而煞轻，印运最利，逢财反吉矣” ：
    - 食伤本泄身，煞又克身，整体偏向“锋利型才华”；
    - 行印绶之运，可一面帮身，一面制煞，使锋芒有节；
    - 若食太重、煞相对轻，则印运尤为关键；
    - 此种结构下，小量财运可被印驾驭而反成调剂，故曰“逢财反吉”。

  关于“食神太旺而带印”的取运：
  - “运最利财，食伤亦吉，印则最忌，官煞皆不吉也” ：
    - 食旺且带印，若再行印运，则印过于笃实，易成滞钝；
    - 此时行财运，反能使“食生财”闭环成形；
    - 官煞运则多生冲突，故不宜.

  关于“食神带印，透财以解”的取运：
  - “运喜财旺，食伤亦吉，印与官煞皆忌也” ：
    - 命局中印已对食有夺气之象，须借财来“解印”；
    - 行财旺之运，有助于平衡“印夺食”之偏；
    - 此时再行印运、官煞运，则印愈重、官煞更为激烈，皆不相宜.

- 分字分词释义：
  - 食神取运：围绕食神主格，选择合宜行运的原则与方法.
  - 食用煞印：以七煞、生印、印护身为主轴，同时食神参与体系.
  - 食伤带煞：食神、伤官与七煞同时参与结构，锋锐而有险.
  - 食神太旺而带印：食神力量极大，并与印绶相连的局面.
  - 透财以解：以透出之财调节印、食、煞之间的紧张关系.

- **规范化释义（primary_lang_explained）**：
  本章从“动态调参”的视角看食神格：
  - 命局是初始结构；
  - 行运是每一阶段的参数调整；
  - 食神格的好坏，不在静态一刻，而在“多年综合效果”。

 - **完整对等诠释（secondary_lang_full）**：  
  Luck for Food‑God charts is evaluated over long spans of time rather than by single striking years. Each period changes how easily the native can convert steady output into Wealth, authority or recognition. Some periods invite more Food and Wealth, encouraging creative work and earning, but may exhaust the body if there is no Printing or Peers to share the load. Others emphasise Printing and Killing, turning Food’s products into credentials, responsibilities or high‑pressure roles; still others over‑stimulate Wealth and competition, causing the fruits of Food to be grabbed away.

  From the "dynamic parameter" viewpoint, the natal chart sets the base configuration, while luck continuously adjusts the strength of Food, body, Wealth, Printing and Killing. Good Food periods are those in which output has somewhere meaningful to go: it feeds rooted Wealth, tempers strong Killing through constructive roles, or enriches a Printing system that supports the self. Periods that simply increase output without channels—too much Food with no Wealth roots, or Food repeatedly colliding with官煞—tend to leave the native tired, with much done but little accumulated. The true quality of a Food‑God pattern is therefore the many‑year composite effect of these adjustments, not any isolated moment.

  对比几类典型：
  - **食生财型**：
    - 行财、食运 → 能让才华与财富双增；
    - 但若财、食过重而不帮身，则晚年易虚疲；
  - **食用煞印型**：
    - 行印运 → 化煞护身，食伤运亦可；
    - 忌财运破印党煞；
  - **食伤带煞型**：
    - 行印绶运 → 为高压环境下的自我保护；
    - 财运多成导火索；
  - **食神带印、透财解印型**：
    - 关键在于找到“财、食、印”的平衡点，行财运往往是解局关键.

- 详细解说：
  - 食神格行运的核心思想是“让泄气有去处”：
    - 要么生财、要么化煞、要么转为印；
    - 若泄而无收，则终至枯竭；
  - 本章提醒我们：
    - 同一“财运”或“印运”，在不同食神结构中，作用完全不同；
    - 工程化时，应把“食神结构 + 行运要素”作为联合特征来建模，而非单看某一五行.

- **核心要点**：
  - 食神生财，身强食旺，财运最宜
  - 食神制煞，运喜身旺，食神之地
  - 食神用印，运喜官印，身旺之方
  - 弃食就煞，运宜身旺，煞印相生

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_553]` `[trigger: 食神格行运的四种主要]` `[role: 主干]` `[factor_trigger: shishen_sheng_cai AND shen_qiang_shi_wang AND cai_yun_zui_yi]` 食神生财，身强食旺，财运最宜 → 《子平真诠》#下卷
  - `[ns_zpzy_554]` `[trigger: 食神格行运的四种主要]` `[role: 条件分支]` `[factor_trigger: shishen_zhi_sha AND yun_xi_shen_wang AND shishen_zhi_di]` 食神制煞，运喜身旺，食神之地 → 《子平真诠》#下卷
  - `[ns_zpzy_555]` `[trigger: 食神格行运的四种主要]` `[role: 条件分支]` `[factor_trigger: shishen_yong_yin AND yun_xi_guan_yin AND shen_wang_zhi_fang]` 食神用印，运喜官印，身旺之方 → 《子平真诠》#下卷
  - `[ns_zpzy_556]` `[trigger: 食神格行运的四种主要]` `[role: 条件分支]` `[factor_trigger: qi_shi_jiu_sha AND yun_xi_shen_wang AND sha_yin_xiang_sheng]` 弃食就煞，运宜身旺，煞印相生 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 食神取运类型     |        | new_candidate | 分型轴     | shi_sheng_cai_xing / shi_yong_sha_yin_xing / shi_shang_dai_sha_xing / shi_tai_wang_dai_yin_xing / shi_dai_yin_tou_cai_jie_yin_xing | 概括本章五类取运情境       |
| 关系类   | 身食财强弱格局   |        | new_candidate | 载荷与资源 | shen_qiang_cai_qian / shen_qiang_cai_qian_shi_zhong / shen_qing_cai_zhong_shi_qian | 对应“财重食轻”“财食重身轻”等组合 |"""
    normalized_text_zh: str = """"""
    subject: str = "食神格行运的四种主要路径"
    factor_refs: list = ['shishen_quyun', 'shiyong_shayin', 'shishang_daisha', 'shishen_taiwang_daiyin', 'toucai_yijie', 'engine_id', 'shige_leixing', 'bazi_rule_engine', 'caishi_qingzhong_shi', 'bazi_rule_engine', 'shige_xiyun', 'bazi_rule_engine', 'shige_jiyun', 'bazi_rule_engine', 'yin_duoshi', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_38_01', 'caishi_qingzhong_shi', 'rel_zpzq_38_02', 'caishi_qingzhong_shi', 'rel_zpzq_38_03', 'shiyong_shayin', 'rel_zpzq_38_04', 'shiyong_shayin', 'rel_zpzq_38_05', 'shishang_daisha', 'rel_zpzq_38_06', 'shishen_taiwang_daiyin', 'rel_zpzq_38_07', 'shishen_taiwang_daiyin', 'rel_zpzq_38_08', 'toucai_yijie', 'evi_zpzq_38_01', 'shige_leixing', 'rule_shige_quyun_fenxing', 'evi_zpzq_38_02', 'caishi_qingzhong_shi', 'rule_shisheng_cai_quyun', 'evi_zpzq_38_03', 'rule_shiyong_shayin_quyun', 'evi_zpzq_38_04', 'shishang_daisha', 'rule_shishang_daisha_quyun', 'evi_zpzq_38_05', 'shishen_taiwang_daiyin', 'rule_shitaiwang_daiyin_quyun', 'concept_output_channel', 'concept_load_balance', 'concept_conflict_resolution']
    
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
        l1_anchor="zpzq_v1.0.0_食神格行运的四种主要路径_001_L1",
    )
    version: str = "1.0.0"
