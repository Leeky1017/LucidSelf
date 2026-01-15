"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436443
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
    semantic_id="smth_v1.0.0_浊格与五行失位之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 浊格与五行失位之象(SemanticEntry):
    """
    - 原文（source_text）：

  浊者混也。乃五行失位，水土互伤，其身太旺，正夫不显，偏夫丛杂，柱多分别，无财官印食，为下贱村浊，或娼妓婢妾，淫巧之人。如己亥、乙亥、癸丑、己未，癸水生十月大...
    """
    
    original_text: str = """- 原文（source_text）：

  浊者混也。乃五行失位，水土互伤，其身太旺，正夫不显，偏夫丛杂，柱多分别，无财官印食，为下贱村浊，或娼妓婢妾，淫巧之人。如己亥、乙亥、癸丑、己未，癸水生十月大泛，癸以戊为夫不显，时引己未是偏夫，嫌丑未皆有土混杂，柱中无财，乙木为食神干旺，己土受克，鬼败临身，五行失位，主先清后浊，不能享福。

- 分字分词释义：

  - **浊者混也**：浊，本义为浑浊不清，引申为结构紊乱、气机混杂。
  - **五行失位，水土互伤**：五行不在得令得所之位，水土相互克伐，表示现实结构与资源配置错位。
  - **正夫不显，偏夫丛杂**：正官夫星力量弱或被遮蔽，而偏官、合煞等“偏夫”成群，象征伴侣位置不稳、关系对象复杂。
  - **无财官印食**：缺乏财、官、印、食等吉神的有力支撑，整体格局偏下，难以稳定向上。
  - **先清后浊**：早年似有清吉之象，随行运推移而趋于浑浊下走。

- **规范化释义（primary_lang_explained）**：

  本节所谓“浊格”，重点在于五行失位、关系与资源结构混乱：

  - 日主自身力量过重而环境承接不足，水土互伤，表示个体力量过重而环境承接不足；
  - 正夫星不显，偏夫星却丛杂，加上财官印食无力，易形成感情关系多线并行、难以稳定的局面；
  - 原例癸水十月生，大水泛滥而无财官印制约，故被古人视为“先清后浊，不能享福”的命式。

  现代阅读时，可把“浊”理解为：人生结构从相对清晰渐趋复杂，情感与经济关系纠缠，加之自身过强而缺乏外在正向约束，容易陷入下行的循环，而不必把“村浊、娼妓婢妾”等字眼直接等同于现实身份判断。

- 核心要点：

  - 浊格以**五行失位、身太旺、夫星混乱**为主要特征。
  - 正夫不显、偏夫丛杂，提示亲密关系重心不稳、角色难以单一。
  - 财官印食不济，使得社会地位与资源支持有限，易由清而浊。

- 详细解说：

  1. **结构上的“混”而不清**  
     - 五行失位、水土互伤，象征现实中责任、界限与资源分配皆不清晰；  
     - 自身过旺而环境承载不足，容易在关系中“以己为主”，却缺乏长期稳固的结构。

  2. **正偏夫星的对比**  
     - 正夫星象征正式伴侣与公开关系，偏夫则象征暧昧、隐性或非主流的关系模式；  
     - 浊格中正夫弱而偏夫多，意味着命主更容易在非主轴关系中消耗大量精力。

  3. **从清转浊的过程**  
     - 早年或行运尚佳时，可能仍有“清”的一面，如学习、事业起步端正；  
     - 随着时间与行运变化，若缺乏财官印的长期支撑，容易逐渐滑向更混杂的生活与关系结构。

  对今人而言，理解“浊格”更适合作为一个提醒：当自身能量很强、关系与资源分布却越来越乱时，需主动做减法、重建边界，而非简单以“命格不好”自我否定。

- **完整对等诠释（secondary_lang_full）**：

  The "Turbid" pattern portrays a life structure in which elements fall out of their proper places and begin to injure one another. The Day Master is often too strong for the environment that is meant to receive it; Water and Earth attack each other rather than cooperating; the rightful spouse star is weak or obscured, while various "side spouse" indications and mixed influences proliferate. At the same time, Wealth, Officer, Seal and Food are either missing or too weak to stabilise the picture.

  In the example, Gui Water is born in the tenth month, when Water overflows without proper banks. Gui takes Wu Earth as the spouse star, yet Wu fails to appear with strength and is instead represented by mixed Earth in Chou and Wei, which themselves clash and muddy the structure. Wealth and Officer are not in clear, supportive positions; the Day Master remains powerful and receives further stimulation, but lacks a clean channel through which that power can be expressed and contained. This is what the text summarises as "first clear, then turbid" – an early phase with some order and potential, followed by a slide into entanglement as time goes on.

  For a modern reader, Turbid does not have to mean "low-born" or morally condemned. It points to a configuration where relationships, money, and obligations are increasingly hard to disentangle, and where a strong personality meets insufficient boundaries and frameworks. The task is not to accept decline as fate, but to consciously simplify commitments, clarify contracts, and rebuild supportive structures so that what is clear in the early years does not gradually dissolve into confusion.

- 校勘与字词辨析：

  - 原文中“已土受克”之“已”，据例命与五行关系，当作“己土”解，本稿在断句中直接用“己土受克”，并于此说明。
  - “村浊、娼妓婢妾、淫巧之人”等用语，反映的是古代对阶层与性别角色的价值判断，本稿统一转译为结构与处境问题，不作道德评断。
  - **English**：
    - Addresses situation issues; not moral judgment.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_025]` `[trigger: 浊格定义]` `[factor_trigger: zhuo_ge_hun]` `[role: 主干]` 浊者混也。 → 《三命通会》卷七#浊格
  - `[ns_smth_07_026]` `[trigger: 五行失位]` `[factor_trigger: wuxing_shiwei AND shui_tu_hushang]` `[role: 主干依赖]` 乃五行失位，水土互伤，其身太旺，正夫不显，偏夫丛杂。 → 《三命通会》卷七#浊格
  - `[ns_smth_07_027]` `[trigger: 无财官印食]` `[factor_trigger: wu_cai_guan_yin_shi]` `[role: 条件分支]` 柱多分别，无财官印食，为下贱村浊。 → 《三命通会》卷七#浊格
  - `[ns_smth_07_028]` `[trigger: 先清后浊]` `[factor_trigger: xian_qing_hou_zhuo]` `[role: 总结]` 五行失位，主先清后浊，不能享福。 → 《三命通会》卷七#浊格"""
    normalized_text_zh: str = """"""
    subject: str = "浊格与五行失位之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_wuxing_degree', 'bazi_semantic', 'bazi_structure_factor_95', 'bazi_semantic', 'bazi_state_relation_3', 'bazi_semantic', 'bazi_qiangruo_1', 'bazi_semantic', 'source_ref', 'rel_smth_07_016', 'wuxing_shiwei', 'rel_smth_07_017', 'guanxi_jiuchan', 'rel_smth_07_018', 'congqing_ruzhuo', 'evi_smth_07_016', 'wuxing_shiwei', 'rule_zhuoge', 'evi_smth_07_017', 'zhengpianfu_qingxi', 'rule_pianfu', 'evi_smth_07_018', 'congqing_ruzhuo', 'rule_qingzhuo', 'map_smth_07_011', 'map_smth_07_012']
    
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
        l1_anchor="smth_v1.0.0_浊格与五行失位之象_001_L1",
    )
    version: str = "1.0.0"
