"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997827
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
    semantic_id="dts_v1.0.0_何知其人吉_喜神为辅弼_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人吉喜神为辅弼(SemanticEntry):
    """
    - 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人吉：此人吉祥、行运顺遂。
  - 喜神：命局中对日主有利的神煗。
  - 辅弼：辅佐帮助、如大臣之于君主。

- 原注（原文注解）...
    """
    
    original_text: str = """- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人吉：此人吉祥、行运顺遂。
  - 喜神：命局中对日主有利的神煗。
  - 辅弼：辅佐帮助、如大臣之于君主。

- 原注（原文注解）：
 　　喜神辅助官星、印星、身星，化解忌神之力，故吉。

- 规范化释义（primary_lang_explained）：
  论一人行运多吉，要看喜神是否得势，并能在关键处起"辅弼"之功：或助用神成格，或救局中之偏，或在凶运中暗中托底，使祸不至极。

- **核心要点**：
  - 吉象的根本，在于喜神有力、有位、有事可做；
  - 喜神若只名义存在而无根、无机，难言真吉；
  - 辅弼之功在“补不足、救其偏”。

- 详细解说：
  “喜神为辅弼”强调：判断吉运不能只看表面合冲，而要看喜神是否真正参与了结构的修复与成就。例如用印之局，行印旺之运能扶身护官；用财之局，行财旺而不伤体用之运能开财路；甚至在凶局中，若喜神恰好制约忌神、疏导滞气，也可化大凶为小凶、化灾为喜。此类运岁的共同特征，是喜神不但出现，而且“用得上”。

- 校勘与字词辨析：
  - “辅弼”：原为辅佐君主之臣，借指能在结构关键处起扶助作用之星。

- **次语种完整诠释（secondary_lang_full）**：  
  We recognise a fundamentally fortunate pattern when the Favorable gods are active as true helpers: they stand beside the main Useful god, repair weaknesses in the structure, and appear in luck cycles at the very times when support is needed. Their presence does not just add decoration but actually turns situations around."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人吉，喜神为辅弼。"
    factor_refs: list = ['ji_grade', 'xishen', 'fubi_function']
    
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
        l1_anchor="dts_v1.0.0_何知其人吉_喜神为辅弼_001_L1",
    )
    version: str = "1.0.0"
