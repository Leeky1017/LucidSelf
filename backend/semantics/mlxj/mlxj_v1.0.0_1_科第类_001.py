"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.804572
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
    semantic_id="mlxj_v1.0.0_1_科第类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1科第类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 唐 | 窦卢署 | 四举成名 | 署字四划 |
| 宋 | 隽宗远 |...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 唐 | 窦卢署 | 四举成名 | 署字四划 |
| 宋 | 隽宗远 | 来年状元王尧臣 | 果然 |
| 宋 | 黄汝楫 | 五子科第 | 子开阁闶阅闿皆登第 |
| 宋 | 祝染 | 施粥之报 | 子特科状元 |
| 明 | 姚夔 | 商辂解元 | 商第一姚次科第一 |
| 明 | 卓天锡 | 王老死之年 | 中解元 |
| 明 | 孙贤 | 明日状元到 | 果状元 |
| 明 | 金石 | 汝中第十名 | 果然 |
| 明 | 王徽 | 登高梯三次坠 | 三场中式丁忧 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 科第类"
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
        l1_anchor="mlxj_v1.0.0_1_科第类_001_L1",
    )
    version: str = "1.0.0"
