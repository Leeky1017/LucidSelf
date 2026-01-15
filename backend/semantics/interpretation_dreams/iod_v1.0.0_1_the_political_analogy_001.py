"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.471224
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
    semantic_id="iod_v1.0.0_1_the_political_analogy_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1ThePoliticalAnalogy(SemanticEntry):
    """
    **Source Text**:
"Whence comes the necessity for the dream distortion? I will explain by an analogy....
    """
    
    original_text: str = """**Source Text**:
"Whence comes the necessity for the dream distortion? I will explain by an analogy. The political writer who has unpleasant truths to tell to those in power finds himself in a similar position. If he tells everything frankly, the holder of power will suppress his speech. The writer must therefore modify and disguise his expression."

"The stricter the censorship, the more thorough the disguise, the more ingenious the means employed to put the reader on the track of the real meaning."

"What we have called the dream distortion proves actually to be an effect of the censorship exercised by the recognised tendencies of the ego upon the wishful stirrings which are in any way shocking."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Dream Censor | 梦的审查者 | Internal blocking agency | Core mechanism |
| Political Analogy | 政治类比 | Writer vs. censor | Explanatory model |
| Recognized Tendencies | 公认倾向 | Ego's moral standards | Censoring agency |
| Wishful Stirrings | 愿望冲动 | Unconscious desires | Censored content |
| Shocking | 令人震惊的 | Morally unacceptable | Why censored |

**English Paraphrase (Primary Language)**:

Freud introduces the **dream censor** through a political analogy: A writer who wishes to criticize those in power cannot speak frankly—the authorities will suppress his work. He must **disguise** his message so it passes the censor while still communicating to discerning readers.

The dream censor works identically:
- **Ego** (with its moral standards) = the authorities
- **Unconscious wishes** (often sexual, aggressive, forbidden) = the critical message
- **Distortion** = the disguise that allows the wish to pass
- **Manifest dream** = the censored, publishable version
- **Latent dream** = the original, forbidden message

The stricter the moral standards, the more thorough the disguise. A Victorian dreamer has more distortion than a child because more wishes are forbidden.

This explains why **children's dreams are transparent**: few wishes are yet forbidden. Adults have internalized prohibitions; their censor works overtime.

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德通过政治类比引入**梦的审查者**：一个想批评当权者的作家不能坦率地说——当局会压制他的作品。他必须**伪装**他的信息，使其通过审查者，同时仍能与明眼读者沟通。

梦的审查者运作方式相同：
- **自我**（及其道德标准）= 当局
- **无意识愿望**（通常是性的、攻击性的、被禁止的）= 批评信息
- **伪装** = 允许愿望通过的变装
- **显梦** = 经过审查的、可发表的版本
- **隐梦** = 原始的、被禁止的信息

道德标准越严格，伪装越彻底。维多利亚时代的梦者比儿童有更多伪装，因为更多愿望被禁止。

这解释了为什么**儿童梦是透明的**：很少有愿望被禁止。成人已内化禁令；他们的审查者加班工作。

**Narrative Snippets**:

- `[ns_freud_dist_004]` `[trigger: censor_analogy]` `[factor_trigger: dream_censor AND dream_distortion]` `[role: 主干]` The political analogy: A writer who has unpleasant truths to tell those in power must disguise his expression—the dream censor works identically on forbidden wishes. → Freud Ch.IV #Censor
- `[ns_freud_dist_005]` `[trigger: stricter_censor]` `[factor_trigger: moral_training AND dream_censor]` `[role: 主干依赖]` The stricter the censorship, the more thorough the disguise—Victorian morality produces more elaborate dream distortion than childhood innocence. → Freud Ch.IV #Censor
- `[ns_freud_dist_006]` `[trigger: ego_censor]` `[factor_trigger: dream_censor AND dream_ego]` `[role: 主干依赖]` Dream distortion is the effect of censorship exercised by the ego's recognized tendencies upon wishful stirrings which are in any way shocking. → Freud Ch.IV #Censor"""
    normalized_text_zh: str = """"""
    subject: str = "1 The Political Analogy"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_1_the_political_analogy_001_L1",
    )
    version: str = "1.0.0"
