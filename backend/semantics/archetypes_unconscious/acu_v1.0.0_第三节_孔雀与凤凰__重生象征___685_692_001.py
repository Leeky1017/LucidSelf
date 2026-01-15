"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559204
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
    semantic_id="acu_v1.0.0_第三节_孔雀与凤凰__重生象征___685_692_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第三节孔雀与凤凰重生象征685692(SemanticEntry):
    """
    **原文** (¶685-687, 行10471-10498):

> [685] 一个非典型的曼陀罗，基于二元。金月和银月形成上下边缘...在它上面坐着一只孔雀，展开尾巴，左边有一个蛋，大概是孔雀的...
    """
    
    original_text: str = """**原文** (¶685-687, 行10471-10498):

> [685] 一个非典型的曼陀罗，基于二元。金月和银月形成上下边缘...在它上面坐着一只孔雀，展开尾巴，左边有一个蛋，大概是孔雀的。鉴于孔雀和孔雀蛋在炼金术和诺斯替主义中扮演的重要角色，我们可以期待cauda pavonis的奇迹，所有颜色的出现（波墨），整体性的展开和实现...
>
> [686] 这幅画转载自苏黎世中央图书馆的炼金术手稿。这里的孔雀代表从火中新生的凤凰。

**英文释义**:

非典型曼陀罗：二元基础（金月/银月）。孔雀+蛋 = 炼金术+诺斯替主义重要象征。Cauda pavonis（孔雀尾）= "所有颜色"（波墨）= 整体性展开。孔雀 = 凤凰（从火中重生）。蛋可能裂开产生蛇。孔雀是古老的重生与复活象征（基督教石棺常见）。

**完整中文诠释**:

**孔雀象征**：
- 孔雀 = 凤凰（同义词在炼金术中）
- 从火中新生重生
- Cauda pavonis（孔雀尾）= 所有颜色出现
- 波墨："所有颜色" = 整体性的展开和实现

**炼金术关联**：
- 孔雀+蛋在炼金术和诺斯替主义中重要
- 转化过程接近目标的标志
- 与vas hermeticum（密封容器）中的小人类似

**变体传说**：
- Semenda鸟自焚
- 灰烬中生虫
- 虫中凤凰重生

**基督教象征**：
- 孔雀 = 古老的重生与复活象征
- 常见于基督教石棺

**核心要点**:
- 孔雀 = 凤凰 = 重生象征
- Cauda pavonis = 所有颜色 = 整体性展开
- 炼金术转化接近完成的标志
- 孔雀蛋可能产生蛇（新开始）

**叙事片段**:
- `[ns_cw9i_X_004]` `[trigger: 孔雀凤凰]` `[factor_trigger: jung_peacock AND jung_phoenix]` `[role: 主干]` 孔雀=凤凰，从火中重生——cauda pavonis是所有颜色，整体性的展开和实现。→ ¶685-686"""
    normalized_text_zh: str = """"""
    subject: str = "第三节：孔雀与凤凰——重生象征 (¶685-692)"
    factor_refs: list = ['peacock_phoenix', 'cauda_pavonis', 'rebirth']
    
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
        l1_anchor="acu_v1.0.0_第三节_孔雀与凤凰__重生象征___685_692_001_L1",
    )
    version: str = "1.0.0"
