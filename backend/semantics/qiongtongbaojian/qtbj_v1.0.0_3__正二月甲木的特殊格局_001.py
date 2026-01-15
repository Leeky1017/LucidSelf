"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619808
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
    semantic_id="qtbj_v1.0.0_3__正二月甲木的特殊格局_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3正二月甲木的特殊格局(SemanticEntry):
    """
    - **原文（source_text）**：
  正二月甲木，素无取从才从杀从化之理。
  或一派庚辛，主一生劳苦，克子刑妻，再支会金局，非贫即夭。
  如无丙丁，一派壬癸，又无戊己制之，名水泛木浮，...
    """
    
    original_text: str = """- **原文（source_text）**：
  正二月甲木，素无取从才从杀从化之理。
  或一派庚辛，主一生劳苦，克子刑妻，再支会金局，非贫即夭。
  如无丙丁，一派壬癸，又无戊己制之，名水泛木浮，死无棺椁。
  如一派戊己，支会金局，为财多身弱，富屋贫人，终生劳苦，妻晚子迟。
  或无庚金，有丁透，亦属文星，为木火通明之象，又名伤官生财格，主聪明雅秀。一见癸水伤丁，但作厚道迂儒。
  或柱中多癸，滋助木神，伤灭丁火，其人奸雄枭险，曹操之徒，言清行浊，笑里藏刀。

- **分字分词释义**：
  - **素无**：向来没有 / 从不适用 / 绝对原则
  - **从才从杀从化**：从财格、从杀格、从化格 / 弃命从势 / 身弱之格
  - **一派庚辛**：满盘庚金辛金 / 七杀正官太重 / 克身太过
  - **克子刑妻**：子女受克、妻子受刑 / 六亲不和 / 凶象
  - **水泛木浮**：水太多木漂浮 / 无根无依 / 极凶格局
  - **死无棺椁**：死后没有棺材 / 极贫极凶 / 惨死之象
  - **富屋贫人**：住在富贵房子里的穷人 / 财多身弱 / 看得到吃不到
  - **木火通明**：木生火形成光明之象 / 文明秀气 / 贵格
  - **伤官生财**：伤官生财格 / 泄秀生财 / 聪明致富
  - **厚道迂儒**：老实但迂腐的读书人 / 癸克丁降格 / 次等文人
  - **奸雄枭险**：奸诈英雄、枭狠险恶 / 心术不正 / 曹操之流
  - **笑里藏刀**：表面和善内心险恶 / 伪善 / 癸多伤丁之象

- **规范化释义（primary_lang_explained）**：
  正月二月（寅卯月）的甲木，本气强旺，向来没有取从财、从杀、从化的道理。
  如果满盘庚金辛金，主一生劳苦，克子刑妻；再遇到地支会成金局，不是贫穷就是夭折。
  如果（金多）没有丙丁火制金，却见一派壬癸水，又没有戊己土制水，这叫“水泛木浮”，死后甚至没有棺椁（极凶）。
  如果满盘戊己土，地支会成金局，这是“财多身弱”，好比富屋里的穷人，终生劳苦，娶妻生子都很晚。
  如果（不用庚金），有丁火透出，也属于文星，构成“木火通明”之象，又叫“伤官生财格”，主聪明文雅秀气。一旦见到癸水伤害丁火，只能做个厚道迂腐的儒生。
  如果柱中癸水很多，过度生助木神，并伤灭了丁火，这人就是奸雄枭险之辈，像曹操一类，言语清高行为污浊，笑里藏刀。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 1st and 2nd Months (Tiger/Rabbit) is naturally strong and cannot follow Wealth, Killings, or Transformation patterns.
  If there is a mass of Geng/Xin Metal, it denotes a life of toil, harming children and punishing the wife; if the branches form a Metal frame, it means either poverty or premature death.
  If there is no Bing/Ding Fire (to control Metal) but a mass of Ren/Gui Water, and no Wu/Ji Earth to control the Water, it is called "Water Flooding Wood Floating", implying death without a coffin.
  If there is a mass of Wu/Ji Earth and branches form a Metal frame, it is "Abundant Wealth Weak Body" (Rich House Poor Man), denoting lifelong toil and late marriage/children.
  If there is no Geng Metal but Ding Fire is revealed, it is also a Star of Literature, forming the "Wood Fire Bright" image, also known as "Hurting Officer Generating Wealth", denoting intelligence and elegance. Once Gui Water appears to hurt Ding, one becomes merely a kind but pedantic scholar.
  If there are many Gui Waters in the pillars aiding the Wood spirit and extinguishing Ding Fire, the person is a treacherous hero, dangerous and deceitful like Cao Cao—speaking purely but acting dirtily, hiding a dagger in a smile.

- **核心要点**：
  - **不从原则**：寅卯月甲木身旺，不从势。
  - **金多之忌**：春木怕重金，无火制金为贫夭。
  - **水多之忌**：水泛木浮（死无棺椁）。
  - **土金交加**：财多身弱（富屋贫人）。
  - **木火通明**：无庚用丁，主文贵。
  - **枭印夺食**：癸多伤丁，主奸险伪诈。

- **详细解说**：
  这段列举了多种病态格局。
  - 春甲身旺，理论上可用杀（庚），但春金休囚，若金太重且无火制，则木被伤，反为“鬼”。
  - 若用丁泄秀（伤官），最怕癸水（枭神）夺食，这不仅影响贵气，更影响心性（笑里藏刀）。
  - “水泛木浮”是极凶格，指水多无土制，木漂流无依。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_081]` `[trigger: 春甲不从]` `[factor_trigger: (month_yin OR month_mao) AND tiangan_jia AND NOT pattern_follow]` `[role: 主干]` 正二月甲木，素无取从才从杀从化之理。 → 《穷通宝鉴·三春甲木》#3.3
  - `[ns_qttbj_082]` `[trigger: 春甲金多凶]` `[factor_trigger: (month_yin OR month_mao) AND tiangan_jia AND metal_excessive AND NOT element_fire]` `[role: 条件分支]` 一派庚辛，主一生劳苦，克子刑妻，支会金局，非贫即夭。 → 《穷通宝鉴·三春甲木》#3.3
  - `[ns_qttbj_083]` `[trigger: 水泛木浮]` `[factor_trigger: pattern_water_flood_wood_float AND water_excessive AND NOT element_earth]` `[role: 条件分支]` 一派壬癸，无戊己制之，名水泛木浮，死无棺椁。 → 《穷通宝鉴·三春甲木》#3.3
  - `[ns_qttbj_084]` `[trigger: 财多身弱]` `[factor_trigger: pattern_rich_house_poor_man AND earth_excessive AND dizhi_metal_frame]` `[role: 条件分支]` 一派戊己，支会金局，为财多身弱，富屋贫人。 → 《穷通宝鉴·三春甲木》#3.3
  - `[ns_qttbj_085]` `[trigger: 木火通明]` `[factor_trigger: pattern_wood_fire_bright AND tiangan_jia AND tiangan_ding AND NOT tiangan_geng]` `[role: 条件分支]` 无庚金，有丁透，为木火通明之象，主聪明雅秀。 → 《穷通宝鉴·三春甲木》#3.3
  - `[ns_qttbj_086]` `[trigger: 枭印夺食]` `[factor_trigger: owl_stealing_food AND tiangan_gui AND tiangan_ding]` `[role: 例外处理]` 癸水伤丁，但作厚道迂儒。 → 《穷通宝鉴·三春甲木》#3.3
  - `[ns_qttbj_087]` `[trigger: 枭印夺食]` `[factor_trigger: owl_stealing_food AND gui_excessive AND tiangan_ding]` `[role: 总结]` 柱中多癸，伤灭丁火，其人奸雄枭险，笑里藏刀。 → 《穷通宝鉴·三春甲木》#3.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 正二月甲木的特殊格局"
    factor_refs: list = ['pattern_water_flood_wood_float', 'pattern_rich_house_poor_man', 'pattern_wood_fire_bright', 'treacherous_hero', 'dagger_in_a_smile']
    
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
        l1_anchor="qtbj_v1.0.0_3__正二月甲木的特殊格局_001_L1",
    )
    version: str = "1.0.0"
