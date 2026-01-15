"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596995
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
    semantic_id="qtbj_v1.0.0_1__四月戊土_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1四月戊土巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  四月戊土，阳气发升，寒气内藏，外实内虚，不畏火炎，无阳气相催，万物不长，故先用甲疏噼，次取丙癸为佐。
  丙透甲出，廊庙之才，丙癸俱透，科甲之士，即透...
    """
    
    original_text: str = """- **原文（source_text）**：
  四月戊土，阳气发升，寒气内藏，外实内虚，不畏火炎，无阳气相催，万物不长，故先用甲疏噼，次取丙癸为佐。
  丙透甲出，廊庙之才，丙癸俱透，科甲之士，即透一位，支藏得所，终非白丁。
  若一派丙火，为火炎土燥，僧道之流，得一癸透壬藏，功名有准。或支藏癸水衣食充足，但骨肉多刑。
  化合成局无破，富贵非轻。

- **分字分词释义**：
  - **阳气发升**：阳气发散上升 / 巳月特点 / 火旺
  - **外实内虚**：外表强实内心空虚 / 土性 / 需疏
  - **疏噼**：疏通劈开 / 甲木作用 / 用神
  - **廊庙之才**：朝廷殿堂的人才 / 丙甲配合 / 大贵
  - **白丁**：平民百姓 / 无功名 / 凶象
  - **火炎土燥**：火焰土干燥 / 丙多无水 / 凶象
  - **骨肉多刑**：亲人多刑克 / 水火交战 / 凶象
  - **化合成局**：合化成局 / 戊癸化火 / 变格

- **规范化释义（primary_lang_explained）**：
  四月（巳月）的戊土，阳气发散上升，寒气内藏（土厚则寒？或指戊土本性），外实内虚，不畏惧火炎（巳月建禄），没有阳气（丙火）相催促，万物不能生长。所以先用甲木疏劈（灵动），其次取丙火癸水辅佐（丙暖癸润）。
  丙火透出甲木出干，是廊庙（朝廷）之才。丙火癸水都透出，是科甲之士。即使只透出一位，地支藏得其所，终究不是白丁。
  如果一派丙火，是“火炎土燥”，僧道之流。得到一个癸水透出、壬水藏支（制火润土），功名有准。如果地支藏癸水，衣食充足，但骨肉多刑克（水火交战）。
  如果化合成局（戊癸化火？生于巳月火旺，真化格）无破，富贵非轻。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the 4th Month (Snake Month): Yang Qi rises; Cold Qi is stored inside; it is solid outside but hollow inside. It does not fear blazing Fire. Without Yang Qi to urge it, things do not grow. Thus first use Jia to split/dredge, then take Bing/Gui to assist.
  If Bing and Jia are revealed, one is a talent for the Temple/Court. If Bing and Gui are both revealed, one is a scholar of Civil Service. Even if one is revealed and grounded in branches, one is not a commoner.
  If there is a mass of Bing Fire, it is "Blazing Fire Dry Earth", a monk/Taoist. Obtaining one Gui revealed and Ren hidden promises fame. If Gui is hidden in branches, food/clothing are sufficient, but flesh/blood (relatives) suffer punishment.
  If Transformation forms a pattern without breakage, wealth and nobility are significant.

- **核心要点**：
  - **首要用神**：甲木（疏劈）。巳月戊土建禄，身旺，喜杀（甲）。
  - **配合**：丙癸（既济）。
  - **火炎土燥**：丙多无水，孤贫。
  - **化火格**：戊癸化火，生于巳月，真化。

- **详细解说**：
  - 戊土在巳月是建禄（临官），气势强旺。
  - “外实内虚”：指土虽厚但无生气（若无木疏水润），故需甲木疏通。
  - “化合成局”：戊癸合火，巳月火当令，若地支火局，化气极真，贵。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_501]` `[trigger: 巳月戊土三用神]` `[factor_trigger: month_si AND tiangan_wu AND tiangan_jia AND tiangan_bing AND tiangan_gui]` `[role: 主干]` 四月戊土，阳气发升，先用甲疏噼，次取丙癸为佐。 → 《穷通宝鉴·三夏戊土》#22.1
  - `[ns_qttbj_502]` `[trigger: 丙甲廊庙才]` `[factor_trigger: month_si AND tiangan_wu AND tiangan_bing AND tiangan_jia AND court_talent]` `[role: 条件分支]` 丙透甲出，廊庙之才。 → 《穷通宝鉴·三夏戊土》#22.1
  - `[ns_qttbj_503]` `[trigger: 丙癸科甲士]` `[factor_trigger: month_si AND tiangan_wu AND tiangan_bing AND tiangan_gui AND kejia_scholar]` `[role: 条件分支]` 丙癸俱透，科甲之士。 → 《穷通宝鉴·三夏戊土》#22.1
  - `[ns_qttbj_504]` `[trigger: 火炎土燥僧道]` `[factor_trigger: month_si AND tiangan_wu AND fire_excessive AND NOT element_water AND monk_poor]` `[role: 例外处理]` 一派丙火，为火炎土燥，僧道之流。 → 《穷通宝鉴·三夏戊土》#22.1
  - `[ns_qttbj_505]` `[trigger: 癸透壬藏功名]` `[factor_trigger: month_si AND tiangan_wu AND tiangan_gui AND ren_in_branch AND fame_promised]` `[role: 条件分支]` 得一癸透壬藏，功名有准。 → 《穷通宝鉴·三夏戊土》#22.1
  - `[ns_qttbj_506]` `[trigger: 癸藏衣食足]` `[factor_trigger: month_si AND tiangan_wu AND gui_in_branch AND water_fire_conflict]` `[role: 条件分支]` 支藏癸水，衣食充足，但骨肉多刑。 → 《穷通宝鉴·三夏戊土》#22.1
  - `[ns_qttbj_507]` `[trigger: 化火格富贵]` `[factor_trigger: month_si AND tiangan_wu AND tiangan_gui AND dizhi_fire_frame AND pattern_transform_fire]` `[role: 总结]` 化合成局无破，富贵非轻。 → 《穷通宝鉴·三夏戊土》#22.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 四月戊土（巳月）"
    factor_refs: list = ['solid_outside_hollow', 'fire_scorching_earth']
    
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
        l1_anchor="qtbj_v1.0.0_1__四月戊土_巳月_001_L1",
    )
    version: str = "1.0.0"
