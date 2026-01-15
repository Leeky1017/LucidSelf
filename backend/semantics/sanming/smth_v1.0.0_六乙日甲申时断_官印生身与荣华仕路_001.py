"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157409
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
    semantic_id="smth_v1.0.0_六乙日甲申时断_官印生身与荣华仕路_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日甲申时断官印生身与荣华仕路(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日甲申时断。

  六乙日生时甲申，官星得印位生成；月中通气无冲破，必定荣华仕路人。乙日甲申时，官印生身，乙用庚为官，壬为印，申上庚旺壬生，身有寄托，通...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日甲申时断。

  六乙日生时甲申，官星得印位生成；月中通气无冲破，必定荣华仕路人。乙日甲申时，官印生身，乙用庚为官，壬为印，申上庚旺壬生，身有寄托，通金水月运者贵；不通，身弱官重，虽贵不永。

  乙丒日甲申时高，纯子辰年月，行东南运，大贵。巳酉丑，贵；中防凶。午未纯，吉。亥卯亦吉。余月平平。

  乙卯日甲申时，化贵。月通水气无伤破者，贵，不然，富。

  乙巳日甲申时，身强官旺。春，聪明显达，官至四品。夏，身心劳碌。秋冬眼疾。午年月，行财运，贵。

  乙未日甲申时，生未酉亥月，聪俊特达，官至二三品。丙丁寅午卯酉年月，伤食制煞，权贵。

  乙酉日甲申时，官煞混杂，若柱丁火制煞留官则吉。亥卯未酉年月，武职极品；不久；行东南方运，大贵。

  乙亥日甲申时，时落空亡，主少子。秋生，官居六卿。亥卯年未月，俱吉。

  乙日相逢时遇甲，长生驿马内相亲；贵人天乙来相助，释却褐衣入紫宸。乙日申时逢贵，其间高人见喜。小人称美有奇希，克破冲刑减力。身旺运逢吉地，信知两旺财官。有鞍有马有衣冠，定主门庭改换。

- 分字分词释义：

  - **官印生身**：庚金正官旺于申，壬水正印生于申，官生印、印生身，形成连环相生。
  - **长生驿马**：申为乙木的驿马，象征奔波发展与外出机遇。
  - **释却褐衣入紫宸**：脱去平民布衣，进入皇宫，比喻由平民跃升为显贵。
  - **门庭改换**：家族地位提升，从普通人家变为官宦之家。

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，甲申时」：

  - 申上庚金正官旺盛，壬水正印长生，形成官生印、印生身的良性结构；
  - 若月令通金水之气，官印双全，必为仕途显达之人；
  - 若身弱官重，虽有贵气但难以持久，需要身旺来承担官星。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Jia-Shen Hour":

  - At Shen, Geng Metal (Direct Official) reaches its peak while Ren Water (Direct Seal) enters long life, forming a beneficial chain of Official generating Seal and Seal nurturing self.
  - When monthly pillar channels Metal-Water energy with Official-Seal complete, this becomes a person destined for official career glory.
  - If body is weak but Official is heavy, though nobility exists it cannot last; strong body is needed to bear the Official star.

- 核心要点：

  - 本格以「官印生身」为核心，强调官场发展与仕途荣华。
  - 申为驿马，象征外出发展、奔波有成。
  - 歌诀强调：若无冲破刑克，则门庭改换、荣华富贵。

- 详细解说：

  1. **官印相生的用法**  
     - 庚金正官在申为建禄，壬水正印在申为长生；  
     - 官生印、印生身，形成「官印双全」的上佳结构。

  2. **身弱官重的风险**  
     - 若日主乙木身弱，无法承担强旺的官星；  
     - 需要印绶扶身或行身旺运，方能发挥官印之福。

  3. **六乙日的差异**  
     - 各日支因根气不同，吉凶有别；  
     - 秋生官旺者最贵，春夏需看身旺配合。

- 校勘与字词辨析：

  - 「释却褐衣入紫宸」为典型的科举登第意象，本稿保留其象征意义。
  - 「有鞍有马有衣冠」形容功成名就、衣锦还乡。
  - **English**：
    - Metaphor describing success and returning home in glory.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_081]` `[trigger: 官印生身]` `[factor_trigger: guanyin_shenshen AND wei_shengcheng]` `[role: 主干]` 六乙日生时甲申，官星得印位生成。 → 《三命通会》卷八#六乙日甲申时
  - `[ns_smth_08_082]` `[trigger: 荣华仕路]` `[factor_trigger: ronghua_shilu AND wu_chongpo]` `[role: 主干依赖]` 月中通气无冲破，必定荣华仕路人。 → 《三命通会》卷八#六乙日甲申时
  - `[ns_smth_08_083]` `[trigger: 贵人天乙]` `[factor_trigger: guiren_tianyi AND lai_xiangzhu]` `[role: 条件分支]` 贵人天乙来相助，释却褐衣入紫宸。 → 《三命通会》卷八#六乙日甲申时
  - `[ns_smth_08_084]` `[trigger: 门庭改换]` `[factor_trigger: menting_gaihuan AND liangwang_caiguan]` `[role: 总结]` 有鞍有马有衣冠，定主门庭改换。 → 《三命通会》卷八#六乙日甲申时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日甲申时断：官印生身与荣华仕路"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_161', 'bazi_semantic', 'bazi_state_factor_92', 'bazi_semantic', 'bazi_state_factor_162', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_metal_water', 'bazi_semantic', 'source_ref', 'rel_smth_08_061', 'guanyin_shenshen', 'rel_smth_08_062', 'guanyin_shuangquan', 'rel_smth_08_063', 'tongjinshui_qi', 'evi_smth_08_061', 'guanyin_shenshen', 'rule_guanyin', 'evi_smth_08_062', 'guanyin_shuangquan', 'rule_shuangquan', 'evi_smth_08_063', 'menting_gaihuan', 'rule_menting', 'map_smth_08_041', 'map_smth_08_042']
    
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
        l1_anchor="smth_v1.0.0_六乙日甲申时断_官印生身与荣华仕路_001_L1",
    )
    version: str = "1.0.0"
