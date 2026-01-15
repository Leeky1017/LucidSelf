"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558823
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
    semantic_id="yhzp_v1.0.0_论正财_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论正财(SemanticEntry):
    """
    - **原文（source_text）**：何谓之正财？犹如正官之意；是阴见阳财，阳见阴财。大抵正财，吾妻之财也。人之女赀财以事我，必精神康强，然后可以享用之；如吾身方且自萎懦而不振，虽妻财丰厚，但能...
    """
    
    original_text: str = """- **原文（source_text）**：何谓之正财？犹如正官之意；是阴见阳财，阳见阴财。大抵正财，吾妻之财也。人之女赀财以事我，必精神康强，然后可以享用之；如吾身方且自萎懦而不振，虽妻财丰厚，但能目视，终不可一毫受用。故财要得时，不要财多。若财多则自家日本有力，可以胜任，当化作官。

- **分字分词释义**：
  - **正财**：我克且阴阳相异者，如甲木克己土，己土为甲木之正财。
  - **阴见阳财/阳见阴财**：阴日干见阳财星，阳日干见阴财星，为正财。
  - **吾妻之财**：正财代表妻子与财富，为男命妻星。
  - **精神康强**：日主旺相有力，方能驾驭财星。
  - **萎懦不振**：日主衰弱无力，无法享用财富。
  - **财要得时**：财星需在适当的时机出现，配合命局。
  - **财多化官**：财星过多且身强，财生官为富贵双全。
  - **身弱不任财**：日主太弱，财多反成祸患。

- **规范化释义（primary_lang_explained）**：正财是我克且阴阳相异者，如妻之财。正财需身强方能享用，身弱财多反为累。财要得时不要多，财多身强可化官，财多身弱主祸患。财喜身旺印绶，忌官星劫财。

- **完整对等诠释（secondary_lang_full）**：Direct Wealth is what-I-control with opposite polarity, like wife's wealth. Direct Wealth requires strong Self to enjoy; weak Self with abundant Wealth becomes burden. Wealth should be timely not excessive—abundant Wealth with strong Self transforms to Officer; abundant Wealth with weak Self brings calamities. Wealth favors strong Self and Seal, taboos Officer Star and Rob Wealth.

- **核心要点**：
  - 正财是我克且阴阳相异者，代表妻与财
  - 正财需日主身强方能享用
  - 身弱财多反为累，虽目视终不可受用
  - 财要得时不要多，财多身强可化官
  - 财喜身旺印绶，忌比劫分夺

- **详细解说**：  
  本条论述正财的性质与身财关系。正财是我克且阴阳相异者（如甲木克己土），犹如"正官"之名，取其"正当"之意。正财代表"妻之财"——既指妻子，又指财富，是男命的核心六亲之一。本条最核心的论断是"身财关系"：只有日主"精神康强"（身旺有力）才能享用财富；若日主"萎懦不振"（身弱无力），即使"妻财丰厚"也只能"目视"而"终不可一毫受用"。这是子平法"身弱不任财"的经典表述。进一步论述"财要得时，不要财多"——财星需配合时机，不宜过多；若财多且身强，则"当化作官"，财生官为富贵双全；若财多身弱，则为祸患。此条是论财的基础理论。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_055]` `[trigger: 正财定义]` `[factor_trigger: direct_wealth]` `[role: 主干]` 何谓之正财？是阴见阳财，阳见阴财。 → 《渊海子平·论正财》
  - `[ns_yhzp_056]` `[trigger: 正财代表]` `[factor_trigger: direct_wealth]` `[role: 主干依赖]` 大抵正财，吾妻之财也。 → 《渊海子平·论正财》
  - `[ns_yhzp_057]` `[trigger: 身强任财]` `[factor_trigger: direct_wealth AND day_master_strength]` `[role: 条件分支]` 必精神康强，然后可以享用之。 → 《渊海子平·论正财》
  - `[ns_yhzp_058]` `[trigger: 身弱不任财]` `[factor_trigger: direct_wealth AND day_master_strength]` `[role: 例外处理]` 如吾身方且自萎懦而不振，虽妻财丰厚，但能目视，终不可一毫受用。 → 《渊海子平·论正财》
  - `[ns_yhzp_059]` `[trigger: 财要得时]` `[factor_trigger: direct_wealth AND caideshi]` `[role: 条件分支]` 故财要得时，不要财多。 → 《渊海子平·论正财》
  - `[ns_yhzp_060]` `[trigger: 财多化官]` `[factor_trigger: direct_wealth AND direct_officer]` `[role: 条件分支]` 若财多则自家日本有力，可以胜任，当化作官。 → 《渊海子平·论正财》"""
    normalized_text_zh: str = """"""
    subject: str = "论正财"
    factor_refs: list = ['direct_wealth', 'state_weak_self_cannot_bear_wealth_proposal', 'relation_wealth_generates_officer_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论正财_001_L1",
    )
    version: str = "1.0.0"
