"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076582
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
    semantic_id="bot_v1.0.0_queen_of_swords__宝剑皇后_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class QueenOfSwords宝剑皇后(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Water of Air | Sensitive intellect | Elastic transmission |
| Child's Head Crest | Fresh intelligence | Sharp light rays |
| Severed Head | Cut bonds | Liberation act |
| Liberator of Mind | Truth force | Clears delusion |

**Title**: Queen of the Thrones of Air (气之宝座的皇后)
**Elemental**: The Watery part of Air (气中之水)
**Zodiac**: 21° Virgo to 20° Libra (处女座21度至天秤座20度)

**Source Text**:
> "The Queen of Swords represents the watery part of Air, the elasticity of that element, and its power of transmission. She rules from the 21st degree of Virgo to the 20th degree of Libra. She is enthroned upon the clouds... Her helmet is crested by the head of a child, and from it stream sharp rays of light... In her right hand, she bears a sword; in her left hand, the newly severed head of a bearded man. She is the clear, conscious perception of Idea, the Liberator of the Mind... If ill-dignified... cruel, sly, deceitful and unreliable... dangerous on account of the superficial beauty and attractiveness."

**English Paraphrase**:
**Clear‑Cut Perception** – Represents the **Watery part of Air**: sensitivity, elasticity and transmission of thought. She sits on clouds, crowned with a child's head from which sharp rays of light stream – symbol of **fresh, lucid intelligence**. In one hand she wields a sword; in the other she holds a freshly severed head, showing her readiness to cut away falsehood, illusion and dependency. She is **conscious, discriminating perception**, the one who frees the mind by naming and cutting. Positively, she is fair, keen, honest, insightful; negatively, she can turn those same powers into **cruelty, manipulation and cold detachment**, hiding behind grace and beauty.

**Core**: **Discerning Clarity** – Honest insight, critical thinking, cutting through illusions, but also potential coldness.

**Chinese Explanation**:
**宝剑皇后**代表**气中之水**——带有情感敏锐度与流动性的理性。她端坐在云端，头盔以**孩童之首**为饰，射出锐利光芒，象征**新鲜、清澈的心智之光**。右手执剑，左手提着刚被斩下的胡须男头，显示她愿意**斩断虚伪、情感依附与自我欺骗**。正位时，她是极具判断力与洞察力的人：公正、理性、敢于说真话，也能帮他人从困境与迷雾中醒来。失衡时，这种洞察会反转为**刻薄、冷酷、算计与背后中伤**，因为她的聪明与外在吸引力使她在伤害他人时更难被察觉与防御。

**In Readings**: Clear‑sighted woman, truth‑telling, honest analysis, cutting ties, objectivity; or, harsh criticism, manipulation, cold rejection.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Queen of Swords is Water of Air - elasticity and transmission. Child's head crest radiates sharp light. Severed head shows cutting away falsehood. Liberator of Mind, but can be cruel if ill-dignified.
- **中文**: Crowley的宝剑皇后是气中之水—弹性与传递。孩童头纹章放射锐利光芒。被斩之首显示斩断虚假。心智解放者，但失衡时可能残忍。

**Narrative Snippets**:
- `[ns_thoth_swords_034]` `[trigger: queen_swords_thoth]` `[factor_trigger: thoth_swords_queen]` `[role: 主干]` Queen of Swords = Water of Air—elasticity and transmission; clear perception; Liberator of Mind. → Core
- `[ns_thoth_swords_035]` `[trigger: child_head_crest]` `[factor_trigger: thoth_swords_queen AND symbol_child_head]` `[role: 条件分支]` Child's head crest radiates sharp light—fresh lucid intelligence; sword + severed head. → Visual
- `[ns_thoth_swords_036]` `[trigger: cruel_deceiver]` `[factor_trigger: thoth_swords_queen AND state_ill_dignified]` `[role: 条件分支]` If ill-dignified: cruel, sly, deceitful—dangerous due to superficial beauty and attractiveness. → Shadow"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Swords (宝剑皇后)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_thoth_swords_queen', 'thoth_swords_queen', 'expressing', 'evi_thoth_swords_queen', 'thoth_swords_queen', 'rule_thoth_swords_queen', 'concept_thoth_swords_queen', 'decan_zodiac', 'archetype']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_queen_of_swords__宝剑皇后_001_L1",
    )
    version: str = "1.0.0"
