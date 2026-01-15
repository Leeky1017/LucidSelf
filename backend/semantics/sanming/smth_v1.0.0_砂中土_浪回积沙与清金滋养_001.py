"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228878
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
    semantic_id="smth_v1.0.0_砂中土_浪回积沙与清金滋养_001",
    book_id="sanming",
    engine_id="bazi"
)
class 砂中土浪回积沙与清金滋养(SemanticEntry):
    """
    - **原文（source_text）**：
  丙辰、丁巳砂中土。砂中土者，浪回所积，波渚而成，龙蛇盘隐之宫，陵谷变迁之地。此土清秀，惟喜清金养之，更得清净之土，主早贵。钗砂、剑泊，此四金清秀相助。...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙辰、丁巳砂中土。砂中土者，浪回所积，波渚而成，龙蛇盘隐之宫，陵谷变迁之地。此土清秀，惟喜清金养之，更得清净之土，主早贵。钗砂、剑泊，此四金清秀相助。如丙人见辛亥，为丙丁入于乾户，号曰驾海长虹，又有星拱北之论，皆贵格也。更得水相涵，尤为土吉。若无水而时日得天上火照亦可。如丙辰、乙未、癸酉、戊午，此命有二金资养，却全无水，得太阳火照，故贵。如丁巳、癸卯、己未、壬申此命，二金资养，得天土火照亦贵。然戊午太燥，巳未稍缓，寿夭不同。水以井涧清洁为吉，若有金以养之，贵。如此土已得金养，而日时有海水，便坏造化。癸亥轻清，丙人见之，限运逢，亦主显荣。余水无用。火喜太阳在格，号为朱雀腾空，主贵。山头山下、炉中覆灯诸火，若无水济，主寿夭。木爱桑柘杨柳，以此土能栽二木故也。余木却以禄马贵人参之。如日中刑破冲克之木，虽见有何造化，不如无为吉。五行见金，只有白镴、怕巽，二者相妨，余金无用，亦须以贵人禄马看之。

- **规范化释义（primary_lang_explained）**：
  丙辰、丁巳为砂中土。砂中土取象为浪回所积、波渚堆叠之沙地，可为龙蛇盘隐之宫、陵谷变迁之所，质地清秀而不浊厚。此土最喜清金滋养，再得清净之土为辅，易早显贵：钗钏金、砂中金、剑锋金、泊金四类清金皆可资生，其中丙火日主见辛亥，有"丙丁入乾户"、"驾海长虹"与"星拱北"之贵格。若再得清水涵养则尤佳；若暂无水而时日得天上火照耀，亦可成名，只是燥湿不同，寿夭有别。水以井泉、涧下等清洁之水为上，配金则贵；若砂中土已得清金之养，却再逢大海水泛滥，则反坏造化。癸亥轻清，丙火见之，行运再逢，多主显荣，余水多不相宜。火方面以太阳火为最喜，号"朱雀腾空"，显达之象；山头火、山下火、炉中火、覆灯火等若无清水制衡，则多有短寿之忧。木以桑柘木、杨柳木最宜，由于砂中土能栽植此二柔木；余木则按禄马贵人权衡。总体上最忌土相刑、土过于杂浊：路傍土若能承载砂中土并配金木，尚主福庆；大驿土往来不定，即使见金水亦多凶象，其余浊土亦然。

- **完整对等诠释（secondary_lang_full）**：
  Bingchen and Dingsi belong to Sand-Center Earth. Sand-Center Earth is formed where waves return and deposit sand, becoming sandbanks and shoals—places where dragons and snakes might coil in hiding and where valleys rise and fall. This Earth is pure and elegant rather than thick and muddy. It delights most in being nourished by pure Metals and further supported by clean Earth, which together bring early nobility. Hairpin-Gold, Sand-Center Metal, Sword-Edge Metal, and Foil-Metal all qualify as such refined Metals. For Bing-Fire Day Masters encountering Xinhai, patterns such as "Bing-Ding Entering the Qian Gate", "Rainbow Riding Across the Sea", and "Stars Arching Around the North" denote high status. When further embraced by Water, this Earth becomes especially fortunate; even without Water, if the day and hour receive illumination from Sky-Above Fire, fame can still be achieved, though varying dryness leads to different spans of life. Among Waters, clear well and stream-below waters are best; when combined with nurturing Metals they signify wealth and rank. If this Earth has already been well nourished by Metal and then day and hour introduce Ocean Water, the configuration is spoiled. Light and clear Guihai Water, when met by Bing-Fire and activated in luck cycles, still promises distinction, while other waters mostly lack benefit. Regarding Fire, Sunlight Fire in pattern—nicknamed "Vermilion Bird Soaring into the Sky"—is most auspicious; yet Mountain-Top, Hillside-Beneath, Furnace, and Covered-Lamp Fires without Water relief shorten life. As for Wood, Mulberry-Zelkova and Willow Woods are favored, since this Earth can cultivate such trees; other Woods must be judged by stipend-horse and nobleman stars. Above all, Earth self-punishments and mixed, clashing soils are feared: when Sand-Center Earth rests upon Roadside Earth with Metal and Wood aiding, blessings remain; but encountering Grand-Post Earth’s ceaseless coming and going, even with Metal and Water present, is ominous, and other turbid Earths do little good.

- **核心要点**：
  - 砂中土为清秀沙壤，宜清金清土滋养
  - 喜井泉涧下清水涵养，忌大海水泛滥坏造化
  - 火以太阳火为贵，诸火无水易损寿
  - 钗钏金与砂金配清水最吉，可成金马嘶风等贵格

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_116]` `[trigger: 砂中土]` `[factor_trigger: bingchen_dingsi AND shazhong_tu]` `[role: 主干]` 砂中土者，浪回所积，波渚而成，龙蛇盘隐之宫，陵谷变迁之地。此土清秀，惟喜清金养之，更得清净之土，主早贵。 → 《三命通会》卷一#砂中土

- **详细解说**：
  砂中土的关键在于"清"与"养"：清金与清水皆可使其由沙变土、由虚变实，因此原文多次强调钗钏金、砂金、剑锋金与井泉涧下之水。若仅有金而无水，则为"火照砂丘"之象，虽暂贵而易燥；若仅有水而缺金与清土，则沙土被冲刷漂移，反难定形。大驿土与其他杂浊之土，则象征道路往来与地基不固，使本已不稳的砂土更难承载木金。命理判断中，可将砂中土视为需要精细工程与清洁环境的基底：金为工匠、水为润泽、清土为固托，三者兼备，则龙蛇盘隐之宫可成大用；反之，则多为漂沙浮土、贫夭之象。

- **校勘与字词辨析（双语）**：
  - **中文**："驾海长虹"比喻丙火入乾、跨海成虹之贵格；"朱雀腾空"是以太阳火照砂为名，主显达但忌过燥。
  - **English**: "Rainbow Riding Across the Sea" describes Bing Fire entering the Qian gate and spanning the sea in a noble pattern; "Vermilion Bird Soaring" names Sunlight Fire illuminating sand earth, indicating prominence with a risk of over-dryness."""
    normalized_text_zh: str = """"""
    subject: str = "砂中土：浪回积沙与清金滋养"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_砂中土_浪回积沙与清金滋养_001_L1",
    )
    version: str = "1.0.0"
