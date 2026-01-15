"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808907
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
    semantic_id="mlxj_v1.0.0_2_占梦官六梦_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2占梦官六梦(SemanticEntry):
    """
    #### 原文（source_text）

占梦掌其岁时，观天地之会，辨阴阳之气，以日月星辰占六梦之吉凶。一曰正梦，二曰噩梦，三曰思梦，四曰寤梦，五曰喜梦，六曰惧梦。季冬聘王梦，献吉梦于王，王拜而受之...
    """
    
    original_text: str = """#### 原文（source_text）

占梦掌其岁时，观天地之会，辨阴阳之气，以日月星辰占六梦之吉凶。一曰正梦，二曰噩梦，三曰思梦，四曰寤梦，五曰喜梦，六曰惧梦。季冬聘王梦，献吉梦于王，王拜而受之，乃舍萌于四方，以赠恶梦，遂令始难敺疫。

#### 规范化释义（primary_lang_explained）

《周礼》占梦官职责：掌其岁时，观天地之会，辨阴阳之气，以日月星辰占六梦之吉凶。

六梦分类：
1. **正梦**：平正无偏之梦
2. **噩梦**：惊愕之梦
3. **思梦**：因思虑而生之梦
4. **寤梦**：似寤非寤之梦
5. **喜梦**：因喜悦而生之梦
6. **惧梦**：因恐惧而生之梦

季冬聘王梦，献吉梦于王，王拜而受之，乃舍萌于四方，以赠恶梦，遂令始傩驱疫。

#### 核心要点

- 来源：《周礼·春官》
- 六梦分类：正、噩、思、寤、喜、惧
- 占法：观天地之会，辨阴阳之气，以日月星辰占之"""
    normalized_text_zh: str = """"""
    subject: str = "2 占梦官六梦"
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
        l1_anchor="mlxj_v1.0.0_2_占梦官六梦_001_L1",
    )
    version: str = "1.0.0"
