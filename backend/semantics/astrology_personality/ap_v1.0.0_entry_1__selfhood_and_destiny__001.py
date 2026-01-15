"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238309
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
    semantic_id="ap_v1.0.0_entry_1__selfhood_and_destiny__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1SelfhoodAndDestiny(SemanticEntry):
    """
    **Source Text** (Lines 13488-13611):
> It is said that on the portal of the temple of Delphi in anci...
    """
    
    original_text: str = """**Source Text** (Lines 13488-13611):
> It is said that on the portal of the temple of Delphi in ancient Greece one could see inscribed these words: KNOW THYSELF... We claim that a new basic life-problem is confronting the "New World" of the West... The new life-problem... is the problem of fulfillment. And thus we present... a key-utterance: FULFILL THYSELF.
>
> Knowledge and Fulfillment: two words of tremendous importance... they can be seen to correspond respectively to two other mighty words: Space and Time. Knowledge is spatial in its essence... Fulfillment is durational and cyclic—holistic.
>
> Selfhood and Destiny. These two terms can be referred respectively to the radical chart, and to the progressions derived therefrom; also to space and time, knowledge and fulfillment.

**Key Term Analysis**:
- **Know Thyself vs Fulfill Thyself**: `Greek vs American` / `knowledge vs fulfillment`
- **Space and Time**: `knowledge = spatial` / `fulfillment = durational`
- **Selfhood**: `radical chart` / `space factor` / `seed-form` / `changeless`
- **Destiny**: `progressions` / `time factor` / `schedule of unfoldment`

**English Paraphrase (Primary Language)**:
"KNOW THYSELF" (Greek, spatial, knowledge) → "FULFILL THYSELF" (American, durational, fulfillment).

Selfhood = radical chart = space = knowledge = seed-form (changeless).
Destiny = progressions = time = fulfillment = schedule of unfoldment.

"Fulfillment is durational and cyclic—holistic... it follows a well-definable rhythm with computable climaxes and critical phases."

"Destiny is selfhood in the becoming. Fulfillment is knowledge demonstrated."

**Complete Chinese Interpretation (Secondary Language)**:
"认识你自己"（希腊，空间的，知识）→"实现你自己"（美国，持续的，实现）。

自性 = 本命盘 = 空间 = 知识 = 种子形式（不变）。
命运 = 推运 = 时间 = 实现 = 展开的时间表。

"实现是持续的和周期性的——整体性的……它遵循可定义的节奏，有可计算的高潮和关键阶段。"

"命运是正在成为中的自性。实现是被证明的知识。"

**Narrative Snippets**:
- `[ns_aop_207]` `[trigger: know_fulfill]` `[factor_trigger: astro_fulfill_thyself]` `[role: 主干]` Know Thyself (Greek/spatial) vs Fulfill Thyself (American/durational); knowledge vs fulfillment. → L13489-13510
- `[ns_aop_208]` `[trigger: selfhood_destiny]` `[factor_trigger: astro_selfhood_vs_destiny AND astro_selfhood AND astro_destiny]` `[role: 总结]` Selfhood = radical chart/space; Destiny = progressions/time. Destiny = selfhood in becoming. → L13609-13611"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Selfhood and Destiny - Knowledge and Fulfillment"
    factor_refs: list = ['selfhood_astro', 'destiny_astro', 'fulfill_self']
    
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
        l1_anchor="ap_v1.0.0_entry_1__selfhood_and_destiny__001_L1",
    )
    version: str = "1.0.0"
