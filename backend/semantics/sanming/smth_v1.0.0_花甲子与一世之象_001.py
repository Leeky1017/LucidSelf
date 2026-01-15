"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227649
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
    semantic_id="smth_v1.0.0_花甲子与一世之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 花甲子与一世之象(SemanticEntry):
    """
    - **原文（source_text）**：
  昔者，黄帝将甲子分轻重而配成六十，号曰花甲子，其花字诚为奥妙，圣人借意而喻之，不可着意执泥。夫自子至亥十二宫，各有金、木、水、火、土之属，始起于子为一...
    """
    
    original_text: str = """- **原文（source_text）**：
  昔者，黄帝将甲子分轻重而配成六十，号曰花甲子，其花字诚为奥妙，圣人借意而喻之，不可着意执泥。夫自子至亥十二宫，各有金、木、水、火、土之属，始起于子为一阳，终于亥为六阴，其五行所属金、木、水、火、土，在天为五星，于地为五岳，于德为五常，于人为五脏，其于命也为五行。是故甲子之属乃应之于命，命则一世之事。故甲子纳音象，圣人喻之，亦如人一世之事也。

- 分字分词释义：
  - **花甲子**：六十甲子的别称，强调其象义繁富，如花团锦簇。
  - **分轻重而配成六十**：根据气机轻重不同，细分为六十种象位。
  - **五行对应五星、五岳、五常、五脏**：说明五行不仅属物，更贯穿天文、地理、德性与人体。

- **规范化释义（primary_lang_explained）**：
  本节说明纳音取象的根本精神：黄帝把六十甲子分出轻重，配成所谓「花甲子」，以丰富的比喻来表达命运的一世之事。十二宫各有其金木水火土之属，这五行又分别对应天上的五星、地上的五岳、人伦的五常以及人体的五脏，因此六十甲子纳音所取之象，不只是材料或景物，而是在用一个象群来描述「一生之结构」。

- **完整对等诠释（secondary_lang_full）**：

  The notion of "Flower Jiazi" explains the spirit behind Nayin imagery. The Yellow Emperor is said to have weighed the light and heavy of Qi and distributed them across the sixty stem–branch positions, making each Jiazi a distinct "flower" in a richly varied cluster. Each of the twelve branches carries its own set of Metal, Wood, Water, Fire and Earth, and these Five Elements in turn correspond to the five planets in heaven, the five sacred mountains on earth, the five constant virtues and the five viscera of the human body. When a Nayin image is assigned to a Jiazi, it is therefore not just naming a material or scenery; it is using a cluster of symbols to encode how one lifetime is structured—what kinds of qualities, terrains, virtues and bodily emphases are woven into that particular sixty‑step pattern."""
    normalized_text_zh: str = """"""
    subject: str = "花甲子与一世之象"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_花甲子与一世之象_001_L1",
    )
    version: str = "1.0.0"
