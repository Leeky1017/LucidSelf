"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997323
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
    semantic_id="dts_v1.0.0_方是方兮局是局_方要得方莫混局_001",
    book_id="dts",
    engine_id="bazi"
)
class 方是方兮局是局方要得方莫混局(SemanticEntry):
    """
    - **原文（source_text）**：
  方是方兮局是局，方要得方莫混局。

- 原注（原文注解）：
  　　如寅卯辰，东方也，杂以亥卯未则太过，岂不为混局哉。

- 分字分词释义：
  - ...
    """
    
    original_text: str = """- **原文（source_text）**：
  方是方兮局是局，方要得方莫混局。

- 原注（原文注解）：
  　　如寅卯辰，东方也，杂以亥卯未则太过，岂不为混局哉。

- 分字分词释义：
  - 方：方位、方气（寅卯辰为东方）。
  - 局：三合局（如亥卯未木局）。
  - 莫混：不可混淆方与局之用。

 - **规范化释义（primary_lang_explained）**：
  方与局是两套体系。用方，当得其方；不可混以局使之太过。

- **次语种完整诠释（secondary_lang_full）**:  
  This rule draws a clear line between directional assemblies and trinity assemblies. A Fang, such as the eastern cluster Yin–Mao–Chen, already concentrates one side of the compass and brings that element to the front. A Ju, such as the Hai–Mao–Wei trinity, is a different way of gathering the same qi. When judgment is based on the Fang, that directional configuration should stand on its own; if you then stack a full Ju of the same element on top, the qi becomes too dense and the pattern turns heavy and distorted. The instruction is therefore to choose one main system at a time: either use the directional Fang as the frame, or use the trinity Ju, but do not mix them just to make the same element look ever stronger."""
    normalized_text_zh: str = """"""
    subject: str = "方是方兮局是局，方要得方莫混局。"
    factor_refs: list = ['fang', 'ju', 'mohun', 'taiguo', 'hunju', 'zhuanfang']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_方是方兮局是局_方要得方莫混局_001_L1",
    )
    version: str = "1.0.0"
