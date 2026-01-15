"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228893
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
    semantic_id="smth_v1.0.0_大驿土_堂堂大道与厚载通行_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大驿土堂堂大道与厚载通行(SemanticEntry):
    """
    - **原文（source_text）**：
  戊申、己酉大驿土。大驿土者，堂堂大道，坦坦平途，九州无所不通，万国无行不至。此乃位属坤方，德乃厚载，轮天转日，负海乘山之土也。发生万物，以木为基。戊申...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊申、己酉大驿土。大驿土者，堂堂大道，坦坦平途，九州无所不通，万国无行不至。此乃位属坤方，德乃厚载，轮天转日，负海乘山之土也。发生万物，以木为基。戊申长生之土，德厚无疆，见三四木，皆能滋生。己酉自败之土，术多则窃气。大林合中逢冲主夭，别木则吉。更以禄贵参之，井泉、涧下二水，清贵不燥。如戊申见丁丑或乙酉，己酉见丙子或甲申，谓之官贵主吉。天河丙午而己酉得之，丁未而戊申得之，亦为贵禄，主福长流。戊申见癸己，巳酉见壬辰，亦吉，多逢则不宁静。大溪乙卯，为东震发生之义，单见亦吉。海水对穿，土不能胜日，时遇主夭，得山稍轻。内戊申见癸亥，戊癸合申亥，为地天交泰，反吉。火见太阳霹雳，谓之圣火，最能发生此土，如逄水助，主显达。其余凡火，再逄木生之更燥，主凶夭。五行见土，惟路傍最宜，屋上、壁上、砂中，纵先得木，亦为泯绝。城头有水，稍吉。命若有金，清秀吉。钗钏得辛亥，金泊得壬寅，戊申遇之，柱中更加水助，乃地天交泰，水绕山环，大格主贵。己酉见庚戌，癸卯稍次。砂金造化亦同。剑金，须候木得用，不然无益。

- **规范化释义（primary_lang_explained）**：
  戊申、己酉为大驿土。大驿土象征驿站大道与平坦通途，能通九州、达万国，是承载车马、人流与山海之土，位属坤方，重在"厚载"。发生万物仍以木为基：戊申为长生之土，德厚而能滋三四木；己酉则自败，木多则反窃其气。若大林木与大驿土合中又逢冲，多主夭折，换成其他木则较吉，仍需禄贵辅助。水以井泉、涧下为清贵之水：戊申见丁丑或乙酉、己酉见丙子或甲申，皆为官贵之象。天河水配丙午、丁未时，分别落在己酉、戊申上，也为贵禄，主福泽绵长。戊申见癸己、巳酉见壬辰等组合亦吉，但多见则不宁静；大溪水乙卯单见也佳。大海水若与大驿土对穿，则土不能胜其冲，多主夭折，仅有山可稍减其凶。内局戊申见癸亥时，戊癸合于申亥，成"地天交泰"之象反吉。火以太阳火与霹雳火为"圣火"，最能发动大驿土之用，若再有水相助，则主显达；其余凡火再逢木生，使土又燥则多为凶夭。土类中以路傍土最宜与大驿土相配，屋上、壁上、砂中诸土纵有木伴，反成泯绝；城头土若有水则稍吉。若命中有清秀之金，如辛亥钗钏金、壬寅泊金，再加水环绕，则大驿土能成"水绕山环"之大格；砂金之造化亦然。剑锋金只有在木得用时方可发挥雕斫之功，否则无益。

- **完整对等诠释（secondary_lang_full）**：
  Wushen and Jiyou belong to Grand-Post Earth. Grand-Post Earth symbolizes major relay stations and broad thoroughfares—roads that connect all regions of the realm and allow travel from every land to every other. Seated in the Kun direction, it emphasizes thick, carrying virtue, capable of bearing seas and mountains alike. It still relies on Wood as its basis: Wushen, as "long-life Earth", has boundless capacity to nourish three or four Woods; Jiyou, as self-defeating Earth, suffers when Wood is excessive and drains its qi. When Great-Forest Wood joins Grand-Post Earth and clashes arise, early death is indicated; with other Woods the outcome is better, still requiring noble and stipend stars. Water from wells and streams is best: Wushen meeting Dingchou or Yiyou, and Jiyou meeting Bingzi or Jiashen, all point to rank and office. Heavenly-River Water together with Bingwu or Dingwei, benefiting Jiyou and Wushen respectively, grants noble stipend and long-lasting blessing. Wushen encountering Guiji and Siyo meeting Renchen are also favorable, though frequent repetition brings restlessness; Great-Stream Water at Yimao alone is likewise good. When Ocean Water runs directly against Grand-Post Earth, the soil cannot withstand it, and such encounters at crucial times lead to premature death, mitigated only if mountains intervene. Internally, when Wushen meets Guihai, Wuwater combining with Guiwater over Shen-Hai forms an "Earth-Heaven Interpenetrating" pattern and becomes auspicious. Regarding Fire, Sunlight and Thunder-Bolt Fires are called "sacred fires"—they most effectively activate this Earth, and with Water support they indicate prominence. Other Fires, when further fueled by Wood, simply over-dry the Earth and point to misfortune or short life. Among Earths, Roadside Earth best matches Grand-Post Earth; Roof-Top, Wall-Top, and Sand-Center Earths, even with Wood, tend toward exhaustion and erasure. City-Top Earth with Water is modestly helpful. If the chart holds refined Metals, such as Hairpin-Gold at Xinhai or Foil-Metal at Renyin, and Wushen meets them with Water also present, "Earth-Heaven Interpenetrating" and "Water-Encircling-Mountains" patterns arise, signaling great nobility. Sand-Metal follows a similar logic. Sword-Edge Metal is only useful once Wood has gained proper function; otherwise it contributes little.

- **核心要点**：
  - 大驿土象征通衢驿站与厚载之土，以木为基
  - 喜井泉涧下清水、天河雨露及清金相助，可成地天交泰、水绕山环格
  - 忌大海水对穿与凡火多木使土燥裂
  - 与路傍土相配最佳，忌与砂中、屋上、壁上诸土混杂

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_118]` `[trigger: 大驿土]` `[factor_trigger: wushen_jiyou AND dayi_tu]` `[role: 主干]` 大驿土者，堂堂大道，坦坦平途，九州无所不通，万国无行不至。此乃位属坤方，德乃厚载，轮天转日，负海乘山之土也。 → 《三命通会》卷一#大驿土

- **详细解说**：
  大驿土的重点在"承载"与"流通"：它既要承受车马人流，又要承受木气与山海之重。因此原文强调"位属坤方，德乃厚载"，并以多种水火金木组合刻画其承载极限：清水与清金可以让驿土成为汇聚四方、物资流通的节点；大海水与凡火多木则使之成为被冲刷、被焚灼之地。与路傍土相比，大驿土更偏向节点与枢纽，而非单纯田地——如果命局中再见城头土有水、路傍土相辅、清金与天河水相绕，则可解读为"交通—城防—资源"三者兼备的结构中心，主大格贵显。实务判断时，可重点观察：大驿土是否有稳固基土、是否配清水而非泛海、是否有清金而非杂金；这些决定了其是"通衢厚载"还是"路断土崩"。

- **校勘与字词辨析（双语）**：
  - **中文**："地天交泰"本为卦名，此处借指大驿土与水木金三者和合之贵象；"水绕山环"则形容山水相抱、格局周全。
  - **English**: "Earth-Heaven Interpenetrating" is a hexagram name here applied to harmonious combinations of Grand-Post Earth with Water, Wood, and Metal; "Water Encircling Mountains" describes configurations where rivers and hills embrace each other to form a complete structure."""
    normalized_text_zh: str = """"""
    subject: str = "大驿土：堂堂大道与厚载通行"
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
        l1_anchor="smth_v1.0.0_大驿土_堂堂大道与厚载通行_001_L1",
    )
    version: str = "1.0.0"
