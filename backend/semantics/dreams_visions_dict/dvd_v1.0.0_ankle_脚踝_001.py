"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439763
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
    semantic_id="dvd_v1.0.0_ankle_脚踝_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ankle脚踝(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: A sensitive area or a point of weakness in your life.

**Pos...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: A sensitive area or a point of weakness in your life.

**Positive** (Acts 3:7): "Immediately his feet and ankle bones received strength." If you dream of your ankle being healed or getting stronger, this refers to a weakness that has been made strong. Likely refers to a character flaw or weakness you have faced and overcome.

**Negative**: Your ankle is often a point of weakness. If you injure your foot, it is likely to occur at the ankle. If you dream of hurting or twisting your ankle, it is referring to a weakness tripping you up. Although strong in other areas, this single weakness has power to trip you—could be character flaw or spiritual weakness.

**See also**: Barefoot, Leg, Feet

### English Paraphrase

Ankle = point of weakness. **Positive**: Ankle healed/strengthened = weakness overcome, character flaw faced and conquered (Acts 3:7 parallel). **Negative**: Ankle hurt/twisted = weakness tripping you up. One weakness can derail you despite other strengths—examine character flaws or spiritual vulnerabilities.

### Chinese Interpretation（完整对等诠释）

脚踝 = 软弱之处。**正面**：脚踝被医治/加强 = 软弱被克服，性格缺陷已面对并战胜（徒3:7对应）。**负面**：脚踝受伤/扭伤 = 软弱绊倒你。尽管在其他方面强大，一个软弱就能使你跌倒——检查性格缺陷或属灵弱点。

### Narrative Snippets

- `[ns_dav_a057]` `[trigger: 梦脚踝]` `[factor_trigger: dream_symbol_ankle]` `[role: 主干]` Ankle = point of weakness—healed = overcome, hurt = tripping you up. → Dreams Dictionary #Ankle
- `[ns_dav_a058]` `[trigger: 脚踝正面]` `[factor_trigger: dream_symbol_ankle AND ankle_condition]` `[role: 条件分支]` Ankle healed/strengthened = weakness overcome, character flaw conquered. → Dreams Dictionary #Ankle
- `[ns_dav_a059]` `[trigger: 脚踝负面]` `[factor_trigger: dream_symbol_ankle AND ankle_condition]` `[role: 条件分支]` Ankle hurt/twisted = weakness tripping you despite other strengths. → Dreams Dictionary #Ankle"""
    normalized_text_zh: str = """"""
    subject: str = "Ankle 脚踝"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_ankle_脚踝_001_L1",
    )
    version: str = "1.0.0"
