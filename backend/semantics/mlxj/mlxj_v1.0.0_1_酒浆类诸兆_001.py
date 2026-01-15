"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.798210
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
    semantic_id="mlxj_v1.0.0_1_酒浆类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1酒浆类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 梦得醇醪：荣华安乐
- 梦馨香甘美：喜事来临
- 饮白酒浆吉：出外遇贤主
- 天雨酒受而饮之：沾天禄
- 把酒邀月吉：秋试领乡荐

**凶类**：
- 饮三白...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 梦得醇醪：荣华安乐
- 梦馨香甘美：喜事来临
- 饮白酒浆吉：出外遇贤主
- 天雨酒受而饮之：沾天禄
- 把酒邀月吉：秋试领乡荐

**凶类**：
- 饮三白酒凶：霜雪、丧服、水灾
- 梦龌龊冷澹：险难多故
- 梦味酸：嗟叹悲伤
- 酒杯中火起凶：阴盛之象

#### 酒味与主应

| 酒味 | 主应 |
|------|------|
| 醇醪 | 荣华安乐 |
| 糟粕 | 窘迫困穷 |
| 甘美 | 喜事来临 |
| 酸 | 嗟叹悲伤 |
| 苦 | 勤劳不素餐 |
| 辛 | 谦让起畏敬 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 酒浆类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_酒浆类诸兆_001_L1",
    )
    version: str = "1.0.0"
