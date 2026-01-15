"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831820
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
    semantic_id="mlxj_v1.0.0_1_节令诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1节令诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 贺年吉：元旦令辰，主益寿延年
- 元宵赏灯大吉：上元观灯，登元之兆，文士大吉
- 中秋玩月大吉：文章秋捷，家室重圆
- 重九登高吉：名高天下，位佐九重

*...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 贺年吉：元旦令辰，主益寿延年
- 元宵赏灯大吉：上元观灯，登元之兆，文士大吉
- 中秋玩月大吉：文章秋捷，家室重圆
- 重九登高吉：名高天下，位佐九重

**吉类**：
- 清明祭扫祖茔吉：耀祖荣宗
- 穿针乞巧吉：婚姻配偶，财货丰盈

**凶类**：
- 游春遇雪：乐极悲生，主外孝之服
- 大热避暑入山凶：解组归山（夏令无妨）

**贞吉否凶类**：
- 龙舟：非有虚喜必有虚惊，浮而不实
- 登高雨阻：功名不能上达"""
    normalized_text_zh: str = """"""
    subject: str = "1 节令诸兆"
    factor_refs: list = []
    
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
        l1_anchor="mlxj_v1.0.0_1_节令诸兆_001_L1",
    )
    version: str = "1.0.0"
