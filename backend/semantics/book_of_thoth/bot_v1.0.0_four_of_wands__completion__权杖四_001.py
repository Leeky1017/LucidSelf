"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088817
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
    semantic_id="bot_v1.0.0_four_of_wands__completion__权杖四_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FourOfWandsCompletion权杖四(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chesed in Fire | Mercy in Fire | Manifested power |
| Venus in Aries | Gentleness + fire | Tact in force |
| Circle boundary | Ring-pass-not | Completion limit |
| Order/Law | Solid system | Government structure |

**Title**: Lord of Completion (完成之主)
**Qabalistic**: Chesed in Fire (火中之仁慈)
**Astrological**: Venus in Aries (金星入白羊座)

**Source Text**:
> "This card refers to Chesed in the suit of Fire. Being below the Abyss, it is the Lord of all manifested active Power. The original Will... is now built up into a solid system: Order, Law, Government. It is also referred to Venus in Aries... One cannot establish one's work without tact and gentleness. ... The ends of the wands touch a circle, showing the completion and limitation of the original work."

**English Paraphrase**:
**Systematized Order** - Corresponds to Chesed (Mercy/Structure) in Fire. It represents **manifested active power** solidified into a system: **Order, Law, Government**. Ruled by **Venus in Aries**, indicating that establishing work requires tact and gentleness alongside force. The wands touch a circle, symbolizing **completion and limitation**. The work is finished and balanced ("four double flames"), but this limitation ("ring-pass-not") inherently contains the seeds of eventual disorder/decay.

**Core**: **Perfected Structure** - Success, settlement, order, completion of a phase, but with the restriction of finality.

**Chinese Explanation**:
**权杖四（完成）**对应火元素中的Chesed（仁慈/构建）。作为深渊之下的第一张牌，它是所有显化活动力量的主宰。原始意志被构建成一个稳固的系统：**秩序、法律、政府**。对应**金星在白羊座**，暗示建立工作需要机智与温柔。权杖末端接触一个圆环，显示原始工作的**完成与限制**。在圆环内火焰平衡，不再扩大范围。虽然代表完美，但这种限制本身也埋下了未来混乱的种子。

**In Readings**: Completion, settlement, successful conclusion, order, structure, marriage (Venus), stability, limitation.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Four of Wands shows Will systematized into Order/Law/Government. Venus in Aries adds tact to establishment. Circle boundary represents completion but also limitation (seeds of decay). First card "below the Abyss" in manifested realm.
- **中文**: Crowley的权杖四展示意志被系统化为秩序/法律/政府。金星入白羊为建立增添机智。圆环边界代表完成但也是限制（衰败的种子）。显化领域中"深渊之下"的第一张牌。

**Narrative Snippets**:
- `[ns_thoth_wands_010]` `[trigger: four_wands_completion]` `[factor_trigger: thoth_wands_four]` `[role: 主干]` Four of Wands = Lord of Completion—Will built into solid system: Order, Law, Government. → Core
- `[ns_thoth_wands_011]` `[trigger: venus_aries_tact]` `[factor_trigger: thoth_wands_four AND planet_venus_aries]` `[role: 条件分支]` Venus in Aries—establishing work requires tact and gentleness alongside force. → Astrological
- `[ns_thoth_wands_012]` `[trigger: circle_boundary]` `[factor_trigger: thoth_wands_four AND symbol_circle]` `[role: 条件分支]` Wands touch circle—completion and limitation; ring-pass-not; contains seeds of disorder. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Four of Wands: Completion (权杖四：完成)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_four_001', 'tarot_solid_system', 'rel_wands_four_002', 'tarot_seeds_of_disorder', 'l1_anchor', 'confidence', 'evi_wands_four_001', 'evi_wands_four_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_four_001', 'tarot_wands_four', 'astro_venus_aries']
    
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
        l1_anchor="bot_v1.0.0_four_of_wands__completion__权杖四_001_L1",
    )
    version: str = "1.0.0"
