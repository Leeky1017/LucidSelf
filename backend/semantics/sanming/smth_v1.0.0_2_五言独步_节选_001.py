"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081167
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
    semantic_id="smth_v1.0.0_2_五言独步_节选_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2五言独步节选(SemanticEntry):
    """
    - 原文（source_text）：
  有病方为贵，无伤不是奇。格中如去病，财禄喜相随。
  寅卯多金丑，贫富高低走。南地怕逢申，北方休见酉。
  建禄生提月，财官喜透天。不宜身再旺，惟喜茂财源。
...
    """
    
    original_text: str = """- 原文（source_text）：
  有病方为贵，无伤不是奇。格中如去病，财禄喜相随。
  寅卯多金丑，贫富高低走。南地怕逢申，北方休见酉。
  建禄生提月，财官喜透天。不宜身再旺，惟喜茂财源。
  土厚多逢火，归金旺遇秋。冬天水木泛，名利总虚浮。
  甲乙生居卯，金多返吉祥。不宜重见煞，火地得衣粮。
  火忌西方酉，金沉怕水乡。木神休见午，水到卯宫伤。
  土宿休行亥，临官在巳宫。南方根有旺，西北莫相逢。
  阴日朝阳格，无根月建辰。西方还有贵，干怕火来侵。
  乙木生居酉，莫逢全己丑。富贵坎离宫，贫穷坤艮守。
  有煞只论煞，无煞方论用。只要去煞星，不怕提纲重。
  甲乙若逢申，煞印暗相生。木旺金逢旺，冠袍必挂身。
  丙火怕重逢，北方返有功。虽然宜见水，犹恐对提冲。
  八月官星旺，甲逢秋气深。财官兼有助，名利自然亨。
  曲直生春月，庚辛干上逢。南离推富贵，坎地却犹凶。
  甲乙生三月，庚辛戌未存。丑宫壬癸位，何虑见无根。
  木茂宜金火，身衰鬼作关。时分西与北，轻重辨东南。
  时上胞胎格，月逢印绶通。煞官行运助，职位至三公。
  二子不冲午，二寅不冲申。二午不冲子，二申不冲寅。
  得一分三格，财官印绶全。运中逢克破，一命丧黄泉。
  进气死不死，退气生不生。终年无发旺，犹忌少年刑。
  时上偏财格，干头忌比肩。月生身主旺，贵气福重深。
  时上一位贵，藏在支中是。日主要刚强，名利方有气。
  运行十载数，上下五年分。先看流年岁，深知来往旬。

- 规范化释义（primary_lang_explained）：  
  本段五言独步围绕“有病方为贵，无伤不是奇”展开，提出命理中的“病药论”。命局若全无偏枯冲克之病，多主平常顺遂而不见奇；反是带有明显偏旺偏弱、刑冲破害的“病处”，却又同时具备能制、能化、能调候的“药”，反而更容易形成高格。歌中以建禄、煞印、偏财、胞胎等具体格局为例：建禄逢财官透出，不再一味助身，而是让身与财官形成互动；木茂得金火，既修剪又点燃，使木从徒长之枝变为可用之材；煞印相生，则是用印绶去承接七煞，把原本的冲克之气转化为权柄与担当。  
  另一方面，歌诀也给出操作上的优先级——“有煞只论煞，无煞方论用”：一旦命局中七煞明显、刑冲繁多，首要任务是评估煞的轻重与制化是否得当，而不是急于寻找其他用神。只有在大局中没有突出“病煞”时，才回到常规的财官印食平衡之道。诸如“时上胞胎格”“二子不冲午”等句，则点出一些看似凶猛却内含转机的特殊组合：时上胞胎逢印绶贯通，再得煞官有情之运，可以自基层跃升三公；双重冲支时，冲力分散，原本绝对的对冲反而被削弱，需要用病药视角重新衡量凶吉。末尾关于大运“十载上下五年分”与流年的配合，则提醒我们：同一病药结构，若药来得早、来得巧，可以成就功名；若药迟至或错位，便可能只是虚惊或白忙。  

- 完整对等诠释（secondary_lang_full）：  
  This five‑syllable verse elaborates the so‑called "illness and medicine" doctrine in chart interpretation. It begins by stating that a chart rarely becomes truly remarkable if nothing in it can be called an "illness"—no serious imbalance, clash, or punishment. What often produces great destinies are those patterns that clearly look problematic on the surface yet meet, within the natal chart or through later luck cycles, genuine "medicine": elements that control, transform, or climatologically moderate the excess. The lines on jianlu (self at its own station of strength), strong Killings, Seals, and partial Wealth show how this works in practice: when the Day Master sits in jianlu and Wealth and Office reveal themselves cleanly, the self is not merely bloated but able to engage with resources and authority; when luxuriant Wood encounters both Metal and Fire, it is pruned and fired into something enduring; when Killing produces Seals, harsh pressure is converted into status and responsibility.  
  At the same time, the text lays down a clear order of operations: "When there is Killing, discuss only Killing; only when there is no Killing do we discuss the usual useful spirit." In other words, once strong Seven Killings and punitive configurations dominate the chart, the first question is whether they are properly checked, transformed, or supported—only afterwards does one consider more ordinary Wealth‑and‑Officer balance. In the absence of such acute "illness", one reverts to standard yongshen reasoning. Phrases such as the "fetal pattern on the Hour branch" and the rules that "two Zi do not clash Wu" point to special structures in which apparent damage may be mitigated by how forces divide or combine. An Hour‑pillar fetal configuration, assisted by Seals and favorable Killing/Officer luck, can raise someone to the rank of high minister; double branches that nominally clash a single branch may in fact split the impact so the clash is less lethal, demanding a subtler reading of harm and remedy. Finally, the instruction to divide each ten‑year fortune into upper and lower five‑year segments, and to cross‑check them with annual flows, underscores that timing is part of the medicine: the same chart can play out as breakthrough or mere struggle depending on when, and how, cure and illness actually meet.  

- 核心要点：
  - **病药说**：有病有药方为贵。
  - **建禄**：喜财官透。
  - **煞为先**：有煞只论煞。
  - **特殊格**：时上胞胎、二不冲一。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_037]` `[trigger: 有病方为贵]` `[factor_trigger: youbing_fangweigui AND wushang_bushiqi]` `[role: 主干]` 有病方为贵，无伤不是奇。格中如去病，财禄喜相随。 → 《三命通会》卷十二#五言独步（节选）
  - `[ns_smth_12_038]` `[trigger: 建禄生提月]` `[factor_trigger: jianlu_shengtiyue AND caiguan_xitoutian]` `[role: 主干依赖]` 建禄生提月，财官喜透天。不宜身再旺，惟喜茂财源。 → 《三命通会》卷十二#五言独步（节选）
  - `[ns_smth_12_039]` `[trigger: 有煞只论煞]` `[factor_trigger: yousha_zhilunsha AND qusha_bupa]` `[role: 条件分支]` 有煞只论煞，无煞方论用。只要去煞星，不怕提纲重。 → 《三命通会》卷十二#五言独步（节选）
  - `[ns_smth_12_040]` `[trigger: 时上胞胎格]` `[factor_trigger: shishang_baotaige AND zhiwei_sangong]` `[role: 总结]` 时上胞胎格，月逢印绶通。煞官行运助，职位至三公。 → 《三命通会》卷十二#五言独步（节选）"""
    normalized_text_zh: str = """"""
    subject: str = "2 五言独步（节选）"
    factor_refs: list = ['engine_id', 'bazi_structure_factor_38', 'bazi_state_qiangruo_2', 'bazi_condition_factor_26', 'jianlu_with_wealth_office', 'bazi_relation_factor_45', 'killing_generates_seal', 'bazi_relation_geju_degree', 'bazi_temporal_factor_6', 'source_ref', 'rel_smth_12_034', 'core_factor', 'rel_smth_12_035', 'cond_factor', 'rel_smth_12_036', 'risk_factor', 'evi_smth_12_034', 'core_factor', 'rule_name34', 'evi_smth_12_035', 'cond_factor', 'rule_name35', 'evi_smth_12_036', 'risk_factor', 'rule_name36', 'map_smth_12_023', 'map_smth_12_024']
    
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
        l1_anchor="smth_v1.0.0_2_五言独步_节选_001_L1",
    )
    version: str = "1.0.0"
