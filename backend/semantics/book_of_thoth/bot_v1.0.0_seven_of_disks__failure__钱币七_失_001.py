"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063484
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
    semantic_id="bot_v1.0.0_seven_of_disks__failure__钱币七_失_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SevenOfDisksFailure钱币七失(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Netzach in Earth | Victory in Earth | Weakening effect |
| Saturn in Taurus | Heavy restriction | Crushing growth |
| Rubeus Pattern | Ugly geomantic | Blight symbol |
| Leaden Disks | Saturn metal | Bad money |

**Title**: Lord of Success Unfulfilled (未遂成功之主)
**Qabalistic**: Netzach in Earth (土中之胜利/情感)
**Astrological**: Saturn in Taurus (土星入金牛座)

**Source Text**:
> "The number Seven, Netzach, has its customary enfeebling effect, and this is made worse by the influence of Saturn in Taurus. The disks are arranged in the shape of the geomantic figure Rubeus, the most ugly and menacing of the Sixteen. (See Five of Cups.) The atmosphere of the card is that of Blight. On the background, which represents vegetation and cultivation, everything is spoiled. The four colours of Netzach appear, but they are blotched with angry indigo and reddish orange. The disks themselves are the leaden disks of Saturn. They suggest bad money."

**English Paraphrase**:
**Blighted Growth** – Corresponds to Netzach (Victory/Emotion) in Earth, but with its usual **weakening effect**. Made worse by **Saturn in Taurus**: heavy restriction crushing stable growth. The disks form **Rubeus**, the geomantic figure called "the most ugly and menacing" – a pattern of blight and decay. The background shows vegetation and cultivation, but everything is spoiled and ruined. The colors are blotched with angry indigo and reddish orange; the disks themselves are **leaden** (Saturn's metal), suggesting counterfeit money, failed investments, or effort that bears no fruit. This is **Failure**: thwarted ambition, wasted work, crops that rot before harvest, promises unfulfilled.

**Core**: **Frustrated Effort** – Failure, blight, wasted labor, bad investments, unfulfilled promise, decay.

**Chinese Explanation**:
**钱币七（失败）**对应土元素中的**Netzach（胜利/情感能量）**，但这里它带来的是**衰弱效应**。加上**土星入金牛座**的沉重限制，将本该稳定增长的物质彻底压垮。七个圆盘排列成地卜图**Rubeus**（红色），被称为十六卦中"最丑陋、最凶险"的图形，象征**枯萎与腐败**。背景是田地与耕作，但一切都已毁坏；颜色中掺杂着愤怒的靛蓝与橙红；圆盘本身是土星的**铅质**圆盘，暗示假币、失败投资、或付出却毫无收获。这张牌代表：抱负落空、劳动白费、庄稼在收获前腐烂、承诺无法兑现的挫败与失望。

**In Readings**: Failure, disappointment, wasted effort, bad investments, blight, decay, unfulfilled ambition, projects that collapse before completion.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Seven of Disks shows Netzach's weakening in Earth. Saturn in Taurus crushes growth. Rubeus pattern - most ugly geomantic figure. Leaden disks suggest bad money. Blighted vegetation.
- **中文**: Crowley的钱币七展示Netzach在大地的衰弱。土星入金牛压垃生长。Rubeus图案—最丑陆的地卜图形。铅质圆盘暗示假币。枯萎植被。

**Narrative Snippets**:
- `[ns_thoth_disks_019]` `[trigger: seven_disks_failure]` `[factor_trigger: thoth_disks_seven]` `[role: 主干]` Seven of Disks = Lord of Success Unfulfilled—Netzach's weakening; atmosphere of Blight. → Core
- `[ns_thoth_disks_020]` `[trigger: saturn_taurus_crush]` `[factor_trigger: thoth_disks_seven AND planet_saturn_taurus]` `[role: 条件分支]` Saturn in Taurus—heavy restriction crushing growth; everything spoiled before fruition. → Astrological
- `[ns_thoth_disks_021]` `[trigger: rubeus_leaden]` `[factor_trigger: thoth_disks_seven AND symbol_rubeus]` `[role: 条件分支]` Rubeus pattern—most ugly geomantic figure; leaden disks suggest bad money and decay. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Seven of Disks: Failure (钱币七：失败)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_seven_001', 'tarot_blighted_growth', 'rel_disks_seven_002', 'tarot_wasted_effort', 'l1_anchor', 'confidence', 'evi_disks_seven_001', 'evi_disks_seven_002', 'tarot_leaden_disks', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_seven_001', 'tarot_disks_seven', 'astro_saturn_taurus']
    
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
        l1_anchor="bot_v1.0.0_seven_of_disks__failure__钱币七_失_001_L1",
    )
    version: str = "1.0.0"
