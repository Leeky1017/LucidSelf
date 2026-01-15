"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228901
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
    semantic_id="smth_v1.0.0_屋上土_瓦屋覆庇与木梁为本_001",
    book_id="sanming",
    engine_id="bazi"
)
class 屋上土瓦屋覆庇与木梁为本(SemanticEntry):
    """
    - **原文（source_text）**：
  丙戌、丁亥屋上土。屋上土者，埏埴为林，水火既济，盖蔽雪霜之积，震凌风雨之功。此土瓦也，非木无以架之，故以木为根基。平地为上，大林次之，余取天干化木亦吉...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙戌、丁亥屋上土。屋上土者，埏埴为林，水火既济，盖蔽雪霜之积，震凌风雨之功。此土瓦也，非木无以架之，故以木为根基。平地为上，大林次之，余取天干化木亦吉，只怕冲破。此已成之土，不宜见火。炉中丙寅最凶，丁卯稍可，太阳霹雳，可取相资。山下山头有木，生之则祸。灯头丙戌见乙巳为上，丁卯见甲辰次之，谓之火土入堂格。若柱中木多，亦不为吉。水宜天河、井泉、涧下皆吉。如先得平地木，成格大贵。溪流无木多夭。若丙戌而得癸巳，丁亥而得甲寅，则又别论，再看日时所成造化何如。大海无山，则不宜见土。土见路傍，如丙戌得辛未，丁亥得庚午，阴阳互见，更假木为基，主贵，壁土亦宜，余则汨没。若缺木而三刑聚，纵是二土亦凶。砂土独丁巳不妨，金惟剑锋、钗钏最吉。丁见壬申，天干化木，地支乾坤清夷。丙见辛亥，天干化水，地支丙入乾户，皆大贵格。若丁亥见庚戌，丙戌见癸酉，则不为吉。泊金有粉饰之用，亦吉。余金无用，当以贵禄参详。

- **规范化释义（primary_lang_explained）**：
  丙戌、丁亥为屋上土。屋上土取象为瓦片之土，经过水火既济、埏埴烧制而成，可遮蔽雪霜、抵挡风雨，是人间屋顶之护持之土。此土必须有木为梁柱以架之：平地木为上，大林木次之，其余可由天干化木而成，只要不被冲破。屋上土已属"成器之土"，不宜再见过多火气：炉中火丙寅最凶，丁卯略可；太阳火、霹雳火可视作相资之力，但须有木、水与结构配合。山下火、山头火若再遇木以生之，则容易引发火灾之祸。灯头火配丙戌见乙巳、丁卯见甲辰时，可成"火土入堂"之贵格；若柱中木过多，则屋上土承载过重亦不吉。水以天河、井泉、涧下之清水为佳，既济瓦土而不冲毁；若先得平地木为梁，再配此三水，则成大贵之格。溪流水无木多主夭折。大海水若无山，则不宜见土，以浪涌易冲毁瓦屋。土类中，路傍土配丙戌得辛未、丁亥得庚午为阴阳互见，再有木为基，可成贵象；壁上土亦可护身，余土则多为汨没。若木缺而三刑聚，即便二土同见亦主凶象。砂中土中独丁巳与屋上土不相妨。金方面，剑锋金与钗钏金最吉，可为瓦片与屋面装饰；泊金有粉饰作用亦佳，余金作用有限，需结合贵禄等综合判断。

- **完整对等诠释（secondary_lang_full）**：
  Bingxu and Dinghai belong to Roof-Top Earth. Roof-Top Earth represents the clay shaped and fired into tiles—Earth that, through the union of Water and Fire, now covers and shields against snow and frost, resisting wind and rain. It is the protecting Earth atop human dwellings. This Earth must rest on Wood beams: Flat-Earth Wood is best, Great-Forest Wood second, and other Woods formed through stem transformations are also acceptable, provided they are not broken by clashes. As an already "formed" Earth, Roof-Top Earth should not be exposed to excessive Fire. Furnace Fire at Bingyin is particularly dangerous, Dingmao somewhat less so; Sunlight and Thunder-Bolt Fires can be beneficial if properly combined with Wood, Water, and structure. Hillside-Beneath and Mountain-Top Fires, when additionally fed by Wood, easily indicate conflagration. Covered-Lamp Fire with Bingxu meeting Yisi or Dingmao meeting Jiachen creates the "Fire-and-Earth Entering-the-Hall" pattern, denoting noble status; yet when too many Woods burden the structure, misfortune results. Water from Heavenly River, wells, and stream-below sources suits this Earth, moistening and sealing without washing it away. If Flat-Earth Wood as beams is already present, configurations with these Waters point to high nobility. Stream Waters without Wood often lead to early death. Without mountains, Ocean Water should not meet Earth, as surging waves can demolish roofs. Among Earths, Roadside Earth combined with Bingxu at Xinwei or Dinghai at Gengwu—yin-yang intermeeting—becomes auspicious when Wood provides a base; Wall-Top Earth is also acceptable, while other soils tend toward muddiness and loss. When Wood is lacking and three-fold punishments gather, even two Earths together are still inauspicious. Among sands, only Ding-si Sand-Center Earth does not conflict. As for Metal, Sword-Edge and Hairpin Metals are most favorable, contributing structural and decorative elements; Foil-Metal beautifies the roof as well. Other Metals are less useful and must be judged via noble and stipend indicators.

- **核心要点**：
  - 屋上土为瓦屋之土，必须有木梁为本
  - 已成之土不宜再受炉火等烈火炙烤，宜天河、井泉、涧下等清水既济
  - 与平地木、路傍土、壁上土配合可成"火土入堂"与贵宅格
  - 忌缺木而多刑冲，亦忌大海水无山直冲屋脊

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_119]` `[trigger: 屋上土]` `[factor_trigger: bingxu_dinghai AND wushang_tu]` `[role: 主干]` 屋上土者，埏埴为林，水火既济，盖蔽雪霜之积，震凌风雨之功。此土瓦也，非木无以架之，故以木为根基。 → 《三命通会》卷一#屋上土

- **详细解说**：
  屋上土是所有土格中"成器度"最高之一：它不再是原始土壤，而是已经通过水火之功成为瓦片。这意味着：一方面，它极适合作为"庇护"与"遮蔽"的象征；另一方面，它对环境要求更精细——稍有不当便会破裂或坍塌。木在此格中扮演绝对基础角色：没有梁柱，瓦片无所附着；平地木、大林木与天干化木分别对应基础梁、上部梁与内在结构。水火则共同定义屋上土的安全边界：适度天河与井泉涧下之水，使瓦土坚实不裂；炉中火与山火则在无水、无木防护下，转为烧屋之象。实务中，判断丙戌丁亥命局时，可特别留意：是否有平地木与路傍土构成完整屋宇、是否有清水既济、是否有剑锋钗钏金作梁瓦加固，而不是仅有大海水与烈火冲击瓦屋——这几乎直接决定其为"安宅"还是"火宅"。

- **校勘与字词辨析（双语）**：
  - **中文**："埏埴为林"是指和泥制瓦成片如林；"火土入堂格"指火与屋上土在堂室中和合成贵象。
  - **English**: "Clay molded into a forest" describes rows of tiles like a forest of clay; "Fire-and-Earth Entering-the-Hall" denotes a pattern where Fire and Roof-Top Earth harmonize within a dwelling, indicating nobility."""
    normalized_text_zh: str = """"""
    subject: str = "屋上土：瓦屋覆庇与木梁为本"
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
        l1_anchor="smth_v1.0.0_屋上土_瓦屋覆庇与木梁为本_001_L1",
    )
    version: str = "1.0.0"
