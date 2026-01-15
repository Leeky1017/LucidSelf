"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.104880
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
    semantic_id="tis_v1.0.0_leo___the_creator__fixed_fire_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class LeoTheCreatorFixedFire(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Fixed Fire | Sustained r...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Fixed Fire | Sustained radiance | Element |
| Self-Expression | Heart-based creation | Core drive |
| Solar Confidence | Inner trust | Strength |
| Generosity | Giving warmth | Function |

#### Source Text

"The Lion. Leo has come into the world to create and celebrate life—to express the unique self, to make something beautiful or meaningful, to bring joy and light. The endpoint is authentic self-expression: living from the heart without apology."

#### English Paraphrase

**Leo** = **Fixed Fire** sign embodying **creative self-expression, celebration, and radiant generosity**. The Lion archetype: regal, confident, living from heart with boldness and warmth.

**Core Drives**:
- **Shine & Radiate**: Step into spotlight, express inner light
- **Create**: Make art, children, businesses—anything bearing unique vision
- **Play**: Approach life with childlike enthusiasm and joy
- **Give Generously**: Share warmth, attention, encouragement freely

**Leonian Strengths**:
- **Confidence**: Deep trust in own worth and creative power (magnetic)
- **Warmth**: Solar radiance, life-giving presence
- **Creative Power**: Channel life-force into form constantly
- **Courage**: Risk being fully self, authentic despite judgment

**Shadow Manifestations**:
- **Vanity**: Desperate need for recognition, performing from fear
- **Arrogance**: Confuse confidence with superiority, demand admiration
- **Drama**: Everything becomes theatrical production, exhausts others
- **Attention-Seeking**: Outrageous behavior for notice, interrupting others' stories

**Evolutionary Challenge**:
Shine WITH others, not instead of them. Celebrate everyone's uniqueness, encourage everyone's creativity, make room for all to play. "I am special, AND astro_so are you. Room for all in the sun."

#### Complete Chinese Interpretation

**狮子座**=**固定火象**星座体现**创造性自我表达、庆祝和辐射慷慨**。狮子原型：威严、自信、从心大胆温暖生活。

**核心驱力**：闪耀与辐射(踏入聚光灯、表达内在光)；创造(制作艺术、孩子、生意——任何带独特视野的)；玩耍(以孩童热情和喜悦接近生活)；慷慨给予(自由分享温暖、注意、鼓励)

**狮子优势**：自信(对自己价值和创造力深信-有磁性)；温暖(太阳辐射、赋予生命临在)；创造力(持续将生命力导入形式)；勇气(冒险完全做自己、尽管被评判仍真实)

**阴影显化**：虚荣(对识别绝望需要、从恐惧表演)；傲慢(混淆自信与优越、要求赞美)；戏剧(一切成戏剧制作、令他人疲惫)；寻求注意(为注意做出格事、打断他人故事)

**进化挑战**：与他人一起闪耀、非替代他们。庆祝每个人独特、鼓励每个人创造、为所有人玩耍腾出空间。"我特别、你也特别。太阳下所有人都有空间。"

#### Core Points

- Fixed Fire: creative radiance through self-expression
- Archetype: regal Lion living from heart
- Resources: confidence, warmth, creative power, courage
- Shadow: vanity, arrogance, drama, attention-seeking
- Challenge: shine with others, not instead
- East parallel: 狮子↔丙火阳刚/食神创造 (yang fire creativity)

#### Detailed Explanation

Leo is **Fixed Fire**—stabilizing creative energy through sustained self-expression. The Lion archetype embodies regal confidence, living boldly and warmly from the heart. Leo has come to **shine**—to radiate inner light through creative expression and generous celebration of life.

Leo's resources include **confidence, warmth, creative power, and courage**—the solar radiance that uplifts and encourages others. Leo believes deeply in its own value, and that belief is magnetic.

**Dysfunction** appears as vanity (obsession with image), arrogance (believing oneself superior), drama (needing constant attention), or attention-seeking (shine as end rather than means). The evolutionary challenge is to **shine with others, not instead of them**—to celebrate everyone's uniqueness, not just one's own.

#### Narrative Snippets

- `[ns_innersky_leo_001]` `[trigger: sign_leo]` `[factor_trigger: sign_leo]` `[role: 主干]` The Lion. Regal, confident, living boldly and warmly from the heart. Leo has come to shine—to radiate inner light through creative self-expression and generous celebration of life. → The Inner Sky Ch.4 #Leo
- `[ns_innersky_leo_002]` `[trigger: sign_leo AND astro_strength]` `[factor_trigger: element_fire]` `[role: 主干依赖]` Leo's gift is solar radiance—life-giving warmth that uplifts, encourages, and celebrates. Deep belief in own value that is magnetic. → The Inner Sky Ch.4 #Leo
- `[ns_innersky_leo_003]` `[trigger: sign_leo AND astro_shadow]` `[factor_trigger: planet_sun]` `[role: 条件分支]` Shadow: desperate need for recognition (vanity), confusion of confidence with superiority (arrogance), everything becomes theatrical production (drama). → The Inner Sky Ch.4 #Leo
- `[ns_innersky_leo_004]` `[trigger: sign_leo AND astro_challenge]` `[factor_trigger: sign_leo]` `[role: 总结]` Evolutionary challenge: shine WITH others, not instead of them. Celebrate everyone's uniqueness. 'I am special, AND so are you. There is room for all under the sun.' → The Inner Sky Ch.4 #Leo"""
    normalized_text_zh: str = """"""
    subject: str = "Leo - The Creator (Fixed Fire)"
    factor_refs: list = ['new_candidate', 'sign_leo', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_leo___the_creator__fixed_fire_001_L1",
    )
    version: str = "1.0.0"
