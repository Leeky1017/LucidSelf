"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.812781
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
    semantic_id="mlxj_v1.0.0_1_草木类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1草木类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 春秋 | 孔子 | 三槐之间 | 汉兴 |
| 三国 | 丁固 | 松...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 春秋 | 孔子 | 三槐之间 | 汉兴 |
| 三国 | 丁固 | 松生腹上 | 后为公 |
| 唐 | 柳宗元 | 柳树仆地 | 牧柳州 |
| 唐 | 张志和 | 枫生腹上 | 入仙班 |
| 唐 | 齐澣 | 摘紫薇花 | 授紫薇舍人 |
| 宋 | 冯元 | 绀莲花 | 户部尚书 |
| 明 | 胡濙 | 持三花 | 礼部尚书 |
| 明 | 王祎 | 五色芝产门 | 文章之兆 |
| 唐 | 韦正贯 | 欠柴七千七百束 | 柳凌卒 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 草木类"
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
        l1_anchor="mlxj_v1.0.0_1_草木类_001_L1",
    )
    version: str = "1.0.0"
