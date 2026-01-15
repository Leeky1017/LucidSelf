"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227818
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
    semantic_id="smth_v1.0.0_五行相克与子母复仇_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行相克与子母复仇(SemanticEntry):
    """
    - **原文（source_text）**：
  五行相克，子皆能为母复雠也。木克土，土之子，金反克木；金克木，木之子，火反克金；火克金，金之子，水反克火；水克火，火之子，土反克水；土克水，水之子，木...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行相克，子皆能为母复雠也。木克土，土之子，金反克木；金克木，木之子，火反克金；火克金，金之子，水反克火；水克火，火之子，土反克水；土克水，水之子，木反克土。互能相生，乃其始也；互能相克，乃其终也，皆出乎天之性也。

- **分字分词释义**：
  - **复雠**：复仇，"雠"通"仇"。
  - **互能相生**：彼此互相生养。
  - **互能相克**：彼此互相制约。
  - **天之性**：天道的自然属性。

- **规范化释义（primary_lang_explained）**：
  五行相克之中，子辈总能为母亲复仇。木克土，土的子是金，金就反过来克木；金克木，木的子是火，火就反过来克金；火克金，金的子是水，水就反过来克火；水克火，火的子是土，土就反过来克水；土克水，水的子是木，木就反过来克土。五行互相生养是其开始，互相制约是其终结，这都是出于天道的自然属性。

- **完整对等诠释（secondary_lang_full）**：
  In Five Elements mutual restriction, the offspring can always avenge the parent. Wood restricts Earth, yet Earth's child (Metal) counter-restricts Wood; Metal restricts Wood, yet Wood's child (Fire) counter-restricts Metal; Fire restricts Metal, yet Metal's child (Water) counter-restricts Fire; Water restricts Fire, yet Fire's child (Earth) counter-restricts Water; Earth restricts Water, yet Water's child (Wood) counter-restricts Earth. Mutual generation serves as the beginning, mutual restriction as the ending, all emanating from heavenly nature. This depicts the Elements' checks-and-balances in cyclical vengeance structure, enabling balance through generation and restriction proceeding together rather than unidirectional domination. This establishes the Elements' dynamic equilibrium in destiny analysis.

- **核心要点**：
  - 五行相克中存在"子为母复仇"的结构
  - 每个被克者的子，都能反克其克者
  - 互相生养是开始，互相制约是终结
  - 生克皆出于天道的自然属性

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_133]` `[trigger: 子母复仇]` `[factor_trigger: wuxing_xiangke AND offspring_vengeance]` `[role: 主干]` 五行相克，子皆能为母复雠也。木克土，土之子，金反克木；金克木，木之子，火反克金。互能相生，乃其始也；互能相克，乃其终也。 → 《三命通会》卷一#五行相克与子母复仇

- **详细解说**：
  此条揭示五行相克中的"复仇"机制，这是五行动态平衡的关键。当一行克另一行时，被克者的子会反过来克制克者，形成制衡。例如木克土，但土的子金会反克木，使木不至于过度克土。这种"子为母复仇"的结构，确保五行之间不会出现单向压制，而是形成循环制衡。原文强调，互相生养（相生）是事物的开始，互相制约（相克）是事物的终结，这一生一克、一始一终，都是天道的自然属性，体现宇宙运行的规律。

- **校勘与字词辨析（双语）**：
  - **中文**："雠"通"仇"，复仇之意。此处用拟人化手法说明五行制衡机制。
  - **English**："复雠" (avenging) uses anthropomorphic metaphor to explain the checks-and-balances mechanism in five elements dynamics."""
    normalized_text_zh: str = """"""
    subject: str = "五行相克与子母复仇"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_五行相克与子母复仇_001_L1",
    )
    version: str = "1.0.0"
