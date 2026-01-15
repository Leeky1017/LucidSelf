"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997748
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
    semantic_id="dts_v1.0.0_夫妻_子女_父母_兄弟_女命_气势_拔要_001",
    book_id="dts",
    engine_id="bazi"
)
class 夫妻子女父母兄弟女命气势拔要(SemanticEntry):
    """
    - 原文与原注（节要）：
  - 夫妻姻缘宿世来，喜神有意傍妻财……依财看妻；活看财与官印比劫之势。
  - 子女根枝一世传，喜神看与杀相联……依官看子；官轻身旺助官，杀重身轻印比。
  - 父母或兴...
    """
    
    original_text: str = """- 原文与原注（节要）：
  - 夫妻姻缘宿世来，喜神有意傍妻财……依财看妻；活看财与官印比劫之势。
  - 子女根枝一世传，喜神看与杀相联……依官看子；官轻身旺助官，杀重身轻印比。
  - 父母或兴与或替，岁月所关果非细……财为父、印为母，岁月最要，兼看大势与生扶之神。
  - 兄弟谁废与谁兴，提纲喜神问重轻……劫比阳刃皆兄弟，较其与财官之轻重定兴替。
  - 女命须要论安详……不执二德三奇与咸池驿马，重安详顺静。
  - 小财杀论精神……四柱平和、气势悠长者，即有关煞亦不伤身。

- **规范化释义（primary_lang_explained）**：
  六亲断法以“体用、喜忌、岁月与气势”为纲，活看会冲合刑与生扶泄制。

- 分字分词释义：
  - 妻财/官杀/印枭/比劫：六亲映射之功能位。
  - 岁月：大势与提纲之权重。
  - 气势：全局之强弱与走向。"""
    normalized_text_zh: str = """"""
    subject: str = "夫妻、子女、父母、兄弟、女命、气势（拔要）。"
    factor_refs: list = ['liuqin', 'sushi_yinyuan', 'genzhi', 'qishi', 'xingti', 'anxiang']
    
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
        l1_anchor="dts_v1.0.0_夫妻_子女_父母_兄弟_女命_气势_拔要_001_L1",
    )
    version: str = "1.0.0"
