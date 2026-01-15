"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027482
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
    semantic_id="bot_v1.0.0_princess_of_cups__圣杯公主_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrincessOfCups圣杯公主(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Earth of Water | Crystallizing moisture | Substance to idea |
| Swan Crest | Creative Word (AUM) | Divine speech |
| Tortoise from Cup | World-bearer | Foundation support |
| Dancing on Sea | Graceful formation | Effortless creation |

**Title**: Princess of the Waters, Lotus of the Palace of the Floods (诸水公主，洪水宫殿之莲)
**Elemental**: The Earthy part of Water (水中之土)
**Rule**: Quadrant around North Pole (北极周围象限)

**Source Text**:
> "The Princess of Cups represents the earthy part of Water; in particular, the faculty of crystallization. She represents the power of Water to give substance to idea, to support life, and to form the basis of chemical combination. She is represented as a dancing figure, robed in a flowing garment on whose edges crystals are seen to form. For her crest she wears a swan with open wings... She bears a covered cup from which issues a tortoise... and the Lotus of Isis... She is dancing upon a foaming sea in which disports himself a dolphin, the royal fish, which symbolizes the power of Creation. The character of the Princess is infinitely gracious... silently and effortlessly she goes about her work."

**English Paraphrase**:
**Crystallizing Water** - Represents the **Earthy part of Water**: the faculty of **crystallization**, giving substance to ideas, supporting life, and providing the basis of chemical combination. She dances upon a **foaming sea**, wearing a flowing robe whose edges grow **crystals**. Her crest is a **swan**, linked to the creative Word (AUM/AUMGN). From her covered cup emerges a **tortoise**, echoing the world-bearing tortoise of Hindu cosmology, while a **dolphin** (royal fish) plays beneath her, symbolizing the power of creation. Her character is gracious, voluptuous, gentle, and tender; she lives in a world of romance and rapture. She may appear indolent, but in truth she works **silently and effortlessly**, allowing forms to precipitate.

**Core**: **Embodied Imagination** - Romantic sensitivity, aesthetic creation, gentle support, formation of emotional/creative structures.

**Chinese Explanation**:
**圣杯公主**代表**水中之土**，特别指水的**结晶能力**：赋予想法以形体、承载生命、成为化学结合与生成的基础。她在**翻涌的海面**上起舞，身披流动的衣袍，衣缘上不断**析出晶体**；头戴**振翅天鹅**，对应东方哲学中作为AUM/AUMGN之象征的创世之声。她手持盖住的圣杯，其中探出**龟**（对应托举世界的宇宙之龟），脚下海中有**海豚**腾跃，象征创造力与王者之鱼。性格上，她**温柔、体贴、感官细腻、充满浪漫幻想**，仿佛沉浸在永恒的幸福幻梦中。表面或许显得慵懒，但实际上，她以**不费力的方式默默完成凝聚与孕育的工作**，是情感与想象力物质化的关键媒介。

**In Readings**: Gentle love, artistic inspiration, pregnancy of ideas, emotional support, romantic daydreaming; or, in shadow, escapist fantasy and passivity.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Princess of Cups is Earth of Water - crystallization faculty. Swan crest represents creative Word (AUM). Tortoise from cup shows world-support. She works silently and effortlessly, precipitating forms.
- **中文**: Crowley的圣杯公主是水中之土—结晶能力。天鹅顶饰代表创世之言（AUM）。杯中之龟显示托世。她默默不费力地工作，沉淀形态。

**Narrative Snippets**:
- `[ns_thoth_cups_040]` `[trigger: princess_cups_thoth]` `[factor_trigger: thoth_cups_princess]` `[role: 主干]` Princess of Cups = Earth of Water—crystallization faculty; gives substance to idea, supports life. → Core
- `[ns_thoth_cups_041]` `[trigger: swan_tortoise]` `[factor_trigger: thoth_cups_princess AND symbol_swan_tortoise]` `[role: 条件分支]` Swan crest (AUM creative Word); tortoise from cup (world-bearer); dolphin plays beneath. → Visual
- `[ns_thoth_cups_042]` `[trigger: effortless_crystallization]` `[factor_trigger: thoth_cups_princess AND state_gracious]` `[role: 条件分支]` Dancing on foaming sea, crystals forming on robe—silently and effortlessly precipitating forms. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Princess of Cups (圣杯公主)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_princess_cups_earth', 'earth_of_water', 'rel_princess_cups_create', 'imagination', 'princess_cups_crystal']
    
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
        l1_anchor="bot_v1.0.0_princess_of_cups__圣杯公主_001_L1",
    )
    version: str = "1.0.0"
