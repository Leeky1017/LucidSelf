"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.795253
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
    semantic_id="mlxj_v1.0.0_2_家伙类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2家伙类诸兆(SemanticEntry):
    """
    #### 桌椅凳位置占断

| 位置 | 主应 |
|------|------|
| 天际 | 朝皇之象 |
| 自天落庭前 | 天锡大位，富贵恩荣 |
| 白云中 | 事不成 |
| 青云中 | ...
    """
    
    original_text: str = """#### 桌椅凳位置占断

| 位置 | 主应 |
|------|------|
| 天际 | 朝皇之象 |
| 自天落庭前 | 天锡大位，富贵恩荣 |
| 白云中 | 事不成 |
| 青云中 | 登高第 |
| 彩云中 | 官宦书信至 |
| 黑云中 | 鬼神之事 |
| 舟中 | 远行 |
| 车中 | 迁移 |
| 山顶 | 有丧事 |
| 田中 | 丰年 |
| 河水中 | 防水火之灾 |
| 庭中 | 吉 |
| 堂房中 | 正吉，歪不利 |

#### 床类诸兆

**大吉类**：
- 象牙床：富贵
- 镂金床：得钱
- 沉香床：佳偶
- 紫檀床：得良佐
- 玉床：见帝

**吉类**：
- 坐凳升青云大吉：第一等人物
- 锦被绣褥高枕：康宁安乐

**凶类**：
- 床出门：妻妾大凶
- 床破碎：家中有祸
- 床折足：奴婢之灾
- 床无屋：口舌争讼

#### 典故

- 召皎梦绳床：梦床去地数丈，后被擒而释放
- 徐孝嗣梦移床：梦童子移床，壁即崩压床"""
    normalized_text_zh: str = """"""
    subject: str = "2 家伙类诸兆"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_2_家伙类诸兆_001_L1",
    )
    version: str = "1.0.0"
