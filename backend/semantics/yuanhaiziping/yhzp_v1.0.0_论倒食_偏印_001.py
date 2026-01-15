"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558962
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
    semantic_id="yhzp_v1.0.0_论倒食_偏印_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论倒食偏印(SemanticEntry):
    """
    - **原文（source_text）**：倒食者，即偏印也；阴见阴，阳见阳，为生我之神。以其克我之食神，故谓之倒食，亦名枭神。主破耗、克子、孤贫、疾病、夺食之意。喜见财星制之，忌见食神被克。倒食多者...
    """
    
    original_text: str = """- **原文（source_text）**：倒食者，即偏印也；阴见阴，阳见阳，为生我之神。以其克我之食神，故谓之倒食，亦名枭神。主破耗、克子、孤贫、疾病、夺食之意。喜见财星制之，忌见食神被克。倒食多者为僧道孤独之命。

- **分字分词释义**：
  - **倒食/偏印**：生我之神且阴阳相同者，如甲木见壬水，壬水为甲木之偏印。
  - **阴见阴/阳见阳**：阴日干见阴印，阳日干见阳印，为偏印。
  - **克我之食神**：偏印克食神，是偏印名为"倒食"的原因。
  - **枭神**：偏印的别名，取枭鸟食母之意，凶恶之神。
  - **夺食**：偏印克食神，使食神不能生财，断其生路。
  - **破耗克子孤贫疾病**：倒食主的凶象——财破、子少、孤独、贫穷、疾病。
  - **财星制之**：财能克印，以财制偏印可化解枭神夺食。
  - **僧道孤独命**：偏印多者常为出家人或孤独终老。

- **规范化释义（primary_lang_explained）**：倒食（偏印）是生我且阴阳相同者，因克食神故名倒食或枭神。倒食主破耗、克子、孤贫、疾病，为夺食之意。倒食喜财星制（财克印），忌食神被克（倒食克食）。倒食多者为僧道孤独命。

- **完整对等诠释（secondary_lang_full）**：Reversed Eating (Indirect Seal) is what-generates-me with same polarity, named thus for controlling Eating God, also called Owl God. Reversed Eating indicates depletion, harming children, poverty/loneliness, illness—seizing-food meaning. Reversed Eating favors Wealth Star controlling it (Wealth controls Seal), taboos Eating God being controlled (Reversed Eating controls Eating God). Abundant Reversed Eating brings monastic/lonely fate.

- **核心要点**：
  - 倒食即偏印，生我且阴阳相同
  - 因克食神故名"倒食"，亦名"枭神"
  - 倒食主破耗、克子、孤贫、疾病
  - 倒食喜财星制之，财克印可化解
  - 忌食神被克，枭神夺食为大凶
  - 倒食多者为僧道孤独之命

- **详细解说**：  
  本条论述偏印（倒食/枭神）的性质与凶象。偏印是生我且阴阳相同者（如甲木见壬水），与正印的关键区别在于"克我之食神"——偏印克制食神，断绝食神生财之路，故名"倒食"（倒塌、断绝之意），又名"枭神"（取枭鸟食母之凶恶意象）。倒食的凶象是"破耗、克子、孤贫、疾病、夺食"——财破耗散、子女缘薄、孤独贫穷、疾病缠身，这都源于"夺食"——偏印克食神，断绝生财之源。化解之法是"财星制之"——以财克印，制住偏印使其不能夺食。特别警示"倒食多者为僧道孤独之命"——偏印过多，六亲无依，常为出家人或孤独终老。此条揭示了偏印的凶性本质。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_099]` `[trigger: 倒食定义]` `[factor_trigger: indirect_seal]` `[role: 主干]` 倒食者，即偏印也；阴见阴，阳见阳，为生我之神。 → 《渊海子平·论倒食》
  - `[ns_yhzp_100]` `[trigger: 倒食名由]` `[factor_trigger: indirect_seal AND seizing_food]` `[role: 主干依赖]` 以其克我之食神，故谓之倒食，亦名枭神。 → 《渊海子平·论倒食》
  - `[ns_yhzp_101]` `[trigger: 倒食凶象]` `[factor_trigger: seizing_food]` `[role: 主干依赖]` 主破耗、克子、孤贫、疾病、夺食之意。 → 《渊海子平·论倒食》
  - `[ns_yhzp_102]` `[trigger: 倒食喜财]` `[factor_trigger: direct_wealth AND indirect_seal]` `[role: 条件分支]` 喜见财星制之。 → 《渊海子平·论倒食》
  - `[ns_yhzp_103]` `[trigger: 倒食忌食]` `[factor_trigger: indirect_seal AND eating_god]` `[role: 例外处理]` 忌见食神被克。 → 《渊海子平·论倒食》
  - `[ns_yhzp_104]` `[trigger: 倒食孤独]` `[factor_trigger: indirect_seal AND sengdao AND daoshi_gudu]` `[role: 总结]` 倒食多者为僧道孤独之命。 → 《渊海子平·论倒食》"""
    normalized_text_zh: str = """"""
    subject: str = "论倒食/偏印"
    factor_refs: list = ['indirect_seal', 'seizing_food']
    
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
        l1_anchor="yhzp_v1.0.0_论倒食_偏印_001_L1",
    )
    version: str = "1.0.0"
