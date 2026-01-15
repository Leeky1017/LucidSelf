"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228854
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
    semantic_id="smth_v1.0.0_平地木_屋梁栋木与雨露滋润_001",
    book_id="sanming",
    engine_id="bazi"
)
class 平地木屋梁栋木与雨露滋润(SemanticEntry):
    """
    - **原文（source_text）**：
  戊戌、己亥平地木。平地木者，初生萌叶，始发枝条，惟资雨露之功，不喜雪霜之积。此乃地上之茂材，人间之屋木。戊戌为栋，己亥为梁，最宜互换见之，须以土为基上...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊戌、己亥平地木。平地木者，初生萌叶，始发枝条，惟资雨露之功，不喜雪霜之积。此乃地上之茂材，人间之屋木。戊戌为栋，己亥为梁，最宜互换见之，须以土为基上爱路傍为正格，更逄子午尤贵。以子午为天地正柱故也。屋壁、城头三土，以此木相资，中间有升化尤吉。砂驿无用，日时见之，主灾夭。火爱太阳霹雳，最为显耀。炉中遇水则福，灯头无风则固，余火无水则凶。此已成之木，不宜剑金，有木相资，则可泊金增饰光辉。又天干合地支旺，更有傍土为基，主大贵。余金无用。水见天河为润泽，主吉。溪海无山俱凶。井泉、涧下虽吉，内甲申合丁丑为山，遇之尤吉。术见大林，有风动摇，主寿促。桑柘癸丑最吉。壬子、己亥人见之为贵。戊戌人不堪松柏木倚辅平地为栋鿄，更有士助，主贵。大抵此木恶金而喜水士。若生三冬时，得寅卯，为寒谷回春，亦贵论也。

- **规范化释义（primary_lang_explained）**：
  戊戌、己亥为平地木。平地木象征地上初生的萌芽与刚出枝条之木，最依赖雨露滋润，不喜雪霜堆积，是人间屋梁栋木之材。戊戌如栋梁、己亥如横梁，两者互见最吉，必须有土为基，其中以路旁土为正格，再逢子午（天地正柱）则尤贵。屋上土、壁上土、城头土三类高位之土若与平地木相资并带升化，能使其上升为真正栋梁；砂中土与大驿土则多为拖累，日时见之多主灾夭。火以太阳火与霹雳火为佳，能令此木显耀；炉中火若遇水则福，覆灯火在无风时则稳固，余火若无水则易焚木。此木多为已成屋木之材，不宜再逢剑锋金过度砍伐；若有他木相辅，则泊金可为装饰增色。天干地支若有合化而得旺，再配傍土为基，则主大贵，其他杂金多无所用。水以天河为上，雨露相滋；井泉、溪涧清水可灌溉石榴，若水势过大如大海水，则多主贫夭。有艮土而稍见太阳火、霹雳火尚可，然不宜二火并见；炉中火在寅卯旺位本吉，再叠加他火则凶。若此木生于五月日时，仅带一火，名"石榴喷火"，主贵。桑柘、大林、杨柳三木皆喜见石榴：桑柘癸丑为山，大林戊辰为脱体，杨柳配之成花红柳绿之象，皆主功名。见松柏则格局更强，见平地则格局更大，若无杂物夹杂，乃"缘绕红园"之象，主富贵；更得城头土为基、水运为助，则享福优游而长久。

- **完整对等诠释（secondary_lang_full）**：
  Wuxu and Jihai belong to Flat-Earth Wood. Flat-Earth Wood represents newly sprouting leaves and first-extending branches on level ground—reliant on rain and dew, disliking accumulated snow and frost—serving as timber for human dwellings. Wuxu acts as beam, Jihai as cross-beam; the two seeing each other is most favorable, but only when Earth provides a base, with Roadside Earth as the proper pattern and Zi-Wu, the vertical pillars of heaven and earth, further enhancing nobility. Roof-Top, Wall-Top, and City-Top Earths, when combined with this Wood and undergoing transformative uplifting, turn it into true ridge-beam timber. Sand-Center and Grand-Post Earths, especially when appearing in the day and hour pillars, bring disasters and short life. Among Fires, Sunlight and Thunder-Bolt Fires are best, granting visibility; Furnace Fire, when moderated by Water, brings blessings; Covered-Lamp Fire without wind is steady; other Fires lacking Water burn destructively. As already-formed timber, this Wood should not face Sword-Edge Metal’s excessive cutting; with other Wood assisting, Foil-Metal can act as ornament, adding luster. When heavenly stems and earthly branches unite at prosperous states with supportive Earth at the side, great nobility is indicated; other Metals are mostly useless here. Water from Heavenly River gives ideal moistening and is auspicious; streams and oceans without mountains are harmful. Well and stream-below waters are beneficial, especially when Jiashen combining with Dingchou forms a mountain. Great-Forest Wood with strong winds shaking Flat-Earth Wood shortens life; Mulberry-Zelkova Wood with Guichou as mountain is most favorable. Renzi and Jihai natives meeting this Wood tend toward high status, whereas Wuxu natives suffer if Pine-Cypress Wood leans upon them, as the beams become too heavy for the base. Overall, this Wood dislikes excessive Metal and prefers Water and Earth nourishment; if born in the three winter months yet gains Yin-Mao as "spring returning to frozen valleys", it, too, becomes noble.

- **核心要点**：
  - 平地木象征屋梁栋木，需路旁等厚土为基，再配天地正柱
  - 喜屋上、壁上、城头三土相资，不宜砂中与大驿土拖累
  - 火以太阳、霹雳、得水之炉火、稳灯火为佳，忌无水之凡火
  - 厌多金，尤忌剑锋重砍；水以天河与山泉为吉，忌溪海无山之漂荡

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_113]` `[trigger: 平地木]` `[factor_trigger: wuxu_jihai AND pingdi_mu]` `[role: 主干]` 平地木者，初生萌蘖，始发枝条，惟资雨露之功，不喜雪霜之积，此乃人间屋木。戊戌为栋，己亥为梁，最宜互换，须得土为基。 → 《三命通会》卷一#平地木

- **详细解说**：
  平地木强调"已成材"与"待用"之间的状态——既是萌芽，又已可作屋木。原文通过不同土类，将平地木分为"可成栋梁"与"易毁之材"两类：路旁、屋上、壁上、城头诸土构成有体系的建筑结构；砂中与大驿则偏向流沙与道路驿站，难以稳固。火与水则决定其是否"显耀而不焚"：太阳与霹雳如同高光与雷声，使屋木出众；炉中与灯头在水与无风条件下可稳固其结构。若金重而无水土调和，则栋梁被斧钺反复砍伐，易有折损。实务推命时，戊戌己亥命局若得路旁土、三类高土与天河水，再配适度之火，而金不过多，即为屋梁成器之象；反之，多金少水、多砂大驿，则为根基不稳、灾夭之象。

- **校勘与字词辨析（双语）**：
  - **中文**："栋"与"梁"分别指大梁与横梁；"天地正柱"借子午为南北对冲之轴，喻支撑结构。
  - **English**: "Beam" and "cross-beam" denote main structural timbers; "heaven-earth vertical pillars" refer to the Zi-Wu axis symbolizing the supportive structure of heaven and earth."""
    normalized_text_zh: str = """"""
    subject: str = "平地木：屋梁栋木与雨露滋润"
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
        l1_anchor="smth_v1.0.0_平地木_屋梁栋木与雨露滋润_001_L1",
    )
    version: str = "1.0.0"
