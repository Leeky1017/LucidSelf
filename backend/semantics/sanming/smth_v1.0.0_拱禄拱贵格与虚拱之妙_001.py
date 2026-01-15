"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412362
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
    semantic_id="smth_v1.0.0_拱禄拱贵格与虚拱之妙_001",
    book_id="sanming",
    engine_id="bazi"
)
class 拱禄拱贵格与虚拱之妙(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：拱禄拱贵，填实则凶。“拱”，向也，夹也。禄是临官之禄，贵是官星之贵，或指天乙贵人。

  拱禄有五日五时：癸亥、癸丑，癸丑、癸亥拱子禄...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：拱禄拱贵，填实则凶。“拱”，向也，夹也。禄是临官之禄，贵是官星之贵，或指天乙贵人。

  拱禄有五日五时：癸亥、癸丑，癸丑、癸亥拱子禄；丁巳、丁未，己未、己巳拱午禄；戊辰、戊午拱巳禄。

  拱贵有五日五时：甲申、甲戌拱酉，乙未、乙酉拱申，是官贵；甲寅、甲子拱丑，戊申、戊午拱未，辛丑、辛卯拱寅，官贵兼天乙贵。

  凡拱格，须日时同干，贵禄与月令通气，运行身旺及贵禄旺地，方大好；印绶、伤官、食神、财运，亦吉。忌刑冲破害、羊刃七煞，伤了日时，拱不住贵气。大忌填实、空亡，譬如器皿空则能容，实则无用，所以只宜虚拱；完则能盛，破则无用，所以怕见空亡。岁运同。

  《赋》云：禄重位显，定知夹禄之乡。假如癸丑见癸亥，拱子位，癸禄生秋冬，禄重有气。又如戊子见甲寅，亦拱丑贵，然戊受甲克，岂能拱之？余以例推。《三命》云：夹禄夹贵，必居八座之尊。《景鉴》云：拱禄拱贵，纯粹者王侯之伦，填实者虚名虚利；无财印不喜伤害，忌官煞，又怕空亡。

  诗曰：日时双拱禄中庭，金匮藏珠格最清，至贵至高君子命，无忧无虑到公卿。又：虚拱贵神兼禄位，不逢填实及空亡，冲刑羊刃并七煞，破败官星不可当。又：拱禄拱贵格中稀，也须月令看支提，提纲有用提纲重，月令无神用此奇。

- 分字分词释义：

  - 拱：向、夹之意，指日支与时支夹着中间之支而起用。
  - 禄：日干的临官、禄地，如子为癸禄、午为丁己禄、巳为戊禄等。
  - 贵：可以指官星之贵，也可指天乙贵人等贵神。
  - 日时同干：日柱与时柱天干相同，是拱格的前提条件之一。
  - 虚拱：中间被拱之位空而不填，象如器皿空以能容，拱出的禄贵得以显用。
  - 填实：中位被实际支神占据，致拱势被截断或贵禄被占，不利成格。
  - 八座之尊：古人对高位宰辅的形容，这里借以形容拱禄拱贵格的高贵程度。

- **规范化释义（primary_lang_explained）**：

  拱禄拱贵格，以“日时同干、夹拱中位之禄或贵”为名。日支与时支如两手，夹住中间的禄位或贵位，使该处气势被日主所用。拱禄的五组日时，主以禄为核心；拱贵的五组日时，则以官星或天乙贵人为核心。

  本格最忌“填实”：一旦中间禄位或贵位被实际支神占据，等于器皿已满，拱势难以再容；同时也忌刑冲破害、羊刃七煞等打破两端支神的平衡，使本来要被“夹拱”的贵禄之气四散。只有在日时同干、月令与贵禄通气、身旺而岁运又行贵禄旺地时，拱格才真正能够“夹禄夹贵、居八座之尊”。

- 核心要点：

  - 拱禄拱贵以“日时同干、夹拱中位禄贵、虚拱不填”为三大条件。
  - 月令须与拱出的禄贵通气，岁运又行身旺与贵禄旺地，方能登高位。
  - 填实、空亡、刑冲、羊刃七煞等，都会削弱或破坏拱格，轻则虚名虚利，重则不入格。
  - 判断时要看拱出的究竟是禄、官，还是天乙贵人，并结合整体格局以定“富贵、清浊”。

- 详细解说：

  拱禄拱贵与前文“日禄归时”“冲禄”等同属“用禄”的格局，但用法不同：

  - 日禄归时侧重“禄位移至时支”；
  - 拱禄拱贵则侧重“日时两端夹拱中位”。

  这类格局体现的是一种“间接掌权”的象：日干并不直接坐在禄位或贵位上，而是通过日支与时支的夹拱，让中间之位为我所用。原文以癸亥见癸丑拱子禄为例说明：癸禄在子，两癸分别坐亥、丑，中间子位虚拱，禄气重叠而不杂；若改作戊子见甲寅拱丑贵，则因戊受甲克，力量相反，“岂能拱之”，正好说明拱格要兼顾干支生克，而非只看形式。

- **校勘与字词辨析（双语）**：

  - 原文将“拱”释为“向、夹”，本稿沿用，并在释义中明确为“日支、时支夹拱中位”。
  - “填实则凶”一语，本稿在白话与详细解说中用“器皿空则能容，实则无用”的比喻加以解释，保持原意不变。
  - 《三命》《景鉴》等书中关于“夹禄夹贵”“纯粹者王侯之伦”的评价，本稿择要引用，以提示本格在古人命理体系中的地位，但不在 L1 层做更多延伸。
  - **English**：
    - The original text interprets "embrace" as "facing, flanking"; this edition follows it and clarifies as "day-branch and hour-branch flanking the middle position."
    - The phrase "filling makes it inauspicious" is explained with the metaphor "an empty vessel can contain, a full one is useless"; the original meaning is preserved.
    - Evaluations from Sanming and Jingjian about "flanking salary, flanking noble" and "the pure ones are of princely rank" are selectively quoted to indicate this pattern's status; not expanded in L1.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_049]` `[trigger: 拱禄拱贵定义]` `[factor_trigger: gonglu_gonggui_presence]` `[role: 主干]` 拱禄拱贵，填实则凶。 → 《三命通会》卷六#拱禄拱贵
  - `[ns_smth_06_050]` `[trigger: 日时同干]` `[factor_trigger: ri_shi_tong_gan AND gui_lu_tongqi]` `[role: 主干依赖]` 凡拱格，须日时同干，贵禄与月令通气。 → 《三命通会》卷六#拱禄拱贵
  - `[ns_smth_06_051]` `[trigger: 忌填实空亡]` `[factor_trigger: ji_tianshi OR ji_kongwang]` `[role: 条件分支]` 忌刑冲破害、羊刃七煞，伤了日时，拱不住贵气。大忌填实、空亡。 → 《三命通会》卷六#拱禄拱贵
  - `[ns_smth_06_052]` `[trigger: 无忧到公卿]` `[factor_trigger: wu_you_dao_gongqing]` `[role: 总结]` 日时双拱禄中庭，金匮藏珠格最清，至贵至高君子命，无忧无虑到公卿。 → 《三命通会》卷六#拱禄拱贵

- **完整对等诠释（secondary_lang_full）**：
  The "Embracing Salary, Embracing Noble" pattern is formed when the day and hour pillars share the same heavenly stem while their earthly branches flank and embrace a middle position that contains either the day-master's salary or its noble star. Classic examples include Gui-Hai day with Gui-Chou hour embracing Zi (Gui's salary), and Ding-Si day with Ding-Wei hour embracing Wu (Ding's salary). The key principle is "empty embrace": the middle position must remain unoccupied by any actual branch in the chart, like an empty vessel that can hold whatever is poured into it.
  
  If the middle position is "filled"—that is, occupied by a branch that physically appears in the chart—then the embracing gesture loses its power, because the vessel is already full and can receive nothing more. Likewise, clashes, punishments, harm, the Blade or Seven-Killer attacking the flanking branches will disrupt the balance and scatter the noble energy. The pattern also fears emptiness-and-void (kong wang), which is likened to a cracked vessel that cannot hold water no matter how carefully one pours.
  
  When all conditions align—same stem on day and hour, empty middle position, month in harmony with the embraced salary or noble, body strong, and fortune cycles passing through territories that strengthen the salary or noble—the classics promise "the honour of the Eight Seats", meaning ministerial rank. Whether the embrace captures salary or noble determines whether the outcome leans toward stable income and position (salary) or toward official rank and heavenly favour (noble or Tianyi noble)."""
    normalized_text_zh: str = """"""
    subject: str = "拱禄拱贵格与虚拱之妙"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_15', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_state', 'bazi_semantic', 'bazi_state_month_command_degree', 'bazi_semantic', 'bazi_condition_factor_157', 'bazi_semantic', 'bazi_condition_factor_145', 'bazi_semantic', 'source_ref', 'rel_smth_06_037', 'gonglu_gonggui_presence', 'rel_smth_06_038', 'xugong_tianshi_zhuangtai', 'rel_smth_06_039', 'xingchong_pohai_risk', 'evi_smth_06_037', 'gonglu_gonggui_presence', 'rule_gonglu', 'evi_smth_06_038', 'xugong_tianshi_zhuangtai', 'rule_xugong', 'evi_smth_06_039', 'xingchong_pohai_risk', 'rule_tianshi', 'map_smth_06_025', 'map_smth_06_026']
    
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
        l1_anchor="smth_v1.0.0_拱禄拱贵格与虚拱之妙_001_L1",
    )
    version: str = "1.0.0"
