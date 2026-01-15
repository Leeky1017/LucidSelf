"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066889
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
    semantic_id="smth_v1.0.0_6_总结与赋文结语_001",
    book_id="sanming",
    engine_id="bazi"
)
class 6总结与赋文结语(SemanticEntry):
    """
    - **原文（source_text）**：
  四柱煞旺运纯，身旺为官清贵。
  凡见天元大弱，内有弱处复生。
  柱中七煞全彰，身旺极贫无寿（一云无救）。
  无煞女人之命，一贵可作良人。
  贵...
    """
    
    original_text: str = """- **原文（source_text）**：
  四柱煞旺运纯，身旺为官清贵。
  凡见天元大弱，内有弱处复生。
  柱中七煞全彰，身旺极贫无寿（一云无救）。
  无煞女人之命，一贵可作良人。
  贵众合多，定是师尼娼婢。
  偏官时遇，制伏太过，乃是贫儒。
  四柱伤官，运入官乡必破。
  五行绝处，即是胎元；生日逢之，名曰受气。
  是以阴阳罕测，不可一例而推；务禀中和之气，神分贵贱。略敷古圣之遗书，约以今贤之博览。若遵此法参详，鉴命无差无误。

- **白话原意**：
  四柱七煞旺，若行运纯粹（制煞或印化），且身旺，主清贵之官。
  若日主太弱，但局中有印比生扶（弱处复生），亦可为福。
  柱中七煞全彰（满盘七煞），若身旺无制，主极贫无寿。
  女命无煞，只有一位贵人（正官），主嫁良夫。若贵众（官煞多）合多，定是师尼娼婢（淫乱或孤独）。
  时上偏官格，若制伏太过（食伤重），乃是贫寒儒士。
  四柱伤官格，运入官乡（见官），必破（伤官见官，为祸百端）。
  五行绝处，往往是胎元所在；生日逢之，叫“受气”（胞胎格），主贵。
  阴阳造化罕测，不可死板推断。务必禀持“中和”之气来分辨贵贱。略述古圣遗书，结合今贤博览，若遵此法，看命无差误。

- **核心要点**：
  - **女命清纯**：一贵为良，多合为贱。
  - **制煞适度**：太过则贫。
  - **伤官忌官**：运入官乡破。
  - **受气格**：绝处逢生贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_079]` `[trigger: 女命一贵]` `[factor_trigger: nvming_yigui AND zuoliangren]` `[role: 主干]` 无煞女人之命，一贵可作良人。贵众合多，定是师尼娼婢。 → 《三命通会》卷十一#总结与赋文结语
  - `[ns_smth_11_080]` `[trigger: 制煞太过]` `[factor_trigger: zhisha_taiguo AND pinru]` `[role: 主干依赖]` 偏官时遇，制伏太过，乃是贫儒。 → 《三命通会》卷十一#总结与赋文结语
  - `[ns_smth_11_081]` `[trigger: 伤官见官]` `[factor_trigger: shangguan_jianguan AND yunru_guanxiang]` `[role: 条件分支]` 四柱伤官，运入官乡必破。 → 《三命通会》卷十一#总结与赋文结语
  - `[ns_smth_11_082]` `[trigger: 中和之气]` `[factor_trigger: zhonghe_zhiqi AND jianming_wucha]` `[role: 总结]` 务禀中和之气，神分贵贱。若遵此法参详，鉴命无差无误。 → 《三命通会》卷十一#总结与赋文结语"""
    normalized_text_zh: str = """"""
    subject: str = "6 总结与赋文结语"
    factor_refs: list = ['engine_id', 'bazi_state_factor_85', 'bazi_semantic', 'bazi_condition_factor_23', 'bazi_semantic', 'bazi_condition_factor_24', 'bazi_semantic', 'bazi_state_factor_86', 'bazi_semantic', 'bazi_state_shangguan_9', 'bazi_semantic', 'bazi_structure_factor_31', 'bazi_semantic', 'source_ref', 'rel_smth_11_067', 'core_factor', 'rel_smth_11_068', 'cond_factor', 'rel_smth_11_069', 'risk_factor', 'evi_smth_11_067', 'core_factor', 'rule_name67', 'evi_smth_11_068', 'cond_factor', 'rule_name68', 'evi_smth_11_069', 'risk_factor', 'rule_name69', 'map_smth_11_045', 'map_smth_11_046']
    
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
        l1_anchor="smth_v1.0.0_6_总结与赋文结语_001_L1",
    )
    version: str = "1.0.0"
