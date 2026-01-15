"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228934
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
    semantic_id="smth_v1.0.0_天河水_乱洒六野与雨露滋生_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天河水乱洒六野与雨露滋生(SemanticEntry):
    """
    - **原文（source_text）**：
  丙午、丁未天河水。天河水者，乱洒六野，密沛千郊，淋淋泻下银河，细细飞来碧落。此乃天上雨露发生，万物无不赖之。银汉之水，土不能克，故见土不忌，而且有滋润...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙午、丁未天河水。天河水者，乱洒六野，密沛千郊，淋淋泻下银河，细细飞来碧落。此乃天上雨露发生，万物无不赖之。银汉之水，土不能克，故见土不忌，而且有滋润之益。天上之水，地金难生，故见金难益，而亦有涵秀之情。生旺太过，则为淫潦，反伤于物；死绝太多，则为旱乾，又不能生物，要生三秋得时为贵也。水喜长流大海。内丙午宜癸巳、癸亥，丁未宜壬辰、壬戌，阴阳互见尤吉。大溪乙卯为雷，井泉己酉为贵，俱以吉论。火喜霹雳，为神龙之火，与此水相济，而倏忽变化，云行雨施，岂有不贵？炉中火旺，大海水旺，如柱中得二火二水，上下相济，谓之精神俱足，大贵格也。灯头有风，山头有贵，皆以吉论，又须以别水济之方吉。天上就位，相克则忌见之。石榴、杨柳俱吉。大林有巽，平地有亥，亦吉。松柏石榴，遇丙辛合化，亦以吉论。妙选有灵槎入天河格，是取死绝无根之木，柱无土培，则漂流天河是也。土虽不能克，而柱逢庚午辛未，就位和克，土壅水滞，或水又冬生，则水结池塘，必主浊滥。

- **规范化释义（primary_lang_explained）**：
  丙午、丁未为天河水。天河水取象为银河之水，乱洒六野、密沛千郊，如从天上淋淋泻下的银汉，细雨从碧空飞来，为万物提供雨露之滋养。此水在象义上属"天水"：土不能真正克制它，反而因其下落而得滋润；地上的金也难以直接生此水，却能赋予其涵秀之气。若生旺太过，则为淫潦洪水，反伤万物；若死绝太过，则为旱乾枯竭，不足以生物，故以三秋得时为最贵。天河水喜欢与长流水、大海水相配：丙午宜癸巳、癸亥，丁未宜壬辰、壬戌，阴阳互见尤佳。大溪水乙卯如雷声、井泉水己酉为贵，两者与天河水相遇亦吉。火以霹雳火为神龙之火，与天河水相济，可成云行雨施、变化莫测之象；炉中火与大海水若与天河水配合成二火二水，上下相济，则为"精神俱足"之大贵格。灯头火有风、山头火有贵，皆因与天河水形成云火互动，仍需配其他水调和方吉。天上火若就位与之相克，则不宜多见。木类中，石榴木与杨柳木皆吉；大林木配巽风，平地木配亥水也佳；松柏与石榴木遇丙辛合化亦为吉象。妙选所谓"灵槎入天河"格，指死绝无根之木、柱中无土培，只得漂流天河之象。总体而言，天河水虽不怕土克，却怕庚午辛未等土就位和克：土壅则水滞，若又逢冬生，则水结为池塘，主浊滥之象。

- **完整对等诠释（secondary_lang_full）**：
  Bingwu and Dingwei belong to Heavenly-River Water. Heavenly-River Water is the Milky Way poured down: scattering across the six wilds, drenching a thousand outskirts, dripping from the silver river and lightly descending from turquoise heavens. It is the rain and dew born in the sky upon which all things depend. As "heavenly water", Earth cannot truly control it; instead Earth is moistened by its descent. Terrestrial Metals likewise struggle to generate it directly, though they lend refinement and elegance. When this Water is overly strong in life and growth, it becomes flooding that harms beings; when it is overly weak or in death, it becomes drought that fails to nourish. Thus it is most valuable when properly timed in the three autumn months. Heavenly-River Water enjoys Long-Flowing and Ocean Waters: internally, Bingwu prefers Guisi or Guihai, and Dingwei prefers Renchen or Renxu, with yin-yang intermeeting especially auspicious. Great-Stream Water at Yimao as thunder and Well Water at Jiyou as honor both pair well with it. Fire-wise, Thunder-Bolt Fire, known as divine-dragon Fire, combines with Heavenly-River Water to produce clouds and rain in sudden transformations, naturally noble. Strong Furnace Fire and vigorous Ocean Water, when present as two Fires and two Waters mutually supporting, are described as "spirit and essence both abundant", a great noble pattern. Covered-Lamp Fire with wind and Mountain-Top Fire with nobility also benefit when other Waters assist. Sky-Above Fire at full positional strength, however, clashes with Heavenly-River Water and must be avoided. Among Woods, Pomegranate and Willow Woods are favorable; Great-Forest Wood with Xun-wind and Flat-Earth Wood with Hai-Water are also good; Pine-Cypress and Pomegranate meeting Bing-Xin transformations are likewise auspicious. The "Spirit-Raft Entering Heavenly-River" pattern from Wonderful-Selection refers to dead, rootless Wood with no Earth in the chart—drifting upon Heavenly-River Water. Although Earth generally cannot overcome this Water, if the pillars meet Gengwu or Xinwei, positional balancing causes Earth to pile up and Water to stagnate; when Water is further born in winter, it congeals into ponds, signifying turbidity and stagnation.

- **核心要点**：
  - 天河水为天上雨露之水，主云行雨施与滋润万物
  - 不惧土克，反给土以润泽，金难直接生之但增其涵秀
  - 喜与长流水、大海等水相济，并配霹雳火成云雷雨施之象
  - 忌庚午辛未等土壅滞与冬令凝结，易从清雨变为浊塘

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_123]` `[trigger: 天河水]` `[factor_trigger: bingwu_dingwei AND tianhe_shui]` `[role: 主干]` 天河水者，乱洒六野，密沛千郊，淋淋泻下银河，细细飞来碧落。此乃天上雨露发生，万物无不赖之。 → 《三命通会》卷一#天河水

- **详细解说**：
  天河水强调"在天"与"下洒"的双重性：它不依赖地上的结构才存在，反而是地上万物依赖其周期性降落。命局中，若天河水配以霹雳火、大海水、长流水与适量土木，即形成一个"从天到地、从云至河"的完整水循环系统，象征制度与资源的上承下济；若只有庚午辛未等位土堆积，加之在冬季，则天河水难以下行，凝滞成浊水塘，喻为资源被堵、恩泽成祸。"灵槎入天河"格尤其典型：死木无根而漂浮天河，象征个人才华虽可触及高处，却缺乏土（现实结构）承接，易有大起大落甚至漂泊之象。

- **校勘与字词辨析（双语）**：
  - **中文**："乱洒六野、密沛千郊"皆形容雨露广布；"灵槎入天河"出自妙选，用以形容无根之木漂于天河。
  - **English**: Phrases like "scattering across the six wilds" and "densely drenching a thousand outskirts" describe widely distributed rain; "spirit-raft entering Heavenly-River" portrays rootless Wood drifting upon the celestial river."""
    normalized_text_zh: str = """"""
    subject: str = "天河水：乱洒六野与雨露滋生"
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
        l1_anchor="smth_v1.0.0_天河水_乱洒六野与雨露滋生_001_L1",
    )
    version: str = "1.0.0"
