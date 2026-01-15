"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424274
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
    semantic_id="dvd_v1.0.0_back_背_脊柱_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Back背脊柱(SemanticEntry):
    """
    ### Source Text

> Strong backbone = confidence, conviction. Weak back = lack of conviction. In visi...
    """
    
    original_text: str = """### Source Text

> Strong backbone = confidence, conviction. Weak back = lack of conviction. In visions, back = strength and structure of the church.

**Positive**: Strengthened back = strong conviction. Burden taken from back = Lord removing pressure.
**Negative**: Broken back = strength taken. Turning back = rebellion. Stiff back = stubbornness (Jer 17:23).

### English Paraphrase

Back = strength, conviction. **Positive**: Strengthened = conviction growing. **Negative**: Broken = lost strength. Turning = rebellion.

### Chinese Interpretation（完整对等诠释）

背 = 力量、信念。**正面**：加强 = 信念增长。**负面**：折断 = 失去力量。转身 = 悖逆。

### Narrative Snippets

- `[ns_dav_b004]` `[trigger: 梦背部]` `[factor_trigger: dream_symbol_back]` `[role: 主干]` Back = strength and conviction—strengthened = growing, broken = lost. → Dreams Dictionary #Back
- `[ns_dav_b005]` `[trigger: 转身背向]` `[factor_trigger: dream_symbol_back AND back_condition]` `[role: 条件分支]` Turning back = rebellion, refusing God's word. → Dreams Dictionary #Back"""
    normalized_text_zh: str = """"""
    subject: str = "Back 背/脊柱"
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
        l1_anchor="dvd_v1.0.0_back_背_脊柱_001_L1",
    )
    version: str = "1.0.0"
