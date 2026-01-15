"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.122602
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
    semantic_id="tis_v1.0.0_tenth_house___the_midheaven__c_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class TenthHouseTheMidheavenC(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Destiny vs Job | True ro...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Destiny vs Job | True role vs rent | Core distinction |
| Natural Authority | Authentic power | Success |
| Impostor Syndrome | Hollow role | Failure |
| Getting Paid for Self | Authentic career | Goal |

#### Source Text

"The midheaven represents that which is most obvious about us. How we look from a social distance. To navigate tenth-house terrain successfully, we must find our destiny. We must find a social role that is in harmony with our inner nature. We must figure out a way to get paid for being ourselves."

#### English Paraphrase

The **Tenth House** (Midheaven) is the arena of **career, public reputation, and destiny**. It represents our standing in the community and our contribution to the world.

**Public Identity**:
- **Social Distance**: How strangers see us (labels, titles, status).
- **Role**: The function we perform for the tribe (Doctor, Teacher, Leader).

**Career vs. Destiny**:
- **Job**: Just paying rent.
- **Destiny**: A social role rooted in our true nature. Getting paid for being who we truly are.

**The Challenge**:
To avoid playing a hollow role ("impostor syndrome") and instead create a public identity that is an authentic extension of the inner self.

**Success**:
Having **natural authority**. When our public role matches our private truth, we are unshakeable. "No one else could play our part."

**Failure**:
Being successful by society's standards but feeling empty and illegitimate inside. Clinging to power because we know it's not really ours.

#### Complete Chinese Interpretation

**第十宫**（中天）是**事业、公众声誉和命运**的领域。它代表我们在社区中的地位以及我们要对世界做出的贡献。

**公众身份**：
- **社会距离**：陌生人如何看我们（标签、头衔、地位）。
- **角色**：我们为部落执行的功能（医生、教师、领袖）。

**事业 vs. 命运**：
- **工作**：只是付房租。
- **命运**：扎根于我们真实本性的社会角色。因为做真实的自己而获得报酬。

**挑战**：
避免扮演空洞的角色（"冒名顶替综合症"），而是创造一个作为内在自我真实延伸的公众身份。

**成功**：
拥有**自然权威**。当我们的公众角色与我们的私人真理相匹配时，我们是不可动摇的。"没有其他人能扮演我们的角色。"

**失败**：
按社会标准成功但内心感到空虚和不合法。紧抓权力因为我们知道那并不真正属于我们。

#### Core Points

- Arena of career, status, and public identity.
- Finding one's destiny (authentic contribution).
- Getting paid for being oneself.
- Natural authority vs. hollow status.
- East parallel: 官禄宫/正官/事业 (Career Palace, Authority, Status).

#### Detailed Explanation

The Tenth House (Midheaven) governs **public identity, career, and status**—how we appear to people who don't know us personally. They see us as representatives of social functions: "doctor," "artist," "activist." This depersonalized perception is inescapable in social life.

The developmental task is finding one's **destiny**: a social role that expresses inner nature. Forrest frames it as "getting paid for being yourself." When work aligns with authentic self, we bring full force to our public role and feel naturally authoritative. No one else could do our part because it emerges from who we uniquely are.

**Unsuccessful navigation** may produce external success without inner alignment—wealth and status that feel hollow and illegitimate. The person senses they're playing a part they didn't create, and clings desperately to position because they know it's not truly theirs. **Successful navigation** means finding the intersection of inner truth and outer contribution.

#### Narrative Snippets

- `[ns_innersky_h10_001]` `[trigger: house_10_general]` `[factor_trigger: astro_house_10]` `[role: 主干]` The midheaven represents how we look to people who do not know us. They see us, not as people, but as embodiments of various functions in society. Depersonalized. Representative of a class. They see our status. → The Inner Sky Ch.7 #10H
- `[ns_innersky_h10_002]` `[trigger: house_10_destiny]` `[factor_trigger: astro_house_10 AND astro_state_success]` `[role: 主干依赖]` To navigate tenth-house terrain successfully, we must find our destiny. We must find a social role that is in harmony with our inner nature. We must figure out a way to get paid for being ourselves. → The Inner Sky Ch.7 #10H
- `[ns_innersky_h10_003]` `[trigger: house_10_success]` `[factor_trigger: astro_house_10 AND astro_state_success]` `[role: 条件分支]` If we succeed, we are at home in the world. Our work, our status, our public identity—all reflect what is going on inside us. We bring the full force of our being to bear upon our public role. → The Inner Sky Ch.7 #10H
- `[ns_innersky_h10_004]` `[trigger: house_10_impostor]` `[factor_trigger: astro_house_10 AND astro_state_dysfunction]` `[role: 条件分支]` We may become wealthy. We may be glamorous. We may have influence. But these facts do not reflect who we are. They only describe a part we have been given to play. We feel like an impostor. → The Inner Sky Ch.7 #10H
- `[ns_innersky_h10_005]` `[trigger: house_10_authenticity]` `[factor_trigger: astro_house_10 AND astro_state_success]` `[role: 总结]` No one else could play our part. That part, whatever it may be, is rooted in our individuality. Knowing that, we feel absolutely secure in our public identity. No one can steal it from us because no one else could do it. → The Inner Sky Ch.7 #10H"""
    normalized_text_zh: str = """"""
    subject: str = "Tenth House - The Midheaven (Career & Destiny)"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_tenth_house___the_midheaven__c_001_L1",
    )
    version: str = "1.0.0"
