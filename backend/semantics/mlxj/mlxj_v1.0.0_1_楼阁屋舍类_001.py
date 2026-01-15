"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.812745
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
    semantic_id="mlxj_v1.0.0_1_楼阁屋舍类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1楼阁屋舍类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 东汉 | 张奂妻 | 登楼而歌 | 子知武威 |
| 唐 | 李贺 |...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 东汉 | 张奂妻 | 登楼而歌 | 子知武威 |
| 唐 | 李贺 | 白玉楼成 | 卒 |
| 宋 | 王迈 | 登阁上第四席 | 移置第四 |
| 东晋 | 谯王司马恬 | 邓艾求治舍宇 | 修造庙宇 |
| 唐 | 杨子系 | 松户枣屋 | 二人俱卒 |
| 宋 | 士子 | 先进塲屋 | 第十一名 |
| 明 | 莫灏 | 起屋骑梁 | 中解元 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 楼阁屋舍类"
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
        l1_anchor="mlxj_v1.0.0_1_楼阁屋舍类_001_L1",
    )
    version: str = "1.0.0"
