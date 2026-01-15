"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066796
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
    semantic_id="smth_v1.0.0_3_印绶背禄与财官喜忌_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3印绶背禄与财官喜忌(SemanticEntry):
    """
    - 原文（source_text）：
  印绶生月，岁时忌见财星；运入财乡，却宜退身避位。
  劫财阳刃，切忌时逢；岁运并临，灾殃立至。
  十干背禄，岁时喜见财星；运至比肩，号曰背禄逐马。
  五行...
    """
    
    original_text: str = """- 原文（source_text）：
  印绶生月，岁时忌见财星；运入财乡，却宜退身避位。
  劫财阳刃，切忌时逢；岁运并临，灾殃立至。
  十干背禄，岁时喜见财星；运至比肩，号曰背禄逐马。
  五行正贵，忌冲刑克破之宫；四柱干支，喜三合六合之地。
  日干无气，时逢阳刃不为凶。
  官煞两停，喜者存之，憎者弃之。
  地支天干合多，亦云贪合忘官。
  四柱煞旺运纯，身旺为官清贵。
  凡见天元大弱，内有弱处复生。
  柱中七煞全彰，身旺极贫无寿；无煞女人之命，一贵可作良人。
  贵众合多，定是师尼娼婢。
  偏官时遇，制伏太过，乃是贫儒。
  四柱伤官，运入官乡必破。
  五行绝处，即是胎元；生日逢之，名曰受气。

- 分字分词释义：
  - **背禄**：伤官格（伤官克官，背离官禄）。
  - **逐马**：比劫夺财（比劫逐马）。
  - **正贵**：正官。
  - **日干无气**：身弱。
  - **一贵**：一位官星。
  - **受气**：受胎，绝处逢生。

- **规范化释义（primary_lang_explained）**：
  月令印绶格，岁运忌见财星坏印。若行运入财乡，应当退身避位，以免灾祸。
  劫财羊刃，最忌在时柱相逢。若岁运再遇羊刃，灾殃立至。
  伤官格（背禄），岁时喜见财星（生财）。若运至比肩，比肩夺财，名为“背禄逐马”，主贫困。
  正官（正贵）忌刑冲克破。四柱喜三合六合（有情）。
  日干无气（身弱），时上逢阳刃（帮身），不以凶论（反为帮身之宝）。
  官煞力量相当（两停），要保留喜欢的（如官），去掉憎恶的（如煞）。
  干支合多，容易贪合忘官（玩物丧志）。
  四柱煞旺，行运纯粹（制煞或印化），身旺者主清贵。
  日主极弱，但地支暗藏生机（如绝处逢生），名为弱处复生。
  七煞全彰（满盘七煞），即使身旺，若无制化，也是极贫无寿（或主凶死）。
  女命无煞，只有一位正官（一贵），主得良夫。若官煞混杂、贵人太多、合局太多，定是师尼娼婢之流（淫滥）。
  时上偏官格，若制伏太过（食伤太重），反是贫儒。
  伤官格，行运入官乡（伤官见官），必破（祸患）。
  五行绝处，往往是胎元所在（如木绝在申，申中壬水长生，木受气）。生日逢之，叫受气（如甲申日），主长寿或绝处逢生。

- 核心要点：
  - **印忌财**：印格忌财。
  - **伤官喜财**：背禄喜马。
  - **女命清纯**：喜一官。
  - **制煞适度**：不可太过。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_044]` `[trigger: 印忌财]` `[factor_trigger: yinshou_jicai AND rucaixiang_tuishen]` `[role: 主干]` 月令印绑，岁运忌逢财伤；若行财运，退身避位。 → 《三命通会》卷十一#印绶背禄与财官喜忌
  - `[ns_smth_11_045]` `[trigger: 背禄逐马]` `[factor_trigger: beilu_zhuma AND shangguange_xicai]` `[role: 主干依赖]` 伤官背禄，岁时喜见财星。若运至比肩，是背禄而逐马。 → 《三命通会》卷十一#印绶背禄与财官喜忌
  - `[ns_smth_11_046]` `[trigger: 日干无气]` `[factor_trigger: rigan_wuqi AND yangrenshi_bushe]` `[role: 条件分支]` 日干无气，时逢阳刃不为凶。 → 《三命通会》卷十一#印绶背禄与财官喜忌
  - `[ns_smth_11_047]` `[trigger: 女命一贵]` `[factor_trigger: nvming_yigui AND zuoliangren]` `[role: 条件分支]` 无煞女人之命，一贵可作良人。贵众合多，定是师尼娼婢。 → 《三命通会》卷十一#印绶背禄与财官喜忌
  - `[ns_smth_11_048]` `[trigger: 绝处受气]` `[factor_trigger: juechu_shouqi AND taiyuan_shengji]` `[role: 总结]` 五行绝处，即是胎元；生日逢之，名曰受气。 → 《三命通会》卷十一#印绶背禄与财官喜忌"""
    normalized_text_zh: str = """"""
    subject: str = "3 印绶背禄与财官喜忌"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_relation_factor_29', 'bazi_semantic', 'bazi_relation_shangguan_1', 'bazi_semantic', 'bazi_state_factor_148', 'bazi_semantic', 'bazi_state_factor_85', 'bazi_semantic', 'bazi_condition_factor_23', 'bazi_semantic', 'bazi_condition_factor_24', 'bazi_semantic', 'source_ref', 'rel_smth_11_040', 'core_factor', 'rel_smth_11_041', 'cond_factor', 'rel_smth_11_042', 'risk_factor', 'evi_smth_11_040', 'core_factor', 'rule_name40', 'evi_smth_11_041', 'cond_factor', 'rule_name41', 'evi_smth_11_042', 'risk_factor', 'rule_name42', 'map_smth_11_027', 'map_smth_11_028']
    
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
        l1_anchor="smth_v1.0.0_3_印绶背禄与财官喜忌_001_L1",
    )
    version: str = "1.0.0"
