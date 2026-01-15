"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699494
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
    semantic_id="zw_v1.0.0_孔明之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 孔明之命(SemanticEntry):
    """
    - 分字分词释义：

  - **左右同宫**：左辅与右彼同宫拱照命身，主贵人扶持、多得助力。
  - **日卯月亥并明**：太阳居卯宫、太阴居亥宫，皆在本位得地，日月并明主聪颖通达。
  - **明...
    """
    
    original_text: str = """- 分字分词释义：

  - **左右同宫**：左辅与右彼同宫拱照命身，主贵人扶持、多得助力。
  - **日卯月亥并明**：太阳居卯宫、太阴居亥宫，皆在本位得地，日月并明主聪颖通达。
  - **明珠两照**：日月并明如双珠相照，主才智卓绝、声名远扬。
  - **多材多能**：一人兼具多种才能与技艺，善筹谋又能执行。
  - **大限太岁天使之地**：大限行至太岁与天使同宫之地，主寿元收束或重大危机。
  - **流羊流陀三方迭并**：流年羊刃与陀罗在三方宫位迭并，主高压与突发性折损。
  - **阴男金四局**：孔明命盘的五行局数，金四局主刚断智谋。

- **原文（source_text）**：  
  孔明之命。阴男金四局。左右同宫，日卯月亥并明，为明珠两照，一生富贵，多材多能。五十四岁，大限太岁天使之地，小限天伤忌耗，流羊流陀，三方迭并，故死。

- **规范化释义（primary_lang_explained）**：  
  孔明命为阴男金四局，命宫左右同宫，日卯月亥并明，如双明珠照临，一方面主才智卓绝、多才多艺，另一方面亦主一生富贵、有贵人相扶。此类配置往往对应「以智谋立身、文武兼备」之人。  
  然而，命局虽佳，寿命仍受限于后期岁运：五十四岁时，大限行至太岁与天使之地，小限又遇天伤，与流年羊刃、陀罗同在三方迭并，形成「天使 + 天伤 + 羊陀」的高压组合。此时既有对身体与气血的强烈消耗，也象征在高负荷谋划与操劳中透支心力，最终在这一阶段殒命。此命例刻画的是「才智与功业极盛，而寿命因重压略短」的谋臣命。

- **完整对等诠释（secondary_lang_full）**：  
  Zhuge Liang’s chart is described as that of a Yin Metal native of the Fourth Configuration. Left and Right Assistants share the same palace, while the Sun in Mao and the Moon in Hai both shine brightly—"two pearls of light." This indicates exceptional intellect, versatility and a life of honour with constant support from patrons. Such a pattern suits a strategist whose standing rests on insight and multifaceted talent.  
  Yet even this refined structure meets its limit. Around the age of fifty‑four, the major period moves into the joint region of Tai Sui and Tian Shi, while the minor period encounters Tian Shang. Transiting Yang Blade and Tuo Luo also form a triplicity with this sector, creating a configuration of heavy pressure: the "envoy" and "wound" stars combine with cutting malefics. This speaks both to physical depletion—years of overwork and strain—and to the heightened risk of sudden collapse under accumulated burdens. The case portrays a brilliant adviser whose life burns intensely and ends somewhat earlier than a truly long span.

- **核心要点**：  
  1. 左右同宫、日卯月亥并明，构成「明珠双照」的高智谋、高贵气命格。  
  2. 一生多材多能、富贵有成，但长期承担重任与高压。  
  3. 五十四岁大限太岁天使之地，小限天伤配合羊陀三方迭并，形成寿元略短的高危阶段。

- **叙事素材（narrative_snippets）**：
  - **明珠双照**："左右同宫，日卯月亥并明，为明珠两照"，孔明命主才智通明、见识通达，为典型谋臣格局。
  - **多材多能**："一生富贵，多材多能"，既善筹谋又能统筹全局，承担远超常人的责任。
  - **五十四岁高压**："五十四岁，大限太岁天使之地，小限天伤忌耗，流羊流陀，三方迭并，故死"，天使天伤与羊陀三方迭并，象征长期过劳在此年集中爆发。
  - **现代应用**：对承担长期高强度决策与智力劳动的人而言，当高压岁运叠至时，若仍坚持「事必躬亲」，极易在身体或精神上突然崩盘；应学会授权、减负与适时退居二线。"""
    normalized_text_zh: str = """"""
    subject: str = "孔明之命"
    factor_refs: list = ['pattern_zuoyou_tonggong', 'pattern_riyue_bingming', 'pattern_mingzhu_liangzhao', 'result_duocai_duoneng', 'timing_daxian_taisui_tianshi', 'malefic_liuyang_liutuo_dibing']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_孔明之命_001_L1",
    )
    version: str = "1.0.0"
