"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.804563
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
    semantic_id="mlxj_v1.0.0_2_头额类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2头额类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 蜀汉 | 魏延 | 头生角 | 为杨仪所杀 |
| 齐 | 高洋 | ...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 蜀汉 | 魏延 | 头生角 | 为杨仪所杀 |
| 齐 | 高洋 | 笔点额 | 王上加点为主字 |
| 齐 | 高浟 | 斩头持去 | 见杀 |
| 宋 | 刘沆 | 砍落头 | 第二名 |
| 宋 | 岳某李某 | 两易其头 | 俱显贵 |
| 明 | 解缙 | 头生羊角 | 状元 |
| 明 | 陈宪副 | 额有兽头 | 除御史 |

#### 头生角典故（详）

蜀汉魏延梦头生角，问占梦赵直。

直诈曰：麒麟有角而不用，此不战而自附之象。

退而告人曰：角之为字，刀下用也。头上用刀，其凶甚矣。

果为杨仪所杀。"""
    normalized_text_zh: str = """"""
    subject: str = "2 头额类"
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
        l1_anchor="mlxj_v1.0.0_2_头额类_001_L1",
    )
    version: str = "1.0.0"
