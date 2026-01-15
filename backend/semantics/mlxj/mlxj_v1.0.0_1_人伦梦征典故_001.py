"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.810822
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
    semantic_id="mlxj_v1.0.0_1_人伦梦征典故_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1人伦梦征典故(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 周 | 武王 | 天命子虞 | 封唐为晋 |
| 东汉 | 叔先雄 |...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 周 | 武王 | 天命子虞 | 封唐为晋 |
| 东汉 | 叔先雄 | 父同出 | 与父同浮江上 |
| 东晋 | 王导 | 五百贯买长子 | 长子暴死 |
| 东晋 | 徐精 | 与妻寝 | 远行归妻果产 |
| 齐 | 康王友孜 | 人害己 | 刺客被擒 |
| 梁 | 武帝后 | 生贵子 | 生后 |
| 隋 | 秦王俊 | 亡妃崔氏 | 痫死 |
| 北魏 | 慕容德 | 先人命立超 | 立超为太子 |
| 唐 | 李节妇 | 男子求为妻 | 截发毁容 |
| 唐 | 杨旬 | 神告子必贵 | 子杨椿状元 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 人伦梦征典故"
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
        l1_anchor="mlxj_v1.0.0_1_人伦梦征典故_001_L1",
    )
    version: str = "1.0.0"
