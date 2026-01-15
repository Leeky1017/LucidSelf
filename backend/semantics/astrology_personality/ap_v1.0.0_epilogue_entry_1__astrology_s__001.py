"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238385
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
    semantic_id="ap_v1.0.0_epilogue_entry_1__astrology_s__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class EpilogueEntry1AstrologyS(SemanticEntry):
    """
    **Source Text** (Lines 15904-15955):
> We hope that... one thing has been made to stand out in clear...
    """
    
    original_text: str = """**Source Text** (Lines 15904-15955):
> We hope that... one thing has been made to stand out in clear relief: The fact that the validity and power of astrology depend primarily on the manner in which it is made to serve the universal goal of "more wholeness"—the goal of individuation for the particular man, and the goal of Living Civilization for humanity as a whole...
>
> Unless astrology is put to use as a revealer of vital significances and of patterns of organic relationships, as a means of probing the secret formulas of all beginnings with the view to leading us to a better consummation—in other words, as a technique of personality-integration—it remains a merely intellectual speculation... or else a dangerous game of fortune-telling.

**Key Term Analysis**:
- **Validity depends on purpose**: `serve goal of more wholeness` / `individuation` / `Living Civilization`
- **Revealer of significances**: `vital significances` / `organic relationships` / `secret formulas of beginnings`
- **Personality-integration technique**: `not intellectual speculation` / `not fortune-telling`
- **Art not science**: `interpretative art` / `individual element enters`

**English Paraphrase (Primary Language)**:
Astrology's "validity and power depend primarily on... serving the universal goal of 'more wholeness'"—individuation for person, Living Civilization for humanity.

Unless astrology = "revealer of vital significances and patterns of organic relationships," it's "merely intellectual speculation or dangerous fortune-telling."

Astrology as "technique of personality-integration"—not science but "interpretative art."

"The main purpose is to contribute to the successful completion of the Great Work of man—that by which man reaches fulfillment and operative wholeness."

**Complete Chinese Interpretation (Secondary Language)**:
占星学的"有效性和力量主要取决于……服务于'更多整体性'的普遍目标"——个人的个体化，人类的活文明。

除非占星学 = "重要意义和有机关系模式的揭示者"，否则它只是"纯粹的智力推测或危险的算命游戏"。

占星学作为"人格整合技术"——不是科学而是"解释性艺术"。

"主要目的是为人类伟大工作的成功完成做出贡献——通过它人达到实现和运作的整体性。"

**Narrative Snippets**:
- `[ns_aop_223]` `[trigger: astro_purpose]` `[factor_trigger: astro_wholeness_goal AND astro_wholeness AND astro_living_civ]` `[role: 主干]` Astrology's validity = serving goal of "more wholeness"; individuation + Living Civilization. → L15906-15919
- `[ns_aop_224]` `[trigger: personality_integration]` `[factor_trigger: astro_great_work]` `[role: 总结]` Astrology = technique of personality-integration; contributes to Great Work of man. → L15943-15948"""
    normalized_text_zh: str = """"""
    subject: str = "Epilogue Entry 1: Astrology's Ultimate Purpose - Wholeness and Individuation"
    factor_refs: list = ['more_wholeness', 'living_civ', 'pers_integ']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_epilogue_entry_1__astrology_s__001_L1",
    )
    version: str = "1.0.0"
