"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831797
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
    semantic_id="mlxj_v1.0.0_1_雪象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1雪象(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 雪成蛾吉：女招贤夫产秀女，男纳美妾买良婢
- 蟹喷泡作雪吉：士人主解首攒花、黄甲惊涛

**吉类**：
- 雪落身上：功名到手，禄位弥新
- 梅花化雪飞：功...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 雪成蛾吉：女招贤夫产秀女，男纳美妾买良婢
- 蟹喷泡作雪吉：士人主解首攒花、黄甲惊涛

**吉类**：
- 雪落身上：功名到手，禄位弥新
- 梅花化雪飞：功名怀孕皆吉
- 狗奔雪地吉：阳驱阴土，万事光明

**凶类**：
- 雪压谷菜倒凶：主有小人侮弄
- 雪冻驴不行：旅邸萧条，经商少利

**贞吉否凶类**：
- 雪中现青莲花：与佛为缘，主有空门之愿
- 燕子飞雪中：孕妇生贵子，秋元获春魁"""
    normalized_text_zh: str = """"""
    subject: str = "1 雪象"
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
        l1_anchor="mlxj_v1.0.0_1_雪象_001_L1",
    )
    version: str = "1.0.0"
