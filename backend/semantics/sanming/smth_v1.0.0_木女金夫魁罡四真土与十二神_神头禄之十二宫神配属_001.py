"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228746
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
    semantic_id="smth_v1.0.0_木女金夫魁罡四真土与十二神_神头禄之十二宫神配属_001",
    book_id="sanming",
    engine_id="bazi"
)
class 木女金夫魁罡四真土与十二神神头禄之十二宫神配属(SemanticEntry):
    """
    - **原文（source_text）**：
  之震，所以甲寅得庚申不为刑，乙卯得辛酉不为鬼，是木女金夫之正体，明左右之神化也。木主魂，金主魄，二者左右相间不合。若能全合，则神之化生以无间也。若庚申...
    """
    
    original_text: str = """- **原文（source_text）**：
  之震，所以甲寅得庚申不为刑，乙卯得辛酉不为鬼，是木女金夫之正体，明左右之神化也。木主魂，金主魄，二者左右相间不合。若能全合，则神之化生以无间也。若庚申得乙卯，辛酉得甲寅，不为元辰，变通之用也。戊辰、戊戌之土，为魁罡相会，乾坤厚德，覆载含生，不得以为返吟。戊辰、戊戌不为冲，土得正位，干守元会也。己丑、己未，是贵神，守忠贞。此四真土，有万物始终之道，非大人君子，孰能备此德？况神头禄各有神以主之，左右运动于六合之中，盈缩于吉凶之变也。己丑土为天乙贵人，己未土为太常福神，解百煞之凶。若得之当用，为横财之喜。戊辰为勾陈，戊戌为天空，土之神，多迁改，居帅外藩，出镇边防，有不常矣。丁巳为螣蛇之神，凶以凶用，吉以吉承，多荧惑之忧，有滑稽之性。丙午为朱雀之神，应阳明之体，文词藻丽。甲寅为青龙之神，博施济众，得四方之利。乙卯为六合之神，主发生荣华，和弱顺党。壬子为天后之神，主阴骘天德，容美多权。癸亥为玄武之神，乃阴阳终极，有潜伏之气，从下如流，虽有大智，非轩昂超达之士，顺则安平，逆则奸宄。庚申为白虎之神，利于武而不利于文，有抱道孤骞之性；善中严外，色厉内荏，有仁义，好幽僻。辛酉为太阴之神，怀肃杀之气，有清白之风，为文章利口，不世之才。然更各以亲疏休旺，定遇者之情性祸福。

- **分字分词释义**：
  - **木女金夫**：木为女、金为夫，阴阳配对。
  - **左右之神化**：左右两方的神妙变化。
  - **魂魄**：魂属木、魄属金，精神之本。
  - **左右相间不合**：本不相合，需全合才化生无间。
  - **元辰**：凶煞之一，此处指不为元辰所害。
  - **魁罡**：戊辰、戊戌为魁罡，刚猛之格。
  - **乾坤厚德**：如天地般厚德载物。
  - **返吟**：天克地冲的凶象。
  - **四真土**：己丑、己未、戊辰、戊戌四土。
  - **天乙贵人**：最尊贵的神煞。
  - **太常**：主福庆之神。
  - **勾陈**：主争讼牢狱之神。
  - **天空**：主虚耗变动之神。
  - **螣蛇**：主惊恐虚妄之神。
  - **朱雀**：主文书口舌之神。
  - **青龙**：主吉庆喜事之神。
  - **六合**：主和合顺利之神。
  - **天后**：主阴德容貌之神。
  - **玄武**：主盗贼阴私之神。
  - **白虎**：主凶丧刑伤之神。
  - **太阴**：主阴柔清秀之神。

- **规范化释义（primary_lang_explained）**：
  （接上）震卦，所以甲寅遇到庚申不为刑，乙卯遇到辛酉不为鬼，这是木女金夫的正体配合，说明左右神化的奥妙。木主魂、金主魄，二者本来左右相间不相合，如果能完全契合，则神的化生就没有间隔了。如果庚申遇到乙卯、辛酉遇到甲寅，也不成为元辰之凶，这是变通的用法。戊辰、戊戌之土，称为魁罡相会，有如乾坤那样厚德载物、覆盖包容一切生命，不能以返吟论凶。戊辰、戊戌虽天克地冲却不为冲，因为土得正位，天干守持元会。己丑、己未是贵神，守持忠贞之德。这四种真土（己丑、己未、戊辰、戊戌），有万物始终循环之道，不是大人君子，谁能具备这样的德行？况且神头禄各有神煞主之，在六合之中左右运动，随吉凶变化而盈缩消长。己丑土为天乙贵人，己未土为太常福神，能解百煞之凶，若得之当用，主横财之喜。戊辰为勾陈，戊戌为天空，都是土神，多主迁移变动，出任边疆军镇，变化无常。丁巳为螣蛇之神，遇凶则凶、遇吉则吉，多有荧惑之忧，性格滑稽。丙午为朱雀之神，应阳明之体，文词华丽。甲寅为青龙之神，广施恩惠救济民众，得四方之利。乙卯为六合之神，主发生荣华，性格和顺柔弱。壬子为天后之神，主阴德天德，容貌美丽多有权柄。癸亥为玄武之神，是阴阳的终极，有潜伏之气，顺从如流水，虽有大智慧，但不是轩昂超达之士，顺则安平，逆则为奸邪。庚申为白虎之神，利于武事不利文事，有抱道孤高之性，内心善良外表严厉，色厉内荏，有仁义，喜好幽僻。辛酉为太阴之神，怀肃杀之气，有清白之风，善于文章辩论，是不世之才。然而还要各自根据亲疏远近、休囚旺相，来判定遇到这些神煞者的性情和祸福。

- **完整对等诠释（secondary_lang_full）**：
  (Continuing) the Zhen trigram, so Jiayin meeting Gengshen is not punishment, Yimao meeting Xinyou is not ghost—this is the proper pairing of Wood-female Metal-husband, illuminating the wondrous transformation of left-right spirits. Wood governs hun-soul, Metal governs po-soul; these two are positioned left-right without matching. If they can fully unite, then spirit's transformation-birth has no gap. If Gengshen meets Yimao, Xinyou meets Jiayin, they do not form Primordial-Star malefic, being flexible application. Wuchen and Wuxu Earths are called Kui-Gang Assembly, having Heaven-Earth thick virtue, covering and carrying all living beings, not to be considered Fan-Yin (return-cry) malefic. Wuchen-Wuxu though stem-clashing branch-clashing, are not considered clash, because Earth attains proper position, stems guard primordial assembly. Jichou and Jiwei are noble spirits, guarding loyalty. These Four True Earths possess the Way of ten-thousand-things' beginning-end; who but great persons and noble lords can embody such virtue? Moreover, each divine-head stipend has spirits governing it, moving left-right within the Six Combinations, expanding-contracting amid fortune-misfortune changes. Jichou Earth is Noble-Person-of-Heaven, Jiwei Earth is Supreme-Constancy blessing-spirit, dissolving hundred malefics' harm. If obtained and properly used, it brings windfall-wealth joy. Wuchen is Gou-Chen, Wuxu is Sky-Void—both Earth-spirits causing much relocation, serving as commanders in outer territories, stationed at border defenses, ever-changing. Dingsi is Soaring-Snake spirit: if inauspicious then inauspicious-use, if auspicious then auspicious-bearing, much Mars-confusion worry, having comical nature. Bingwu is Vermillion-Bird spirit, embodying Yang-Brilliance, literary elegant. Jiayin is Azure-Dragon spirit, broadly bestowing and aiding multitudes, gaining four-directions' benefits. Yimao is Six-Harmony spirit, governing birth-flourishing prosperity, gentle-weak compliant-faction. Renzi is Heavenly-Empress spirit, governing hidden-virtue heavenly-virtue, beautiful appearance much authority. Guihai is Dark-Warrior spirit, being yin-yang's ultimate, having latent-hiding qi, following downward like flow; though having great wisdom, not lofty-transcendent scholars—if obedient then peaceful, if rebellious then treacherous. Gengshen is White-Tiger spirit, favorable for martial not for civil, having way-embracing solitary-soaring nature; kind within stern without, fierce-appearance soft-inside, having benevolence-righteousness, fond of secluded-remote. Xinyou is Greater-Yin spirit, harboring solemn-killing qi, having clean-pure manner, skilled in writing sharp-tongue, unequaled talent. Yet must further according to proximity-distance rest-flourishing, determine those encountering these spirits' temperament fortune-misfortune.

- **核心要点**：
  - 木女金夫正体：甲寅庚申、乙卯辛酉不刑不鬼
  - 魂魄：木主魂金主魄，左右相间，全合则神化无间
  - 魁罡：戊辰戊戌为魁罡相会，乾坤厚德，不为冲
  - 四真土：己丑（天乙贵人）、己未（太常福神）、戊辰（勾陈）、戊戌（天空）
  - 十二神配属：丁巳螣蛇、丙午朱雀、甲寅青龙、乙卯六合、壬子天后、癸亥玄武、庚申白虎、辛酉太阴
  - 各神煞有不同性情与吉凶主事，需配合休旺判断

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_251]` `[trigger: 木女金夫魁罡四真土十二神]` `[factor_trigger: wood_female_metal_husband AND kui_gang_pattern AND four_true_earths AND twelve_spirits_assignment]` `[role: 主干]` 甲寅得庚申不为刑，乙卯得辛酉不为鬼，是木女金夫之正体。木主魂，金主魄，若能全合，则神之化生以无间也。戊辰、戊戌之土，为魁罡相会，乾坤厚德，覆载含生，不得以为返吟。己丑、己未，是贵神，守忠贞。此四真土，有万物始终之道。己丑土为天乙贵人，己未土为太常福神。戊辰为勾陈，戊戌为天空。丁巳为螣蛇之神，丙午为朱雀之神，甲寅为青龙之神，乙卯为六合之神，壬子为天后之神，癸亥为玄武之神，庚申为白虎之神，辛酉为太阴之神。 → 《三命通会》卷一#木女金夫魁罡四真土十二神

- **详细解说**：
  本段是神头禄论述的延续，深入阐述十干专位与十二神煞的对应关系。首先说明甲寅乙卯木与庚申辛酉金的"木女金夫"配对，虽木金相克，却因阴阳得位而不刑不鬼，体现魂魄左右相间的神化原理。然后论述魁罡（戊辰戊戌）与四真土（加上己丑己未）的特殊性质：魁罡虽天克地冲却不为冲，因土得正位；四真土各有职司，己丑为天乙贵人最尊、己未为太常福神解煞、戊辰为勾陈主争讼、戊戌为天空主变动。接着详细列举十二神的配属与性情：丁巳螣蛇主惊恐、丙午朱雀主文书、甲寅青龙主吉庆、乙卯六合主和合、壬子天后主阴德、癸亥玄武主阴私、庚申白虎主凶丧、辛酉太阴主清秀。每一神煞都有独特的性格特征与主事范围，在实际推命中需结合休旺、亲疏来综合判断吉凶祸福。这是神头禄理论体系中关于神煞配属的核心内容，为后续格局判断提供重要依据。

- **校勘与字词辨析（双语）**：
  - **中文**："魁罡"为戊辰戊戌，刚猛有力，不同于一般冲克。"四真土"指命理中最重要的四个土日，各有特殊职司。十二神煞（天乙、太常、勾陈、天空、螣蛇、朱雀、青龙、六合、天后、玄武、白虎、太阴）是六壬与奇门中的重要神煞体系，在命理中广泛应用。
  - **English**: "Kui-Gang" refers to Wuchen-Wuxu, fierce and powerful, different from ordinary clash-control. "Four True Earths" are the four most important Earth-days in destiny studies, each with special functions. The Twelve Spirits (Noble-Person, Supreme-Constancy, Gou-Chen, Sky-Void, Soaring-Snake, Vermillion-Bird, Azure-Dragon, Six-Harmony, Heavenly-Empress, Dark-Warrior, White-Tiger, Greater-Yin) are an important spirit system from Liu-Ren and Qi-Men divination, widely applied in destiny analysis."""
    normalized_text_zh: str = """"""
    subject: str = "木女金夫魁罡四真土与十二神：神头禄之十二宫神配属"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_木女金夫魁罡四真土与十二神_神头禄之十二宫神配属_001_L1",
    )
    version: str = "1.0.0"
