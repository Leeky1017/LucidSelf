"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.782238
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
    semantic_id="mlxj_v1.0.0_2_身体类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2身体类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 全现己身大吉：自知之明，征祥备矣
- 身飞吉：高飞远举之兆
- 身生羽翼大吉：有扶持之兆
- 画两翅在身大吉：齐世祖梦典故
- 身上生甲吉：寿增一纪，身登黄...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 全现己身大吉：自知之明，征祥备矣
- 身飞吉：高飞远举之兆
- 身生羽翼大吉：有扶持之兆
- 画两翅在身大吉：齐世祖梦典故
- 身上生甲吉：寿增一纪，身登黄甲

**吉类**：
- 遍体光鲜润泽：神旺色润，学长才高
- 沐浴伤皮露骨吉：除旧布新

**凶类**：
- 出身露体凶：恐有羞辱
- 懒惰凶：孟虎梦典故
- 寒颤大凶：有虚惊灾病
- 倒立凶：头在地下，下欺上象
- 横跌着地凶：水火之灾

**贞吉否凶类**：
- 如木偶人：有人提挈/病者筋络枯槁
- 如老季景象：少年病后梦大寿/竖子梦凶

#### 身体变化占断原则

| 变化类型 | 吉凶 | 主应 |
|---------|------|------|
| 身飞/生翼 | 大吉 | 高升扶持 |
| 身生甲 | 吉 | 寿增登科 |
| 身光润 | 吉 | 才高貌美 |
| 身露体 | 凶 | 羞辱 |
| 身倒立 | 凶 | 下犯上 |
| 身寒颤 | 大凶 | 灾病 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 身体类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_身体类诸兆_001_L1",
    )
    version: str = "1.0.0"
