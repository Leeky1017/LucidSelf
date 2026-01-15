"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997385
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
    semantic_id="dts_v1.0.0_官煞相混来问我_有可有不可_001",
    book_id="dts",
    engine_id="bazi"
)
class 官煞相混来问我有可有不可(SemanticEntry):
    """
    - **原文（source_text）**：
  官煞相混来问我，有可有不可。

 - 原注（原文注解）：
  　　煞，即官也。同流同止，可混也。官非煞也，各立门庭，不可混也，煞重矣，官从之，非混也。...
    """
    
    original_text: str = """- **原文（source_text）**：
  官煞相混来问我，有可有不可。

 - 原注（原文注解）：
  　　煞，即官也。同流同止，可混也。官非煞也，各立门庭，不可混也，煞重矣，官从之，非混也。
  　　官轻矣，煞助之，即混也。劫财与比肩双至者，煞可使官混也，一煞而遇食伤者，官助之，非混煞也，势在于官，官有根，杀之情依乎官，依官之煞，岁助之而混官可不也，势在于煞，煞有根，官之情依乎煞，依煞之官，岁忌之而混煞不可也，岁官露煞，干神助官，合官留煞，皆成煞气，不可使官混也，岁煞露官，干神助官，合煞留官，皆成官象，不可使煞混也。

 - 分字分词释义：
  - 官：正官，正当之权与秩序之神，以克身而有礼制。
  - 煞：七杀，偏烈之权，性急劲，克身多险。
  - 相混：官、煞同柱或互见，力量互相牵扯、同对日主起作用。
  - 势在于官/煞：就“旺衰、位置、通根、得令”综合判断谁为主导。
  - 根：在地支得长生、帝旺、比劫等通根之处。

 - **规范化释义（primary_lang_explained）**：
  官星与七杀同属“克我之权”，但有“可混”与“不可混”之别。煞本亦官，若同流同止而势在官、官有根，则煞随官，可混而成“权重”之象；若势在煞、煞有根，而官轻无力，则官随煞，多成“偏狠”之象，不可轻混。又须视劫财比肩、食神等之助力，以及岁运所助何方：岁助官则官为主，岁助煞则煞为主。关键在“势与根”，不可只因见官煞同现便一概混谈。

- **次语种完整诠释（secondary_lang_full）**:  
  Official-Sha官煞相混 context-dependent: 可混 allowed when同流同止 same-direction势在官 guan-dominant官有根 rooted—煞随官 sha-follows-guan as权重 empowered-authority; 不可混 forbidden when势在煞 sha-dominant煞有根 rooted官轻 guan-weak—煞统官 sha-dominates-guan as偏狠 harsh-aggressive; 势与根 power-root determines谁主导 who-leads requiring岁运倾向 transit-alignment not机械混谈 mechanical-mixing."""
    normalized_text_zh: str = """"""
    subject: str = "官煞相混来问我，有可有不可。"
    factor_refs: list = ['guansha_xianghun', 'kehun', 'bukehun', 'shi_zai_guan', 'shi_zai_sha', 'quanzhong']
    
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
        l1_anchor="dts_v1.0.0_官煞相混来问我_有可有不可_001_L1",
    )
    version: str = "1.0.0"
