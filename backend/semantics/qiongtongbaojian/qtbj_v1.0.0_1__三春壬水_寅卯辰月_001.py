"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578587
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
    semantic_id="qtbj_v1.0.0_1__三春壬水_寅卯辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三春壬水寅卯辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  **正月壬水**，汪洋之象，能并百川之流，然水性柔弱，宜用庚金之源，庶不致汪洋无度。有庚丙戊三者齐透，科甲功名。或庚戊藏支，丙坐寅支者，亦有恩诰，即一...
    """
    
    original_text: str = """- **原文（source_text）**：
  **正月壬水**，汪洋之象，能并百川之流，然水性柔弱，宜用庚金之源，庶不致汪洋无度。有庚丙戊三者齐透，科甲功名。或庚戊藏支，丙坐寅支者，亦有恩诰，即一庚透，贡监有之。
  凡壬日无比肩羊刃者，不必用戊，专用庚金，以丙为佐。
  或见比劫，又有庚辛，此弱极复旺，又宜制伏。戊透、可云科甲。戊藏、则是秀才。然必丙透不合、为妙。
  或支见多戊，又有甲出，名一将当关，群邪自伏，主光明磊落，名重百僚。或支成火局，惜不逢时，主名利皆虚，文章骇俗。
  用庚者，土妻庚子。用丙者，木妻火子。用戊者，火妻土子。

  **二月壬水**，寒气初除，有并流之象，不用丙暖，专取戊土辛金。二月壬水，先戊后辛，庚金次之。
  戊辛两透，雁塔题名。戊透辛藏，亦有恩诰。或戊辛不透，有庚出干者、主富。或支成木局，有庚透者，金榜题名。庚在支者，异途之仕。
  或木出火多，名木盛火炎，须比肩羊刃，尤宜水透，富贵恩荣。乏水者则否。
  或比肩重重，又须戊土，书曰：土止流水福寿全。若戊不见，名水泛木浮。一生辛苦，再行水运，落水而亡。
  或甲乙重重无比肩者，此依人度日，全无作为。若见庚辛，饥寒可免。

  **三月壬水**，戊土司权，恐有推山填海之患，先用甲疏季土，次取庚金。甲庚俱透，科甲定然。甲透庚藏，修齐品格。甲藏有根，可云俊秀。有癸滋甲，必主干城。独甲藏支，必富。独庚在柱，常人。无甲、刚暴之徒。乏庚、愚顽之辈。
  或时干透丁者，此为化合，助火而不助水。见丁未一理。或支成四库，乏甲者，名杀重身轻，终身有损。
  凡水旺多见庚金者，乃无用之人，须丙制之方妙。

- **分字分词释义**：
  - **汪洋之象**：大水浩渺之象 / 水势浩大 / 正月壬水
  - **庚金之源**：庚金为水之源头 / 印绶生身 / 发源
  - **恩诰**：皇帝恩诰 / 封官 / 吉象
  - **一将当关**：一人守关 / 甲木制戊 / 格局名
  - **群邪自伏**：众邪自然降伏 / 七杀被制 / 吉象
  - **雁塔题名**：科举高中 / 进士 / 吉象
  - **木盛火炎**：木旺火旺 / 财官双旺 / 需水制
  - **水泛木浮**：水多木漂浮 / 比劫重无土 / 凶象
  - **推山填海**：土多克水 / 杀重身轻 / 凶象
  - **干城**：国家干城 / 栋梁之材 / 吉象

- **规范化释义（primary_lang_explained）**：
  **正月（寅月）壬水**：汪洋之象，能并百川之流。然水性柔弱（泄气于寅），宜用庚金发源，庶不致汪洋无度（？此处"汪洋无度"应指水多，但寅月水病，应指"泄气无度"？原文可能有歧义，或指需要金生水才有汪洋之势）。有庚、丙、戊三者齐透，科甲功名。凡壬日无比肩羊刃者，不必用戊，专用庚金，以丙为佐。
  **二月（卯月）壬水**：寒气初除，有并流之象，不用丙暖，专取戊土（止流）、辛金（发源）。先戊后辛，庚金次之。戊辛两透，雁塔题名。若比肩重重，须戊土止水，书曰：土止流水福寿全。若戊不见，名"水泛木浮"，一生辛苦。
  **三月（辰月）壬水**：戊土司权，恐有推山填海之患（土重塞流），先用甲木疏季土，次取庚金发源。甲庚俱透，科甲定然。甲透庚藏，修齐品格。无甲，刚暴之徒；乏庚，愚顽之辈。或支成四库，乏甲者，名"杀重身轻"，终身有损。

- **完整对等诠释（secondary_lang_full）**：
  **1st Month (Tiger) Ren Water**: Vast ocean image, merging hundred rivers. But nature soft/weak (leaking in Tiger), suitable using Geng Metal source, preventing leaking-without-limit. Geng/Bing/Wu three revealing, imperial fame. If no Parallel/YangRen, no need Wu, focus on Geng, Bing as assist.
  **2nd Month (Rabbit) Ren Water**: Cold removed, merging flow image, no need Bing warm, focus Wu Earth (dike) Xin Metal (source). First Wu then Xin, Geng next. Wu/Xin both revealing, Yanta List fame. If Parallel heavy, must Wu Earth, book says: Earth stopping flowing water, fortune-longevity complete. If Wu absent, name "Water Flooding Wood Floating", life toil.
  **3rd Month (Dragon) Ren Water**: Wu Earth commands, fear of pushing-mountain-filling-sea (Earth blocking), first use Jia to dredge Earth, then Geng Metal. Jia/Geng both revealing, exam success certain. Without Jia, violent person; lacking Geng, foolish person. If branches four tombs lacking Jia, name "Killings Heavy Body Weak", lifelong damage.

- **核心要点**：
  - **正月**：喜庚金发源，丙火暖局（初春犹寒）。
  - **二月**：喜戊土堤防（水泛木浮），辛金发源。
  - **三月**：喜甲木疏土（杀重），庚金发源。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_383]` `[trigger: 壬生寅月]` `[factor_trigger: month_yin AND tiangan_ren AND tiangan_geng AND vast_ocean_image]` `[role: 主干]` 正月壬水，汪洋之象，能并百川之流，宜用庚金之源。 → 《穷通宝鉴·论壬水》#36.1
  - `[ns_qttbj_384]` `[trigger: 壬生卯月]` `[factor_trigger: month_mao AND tiangan_ren AND tiangan_wu AND tiangan_xin]` `[role: 主干]` 二月壬水，寒气初除，有并流之象，专取戊土辛金。 → 《穷通宝鉴·论壬水》#36.1
  - `[ns_qttbj_385]` `[trigger: 壬生辰月]` `[factor_trigger: month_chen AND tiangan_ren AND tiangan_jia AND tiangan_geng]` `[role: 主干]` 三月壬水，戊土司令，恐有推山填海之患，先用甲疏季土，次取庚金。 → 《穷通宝鉴·论壬水》#36.1
  - `[ns_qttbj_386]` `[trigger: 水泛木浮]` `[factor_trigger: month_mao AND tiangan_ren AND parallel_heavy AND NOT tiangan_wu AND water_flood_wood_float]` `[role: 例外处理]` 若戊不见，名水泛木浮，一生辛苦，再行水运，落水而亡。 → 《穷通宝鉴·论壬水》#36.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三春壬水（寅卯辰月）"
    factor_refs: list = ['water_flood_wood_float', 'push_mountain_fill_sea', 'yanta_title']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__三春壬水_寅卯辰月_001_L1",
    )
    version: str = "1.0.0"
