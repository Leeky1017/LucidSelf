"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.796522
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
    semantic_id="mlxj_v1.0.0_2_干支天象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2干支天象(SemanticEntry):
    """
    #### 天干

| 干支 | 梦象 | 主应 |
|------|------|------|
| 甲乙日 | 苍色事生殖 | 西坠大凶 |
| 丙丁日 | 开眼文显得财 | 沉水凶 |
| 戊巳日...
    """
    
    original_text: str = """#### 天干

| 干支 | 梦象 | 主应 |
|------|------|------|
| 甲乙日 | 苍色事生殖 | 西坠大凶 |
| 丙丁日 | 开眼文显得财 | 沉水凶 |
| 戊巳日 | 压地夫妇和 | 逐身得酒食 |
| 庚辛日 | 开裂兵戈大起 | 色红损害 |
| 壬癸日 | 昏黑阴私事至 | 入怀阴贵会合 |

#### 地支

| 地支 | 梦象 | 主应 |
|------|------|------|
| 亥子日 | 登上肾虚 | 昏黑肝病 |
| 寅卯日 | 青亮肝气平 | 东升红绚吉 |
| 巳午日 | 红赤心火旺 | 两日并出私事 |
| 申酉日 | 转运金戈将起 | 吞食不明事至 |
| 辰戌丑未日 | 门开脾气实 | 初出肝旺凡事吉 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 干支天象"
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
        l1_anchor="mlxj_v1.0.0_2_干支天象_001_L1",
    )
    version: str = "1.0.0"
