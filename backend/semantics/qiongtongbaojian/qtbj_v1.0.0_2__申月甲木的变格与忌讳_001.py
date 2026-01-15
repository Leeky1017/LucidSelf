"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619916
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
    semantic_id="qtbj_v1.0.0_2__申月甲木的变格与忌讳_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2申月甲木的变格与忌讳(SemanticEntry):
    """
    - **原文（source_text）**：
  或四柱庚旺，支内水多，不作弃命从杀。见土多可作从才而看。
  庚多无癸，而壬水多，戊己亦多，此则专用一点丁火，方可制金以养群土，此命大富。丁藏富小，不...
    """
    
    original_text: str = """- **原文（source_text）**：
  或四柱庚旺，支内水多，不作弃命从杀。见土多可作从才而看。
  庚多无癸，而壬水多，戊己亦多，此则专用一点丁火，方可制金以养群土，此命大富。丁藏富小，不显。丁露定作富豪。得二丁，不坐死绝，必然富贵双全，即风水不及，亦可富中取贵，纳粟奏名。
  或癸叠叠制伏丁火，虽满腹文章，终难显达。得运行火土，破癸，略可假就功名，岁运皆背，刀笔之徒。
  支成水局，戊己透干，制去癸水，存其丁火又可云科甲，但此等命，主为人心奸巧诈，好讼争非，因贪致祸。奸险之徒，决非安份之人也。

- **分字分词释义**：
  - **弃命从杀**：放弃自身从属于七杀 / 变格 / 身极弱杀极旺
  - **从才**：从财格 / 身弱财旺 / 变格
  - **制金养土**：制服金气滋养土 / 丁火功能 / 富象
  - **纳粟奏名**：捐献粮食换取功名 / 买官 / 富中取贵
  - **癸叠叠**：癸水重重叠叠 / 枭神太旺 / 克丁之象
  - **满腹文章**：才华横溢 / 有才无运 / 被制之象
  - **刀笔之徒**：擅长文笔诉讼的小吏 / 讼师 / 下等人物
  - **奸巧诈**：奸诈巧伪 / 心术不正 / 水局特征
  - **好讼争非**：喜欢诉讼争是非 / 性格缺陷 / 凶象

- **规范化释义（primary_lang_explained）**：
  如果四柱庚金旺，地支水多（泄金），不能作弃命从杀格论。如果见到土多，可以当作从财格看。
  如果庚金多而没有癸水，但是壬水多，戊己土也多，这种情况必须专用一点丁火，制住金气并生养群土，这命主大富。丁火藏支则富小且不显赫，丁火透出定是大富豪。如果得到两个丁火，且不坐在死绝之地，必然富贵双全，即使风水不及，也能富中取贵，捐官得名。
  如果癸水重叠制伏丁火（枭神夺食），虽然满腹文章，终究难以显达。如果运行火土运破除癸水，勉强可以获得功名；如果岁运都背逆，只是个刀笔吏（讼师）。
  如果地支合成水局，戊己土透出制去癸水，保存了丁火，又可以说有科甲，但这种命造，主为人奸诈巧伪，喜欢诉讼争是非，因为贪婪招致祸患。是奸险之徒，决不是安分的人。

- **完整对等诠释（secondary_lang_full）**：
  If the pillars have prosperous Geng but abundant Water in branches, it is not "Abandon Life Follow Killing" (as Water supports Wood). If abundant Earth is seen, it can be viewed as "Follow Wealth".
  If Geng is numerous without Gui, but Ren and Wu/Ji are numerous, one must exclusively use a bit of Ding Fire to control Metal and nourish the Earths; this life is greatly wealthy. If Ding is hidden, wealth is small; if revealed, a tycoon. With two Dings not in death stages, wealth and nobility are complete.
  If layers of Gui Water suppress Ding Fire (Owl steals Food), despite a belly full of essays, one will hard to achieve prominence. If Luck runs through Fire/Earth to break Gui, one might barely achieve fame. If Luck is adverse, one is merely a "Knife and Pen disciple" (petty clerk).
  If branches form a Water frame and Wu/Ji are revealed to control Gui and save Ding, one can speak of Civil Service. But such a life implies a treacherous and deceitful heart, loving litigation and conflict, courting disaster through greed. A dangerous person, definitely not law-abiding.

- **核心要点**：
  - **从杀失效**：见水泄金生木，不从杀。
  - **从财条件**：见土多。
  - **伤官生财**：庚多土多壬多，用丁制金生土，主富。
  - **枭印夺食**：癸叠制丁，难显达，刀笔吏。
  - **水局制枭**：戊制水存丁，虽贵但心术不正（奸诈好讼）。

- **详细解说**：
  申月本气七杀，最喜丁火。
  - 若见癸水（印），虽能化杀，但会伤丁（食神），导致秀气受损，格局由“贵”转为“富”或“吏”。
  - “刀笔之徒”形象地描绘了有才华（木火）但被压制（癸水）且心性阴暗（印多坏食）的人。
  - “纳粟奏名”指买官，说明其贵气不足，需用钱买。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_133]` `[trigger: 申月从杀]` `[factor_trigger: month_shen AND tiangan_jia AND metal_prosperous AND water_in_branches]` `[role: 主干]` 四柱庚旺，支内水多，不作弃命从杀。 → 《穷通宝鉴·三秋甲木》#5.2
  - `[ns_qttbj_134]` `[trigger: 申月大富]` `[factor_trigger: month_shen AND tiangan_jia AND metal_excessive AND tiangan_ren AND element_earth AND tiangan_ding]` `[role: 条件分支]` 庚多无癸，而壬水多，戊己亦多，专用一点丁火，制金以养群土，此命大富。 → 《穷通宝鉴·三秋甲木》#5.2
  - `[ns_qttbj_135]` `[trigger: 枭神夺食]` `[factor_trigger: month_shen AND tiangan_jia AND gui_excessive AND tiangan_ding]` `[role: 例外处理]` 癸叠叠制伏丁火，虽满腹文章，终难显达，刀笔之徒。 → 《穷通宝鉴·三秋甲木》#5.2
  - `[ns_qttbj_136]` `[trigger: 奸诈好讼]` `[factor_trigger: month_shen AND tiangan_jia AND dizhi_water_frame AND (tiangan_wu OR tiangan_ji) AND tiangan_ding]` `[role: 总结]` 支成水局，戊己透干制癸存丁，主为人心奸巧诈，好讼争非。 → 《穷通宝鉴·三秋甲木》#5.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 申月甲木的变格与忌讳"
    factor_refs: list = ['knife_pen_disciple', 'donate_grain_for_title', 'belly_full_of_essays']
    
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
        l1_anchor="qtbj_v1.0.0_2__申月甲木的变格与忌讳_001_L1",
    )
    version: str = "1.0.0"
