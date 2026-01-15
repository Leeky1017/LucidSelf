"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157399
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
    semantic_id="smth_v1.0.0_六乙日癸未时断_入墓倒食与财微之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日癸未时断入墓倒食与财微之象(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日癸未时断。

  六乙日生时癸未，入墓之中遇倒伤；马劣财微食见克，一生衣禄主平常。乙日癸未时，乙以癸为倒食，未中丁火食神，己土偏财，破癸癸倒未中丁火之...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日癸未时断。

  六乙日生时癸未，入墓之中遇倒伤；马劣财微食见克，一生衣禄主平常。乙日癸未时，乙以癸为倒食，未中丁火食神，己土偏财，破癸癸倒未中丁火之食，平常衣禄。通土气月则吉。

  乙丒日癸未时，凶刑孤独，年月通土气，吉。

  乙卯日癸未时，改祖离亲，就妻为家。午未年月，贵。春尤贵。

  乙巳日癸未时，不贵则富，先难后易。纯午、三品贵。辰戌丑月，俱吉。

  乙未日癸未时，春，身旺刑伤。秋，官煞旺，科名有分。冬安稳。夏平常。

  乙酉日癸未时，身坐煞，春，身旺，吉。夏，身弱煞衰，贫。秋，煞旺，身能从化，贵。冬平。辰戌丑未月，透庚辛，行金运，贵。一到刃运，退官罢职。

  乙亥日癸未时，春木旺，刑伤妻子。申月官旺，贵。酉煞旺，年月有火则吉。午未戌年月，一二品贵。冬生稳厚。

  乙日相逢时癸未，算来离祖不成家；有刑克害多成败，运吉如添锦上花。乙日相逢癸未，生逢木墓夭孤。雁行兄弟有如无，心性不常喜怒。自立自成事业，六亲骨肉亲疏，贵人得合两相扶，此命先贫后富。

- 分字分词释义：

  - **倒食**：癸水为乙木偏印，又称枭神或倒食，有夺食之象。
  - **入墓**：未为木之墓库，乙木入未有收藏、沉潜之意。
  - **马劣财微**：驿马无力、财星薄弱，比喻外出发展不利、财源有限。
  - **改祖离亲**：离开祖业、远离父母，多指自立门户或入赘。

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，癸未时」：

  - 乙木在未为墓地，癸水为倒食（偏印），未中虽有丁火食神、己土偏财，但癸水克丁，形成倒食夺食之象；
  - 若不通土气月令，则财源有限，衣禄平常；
  - 歌诀提示：此格多有离祖自立之象，六亲缘薄，但若运势配合，仍可「先贫后富」。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Gui-Wei Hour":

  - Yi Wood at Wei enters the tomb; Gui Water serves as Reversed Food (Indirect Seal). Although Wei hides Ding Fire (Food God) and Ji Earth (Indirect Wealth), Gui Water overcomes Ding, forming a pattern of owl-god seizing food.
  - Without Earth-energy monthly pillar, wealth sources are limited and livelihood remains ordinary.
  - The verse indicates this pattern often involves leaving ancestral home and establishing independence; family bonds are thin, but with proper fortune alignment, one can go "from poverty to wealth."

- 核心要点：

  - 本格以「入墓遇倒食」为核心，结构偏弱。
  - 食神被克、财星微薄，需要土气月令或好运扶持。
  - 歌诀强调：自立自成，先难后易。

- 详细解说：

  1. **倒食夺食的困境**  
     - 癸水偏印克制丁火食神，形成「枭神夺食」之象；  
     - 食神被克则生财无源，需要其他配合来化解。

  2. **入墓的双重意义**  
     - 未为木墓，一方面有收藏、沉潜之意，另一方面也有气衰、受限之象；  
     - 若能冲开墓库或行运得当，反可晚发。

  3. **六乙日的差异**  
     - 各日支因季节与月令不同，吉凶差异较大；  
     - 春生身旺者较吉，秋冬需看官印配合。

- 校勘与字词辨析：

  - 「雁行兄弟有如无」形容兄弟姐妹缘分薄弱，各自发展。
  - 「先贫后富」强调此格需要时间积累，中晚年方见成就。
  - **English**：
    - Requires time accumulation; achievements visible in middle to late years.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_077]` `[trigger: 入墓倒食]` `[factor_trigger: rumu_daoshi AND you_sunshang]` `[role: 主干]` 六乙日生时癸未，入墓之中遇倒伤。 → 《三命通会》卷八#六乙日癸未时
  - `[ns_smth_08_078]` `[trigger: 马劣财微]` `[factor_trigger: malie_caiwei AND yilu_pingchang]` `[role: 主干依赖]` 马劣财微食见克，一生衣禄主平常。 → 《三命通会》卷八#六乙日癸未时
  - `[ns_smth_08_079]` `[trigger: 改祖离亲]` `[factor_trigger: gaizu_liqin AND jiu_qi_wei_jia]` `[role: 条件分支]` 改祖离亲，就妻为家。 → 《三命通会》卷八#六乙日癸未时
  - `[ns_smth_08_080]` `[trigger: 先贫后富]` `[factor_trigger: xianpin_houfu AND guiren_fuhe]` `[role: 总结]` 贵人得合两相扶，此命先贫后富。 → 《三命通会》卷八#六乙日癸未时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日癸未时断：入墓倒食与财微之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_160', 'bazi_semantic', 'bazi_state_factor_51', 'bazi_semantic', 'bazi_state_li', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_earth_1', 'bazi_semantic', 'source_ref', 'rel_smth_08_058', 'rumu_daoshi', 'rel_smth_08_059', 'xiaoshen_duoshi', 'rel_smth_08_060', 'tongtuqi_yue', 'evi_smth_08_058', 'rumu_daoshi', 'rule_rumu', 'evi_smth_08_059', 'xiaoshen_duoshi', 'rule_xiaoshen', 'evi_smth_08_060', 'gaizu_liqin', 'rule_gaizu', 'map_smth_08_039', 'map_smth_08_040']
    
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
        l1_anchor="smth_v1.0.0_六乙日癸未时断_入墓倒食与财微之象_001_L1",
    )
    version: str = "1.0.0"
