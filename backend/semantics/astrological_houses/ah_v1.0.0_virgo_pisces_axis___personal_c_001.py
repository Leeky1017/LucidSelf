"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333902
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
    semantic_id="ah_v1.0.0_virgo_pisces_axis___personal_c_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class VirgoPiscesAxisPersonalC(SemanticEntry):
    """
    #### Source Text

"Virgo is characterized by analytical and critical temperament, and by the urge to...
    """
    
    original_text: str = """#### Source Text

"Virgo is characterized by analytical and critical temperament, and by the urge to reorient or repolarize essential energies of emotional-personal nature. Virgo is a symbol of psychological crisis. The Virgo-rising person will seek to single himself out by progressive transformations, spiritual overcomings, bodily rejuvenations. Pisces symbolizes a state of social, collective crisis. At this stage man finds himself swept by social storms against which he is powerless. The Pisces-Ascendant type may be wide open to the collective unconscious—perhaps a medium, perhaps a true seer, perhaps a crusader, a leader of armies or groups dedicated to a greater future."

#### English Paraphrase (Primary Language)

The Virgo/Pisces axis represents the polarity between personal transformation and collective dissolution—both mutable signs referring to critical states in evolution. Virgo rising seeks distinction through progressive transformations, spiritual overcomings, and self-improvement. There may be deep yearning for purity and sanctity. But meeting associates in Piscean manner, this person may be too open as lover or partner—longing to lose self in collectivity or cause. When Pisces rises, the individual is wide open to collective unconscious—medium, seer, crusader, or leader of armies. Such openness calls for partnerships of critical Virgo type—demanding rigorous discipline and spotless conduct. The axis represents the sixth house (personal crisis) / twelfth house (collective karma) polarity at its deepest level.

#### Complete Chinese Interpretation (Secondary Language)

处女/双鱼轴代表个人转化与集体消解之间的极性——两个变动星座都指向进化中的关键状态。

**处女上升**：
- 通过渐进式转化、精神超越、身体更新来突出自我
- 对纯洁和圣洁有深深的渴望
- 可能有很多自我批评或对技术成就的坚持
- 但以双鱼方式遇见伴侣时，可能作为爱人或伴侣过于开放——渴望在集体或事业中失去自我

**双鱼上升**：
- 对集体无意识敞开——可能是灵媒、真正的先知、十字军战士或军队领袖
- 愿景被巨大变革吸收
- 依赖直觉
- 需要处女式批判型伙伴关系——要求严格纪律和无暇行为

**轴线的核心张力**：
- 个人危机vs集体业力
- 第六宫（个人转化）vs第十二宫（集体消解）
- 分析vs综合
- 批判vs接纳

#### Core Points

- **Mutable signs**: Critical states in consciousness evolution
- **Virgo rising**: Transformation through self-improvement, purity yearning
- **Pisces balancing**: Collective immersion, loss of separate self
- **Pisces rising**: Open to collective unconscious, visionary or crusader
- **Virgo partner needed**: Discipline, critical analysis, technique
- **Core polarity**: Personal metamorphosis vs collective dissolution"""
    normalized_text_zh: str = """"""
    subject: str = "Virgo/Pisces Axis - Personal Crisis vs Collective Dissolution"
    factor_refs: list = []
    
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_virgo_pisces_axis___personal_c_001_L1",
    )
    version: str = "1.0.0"
