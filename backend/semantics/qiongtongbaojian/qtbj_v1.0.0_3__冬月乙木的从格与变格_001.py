"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620133
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
    semantic_id="qtbj_v1.0.0_3__冬月乙木的从格与变格_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3冬月乙木的从格与变格(SemanticEntry):
    """
    - **原文（source_text）**：
  十一月乙木，木寒宜丙，有寒谷回春之象...
  或四柱多己，不逢比劫，乃为从才，富比王侯，若见比劫，贫无立锥。虽或一派戊己，见甲颇有衣禄。耑以丙火为用...
    """
    
    original_text: str = """- **原文（source_text）**：
  十一月乙木，木寒宜丙，有寒谷回春之象...
  或四柱多己，不逢比劫，乃为从才，富比王侯，若见比劫，贫无立锥。虽或一派戊己，见甲颇有衣禄。耑以丙火为用，方妙。

- **分字分词释义**：
  - **寒谷回春**：寒冷山谷回复春天 / 丙火功能 / 解冻
  - **从才**：从属财格 / 多己无劫 / 变格
  - **富比王侯**：富贵比得上王侯 / 从财成功 / 极富
  - **贫无立锥**：贫穷到没有立锥之地 / 见比劫 / 极贫
  - **耑以丙火为用**：专门以丙火为用神 / 冬乙总纲 / 核心

- **规范化释义（primary_lang_explained）**：
  十一月（含十二月气）的乙木，木寒适宜丙火，有寒谷回春的象。
  如果四柱多己土，没有遇到比劫（甲乙），这是“从财格”，富比王侯。如果见到比劫，贫无立锥之地。
  虽或者有一派戊己土，若见到甲木（制财），颇有衣禄（不能从财，但有甲帮身）。
  总之，专门以丙火为用神，才是妙法。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 11th Month: Wood is cold and suits Bing, creating the image of "Spring Returning to Cold Valley".
  If the four pillars have much Ji Earth and do not meet Parallel/Rob Wealth, it is "Follow Wealth", richer than princes. If Parallel/Rob Wealth is seen, one is poor without a place to stand.
  Even if there is a mass of Wu/Ji Earth, if Jia is seen (to control Earth), there is decent food and clothing.
  Exclusively using Bing Fire is the wondrous way.

- **核心要点**：
  - **从财**：冬月水旺，若土极多且无木，可从财（土克水反致富）。
  - **忌比劫**：从格忌比劫破格。
  - **总纲**：冬乙耑用丙。

- **详细解说**：
  - 冬月从财比较特殊，因为土冻。若无丙火暖局，土也是冻土，富而不贵或富难久。故从财格在冬月也喜带火。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_212]` `[trigger: 寒谷回春]` `[factor_trigger: season_winter AND tiangan_yi AND tiangan_bing]` `[role: 主干]` 十一月乙木，木寒宜丙，有寒谷回春之象。 → 《穷通宝鉴·三冬乙木》#10.3
  - `[ns_qttbj_213]` `[trigger: 冬乙从财]` `[factor_trigger: season_winter AND tiangan_yi AND ji_multiple AND NOT shishen_parallel AND pattern_follow_wealth]` `[role: 条件分支]` 四柱多己，不逢比劫，乃为从才，富比王侯，若见比劫，贫无立锥。 → 《穷通宝鉴·三冬乙木》#10.3
  - `[ns_qttbj_214]` `[trigger: 冬乙总纲]` `[factor_trigger: season_winter AND tiangan_yi AND winter_yi_likes_bing]` `[role: 总结]` 耑以丙火为用，方妙。 → 《穷通宝鉴·三冬乙木》#10.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 冬月乙木的从格与变格"
    factor_refs: list = ['pattern_follow_wealth', 'cold_valley']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_3__冬月乙木的从格与变格_001_L1",
    )
    version: str = "1.0.0"
