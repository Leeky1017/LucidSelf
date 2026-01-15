"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.847077
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
    semantic_id="mlxj_v1.0.0_1_天干人伦_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1天干人伦(SemanticEntry):
    """
    | 干支 | 君臣 | 父母 | 师友 | 兄弟 |
|------|------|------|------|------|
| 甲乙日 | 东方见君父加衣服吉 | 母加衣血气 | 师得吉友好人相逢...
    """
    
    original_text: str = """| 干支 | 君臣 | 父母 | 师友 | 兄弟 |
|------|------|------|------|------|
| 甲乙日 | 东方见君父加衣服吉 | 母加衣血气 | 师得吉友好人相逢 | 兄左弟右方吉事 |
| 丙丁日 | 帝王南行得吉 | 祖考祭祀得吉 | 师友南方喜事 | 兄弟姊妹火口舌烛 |
| 戊巳日 | 帝王太平安吉 | 父精神旺吉 | 师友宅安 | 兄弟衣服攺易 |
| 庚辛日 | 天子命召 | 父母金银财物 | 师怒得财吉 | 兄弟吉祥 |
| 壬癸日 | 君召水中得利 | 祖考阴人事 | 师友妻家多事 | 兄左手足病弟右手足病 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 天干人伦"
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
        l1_anchor="mlxj_v1.0.0_1_天干人伦_001_L1",
    )
    version: str = "1.0.0"
