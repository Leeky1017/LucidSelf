"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559218
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
    semantic_id="acu_v1.0.0_第3_5节_四与五的困境_魔法圆与阴影___680_691_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第35节四与五的困境魔法圆与阴影680691(SemanticEntry):
    """
    **原文** (¶680-691, 行10403-10549):

> [680-681] These mandalas show a dilemma between four and five. F...
    """
    
    original_text: str = """**原文** (¶680-691, 行10403-10549):

> [680-681] These mandalas show a dilemma between four and five. Five is the number of the "natural" man (trunk with five appendages). Four signifies a conscious totality, the "spiritual" man. The swastika symbolizes the "ideal" man; the five-pointed star symbolizes the material and bodily man. The conflict between "culture" and "nature" was the patient's problem. The patient was thirty-five, in doubt whether to have another child. Fate decided for a cultural, not biological, goal.
>
> [682] Picture by a middle-aged man. At the four cardinal points: an old man (contemplation), Loki/Hephaestus with flaming hair holding a temple, and a light and dark female figure (two aspects of the anima). The old man = archetype of meaning/spirit; the dark chthonic figure = the magical Luciferian element. In alchemy: Hermes Trismegistus versus Mercurius, the "trickster."
>
> [687-689] A seven-year-old boy did a series of circle drawings and hung them round his bed, calling them his "loves." They functioned as a protective magic circle. An eleven-year-old girl drew magic circles intended to stop difficulties from entering the inner psychic space—self-protection. Behind the mandala lurks the devil—the shadow aspect represents disorderly tendencies, the "chaos" that hides behind the self.
>
> [690-691] Round the sun is a circle with eyes, and round this an uroboros. Polyophthalmia (many eyes) frequently occurs in mandalas. The eyes signify observing consciousness. A medieval city with walls and moats arranged quadratically—the Heavenly Jerusalem. In Indian thought: the city of Brahma on Mount Meru.

**英文释义**：
- 四与五的困境：五=自然人（躯干+五肢）；四=意识整体/精神人
- 卐符号=理想人；五角星=物质/身体人
- 文化vs自然的冲突 → 患者的问题
- 四方位四原型：老人（精神）、洛基/赫菲斯托斯（路西法元素）、明暗女性（阿尼玛两面）
- 炼金术：Hermes Trismegistus vs Mercurius骗术师
- 7岁男孩的圆圈画 = "爱" = 保护魔法圆
- 11岁女孩的魔法圆 = 自我保护，阻止困难进入内在
- 曼陀罗背后潜伏魔鬼 = 阴影面 = 混乱
- 多眼性 = 观察意识
- 中世纪城市 = 天上耶路撒冷 = 梵天之城

**中文诠释**：
- 四与五的困境
- 五 = 自然人（躯干+五肢）
- 四 = 意识整体/精神人
- 卐 = 理想人；五角星 = 物质人
- 文化vs自然 = 患者问题
- 四方位四原型形象
- 老人 = 精神/意义原型
- 洛基 = 路西法元素/骗术师
- 明暗女性 = 阿尼玛两面
- 儿童的魔法圆 = 保护功能
- 曼陀罗背后 = 魔鬼/阴影/混乱
- 多眼性 = 观察意识
- 城市曼陀罗 = 天上耶路撒冷 = 梵天城

**Narrative Snippets**:
- `[ns_cw9i_X_680]` `[trigger: four_five]` `[factor_trigger: jung_number AND jung_conflict]` `[role: 主干]` Five = natural man; four = spiritual man. The dilemma of four and five corresponds to the conflict between culture and nature. → ¶680
- `[ns_cw9i_X_687]` `[trigger: children_circles]` `[factor_trigger: jung_mandala AND jung_child]` `[role: 主干依赖]` Children's circle drawings function as protective magic circles—self-protection against outer difficulties. → ¶687-688
- `[ns_cw9i_X_689]` `[trigger: devil_mandala]` `[factor_trigger: jung_shadow AND jung_mandala]` `[role: 条件分支]` Behind the mandala lurks the devil—the shadow aspect represents the chaos that hides behind the self. → ¶689"""
    normalized_text_zh: str = """"""
    subject: str = "第3.5节：四与五的困境、魔法圆与阴影 (¶680-691)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_第3_5节_四与五的困境_魔法圆与阴影___680_691_001_L1",
    )
    version: str = "1.0.0"
