"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596810
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
    semantic_id="qtbj_v1.0.0_1__十月丙火_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1十月丙火亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  十月丙火，太阳失令，得见甲戊庚出干，可云科甲，主为人性好清高，斯文领袖。如辛透见辰，名化合逢时，主大贵。
  或壬多无甲，乃作弃命从杀，即不科甲，亦是...
    """
    
    original_text: str = """- **原文（source_text）**：
  十月丙火，太阳失令，得见甲戊庚出干，可云科甲，主为人性好清高，斯文领袖。如辛透见辰，名化合逢时，主大贵。
  或壬多无甲，乃作弃命从杀，即不科甲，亦是宦僚。或壬多有甲无戊，却非从杀，宜用己土混壬。
  总之十月丙火，木旺宜庚，水旺宜戊，火旺用壬，随宜酌用可也。

- **分字分词释义**：
  - **太阳失令**：太阳失去时令 / 亥月特征 / 绝地
  - **斯文领袖**：文人中的领袖 / 甲戊庚透 / 贵
  - **化合逢时**：化气格逢时令 / 丙辛化水 / 大贵
  - **弃命从杀**：放弃本命从七杀 / 壬多无甲 / 变格
  - **宦僚**：官吏 / 从杀格 / 异途贵
  - **随宜酌用**：根据情况斟酌使用 / 灵活 / 总纲

- **规范化释义（primary_lang_explained）**：
  十月（亥月）的丙火，太阳失去了时令（绝地），如果能见到甲木、戊土、庚金出干（三奇？或取其配合），可以说科甲功名，主为人性情喜好清高，是斯文人的领袖。如果辛金透出见到辰土（丙辛化水，生于亥月水旺），这叫“化合逢时”，主大贵。
  如果壬水多而没有甲木（化杀），就作“弃命从杀格”看，即使不是科甲出身，也是官僚（异途之贵）。如果壬水多、有甲木而没有戊土，这就不是从杀（甲木泄水生身），适宜用己土来混杂壬水（此处存疑，己土混壬通常不吉，可能意指制水不如戊土有力，仅能混浊之，或取己土卑湿养木）。
  总之十月丙火，如果木旺适宜用庚金（劈甲/制印），水旺适宜用戊土（制杀），火旺适宜用壬水（既济），随着具体情况斟酌使用即可。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 10th Month (Pig Month): The Sun loses its command. If Jia, Wu, and Geng appear on stems, Civil Service is implied; the person is aloof and a leader of culture. If Xin is revealed and sees Chen, it is "Transformation Meeting Season" (Bing-Xin to Water), implying great nobility.
  If Ren is abundant without Jia, it is "Abandon Life Follow Killing"; even if not Civil Service, one becomes an official. If Ren is abundant with Jia but no Wu, it is not Follow Killing; using Ji Earth to mix with Ren is suitable (though usually inferior to Wu).
  In summary, for Bing in the 10th Month: If Wood is prosperous, use Geng; if Water is prosperous, use Wu; if Fire is prosperous, use Ren. Use discreetly according to the situation.

- **核心要点**：
  - **首要用神**：甲戊庚（配合使用）。亥月水旺，喜甲化杀，戊制杀，庚生水（若从杀）或制木（若木旺）。
  - **化气格**：丙辛化水，亥月当令，大贵。
  - **从杀格**：壬多无甲，从杀。
  - **用己土**：有甲不从杀，无戊可用己（效果较差）。

- **详细解说**：
  - 亥月丙火绝地，杀印相生（亥中壬甲）。
  - "太阳失令"：故需生扶（甲）或制杀（戊）。
  - "斯文领袖"：甲木印星化杀，主文名。
  - "化合逢时"：丙辛化水，最喜亥子月。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_254]` `[trigger: 亥月丙火]` `[factor_trigger: month_hai AND tiangan_bing AND tiangan_jia AND tiangan_wu AND tiangan_geng AND sun_loses_command]` `[role: 主干]` 十月丙火，太阳失令，得见甲戊庚出干，可云科甲，主为人性好清高，斯文领袖。 → 《穷通宝鉴·三冬丙火》#15.1
  - `[ns_qttbj_255]` `[trigger: 化合逢时]` `[factor_trigger: month_hai AND tiangan_bing AND tiangan_xin AND dizhi_chen AND transform_in_season]` `[role: 条件分支]` 辛透见辰，名化合逢时，主大贵。 → 《穷通宝鉴·三冬丙火》#15.1
  - `[ns_qttbj_256]` `[trigger: 弃命从杀]` `[factor_trigger: month_hai AND tiangan_bing AND ren_multiple AND NOT tiangan_jia AND pattern_abandon_life_follow_killing]` `[role: 条件分支]` 壬多无甲，乃作弃命从杀，即不科甲，亦是宦僚。 → 《穷通宝鉴·三冬丙火》#15.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 十月丙火（亥月）"
    factor_refs: list = ['sun_loses_command', 'transform_in_season', 'culture_leader']
    
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
        l1_anchor="qtbj_v1.0.0_1__十月丙火_亥月_001_L1",
    )
    version: str = "1.0.0"
