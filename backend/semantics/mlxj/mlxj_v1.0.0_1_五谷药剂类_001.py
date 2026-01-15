"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.812773
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
    semantic_id="mlxj_v1.0.0_1_五谷药剂类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1五谷药剂类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 东晋 | 刘殷 | 西篱下有粟 | 得粟十五钟 |
| 齐 | 陈皇后...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 东晋 | 刘殷 | 西篱下有粟 | 得粟十五钟 |
| 齐 | 陈皇后 | 两瓯麻粥 | 有乳 |
| 隋 | 孛礼之 | 煮小麦渍之 | 卒 |
| 宋 | 叶文凤 | 食麻糍 | 知前生子 |
| 明 | 张守规 | 支米七十二人 | 中七十二名 |
| 梁 | 何点 | 授丸一掬 | 病差 |
| 陈 | 王颁 | 人投药 | 创不痛 |
| 宋 | 赵子固 | 牛黄金虎丹 | 母病愈 |
| 宋 | 张汝明 | 服天南星 | 验 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 五谷药剂类"
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
        l1_anchor="mlxj_v1.0.0_1_五谷药剂类_001_L1",
    )
    version: str = "1.0.0"
