"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.080976
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
    semantic_id="smth_v1.0.0_1_富贵贫贱与五行气数_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1富贵贫贱与五行气数(SemanticEntry):
    """
    - 原文（source_text）：
  人生有命，得失顿殊；富贵贫贱，那能一体。
  红光满室，五行都聚于贵乡；佳气充庐，四柱并集于福地。
  先贫后富，生时值禄马同乡；始吉终凶，日时犯空破之处。
...
    """
    
    original_text: str = """- 原文（source_text）：
  人生有命，得失顿殊；富贵贫贱，那能一体。
  红光满室，五行都聚于贵乡；佳气充庐，四柱并集于福地。
  先贫后富，生时值禄马同乡；始吉终凶，日时犯空破之处。
  平生坎坷，基薄与凶运交杂；一世荣华，命高逢好运叠至。
  刚金遇火方成器，决定超群；旺火得水为既济，必然出众。
  木须金而不繁，水赖土而不散。
  戊己见寅卯，得位于勾陈；壬癸坐巳午，当权于元武。
  贵神入命，遇奇仪必是公卿；华盖临时，值孤寡定为僧道。
  玉堂拜相，炎炎火秀在离宫；金阙朝元，洋洋水德宅坎位。
  重逢水位，断为云水之仙；累犯纯阳，定作空门之子。
  遇长生而聪明智慧，逢死败而蒙蠢愚顽。
  父母难靠，年月俱陷空亡；妻子易亏，日时并临孤寡。

- 分字分词释义：
  - **禄马同乡**：壬午、癸巳等。
  - **奇仪**：三奇六仪（遁甲术语，此处指三奇贵人）。
  - **勾陈得位**：土生木月（寅卯），官煞得地。
  - **元武当权**：水生火月（巳午），财官得地。
  - **火秀离宫**：火得地（午）。
  - **水德坎位**：水得地（子）。

- 规范化释义（primary_lang_explained）：  
  本段从“人生有命，得失顿殊；富贵贫贱，那能一体”落笔，指出命中贵贱差别，并非一句“命好命坏”可以概括，而是看五行气数能否聚于贵乡福地。原局中财、官、印、食等用神分布得地，又能在四柱之间相互呼应时，就如“红光满室”“佳气充庐”，象征物质、权力与声望都进入良性循环；若只是零散之气不成局，或基础本就薄弱又反复行到凶运，便容易应在“基薄与凶运交杂”的一生，多是辛劳坎坷。相反，命格本身厚重，再逢好运叠至，则是“命高逢好运叠至”，一世荣华。  
  赋文又通过“禄马同乡”“空亡”“长生死败”等节点，讲明时间节奏与位置配合的重要：生时值禄马同乡者，多主先贫后富，早年辛劳铺垫，晚景方见回报；若日时落在空亡、死败之处，或被冲破用神，则常见“始吉终凶”，开局不差却难以善终。对六亲而言，年月俱陷空亡，多象征父母难以依靠；日时并临孤寡、元辰，则配偶与子女宫受损。至于“刚金遇火方成器，旺火得水为既济；木须金而不繁，水赖土而不散”，则说明五行只有在合适的对宫或对宫之气中才能“成器”：金旺得火，以冶炼成器；火旺得水，水火既济；木盛得金，不再枝叶横生而成为可用之材；水盛得土，则不致泛滥，而能归库有主。  
  后半篇以贵神、奇仪、华盖、云水等象，勾勒出从公卿权贵到僧道云水的不同去向：戊己日主生于寅卯木旺之月，为“勾陈得位”，象征官煞有根、职位得当；壬癸日主坐巳午火旺之乡，为“元武当权”，象征财官得地，既能掌财又能掌势。命带贵神奇仪，再得吉运引发，多应公卿权贵之命；华盖重而孤寡并见、又逢重重空亡与纯阳，则多走出家清修之路，成为“云水之仙”“空门之子”。火在离宫为文明之象，水在坎位为润下之德，配合前文的长生与死败，构成一整套关于富贵贫贱、显达与出世的五行去向地图。  

- 完整对等诠释（secondary_lang_full）：  
  This section opens by stating that wealth and poverty, honour and lowliness, are far from uniform; what truly differentiates destinies is whether the Five Elements gather in noble, supportive positions. When Wealth, Office, Seals and productive Food Spirits all occupy dignified places and echo one another across the Four Pillars, the chart resembles a house filled with rosy light and auspicious qi—material conditions, status and reputation reinforce one another in a virtuous cycle. If, by contrast, these indications are scattered, contradictory or weak, or if a fragile natal structure repeatedly runs into harsh luck cycles, the result tends toward a life in which "thin foundations" mix with "malefic运", marked by toil and setbacks. A strong configuration that is repeatedly met by favourable运, on the other hand, describes someone whose "noble命" is backed by recurring opportunities, allowing a lifetime of flourishing.  
  The text also highlights how timing and placement co‑determine outcomes. When the Day and Hour pillars form a "salary and Horse in the same neighbourhood" pattern, early hardship often gives way to late prosperity; the person spends the first part of life building a base and only reaps abundant returns later on. If those same positions fall into void, death or defeat stages, or if they are violently disrupted, the pattern can flip to "good beginnings but poor endings": promising starts that cannot be carried through. In terms of kinship, voided year and month pillars frequently point to parents who are unreliable or absent, while lonely, solitary or calamity indicators on the day and hour often damage the spouse and children. The formulae about strong Metal meeting Fire, blazing Fire receiving Water, luxuriant Wood encountering Metal, and surging Water relying on Earth all reinforce a single idea: each element must find its proper counterpart to become "a crafted vessel" or a completed state of "crossed and completed".  
  Finally, the ode uses a network of spirit names and star images—Gouchen gaining position, Yuanwu holding power, noble spirits and auspicious configurations, Huagai and the wandering "water cloud" immortal—to map out divergent life paths. Earth Day Masters born in Wood‑prosperous months are said to give Officials real footing; Water Day Masters seated in Fire‑prosperous branches are portrayed as holding both wealth and authority. Charts graced by noble spirits and refined configurations, and then reinforced by good运, tend toward ministerial, courtly or high administrative roles. Charts dominated by emptiness, repeated solitary and calamity signs, heavy Huagai and pure Yang with little worldly support, incline instead toward monastic or wandering religious lives, "cloud‑and‑water immortals" and "children of the gate of emptiness". Fire shining in the Li palace evokes culture and civilisation; Water abiding in the Kan position suggests depth and receptivity. Together with the life‑and‑death stages, these images sketch a complete diagram of how the Five Elements can manifest as high or low station, worldly success or spiritual withdrawal.  

- 核心要点：
  - **五行成器**：金火、水火、木金、水土。
  - **神煞定业**：奇仪公卿，华盖僧道。
  - **六亲**：空亡孤寡。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_017]` `[trigger: 红光满室]` `[factor_trigger: hongguang_manshi AND wuxing_juguixiang]` `[role: 主干]` 红光满室，五行都聚于贵乡；佳气充庐，四柱并集于福地。 → 《三命通会》卷十二#富贵贫贱与五行气数
  - `[ns_smth_12_018]` `[trigger: 刚金遇火]` `[factor_trigger: gangjin_yuhuo AND wanghuo_deshui]` `[role: 主干依赖]` 刚金遇火方成器，决定超群；旺火得水为既济，必然出众。 → 《三命通会》卷十二#富贵贫贱与五行气数
  - `[ns_smth_12_019]` `[trigger: 贵神奇仪]` `[factor_trigger: guishen_qiyi AND huagai_sengdao]` `[role: 条件分支]` 贵神入命，遇奇仪必是公卿；华盖临时，值孤寡定为僧道。 → 《三命通会》卷十二#富贵贫贱与五行气数
  - `[ns_smth_12_020]` `[trigger: 长生死败]` `[factor_trigger: changsheng_sibai AND congming_yuchun]` `[role: 总结]` 遇长生而聪明智慧，逢死败而蒙蠢愚顽。 → 《三命通会》卷十二#富贵贫贱与五行气数"""
    normalized_text_zh: str = """"""
    subject: str = "1 富贵贫贱与五行气数"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_wuxing_2', 'wealth_officer_seal_food_in_noble_positions', 'bazi_state_factor_98', 'bazi_semantic', 'bazi_state_factor_99', 'bazi_semantic', 'bazi_relation_metal_fire_wood_water_relation', 'bazi_semantic', 'bazi_relation_factor_42', 'bazi_semantic', 'bazi_relation_factor_43', 'bazi_semantic', 'source_ref', 'rel_smth_12_019', 'core_factor', 'rel_smth_12_020', 'cond_factor', 'rel_smth_12_021', 'risk_factor', 'evi_smth_12_019', 'core_factor', 'rule_name19', 'evi_smth_12_020', 'cond_factor', 'rule_name20', 'evi_smth_12_021', 'risk_factor', 'rule_name21', 'map_smth_12_013', 'map_smth_12_014']
    
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
        l1_anchor="smth_v1.0.0_1_富贵贫贱与五行气数_001_L1",
    )
    version: str = "1.0.0"
