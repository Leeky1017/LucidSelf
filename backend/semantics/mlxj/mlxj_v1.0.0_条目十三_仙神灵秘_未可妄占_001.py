"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850645
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
    semantic_id="mlxj_v1.0.0_条目十三_仙神灵秘_未可妄占_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目十三仙神灵秘未可妄占(SemanticEntry):
    """
    ### 原文（source_text）

仙神灵秘，未可妄占。凡泛常之梦，不必用占，惟精诚所感，神灵所告者，方为可占。或神灵指示姓名数目、文字器皿之类，如天机微露，不尽泄漏者，必俟后应，乃见灵验。虽善...
    """
    
    original_text: str = """### 原文（source_text）

仙神灵秘，未可妄占。凡泛常之梦，不必用占，惟精诚所感，神灵所告者，方为可占。或神灵指示姓名数目、文字器皿之类，如天机微露，不尽泄漏者，必俟后应，乃见灵验。虽善占之士，不可妄占，姑识始末，徐以待之。又或冥冤报复，梦既无象，机难悬揣也。

### 规范化释义（primary_lang_explained）

占梦的第十三条核心原则是「仙神灵秘，未可妄占」——涉及仙神灵异的梦，不可轻率妄占。

一般泛常的梦不必刻意占断，只有精诚感应所得、神灵告知的梦，才值得占断。如果神灵指示姓名、数目、文字、器皿等信息，这是天机微露而不尽泄漏，必须等待后来应验，才能见其灵验。

即使是擅长占梦的高手，也不可妄自占断这类梦，应当先记录始末，徐徐等待验证。又如冥冤报复之类的梦，既无明确象征，机缘也难以悬空推测。

### 核心要点

- 仙神灵秘未可妄占是占梦第十三条原则
- 泛常之梦不必用占
- 精诚所感、神灵所告者可占
- 天机微露，必俟后应
- 善占者亦不可妄占，姑识始末，徐以待之
- 冥冤报复之梦，机难悬揣

### 叙事素材（narrative_snippets）

- `[ns_mlxj_030]` `[trigger: 灵异梦]` `[factor_trigger: divine_dream]` `[role: 特殊处理]` 惟精诚所感，神灵所告者，方为可占。 → 《梦林玄解·卷之首》#仙神灵秘
- `[ns_mlxj_031]` `[trigger: 天机]` `[factor_trigger: divine_revelation]` `[role: 等待验证]` 如天机微露，不尽泄漏者，必俟后应，乃见灵验。 → 《梦林玄解·卷之首》#仙神灵秘
- `[ns_mlxj_032]` `[trigger: 梦之结果]` `[factor_trigger: dream_outcome AND dreamer_shenfen AND dreamer_status]` `[role: 核心框架]` 梦之吉凶主应，因人身份而有分化。 → 《梦林玄解·卷之首》#核心概念
- `[ns_mlxj_033]` `[trigger: 历史应验]` `[factor_trigger: lishi_yingyan AND lishi_diangu]` `[role: 验证依据]` 古人之梦有验，可为今人占断之依据。 → 《梦林玄解·卷之首》#核心概念"""
    normalized_text_zh: str = """"""
    subject: str = "条目十三：仙神灵秘，未可妄占"
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
        l1_anchor="mlxj_v1.0.0_条目十三_仙神灵秘_未可妄占_001_L1",
    )
    version: str = "1.0.0"
