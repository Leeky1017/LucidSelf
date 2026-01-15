"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559175
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
    semantic_id="yhzp_v1.0.0_论小儿关煞_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论小儿关煞(SemanticEntry):
    """
    - **原文（source_text）**：小儿之命，当论时辰为主；先看关煞，次看格局。日主强，财官旺，有关无煞。日干弱，财官多，有关有煞；又有三合，聚煞者难养。子平之法，偏官为关，偏财为煞，取生辰之...
    """
    
    original_text: str = """- **原文（source_text）**：小儿之命，当论时辰为主；先看关煞，次看格局。日主强，财官旺，有关无煞。日干弱，财官多，有关有煞；又有三合，聚煞者难养。子平之法，偏官为关，偏财为煞，取生辰之数断之；水一、火二、木三、金四、土五。

- **分字分词释义**：
  - **小儿之命**：特指尚在幼年阶段的命局分析，重在关口与夭折风险。
  - **时辰为主**：以时柱为小儿命的核心落点，代表幼年身体状态与早年环境。
  - **关煞**：关口与凶煞的合称，主生死关卡、重病、意外等重大风险。
  - **格局**：命局整体十神配置与旺衰结构，是次一级的长期命运框架。
  - **有关无煞**：有关口但无实质凶煞，形同有惊无险，多能逢凶化吉。
  - **有关有煞**：既有关口又有实质凶煞，会在特定年龄段形成实质危险。
  - **三合聚煞**：三合局将偏官、偏财等凶神聚合成势，煞气成团而不易化解。
  - **偏官为关**：以七杀（偏官）象征小儿需跨越的重大关口，如病关、险关。
  - **偏财为煞**：以偏财象征消耗性、压迫性的外在因素，成为凶煞来源。
  - **生辰之数**：按出生时干支所属五行折算成数字，用以推算应验年龄。
  - **水一、火二、木三、金四、土五**：五行与数字的一一对应，作为断关煞年限的基础码表。

- **规范化释义（primary_lang_explained）**：小儿命以时辰为主，先看关煞后看格局。偏官为关（关口），偏财为煞（凶煞）。日主强财官旺有关无煞易养；日主弱财官多有关有煞难养。用五行生数断关煞年龄：水1、火2、木3、金4、土5。

- **完整对等诠释（secondary_lang_full）**：Children's fate primarily analyzes Hour Pillar—first examine gates/obstacles then patterns. Indirect Officer represents gates (checkpoints), Indirect Wealth represents obstacles (calamities). Strong Day Master with prosperous Wealth/Officer has gates without obstacles (easy to raise); weak Day Master with abundant Wealth/Officer has both gates and obstacles (difficult to raise). Use Five-Element birth numbers to determine critical ages: Water=1, Fire=2, Wood=3, Metal=4, Earth=5.

- **核心要点**：小儿论时辰为主；偏官为关偏财为煞；日强易养日弱难养；用五行数断关煞年龄

- **详细解说**：  本条在前一条“小儿命总论”的基础上，进一步细化“关煞”这一高危维度。首先，将时柱定位为小儿命的核心落点——因为时柱所主多应在出生日后的人身状态与早年环境，所以判断幼年夭折与否，优先看时辰。其次，以“偏官为关、偏财为煞”建立了小儿关煞的十神映射：七杀象征严峻考验与危险关口，偏财则多主外在环境压力与消耗，两者合并构成“有关无煞 / 有关有煞”的判断框架。日主强、财官旺而又有关无煞，好比体质好、环境有挑战但无致命打击，多数能有惊无险地跨过；日主弱、财官多又聚合成煞，则如同体弱的孩子被推向高强度环境，极易在特定年龄段触发重病或大灾。最后，通过“五行生数：水一、火二、木三、金四、土五”的编码，给出了推算应验年龄的大致方法：依据时柱与相关凶神所属五行，换算成数字，并结合大运流年流转，判断在哪几个岁数附近最易应关，将“难养”的问题细化为“难在几岁”的时间结构。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_209]` `[trigger: 时辰为主]` `[factor_trigger: indirect_officer_gate AND indirect_wealth_obstacle]` `[role: 主干]` 小儿之命，当论时辰为主；先看关煞，次看格局。 → 《渊海子平·论小儿关煞》
  - `[ns_yhzp_210]` `[trigger: 日强有关无煞]` `[factor_trigger: children_strong_self AND indirect_officer_gate]` `[role: 条件分支]` 日主强，财官旺，有关无煞者，虽有关口，多能平安度过。 → 《渊海子平·论小儿关煞》
  - `[ns_yhzp_211]` `[trigger: 日弱有关有煞]` `[factor_trigger: has_gates_obstacles AND nan_yang]` `[role: 条件分支]` 日干弱，财官多，有关有煞，又有三合聚煞者，最为难养。 → 《渊海子平·论小儿关煞》
  - `[ns_yhzp_212]` `[trigger: 偏官为关偏财为煞]` `[factor_trigger: indirect_officer_gate AND indirect_wealth_obstacle AND obstacle]` `[role: 主干依赖]` 子平之法，偏官为关，偏财为煞，以此定小儿关煞轻重。 → 《渊海子平·论小儿关煞》
  - `[ns_yhzp_213]` `[trigger: 五行生数断关煞]` `[factor_trigger: five_element_birth_numbers AND guansha_nianling]` `[role: 条件分支]` 取生辰之数断之：水一、火二、木三、金四、土五，以此推关煞应验之年。 → 《渊海子平·论小儿关煞》
  - `[ns_yhzp_214]` `[trigger: 三合聚煞难养]` `[factor_trigger: has_gates_obstacles]` `[role: 条件分支]` 又有三合，聚煞成局者，小儿多病多惊，养育尤难。 → 《渊海子平·论小儿关煞》
  - `[ns_yhzp_215]` `[trigger: 有关无煞之象]` `[factor_trigger: indirect_officer_gate]` `[role: 例外处理]` 有关而无煞者，虽有小病小惊，终不至成大害。 → 《渊海子平·论小儿关煞》
  - `[ns_yhzp_216]` `[trigger: 小儿关煞纲领]` `[factor_trigger: indirect_officer_gate AND has_gates_obstacles]` `[role: 总结]` 小儿关煞之断，贵在时辰为主，先辨日主强弱，再看关煞聚散轻重。 → 《渊海子平·论小儿关煞》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 偏官为关 | Indirect Officer as Gate | 偏官代表关口障碍 | Indirect Officer represents gate/checkpoint | indirect_officer_gate | existing |
| 偏财为煞 | Indirect Wealth as Obstacle | 偏财代表凶煞 | Indirect Wealth represents calamity/obstacle | indirect_wealth_obstacle | existing |
| 五行生数 | Five-Element Birth Numbers | 水1火2木3金4土5 | Water-1, Fire-2, Wood-3, Metal-4, Earth-5 | five_element_birth_numbers | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "论小儿关煞"
    factor_refs: list = []
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论小儿关煞_001_L1",
    )
    version: str = "1.0.0"
