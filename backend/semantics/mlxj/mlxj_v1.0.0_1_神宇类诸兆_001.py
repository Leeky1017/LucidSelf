"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.814396
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
    semantic_id="mlxj_v1.0.0_1_神宇类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1神宇类诸兆(SemanticEntry):
    """
    #### 分类汇总

**佛寺类**：
- 宝刹壮丽：吉祥
- 宝塔辉煌：高举
- 登殿礼拜：身心斋洁
- 入佛寺：平人吉，贵人凶

**道家类**：
- 入道家宫观：常人吉，病者不祥
- 仙府：张亶...
    """
    
    original_text: str = """#### 分类汇总

**佛寺类**：
- 宝刹壮丽：吉祥
- 宝塔辉煌：高举
- 登殿礼拜：身心斋洁
- 入佛寺：平人吉，贵人凶

**道家类**：
- 入道家宫观：常人吉，病者不祥
- 仙府：张亶典故

**家庙类**：
- 建造修葺：富贵增益
- 拜奠蒸尝：爵禄丰亨

#### 典故

- 宋王球狱中念观音：梦沙门授经，锁皆断脱
- 宗泽梦九级浮屠：见岳飞荐为将
- 苏辙梦三清殿老子：戒杀生延寿"""
    normalized_text_zh: str = """"""
    subject: str = "1 神宇类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_神宇类诸兆_001_L1",
    )
    version: str = "1.0.0"
