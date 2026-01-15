"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.804579
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
    semantic_id="mlxj_v1.0.0_2_官禄类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2官禄类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 唐 | 钟离介 | 君尹吾邑 | 知仙居县 |
| 唐 | 戴胄 | ...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 唐 | 钟离介 | 君尹吾邑 | 知仙居县 |
| 唐 | 戴胄 | 君得五品 | 授婺州治中 |
| 唐 | 王潘 | 河南尹 | 二十年后果除 |
| 唐 | 高元裕 | 十年作襄州刺史 | 二十年后验 |
| 宋 | 查道 | 子位正郎寿五十七 | 右司郎中年六十四 |
| 宋 | 冯商 | 鼓吹送状元 | 子冯京三元 |
| 明 | 李本 | 十八岁尚书 | 本字含十八 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 官禄类"
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
        l1_anchor="mlxj_v1.0.0_2_官禄类_001_L1",
    )
    version: str = "1.0.0"
