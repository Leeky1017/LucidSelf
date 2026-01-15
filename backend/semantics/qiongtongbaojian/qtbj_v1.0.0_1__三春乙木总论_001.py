"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620016
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
    semantic_id="qtbj_v1.0.0_1__三春乙木总论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三春乙木总论(SemanticEntry):
    """
    - **原文（source_text）**：
  三春乙木，为芝兰蒿草之物，丙癸不可离也。春乙见丙，卉木向阳，万象回春，须癸滋养根基。
  丙癸齐透天干，无化合制克，自然登科及第。
  故书云：乙木根...
    """
    
    original_text: str = """- **原文（source_text）**：
  三春乙木，为芝兰蒿草之物，丙癸不可离也。春乙见丙，卉木向阳，万象回春，须癸滋养根基。
  丙癸齐透天干，无化合制克，自然登科及第。
  故书云：乙木根荄种得深，只须阳地不宜阴，漂浮只怕多逢水，克制何须苦用金。

- **分字分词释义**：
  - **芝兰蒿草**：芝兰草蒿一类植物 / 乙木取象 / 柔弱芬芳
  - **丙癸不可离**：丙火癸水不可缺少 / 太阳雨露 / 核心用神
  - **卉木向阳**：花草树木向着太阳 / 见丙吉象 / 万象回春
  - **滋养根基**：滋润养护根本 / 癸水功能 / 防燥
  - **登科及第**：科举考中功名 / 贵象 / 丙癸齐透
  - **根荄种得深**：根基种植得深 / 有根 / 稳固
  - **阳地**：阳气旺盛的地方 / 火运 / 宜行
  - **阴地**：阴气重的地方 / 水运 / 不宜

- **规范化释义（primary_lang_explained）**：
  春天的乙木，是芝兰、蒿草一类的植物，丙火（太阳）和癸水（雨露）是绝对不可离开的。春天的乙木见到丙火，叫“卉木向阳”，万象回春，但必须还要有癸水来滋养根基（防燥）。
  如果丙火和癸水一齐透出天干，且没有被合化或克制，自然能够登科及第。
  所以古书说：乙木的根基如果种得深（有根），只须运行阳地（火暖）不宜运行阴地（水寒），最怕遇到太多的水导致漂浮，至于克制（修剪），何必苦苦使用金呢（乙木柔弱，不喜金砍）？

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the Three Spring Months is like orchids and mugwort (delicate plants); Bing Fire and Gui Water are indispensable. When Spring Yi sees Bing, it is "Plants Facing the Sun", signifying the return of Spring to all things; yet it requires Gui to nourish the roots.
  If both Bing and Gui are revealed in the Heavenly Stems without being combined or controlled, one will naturally pass the Civil Service exams.
  Thus the book says: If Yi Wood's roots are planted deep, it only needs Yang lands (Fire) and not Yin lands (Water). It fears floating when meeting too much Water; as for control, why bother using Metal (since delicate wood doesn't need pruning)?

- **核心要点**：
  - **取象**：芝兰蒿草（Delicate Plants）。
  - **首要用神**：丙癸并用（Sun & Rain）。
  - **忌讳**：阴地（水多漂浮）、金（克制/乙木不喜斫削）。

- **详细解说**：
  乙木与甲木不同。甲木是栋梁，喜庚劈；乙木是花草，喜丙晒癸润。
  - “卉木向阳”是乙木最高格局，即见丙火。
  - 癸水润根，无癸则枯，无丙则腐。
  - “只须阳地不宜阴”：指运势喜火（阳）忌水（阴）。
  - “克制何须苦用金”：乙木柔弱，金克则伤，除特殊格局（如藤萝系甲或化金）外，一般不喜金。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_170]` `[trigger: 三春乙木]` `[factor_trigger: season_spring AND tiangan_yi AND tiangan_bing AND tiangan_gui]` `[role: 主干]` 三春乙木，为芝兰蒿草之物，丙癸不可离也。 → 《穷通宝鉴·三春乙木》#7.1
  - `[ns_qttbj_171]` `[trigger: 卉木向阳]` `[factor_trigger: season_spring AND tiangan_yi AND bing_revealed AND gui_revealed]` `[role: 主干依赖]` 春乙见丙，卉木向阳，万象回春，须癸滋养根基。 → 《穷通宝鉴·三春乙木》#7.1
  - `[ns_qttbj_172]` `[trigger: 乙木根荄]` `[factor_trigger: tiangan_yi AND yi_has_root AND likes_fire_luck AND fears_water_excess]` `[role: 总结]` 乙木根荄种得深，只须阳地不宜阴，漂浮只怕多逢水，克制何须苦用金。 → 《穷通宝鉴·三春乙木》#7.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三春乙木总论"
    factor_refs: list = ['plants_facing_sun', 'roots_rhizomes', 'orchids_mugwort']
    
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
        l1_anchor="qtbj_v1.0.0_1__三春乙木总论_001_L1",
    )
    version: str = "1.0.0"
