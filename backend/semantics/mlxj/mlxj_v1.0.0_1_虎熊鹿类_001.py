"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.806601
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
    semantic_id="mlxj_v1.0.0_1_虎熊鹿类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1虎熊鹿类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 虞 | 帝尧 | 白虎 | 皋陶生 |
| 春秋 | 晋侯 | 黄熊入...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 虞 | 帝尧 | 白虎 | 皋陶生 |
| 春秋 | 晋侯 | 黄熊入寝门 | 祀夏郊病愈 |
| 西汉 | 鲁宗范妻 | 鹿迹日炙 | 嫁得夫 |
| 蜀汉 | 张茂 | 大象 | 为郡不善终 |
| 西晋 | 张邈 | 狼啖一脚 | 不行得免 |
| 隋 | 王敬则 | 骑狮子 | 贵达 |
| 北魏 | 张弘士 | 白虎啮指 | 死 |
| 唐 | 史思明 | 群鹿渡水 | 鹿死水乾命尽 |
| 唐 | 某人 | 虎啮伤 | 被虎噬 |
| 宋 | 滕元发母 | 虎行月中 | 生元发 |
| 宋 | 苏长公 | 袖障叱虎 | 识破幻术 |
| 宋 | 伍寺之 | 杀猴 | 病卒 |
| 明 | 夏元吉母 | 舁一巨狼 | 生元吉 |
| 明 | 金纯 | 绿毛虎 | 定襄伯郭公 |
| 明 | 金章 | 二鹿一羊 | 二录乙未 |
| 明 | 郑怀玉女 | 虎跃入其家 | 嫁魏国公 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 虎熊鹿类"
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
        l1_anchor="mlxj_v1.0.0_1_虎熊鹿类_001_L1",
    )
    version: str = "1.0.0"
