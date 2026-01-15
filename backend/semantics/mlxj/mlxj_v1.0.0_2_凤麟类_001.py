"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.806591
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
    semantic_id="mlxj_v1.0.0_2_凤麟类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2凤麟类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 春秋 | 孔子 | 刍儿捶麟 | 得麟书三卷 |
| 梁 | 王昙逸母...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 春秋 | 孔子 | 刍儿捶麟 | 得麟书三卷 |
| 梁 | 王昙逸母 | 灵凤集身 | 为神仙宗伯 |
| 齐 | 世祖 | 凤下溪泽 | 位禅宋朝 |
| 宋 | 段少连 | 凤止家庭 | 官居学士 |
| 唐 | 杨雄 | 吐白凤 | 甘泉赋成 |
| 唐 | 汉祖 | 赤乌 | 祥显 |
| 宋 | 张九龄母 | 群鹤 | 生九龄 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 凤麟类"
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
        l1_anchor="mlxj_v1.0.0_2_凤麟类_001_L1",
    )
    version: str = "1.0.0"
