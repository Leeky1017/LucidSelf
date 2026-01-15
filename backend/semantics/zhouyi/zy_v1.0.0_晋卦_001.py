"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919258
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
    semantic_id="zy_v1.0.0_晋卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 晋卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  晋：康侯用锡马蕃庶，昼日三接。

  【彖传】
  《彖》曰：晋，进也。明出地上。顺而丽乎大明，柔进而上行，是以“康侯用锡马蕃庶，昼日...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  晋：康侯用锡马蕃庶，昼日三接。

  【彖传】
  《彖》曰：晋，进也。明出地上。顺而丽乎大明，柔进而上行，是以“康侯用锡马蕃庶，昼日三接”也。

  【象传】
  《象》曰：明出地上，晋；君子以自昭明德。

  【爻辞】
  初六，晋如，摧如，贞吉，罔孚，裕无咎。
  六二，晋如，愁如，贞吉；受兹介福，于其王母。
  六三，众允，悔亡。
  九四，晋如鼫鼠，贞厉。
  六五，悔亡，失得勿恤，往吉，无不利。
  上九，晋其角，维用伐邑，厉吉，无咎，贞吝。

- 分字分词释义：

  - **晋**：前进、进升之意，既指地位、声望之进，也指光明扩展。
  - **康侯用锡马蕃庶，昼日三接**：安康的诸侯受赐众多良马，一日之内被多次召见，象征恩宠与进用之盛。
  - **明出地上**：离火之明在坤地之上，象征光明出于地面，逐渐照耀四方。
  - **顺而丽乎大明**：顺从并依附于更大的光明（上位者、天道），而非自恃其光。
  - **自昭明德**：自己彰显、照亮自身的德行，而非只借外在光环。
  - **晋如，摧如 / 愁如**：前进之际，同时感到受挫、忧愁，体现带着不安与压力的上升。
  - **众允**：众人认可、信服。
  - **鼫鼠**：田鼠，比喻小而贪、潜伏于暗处的形象，用于警示不正当的前进。
  - **失得勿恤**：不必为得失忧虑，顺势而行即可。
  - **晋其角**：前进到极点，如同角之突出锋锐，象征极端的进取。

- **规范化释义（primary_lang_explained）**：

  晋卦讲的是“在光明中上升”的路径与风险。卦辞以“康侯用锡马蕃庶，昼日三接”起头，描绘一位受宠的诸侯：被赐予许多良马、频繁被接见——看似荣耀之极，却也暗含“身在光照之下”的压力。

  彖传把“晋”解释为“进也”：离火在坤地之上，光明出地而上行，是一种由内向外、由下向上的明进。但要“顺而丽乎大明”，即顺应更大的光源与法则，把自己的进升附着在大明之上，而不是与之争焰。柔爻上行，说明进升当以柔顺、中正之德，而非刚猛争夺。

  象传“明出地上，晋；君子以自昭明德”进一步指出：真正的进步在于“明德”的自我昭示——内在德性足够亮，所处位置自然会迎来增长，而非单纯追求外在职位的上升。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Jin (Progress) portrays a time of gradual and harmonious progress, where one's inner light and virtues are acknowledged and appreciated by others. The image of fire emerging from the earth symbolizes the natural unfolding of one's talents and character, as one moves upward in life. The Judgment "Progress: the duke uses the gift of horses to aid the multitudes, and is thrice received in audience" illustrates the rewards of such progress, where one's abilities and virtues are recognized and valued by those in positions of authority. The hexagram teaches that true progress is not just about external advancement, but also about cultivating one's inner light and virtues, and being guided by a sense of purpose and direction.

- 核心要点：

  - 晋卦核心是**“在光明秩序中稳健上升”**，强调进而不躁、升而不骄。
  - 光明的来源在上，晋者须顺应与依附，而非抢占光源。
  - 爻辞通过“摧如、愁如、鼫鼠、晋其角”等意象，展示从谨慎上升到危险用进的全过程。

- 详细解说：

  卦象为上离下坤：地上有火，光明从地表升起。与明夷相对：明夷是光明入地而晦，晋则是光明在地中燃烧，再被风带出。

  初六“晋如，摧如，贞吉，罔孚，裕无咎”说明：起步之时，虽有前进之象，却感到压抑和受挫；只要守正，即便暂时得不到信任，只要心态宽裕，不急于求成，终可无咎。六二“晋如，愁如，贞吉；受兹介福，于其王母”则表现为：在忧愁中行进，只要守正，反而能从更高处（王母）获得大福。

  六三“众允，悔亡”提示：当进升到了众人认可的位置，先前的忧虑与悔意可以消解，但也要警惕随后的考验。九四“晋如鼫鼠，贞厉”则警告：若在高位以鼠之形态前进——小心眼、趋利避险，则即便占贞仍有危厉。

  六五“悔亡，失得勿恤，往吉，无不利”象征最理想的晋：在尊位之柔爻能够不被得失牵累，以中正之心前行，自然吉且无不利。上九“晋其角，维用伐邑，厉吉，无咎，贞吝”则刻画出进升极点的两面：以既成之势用于征伐，可有功而无咎；但若占贞仍执迷于锋芒毕露之进攻，则终归可惜（吝）。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_317]` `[trigger: 卦=晋 AND 卦辞=康侯用锡马]` `[factor_trigger: zhouyi_gua_jin AND zhouyi_guaci AND zhouyi_mingyu_fengxian]` `[role: 主干]` 晋，康侯用锡马蕃庶，昼日三接：光明上进，受宠日增。 → 《周易·晋卦·卦辞》
  - `[ns_zhouyi_318]` `[trigger: 卦=晋 AND 彖传]` `[factor_trigger: zhouyi_gua_jin AND zhouyi_tuan AND zhouyi_jinsheng_chengdu]` `[role: 主干依赖]` 进也。明出地上，顺而丽乎大明。 → 《周易·晋卦·彖传》
  - `[ns_zhouyi_319]` `[trigger: 卦=晋 AND 象传=明出地上]` `[factor_trigger: zhouyi_gua_jin AND zhouyi_xiang]` `[role: 主干依赖]` 明出地上，晋；君子以自昭明德：光明自下而上，照耀德行。 → 《周易·晋卦·象传》
  - `[ns_zhouyi_320]` `[trigger: 卦=晋 AND 初六=晋如摧如]` `[factor_trigger: zhouyi_gua_jin]` `[role: 条件分支]` 晋如摧如，贞吉：虽进而遇挫，守正仍吉。 → 《周易·晋卦·爻辞》
  - `[ns_zhouyi_321]` `[trigger: 卦=晋 AND 六二=晋如愁如]` `[factor_trigger: zhouyi_gua_jin]` `[role: 条件分支]` 晋如愁如，贞吉：虽进而忧愁，守正自吉。 → 《周易·晋卦·爻辞》
  - `[ns_zhouyi_322]` `[trigger: 卦=晋 AND 六三=众允悔亡]` `[factor_trigger: zhouyi_gua_jin]` `[role: 条件分支]` 众允，悔亡：众人信服，悔恨消解。 → 《周易·晋卦·爻辞》
  - `[ns_zhouyi_323]` `[trigger: 卦=晋 AND 九四=晋如鼫鼠]` `[factor_trigger: zhouyi_gua_jin]` `[role: 例外处理]` 晋如鼫鼠，贞厉：如鼫鼠般贪进，虽贞亦厉。 → 《周易·晋卦·爻辞》
  - `[ns_zhouyi_324]` `[trigger: 卦=晋 AND 六五=悔亡失得勿恤]` `[factor_trigger: zhouyi_gua_jin]` `[role: 主干依赖]` 悔亡，失得勿恤：不计得失，悔恨自消。 → 《周易·晋卦·爻辞》
  - `[ns_zhouyi_325]` `[trigger: 卦=晋 AND 上九=晋其角]` `[factor_trigger: zhouyi_gua_jin]` `[role: 总结]` 晋其角，维用伐邑：进至极处，宜用于内治。 → 《周易·晋卦·爻辞》
  - **中文**：
  - 卦辞"晋：康侯用锡马蕃庶，昼日三接"依通行王弼本；"晋"为进，"康侯"为安邦之诸侯，"锡马"为赐马。
  - "明出地上"谓离日自地平线升起，象征光明渐显、事业上升。
  - "蕃庶"释为繁盛众多；"昼日三接"谓一日之内三次觐见，受宠日增。
  - "晋如摧如"之"摧如"释为受挫之貌，进而遇挫仍守正则吉。
  - "鼫鼠"为贪婪之鼠，既能飞又能游又能爬又能穴居，然皆不精，以喻贪多而不专者。
  - "晋其角"谓进至极点如兽之角，过刚而易折，"维用伐邑"示宜用于内治而非外征。
  - **English**: Based on Wang Bi commentary edition. "康侯" is a pacifying lord. "锡马蕃庶" means granting horses and prosperity. "鼫鼠" (mole-rat) symbolizes greedy but unfocused advancement. "晋其角" indicates reaching the extreme point."""
    normalized_text_zh: str = """"""
    subject: str = "晋卦（䷢）"
    factor_refs: list = ['zhouyi_gua_035', 'symbol_brightness_earth_proposal', 'principle_self_illuminating_virtue_proposal', 'state_rewarded_noble_proposal', 'warning_progress_extreme_proposal']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_晋卦_001_L1",
    )
    version: str = "1.0.0"
