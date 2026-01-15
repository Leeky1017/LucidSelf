"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994716
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
    semantic_id="pt_v1.0.0_four_of_wands__completion___ce_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class FourOfWandsCompletionCe(SemanticEntry):
    """
    **Visual Elements**:
- Four wands form gateway/chuppah structure
- Two figures celebrating
- Garland...
    """
    
    original_text: str = """**Visual Elements**:
- Four wands form gateway/chuppah structure
- Two figures celebrating
- Garland of flowers
- Castle/city in background
- Festive, joyous atmosphere

**English Paraphrase**:

The **Four of Wands** represents **completion of initial phase** and **celebration of achievement**. The four wands create a stable structure (square = stability), but it's festive, not rigid. This is **harvest time** - reaping rewards of earlier planting.

**Core Symbolism**:
- **Four wands as gateway**: Threshold moment, passage from one phase to next
- **Garland**: Victory, harvest, fruition
- **Two figures**: Community celebration, not isolated success
- **Castle background**: Security, foundation established
- **Open structure**: Stable yet flexible, allowing movement through

**Upright Meaning**:
- **Harvest/completion**: Initial phase of project/relationship successful
- **Celebration**: Time to acknowledge achievement before next phase
- **Stability with joy**: Unlike rigid Four of Pentacles, this stability dances
- **Community/marriage**: Often associated with weddings, partnerships
- **Home/foundation**: Secure base established
- **Freedom within structure**: Rules that liberate rather than constrain

**Reversed/Challenged**:
- **Incomplete celebration**: Success undermined or unacknowledged
- **Instability**: Foundation shaky, premature celebration
- **Isolation**: Achievement not shared, joy withheld
- **Transition blocked**: Unable to pass through gateway to next phase

**完整中文诠释**:
**权杖四**=**初始阶段完成与庆祝成就**。四权杖形成门户/稳定结构（方形=稳定），但欢庆并非僵化。**收获时节**——收获早期播种之回报。**图像元素**：**四权杖门户**=阈限时刻，从一阶段到下一阶段；**花环装饰**=胜利、收获、欢庆；**两人庆祝**=社群庆祝，非孤立成功；**远处城堡**=稳固家园基础；**开放构图**=结构内的自由移动。**正位含义**：**收获/完成**（努力初步成果），**庆祝**（公开承认成就），**有喜悦的稳定**（非僵化的安全），**社群/婚姻**（人际关系确立），**家园/基础**（建立稳固根基），**结构内的自由**（有序中的欢乐）。**逆位/挑战**：**不完整庆祝**（成功被破坏或不承认），**不稳定**（基础动摇、过早庆祝），**孤立**（成就未分享、欢乐被扣留），**转变受阻**（无法通过门户到下一阶段）。**心理层面**：**努力间的应得休息**时刻。不同于隐者的孤立或世界的宇宙完成，这是**人类规模的庆祝**。下一次攀登前的舞蹈。**实际应用**：婚礼/伴侣仪式，商业里程碑庆祝，乔迁新居、建立家园，项目阶段完成，社区聚会。

**Psychological Layer**: The moment of **earned rest** between efforts. Unlike Hermit's isolation or World's cosmic completion, this is **human-scale celebration**. The dance before the next climb.

**Practical Applications**:
- Wedding/partnership ceremony
- Business milestone celebration
- Housewarming, establishing home
- Project phase completion
- Community gathering

**Narrative Snippets**:
- `[ns_78deg_177]` `[trigger: four_wands_completion]` `[factor_trigger: tarot_four_wands AND state_completion]` `[role: 主干]` Four of Wands represents completion of initial phase and celebration of achievement—harvest time, reaping rewards of earlier planting. → English Paraphrase
- `[ns_78deg_178]` `[trigger: four_wands_gateway]` `[factor_trigger: tarot_four_wands AND symbol_gateway]` `[role: 条件分支]` Four wands create a gateway/threshold—passage from one phase to next, stable structure that is festive not rigid. → Core Symbolism
- `[ns_78deg_179]` `[trigger: community_celebration]` `[factor_trigger: tarot_four_wands AND state_communal_joy]` `[role: 主干]` Two figures celebrating together—community joy, not isolated success; achievement shared multiplies the blessing. → Visual Elements
- `[ns_78deg_180]` `[trigger: four_wands_reversed]` `[factor_trigger: tarot_four_wands AND polarity_reversed]` `[role: 条件分支]` Reversed: incomplete celebration, foundation shaky, isolation from community, transition blocked—unable to pass through gateway. → Reversed Meaning
- `[ns_78deg_181]` `[trigger: earned_rest_moment]` `[factor_trigger: tarot_four_wands AND state_earned_rest]` `[role: 总结]` Human-scale celebration—the dance before the next climb; unlike Hermit's isolation or World's cosmic completion, this is earned rest between efforts. → Psychological Layer
- `[ns_78deg_396]` `[trigger: chuppah_symbolism]` `[factor_trigger: tarot_four_wands AND symbol_chuppah]` `[role: 条件分支]` Four wands as Jewish chuppah (wedding canopy)—open on all sides yet structurally stable; intimacy within community; marriage as completion and new beginning. → Symbolic Reference
- `[ns_78deg_397]` `[trigger: harvest_time]` `[factor_trigger: tarot_four_wands AND cycle_harvest]` `[role: 条件分支]` Harvest time after planting—the reaping of rewards from earlier effort; garlands represent abundance freely shared; first fruits of labor now enjoyed. → Agricultural Symbolism
- `[ns_78deg_473]` `[trigger: freedom_within_structure]` `[factor_trigger: tarot_four_wands AND principle_structured_freedom]` `[role: 条件分支]` Freedom within structure—rules that liberate rather than constrain; stable yet flexible, allowing movement through; unlike rigid Four of Pentacles, this stability dances. → Upright Meaning
- `[ns_78deg_502]` `[trigger: open_gateway]` `[factor_trigger: tarot_four_wands AND symbol_open_structure]` `[role: 条件分支]` Open gateway structure—stable yet permeable, welcoming passage; completion that does not close off but opens up; the threshold between phases of growth. → Core Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Four of Wands: Completion & Celebration"
    factor_refs: list = ['milestone', 'existing', 'emotion', 'existing', 'state', 'existing', 'passage', 'existing', 'bond', 'existing']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_four_of_wands__completion___ce_001_L1",
    )
    version: str = "1.0.0"
