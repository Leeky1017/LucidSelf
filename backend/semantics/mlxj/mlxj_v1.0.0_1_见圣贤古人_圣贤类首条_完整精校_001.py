"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.842907
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
    semantic_id="mlxj_v1.0.0_1_见圣贤古人_圣贤类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1见圣贤古人圣贤类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

见圣贤古人，贞吉，否，凶。此梦或神灵降感，或思虑潜通，如见大圣大贤，必有瑞征；如见文臣武将，必有奇应。详其见梦于何处，得梦于何日，并审其得梦者是何人品，处何...
    """
    
    original_text: str = """#### 原文（source_text）

见圣贤古人，贞吉，否，凶。此梦或神灵降感，或思虑潜通，如见大圣大贤，必有瑞征；如见文臣武将，必有奇应。详其见梦于何处，得梦于何日，并审其得梦者是何人品，处何时势，因人而论，因事而推，吉凶见矣。

#### 规范化释义（primary_lang_explained）

梦见圣贤古人，正则吉，否则凶。这种梦可能是神灵降临感应，也可能是思虑暗中相通。如果见到大圣大贤，必有祥瑞之征；如果见到文臣武将，必有奇异的应验。

应当详细审查：梦见于何处？得梦于何日？并审查做梦者是什么人品，处于什么时势，因人而论，因事而推，吉凶就能明白了。

#### 完整对等诠释（secondary_lang_full）

Dreaming of sages and ancient worthies—upright interpretation brings fortune, otherwise misfortune. Such dreams may arise from divine spirits descending in response, or from subconscious thoughts connecting. Seeing great sages and worthies portends auspicious signs; seeing civil or military officials portends remarkable fulfillments.

One should examine in detail: Where did the dream occur? On what day was the dream received? What is the character of the dreamer? What are the circumstances of the times? Interpret according to the person, deduce according to the matter, and fortune or misfortune will become clear.

#### 核心要点

- 圣贤梦象的双重来源：神灵降感 / 思虑潜通
- 大圣大贤→瑞征，文臣武将→奇应
- **四要素占断法**：何处+何日+何人品+何时势
- 「因人而论，因事而推」——核心方法论

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v4_004]` `[trigger: 梦见圣贤]` `[factor_trigger: dream_jian_shengxian]` `[role: 主干]` 见圣贤古人，贞吉，否，凶。此梦或神灵降感，或思虑潜通。 → 《梦林玄解·卷四》#见圣贤古人"""
    normalized_text_zh: str = """"""
    subject: str = "1 见圣贤古人（圣贤类首条·完整精校）"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="mlxj_v1.0.0_1_见圣贤古人_圣贤类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
