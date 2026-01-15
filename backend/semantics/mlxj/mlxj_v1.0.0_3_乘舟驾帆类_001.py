"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.799587
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
    semantic_id="mlxj_v1.0.0_3_乘舟驾帆类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3乘舟驾帆类(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 升银汉才郎：幸任紫薇郎
- 至日宫雅士：恩荣赤黻
- 涉湖海：获千箱厚利
- 泛江河：达万里前程
- 济濠隍：嘉遁吉祥无悔
- 浮池照：丰亨游玩有情

**...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 升银汉才郎：幸任紫薇郎
- 至日宫雅士：恩荣赤黻
- 涉湖海：获千箱厚利
- 泛江河：达万里前程
- 济濠隍：嘉遁吉祥无悔
- 浮池照：丰亨游玩有情

**吉类**：
- 逆风驾蓬：得计不愁逆径
- 舟过高山松柏：史巫纷若利无灾
- 泛舟青云彩雾：名誉升腾达天听

**凶类**：
- 顺帆达岸：失时误入欹斜
- 逆风逆水落蓬帆：作事须谦退
- 河狭水乾篙费力：收心且待时

#### 舟载物类

| 所载 | 卦象 | 主应 |
|------|------|------|
| 木 | 风雷益 | 损上益下 |
| 金 | - | 财利 |
| 土石 | - | 建造 |
| 麦 | - | 丧事/吊奠 |"""
    normalized_text_zh: str = """"""
    subject: str = "3 乘舟驾帆类"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_3_乘舟驾帆类_001_L1",
    )
    version: str = "1.0.0"
