"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559259
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
    semantic_id="acu_v1.0.0_第五节_曼陀罗的起源与结论___627_635___700__001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第五节曼陀罗的起源与结论627635700(SemanticEntry):
    """
    **原文** (¶627-635, 行9695-9735):

> [627] In what follows I shall try to describe a special category o...
    """
    
    original_text: str = """**原文** (¶627-635, 行9695-9735):

> [627] In what follows I shall try to describe a special category of symbols, the mandala, with the help of a wide selection of pictures. I have dealt with this theme on several occasions before.
>
> [629] The Sanskrit word mandala means 'circle.' It is the Indian term for the circles drawn in religious rituals. In the great temple of Madura, in southern India, I saw how such a picture was made. The woman who drew it evidently did not want to be disturbed in her work. The best and most significant mandalas are found in the sphere of Tibetan Buddhism.
>
> [630-631] A mandala of this sort is known in ritual usage as a yantra, an instrument of contemplation. It is meant to aid concentration by narrowing down the psychic field of vision and restricting it to the centre. Usually the mandala contains three circles painted in black or dark blue—to shut out the outside and hold the inside together. The centre is treated differently depending on the requirements of the ritual. As a rule it shows Shiva in his world-creating emanations with Shakti.

**英文释义**：
- 梵语mandala = 圆
- 印度宗教仪式中绘制的圆
- 最佳曼陀罗见于藏传佛教
- 仪式用途中称为yantra（冥想工具）
- 目的：通过缩窄心理视野、限制于中心来辅助集中
- 通常三层黑/深蓝色圆圈 → 隔绝外部、维系内部
- 中心：根据仪式需求不同处理
- 通常显示湿婆（Shiva）与沙克提（Shakti）的创世流出

**中文诠释**：
- 曼陀罗 = 梵语"圆"
- 源于印度宗教仪式
- 最显著曼陀罗在藏传佛教中
- 仪式名称：yantra（冥想工具）
- 功能：缩窄心理视野，集中于中心
- 结构：三层深色圆圈（隔绝外部/维系内部）
- 中心根据仪式/修行者等级/宗派而异
- 通常：湿婆与沙克提的创世流出
- Shiva-bindu（湿婆点）= 非延展点 = 永恒拥抱女性面

**Narrative Snippets**:
- `[ns_cw9i_X_629]` `[trigger: mandala_origin]` `[factor_trigger: jung_mandala AND jung_tibet]` `[role: 主干]` Sanskrit mandala means 'circle'—best and most significant mandalas are found in Tibetan Buddhism. → ¶629
- `[ns_cw9i_X_630]` `[trigger: yantra_function]` `[factor_trigger: jung_mandala AND jung_concentration]` `[role: 主干依赖]` Mandala as yantra (instrument of contemplation)—aids concentration by narrowing psychic field to the centre. → ¶630"""
    normalized_text_zh: str = """"""
    subject: str = "第五节：曼陀罗的起源与结论 (¶627-635, ¶700-712)"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="acu_v1.0.0_第五节_曼陀罗的起源与结论___627_635___700__001_L1",
    )
    version: str = "1.0.0"
