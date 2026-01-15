"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386876
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
    semantic_id="ld_v1.0.0_water__emotions_unconscious_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class WaterEmotionsUnconscious(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Water | Emotions/unconsc...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Water | Emotions/unconscious | Universal symbol |
| Clarity/Murky | Emotional state | Clear=clarity |
| Depth | Consciousness level | Surface/deep |
| Variations | Ocean/river/flood | Specific meanings |

**Source Text** (Paraphrased):
> "Water universally represents emotions and the unconscious. Ocean = vast unconscious, River = life flow, Rain = emotional cleansing, Flood = overwhelming emotions. Water clarity reflects emotional state: clear water = emotional clarity, murky water = confusion. Depth matters: Surface water = conscious emotions, Deep water = unconscious depths."

**English Paraphrase**:
**Water**: universal symbol for **emotions and unconscious**. Variations: **Ocean** = vast unconscious depths; **River** = life flow, change current; **Rain** = emotional cleansing, release; **Flood** = overwhelming emotions, loss of control; **Still water** = emotional peace. **Clarity** = emotional state (clear = clarity, murky = confusion). **Depth** = consciousness level (surface = conscious, deep = unconscious).

**Complete Chinese Interpretation**:
**水**：**情绪与无意识**的普遍象征。变体：**海洋**=广阔无意识深处；**河流**=生命流动、改变潮流；**雨**=情绪净化、释放；**洪水**=压倒性情绪、失控；**静水**=情绪平和。**清晰度**=情绪状态（清澈=清晰、浑浊=混乱）。**深度**=意识层次（表面=有意识、深=无意识）。

#### Core Points

- **Universal Symbol**: Water universally represents emotions and the unconscious.
- **Clarity = Emotional State**: Clear water = emotional clarity; murky water = confusion.
- **Depth = Consciousness Level**: Surface water = conscious emotions; deep water = unconscious depths.
- **Variations**: Ocean = vast unconscious; River = life flow; Rain = cleansing; Flood = overwhelm.
- **Cross-cultural**: One of the most universal dream symbols worldwide.

#### Detailed Explanation

Water universally represents emotions and the unconscious. The variations carry specific meanings: Ocean = vast unconscious depths; River = life flow, change current; Rain = emotional cleansing, release; Flood = overwhelming emotions, loss of control; Still water = emotional peace. Water clarity reflects emotional state: clear water = emotional clarity, murky water = confusion. Depth matters: surface water = conscious emotions, deep water = unconscious depths."""
    normalized_text_zh: str = """"""
    subject: str = "Water (Emotions/Unconscious)"
    factor_refs: list = ['dream_symbol_water', 'dream_symbol_ocean', 'dream_symbol_river', 'dream_symbol_flood', 'dream_water_clarity']
    
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
        l1_anchor="ld_v1.0.0_water__emotions_unconscious_001_L1",
    )
    version: str = "1.0.0"
