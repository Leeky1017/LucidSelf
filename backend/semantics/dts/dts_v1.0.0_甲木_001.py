"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008830
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
    semantic_id="dts_v1.0.0_甲木_001",
    book_id="dts",
    engine_id="bazi"
)
class 甲木(SemanticEntry):
    """
    - 原文（source_text）：
  甲木参天，脱胎要火，春不容金，秋不容土，火炽乘龙，水荡骑虎，地润天和，植立千古。

- 原注（原文注解）：
  　　甲为根干之木，纯阳之本，参天雄壮，火者，木...
    """
    
    original_text: str = """- 原文（source_text）：
  甲木参天，脱胎要火，春不容金，秋不容土，火炽乘龙，水荡骑虎，地润天和，植立千古。

- 原注（原文注解）：
  　　甲为根干之木，纯阳之本，参天雄壮，火者，木之子也，旺木得火而愈敷荣，生于春，则助火而不能容金也，生于秋则助金而不能容土也，寅午戌丙丁多见而坐辰，能摄之，申子辰壬癸多见而坐寅，则能纳之，土气不干，水汽不消，则能长生矣。
  　　辰为水库，能制火滋木，而土能泄火，则甲之根润，故不怕火，甲禄于寅，寅属艮，土厚，故能纳水。

- 分字分词释义：
  - 甲：天干之首，阳木，象参天之干；性刚健、直上。
  - 木：五行之一，主生发、条达、仁。
  - 参天：高大挺拔，直指上升之势；喻其性“上达、不屈、求通天时”。
  - 脱胎：去糟粕、炼其质，使材成器；于命理即“去其粗浊、成其文质”。
  - 要火：关键须火来炼木（子能成母，火为木之子而能炼其质）。
  - 春：木旺之时，助火，故“春不容金”（金来伐木，反违时令）。
  - 不容金：春木当令，金若强见，多为逆势；需看是否有水木通关、土载以缓。
  - 秋：金旺之时，木气反弱，故“秋不容土”（土泄火、助金而困木）。
  - 不容土：秋金当令，土多泄火、助金克木，易成伐木之势。
  - 火炽：火性炽盛，能“乘龙”。
  - 乘龙：龙喻辰（水库、湿土），火乘辰可不至焚木，得以化精；亦指火依有承载之地而不妄烈。
  - 水荡：水性荡涤，能“骑虎”。
  - 骑虎：虎喻寅（甲禄位、艮宫），水荡寅木，润而不没，助其生发与曲直.
  - 地润：地中有湿润（土中含水），能滋木根.
  - 天和：天时调匀（气候与时令相宜），阴阳得其中和.
  - 植立千古：根深枝茂，得以长久成立；喻格局得宜、寿命与事业可久.

 - 规范化释义（primary_lang_explained）：
  甲木像一株直插天际的大树，本性刚健、一路向上，需要经过火的锻炼脱胎，粗木才能成材。春天生的甲木，木气当令又兼助火，不宜再见强金来砍伐；秋天生的甲木，金气得势而木本已弱，再加厚土去帮金，更容易困折其根。甲木若得辰这类湿土来承火、藏水，使根不焦，又在寅位通根、引水上腾，地气润泽、天时和畅，如此根深枝茂，才能长久屹立。

- **次语种完整诠释（secondary_lang_full）**：  
  Jia Wood is portrayed as a tall, upright tree that strives to reach the sky. Its nature is strong, direct and growth‑oriented, yet raw timber must be tempered before it can become usable material. True refinement therefore depends on fire that can purify without burning the roots away, moist earth that can hold both fire and water, and seasons that do not work against Wood. In spring, when Wood already dominates, heavy Metal usually acts like a crude axe that cuts against the direction of the season; in autumn, when Metal is strong and Wood is weak, excessive Earth easily joins forces with Metal to trap and exhaust the roots. When Jia is rooted in positions such as Yin and supported by moist earth like Chen, water can be stored and lifted, fire can be carried without becoming destructive, and the soil around the roots stays damp rather than scorched. Under these conditions—deep anchoring, appropriate fire for tempering, and water that circulates instead of flooding—Jia Wood can stand firm “for a thousand years”, symbolizing lives and structures that grow tall without becoming brittle or uprooted.

 - **核心要点**：
  - 甲木为阳木，象参天之干，性刚健、直上
  - 脱胎要火：火为木之子，能炼质成材，但须有承载
  - 春不容金：春木当令，强金为逆势，需水通关或火制其锐
  - 秋不容土：秋金旺时厚土助金困木，需水泄金或木通根
  - 火炽乘龙：辰湿土能承火滋木，使根不焦
  - 水荡骑虎：寅禄位能纳水润木，使水不淹

- **详细解说**：
 甲木为天干之首、阳木之表，象征高大挺拔的参天大树。甲木成材需三要素：火炼（去粗存精）、根深（寅卯辰通根）、调候（水润土承）。"脱胎要火"非越多越好，须有辰等湿土承载，使火能炼质而不焚根。"春不容金"指春木当令时强金为逆势，"秋不容土"指秋金旺时厚土助金困木——但这非死法，须看全局有无通关泄化之路。"乘龙"取辰（水库湿土）之象，"骑虎"取寅（甲禄位）之象，二者分别承火、纳水，使地润天和、根深枝茂。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_025]` `[trigger: 日主=甲木]` `[factor_trigger: tiangan_jia]` `[role: 主干]` 甲木参天需根深土厚，若无水润火炼则枯燥难成材。 → 《滴天髓·天干论》#甲木
  - `[ns_dts_026]` `[trigger: 甲木春令见强金]` `[factor_trigger: jia_seasonal_flags]` `[role: 条件分支]` 春木当令而强金来伐，需水通关或火制其锐。 → 《滴天髓·天干论》#甲木
  - `[ns_dts_027]` `[trigger: 甲木得辰寅]` `[factor_trigger: jia_earth_support]` `[role: 主干依赖]` 甲木得辰承火、得寅纳水，骑龙乘虎，生发之机无穷。 → 《滴天髓·天干论》#甲木
  - `[ns_dts_113]` `[trigger: 调候三要]` `[factor_trigger: jia_fire_training]` `[role: 主干依赖]` 甲木成材须火炼、湿土承、水润调候，三者失衡则难植立千古。 → 《滴天髓·天干论》#甲木
  - `[ns_dts_114]` `[trigger: 节令禁忌]` `[factor_trigger: jia_seasonal_flags]` `[role: 总结]` 春金秋土皆可为病，须察节令与通关泄化，不可执一端论吉凶。 → 《滴天髓·天干论》#甲木"""
    normalized_text_zh: str = """"""
    subject: str = "甲木"
    factor_refs: list = ['jia_mu_cantian', 'tuotai_yaohuo', 'chun_burong_jin', 'qiu_burong_tu', 'chenglong_chentu', 'qihu_yinmu']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_甲木_001_L1",
    )
    version: str = "1.0.0"
