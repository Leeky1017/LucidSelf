"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042594
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
    semantic_id="smth_v1.0.0_己土为云_001",
    book_id="sanming",
    engine_id="bazi"
)
class 己土为云(SemanticEntry):
    """
    - **原文（source_text）**：
  己土为云。己土生居酉，酉兑方也，其象为泽。先正曰：「天降时雨，山川出云。」然则云者，山泽之气也，己虽属土，以此论之，则其谓之云也亦宜。故甲己合而化土，...
    """
    
    original_text: str = """- **原文（source_text）**：
  己土为云。己土生居酉，酉兑方也，其象为泽。先正曰：「天降时雨，山川出云。」然则云者，山泽之气也，己虽属土，以此论之，则其谓之云也亦宜。故甲己合而化土，其气上升而云施；云雷交而作雨，其泽下究而土润。此造化之至妙者与！凡身主属己土，贵坐酉，贵春生，贵见印；坐亥者不可见乙木，云升天，遇风则狼藉而不禁也。

- **分字分词释义**：
  - **云者山泽之气**：云是山川泽气上升所成，比喻己土之气轻灵化腾。
  - **甲己合土、气上成云**：干合之象，土气上升为云，云又化雨润土。
  - **云升遇风狼藉**：提示己土上腾无所依托时，易被风散。

- **规范化释义（primary_lang_explained）**：
  己土比云：虽属土，却善于化气上升，如山泽之气蒸腾为云。甲己合土之象，喻土气上腾成云，又由云雷化雨下润大地，循环出入。己日身主若坐酉位、得春生、有印绶，土气上升得其所，用之有度；若坐亥见乙，则云升遇风，被木风所散，气机狼藉。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth is compared to clouds rising from mountains and marshes: although it is still earth in substance, its qi tends to dissolve upward into vapour. The union of Jia and Ji forming earth is taken further here: their combined earth‑qi ascends to become cloud, and when cloud joins with thunder it turns back into rain that returns to moisten the soil. Ji‑day people who sit on You, are born in spring, and receive support from Seals show this pattern at its best: their grounding can rise into thought, mood, and imagination without losing contact with reality, and what goes up eventually falls back as nourishment. When Ji sits on Hai and meets Yi, by contrast, the text warns of “clouds rising into the sky and being scattered by wind”: ideas and feelings are whipped about by Wood‑type winds, leading to confusion and loss of focus. In practice, this image encourages us to treat Ji Earth as the mediator between solid ground and weather—good at buffering, digesting, and sending signals upward—while being wary of situations where it evaporates into mist that never condenses into real support."""
    normalized_text_zh: str = """"""
    subject: str = "己土为云"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_己土为云_001_L1",
    )
    version: str = "1.0.0"
