"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412570
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
    semantic_id="smth_v1.0.0_论建禄与身旺之利弊_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论建禄与身旺之利弊(SemanticEntry):
    """
    - 原文（source_text）：

  论建禄（此与前论禄同参）：建禄者，乃甲日寅月，乙日卯月，五行临官之位也。甲用金为官，金绝在寅，用土为财，土病于寅，以身旺太过，财官俱不得。若别无财官可取，再...
    """
    
    original_text: str = """- 原文（source_text）：

  论建禄（此与前论禄同参）：建禄者，乃甲日寅月，乙日卯月，五行临官之位也。甲用金为官，金绝在寅，用土为财，土病于寅，以身旺太过，财官俱不得。若别无财官可取，再遇劫夺，马既不扶，禄又不养，多主贫贱，颇宜时带偏官、偏财或食神，更看年时上露者取用。若略见财官，反争夺，不吉。凡命月令建禄，难招祖业，必主平生见财不聚，却病少寿长。行运再见比肩，克妻妨父损子，或官非破财，或因妻孥财帛争夺。如八字内外元有财官，引旺得地，官星有助，运临官星有气之地，亦贵；财星有助，运临财旺之地，亦富；财官俱旺，乃富贵之命。若时逢财库，运至财乡，必主晚年大富。年上财官有助，必享祖荫。若四柱元无财官，纵运行财官之地，亦止虚花而已。命无财官，岁运又行比肩，一生贫蹇。赋云：“根在苗先，实在花后。”言先有根然后长苗，有花然后结果。若当生岁元无财官，虽遇财官吉运，发福不大。假如甲日寅月，柱中乙卯未字多，主无祖财，克妻，一世孤贫，作事虚诈，为人大模样。乙日生卯月，柱有庚辛巳酉丑申及戊己巳午辰戌等字，财官多则贵；壬癸申子辰亥水印成局亦佳，更运逢之尤妙。若柱不见财官印食，同前断。丙生巳月，岁时干支水金成局，运历财官旺地，亦主富贵。丁生午月，金败水绝，财官俱背，顺运克妻，逆运克三妻。若柱有巳酉丑庚辛壬癸亥申子辰，运临财官旺地亦发，用煞或印，以多为贵。若止建禄，亦同前断。戊日巳月，年日时无水，主克妻，无祖业，子多不肖；柱中多有官则吉，如见偏官，主尊贵。岁月若是火多，及或印绶，虽无财官，主吉。若柱内隐显壬癸亥申子辰水局，晚子一二，有甲寅乙卯亥未木局，运至财官旺地亦发。己生午月，以壬水为...

- 分字分词释义：

  - **建禄**：日主生于自身临官之月，如甲日寅月、乙日卯月等，身气极旺。
  - **身旺太过，财官俱不得**：若无适当财官、食伤、印绶调剂，单纯身旺反成“有力无用”。
  - **难招祖业、见财不聚**：建禄多主自立门庭、少承祖荫，且易因好强、好胜而破财。
  - **“根在苗先，实在花后”**：比喻财官之应必须有“根”（原局基础），方能在运程中开花结果。

- **规范化释义（primary_lang_explained）**：

  建禄格，讨论的是“身旺在月令”的利与弊。以甲日寅月、乙日卯月为代表，日主在月令得临官之位，本身力量极强：

  - 若同时有清纯的财官、印绶等相配，则如大树根深、枝叶繁茂，既能担财，又能承官，易成富贵；
  - 若全局只有比肩、劫财，而少见财官印食，则如一片密林抢占土地，却无果实与花朵，容易表现为好强好胜、破财伤亲、见财不聚。

  原文因此一再强调：建禄之人要有“根基上的财官”，行运再逢财官旺地，方能真正发福；若原局无财官，即使行至财官之运，多半也只是“虚花”，难成大器。

- 核心要点：

  - 建禄的本质是**身旺在月令**，重点在“如何用身”。
  - 身旺配清财官、印绶时，多主自立成家、后发成名；
  - 身旺配比劫重、少财官时，多主克妻伤亲、见财不聚、劳而不显。

- 详细解说：

  可从三层理解建禄：

  1. **力量层面**：建禄表示日主在月令势力极强，做事有冲劲、有担当；
  2. **结构层面**：看这股力量是用来生财、任官，还是用在内耗（比劫争财、伤官克官）上；
  3. **时序层面**：看原局是否先具财官之根，再在行运中开花结果。

  例如文中所举：

  - 甲日寅月而局中乙卯未太多者，木气过盛反失财官之用，多主无祖业、克妻孤贫；
  - 乙日卯月若兼见庚辛巳酉丑申等财官，或壬癸申子辰亥印局，则建禄之力被财官印所用，反成贵命；
  - 丙巳、丁午、戊巳、己午等建禄日，也需分别看水、金、木等是否到位，以定其富贵层次。

  因此，面对建禄，不宜仅以"身旺则吉"一语带过，而应细分"身旺为谁而旺""旺后往哪里去"；只有当旺气被正确引导时，建禄才是真正的贵格。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_137]` `[trigger: 建禄定义]` `[factor_trigger: rizhu_linguan AND yueling_shenwang]` `[role: 主干]` 建禄者，乃甲日寅月，乙日卯月，五行临官之位也。身旺太过，财官俱不得。 → 《三命通会》卷六#论建禄与身旺之利弊
  - `[ns_smth_06_138]` `[trigger: 根在苗先]` `[factor_trigger: yuanju_caiguan AND yougen_shifa]` `[role: 主干依赖]` 根在苗先，实在花后。先有根然后长苗，有花然后结果。 → 《三命通会》卷六#论建禄与身旺之利弊
  - `[ns_smth_06_139]` `[trigger: 无财官虚花]` `[factor_trigger: yuanju_wucaiguan AND suiyun_xuhua]` `[role: 条件分支]` 若四柱元无财官，纵运行财官之地，亦止虚花而已。 → 《三命通会》卷六#论建禄与身旺之利弊
  - `[ns_smth_06_140]` `[trigger: 建禄结论]` `[factor_trigger: jianlu_ge AND caiguanyinyou]` `[role: 总结]` 建禄配清财官印绶时，多主自立成家、后发成名。 → 《三命通会》卷六#论建禄与身旺之利弊

- 完整对等诠释（secondary_lang_full）：

  This section presents "On Jian-Lu (Establishing-Salary) and Body-Prosperous Pros-Cons":

  Jian-Lu (Establishing-Salary): When the Month-Branch is the Day-Master's Lu (salary) position. This creates naturally body-prosperous configuration as Day-Master gains direct support from Month Command.

  Pros of body-prosperous: Strong self-identity, independent capability, not easily overwhelmed. Can handle Wealth and Officer energies that would crush weaker day-masters.

  Cons of body-prosperous: Too strong without outlet creates stagnation. Needs Wealth-Officer-Food to channel excess strength. Purely body-strong without usage becomes mere physical health without achievement.

  Balance principle: Jian-Lu thrives with appropriate counterbalance - neither too supported (stagnation) nor too drained (exhaustion). The "establishing" suggests foundational stability requiring purposeful direction.

  Engineering note: Model as "foundational-strength pattern" with optimal range requiring balanced resource-usage ratio."""
    normalized_text_zh: str = """"""
    subject: str = "论建禄与身旺之利弊"
    factor_refs: list = ['engine_id', 'bazi_structure_marker_29', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_factor_17', 'bazi_semantic', 'bazi_state_degree_14', 'bazi_semantic', 'bazi_condition_factor_174', 'bazi_semantic', 'bazi_condition_bijian', 'bazi_semantic', 'source_ref', 'rel_smth_06_094', 'jianlu_ge_presence', 'rel_smth_06_095', 'yuanju_caiguan_genji', 'rel_smth_06_096', 'yun_caiguan_fafu', 'evi_smth_06_094', 'jianlu_ge_presence', 'rule_jianlu', 'evi_smth_06_095', 'yuanju_caiguan_genji', 'rule_gengen', 'evi_smth_06_096', 'bijian_keqin_risk', 'rule_bikeqin', 'map_smth_06_063', 'map_smth_06_064']
    
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
        l1_anchor="smth_v1.0.0_论建禄与身旺之利弊_001_L1",
    )
    version: str = "1.0.0"
