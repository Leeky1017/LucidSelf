"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850620
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
    semantic_id="mlxj_v1.0.0_条目十_不占有五_不验有五_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目十不占有五不验有五(SemanticEntry):
    """
    ### 原文（source_text）

梦有不占，占有不验。不占有五：神未定而梦者不占，妄虑而梦者不占，寤知凶阨者不占，寐中撼窉而梦未竟者不占，梦有终始而觉佚其半者不占。不验有五：占梦之人昧厥本原者...
    """
    
    original_text: str = """### 原文（source_text）

梦有不占，占有不验。不占有五：神未定而梦者不占，妄虑而梦者不占，寤知凶阨者不占，寐中撼窉而梦未竟者不占，梦有终始而觉佚其半者不占。不验有五：占梦之人昧厥本原者不验，术业不专者不验，精诚未至者不验，削远为近、揉大为小者不验，依违两端者不验。

### 规范化释义（primary_lang_explained）

占梦的第十条核心原则是「不占有五·不验有五」——列举了五种不宜占梦的情况和五种占梦不验的原因。

**不占有五**：
1. 神志未定时做的梦不占
2. 因妄想忧虑而做的梦不占
3. 醒来就知道是凶厄之梦者不占（因已明其凶，不必强占）
4. 睡眠中被惊扰、梦境未完者不占
5. 梦有始终但醒来遗忘一半者不占

**不验有五**：
1. 占梦者不明梦学根本原理者不验
2. 术业不专精者不验
3. 精诚未至、心不诚者不验
4. 将远事削为近事、将大事揉为小事者不验
5. 两端依违、态度模棱两可者不验

### 核心要点

- 不占有五、不验有五是占梦第十核心原则
- 五种情况不宜占梦
- 五种原因导致占梦不验
- 强调梦境完整性和占者专业性

### 叙事素材（narrative_snippets）

- `[ns_mlxj_025]` `[trigger: 占梦禁忌]` `[factor_trigger: dream_validity]` `[role: 限制条件]` 神未定而梦者不占，妄虑而梦者不占。 → 《梦林玄解·卷之首》#不占有五
- `[ns_mlxj_026]` `[trigger: 占验条件]` `[factor_trigger: interpreter_quality]` `[role: 限制条件]` 占梦之人昧厥本原者不验，术业不专者不验。 → 《梦林玄解·卷之首》#不验有五"""
    normalized_text_zh: str = """"""
    subject: str = "条目十：不占有五·不验有五"
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
        l1_anchor="mlxj_v1.0.0_条目十_不占有五_不验有五_001_L1",
    )
    version: str = "1.0.0"
