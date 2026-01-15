"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088888
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
    semantic_id="bot_v1.0.0_nine_of_wands__strength__权杖九_力_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class NineOfWandsStrength权杖九力(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Yesod in Fire | Foundation in Fire | Restored balance |
| Moon in Sagittarius | Double lunar | Change is Stability |
| Arrows | Directed force | Defensive aim |
| Fullest Development | Peak before descent | Maximum force |

**Title**: Lord of Strength (力量之主)
**Qabalistic**: Yesod in Fire (火中之基础)
**Astrological**: Moon in Sagittarius (月亮入射手座)

**Source Text**:
> "This card is referred to Yesod, the Foundation; this brings the Energy back into balance. ... The Nine represents always the fullest development of the Force... This card is also governed by the Moon in Sagittarius; so here is a double influence of the Moon on the Tree of Life. Hence the aphorism 'Change is Stability'. ... The Wands have now become arrows. ... The flames in the card are tenfold, implying that the Energy is directed downwards."

**English Paraphrase**:
**Stable Strength** - Corresponds to Yesod (Foundation) in Fire, bringing energy back into balance. It represents the **fullest development** of the force in relation to superiors. Ruled by the **Moon in Sagittarius**, creating a double Lunar influence (Yesod is Moon, plus Moon in sign). This leads to the paradox **"Change is Stability"**. The wands become **arrows** (directed force), with one master arrow connecting Sun and Moon. It signifies strength maintained through constant adjustment and defense.

**Core**: **Resilience and Defense** - Strength through stability, prepared defense, recovery of balance, successful maintenance of position.

**Chinese Explanation**:
**权杖九（力量）**对应火元素中的Yesod（基础），将能量带回平衡。代表力量在某种层面上达到了**最充分的发展**。对应**月亮在射手座**，加上Yesod本身的月亮属性，形成双重月亮影响，引出格言"**变化即稳定**"（Change is Stability）。权杖变成了**箭**（定向的力量），其中一支主箭连接日月。这象征通过不断的调整和防御来维持力量，是一种韧性与稳固。

**In Readings**: Strength, defense, resilience, holding one's ground, recovery, stability amidst change, preparedness.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Nine of Wands shows energy restored to balance through Yesod. Moon in Sagittarius creates "Change is Stability" paradox. Wands become arrows for directed defense. Fullest development before solidification.
- **中文**: Crowley的权杖九展示能量通过Yesod恢复平衡。月亮入射手创造"变化即稳定"悖论。权杖变成箭用于定向防御。固化前的最充分发展。

**Narrative Snippets**:
- `[ns_thoth_wands_025]` `[trigger: nine_wands_strength]` `[factor_trigger: thoth_wands_nine]` `[role: 主干]` Nine of Wands = Lord of Strength—Yesod in Fire; fullest development; energy back in balance. → Core
- `[ns_thoth_wands_026]` `[trigger: moon_sagittarius]` `[factor_trigger: thoth_wands_nine AND planet_moon_sagittarius]` `[role: 条件分支]` Moon in Sagittarius—double lunar; "Change is Stability" paradox; fluctuating directed force. → Astrological
- `[ns_thoth_wands_027]` `[trigger: arrows_defense]` `[factor_trigger: thoth_wands_nine AND symbol_arrows]` `[role: 条件分支]` Wands become arrows—directed force; master arrow linking Sun and Moon; defensive aim. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Wands: Strength (权杖九：力量)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_nine_001', 'tarot_resilient_defense', 'rel_wands_nine_002', 'tarot_fullest_development', 'l1_anchor', 'confidence', 'evi_wands_nine_001', 'evi_wands_nine_002', 'tarot_change_stability', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_nine_001', 'tarot_wands_nine', 'astro_moon_sagittarius']
    
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
        l1_anchor="bot_v1.0.0_nine_of_wands__strength__权杖九_力_001_L1",
    )
    version: str = "1.0.0"
