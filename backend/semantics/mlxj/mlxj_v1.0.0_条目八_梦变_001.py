"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850603
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
    semantic_id="mlxj_v1.0.0_条目八_梦变_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目八梦变(SemanticEntry):
    """
    ### 原文（source_text）

梦变凡一梦而种种传变，如俄见白日，日出忽雨，才得欢笑，笑者随泣。方登山而泛舟，乃舟行陆地；顷立地而升天，若天包我闼。又如一寝之梦，或屡迁多化，或屡梦不更，或百...
    """
    
    original_text: str = """### 原文（source_text）

梦变凡一梦而种种传变，如俄见白日，日出忽雨，才得欢笑，笑者随泣。方登山而泛舟，乃舟行陆地；顷立地而升天，若天包我闼。又如一寝之梦，或屡迁多化，或屡梦不更，或百物代至，数事一时。梦固多端，记宜全备。倘梦者不能详其前后，述其始终，故占有不中，非占者过，梦者过也。或梦审矣，而占者不能连类博观，精参通变，故占有不验。非经之陋，乃说之陋也。是故占梦者，必求其备，审其变，稽其征候，内考性情，外推王相，庶几凶吉之符，无毛发之爽云。

### 规范化释义（primary_lang_explained）

占梦的第八条核心原则是「梦变」——必须完整记录梦境的变化过程。

一梦之中往往有种种传变：比如刚见白日，忽然下雨；才得欢笑，笑者随即哭泣；方才登山忽而泛舟，舟却行于陆地；刚刚立地忽而升天，天仿佛包裹着门户。又如一夜之梦，或屡次迁变、或始终不变、或百物轮番出现、或数事同时发生。

梦境本来就多端变化，记录务必完备。如果做梦者不能详述前后、讲清始终，导致占断不准，这是梦者的过失而非占者的过失。如果梦境记录清楚，而占者不能连类博观、精参通变，导致占断不验，这是解说者的浅陋而非经典的浅陋。

因此占梦者必须求其完备、审其变化、考其征候、内察性情、外推旺相，才能使吉凶判断毫发不差。

### 核心要点

- 梦变是占梦第八核心原则
- 一梦中往往有多种变化和转折
- 记录梦境必须完备详尽
- 占不中可能是梦者记录不详的过失
- 占不验可能是占者分析不精的过失
- 必须求备、审变、稽征候、考性情、推王相

### 叙事素材（narrative_snippets）

- `[ns_mlxj_021]` `[trigger: 梦境记录]` `[factor_trigger: dream_record_completeness]` `[role: 方法要求]` 梦固多端，记宜全备。 → 《梦林玄解·卷之首》#梦变
- `[ns_mlxj_022]` `[trigger: 占断责任]` `[factor_trigger: dream_record_completeness]` `[role: 责任归属]` 倘梦者不能详其前后，故占有不中，非占者过，梦者过也。 → 《梦林玄解·卷之首》#梦变"""
    normalized_text_zh: str = """"""
    subject: str = "条目八：梦变"
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
        l1_anchor="mlxj_v1.0.0_条目八_梦变_001_L1",
    )
    version: str = "1.0.0"
