"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578483
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
    semantic_id="qtbj_v1.0.0_9__五月辛金_午月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 9五月辛金午月(SemanticEntry):
    """
    - **原文（source_text）**：
  五月辛金，丁火司权，辛金失令，阴柔之极，不宜煅炼，须己壬兼用，何也？己为泥沙，壬为湖海，己无壬不湿，辛无己不生，故壬己并用。无壬、癸亦可用。但癸力小。...
    """
    
    original_text: str = """- **原文（source_text）**：
  五月辛金，丁火司权，辛金失令，阴柔之极，不宜煅炼，须己壬兼用，何也？己为泥沙，壬为湖海，己无壬不湿，辛无己不生，故壬己并用。无壬、癸亦可用。但癸力小。或支成火局，即重见癸出亦不济，得壬透破火方可，必主生员。若无壬，癸见戊，虽有午宫己土，燥泥成灰，金必毁镕，反遭埋没，必为僧道。有一二重比肩，不致孤独。
  五月辛金，壬、癸、己、三者皆用。或壬己两透，支见癸水，不克，定主显达。即己藏支，亦有廪贡。或无壬有己，须得异途。或癸出有庚，必主衣锦，叨受恩荣。若水土多见，见甲方妙。
  庚辛生于夏月，要壬癸得地，若木多火多，不见金水，逢金水运必败。

- **分字分词释义**：
  - **阴柔之极**：阴柔达到极点 / 午月辛金 / 失令
  - **煅炼**：火炼金属 / 丁火克辛 / 不宜
  - **泥沙**：泥土沙石 / 己土 / 生金之本
  - **湖海**：湖泊大海 / 壬水 / 润土洗金
  - **壬己并用**：壬水己土一起用 / 用神配合 / 必须
  - **破火**：破除火势 / 壬水作用 / 制杀
  - **燥泥成灰**：干燥泥土变成灰 / 无壬见戊 / 凶象
  - **毁镕**：毁坏熔化 / 金受火害 / 凶象
  - **叨受恩荣**：承受皇恩荣耀 / 癸庚配合 / 吉象

- **规范化释义（primary_lang_explained）**：
  五月（午月）辛金丁火司权辛金失令阴柔之极不宜煅炼须己壬兼用。何也？己为泥沙壬为湖海己无壬不湿辛无己不生故壬己并用。无壬癸亦可用但癸力小。或支成火局即重见癸出亦不济得壬透破火方可必主生员。若无壬癸见戊虽有午宫己土燥泥成灰金必毁镕反遭埋没必为僧道。有一二重比肩不致孤独。
  五月辛金壬癸己三者皆用。或壬己两透支见癸水不克定主显达。即己藏支亦有廪贡。或无壬有己须得异途。或癸出有庚必主衣锦叨受恩荣。若水土多见见甲方妙。
  庚辛生于夏月要壬癸得地若木多火多不见金水逢金水运必败。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 5th Month (Horse Month): Ding Fire commanding Xin Metal losing-season yin-soft extreme not-suitable tempering must Ji/Ren both-use. Why? Ji as mud-sand Ren as lake-sea Ji without Ren not-wet Xin without Ji not-born therefore Ren/Ji together-use. Without Ren Gui also usable but Gui strength-small. Or branches form Fire Frame even重見Gui revealing also not-help gaining Ren revealing breaking Fire then-possible surely main scholar. If without Ren Gui見Wu although有Horse-palace Ji Earth dry-mud becoming-ash Metal surely destroyed-melted conversely buried surely monk/Taoist. Having 1-2重比肩 not致lonely.
  5th month Xin Metal Ren/Gui/Ji three all-use. Or Ren/Ji revealing branches見Gui Water not克 surely main prominent. Even Ji hidden branches also有廪贡. Or without Ren having Ji must-get alternative. Or Gui revealing having Geng surely main silk-robed receiving honors. If Water/Earth many-見 seeing Jia才妙.
  Geng/Xin born summer must Ren/Gui得地 if Wood-many Fire-many not見Metal/Water meeting Metal/Water luck必败.

- **核心要点**：
  - **首要用神**：壬己并用（湖海泥沙）
  - **配合**：癸水辅助庚金
  - **午月特点**：丁火司权阴柔之极不宜煅炼需壬己并用

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_418]` `[trigger: 辛生午月]` `[factor_trigger: month_wu AND tiangan_xin AND tiangan_ji AND tiangan_ren]` `[role: 主干]` 五月辛金，丁火司权，辛金失令，阴柔之极，不宜煅炼，须己壬兼用。 → 《穷通宝鉴·三夏辛金》#34.9
  - `[ns_qttbj_419]` `[trigger: 壬己并用]` `[factor_trigger: month_wu AND tiangan_xin AND ji_ren_combined AND mud_sand_lake_sea]` `[role: 主干依赖]` 己为泥沙，壬为湖海，己无壬不湿，辛无己不生，故壬己并用。 → 《穷通宝鉴·三夏辛金》#34.9
  - `[ns_qttbj_420]` `[trigger: 燥泥成灰]` `[factor_trigger: month_wu AND tiangan_xin AND NOT tiangan_ren AND tiangan_wu AND dry_mud_ash]` `[role: 例外处理]` 若无壬，癸见戊，虽有午宫己土，燥泥成灰，金必毁镕，必为僧道。 → 《穷通宝鉴·三夏辛金》#34.9
  - `[ns_qttbj_422]` `[trigger: 夏金通则]` `[factor_trigger: season_summer AND (tiangan_geng OR tiangan_xin) AND ren_gui_rooted]` `[role: 总结]` 庚辛生于夏月，要壬癸得地，若木多火多，不见金水，逢金水运必败。 → 《穷通宝鉴·三夏辛金》#34.9"""
    normalized_text_zh: str = """"""
    subject: str = "9. 五月辛金（午月）"
    factor_refs: list = ['ren_ji_together_use', 'dry_mud_ash']
    
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
        l1_anchor="qtbj_v1.0.0_9__五月辛金_午月_001_L1",
    )
    version: str = "1.0.0"
