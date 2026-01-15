"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482440
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
    semantic_id="iod_v1.0.0_source_text_009",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "In every dream it is possible to find a point of contact with the experiences of the previous day. ...
    """
    
    original_text: str = """"In every dream it is possible to find a point of contact with the experiences of the previous day. Every dream contains some reference to the experiences of the preceding day, though this reference may be of the most remote and disguised character. Even the most elaborate dream has borrowed some element from the immediate past."

#### English Paraphrase (Primary Language)

Day residues are recent experiences, typically from the preceding day, that provide raw material for dream construction. Every dream, without exception, incorporates some reference to the previous day's events, thoughts, or perceptions—though this connection may be highly disguised or involve trivial details. The day residue serves a crucial function: it provides the preconscious material that can be used to represent unconscious infantile wishes. An ancient unconscious wish (perhaps decades old) cannot directly form a dream; it requires connection to recent preconscious material (day residue) that provides the "hook" allowing the unconscious wish to achieve representation. The day residue is often insignificant in itself—a fleeting impression, overheard conversation, or trivial incident—selected precisely because it offers associative connections to the underlying unconscious wish.

#### Complete Chinese Interpretation

**日间余留**指的是紧邻梦之前一两天内的清醒经验——看到的场景、听到的话、偶然翻到的一段文字，甚至只是路过时短暂的一瞥。弗洛伊德强调，几乎每一个梦都能在其中找到这种“昨日残渣”的痕迹：哪怕是结构极其复杂的梦，其材料中也至少有一小部分可追溯到前一天或前几天的事件。

然而，日间余留本身往往并不重要：它可能只是一个无足轻重的段子、一句随口之言或一件微不足道的小事。真正赋予它意义的，是它在联想网络中与**古老无意识愿望**之间建立的桥梁。久远的童年欲望本不能直接“上台唱戏”，只有当它找到某个与之有关联的近期印象时，才有机会借这块新近的感知材料“挂钩”，进入梦的构造过程——日间余留正是这块“挂钩点”。

因此，理解日间余留的关键，不在于高估昨天发生了什么，而在于从这些看似随机的碎片向下追溯：为什么在无数昨日经验中，正是这一个细节被选中进入梦？它在情绪色彩、象征联想或人际结构上，与更深层的无意识主题有何对应？这样，日间余留就从单纯的“原料”，变成解开梦中深层愿望与当前生活情境如何**捆绑在一起**的重要线索。

#### Core Points

- **Universal presence**: Every dream contains reference to previous day's experiences
- **Preconscious material**: Recent experiences provide representable content
- **Connection function**: Links ancient unconscious wishes to current material
- **Often trivial**: Insignificant details selected for associative value
- **Necessary but insufficient**: Required for dream but doesn't explain dream's meaning

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Day Residues (Tagesreste) | Previous day's experiences | Universal in dreams |
| Preconscious Material | Recent accessible content | Provides raw material |
| Connection Function | Links wishes to content | Bridge old-new |
| Selection by Association | Why this detail? | Reveals underlying wish |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Day residues: every dream contains previous day's material. Often trivial. Links ancient unconscious wishes to recent content. Necessary but not sufficient.
- **中文**: 日间余留:每个梦都包含前一天的材料。往往琐碎。连接古老无意识愿望与近期内容。必要但不充分。

**Narrative Snippets**:
- `[ns_freud_mech_033]` `[trigger: day_residues]` `[factor_trigger: dream_day_residue AND dream_universal]` `[role: 主干]` Every dream contains some reference to the experiences of the preceding day—this connection may be highly disguised or involve trivial details. → Day Residue
- `[ns_freud_mech_034]` `[trigger: connection_function]` `[factor_trigger: dream_day_residue AND dream_wish]` `[role: 条件分支]` Day residue provides the "hook" allowing ancient unconscious wishes (perhaps decades old) to achieve representation in dreams. → Connection
- `[ns_freud_mech_035]` `[trigger: trivial_selection]` `[factor_trigger: dream_day_residue AND dream_association]` `[role: 条件分支]` Day residue is often insignificant in itself—selected precisely because it offers associative connections to underlying unconscious wishes. → Selection"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_source_text_009_L1",
    )
    version: str = "1.0.0"
