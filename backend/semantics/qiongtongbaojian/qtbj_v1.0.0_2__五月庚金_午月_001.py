"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578317
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
    semantic_id="qtbj_v1.0.0_2__五月庚金_午月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2五月庚金午月(SemanticEntry):
    """
    - **原文（source_text）**：
  五月庚金，丁火旺烈，庚金败地，专用壬水，癸又次之。
  壬透癸藏，支见庚辛，必然科甲，切忌戊己透干制水、则否。
  戊藏支内，不失儒林。
  或壬在支...
    """
    
    original_text: str = """- **原文（source_text）**：
  五月庚金，丁火旺烈，庚金败地，专用壬水，癸又次之。
  壬透癸藏，支见庚辛，必然科甲，切忌戊己透干制水、则否。
  戊藏支内，不失儒林。
  或壬在支，有金生助，又得金神出干，明经之贵。
  或癸出带辛，异路之荣。
  或支成火局，乏水者，奔波之客。有壬癸制者，捐纳之人。又见戊己透者则吉。无壬癸制火者，又宜戊己出干补金泄火，庶不夭折孤贫。
  总之，仲夏无水，必非上格，或一派木火，无伤、印、比劫，又作从杀而论。

- **分字分词释义**：
  - **五月**：午月 / 农历五月 / 丁火当令
  - **丁火旺烈**：丁火极旺猛烈 / 正官旺 / 杀重
  - **败地**：沐浴之地 / 庚金在午 / 气弱
  - **壬水**：阳水 / 食神 / 制杀用神
  - **制水**：克制水 / 枭神夺食 / 凶象
  - **儒林**：读书人 / 文士 / 功名
  - **金神**：庚辛金 / 比劫印绶 / 发水源
  - **明经**：贡生科名 / 功名 / 吉象
  - **奔波之客**：漂泊流浪 / 无定所 / 凶象
  - **捐纳**：捐钱买官 / 异途 / 次吉
  - **从杀**：从七杀格 / 弃命从杀 / 变格

- **规范化释义（primary_lang_explained）**：
  五月（午月）的庚金，丁火（正官）旺烈，庚金败地（沐浴），专用壬水（食神制杀），癸水（伤官）次之。
  壬水透出癸水藏支，地支见到庚辛金（帮身发水源），必然科甲。切忌戊己土透干制水（枭神夺食），否则不行。
  戊土藏在支内，不失为儒林（读书人）。
  如果壬水在支，有金生助，又得金神（庚辛）出干，是明经（贡生）之贵。
  如果癸水透出带辛金，异路之荣。
  如果地支合成火局（杀重），缺乏水者，奔波之客。有壬癸水制约者，捐纳之人。又见到戊己土透者则吉（泄火生身）。无壬癸水制火者，又适宜戊己土出干补金泄火，才不致夭折孤贫。
  总之，仲夏（午月）无水，必非上格。或者一派木火，无伤官、印绶、比劫，又作从杀格论。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 5th Month (Horse Month): Ding Fire is intensely prosperous; Geng is in "Bath/Defeat" land. Exclusively use Ren Water; Gui is secondary.
  If Ren reveals and Gui hides, with branches seeing Geng/Xin, Civil Service is certain. Avoid Wu/Ji revealing to control Water; that denies success.
  If Wu is hidden in branches, one remains a scholar.
  If Ren is in branches, supported by Metal, and Metal God reveals, one has the nobility of "Mingjing" (Tribute Student).
  If Gui reveals with Xin, alternative glory.
  If branches form a Fire Frame without Water, one is a wanderer. With Ren/Gui to control, one gains office via donation. Seeing Wu/Ji reveal is auspicious. Without Ren/Gui to control Fire, it is suitable for Wu/Ji to reveal to replenish Metal and leak Fire, avoiding early death and poverty.
  In summary, Mid-summer without Water is definitely not a High Pattern. Or if a mass of Wood/Fire, without Output, Seal, or Parallels, view as "Follow Killing".

- **核心要点**：
  - **首要用神**：壬水（反克）。午月火太旺，金太弱，非水不救。
  - **配合**：庚辛（发水源）。
  - **忌讳**：戊己制水。
  - **救应**：无水喜湿土（戊己泄火）。

- **详细解说**：
  - 午月庚金沐浴，正如“火中莲花”，极其脆弱。
  - 壬水食神制杀是最佳解药，所谓“水火既济”。
  - 若无水，必须用土泄火生金，否则金被熔化。
  - "从杀"：若全盘木火，无金水土，从杀反贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_340]` `[trigger: 庚生午月]` `[factor_trigger: month_wu AND tiangan_geng AND tiangan_ren]` `[role: 主干]` 五月庚金，丁火旺烈，庚金败地，专用壬水，癸又次之。 → 《穷通宝鉴·三夏庚金》#31.2
  - `[ns_qttbj_341]` `[trigger: 壬透癸藏]` `[factor_trigger: month_wu AND tiangan_geng AND ren_revealed AND gui_hidden AND (dizhi_shen OR dizhi_you)]` `[role: 条件分支]` 壬透癸藏，支见庚辛，必然科甲，切忌戊己透干制水。 → 《穷通宝鉴·三夏庚金》#31.2
  - `[ns_qttbj_342]` `[trigger: 火局无水]` `[factor_trigger: month_wu AND tiangan_geng AND dizhi_fire_frame AND NOT element_water]` `[role: 例外处理]` 或支成火局，乏水者，奔波之客。 → 《穷通宝鉴·三夏庚金》#31.2
  - `[ns_qttbj_343]` `[trigger: 仲夏无水]` `[factor_trigger: month_wu AND tiangan_geng AND NOT element_water]` `[role: 总结]` 总之，仲夏无水，必非上格。 → 《穷通宝鉴·三夏庚金》#31.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 五月庚金（午月）"
    factor_refs: list = ['mingjing_tribute', 'defeated_land']
    
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
        l1_anchor="qtbj_v1.0.0_2__五月庚金_午月_001_L1",
    )
    version: str = "1.0.0"
