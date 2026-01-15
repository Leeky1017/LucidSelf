"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994626
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
    semantic_id="pt_v1.0.0_card_18__the_moon_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card18TheMoon(SemanticEntry):
    """
    ### Illusion, Fear, Imagination Distorts Return

#### Key Term Analysis

| Term | Definition | Signi...
    """
    
    original_text: str = """### Illusion, Fear, Imagination Distorts Return

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 18 | 1+8=9 Hermit | Guide needed |
| Reflected Light | Moon reflects | vs Star/Sun emit |
| Distortion | Imagination molds | Shapes for consciousness |
| Lunar Wildness | Fearful journey | Through visions |

**Source Text**: The true task is bringing inner ecstasy back to consciousness. The Star had no road. To use that light we must pass through distortion and fear. The Moon is imagination molding Star energy into shapes consciousness can comprehend. Myths always distorted. Imagination distorts because reflecting inner to outer mind.

**English Paraphrase**:

**The Moon** = **Imagination**, **Distortion**, **Lunar Wildness** — fearful journey back through visions.

**Core Symbolism**:
- **Number 18**: 1+8=9 (Hermit guide), relates 8 (Strength tamed→Moon wild)
- **Reflected light**: Moon reflects (vs. Star/Sun emit)

**Visual**:
- **Dog + Wolf howling** = animal self roused (domestic/wild), id surfaces
- **Crayfish emerging** = "deeper than savage beast" (Waite), nameless demons, deepest fears
- **Two towers** = gateway, last duality, looking from other side (already passed)
- **Yod drops** = grace not fear
- **Winding path** = road back through distortion

**Why distorted**: Star formless, Moon shapes for consciousness. Can't bring all back→partial loss→disturbing.

**Dual**: Wild (lunacy, nightmares, madness) + Grace (yods, "Peace be still", if accepted→enriched)

**完整中文诠释**:
**月亮**=**想象**、**扭曲**、**月之野性**——通过愿景的恐惧归返旅程。**数字18**：1+8=9（隐者引导），关联8（力量驯服→月亮狂野）；**反射光**：月亮反射（vs星星/太阳发射）。**图像**（RWS牌）：**狗+狼嚎叫**=动物自我被唤起（驯养/野生），本我浮现；**龙虾涌现**="比野兽更深"（Waite），无名恶魔，最深恐惧；**两座塔**=门径，最后二元性，从另侧观看（已穿越）；**Yod滴**=恩典非恐惧；**蜿蜒路**=通过扭曲的归返之路。**为何扭曲**：星星无形，月亮为意识塑形。无法带全部回→部分失落→干扰。**双重性**：狂野（lunacy、梦魇、疯癫）+恩典（yods，"平安静止"，若接受→丰富）。真正任务是将内在狂喜带回意识。星星无路。要用那光我们必须通过扭曲与恐惧。月亮是想象将星星能量塑造为意识能理解之形。神话总扭曲。想象扭曲因从内反射至外在心智。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Pollack's Moon: Number 18=9 guide. Reflected light. Dog+wolf+lobster. Two towers=gateway. Yod drops=grace despite fear.
- **中文**: Pollack的月亮:数字18=9向导。反射光。狗+狼+龙虾。两塔=门径。Yod滴=恐惧中恩典。

**Narrative Snippets**:
- `[ns_78deg_159]` `[trigger: moon_major]` `[factor_trigger: tarot_major_moon AND sequence_star_moon_sun AND state_lunar_wildness AND tarot_number_18 AND symbol_crayfish AND symbol_dog_wolf]` `[role: 主干]` The Moon represents the fearful journey back from Star's ecstasy—imagination distorting formless experience into shapes consciousness can grasp. → English Paraphrase
- `[ns_78deg_160]` `[trigger: imagination_distortion]` `[factor_trigger: principle_imagination_distortion]` `[role: 主干]` Imagination shapes Star's energy into comprehensible forms—necessary but distorting; myths always distort reflecting inward to outward mind. → English Paraphrase
- `[ns_78deg_161]` `[trigger: pisces_ruler]` `[factor_trigger: sign_pisces]` `[role: 主干依赖]` Pisces rules Moon—depths, imagination, the collective; water element of dreams and the unconscious return journey. → English Paraphrase
- `[ns_78deg_162]` `[trigger: yod_grace]` `[factor_trigger: symbol_yod_grace]` `[role: 条件分支]` Yod drops from moon—grace despite fear; divine protection guides through distortion and terror of the passage. → English Paraphrase
- `[ns_78deg_349]` `[trigger: dog_wolf_crayfish]` `[factor_trigger: tarot_major_moon AND symbol_animals]` `[role: 条件分支]` Dog + wolf howling—animal self roused (domestic/wild), id surfaces; crayfish emerging "deeper than savage beast," nameless demons, deepest fears. → Visual Elements
- `[ns_78deg_350]` `[trigger: two_towers_gateway]` `[factor_trigger: tarot_major_moon AND symbol_towers]` `[role: 条件分支]` Two towers form gateway—last duality; looking from other side (already passed); the winding path leads back through distortion. → Visual Elements
- `[ns_78deg_351]` `[trigger: reflected_light]` `[factor_trigger: tarot_major_moon AND principle_reflection]` `[role: 条件分支]` Reflected light—Moon reflects (vs Star/Sun emit); Number 18=9 (Hermit guide needed); relates to 8 (Strength tamed becomes Moon wild). → Core Symbolism
- `[ns_78deg_352]` `[trigger: lunar_dual_nature]` `[factor_trigger: tarot_major_moon AND principle_duality AND state_lunar_wisdom]` `[role: 总结]` Moon's dual nature: Wild (lunacy, nightmares, madness) + Grace (yods, "Peace be still"); if accepted→enriched; necessary passage to Sun. → Dual Interpretation
- `[ns_78deg_544]` `[trigger: winding_path]` `[factor_trigger: tarot_major_moon AND symbol_winding_path]` `[role: 条件分支]` Winding path through distortion—not straight but twisting through fears; the only road back from formless ecstasy to consciousness. → Visual Elements
- `[ns_78deg_545]` `[trigger: necessary_distortion]` `[factor_trigger: tarot_major_moon AND principle_necessary_distortion]` `[role: 条件分支]` Can't bring all back—partial loss inevitable; what returns is disturbing because incomplete; imagination shapes but also loses; the price of translation. → Core Symbolism

---"""
    normalized_text_zh: str = """"""
    subject: str = "Card 18: The Moon"
    factor_refs: list = ['tarot_major_moon', 'tarot_number_18', 'principle_imagination_distortion', 'symbol_crayfish', 'state_lunar_wildness']
    
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
        l1_anchor="pt_v1.0.0_card_18__the_moon_001_L1",
    )
    version: str = "1.0.0"
