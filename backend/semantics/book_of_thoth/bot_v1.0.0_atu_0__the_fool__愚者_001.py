"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044405
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
    semantic_id="bot_v1.0.0_atu_0__the_fool__愚者_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class Atu0TheFool愚者(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Aleph (א) | First Hebrew letter, value 1 | Breath/spirit, highest path |
| Primordial Chaos | Pre-manifestation creative state | Zero pregnant with infinity |
| Holy Guardian Angel | Inner divine guide (Thelema) | True Will connection |
| Green Man | Celtic fertility spirit | Spring creative force |

**Qabalistic Correspondences**:
- **Hebrew Letter**: Aleph (א, value 1)
- **Path**: Connects Kether (Crown) to Chokmah (Wisdom) - highest path on Tree
- **Element**: Air (in Thoth system, vs Earth in some traditions)
- **Astrological**: Not assigned specific planet/sign (represents primordial chaos before manifestation)

**English Paraphrase**:

The **Fool** in Thoth system represents **primordial creative chaos** - the first stirring of divine consciousness before it takes form. Unlike Rider-Waite's innocent wanderer, Crowley's Fool is **actively chaotic**: a divine madness, the "Green Man" of spring fertility, the **Holy Guardian Angel** in its most primal aspect.

**Visual Key Elements**:
- Tiger (replacing dog): Primal instinctive force, not domesticated
- Crocodile/Set: Egyptian god of chaos, transformation through destruction
- Spiraling energy: Constant motion, nothing fixed or defined
- Dove and butterfly: Spirit and transformation emerging from chaos

**Core Meaning**:
The Fool is **zero pregnant with infinite possibility** - not absence but潜能 (potential) before manifestation. In Thelemic context, represents the moment before discovering True Will, the **divine spark** seeking expression. This is **holy madness** - abandoning rationality to access higher wisdom.

**Rider-Waite Comparison**:
- **RW**: Innocent beginning, childlike trust, lighthearted adventure
- **Thoth**: Primal chaos, divine madness, creative destruction, "Great Fool" of Celtic tradition
- **Shift**: From gentle innocence to ecstatic wildness

**完整中文诠释**: 透特系统中**愚者**代表**原始创造性混沌**——神圣意识在成形前的最初搅动。不同于Rider-Waite的无辜流浪者，Crowley的愚者**主动混沌**：神圣疯狂、春季生育的"绿人"、最原始面貌的**神圣守护天使**。卡巴拉对应：希伯来字母Aleph(א)、连接Kether至Chokmah的路径（生命之树最高路径）、风元素。视觉元素：老虎（非狗=原始本能力量非驯化）、鳄鱼/Set（埃及混沌之神通过破坏转化）、螺旋能量（恒动无固定）、鸽子与蝴蝶（从混沌中浮现的灵与转化）。核心含义：愚者是**零孕育无限可能**——非缺席而是显化前的潜能。泰勒玛语境中代表发现真实意志前的时刻、寻求表达的**神圣火花**。这是**神圣疯狂**——放弃理性以获取更高智慧。

#### Core Points

- **Primordial creative chaos**: The Fool symbolizes the first stirring of divine consciousness before form, not naive wandering.
- **Zero pregnant with infinity**: Card 0 stands outside the sequence, representing infinite potential before manifestation.
- **Holy madness and True Will**: Contact with the Holy Guardian Angel appears as sacred madness preceding discovery of True Will.
- **Visual symbols as functions**: Tiger, crocodile/Set, spiral energy, dove and butterfly each encode aspects of untamed instinct, chaos, motion, and transformation.
- **From innocence to ecstatic wildness**: Compared to RWS, Thoth shifts the Fool from gentle, childlike innocence to an ecstatic, risky creative force.

#### Detailed Explanation

In the Thoth system, the Fool is not a simple figure of naive optimism but the **source-point of all subsequent cards**. By assigning Aleph and the highest path from Kether to Chokmah, Crowley roots this archetype in the very first differentiation of divine consciousness. The card gathers images of chaos (crocodile/Set), fertility (Green Man), and unbounded movement (spiral energy) to show that creation begins in a state where forms have not yet solidified.

This re-framing explains why the Fool is both dangerous and holy: stepping into the unknown here means entering a field of raw power. The shift from Rider–Waite's innocent traveler to Thoth's wild initiatory force alters reading practice—where RWS might suggest a lighthearted new beginning, Thoth Fool often indicates a **volatile threshold**, demanding willingness to abandon control and accept temporary instability so that a deeper, Thelemic True Will can emerge. The visual and Qabalistic correspondences together support this interpretation as a structured doctrine, not merely stylistic difference.

**In Readings**:
- New beginning requiring abandon of rational control
- Divine inspiration breaking through normal consciousness
- Need to embrace chaos/uncertainty as creative force
- Connection to True Will beginning to stir

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Fool differs radically from RWS's innocent wanderer. The tiger replacing the dog emphasizes untamed instinct. The crocodile/Set imagery connects to Egyptian mystery tradition. The Green Man reference links to Celtic fertility rites. Harris's artwork captures spiral energy suggesting perpetual motion.
- **中文**: Crowley的愚者与RWS的无辜流浪者截然不同。老虎取代狗强调未驯化的本能。鳄鱼/Set意象连接埃及神秘传统。绿人引用关联凯尔特生育仪式。Harris的艺术捕捉了暗示永恒运动的螺旋能量。

**Narrative Snippets**:
- `[ns_thoth_005]` `[trigger: fool_chaos]` `[factor_trigger: card_atu_0 AND element_air AND letter_aleph AND path_11]` `[role: 主干]` The Fool represents primordial creative chaos—the first stirring of divine consciousness before it takes form. → English Paraphrase
- `[ns_thoth_006]` `[trigger: zero_infinite]` `[factor_trigger: depth AND destruction]` `[role: 主干依赖]` The Fool is zero pregnant with infinite possibility—not absence but potential before manifestation. → English Paraphrase
- `[ns_thoth_007]` `[trigger: holy_madness]` `[factor_trigger: diamond AND dignity_system]` `[role: 主干依赖]` This is holy madness—abandoning rationality to access higher wisdom, the divine spark seeking expression. → English Paraphrase
- `[ns_thoth_008]` `[trigger: fool_vs_rws]` `[factor_trigger: disorder AND divination_method]` `[role: 总结]` RWS Fool = innocent beginning; Thoth Fool = primal chaos, divine madness, creative destruction. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU 0: The Fool (愚者)"
    factor_refs: list = ['card_atu_0', 'new_candidate', 'new_candidate', 'letter_aleph', 'new_candidate', 'new_candidate', 'engine_id', 'card_atu_0', 'tarot_semantic', 'letter_aleph', 'tarot_semantic', 'path_11', 'tarot_semantic', 'element_air', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'source_ref', 'rel_thoth_fool_001', 'tarot_primordial_potential', 'rel_thoth_fool_002', 'tarot_manifestation', 'rel_thoth_fool_003', 'tarot_transcendence', 'rel_thoth_fool_004', 'tarot_fool_archetype', 'l1_anchor', 'confidence', 'evi_thoth_fool_001', 'evi_thoth_fool_002', 'evi_thoth_fool_003', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_thoth_fool_001', 'tarot_fool', 'astro_planet_uranus', 'map_thoth_fool_002', 'tarot_primordial_chaos', 'jung_collective_unconscious']
    
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
        l1_anchor="bot_v1.0.0_atu_0__the_fool__愚者_001_L1",
    )
    version: str = "1.0.0"
