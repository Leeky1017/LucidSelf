"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559569
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
    semantic_id="yhzp_v1.0.0_五行生克赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 五行生克赋(SemanticEntry):
    """
    - **原文（source_text）**：  
  五行生克赋。  
  大哉干支，生物之始，本乎天地，万象宗焉。有阴阳变化之机，时候浅深之用；故，金木水火土无正形，生克制化理取不一。假如死木，偏宜...
    """
    
    original_text: str = """- **原文（source_text）**：  
  五行生克赋。  
  大哉干支，生物之始，本乎天地，万象宗焉。有阴阳变化之机，时候浅深之用；故，金木水火土无正形，生克制化理取不一。假如死木，偏宜活水长濡。譬若顽金，最喜红炉煆炼。太阳火忌林木为仇。栋梁材求斧斤为友。火隔水，不能镕金。金沉水，岂能克木。活木忌埋根之铁。死金嫌盖顶之泥。甲乙欲成一块，须加穿凿之功。壬癸能达五湖，盖有并流之性。樗木不禁利斧。真珠最怕明炉。弱柳乔松，时分衰旺。寸金尺铁，气用刚柔。陇头之土，少木难疏。炉内之金，湿泥反蔽。雨露安滋朽木。城墙不产真金。剑戟成功，遇火乡而反坏。城墙积就，至木地而愁伤。癸丙春生，不雨不晴之象。乙丁冬产，非寒非暖之天。极锋抱水之金，最钝离炉之铁。甲乙遇金强，魂归西兑（酉）。庚辛逢火旺，气散南离（午）。土燥火炎，金无所赖。木浮水泛，火不能生。三夏镕金，安制坚刚之木。三冬湿土，难堤泛滥之波。轻尘撮土，终非活木之基。废铁销金，岂是滋流之本。木盛，能令金自缺。土虚，反被水相欺。火无木，则终其光。木无火，则晦其质。乙木秋生，拉朽摧枯之易也。庚金冬死，沉沙坠海岂难乎！凝霜之草，奚用逢金。出土之金，不能胜木。火未焰，而先烟。水既往，而犹湿。大抵，水寒不流，木寒不发，土寒不生，火寒不烈，金寒不镕；皆非天地之正气也。然，万物初生未成，而成久则灭。其超凡入圣之机，脱死回生之妙；不象而成，不形而化，固用不如固本，花繁岂若根深。且如，北金恋水而沉形（水多金沉）；南木飞灰而脱体（火旺木焚）；东水旺木以枯源（木盛水缩）；西土实金而虚己（金多土变）；火因土晦皆太过（土多火埋）。五行贵在中和。以理求之，慎勿茍言，掬尽寒潭须见底。


- **分字分词释义**：
  - **金木水火土无正形生克制化理取不一**：五行无定形，生克制化理取不一。
  - **死木偏宜活水长濡**：死木需活水滋润。
  - **顽金最喜红炉煆炼**：顽金需红炉煆炼。
  - **火隔水不能镕金**：火被水隔不能熔金。
  - **金沉水岂能克木**：金沉水中不能克木。
  - **水寒不流木寒不发土寒不生火寒不烈金寒不镕**：五行寒则失功能。
  - **北金恋水而沉形南木飞灰而脱体**：金多水沉，火旺木焚。
  - **五行贵在中和**：五行贵在中和不偏。
  - **固用不如固本花繁岂若根深**：固本比固用重要，根深比花繁重要。
  - **不象而成不形而化**：不拘泥于形象而成化。
- **规范化释义（primary_lang_explained）**：  
  《五行生克赋》系统阐述五行生克制化的精微变化与活用原则，突破机械生克模式，强调"无正形"与"理取不一"的灵活判断。**死木活木与顽金真金**：死木偏宜活水长濡，顽金最喜红炉煆炼；强调五行状态（死活、刚柔、寒暖）决定生克效果。**火水隔绝与金木沉浮**：火隔水不能镕金，金沉水岂能克木；活木忌埋根之铁，死金嫌盖顶之泥；强调五行位置与状态的相互影响。**五行寒温与气候**：水寒不流、木寒不发、土寒不生、火寒不烈、金寒不镕，皆非天地正气；癸丙春生不雨不晴，乙丁冬产非寒非暖；强调气候调候的重要性。**太过不及与中和**：北金恋水沉形、南木飞灰脱体、东水旺木枯源、西土实金虚己、火因土晦太过；五行贵在中和，太过不及皆非正道。**根本与枝叶**：固用不如固本，花繁岂若根深；万物初生未成成久则灭，超凡入圣之机在于不象而成不形而化。

- **完整对等诠释（secondary_lang_full）**：  
  **Five Elements Generation-Restraint Rhapsody**: Systematic exposition of the Five Elements' generation, restraint, control, and transformation, explaining subtle changes and flexible application principles; it breaks away from mechanical generation-restraint patterns, emphasizing "no fixed form" and "principles vary according to context." **Dead-Live Wood and Dull-True Metal**: Dead Wood favors active Water for long moistening; dull Metal most delights in red furnace smelting; this emphasizes that Five Elements' states (dead-alive, hard-soft, cold-warm) determine their generation-restraint effects. **Fire-Water Separation and Metal-Wood Sinking-Floating**: Fire separated by Water cannot smelt Metal; Metal sinking in Water cannot restrain Wood; live Wood taboos Iron burying its roots; dead Metal dislikes Mud covering its top; this emphasizes how positions and states of Five Elements mutually influence each other. **Five Elements Cold-Warm and Climate**: Water cold does not flow, Wood cold does not germinate, Earth cold does not grow, Fire cold does not blaze, Metal cold does not melt—all are not the Proper Qi of Heaven and Earth; Gui and Bing born in spring indicate neither rain nor clear sky; Yi and Ding born in winter indicate weather neither cold nor warm; this emphasizes the importance of Climate Adjustment. **Excess-Deficiency and Harmony**: North Metal loving Water sinks its form; South Wood flying as ash sheds its body; East Water vigorous makes Wood wither at the source; West Earth solid makes Metal empty itself; Fire obscured by Earth becomes excessive. Five Elements value Harmony—excess and deficiency are both not the correct path. **Root-Foundation and Branches-Leaves**: Consolidating use is not as good as consolidating the foundation; flourishing flowers are not as good as deep roots. Ten thousand things at first birth are unformed, but when formed for long they perish. The mechanism of transcending the ordinary and entering the saintly lies in accomplishing without image, and transforming without form.

- **核心要点**：  
  - 系统阐述五行生克制化的灵活变化，突破机械生克模式  
  - 强调五行状态（死活、刚柔、寒温）与位置（隔绝、沉浮、埋盖）决定生克效果  
  - 气候调候为核心：水寒不流木寒不发土寒不生火寒不烈金寒不镕  
  - 太过不及皆非正道，五行贵在中和；固本胜于固用，根深胜于花繁

- **详细解说**：  《五行生克赋》阐述五行生克的精微变化。**无正形理取不一**——"金木水火土无正形，生克制化理取不一"揭示五行生克的灵活性。**死木活金**——"死木偏宜活水长濡，顽金最喜红炉煆炼"强调五行状态决定生克效果。**隔绝沉浮**——"火隔水不能镕金，金沉水岂能克木"揭示五行位置的影响。**五行寒温**——"水寒不流，木寒不发，土寒不生，火寒不烈，金寒不镕"强调气候调候的重要。**太过中和**——"北金恋水而沉形，南木飞灰而脱体"等揭示太过之害；"五行贵在中和"为核心结论。**根本枝叶**——"固用不如固本，花繁岂若根深"揭示根本与枝叶的关系；"不象而成，不形而化"点明超凡入圣之机。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_500]` `[trigger: 无正形]` `[factor_trigger: wuxing_wu_zhengxing AND shengke_zhihua_liqu_buyi]` `[role: 主干]` 金木水火土无正形生克制化理取不一；五行生克灵活性。 → 《渊海子平·五行生克赋》
  - `[ns_yhzp_501]` `[trigger: 死木活金]` `[factor_trigger: simu_yi_huoshui AND wanjin_xi_honglu_duan]` `[role: 条件分支]` 死木偏宜活水长濡；顽金最喜红炉煆炼；五行状态。 → 《渊海子平·五行生克赋》
  - `[ns_yhzp_502]` `[trigger: 隔绝沉浮]` `[factor_trigger: huo_geshui_buneng_rongjin AND jin_chenshui_qineng_kemu]` `[role: 条件分支]` 火隔水不能镕金；金沉水岂能克木；五行位置。 → 《渊海子平·五行生克赋》
  - `[ns_yhzp_503]` `[trigger: 五行寒温]` `[factor_trigger: shui_han_buliu AND mu_han_bufa AND huo_han_bulie AND jin_han_burong AND buliu_bufa]` `[role: 条件分支]` 水寒不流木寒不发土寒不生火寒不烈金寒不镕；气候调候。 → 《渊海子平·五行生克赋》
  - `[ns_yhzp_504]` `[trigger: 太过中和]` `[factor_trigger: beijin_lianshui_chenxing AND beijin_lianshui AND nanmu_feihui_tuoti AND wuxing_gui_zhonghe AND anchong_qugui AND angui AND chenxing AND nanmu_feihui]` `[role: 例外处理]` 北金恋水而沉形南木飞灰而脱体；五行贵在中和。 → 《渊海子平·五行生克赋》
  - `[ns_yhzp_505]` `[trigger: 固本根深]` `[factor_trigger: guyong_buru_guben AND huafan_qiruo_genshen AND buxiang_ercheng AND guben_youyu AND guyong]` `[role: 条件分支]` 固用不如固本花繁岂若根深；不象而成不形而化。 → 《渊海子平·五行生克赋》
  - `[ns_yhzp_506]` `[trigger: 五行生克赋纲领]` `[factor_trigger: wuxing_shengke_fu AND wu_zhengxing AND sihuo_zhuangtai AND hanwen_tiaohou AND zhonghe]` `[role: 总结]` 五行生克赋以无正形、死活状态、寒温调候、太过中和为核心，阐述五行活用法则。 → 《渊海子平·五行生克赋》"""
    normalized_text_zh: str = """"""
    subject: str = "五行生克赋"
    factor_refs: list = ['five_elements_no_fixed', 'dead_live_wood', 'five_elements_cold_warm', 'five_elements_harmony', 'fix_foundation_use']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_五行生克赋_001_L1",
    )
    version: str = "1.0.0"
