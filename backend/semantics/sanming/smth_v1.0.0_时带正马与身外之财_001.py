"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412629
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
    semantic_id="smth_v1.0.0_时带正马与身外之财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 时带正马与身外之财(SemanticEntry):
    """
    - **原文（source_text）**：

  时带正马：如甲日带巳午时之例，无刑冲破劫，主招美妻，得外来财物，生子荣贵，财产丰厚。此非父母之财，乃身外之财，招来产业，宜俭不宜奢。

- 分字分词...
    """
    
    original_text: str = """- **原文（source_text）**：

  时带正马：如甲日带巳午时之例，无刑冲破劫，主招美妻，得外来财物，生子荣贵，财产丰厚。此非父母之财，乃身外之财，招来产业，宜俭不宜奢。

- 分字分词释义：

  - **时带正马**：时支落在日主正财所居之驿马位，例如甲日见巳、午之类。
  - **无刑冲破劫**：时支之马与财须不受刑冲、合去或比劫分夺，方可成格。
  - **招美妻，得外来财物**：时柱主晚年、主子息、主外缘，故多应在婚姻伴侣与中晚年所得之财。
  - **此非父母之财，乃身外之财**：强调此处的财更多是通过个人努力、伴侣或外缘所得，而非纯粹继承自上一代。

- **规范化释义（primary_lang_explained）**：

  时带正马，偏重于“晚年与外来”的财马之象。日主在时支上坐正财之马，且不受刑冲破劫，多主：

  - 婚姻伴侣条件较好，能带来资源或人脉；
  - 中晚年凭借事业拓展、迁居、远行等动作而获财；
  - 子女或晚辈亦有成就，带来荣光与实质助益。

  但原文也提醒“宜俭不宜奢”：因为此财多为后天所获、身外之财，若过度消费享乐，则易“来得快、去得也快”。

- 核心要点：

  - 时带正马着眼于**个人后天开拓与婚姻、子息所带来的资源**。
  - 关键条件是“无刑冲破劫”，否则马反为奔波、财反为耗散。
  - 在实际判断中，宜结合婚姻宫、子女宫与行运来综合评估。

- 详细解说：

  若把“岁带正马”看作家族层面的资源流动，那么“时带正马”更像个人层面的“身外之财”：多通过职业变化、合作伙伴、伴侣家庭、异地机缘等渠道而来。

  - 若命局财为用神，且印比能护身，则此类配置常对应“先平常、后渐丰”的人生曲线；
  - 若命局本就财多身弱，又在时柱再添一马一财，却无印比扶持，则易成“晚年奔波为财”，甚至因追逐机会而劳形伤身。

- **校勘与字词辨析（双语）**：

  - 原文以“招美妻、得外来财物、生子荣贵”一句涵盖婚姻与子息两端，本稿在白话中将其拆解为不同现实路径，便于理解。
  - “宜俭不宜奢”一语，本稿直接保留为行为建议，不延伸过多道德判断。
  - **English**:
    - Interpretation kept technical without extending into moral judgments.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_109]` `[trigger: 时带正马]` `[factor_trigger: shizhu_zhengcai AND yima_weizhi]` `[role: 主干]` 时带正马，如甲日带巳午时之例，无刑冲破劫。 → 《三命通会》卷六#时带正马
  - `[ns_smth_06_110]` `[trigger: 招美妻得外财]` `[factor_trigger: wu_xingchong AND zhao_meiqi]` `[role: 主干依赖]` 主招美妻，得外来财物，生子荣贵，财产丰厚。 → 《三命通会》卷六#时带正马
  - `[ns_smth_06_111]` `[trigger: 身外之财]` `[factor_trigger: fei_fumu_cai AND zhaolai_chanye]` `[role: 条件分支]` 此非父母之财，乃身外之财，招来产业。 → 《三命通会》卷六#时带正马
  - `[ns_smth_06_112]` `[trigger: 宜俭不宜奢]` `[factor_trigger: shenwai_cai AND yijian_buyishe]` `[role: 总结]` 宜俭不宜奢。身外之财招来不易，宜节俭持守。 → 《三命通会》卷六#时带正马"""
    normalized_text_zh: str = """"""
    subject: str = "时带正马与身外之财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_31', 'bazi_semantic', 'bazi_structure_hour_pillar_zhengcai_combo', 'bazi_semantic', 'bazi_state_degree_18', 'bazi_semantic', 'bazi_state_factor_21', 'bazi_semantic', 'bazi_condition_factor_183', 'bazi_semantic', 'bazi_condition_factor_184', 'bazi_semantic', 'source_ref', 'rel_smth_06_109', 'shidai_zhengma_presence', 'rel_smth_06_110', 'waicai_huoqu', 'rel_smth_06_111', 'xingchong_pojie_risk', 'evi_smth_06_109', 'shidai_zhengma_presence', 'rule_shidai', 'evi_smth_06_110', 'waicai_huoqu', 'rule_waicai', 'evi_smth_06_111', 'shechi_huihuo_risk', 'rule_yijian', 'map_smth_06_073', 'map_smth_06_074']
    
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
        l1_anchor="smth_v1.0.0_时带正马与身外之财_001_L1",
    )
    version: str = "1.0.0"
