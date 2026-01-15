"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997400
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
    semantic_id="dts_v1.0.0_从得真者只论从_从神又有吉和凶_001",
    book_id="dts",
    engine_id="bazi"
)
class 从得真者只论从从神又有吉和凶(SemanticEntry):
    """
    - **原文（source_text）**：
  从得真者只论从，从神又有吉和凶。

- 原注（原文注解）：
  　　日主孤弱无气，天地人三元，绝无一毫生扶之意，财官等强甚，乃为真从也，既从矣，当论所...
    """
    
    original_text: str = """- **原文（source_text）**：
  从得真者只论从，从神又有吉和凶。

- 原注（原文注解）：
  　　日主孤弱无气，天地人三元，绝无一毫生扶之意，财官等强甚，乃为真从也，既从矣，当论所从之神，如从财则以财为主，财神是木，又看意向，或要火，或要土，而行运得所者必吉，否则凶，从煞等仿此。

- 分字分词释义：
  - 从：不自为体，随所从之神而行。
  - 真从：日主孤弱无根，三元（天干、地支、人元）绝无生扶之意。
  - 从神：所依附之神（财、官、印、煞等），成为新的“体”。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 从 | Following (Cong) | 不自为体随势而行 | Not being own master | cong | existing |
| 真从 | True Following | 彻底弃身从强 | Complete surrender to strong | zhencong | existing |
| 三绝一强 | Three Absolutes One Strong | 根令扶皆绝一方独强 | No root one dominant | sanjue_yiqiang | new_candidate |
| 弃身从之 | Abandon Self to Follow | 舍弃日主意向从之 | Give up self to follow | qishen_congzhi | new_candidate |
| 从神 | Following Spirit | 所依附之强神 | Dominant spirit followed | congshen | existing |
| 顺从神 | Align with Followed | 岁运顺从神之势 | Luck supports followed | shun_congshen | new_candidate |

- **规范化释义（primary_lang_explained）**：
  真从之格，重在“身孤、势绝”：日主全无根气，三元不生扶，而一方财官印煞极强，日主只得弃自身而从之，方为“从得真”。既从之后，就不再以日主为体，只按“从谁”来定吉凶：从财则以财为主，再看财所喜之火土；从官则官为主，再看印、财、比劫之陪衬。岁运若顺从神所喜方向，则吉；反之违其所喜，则凶。

- **次语种完整诠释（secondary_lang_full）**:  
  True-Follow真从 requires三绝一强 three-absolute-one-dominant: 日主body孤弱无根 rootless绝无生扶 no-support from三元 three-sources; 一方财官印煞 one-side独强 uniquely-strong enabling弃身从之 abandon-self-follow—从得真 true-cong只论从神 follow-spirit-as-body not日主 not-self; 从神吉凶 follow-spirit-fortunes via路径喜忌 pathway-preferences requiring顺从神 aligning-follow-spirit忌扶身 avoiding-body-support破从 breaking-follow."""
    normalized_text_zh: str = """"""
    subject: str = "从得真者只论从，从神又有吉和凶。"
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_从得真者只论从_从神又有吉和凶_001_L1",
    )
    version: str = "1.0.0"
