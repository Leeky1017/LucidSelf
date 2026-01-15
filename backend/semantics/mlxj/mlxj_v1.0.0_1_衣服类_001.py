"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.812762
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
    semantic_id="mlxj_v1.0.0_1_衣服类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1衣服类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 东晋 | 姚襄 | 弟服衮衣升御座 | 苌称秦王 |
| 东晋 | 索...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 东晋 | 姚襄 | 弟服衮衣升御座 | 苌称秦王 |
| 东晋 | 索充 | 虏脱上衣 | 妇生男 |
| 齐 | 柳庆远 | 褥席见赐 | 开府 |
| 宋 | 岳真人母 | 老人皓发长身 | 生真人 |
| 唐 | 玄宗 | 兵着绯禈 | 赐钱五百千 |
| 唐 | 张𬸦 | 着绯乘驴 | 授鸿胪丞 |
| 宋 | 沈彬 | 锦衣贴月飞 | 吏部郎中 |
| 宋 | 王元规 | 衣冠高古 | 河清县主簿 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 衣服类"
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
        l1_anchor="mlxj_v1.0.0_1_衣服类_001_L1",
    )
    version: str = "1.0.0"
