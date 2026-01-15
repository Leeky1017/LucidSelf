"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.840345
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
    semantic_id="mlxj_v1.0.0_1_见老人_老幼类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1见老人老幼类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

见老人，大吉。梦见之者，或系神物，或系亡灵，或告以福庆，或告以祸患，详其形像，推其指示，兆吉则吉，兆凶则凶。大凡须眉皓白之人，来形梦寐，主寿年绵永，财帛丰盈...
    """
    
    original_text: str = """#### 原文（source_text）

见老人，大吉。梦见之者，或系神物，或系亡灵，或告以福庆，或告以祸患，详其形像，推其指示，兆吉则吉，兆凶则凶。大凡须眉皓白之人，来形梦寐，主寿年绵永，财帛丰盈之占也。

#### 规范化释义（primary_lang_explained）

梦见老人，大吉。做此梦者，所见老人或是神物，或是亡灵，或告以福庆，或告以祸患。应详审其形象，推究其指示，兆吉则吉，兆凶则凶。大凡须眉皓白之人来入梦，主寿年绵永、财帛丰盈之占。

#### 完整对等诠释（secondary_lang_full）

Dreaming of an elderly person is greatly auspicious. What appears may be a divine being, a departed spirit, coming to announce good fortune or warn of disaster. Examine the figure carefully, interpret the indication—if the omen is auspicious, fortune follows; if ominous, misfortune. Generally, when a white-bearded elder appears in dreams, it portends longevity and abundant wealth.

#### 核心要点

- 见老人=大吉（通则）
- 老人可能是：神物/亡灵/福庆使者/祸患警示
- 须眉皓白→寿年绵永、财帛丰盈
- 占断原则：详形像、推指示、随兆定吉凶

#### 典故

- **田千秋**：梦白头翁教言，后拜丞相
- **文处**：梦白头翁，明日果大霁
- **裴寂**：梦白头翁言「位极人臣」，后果应

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v6_003]` `[trigger: 梦见老人]` `[factor_trigger: dream_jian_laoren]` `[role: 主干]` 见老人，大吉。大凡须眉皓白之人，来形梦寐，主寿年绵永，财帛丰盈之占也。 → 《梦林玄解·卷六》#见老人"""
    normalized_text_zh: str = """"""
    subject: str = "1 见老人（老幼类首条·完整精校）"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_见老人_老幼类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
