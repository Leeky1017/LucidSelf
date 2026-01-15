"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.552708
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
    semantic_id="acu_v1.0.0_310_kore在男性与女性中的不同意义_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 310Kore在男性与女性中的不同意义(SemanticEntry):
    """
    **原文** (§310, 行5217-5229):

> [310] The above types are far from exhausting all the statistical regu...
    """
    
    original_text: str = """**原文** (§310, 行5217-5229):

> [310] The above types are far from exhausting all the statistical regularities in this respect. The figure of the Kore that interests us here belongs, when observed in a man, to the anima type; and when observed in a woman to the type of supraordinate personality. It is an essential characteristic of psychic figures that they are duplex or at least capable of duplication; at all events they are bipolar and oscillate between their positive and negative meanings. Thus the "supraordinate" personality can appear in a despicable and distorted form, like for instance Mephistopheles, who is really more positive as a personality than the vapid and unthinking careerist Faust.

**英文释义（主语言）**:

**Kore的性别差异意义**：
Kore的形象在**男性中**属于**阿尼玛类型**；在**女性中**属于**超位人格类型**。

**心理形象的双重性**：
心理形象的本质特征是它们是**双重的**或至少能够**复制**；无论如何它们是**双极的**，在正面和负面意义之间**摆动**。

**超位人格的负面形式**：
"超位"人格可以以可鄙和扭曲的形式出现，如**梅菲斯托费勒斯**——他作为人格实际上比空洞无思想的野心家浮士德更为正面。

**得墨忒耳-科瑞的女性主导**：
在女性中，与Kore对应的形象通常是双重的，即母亲和少女。荣格推断，在得墨忒耳-科瑞神话的形成中，女性影响远超男性，后者几乎没有意义。男性在得墨忒耳神话中的角色实际上只是诱惑者或征服者。

**完整中文诠释（次语言）**:

**Kore的性别差异功能**：
Kore的形象在**男性中**属于**阿尼玛类型**——代表男性心灵中的女性成分；在**女性中**属于**超位人格类型**——代表女性的更大人格整体。

**心理形象的本质双极性**：
心理形象的本质特征是它们是**双重的**或至少能够复制；无论如何它们是**双极的**，在正面和负面意义之间摆动。因此"超位"人格可以以可鄙和扭曲的形式出现，如梅菲斯托费勒斯——他作为人格实际上比空洞无思想的野心家浮士德更为正面。

**神话中的性别主导**：
另一个负面形象是童话中的拇指汤姆或傻汉斯。在女性中，与Kore对应的形象通常是双重的，即母亲和少女——她时而以这个形式出现，时而以那个形式出现。由此荣格推断，在得墨忒耳-科瑞神话的形成中，女性影响远超男性，后者几乎没有意义。男性在得墨忒耳神话中的角色实际上只是诱惑者或征服者。

**核心要点**:
- Kore在男性中 = 阿尼玛类型
- Kore在女性中 = 超位人格类型
- 心理形象本质上是双重的、双极的
- 正负面之间摆动（如梅菲斯托vs浮士德）
- 女性中Kore常显现为母亲+少女双重形象
- 得墨忒耳-科瑞神话由女性心理主导

**叙事片段**:
- `[ns_cw9i_V_310_001]` `[trigger: kore_gender]` `[factor_trigger: jung_kore AND jung_gender]` `[role: 主干]` Kore在男性中=阿尼玛，在女性中=超位人格——心理形象本质双重双极。→ §310"""
    normalized_text_zh: str = """"""
    subject: str = "§310 Kore在男性与女性中的不同意义"
    factor_refs: list = ['engine_id', 'kore_male_anima', 'psych_semantic', 'kore_female_self', 'psych_semantic', 'bipolarity', 'psych_semantic']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_310_kore在男性与女性中的不同意义_001_L1",
    )
    version: str = "1.0.0"
