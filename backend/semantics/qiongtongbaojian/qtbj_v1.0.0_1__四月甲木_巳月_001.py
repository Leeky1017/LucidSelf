"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619872
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
    semantic_id="qtbj_v1.0.0_1__四月甲木_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1四月甲木巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  四月甲木退气，丙火司权，先癸后丁。
  庚金太多，甲反受病。若得壬水，方配得中和，此人性好清高，假装富贵。即荫袭显达，终日好作祸乱，善辨巧谈，喜作诗文...
    """
    
    original_text: str = """- **原文（source_text）**：
  四月甲木退气，丙火司权，先癸后丁。
  庚金太多，甲反受病。若得壬水，方配得中和，此人性好清高，假装富贵。即荫袭显达，终日好作祸乱，善辨巧谈，喜作诗文。此理最验。
  如一庚二丙，稍有富贵。金多火多，又为下格。
  或癸丁与庚齐透天干，此命可言科甲，即风水浅薄，亦有选拔之才。癸水不出，虽有庚金丁火，不过富中取贵异途官职而已。壬透可云一富，若全无点水，又无庚金丁火，一派丙戊，此无用之人也。

- **分字分词释义**：
  - **退气**：气势退缩 / 病地衰退 / 巳月甲木状态
  - **司权**：主管当权 / 月令司令 / 丙火当令
  - **先癸后丁**：首先用癸水，其次用丁火 / 调候为先 / 用神次序
  - **甲反受病**：甲木反而生病受损 / 金多克身 / 身弱之患
  - **配得中和**：配合达到中和 / 壬水化杀 / 平衡之象
  - **假装富贵**：假装有钱有势 / 虚荣心重 / 壬多之性
  - **善辨巧谈**：善于辩论、巧于言谈 / 聪明伶俐 / 食伤之象
  - **异途官职**：非科举正途的官位 / 吏职武职 / 次等功名
  - **一派丙戊**：满盘丙火戊土 / 火炎土燥 / 极凶之象

- **规范化释义（primary_lang_explained）**：
  四月（巳月）的甲木，木气退缩（病地），丙火（食神）掌权。首先用癸水（调候润木），其次用丁火（泄秀/配合庚）。
  如果庚金太多，甲木身弱反而受病（克泄交加）。如果得到壬水化杀生身，才能配合中和。这种人性情喜好清高，假装富贵。即使有祖荫袭爵显达，也终日喜欢制造祸乱，善于辩论巧谈，喜欢作诗文。这个道理最灵验。
  如果有一个庚金、两个丙火（食神制杀），稍有富贵。如果金多火也多（克泄交加且交战），就是下等格局。
  如果癸水、丁火与庚金一起透出天干（配合得宜），这命可以说能中科甲，即使风水浅薄，也是选拔的人才。如果癸水不透出，虽然有庚金丁火，不过是富中取贵、异途（非科举）做官而已。壬水透出可说有一富。如果全无一点水，又没有庚金丁火，满盘丙火戊土（火炎土燥），这是无用的人。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 4th Month (Snake Month) is retreating in Qi (Sickness stage), while Bing Fire holds authority. First use Gui Water (to cool and moisten), then Ding Fire.
  If Geng Metal is excessive, Jia Wood falls ill (due to restriction and leakage). If Ren Water is obtained (to transform Metal), balance is achieved. Such a person loves being aloof and pretending to be wealthy. Even if they inherit prominence, they enjoy creating chaos all day, are skilled in debate and clever talk, and like writing poetry. This principle is most verified.
  If there is one Geng and two Bings (Food controlling Killing), there is slight wealth and nobility. But if both Metal and Fire are excessive, it is a lower pattern.
  If Gui, Ding, and Geng are all revealed in the Heavenly Stems, this life can speak of Civil Service Exams. Even if Feng Shui is shallow, they are selected talents. If Gui does not appear, even with Geng and Ding, it is merely wealth with some nobility, or official posts via alternative paths. If Ren is revealed, one can speak of wealth. If there is absolutely no Water, and no Geng/Ding, but a mass of Bing/Wu (Scorching Fire/Dry Earth), this is a useless person.

- **核心要点**：
  - **首要用神**：癸水（调候）。巳月火旺，无水木枯。
  - **次要用神**：丁火、庚金（配合癸水）。
  - **忌讳**：庚多无水（克泄交加），丙戊无水（火炎土燥）。
  - **特殊性格**：庚多见壬（清高、好乱、善辩）。

- **详细解说**：
  巳月甲木为病地，火旺土燥。
  - 必须见水，癸水优于壬水（癸为雨露，壬为江河，巳月喜雨露润燥）。
  - “先癸后丁”：先活命（水），再才华（丁）。
  - 庚金在四月长生，杀气不弱，若无水化，甲木受不了（又病又克）。
  - "善辨巧谈"：壬水化杀生身且带丙火食神气，主聪明但浮躁。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_113]` `[trigger: 巳月甲木]` `[factor_trigger: month_si AND tiangan_jia AND tiangan_gui AND tiangan_ding]` `[role: 主干]` 四月甲木退气，丙火司权，先癸后丁。 → 《穷通宝鉴·三夏甲木》#4.1
  - `[ns_qttbj_114]` `[trigger: 巳月庚多]` `[factor_trigger: month_si AND tiangan_jia AND metal_excessive AND tiangan_ren]` `[role: 条件分支]` 庚金太多，甲反受病，若得壬水，方配得中和。 → 《穷通宝鉴·三夏甲木》#4.1
  - `[ns_qttbj_115]` `[trigger: 巳月甲木性格]` `[factor_trigger: month_si AND tiangan_jia AND tiangan_ren AND tiangan_bing]` `[role: 主干依赖]` 此人性好清高，假装富贵，善辨巧谈，喜作诗文。 → 《穷通宝鉴·三夏甲木》#4.1
  - `[ns_qttbj_116]` `[trigger: 巳月甲木科甲]` `[factor_trigger: month_si AND tiangan_jia AND gui_revealed AND ding_revealed AND geng_revealed]` `[role: 条件分支]` 癸丁与庚齐透天干，此命可言科甲。 → 《穷通宝鉴·三夏甲木》#4.1
  - `[ns_qttbj_117]` `[trigger: 火炎土燥]` `[factor_trigger: month_si AND tiangan_jia AND NOT element_water AND fire_earth_excessive]` `[role: 例外处理]` 全无点水，又无庚金丁火，一派丙戊，此无用之人也。 → 《穷通宝鉴·三夏甲木》#4.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 四月甲木（巳月）"
    factor_refs: list = ['retreating_qi', 'holding_authority', 'pretending_to_be_wealthy', 'alternative_path_official_career']
    
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
        l1_anchor="qtbj_v1.0.0_1__四月甲木_巳月_001_L1",
    )
    version: str = "1.0.0"
