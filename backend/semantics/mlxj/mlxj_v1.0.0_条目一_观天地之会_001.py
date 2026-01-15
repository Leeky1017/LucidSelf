"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850512
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
    semantic_id="mlxj_v1.0.0_条目一_观天地之会_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目一观天地之会(SemanticEntry):
    """
    ### 原文（source_text）

观天地之会。如分至有节，建厌有位。春秋之中曰分。二分之日，日出卯，入酉，昼行地上，夜行地下，皆一百八十二度半强，故昼夜长短同也。冬夏之中曰至。夏至者，阳极之至...
    """
    
    original_text: str = """### 原文（source_text）

观天地之会。如分至有节，建厌有位。春秋之中曰分。二分之日，日出卯，入酉，昼行地上，夜行地下，皆一百八十二度半强，故昼夜长短同也。冬夏之中曰至。夏至者，阳极之至，阴气始至，日北至，日长之至，日影短至也。冬至者，阴极之至，阳气始至，日南至，日短之至，曰影长至也。建厌者，日辰所会也。斗柄所建为阳建，正月寅，二月卯、三月辰，顺数也。日前一次为阴建，正月戍，二月西，三月申，逆数也。阴建即月厌也。厌对者，正月辰、二月卯，三月寅，亦逆数也。四月阳建于巳，破于亥，阴建于未，破于癸，是为阳破阴，阴破阳，故四月有癸亥，十月有丁巳，皆为天地交会之辰也。占梦者必考于其会，始能按候而定吉凶。

### 分字分词释义

- **天地之会**：天地之气交会的时节/阴阳之气会合的关键节点/占梦时机判断的首要依据
- **分至**：春分、秋分、夏至、冬至/一年之中阴阳消长的四个极点/天文历法核心节气
- **建厌**：斗柄所指之月建与月厌/阳建顺行、阴建逆行/日月会合的天文坐标
- **阳建**：斗柄所建之方位，正月寅、二月卯、三月辰，顺时针行进
- **阴建**：月厌之位，正月戌、二月酉、三月申，逆时针行进
- **阳破阴、阴破阳**：四月阳建巳破亥、阴建未破癸/十月丁巳亦然/阴阳相冲的交会点
- **考于其会**：审察天地交会的时机/将梦境与天文历法对应/精准定位吉凶应验之期

### 规范化释义（primary_lang_explained）

占梦的第一条核心原则是「观天地之会」——必须审察天地阴阳之气交会的时节。所谓「分至有节」，指春分、秋分、夏至、冬至这四个关键节气。春分秋分之日，太阳从卯位升起、酉位落下，昼行于地上、夜行于地下各一百八十二度半强，故昼夜等长。夏至是阳气极盛、阴气始生之时，太阳北至、白昼最长、日影最短；冬至则是阴气极盛、阳气始生之时，太阳南至、白昼最短、日影最长。

所谓「建厌有位」，是指北斗斗柄所指的月建与月厌的方位。斗柄所建为阳建，正月指寅、二月指卯、三月指辰，是顺时针方向行进。而阴建即月厌，正月在戌、二月在酉、三月在申，是逆时针方向行进。四月阳建于巳而破于亥，阴建于未而破于癸，这就是阳破阴、阴破阳的交会时刻。因此四月有癸亥日、十月有丁巳日，都是天地交会的关键时辰。

占梦者必须精准考察这些天地交会的时机，才能按照时令节候准确判定梦境的吉凶。

### 完整对等诠释（secondary_lang_full）

The first principle of dream interpretation is "Observing the Meeting of Heaven and Earth" — one must examine the critical junctures when the Yin and Yang energies of Heaven and Earth converge. The "solstices and equinoxes have their nodes" refers to the four pivotal solar terms: Spring Equinox, Autumn Equinox, Summer Solstice, and Winter Solstice. On the equinoxes, the sun rises from the Mao position and sets at the You position, traveling 182.5 degrees above ground during daytime and below ground at night, thus equalizing day and night.

The Summer Solstice marks the zenith of Yang energy and the inception of Yin; the sun reaches its northernmost point, the day is longest, and shadows are shortest. The Winter Solstice marks the zenith of Yin energy and the inception of Yang; the sun reaches its southernmost point, the day is shortest, and shadows are longest.

The "monthly establishments and suppressions have their positions" refers to the directional indicators of the Big Dipper's handle. The Yang establishment follows the Dipper's direction: Yin in the first month, Mao in the second, Chen in the third — progressing clockwise. The Yin establishment (monthly suppression) runs counterclockwise: Xu in the first month, You in the second, Shen in the third. In the fourth month, Yang establishes at Si and breaks at Hai, while Yin establishes at Wei and breaks at Gui — this represents Yang breaking Yin and Yin breaking Yang. Therefore, the Gui-Hai day in the fourth month and the Ding-Si day in the tenth month are critical moments of Heaven-Earth convergence.

Dream interpreters must precisely examine these convergence points to accurately determine auspiciousness based on seasonal timing.

### 核心要点

- 占梦必须首先考察天地阴阳交会的时机
- 分至（春分、秋分、夏至、冬至）是阴阳消长的四个极点
- 春分秋分昼夜等长，标志阴阳平衡
- 夏至阳极阴始，冬至阴极阳始
- 斗柄所建为阳建，顺行（寅卯辰巳午未申酉戌亥子丑）
- 月厌为阴建，逆行（戌酉申未午巳辰卯寅丑子亥）
- 四月癸亥、十月丁巳为天地交会之辰
- 必须按时令节候定吉凶，不可脱离天文历法

### 详细解说

此条为占梦十三条之首，确立了「天人感应」的基本框架：梦境不是孤立的心理现象，而是与天地运行节律紧密相关。占梦者必须具备历法天文知识，将梦境发生的时间节点与天地阴阳交会的周期对应，才能准确判断梦境的吉凶应验。

「分至」代表太阳周年视运动的四个极值点，是阴阳消长的转折。「建厌」则是月建与月厌的阴阳对冲，反映了更细密的时间节奏。占梦者需要同时考虑年节（分至）与月节（建厌），形成多层次的时间坐标系。

此原则奠定了《梦林玄解》「以时占梦」的方法论基础：同一梦象在不同节气、不同月建下，吉凶判断可能截然不同。

### 叙事素材（narrative_snippets）

- `[ns_mlxj_001]` `[trigger: 占梦时机判断]` `[factor_trigger: dream_timing_judgment AND dream_timing_convergence AND dream_month_jian AND dream_month_yan]` `[role: 主干]` 占梦者必考于其会，始能按候而定吉凶。 → 《梦林玄解·卷之首》#观天地之会
- `[ns_mlxj_002]` `[trigger: 春秋分]` `[factor_trigger: dream_solar_term_pivot]` `[role: 主干依赖]` 二分之日，昼行地上，夜行地下，皆一百八十二度半强，故昼夜长短同也。 → 《梦林玄解·卷之首》#观天地之会
- `[ns_mlxj_003]` `[trigger: 夏至]` `[factor_trigger: dream_solar_term_pivot]` `[role: 条件分支]` 夏至者，阳极之至，阴气始至，日北至，日长之至，日影短至也。 → 《梦林玄解·卷之首》#观天地之会
- `[ns_mlxj_004]` `[trigger: 冬至]` `[factor_trigger: dream_solar_term_pivot]` `[role: 条件分支]` 冬至者，阴极之至，阳气始至，日南至，日短之至，日影长至也。 → 《梦林玄解·卷之首》#观天地之会
- `[ns_mlxj_005]` `[trigger: 天地交会日]` `[factor_trigger: dream_convergence_day]` `[role: 总结]` 四月有癸亥，十月有丁巳，皆为天地交会之辰也。 → 《梦林玄解·卷之首》#观天地之会"""
    normalized_text_zh: str = """"""
    subject: str = "条目一：观天地之会"
    factor_refs: list = ['dream_timing_convergence', 'dream_solar_term_pivot', 'month_jianyan', 'yang_jian', 'yin_jian']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_条目一_观天地之会_001_L1",
    )
    version: str = "1.0.0"
