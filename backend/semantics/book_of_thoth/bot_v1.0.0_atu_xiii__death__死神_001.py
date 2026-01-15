"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044476
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
    semantic_id="bot_v1.0.0_atu_xiii__death__死神_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuXiiiDeath死神(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Nun (נ) | Hebrew letter "fish" | Water transformation |
| Putrefaction | Alchemical decay stage | Breakdown before rebirth |
| Scorpio Forms | Scorpion→Snake→Eagle | Transformation sequence |
| Ego Death | False identity dissolution | True Will emergence |

**Qabalistic Correspondences**:
- **Hebrew Letter**: Nun (נ, value 50, means "fish" - transformation through water)
- **Path**: Connects Tiphareth (Beauty) to Netzach (Victory) - beauty transformed into enduring form
- **Zodiac**: Scorpio ♏ (death, rebirth, transformation, hidden depths)
- **Element**: Water (fixed water = ice, transformation through dissolution)

**English Paraphrase**:

**Death** in Thoth system represents **transformation and renewal**, not literal physical death. Crowley emphasizes Death as the **destroyer that creates** - clearing away the old to make space for the new. This is the alchemical **putrefaction stage** where matter must rot before it can be reborn in higher form.

**Visual Key Elements**:
- Skeleton with scythe: Inevitable change, cutting away dead forms
- Fish/serpent: Nun's symbol, transformation through dissolution (water element)
- Scorpion imagery: Scorpio's lowest form (sting/poison) before transformation to eagle (transcendence)
- Eagle in background: Scorpio's highest form, resurrection after death
- Bubbles/decomposition: Material breaking down into constituent elements

**Core Meaning**:
Death is **absolute transformation** - not gentle change but complete dissolution of existing form. In Thelemic context, Death represents **ego death** necessary to discover True Will. The old identity must die for authentic self to emerge. This is **necessary destruction**, not punishment - the universe constantly dying and being reborn in every moment.

**Rider-Waite Comparison**:
- **RW Death (XIII)**: Transformation, endings, transition, the "necessary change" message softened
- **Thoth Death (XIII)**: More explicit about dissolution/putrefaction, alchemical focus, death as creative force
- **Similar**: Both emphasize transformation over literal death
- **Thoth adds**: Explicit alchemical stage, Scorpio's three forms (scorpion-snake-eagle), water dissolution

**完整中文诠释**: 透特系统中**死神**代表**转化与更新**，非字面肉体死亡。Crowley强调死神作为**创造的毁灭者**——清除旧有为新开辟空间。这是炼金术**腐化阶段**——物质必须腐烂才能以更高形式重生。卡巴拉对应：希伯来字母Nun(נ/鱼=通过水的转化)、连接Tiphareth至Netzach路径（美转化为持久形式）、天蝎座♏（死亡/重生/转化/隐藏深度）、水元素（固定水=冰通过溶解转化）。视觉元素：持镰刀骷髅（不可避免变化砍去死亡形式）、鱼/蛇（Nun符号通过溶解转化/水元素）、蝎子意象（天蝎最低形式蜇针/毒药在转化为鹰前/超越）、背景鹰（天蝎最高形式死后复活）、泡沫/分解（物质分解为组成元素）。核心含义：死神是**绝对转化**——非温和改变而是现存形式完全溶解。泰勒玛语境中死神代表发现真实意志所必需的**自我死亡**。旧身份必须死去以便真实自我浮现。这是**必要破坏**非惩罚——宇宙每时每刻不断死亡与重生。

**In Readings**:
- Major transformation underway, old form dying
- Ego death necessary for spiritual growth
- Letting go of outdated identity/beliefs/situations
- Putrefaction before rebirth (feels like dying but is transformation)
- Scorpio themes: intensity, depth, hidden truths emerging

#### Core Points

- **Death as transformation**: The card represents total transformation and renewal, not literal physical death.
- **Alchemical putrefaction**: Highlights the stage where forms rot and break down before higher rebirth.
- **Scorpio threefold path**: Scorpion, snake, and eagle show stages from destructive sting through shedding to transcendence.
- **Ego death and True Will**: Old identity must dissolve so authentic self and True Will can emerge.
- **Creative destruction**: Necessary clearing of dead structures so new life can arise.

#### Detailed Explanation

By emphasizing Nun, Scorpio, and fixed water, Thoth's Death insists that true change involves dissolution rather than surface adjustment. The skeleton with scythe, decomposition bubbles, and fish/serpent imagery all point to a process where existing structures are reduced to raw material. This is the alchemical Nigredo phase: uncomfortable, messy, but essential for genuine rebirth.

The three forms of Scorpio chart a developmental arc—scorpion as toxic, defensive impulse; snake as capacity to shed old skins; eagle as the capacity to rise above former limitations. Within a Thelemic frame, this sequence describes ego death: when outdated self-concepts die, consciousness can realign with True Will. In readings, Death thus signals that clinging to obsolete forms is more dangerous than surrendering to the transformative current already in motion.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Death emphasizes alchemical putrefaction (Nigredo) rather than gentle transition. The three forms of Scorpio (scorpion→snake→eagle) represent progressive transformation stages. Harris's imagery includes decomposition bubbles and the skeleton's creative dance, depicting death as generative force.
- **中文**: Crowley的死神强调炼金术腐化（黑化阶段）而非温和过渡。天蝎座的三种形态（蠎子→蛇→鹰）代表逐步转化阶段。Harris的图像包括分解气泡和骷髅的创造性跳舞，将死亡描绘为生成力量。

**Narrative Snippets**:
- `[ns_thoth_015]` `[trigger: death_transformation]` `[factor_trigger: tarot_death AND tarot_transformation]` `[role: 主干]` Death in Thoth system represents transformation and renewal, not literal physical death. → English Paraphrase
- `[ns_thoth_016]` `[trigger: putrefaction]` `[factor_trigger: tarot_putrefaction AND tarot_rebirth]` `[role: 主干依赖]` This is the alchemical putrefaction stage where matter must rot before it can be reborn in higher form. → English Paraphrase
- `[ns_thoth_017]` `[trigger: scorpio_forms]` `[factor_trigger: tarot_scorpio AND tarot_transformation]` `[role: 主干依赖]` The three forms of Scorpio (scorpion→snake→eagle) represent progressive transformation stages. → Source Text
- `[ns_thoth_018]` `[trigger: ego_death]` `[factor_trigger: tarot_ego_death AND tarot_true_will]` `[role: 总结]` Death represents ego death necessary to discover True Will—the old identity must die for authentic self to emerge. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU XIII: Death (死神)"
    factor_refs: list = ['card_atu_13', 'letter_nun', 'path_24', 'sign_scorpio', 'new_candidate', 'new_candidate', 'source_ref', 'rel_thoth_death_001', 'tarot_renewal', 'rel_thoth_death_002', 'tarot_higher_form', 'rel_thoth_death_003', 'tarot_transcendence', 'rel_thoth_death_004', 'tarot_authentic_self', 'l1_anchor', 'confidence', 'evi_thoth_death_001', 'evi_thoth_death_002', 'evi_thoth_death_003', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_thoth_death_001', 'tarot_death', 'astro_sign_scorpio', 'map_thoth_death_002', 'tarot_ego_death', 'jung_process_individuation']
    
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
        l1_anchor="bot_v1.0.0_atu_xiii__death__死神_001_L1",
    )
    version: str = "1.0.0"
