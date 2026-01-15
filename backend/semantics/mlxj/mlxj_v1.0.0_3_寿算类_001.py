"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.804587
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
    semantic_id="mlxj_v1.0.0_3_寿算类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3寿算类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 西汉 | 孙泰 | 神人增寿 | 寿九十七 |
| 西汉 | 陈泊 |...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 西汉 | 孙泰 | 神人增寿 | 寿九十七 |
| 西汉 | 陈泊 | 福寿双全 | 历官台省 |
| 东晋 | 徐宗仁 | 寿延三纪 | 果逾三纪 |
| 宋 | 陈希亮 | 六十四 | 果应 |
| 宋 | 蔡襄 | 青牛托梦 | 高寿 |
| 宋 | 曾公亮 | 必获福寿 | 年八十卒 |
| 宋 | 李谦 | 寿延百岁 | 果百岁终 |
| 明 | 林某 | 寿问孔老人 | 五十七卒 |
| 明 | 唐寅 | 南吕一枝花 | 生年半百 |"""
    normalized_text_zh: str = """"""
    subject: str = "3 寿算类"
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
        l1_anchor="mlxj_v1.0.0_3_寿算类_001_L1",
    )
    version: str = "1.0.0"
