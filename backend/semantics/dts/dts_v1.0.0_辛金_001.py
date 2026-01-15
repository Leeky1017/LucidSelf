"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008996
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
    semantic_id="dts_v1.0.0_辛金_001",
    book_id="dts",
    engine_id="bazi"
)
class 辛金(SemanticEntry):
    """
    - 原文（source_text）：
  辛金软弱，温润而清，畏土之叠，乐水之盈，能扶社稷，能救生灵，热则喜母，寒则喜丁。

- 原注（原文注解）：
  　　辛乃阴金，非珠玉之谓，特温柔清润耳，戊土多...
    """
    
    original_text: str = """- 原文（source_text）：
  辛金软弱，温润而清，畏土之叠，乐水之盈，能扶社稷，能救生灵，热则喜母，寒则喜丁。

- 原注（原文注解）：
  　　辛乃阴金，非珠玉之谓，特温柔清润耳，戊土多则埋故之，壬水多则秀故乐之，辛为丙之臣也，抚恤壬水，使不克丙火，而匡扶社稷，辛为甲之君也，合化丙火，使不焚甲木，而救援生灵，生于九夏，而得己土，则能晦火而存之，生于隆冬，而得丁火，则能敌寒而养之，故辛金生于冬月，见丙则男命不贵，（丙辛合而化水）虽贵亦不忠，女命克夫，不克亦不和，若见丁则男女皆贵且顺。

- 分字分词释义：
  - 辛：阴金，温润清秀，非刚强之象。
  - 软弱：柔软不刚，与庚金刚健形成对照。
  - 温润而清：温和柔润，清秀可观。
  - 畏土之叠：怕多土埋金，使金无光。
  - 乐水之盈：喜水多则金水相生，清秀流通。
  - 能扶社稷：辛金能调和丙火与壬水关系，匡扶大局。
  - 能救生灵：辛金能合化丙火，使甲木不被焚烧。
  - 热则喜母：夏热需己土晦火护金。
  - 寒则喜丁：冬寒需丁火暖金养生。

- 规范化释义（primary_lang_explained）：
  辛金如珠玉之润，温柔清秀，与庚金的"刚健带煞"形成对照。其特点在于"温润调和"：怕多土埋没其光，喜水多则清秀流通；能调和丙火与壬水关系而扶社稷，能合化丙火使甲木不焚而救生灵。辛金在不同季节有不同调候需求：夏热时需己土晦火护金，冬寒时需丁火暖金养生。特别要注意辛金与丙火的关系：丙辛相合化水，冬月辛金见丙反不如见丁为贵顺。

- **次语种完整诠释（secondary_lang_full）**：  
  Xin Metal is the image of refined jade and polished gems—soft, lustrous, and pure rather than hard and martial like Geng. Its nature is "warm, moist, and clear" (Wenrun Er Qing): it shines through gentle refinement rather than forceful edge. Xin fears being buried under excessive earth (especially Wu Earth piled high), which smothers its luster; it delights in abundant water, which brings out its clarity and allows its qi to flow elegantly. Xin plays unique mediating roles in the cosmic order. As minister to Bing Fire, it can restrain Ren Water on Bing's behalf, preventing water from extinguishing the fire—"supporting the state" (Fu Sheji). As ruler over Jia Wood, it can combine with Bing Fire to transform it away, protecting Jia from being burned—"rescuing living beings" (Jiu Shengling). Seasonal adjustment is crucial: in summer's heat, Xin needs Ji Earth to dim the fire and preserve the metal; in winter's cold, Xin needs Ding Fire to warm and nurture it. The Bing-Xin combination requires special attention: in winter months, if Xin meets Bing, the combination transforms to water, which is cold and unhelpful—better to meet Ding Fire for genuine warmth and auspiciousness.

- **核心要点**：
  - 辛为阴金，如珠玉之润，温柔清秀
  - 软弱温润：柔软不刚，与庚金形成对照
  - 畏土之叠：怕多土埋没金光
  - 乐水之盈：喜水多则清秀流通
  - 扶社稷救生灵：能调和五行关系，发挥中介作用
  - 热则喜母：夏热需己土晦火护金
  - 寒则喜丁：冬寒需丁火暖金养生

- **详细解说**：
  辛金为阴金之代表，如珠玉宝石，温润清秀而非刚猛。其精髓在于"温润调和"——不以强力取胜，而以柔和协调发挥作用。辛金怕多土埋没，土叠则金无光；喜水多流通，水盈则金更秀。辛金在五行关系中扮演独特的中介角色：作为丙火之臣，能抚恤壬水使其不克丙火；作为甲木之君，能合化丙火使其不焚甲木——这便是"能扶社稷，能救生灵"的深意。季节调候同样重要：夏热时需己土晦火护金存身，冬寒时需丁火暖金养生。特别要注意丙辛合化：冬月辛金见丙，丙辛合化为水，寒上加寒反不利；若见丁火则得真暖，男女皆贵且顺。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_046]` `[trigger: 日主=辛金]` `[factor_trigger: tiangan_xin]` `[role: 主干]` 辛金如珠玉之润，温柔清秀，以温润调和发挥作用。 → 《滴天髓·天干论》#辛金
  - `[ns_dts_047]` `[trigger: 辛金见水多]` `[factor_trigger: xin_jin_water_clarity]` `[role: 主干依赖]` 辛金乐水之盈，水多则清秀流通，金水相生。 → 《滴天髓·天干论》#辛金
  - `[ns_dts_048]` `[trigger: 辛金见土叠]` `[factor_trigger: xin_jin_earth_burial]` `[role: 条件分支]` 辛金畏土之叠，土多埋金则光彩无存。 → 《滴天髓·天干论》#辛金
  - `[ns_dts_127]` `[trigger: 辛金冬月见丙]` `[factor_trigger: xin_jin_seasonal_adjustment]` `[role: 例外处理]` 冬月辛金见丙，丙辛合化水，寒上加寒反不利，不如见丁为暖。 → 《滴天髓·天干论》#辛金
  - `[ns_dts_128]` `[trigger: 辛金调和作用]` `[factor_trigger: tiangan_xin]` `[role: 总结]` 辛金能扶社稷救生灵，在五行关系中发挥独特的中介调和作用。 → 《滴天髓·天干论》#辛金"""
    normalized_text_zh: str = """"""
    subject: str = "辛金"
    factor_refs: list = ['xin_ruanruo', 'tiangan_xin_wenrun', 'xin_weitu_die', 'xin_leshui_ying', 'xin_fusheji', 'xin_reze_ximu']
    
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
        l1_anchor="dts_v1.0.0_辛金_001_L1",
    )
    version: str = "1.0.0"
