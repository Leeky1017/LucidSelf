"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559164
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
    semantic_id="acu_v1.0.0_第二节_曼陀罗图像分析___650_680_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第二节曼陀罗图像分析650680(SemanticEntry):
    """
    **原文** (¶662-676, 行10212-10357):

> [662] 这里从中心发出的四道光芒扩展到整个画面。这给中心一个动态特征。花的结构是四的倍数...
>
> [671] 鱼代替蛇...
    """
    
    original_text: str = """**原文** (¶662-676, 行10212-10357):

> [662] 这里从中心发出的四道光芒扩展到整个画面。这给中心一个动态特征。花的结构是四的倍数...
>
> [671] 鱼代替蛇。鱼和蛇同时是基督和魔鬼的属性。鱼在无意识的海洋中制造漩涡，在其中形成珍贵的珍珠...
>
> [672] 通常蛇人格化无意识，而鱼通常代表其内容之一。这些微妙的区别在解释曼陀罗时必须牢记...
>
> [676] 病人是一位六十岁的女性，有艺术天赋。个体化过程，长期受阻但通过治疗释放，刺激了她的创造活动...

**英文释义**:

图像分析：四道光芒从中心扩展 = 动态中心。花结构 = 四的倍数。鱼/蛇 = 基督+魔鬼的双重属性。蛇 = 无意识本身；鱼 = 无意识的内容。鱼在无意识海洋制造漩涡 → 珍珠形成。蛇更原始/本能；鱼更高级/权威（Ichthys象征）。治疗释放个体化过程 → 刺激创造活动。

**完整中文诠释**:

**图像结构分析**：
- 四道光芒从中心扩展 = 动态中心
- 花结构 = 四的倍数
- 太阳/星星 = 中心象征
- 上/下区分 = 意识/无意识

**蛇与鱼的区别**：
- 蛇 = 无意识本身（更原始、本能）
- 鱼 = 无意识的内容（更高级、分化）
- 两者都是基督和魔鬼的属性
- 鱼的历史权威高于蛇（Ichthys象征）

**珍珠象征**：
- 鱼在无意识海洋制造漩涡
- 漩涡中心形成珍珠
- 珍珠 = "难以获得的宝藏"

**治疗与创造**：
- 个体化过程释放 → 创造活动
- 60岁女性的曼陀罗系列
- 颜色丰富表达体验强度

**核心要点**:
- 四道光芒 = 动态中心
- 蛇 = 无意识；鱼 = 无意识内容
- 鱼比蛇更分化（发展阶段不同）
- 珍珠 = 难以获得的宝藏
- 治疗释放个体化和创造力

**叙事片段**:
- `[ns_cw9i_X_002]` `[trigger: 蛇鱼区别]` `[factor_trigger: jung_snake AND jung_fish]` `[role: 主干]` 蛇人格化无意识本身，鱼代表其内容——鱼更分化，历史上有更高权威（Ichthys）。→ ¶671-672
- `[ns_cw9i_X_003]` `[trigger: 珍珠形成]` `[factor_trigger: jung_pearl AND jung_treasure]` `[role: 主干依赖]` 鱼在无意识海洋制造漩涡，在中心形成珍贵珍珠——难以获得的宝藏。→ ¶671"""
    normalized_text_zh: str = """"""
    subject: str = "第二节：曼陀罗图像分析 (¶650-680)"
    factor_refs: list = ['snake_unconscious', 'fish_content', 'pearl_treasure', 'dynamic_center']
    
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
        l1_anchor="acu_v1.0.0_第二节_曼陀罗图像分析___650_680_001_L1",
    )
    version: str = "1.0.0"
