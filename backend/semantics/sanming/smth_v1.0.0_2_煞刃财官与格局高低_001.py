"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.080872
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
    semantic_id="smth_v1.0.0_2_煞刃财官与格局高低_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2煞刃财官与格局高低(SemanticEntry):
    """
    - 原文（source_text）：
  煞无刃不威，刃无煞不显。权刃双显均停，位至王侯；刃煞轻重无制，身为胥吏。
  生平富而且贵，煞重身柔，中途忽死；或危运扶干旺，处身僧道之首。
  用煞反轻，受...
    """
    
    original_text: str = """- 原文（source_text）：
  煞无刃不威，刃无煞不显。权刃双显均停，位至王侯；刃煞轻重无制，身为胥吏。
  生平富而且贵，煞重身柔，中途忽死；或危运扶干旺，处身僧道之首。
  用煞反轻，受职台谏之除；偏官得地，岂知大贵者用财而不用官。
  当权者用煞而不用印，印赖煞生，官因财旺。
  五行消息，元理可知；四柱推明，用神可见。
  食居先，煞居后，功名两全；酉破卯，卯破午，财官双美。
  享福五行归禄，眉寿八字相停。
  晦火无光于稼穑，盗木多困于丙丁。
  火虚有焰，金实无声。
  水泛木浮者活木，土重金埋者阳金。水盛则危，火明则灭。
  阳金得炼太过，变革奔波；阴木归垣失令，终为身弱。

- 分字分词释义：
  - **煞刃均停**：七煞与羊刃力量相当。
  - **食居先**：食神在年或月。
  - **煞居后**：七煞在时。
  - **酉破卯，卯破午**：地支相破，却能破出财官（如卯破午，午中丁己为财官）。
  - **晦火**：土多晦火。
  - **盗木**：火多泄木。
  - **活木**：甲木。
  - **阳金**：庚金。

- 规范化释义（primary_lang_explained）：  
  本段从“煞无刃不威，刃无煞不显”开篇，把七煞和羊刃视为同一股猛烈力量的两端：七煞像军令与外来压力，羊刃则像手中利器与自身锋芒。只有当两者力量相当、互为倚托时，才成“权刃双显均停”的高格，可以承担兵权、刑权等极端职位；若煞重身轻、或刃重煞轻，又缺乏食神、印绶的调剂，便容易从“威权”滑向“横暴”或“中途忽死”的凶象，甚至在危运中因身煞相战而以僧道之身收场。  
  文中进一步用“食居先，煞居后”“酉破卯，卯破午”“五行归禄”等句，把煞刃与食神、归禄、财官的排序讲清：食神在先、七煞在后，代表以柔克刚、以才华和恩惠化解压力，既保功名又保性命；酉破卯、卯破午一类“破中取用”，强调有时必须承认冲破与损伤，才能把藏在地支中的财官唤出为我所用；而日禄归时、五行相停则是全段的终点——一切煞刃财官，归根结底都要落到“中和有禄”的结果，否则不是短寿，就是劳而无功。  

- 完整对等诠释（secondary_lang_full）：  
  This section begins with the statement that "without Blade, Killing has no awe; without Killing, Blade does not stand out," treating Seven Killings and Yang Blade as two faces of the same fierce potential. Killing represents command, danger and pressure from outside; Blade represents the edge of the self, courage and readiness to act. Only when the two are of comparable strength and properly harnessed does the configuration of "balanced authority and Blade" arise, fit to wield military or judicial power. When Killing is heavy and the body weak, or Blade is heavy and Killing shallow, and there is no moderating Food God or Seal, the pattern tilts toward violence, sudden death, or retreat into monastic leadership under the strain of harsh luck cycles.  
  Later lines such as "Food resides first, Killing last," "You breaks Mao, Mao breaks Wu," and "enjoying blessings when the Five Elements return to salary" spell out how these forces should be sequenced. Food God placed earlier and Killing later symbolises using gentleness, talent and generosity to tame harshness, preserving both career and life. The seemingly destructive clashes that "break" Mao and Wu are re‑read as ways of uncovering hidden Wealth and Office in the branches, provided the overall structure can absorb the blow. The motif of returning to禄—Day Master meeting its own place of salary—summarises the teaching: whatever mix of Killing, Blade, Wealth and Office one holds, the chart is judged by whether it can stabilise into a balanced, life‑supporting pattern rather than remaining locked in excess and imbalance.  

- 核心要点：
  - **煞刃驾杀**：威权。
  - **食神制煞**：先食后煞。
  - **归禄长寿**：中和。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_005]` `[trigger: 煞无刃不威]` `[factor_trigger: shawuren_buwei AND quanren_junting]` `[role: 主干]` 煞无刃不威，刃无煞不显。权刃双显均停，位至王侯。 → 《三命通会》卷十二#煞刃财官与格局高低
  - `[ns_smth_12_006]` `[trigger: 食先煞后]` `[factor_trigger: shixian_shahou AND gongming_liangquan]` `[role: 主干依赖]` 食居先，煞居后，功名两全；酉破卯，卯破午，财官双美。 → 《三命通会》卷十二#煞刃财官与格局高低
  - `[ns_smth_12_007]` `[trigger: 晦火盗木]` `[factor_trigger: huihuo_wuguang AND daomu_duokun]` `[role: 条件分支]` 晦火无光于稼穑，盗木多困于丙丁。火虚有焰，金实无声。 → 《三命通会》卷十二#煞刃财官与格局高低
  - `[ns_smth_12_008]` `[trigger: 五行归禄]` `[factor_trigger: wuxing_guilu AND meishou_bazi_xiangting]` `[role: 总结]` 享福五行归禄，眉寿八字相停。 → 《三命通会》卷十二#煞刃财官与格局高低"""
    normalized_text_zh: str = """"""
    subject: str = "2 煞刃财官与格局高低"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_34', 'bazi_semantic', 'bazi_state_factor_94', 'bazi_semantic', 'bazi_relation_shishen', 'food_before_killing', 'bazi_relation_relation_1', 'break_branch_to_use_hidden_stems', 'bazi_condition_wuxing_condition', 'return_to_salary_with_balance', 'bazi_factor_37', 'bazi_semantic', 'source_ref', 'rel_smth_12_004', 'core_factor', 'rel_smth_12_005', 'cond_factor', 'rel_smth_12_006', 'risk_factor', 'evi_smth_12_004', 'core_factor', 'rule_name4', 'evi_smth_12_005', 'cond_factor', 'rule_name5', 'evi_smth_12_006', 'risk_factor', 'rule_name6', 'map_smth_12_003', 'map_smth_12_004']
    
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
        l1_anchor="smth_v1.0.0_2_煞刃财官与格局高低_001_L1",
    )
    version: str = "1.0.0"
