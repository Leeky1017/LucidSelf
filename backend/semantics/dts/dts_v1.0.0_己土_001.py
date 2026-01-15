"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008964
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
    semantic_id="dts_v1.0.0_己土_001",
    book_id="dts",
    engine_id="bazi"
)
class 己土(SemanticEntry):
    """
    - 原文（source_text）：
  己土卑湿，中正蓄藏，不愁木盛，不畏水旺，火少火晦，金多金明，若要物昌，宜助宜帮。

- 原注（原文注解）：
  　　己为田园之土，其性卑湿，乃戊土枝叶之地，亦...
    """
    
    original_text: str = """- 原文（source_text）：
  己土卑湿，中正蓄藏，不愁木盛，不畏水旺，火少火晦，金多金明，若要物昌，宜助宜帮。

- 原注（原文注解）：
  　　己为田园之土，其性卑湿，乃戊土枝叶之地，亦主中正，蓄藏万物，柔土能生木，非木所能克，故不愁木盛，土深能纳水，非水所能荡，故不畏水旺，无根之火，不能生湿土，故火少而光晦，湿土能润金，故金多而金之光彩，反精莹可观，此其无为而有为之妙用，若欲充盛长旺乎万物，则宜帮助为佳。

- 分字分词释义：
  - 己：阴土，田园之土，卑湿柔顺。
  - 卑湿：低洼湿润，性质柔顺。
  - 中正蓄藏：居中守正，蓄藏万物于其中。
  - 不愁木盛：柔土能生木，木盛不为患。
  - 不畏水旺：土深能纳水，水旺不能荡。
  - 火少火晦：无根之火难生湿土，故火少则光晦。
  - 金多金明：湿土能润金，金多则光彩精莹。
  - 宜助宜帮：若要万物昌盛，需比劫帮扶。

- 规范化释义（primary_lang_explained）：
  己土如田园沃壤，卑湿柔顺，与戊土的"高厚刚燥"形成对照。其特点在于"无为而有为"：柔土能生木而不怕木克，深土能纳水而不怕水荡；火少时湿土难以被生故火晦，金多时湿土润金而使金更明亮。己土的妙用在于以柔克刚、以静制动、以包容成就万物。但若要己土本身昌盛发达，则需要比劫帮扶，以增其厚度与力量。

- **次语种完整诠释（secondary_lang_full）**：  
  Ji Earth is the image of garden fields and fertile soil—low-lying, moist, and yielding. Compared to Wu Earth's mountain-like solidity, Ji represents the cultivated ground where things actually grow. Its nature is paradoxically resilient through softness. Wood cannot truly overcome it because soft earth nurtures wood growth rather than resisting it—the wood that "conquers" Ji actually depends on it. Water cannot wash it away because deep, absorbent soil takes in water rather than being displaced. Fire without strong roots cannot effectively generate Ji because moisture dampens the sparks—hence "fire dims when scarce." Yet Metal thrives when Ji is abundant: moist earth polishes and refines metal, making it shine brighter—"metal brightens when plentiful." This demonstrates Ji's principle of "accomplishing through non-action" (Wuwei Er Youwei): yielding to pressures, absorbing challenges, and transforming apparent threats into nourishment. However, for Ji Earth itself to flourish and expand, it requires assistance from fellow earth elements—without such support, its softness becomes mere weakness rather than strategic flexibility.

- **核心要点**：
  - 己为阴土，如田园沃壤，卑湿柔顺
  - 中正蓄藏：居中守正，蓄藏万物
  - 不愁木盛：柔土生木，木盛不为患
  - 不畏水旺：深土纳水，水旺不能荡
  - 火少火晦：湿土难被无根之火所生
  - 金多金明：湿土润金，使金光彩精莹
  - 宜助宜帮：己土本身昌盛需比劫帮扶

- **详细解说**：
  己土为阴土之代表，如田园沃壤，卑湿柔顺而善于蓄藏。与戊土的"高厚刚燥"形成对照，己土的精髓在于"无为而有为"——以柔顺包容的方式成就万物。木克土？柔土反能生木，木越盛反越得己土之养；水荡土？深土能纳水，水越旺反越被己土所容。火生土？无根之火难生湿土，故火少则光晦；金泄土？湿土能润金，金越多则光彩越明亮。这种"以柔克刚、以退为进"的特质使己土成为五行中最善于转化与包容的存在。但判断己土命局时，关键看是否有比劫帮扶：己土本身若要昌盛发达而非仅作为滋养他物的土壤，则需要戊己比劫助力。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_040]` `[trigger: 日主=己土]` `[factor_trigger: tiangan_ji]` `[role: 主干]` 己土如田园沃壤，卑湿柔顺，以无为而有为成就万物。 → 《滴天髓·天干论》#己土
  - `[ns_dts_041]` `[trigger: 己土见木盛]` `[factor_trigger: ji_wood_absorption]` `[role: 主干依赖]` 己土柔顺能生木，木盛不为患反得其养。 → 《滴天髓·天干论》#己土
  - `[ns_dts_042]` `[trigger: 己土见水旺]` `[factor_trigger: ji_water_containment]` `[role: 主干依赖]` 己土深能纳水，水旺不能荡反被其容。 → 《滴天髓·天干论》#己土
  - `[ns_dts_123]` `[trigger: 己土见金多]` `[factor_trigger: ji_metal_polishing]` `[role: 条件分支]` 己土湿润能养金，金多则光彩精莹。 → 《滴天髓·天干论》#己土
  - `[ns_dts_124]` `[trigger: 己土需帮扶]` `[factor_trigger: ji_peer_support]` `[role: 总结]` 己土若要本身昌盛，需比劫帮扶增厚其力。 → 《滴天髓·天干论》#己土"""
    normalized_text_zh: str = """"""
    subject: str = "己土"
    factor_refs: list = ['ji_beishi', 'ji_zhongzheng_xucang', 'ji_buchou_musheng', 'ji_buwei_shuiwang', 'ji_huohui_jinming', 'ji_yizhu_yibang']
    
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
        l1_anchor="dts_v1.0.0_己土_001_L1",
    )
    version: str = "1.0.0"
