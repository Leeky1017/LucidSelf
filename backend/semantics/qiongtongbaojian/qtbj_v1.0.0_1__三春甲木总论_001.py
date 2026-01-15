"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619784
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
    semantic_id="qtbj_v1.0.0_1__三春甲木总论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三春甲木总论(SemanticEntry):
    """
    - **原文（source_text）**：
  春月之木，渐有生长之象。初春犹有余寒，当以火温暖，则有舒畅之美，水多变克，有损精神。重见生旺，必用庚金斲凿，可成楝梁。
  春末阳壮水渴，藉水资扶，则...
    """
    
    original_text: str = """- **原文（source_text）**：
  春月之木，渐有生长之象。初春犹有余寒，当以火温暖，则有舒畅之美，水多变克，有损精神。重见生旺，必用庚金斲凿，可成楝梁。
  春末阳壮水渴，藉水资扶，则花繁叶茂。
  初春无火，增之以水，则阴浓气弱，根损枝枯，不能华秀。春末失水，增之以火，则阳气太盛，燥渴相加，枝枯叶干，亦不华秀。
  是以水火二物，要得时相济为美。

- **分字分词释义**：
  - **渐有生长之象**：逐渐显现生长气象 / 春木复苏 / 阳气回升
  - **余寒**：冬季残留的寒气 / 初春气候 / 需火调候
  - **舒畅之美**：舒展畅达的美感 / 木得暖而条达 / 理想状态
  - **变克**：反变为克 / 水多寒木 / 适得其反
  - **重见生旺**：多次见到生旺之气 / 身极旺 / 比劫重重
  - **斲凿**：雕琢凿削 / 庚金修剪 / 成器之功
  - **楝梁**：栋梁 / 可用之材 / 大器之象
  - **阳壮水渴**：阳气强盛木口渴 / 春末需水 / 辰月气候
  - **花繁叶茂**：花朵繁盛叶片茂密 / 得水滋润 / 理想状态
  - **阴浓气弱**：阴气浓重气机虚弱 / 水多寒困 / 初春大忌
  - **得时相济**：按时节配合得当 / 调候关键 / 水火既济

- **规范化释义（primary_lang_explained）**：
  春天的甲木，逐渐有生长的气象。初春（寅月）还有余寒，应当用火（丙）来温暖，木才有舒畅条达的美感；如果水多，反而变成了克制（冻木），会损伤木的精神。如果木非常旺盛（重见比劫），必须用庚金来雕琢凿削，才能成为栋梁之材。
  春末（辰月）阳气壮大，木口渴，借助水（癸）来滋润扶持，就能花繁叶茂。
  初春如果没有火，反而增加水，就会阴气太重导致木气虚弱，根基受损枝叶枯萎，不能秀丽。春末如果失去水，反而增加火，就会阳气太盛，燥热干渴叠加，枝枯叶干，也不秀丽。
  所以水和火这两样东西，必须根据时节（初春/春末）配合得当（既济）才是好的。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in Spring shows signs of gradual growth. In Early Spring (Tiger month), there is still residual coldness; it should be warmed by Fire (Bing), giving it the beauty of comfort and expansion. If there is too much Water, it turns into restriction (freezing), damaging the Wood's spirit. If the Wood is heavily prosperous, Geng Metal must be used for carving and chiseling to make it into a ridgepole and beam (useful timber).
  In Late Spring (Dragon month), Yang energy is strong and the Wood is thirsty; borrowing Water for support makes flowers lush and leaves abundant.
  In Early Spring, if there is no Fire but Water is added, Yin becomes thick and Qi becomes weak, damaging roots and withering branches, preventing elegance. In Late Spring, if Water is lost and Fire is added, Yang becomes too excessive, adding dryness to thirst, creating withered branches and dry leaves, which is also not elegant.
  Therefore, Water and Fire must be balanced according to the specific timing to be excellent.

- **核心要点**：
  - **时节区分**：初春（寅）重火暖局；春末（辰）重水滋润。
  - **水火既济**：关键在于“得时”（Time-appropriate balance）。
  - **庚金用法**：仅在“重见生旺”（身极强）时使用，打造栋梁。

- **详细解说**：
  这段再次强调了春木的调候原则。
  - 初春（寅）：丙火第一（暖），癸水第二（润），忌水多。
  - 春末（辰）：癸水第一（润），丙火第二（暖/泄），忌火多。
  - 这里的“重见生旺”通常指支会木局或干透甲乙，此时必须用庚金（七杀）制身，即“羊刃驾杀”或“身杀两停”的格局。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_070]` `[trigger: 春甲调候]` `[factor_trigger: season_early_spring AND tiangan_jia AND tiangan_bing]` `[role: 主干]` 初春犹有余寒，当以火温暖，则有舒畅之美。 → 《穷通宝鉴·三春甲木》#3.1
  - `[ns_qttbj_071]` `[trigger: 春甲忌水多]` `[factor_trigger: season_early_spring AND tiangan_jia AND water_excessive]` `[role: 例外处理]` 水多变克，有损精神。 → 《穷通宝鉴·三春甲木》#3.1
  - `[ns_qttbj_072]` `[trigger: 春甲用庚]` `[factor_trigger: tiangan_jia AND wood_prosperous AND tiangan_geng]` `[role: 条件分支]` 重见生旺，必用庚金斲凿，可成楝梁。 → 《穷通宝鉴·三春甲木》#3.1
  - `[ns_qttbj_073]` `[trigger: 春末甲木]` `[factor_trigger: season_late_spring AND tiangan_jia AND tiangan_gui]` `[role: 条件分支]` 春末阳壮水渴，藉水资扶，则花繁叶茂。 → 《穷通宝鉴·三春甲木》#3.1
  - `[ns_qttbj_074]` `[trigger: 初春忌水]` `[factor_trigger: season_early_spring AND tiangan_jia AND NOT tiangan_bing AND water_excessive]` `[role: 例外处理]` 初春无火，增之以水，则阴浓气弱，根损枝枯。 → 《穷通宝鉴·三春甲木》#3.1
  - `[ns_qttbj_075]` `[trigger: 春末忌火多]` `[factor_trigger: season_late_spring AND tiangan_jia AND NOT element_water AND fire_excessive]` `[role: 例外处理]` 春末失水，增之以火，则阳气太盛，枝枯叶干。 → 《穷通宝鉴·三春甲木》#3.1
  - `[ns_qttbj_076]` `[trigger: 水火既济]` `[factor_trigger: principle_jiji AND element_water AND element_fire]` `[role: 总结]` 水火二物，要得时相济为美。 → 《穷通宝鉴·三春甲木》#3.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三春甲木总论"
    factor_refs: list = ['beauty_of_comfort', 'yin_thick_qi_weak', 'yang_strong_water_thirsty', 'ridgepole_beam']
    
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
        l1_anchor="qtbj_v1.0.0_1__三春甲木总论_001_L1",
    )
    version: str = "1.0.0"
