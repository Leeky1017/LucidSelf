"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076549
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
    semantic_id="bot_v1.0.0_ten_of_swords__ruin__宝剑十_毁灭_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TenOfSwordsRuin宝剑十毁灭(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Malkuth in Air | Kingdom in Air | Ultimate degeneration |
| Sun in Gemini | Bright + scattered | Reason run mad |
| Shattered Swords | Broken weapons | System collapse |
| Sephirothic Pattern | Tree layout | Total failure |

**Title**: Lord of Ruin (毁灭之主)
**Qabalistic**: Malkuth in Air (气中之王国)
**Astrological**: Sun in Gemini (太阳入双子座)

**Source Text**:
> "The number Ten, Malkuth, as always, represents the culmination of the unmitigated energy of the idea. It shows reason run mad, ramshackle riot of soulless mechanism; it represents the logic of lunatics and (for the most part) of philosophers. It is reason divorced from reality. The card is also ruled by the Sun in Gemini... this card shows the disruption and disorder of harmonious and stable energy. The hilts of the Swords occupy the positions of the Sephiroth, but the points One to Five and Seven to Nine touch and shatter the central Sword (six)... The tenth Sword is also in splinters. It is the ruin of the Intellect, and even of all mental and moral qualities."

**English Paraphrase**:
**Logic Gone Mad** – Corresponds to Malkuth (Kingdom/Manifestation) in Air. Here the energy of the suit reaches its **worst possible conclusion**. With **Sun in Gemini**, brilliant mental power has become **fragmented and self‑destructive**: "reason run mad", mechanical thinking with no soul or grounding in reality. Ten swords occupy the positions of the Sephiroth; their points shatter the central solar sword (Tiphareth), and even the tenth is in splinters. This is the **Ruin** of intellect – collapse of mental and moral structure, burnout of thought itself.

**Core**: **Total Mental Collapse** – Rock bottom, burnout, over‑analysis to destruction, catastrophic over‑thinking.

**Chinese Explanation**:
**宝剑十（毁灭）**对应空气元素中的**Malkuth（王国/具体显化）**，代表宝剑能量走到**极端、失控的终点**。统治星为**太阳入双子座**，象征本应光明活跃的心智，却在过度分析与分裂中**自我瓦解**，成为"发疯的逻辑"：推理不断自我叠加，却早已脱离现实。牌面上十把剑的剑柄位于十个 Sephiroth 的位置，但剑尖却刺碎了中央代表太阳/心/子体的那把剑，连第十把剑本身也粉碎，象征**理性与道德架构的完全崩塌**。它往往指向：过度用脑、过度算计、过度担忧导致的精神崩溃，或一个思想体系的终极失败。

**In Readings**: Ruin, mental breakdown, hitting bottom, disastrous over‑analysis, a system or plan that has utterly failed and must be abandoned.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ten of Swords shows Malkuth as culmination of unmitigated energy. Sun in Gemini brings "reason run mad". Swords shatter central blade. Total ruin of intellect and moral structure.
- **中文**: Crowley的宝剑十展示Malkuth作为未缓和能量的顶点。太阳入双子带来"发疯的理性"。剑刺破中央刃。理智与道德结构彻底崩溃。

**Narrative Snippets**:
- `[ns_thoth_swords_028]` `[trigger: ten_swords_ruin]` `[factor_trigger: thoth_swords_ten]` `[role: 主干]` Ten of Swords = Lord of Ruin—Malkuth; culmination of unmitigated energy; reason run mad. → Core
- `[ns_thoth_swords_029]` `[trigger: sun_gemini_mad]` `[factor_trigger: thoth_swords_ten AND planet_sun_gemini]` `[role: 条件分支]` Sun in Gemini—bright mind fragmented; ramshackle riot of soulless mechanism; logic of lunatics. → Astrological
- `[ns_thoth_swords_030]` `[trigger: sephirothic_shatter]` `[factor_trigger: thoth_swords_ten AND symbol_shattered_swords]` `[role: 条件分支]` Ten swords in Sephiroth positions shatter central sword (Tiphareth)—ruin of intellect and morals. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Ten of Swords: Ruin (宝剑十：毁灭)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_ten_001', 'tarot_total_collapse', 'rel_swords_ten_002', 'tarot_system_failure', 'l1_anchor', 'confidence', 'evi_swords_ten_001', 'evi_swords_ten_002', 'tarot_shattered_swords', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_ten_001', 'tarot_swords_ten', 'astro_sun_gemini']
    
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
        l1_anchor="bot_v1.0.0_ten_of_swords__ruin__宝剑十_毁灭_001_L1",
    )
    version: str = "1.0.0"
