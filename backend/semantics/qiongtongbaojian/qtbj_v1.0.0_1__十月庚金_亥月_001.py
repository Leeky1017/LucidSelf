"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578371
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
    semantic_id="qtbj_v1.0.0_1__十月庚金_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1十月庚金亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  十月庚金，水冷性寒，非丁莫造，非丙不暖。
  丁甲两透，支无水局，一榜有之。支藏丙火，桃浪之仙。支见亥子，得己出制，亦有功名。
  若见丙透无丁者，决...
    """
    
    original_text: str = """- **原文（source_text）**：
  十月庚金，水冷性寒，非丁莫造，非丙不暖。
  丁甲两透，支无水局，一榜有之。支藏丙火，桃浪之仙。支见亥子，得己出制，亦有功名。
  若见丙透无丁者，决无显达。丁藏甲透，武职之人。以上不合者，庸俗。
  如金水混杂，全无丙丁者，鄙夫。支成金局，无火者，僧道之命也。书曰：水冷金寒爱丙丁。

- **分字分词释义**：
  - **十月**：亥月 / 农历十月 / 壬水司令
  - **水冷性寒**：水气冰冷金性寒凉 / 冬金 / 需火暖
  - **非丁莫造**：没有丁火不能成器 / 炼金 / 必须用神
  - **非丙不暖**：没有丙火不能温暖 / 调候 / 必须用神
  - **桃浪之仙**：进士 / 科举高第 / 吉象
  - **己出制**：己土出干制水 / 印制伤官 / 救应
  - **金水混杂**：金水相混 / 金水伤官 / 需火制
  - **鄙夫**：鄙陋凡人 / 无成就 / 凶象
  - **水冷金寒爱丙丁**：冬金需要火暖 / 调候口诀 / 用神

- **规范化释义（primary_lang_explained）**：
  十月（亥月）的庚金，水冷性寒，没有丁火不能造作（炼金），没有丙火不能温暖（解冻）。
  丁火甲木两透，地支无水局（食伤局），一榜（举人）是有的。地支藏有丙火，是桃浪之仙（进士）。地支见到亥子水（食伤重），得到己土出干制约（印制食伤），也有功名。
  如果见到丙火透出而无丁火者，决无显达（丙火不炼金，且冬日丙火无力，只能暖局，不能成大器？或者指官杀混杂不如丁火专一？）。丁火藏支甲木透出，武职之人。以上不合者（无丁甲丙），庸俗。
  如果金水混杂，全无丙丁火者，鄙陋的凡夫（金寒水冷）。地支合成金局，无火者，僧道之命（身旺无依）。古书说：水冷金寒爱丙丁。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 10th Month (Pig Month): Water is cold, nature is chilly. Without Ding, it cannot be forged; without Bing, it is not warm.
  If Ding and Jia are both revealed, and branches have no Water Frame, one List (Provincial degree) is possible. If Bing is hidden in branches, an Immortal of Peach Waves (Jinshi). If branches see Hai/Zi, obtaining Ji to control them also brings fame.
  If Bing reveals without Ding, there is definitely no prominence. Ding hidden and Jia revealed implies a military career. Those not matching the above are vulgar.
  If Metal and Water are mixed without any Bing/Ding, a vulgar person. If branches form a Metal Frame without Fire, a monk/Taoist destiny. The book says: Cold Water and Chilly Metal love Bing and Ding.

- **核心要点**：
  - **首要用神**：丁火（炼金）、丙火（暖局）。
  - **配合**：甲木（引丁）。
  - **金水伤官**：亥月金水伤官，最喜见官（丙丁）。无火则冷，无成。

- **详细解说**：
  - 亥月庚金病地（土病在亥，金病在亥？不，庚长生在巳，病在亥），气泄。
  - 关键在于“水冷金寒”。必须火来暖局和炼金。
  - 丁甲配合最佳，丙火辅助暖局。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_359]` `[trigger: 庚生亥月]` `[factor_trigger: month_hai AND tiangan_geng AND tiangan_ding AND tiangan_bing]` `[role: 主干]` 十月庚金，水冷性寒，非丁莫造，非丙不暖。 → 《穷通宝鉴·三冬庚金》#33.1
  - `[ns_qttbj_360]` `[trigger: 丁甲两透]` `[factor_trigger: month_hai AND tiangan_geng AND ding_revealed AND jia_revealed AND NOT dizhi_water_frame]` `[role: 条件分支]` 丁甲两透，支无水局，一榜有之。支藏丙火，桃浪之仙。 → 《穷通宝鉴·三冬庚金》#33.1
  - `[ns_qttbj_361]` `[trigger: 无丙丁]` `[factor_trigger: month_hai AND tiangan_geng AND NOT tiangan_bing AND NOT tiangan_ding]` `[role: 例外处理]` 如金水混杂，全无丙丁者，鄙夫。支成金局，无火者，僧道之命也。 → 《穷通宝鉴·三冬庚金》#33.1
  - `[ns_qttbj_362]` `[trigger: 水冷金寒]` `[factor_trigger: season_winter AND tiangan_geng AND cold_water_chilly_metal AND likes_bing_ding]` `[role: 总结]` 书曰：水冷金寒爱丙丁。 → 《穷通宝鉴·三冬庚金》#33.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 十月庚金（亥月）"
    factor_refs: list = ['peach_wave_immortal', 'cold_water_chilly_metal']
    
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
        l1_anchor="qtbj_v1.0.0_1__十月庚金_亥月_001_L1",
    )
    version: str = "1.0.0"
