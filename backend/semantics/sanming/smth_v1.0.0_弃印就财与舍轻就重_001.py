"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412743
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
    semantic_id="smth_v1.0.0_弃印就财与舍轻就重_001",
    book_id="sanming",
    engine_id="bazi"
)
class 弃印就财与舍轻就重(SemanticEntry):
    """
    - **原文（source_text）**：

  弃印就财：《经》云：弃印就财明偏正，印绶忌财，此理甚明。正印居月令者，决不可见财。若居年时，月令见财，只用财格，喜印生身，敌财为福。若偏印，月令年时...
    """
    
    original_text: str = """- **原文（source_text）**：

  弃印就财：《经》云：弃印就财明偏正，印绶忌财，此理甚明。正印居月令者，决不可见财。若居年时，月令见财，只用财格，喜印生身，敌财为福。若偏印，月令年时见财无妨，为弃印就财，舍轻用重。如壬生申月，丙生寅月，坐长生之地，年时得财，即身旺喜见财地，如此造化，必主弃祖基而自创别业立身。

- 分字分词释义：

  - **弃印就财**：放弃依赖印绶（家世、资格）而转向以财星（现实利益）为主的格局。
  - **正印居月令者，决不可见财**：正印若在月令得权，再见财星则破印，格局易失。
  - **偏印月令年时见财无妨**：偏印较灵活，可在一定条件下“弃印就财”。

- **规范化释义（primary_lang_explained）**：

  弃印就财，更多是对**人生路径选择**的一种描述：

  - 有的人原本具备良好家世或学历背景（印绶），但其命局与行运更适合在市场、经商或实业中发展，于是“舍弃”原有路径，转而依靠财星所代表的现实能力；
  - 若处理得当，反而更合本命之用，成为“舍轻就重”的明智选择。

- 核心要点：

  - 关键在于判断：印是否真能为用？财是否更适合本命？
  - 正印当令不宜轻弃；偏印居边位时，则有更大腾挪空间。

- 详细解说：

  在现代社会，此类配置常见于：

  - 家族有体制路径、本人却选择创业或市场化职业；
  - 原本有专业资格，却在实践中发现自己更适合经营与管理，而非纯学术或官场。

- **校勘与字词辨析（双语）**：

  - “弃祖基而自创别业”一语，本稿理解为事业路径的转向，而非简单的断绝家族关系。
  - **English**：
    - Not simply breaking family ties; nuanced interpretation provided.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_153]` `[trigger: 弃印就财]` `[factor_trigger: qiyin_jiucai AND sheqing_jiuzhong]` `[role: 主干]` 弃印就财明偏正，印纶忌财，此理甚明。 → 《三命通会》卷六#弃印就财
  - `[ns_smth_06_154]` `[trigger: 正印月令]` `[factor_trigger: zhengyin_yueling AND juebukejiancai]` `[role: 主干依赖]` 正印居月令者，决不可见财。 → 《三命通会》卷六#弃印就财
  - `[ns_smth_06_155]` `[trigger: 舍轻用重]` `[factor_trigger: pianyin_jiancai AND yongcai_ge]` `[role: 条件分支]` 若偏印，月令年时见财无妨，为弃印就财，舍轻用重。 → 《三命通会》卷六#弃印就财
  - `[ns_smth_06_156]` `[trigger: 自创别业]` `[factor_trigger: qizu_ji AND zichuang_bieye]` `[role: 总结]` 如此造化，必主弃祖基而自创别业立身。 → 《三命通会》卷六#弃印就财"""
    normalized_text_zh: str = """"""
    subject: str = "弃印就财与舍轻就重"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_40', 'bazi_semantic', 'bazi_structure_config_5', 'bazi_semantic', 'bazi_state_degree_28', 'bazi_semantic', 'bazi_state_factor_30', 'bazi_semantic', 'bazi_condition_zhengyin_month_command', 'bazi_semantic', 'bazi_condition_factor_201', 'bazi_semantic', 'source_ref', 'rel_smth_06_142', 'qiyin_jiucai_presence', 'rel_smth_06_143', 'shenwang_chengdu', 'rel_smth_06_144', 'zhengyin_yueling_risk', 'evi_smth_06_142', 'qiyin_jiucai_presence', 'rule_qiyin', 'evi_smth_06_143', 'chuangye_qingxiang', 'rule_chuangye', 'evi_smth_06_144', 'zhengyin_yueling_risk', 'rule_jincai', 'map_smth_06_095', 'map_smth_06_096']
    
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
        l1_anchor="smth_v1.0.0_弃印就财与舍轻就重_001_L1",
    )
    version: str = "1.0.0"
