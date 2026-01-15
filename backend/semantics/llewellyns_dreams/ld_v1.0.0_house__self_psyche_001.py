"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386911
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
    semantic_id="ld_v1.0.0_house__self_psyche_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class HouseSelfPsyche(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| House | Self/psyche stru...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| House | Self/psyche structure | Universal symbol |
| Rooms | Personality aspects | Attic/basement/etc |
| House Condition | Psyche health | Maintained/dilapidated |
| Vertical Axis | Consciousness levels | Attic=high, basement=low |

**Source Text** (Paraphrased):
> "House symbolizes self and psyche structure. Different rooms represent different personality aspects: Attic = higher consciousness/spirituality, Basement = unconscious/shadow, Bedroom = intimate self/sexuality, Kitchen = nourishment/self-care, Bathroom = cleansing/release. House condition reflects psyche state: Well-maintained = healthy psyche, Dilapidated = neglected self."

**English Paraphrase**:
**House**: **symbol of self/psyche**. Rooms = personality aspects: **Attic** = higher consciousness, spirituality, superconscious; **Basement** = unconscious, shadow, repressed material; **Bedroom** = intimate self, sexuality, privacy; **Kitchen** = nourishment, how self fed/cared for; **Bathroom** = cleansing, emotional release, elimination. **House condition** = psyche state: Well-maintained = healthy; Dilapidated = neglected; Under construction = transformation in process.

**Complete Chinese Interpretation**:
**房屋**：**自我/心理象征**。房间=人格面相：**阁楼**=更高意识、灵性、超意识；**地下室**=无意识、阴影、被压抑材料；**卧室**=亲密自我、性、隐私；**厨房**=滋养、自我被喂养/照顾方式；**浴室**=净化、情绪释放、排除。**房屋状况**=心理状态：维护良好=健康；破败=被忽视；建设中=转化进行中。

#### Core Points

- **Self/Psyche Symbol**: House symbolizes self and psyche structure.
- **Rooms = Aspects**: Different rooms represent different personality aspects.
- **Vertical Axis**: Attic = higher consciousness; Basement = unconscious/shadow.
- **Functional Rooms**: Kitchen = nourishment; Bedroom = intimacy; Bathroom = cleansing.
- **House Condition**: Well-maintained = healthy psyche; dilapidated = neglected self.

#### Detailed Explanation

House symbolizes self and psyche structure. Different rooms represent different personality aspects: Attic = higher consciousness, spirituality; Basement = unconscious, shadow, repressed material; Bedroom = intimate self, sexuality; Kitchen = nourishment, self-care; Bathroom = cleansing, emotional release. House condition reflects psyche state: well-maintained = healthy psyche; dilapidated = neglected self; under construction = transformation in process."""
    normalized_text_zh: str = """"""
    subject: str = "House (Self/Psyche)"
    factor_refs: list = ['dream_symbol_house', 'dream_symbol_attic', 'dream_symbol_basement', 'dream_symbol_bedroom', 'dream_symbol_kitchen', 'dream_house_condition']
    
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
        book_id="llewellyns_dreams",
        chapter="",
        l1_anchor="ld_v1.0.0_house__self_psyche_001_L1",
    )
    version: str = "1.0.0"
