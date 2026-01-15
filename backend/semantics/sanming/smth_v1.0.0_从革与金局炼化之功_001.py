"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412826
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
    semantic_id="smth_v1.0.0_从革与金局炼化之功_001",
    book_id="sanming",
    engine_id="bazi"
)
class 从革与金局炼化之功(SemanticEntry):
    """
    - **原文（source_text）**：

  庚辛日见巳酉丑局，须带丙丁巳午一二位方成其器，但不可火多。如辛巳、辛酉、辛丑三日不喜五月生，被火所伤，宜八月或水土养育食神印绶为吉。诗曰：白虎但逢巳...
    """
    
    original_text: str = """- **原文（source_text）**：

  庚辛日见巳酉丑局，须带丙丁巳午一二位方成其器，但不可火多。如辛巳、辛酉、辛丑三日不喜五月生，被火所伤，宜八月或水土养育食神印绶为吉。诗曰：白虎但逢巳酉丑，格乎从革名偏厚，丙丁巳午少逢之，贵气炼成官最久。又：金居从革贵人钦，造化清高福最深，四柱火来相混杂，空门艺术谩经论。

- 分字分词释义：

  - **从革**：本义为随金而变，象征金在火炼之下成器，兼有革故鼎新之意。
  - **庚辛日见巳酉丑局**：日主为庚辛金，支成巳酉丑金局，金气专一而聚。
  - **须带丙丁巳午一二位方成其器**：从革之金须经火炼制，方能成器，故需见丙丁火或巳午火地一两处为宜。
  - **但不可火多**：火若太多，则金被烧损，不复为用，反成破坏之象。
  - **辛巳、辛酉、辛丑三日不喜五月生，被火所伤**：指辛金本已近火地，如再生于火旺之五月，则火势过猛，金受损伤。
  - **宜八月或水土养育食神印绶为吉**：八月金旺，兼得水土食神印绶养护，则金之成器而不受伤害。

- **规范化释义（primary_lang_explained）**：

  从革格，是以庚辛金日坐巳酉丑金局、并得适量火来炼化的一类格局。金若孤立，则刚而未成器；经火炼之后，方能成为可用之兵器、工具或制度，既有刚劲之性，又有实际之用，故原文以“格乎从革名偏厚”形容其格之厚重。

  关键在于“火之多少得宜”：须有丙丁或巳午来炼金，却不可过多；火微则金不化，成顽钝之象；火过则金焦毁，反成凶象。辛巳、辛酉、辛丑等日柱，若又生于五月火旺之时，便是火势太过、伤及金性之例。相对地，若生于秋令或行运多见水土食神印绶，则像是金在成熟季节中被适当锻炼和养护，更利于其发挥正面作用。

- 核心要点：

  - 以**庚辛日 + 巳酉丑金局**为基础，须有适量丙丁巳午之火来炼化金气。
  - 火宜有而不宜多：有火则成器，无火则顽钝，火过则伤金。
  - 喜秋令与水土食神印绶之助，忌火土混杂过甚，以防走向“空门艺术”之偏途或劳而无功。

- 详细解说：

  从革格所呈现的是一种“经磨炼而后成”的人生图像。庚辛金日若居巳酉丑金局，本身就具备坚硬、决断的性质；当局中再有丙丁或巳午之火，便如金铁入炉，经反复锤炼而成为利器。这类命局之人，多在经历较多考验与磨难之后，方能逐渐显出能力与地位。

  然而，考验与毁伤之间只有一线之隔：当火势适度时，是锻炼；火势过盛时，则是焚毁。原文以“白虎但逢巳酉丑”“四柱火来相混杂，空门艺术谩经论”等语，暗示从革格若失去平衡，就可能由“贵气炼成官最久”转为“遁入空门或流连艺术而难成实业”。实务判断时，需要综合金火强弱、印食配置与行运方向，分辨其究竟偏向“革故鼎新、成器为用”，还是走向“刚强无用或消磨于兴趣嗜好之中”。

- **校勘与字词辨析（双语）**：

  - “格乎从革名偏厚”一句，本稿理解为从革格之结构厚重、非一般轻清之格，不以“偏厚”为贬义。
  - “金居从革贵人钦，造化清高福最深”诸句，本稿归纳为“若金火得宜，则有清高而持久之福”的象意，不就诗句逐字硬译。
  - “空门艺术谩经论”一语，本稿视作对失衡格局的一种归宿提示，意指若火多混杂而失其用，易流于出世或艺术清谈之途，而非必然以出家或学艺为凶兆。
  - **English**：
    - Does not simply treat religious life or artistic pursuits as inauspicious signs.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_185]` `[trigger: 从革定义]` `[factor_trigger: congge_presence AND siyouchou_jinju]` `[role: 主干]` 庚辛日见巳酉丑局，须带丙丁巳午一二位方成其器。 → 《三命通会》卷六#从革
  - `[ns_smth_06_186]` `[trigger: 火炼成器]` `[factor_trigger: huolian_jin AND chengqi_weiyong]` `[role: 主干依赖]` 贵气炼成官最久。 → 《三命通会》卷六#从革
  - `[ns_smth_06_187]` `[trigger: 不可火多]` `[factor_trigger: huo_duo AND jin_shang]` `[role: 条件分支]` 但不可火多，火多则金被烧损。 → 《三命通会》卷六#从革
  - `[ns_smth_06_188]` `[trigger: 空门艺术]` `[factor_trigger: huohun_shiqu AND kongmen_yishu]` `[role: 总结]` 四柱火来相混杂，空门艺术谩经论。 → 《三命通会》卷六#从革"""
    normalized_text_zh: str = """"""
    subject: str = "从革与金局炼化之功"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_46', 'bazi_semantic', 'bazi_structure_metal_1', 'bazi_semantic', 'bazi_state_fire_metal_degree', 'bazi_semantic', 'bazi_state_degree_36', 'bazi_semantic', 'bazi_condition_fire_2', 'bazi_semantic', 'bazi_condition_fire_3', 'bazi_semantic', 'source_ref', 'rel_smth_06_166', 'congge_ge_presence', 'rel_smth_06_167', 'huolianjin', 'rel_smth_06_168', 'huoliang_pinghengdu', 'evi_smth_06_166', 'congge_ge_presence', 'rule_congge', 'evi_smth_06_167', 'huolianjin', 'rule_lianjin', 'evi_smth_06_168', 'wuyue_huoshang_risk', 'rule_huoshang', 'map_smth_06_111', 'map_smth_06_112']
    
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
        l1_anchor="smth_v1.0.0_从革与金局炼化之功_001_L1",
    )
    version: str = "1.0.0"
