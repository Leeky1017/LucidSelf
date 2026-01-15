"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008912
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
    semantic_id="dts_v1.0.0_丙火_001",
    book_id="dts",
    engine_id="bazi"
)
class 丙火(SemanticEntry):
    """
    - 原文（source_text）：
  丙火猛烈，欺霜侮雪，能煆庚金，逄辛反怯，土众成慈，水猖显节，虎马犬乡，甲来焚灭.

- 原注（原文注解）：
  　　丙为焚烈之火，纯阳之性，故不畏秋而欺霜，不...
    """
    
    original_text: str = """- 原文（source_text）：
  丙火猛烈，欺霜侮雪，能煆庚金，逄辛反怯，土众成慈，水猖显节，虎马犬乡，甲来焚灭.

- 原注（原文注解）：
  　　丙为焚烈之火，纯阳之性，故不畏秋而欺霜，不畏冬而侮雪，庚金虽顽，力能煆之，辛金虽柔，合而反弱，土其子也，见戊己多而慈惠之德，水其君也，遇壬癸旺而显忠节之风，至丙遂炎上之性，而寅午戌更露甲木，（身旺遇印）则燥而焚灭也.

- 分字分词释义：
  - 丙：阳火，光明、外向、显达之象.
  - 猛烈：势烈、力强，焚而上升.
  - 欺霜侮雪：不畏秋冬之寒，仍能发光发热.
  - 煆：以火炼金，使之成器；“煆庚金”喻以烈火炼刚金.
  - 逄：通“逢”，遇也；“逄辛反怯”，遇辛金反使其怯弱（合而弱）.
  - 土众成慈：土为丙之子，多土则火性缓，显慈和之德.
  - 水猖显节：水为丙之君，水旺之际，丙显示忠节之风（制水而不失义）.
  - 虎马犬乡：寅午戌火局乡里，助丙炎上.
  - 甲来焚灭：若身旺再遇甲木印透，助火炎上，反致燥烈焚灭之患.

- 规范化释义（primary_lang_explained）：
  丙火像烈日之光，先天就带着“要亮出来”的冲劲，即使在秋霜冬雪之时，也要冲破寒意去照人。遇到庚金，可以用火反复锻炼，使其由顽钝变成利器；但碰到辛金，多是合而化气，丙火自身反被牵弱，不能再拿“煆辛”当本事。土多时，火势有了承托，烈焰慢下来，人的性情也就多了几分宽厚慈和；水旺时，丙火立在水的对面守节，一面制伏水势，一面不至于把水全数烤干，才见“忠节”之风。若丙火本身已经十分强旺，又身在寅午戌火乡，再有甲木印星一味透出助火，就成了添柴加油，炎上太过，连本来可以依靠的木也被焚尽，反从成器之火变成焚物之火，这时必须以适量之水来润，以厚土来承，让火有出处、有归处，明而不虐。

- **次语种完整诠释（secondary_lang_full）**：  
  Bing Fire is the image of blazing sunlight. It wants to shine outward and rise up, and even in the cold of autumn frost and winter snow it pushes through to give light and warmth. When it meets hard Geng Metal, sustained heat can refine what is coarse into a useful tool; when it meets soft Xin Metal, the relationship is more about fusion and softening, and insisting on “forging” easily damages both sides. Abundant earth slows and carries the flames so that severity turns into generosity; surging water draws out Bing’s sense of duty, allowing it to restrain without annihilating, like a loyal minister who holds the line without overthrowing the ruler. The real danger appears when Bing is already very strong, sits in a fire triplicity such as Yin–Wu–Xu, and is further fuelled by exposed Jia resource: then the fire that should temper and illuminate becomes a blaze that burns its own roots and allies. Only when there is enough water to moisten and enough earth to bear the weight can Bing Fire be “bright with measure”: still capable of courage and achievement, but no longer a solitary flame that exhausts itself and consumes everything around it.


- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 猛烈 | Fierce Yang (Meng Lie) | 阳火刚烈、势强力猛 | Fierce yang solar fire with strong force | bing_menglie | new_candidate |
| 欺霜侮雪 | Defying Frost Scorning Snow | 不畏秋冬寒冷仍能发光发热 | Maintaining radiance even in cold seasons | qishuang_wuxue | new_candidate |
| 煆庚 | Forging Geng (Duan Geng) | 以烈火锻炼庚金成器 | Tempering Geng Metal into implements | duan_geng | new_candidate |
| 土众成慈 | Earth Abundance Brings Benevolence | 多土承载使火性缓和慈和 | Abundant Earth moderates fire into warmth | tuzhong_chengci | new_candidate |
| 水猖显节 | Water Surge Reveals Loyalty | 水旺时丙火守节制水而不灭 | Demonstrating restraint when controlling Water | shuichang_xianjie | new_candidate |
| 焚灭 | Over-combustion (Fen Mie) | 炎上太过焚毁根基 | Excessive burning destroying foundations | fenmie_risk | new_candidate |

- **核心要点**：
  - 丙为阳火，象烈日之光，性在向外照耀与上升
  - 欺霜侮雪：不畏秋冬寒冷，仍能发光发热
  - 煆庚合辛：庚金宜以烈火锻炼成器，辛金则宜柔合化气
  - 土众成慈：多土承载使火性缓和，显慈和之德
  - 水猖显节：水旺时丙火制水而不灭，显忠节之风
  - 虎马犬乡甲来焚灭：身旺遇火局再透甲木，炎上太过反致焚灭

- **详细解说**：
  丙火为阳火之代表，如烈日之光，先天带着"要亮出来"的冲劲。其贵在"明而有度"：光可以照人、烈可以成器，但不可灼伤焚根。对庚金宜以烈火锻炼使之成器（煆庚），对辛金则宜柔合化气收锋（合辛），不可一概用"火炼"的思路。土多时火有承托，烈焰缓和显慈和之德；水旺时丙火制水而不灭，守节而显忠义。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_031]` `[trigger: 日主=丙火]` `[factor_trigger: tiangan_bing]` `[role: 主干]` 丙火如烈日之光，贵在明而有度，光可照人不可灼伤。 → 《滴天髓·天干论》#丙火
  - `[ns_dts_032]` `[trigger: 丙火遇庚辛]` `[factor_trigger: bing_geng_relation]` `[role: 主干依赖]` 煆庚合辛，庚金宜以烈火锻炼成器，辛金则宜柔合化气。 → 《滴天髓·天干论》#丙火
  - `[ns_dts_033]` `[trigger: 丙火入火局透甲]` `[factor_trigger: bing_fenmie_risk]` `[role: 条件分支]` 寅午戌火乡再透甲印，从成器之火变焚物之火，须水润土承调候。 → 《滴天髓·天干论》#丙火
  - `[ns_dts_117]` `[trigger: 明而有度]` `[factor_trigger: bing_earth_support]` `[role: 主干依赖]` 丙火贵在光可照人而不焚物，须有水润与厚土承托。 → 《滴天髓·天干论》#丙火
  - `[ns_dts_118]` `[trigger: 夏令过炎]` `[factor_trigger: bing_water_control]` `[role: 例外处理]` 夏月丙火居火局又多印助炎时，当以壬水节制以防焚根。 → 《滴天髓·天干论》#丙火"""
    normalized_text_zh: str = """"""
    subject: str = "丙火"
    factor_refs: list = []
    
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
        l1_anchor="dts_v1.0.0_丙火_001_L1",
    )
    version: str = "1.0.0"
