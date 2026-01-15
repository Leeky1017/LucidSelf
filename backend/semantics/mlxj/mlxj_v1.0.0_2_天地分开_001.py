"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793412
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
    semantic_id="mlxj_v1.0.0_2_天地分开_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2天地分开(SemanticEntry):
    """
    #### 原文（source_text）

天地分开，贞吉，否，凶。占上下隔绝之象，贵者梦此，名位肃清；常人梦之，主父母夫妇、主仆分离违背。

#### 规范化释义（primary_lang_expl...
    """
    
    original_text: str = """#### 原文（source_text）

天地分开，贞吉，否，凶。占上下隔绝之象，贵者梦此，名位肃清；常人梦之，主父母夫妇、主仆分离违背。

#### 规范化释义（primary_lang_explained）

梦见天地分开，正则吉，否则凶。占断为上下隔绝之象。贵人梦此，主名位肃清整肃；常人梦此，主父母、夫妇、主仆之间分离违背。

#### 核心要点

- **梦象**：天地分开
- **吉凶**：贞吉否凶（正则吉，不正则凶）
- **象义**：上下隔绝
- **人群分占**：贵人主名位肃清；常人主亲属分离

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v1_006]` `[trigger: 天地分]` `[factor_trigger: dream_symbol_tiandi_fen AND yijing_pi]` `[role: 条件吉凶]` 贵者梦此，名位肃清；常人梦之，主父母夫妇分离。 → 《梦林玄解·卷一》#天地分开"""
    normalized_text_zh: str = """"""
    subject: str = "2 天地分开"
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
        l1_anchor="mlxj_v1.0.0_2_天地分开_001_L1",
    )
    version: str = "1.0.0"
