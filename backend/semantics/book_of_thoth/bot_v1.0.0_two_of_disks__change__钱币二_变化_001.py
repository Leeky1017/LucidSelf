"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063363
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
    semantic_id="bot_v1.0.0_two_of_disks__change__钱币二_变化_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TwoOfDisksChange钱币二变化(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chokmah in Earth | Wisdom in Earth | Fixed yet changing |
| Jupiter in Capricorn | Expansion + restriction | Paradoxical harmony |
| Ouroboros | Tail-eating serpent | Infinity figure-8 |
| 0=2 | Unity = duality | Change supports stability |

**Title**: Lord of Harmonious Change (和谐变化之主)
**Qabalistic**: Chokmah in Earth (土中之智慧)
**Astrological**: Jupiter in Capricorn (木星入摩羯座)

**Source Text**:
> "The number Two, Chokmah, here rules in the suit pertaining to Earth. It shows the type of Energy appropriate to Two, in its most fixed form. According to the doctrine that Change is the support of stability, the card is called Change. Its celestial rulers are Jupiter and Capricornus; and these symbols are most inharmonious... The card represents two Pantacles, one above the other; they are the Chinese symbols of the Yang and Yin duplicated as in the Hsiang. One wheel is dextro- and the other laevo-rotatory. They thus represent the harmonious interplay of the Four Elements in constant movement... About them is entwined a green Serpent... His tail is in his mouth. He forms the figure Eight, the symbol of the Infinite, the equation 0=2."

**English Paraphrase**:
**Dynamic Balance** – Corresponds to Chokmah (Wisdom/Force) in Earth, showing primal energy in its most **fixed yet paradoxically changing** form. Ruled by **Jupiter in Capricorn** (expansion in restriction), yet the card shows harmony. Two pantacles rotate oppositely: one clockwise, one counter-clockwise, bearing duplicated **Yang/Yin** symbols (Chinese Hsiang). Around them a green **Ouroboros serpent** (tail in mouth) forms the figure-8, the symbol of infinity and the equation **0=2**: Change is the support of stability. This is the dance of dualities in constant motion, creating equilibrium through flux.

**Core**: **Cyclical Change** – Flux, adaptation, rhythmic movement, balancing opposites, the Tao.

**Chinese Explanation**:
**钱币二（变化）**对应土元素中的**Chokmah（智慧/原初力量）**，展示"最固定"的能量形式——而它的名字恰恰叫"变化"，体现"**变化是稳定的支撑**"这一悖论性智慧。统治星为**木星入摩羯座**（扩张被限制，两者本不和谐），但牌面却呈现动态和谐。两个圆盘上下排列，一个顺时针旋转、一个逆时针旋转，上有**阴阳（Yang/Yin）**的中国符号；周围缠绕着绿色衔尾蛇，尾巴咬在嘴里，形成数字8（无穷符号）与方程式 **0=2**。这是对立统一的完美表达：通过不断变化来维持平衡，正如道家所云"动中求静"。

**In Readings**: Change, flux, adaptability, juggling multiple things, ups and downs, maintaining balance through movement, cycles.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Two of Disks shows "change is the support of stability". Jupiter in Capricorn paradoxically harmonious. Two wheels rotate opposite with Yang/Yin. Ouroboros forms figure-8 infinity, equation 0=2.
- **中文**: Crowley的钱币二展示"变化是稳定的支撑"。木星入摩羯异常和谐。两个轮子以阴阳相反旋转。衮尾蛇形成无穷数字8，方程式0=2。

**Narrative Snippets**:
- `[ns_thoth_disks_004]` `[trigger: two_disks_change]` `[factor_trigger: thoth_disks_two]` `[role: 主干]` Two of Disks = Lord of Harmonious Change—Chokmah in Earth; "change is the support of stability". → Core
- `[ns_thoth_disks_005]` `[trigger: jupiter_capricorn]` `[factor_trigger: thoth_disks_two AND planet_jupiter_capricorn]` `[role: 条件分支]` Jupiter in Capricorn—expansion + restriction paradoxically harmonious; growth within limits. → Astrological
- `[ns_thoth_disks_006]` `[trigger: ouroboros_eight]` `[factor_trigger: thoth_disks_two AND symbol_ouroboros]` `[role: 条件分支]` Ouroboros forms figure-8 infinity; two Yang/Yin wheels rotate opposite; equation 0=2. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Two of Disks: Change (钱币二：变化)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_two_001', 'tarot_dynamic_stability', 'rel_disks_two_002', 'tarot_infinite_cycle', 'l1_anchor', 'confidence', 'evi_disks_two_001', 'evi_disks_two_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_two_001', 'tarot_disks_two', 'astro_jupiter_capricorn']
    
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
        l1_anchor="bot_v1.0.0_two_of_disks__change__钱币二_变化_001_L1",
    )
    version: str = "1.0.0"
