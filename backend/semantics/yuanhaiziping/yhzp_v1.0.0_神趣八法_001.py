"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559316
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
    semantic_id="yhzp_v1.0.0_神趣八法_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 神趣八法(SemanticEntry):
    """
    - **原文（source_text）**：
  类象者：乃天地一类也。如春生人，甲乙天干，地支寅卯辰全，无间断破坏，谓之夺东方一片秀气；最怕引至时为死绝之乡，谓之破了秀气，运至死绝，则不吉。或时上年...
    """
    
    original_text: str = """- **原文（source_text）**：
  类象者：乃天地一类也。如春生人，甲乙天干，地支寅卯辰全，无间断破坏，谓之夺东方一片秀气；最怕引至时为死绝之乡，谓之破了秀气，运至死绝，则不吉。或时上年上引生旺，为之秀气加临，十分大美。
  属象者：乃天干甲乙木，地支寅卯未全者是也。
  从象者：如甲乙日主无根，地支全金，谓之从金；四柱纯土，谓之从土；四柱纯水，谓之从水；四柱纯木，谓之从木；只有秀气者吉，无秀气者不吉。或天干有甲己字，或有根者不吉。其从火者，大旺运吉，死绝地凶。
  化象者：乃甲乙日生人，在辰戌丑未月，天干有一己字合甲字，谓之甲己化土，喜行火运；如逢甲乙木生旺运，化不成，反为不吉。己字中露出二甲字，谓之争合；有一个乙字露出，谓之妒合，为破格不成。
  照象者：如丙日巳午未，年月日遇时上一位卯木，谓之木火相照，甚吉；如壬癸日申子辰全属象者，遇时上一位金，谓之金水相照，大吉。年干有照者，亦吉也。
  返象者：乃所谓值月令用神，引至时上一位为绝之乡，谓之用之不用，皆为返运；又遇返之太甚，则不吉。
  鬼象者：乃秋月生甲乙日，地支四位纯金，谓之鬼象；只要鬼生旺运皆吉。怕见至死绝之乡，而又身旺则不吉。
  伏象者：乃寅午戌三合全，又值午月生逢壬日，而天干无丁字透露，壬水又无根；乃取午中有丁火，合壬水而伏之。所谓伏象，运至木火之乡皆吉；只愁水旺之乡，则不利也。

- **规范化释义（primary_lang_explained）**：
  神趣八法是判断特殊格局的八种法则：
  1. **类象**：天干地支五行同类一气。如春生甲乙日，地支寅卯辰全，无克破，称为夺东方秀气；忌行死绝运，喜生旺运。
  2. **属象**：天干甲乙木，地支寅卯未全（未为木库），亦属木类。
  3. **从象**：日主无根，地支全为异党。如甲乙日全金从杀，全土从财，全水从印，全木从旺（专旺）。从格需有秀气为吉，忌有根或透比劫。
  4. **化象**：如甲日生于辰戌丑未月，见己土合化为土，喜行生助化神之运（火土）。若行木旺运则还原，反为不吉。争合妒合皆破格。
  5. **照象**：五行相生互照。如丙日（火）见卯（木）为木火相照；壬癸（水）见金为金水相照。
  6. **返象**：月令用神引至时柱归于绝地，称为"用之不用"，为返运；太过则凶。
  7. **鬼象**：日主弱而地支纯官杀（如甲乙生秋，支全金）。只要官杀生旺则吉（从杀之意），怕行身旺或死绝之地。
  8. **伏象**：日主无根，藏于地支局中。如壬日无根，见寅午戌火局，取午中丁火合壬水伏藏。喜木火运，忌水旺运。

- **完整对等诠释（secondary_lang_full）**：
  **Eight Methods of Spiritual Interest**:
  1. **Category Image (Lèi Xiàng)**: Heaven and Earth are of the same category. E.g., Jia/Yi born in spring with Yin-Mao-Chen complete, creating an "East Region Elegance." Fears Dead/Extinct pillars; favors Prosperous pillars.
  2. **Attribute Image (Shǔ Xiàng)**: Jia/Yi stems with Yin-Mao-Wei complete (Wei being wood storage).
  3. **Following Image (Cóng Xiàng)**: Day Master rootless, branches fully opposing. E.g., Jia/Yi with full Metal follows Metal; full Earth follows Earth. Requires "Elegant Qi" to be auspicious. Presence of roots or combining stems (like Jia-Ji) without transformation breaks the pattern.
  4. **Transformation Image (Huà Xiàng)**: Jia/Yi born in Earth months combining with Ji to transform into Earth. Favors Fire/Earth luck; fears Wood prosperous luck which reverts the transformation. "Contention to combine" (two Jia one Ji) or "Jealousy to combine" (Yi appearing) breaks the pattern.
  5. **Reflection Image (Zhào Xiàng)**: Mutual generation. E.g., Bing Fire meeting Mao Wood is "Wood-Fire Mutual Reflection"; Ren/Gui Water meeting Metal is "Metal-Water Mutual Reflection." Highly auspicious.
  6. **Return Image (Fǎn Xiàng)**: Month Command Use-God leads to an Extinct position in the Hour Pillar, called "Using yet not Using." Excessive return is inauspicious.
  7. **Ghost Image (Guǐ Xiàng)**: Autumn Jia/Yi with full Metal branches (Killings). As long as the Ghost (Killing) is prosperous, it is auspicious (similar to Following Killing). Fears Self-prosperity or Extinction luck.
  8. **Submersion Image (Fú Xiàng)**: E.g., Ren Water rootless meeting Yin-Wu-Xu Fire frame, submerged by combining with Ding hidden in Wu. Favors Wood/Fire; fears Water prosperity.

- **核心要点**：
  - **八法体系**：类、属、从、化、照、返、鬼、伏
  - **从格条件**：日主无根，满盘异党，忌印比生扶
  - **化格条件**：合神得月令，无争合妒合
  - **吉凶关键**：顺势而为吉，逆势反背凶

- **详细解说**：  《神趣八法》是子平命理中处理特殊格局（外格）的高级技法，包含类、属、从、化、照、返、鬼、伏八种判断法则。**类象与属象**——即专旺格（曲直、炎上等），强调一方秀气聚集，如春生甲乙日支全寅卯辰为"夺东方秀气"。**从象与鬼象**——即从格（从财、从杀），日主无根而满盘异党，弃命从旺神。"鬼象"专指满盘七杀，身弱从杀。**化象**——即化气格，如甲己化土，需合神得月令且无争合妒合。**照象**——讲究相生五行互照，如木火相照、金水相照。**返象**——用神引至时柱绝地，称"用之不用"为返运。**伏象**——日主无根，暗藏于地支局中，如壬水伏于午中丁火。八法的核心在于"顺势而为"：顺格吉，逆格凶。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_607]` `[trigger: 类象秀气]` `[factor_trigger: leixiang AND zhuanwang_ge AND dongfang_xiuqi AND category_image AND elegant_qi]` `[role: 主干]` 类象者：乃天地一类也，如春生人甲乙天干地支寅卯辰全，谓之夺东方一片秀气。 → 《渊海子平·神趣八法》
  - `[ns_yhzp_608]` `[trigger: 从象无根]` `[factor_trigger: congxiang AND rizhu_wugen AND congcai_congsha]` `[role: 条件分支]` 从象者：如甲乙日主无根，地支全金谓之从金；四柱纯土谓之从土。 → 《渊海子平·神趣八法》
  - `[ns_yhzp_609]` `[trigger: 化象合化]` `[factor_trigger: huaxiang AND hehua_ge AND jiaji_huatu]` `[role: 条件分支]` 化象者：乃甲乙日生人在辰戌丑未月，天干有一己字合甲字谓之甲己化土。 → 《渊海子平·神趣八法》
  - `[ns_yhzp_610]` `[trigger: 照象相生]` `[factor_trigger: zhaoxiang AND muhuo_xiangsheng AND ji]` `[role: 条件分支]` 照象者：如丙日巳午未遇时上一位卯木谓之木火相照甚吉。 → 《渊海子平·神趣八法》
  - `[ns_yhzp_611]` `[trigger: 返象用之不用]` `[factor_trigger: fanxiang AND yongshen_jue AND yongzhi_buyong]` `[role: 条件分支]` 返象者：乃月令用神引至时上一位为绝之乡谓之用之不用。 → 《渊海子平·神趣八法》
  - `[ns_yhzp_612]` `[trigger: 鬼象从杀]` `[factor_trigger: guixiang AND shenruo_congsha AND shunshi_ji AND anchong_qugui AND angui AND congsha AND ghost_image]` `[role: 条件分支]` 鬼象者：乃秋月生甲乙日地支四位纯金谓之鬼象；只要鬼生旺运皆吉。 → 《渊海子平·神趣八法》
  - `[ns_yhzp_613]` `[trigger: 伏象暗合]` `[factor_trigger: fuxiang AND anhe AND zhicang_fu]` `[role: 条件分支]` 伏象者：乃寅午戌三合全又值午月生逢壬日，取午中丁火合壬水而伏之。 → 《渊海子平·神趣八法》
  - `[ns_yhzp_614]` `[trigger: 神趣八法纲领]` `[factor_trigger: shenqu_bafa AND teshu_geju AND shunshi]` `[role: 总结]` 神趣八法为特殊格局判断体系，核心在于顺势而为：顺格吉，逆格凶。 → 《渊海子平·神趣八法》

- **校勘与字词辨析**：
  - **神趣**：神妙的旨趣。
  - **鬼象**：此处"鬼"指七杀（偏官），非鬼怪。"""
    normalized_text_zh: str = """"""
    subject: str = "神趣八法"
    factor_refs: list = ['eight_methods_pattern', 'category_image', 'following_image', 'transformation_image', 'zhaoxiang', 'ghost_image']
    
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
        l1_anchor="yhzp_v1.0.0_神趣八法_001_L1",
    )
    version: str = "1.0.0"
