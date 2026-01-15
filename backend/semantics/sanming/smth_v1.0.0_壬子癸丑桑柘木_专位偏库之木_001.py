"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228668
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
    semantic_id="smth_v1.0.0_壬子癸丑桑柘木_专位偏库之木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬子癸丑桑柘木专位偏库之木(SemanticEntry):
    """
    - **原文（source_text）**：
  壬子专位之木，癸丑偏库之木，遇死绝则富贵，生旺则贫贱，水多则夭折，金多土盛为佳。五行要论云：壬子幽阴之木，阳弱阴盛，柔而无立，类仁水德，用事，惟对以丙...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬子专位之木，癸丑偏库之木，遇死绝则富贵，生旺则贫贱，水多则夭折，金多土盛为佳。五行要论云：壬子幽阴之木，阳弱阴盛，柔而无立，类仁水德，用事，惟对以丙午水，则为水木冲粹之德，类入神仙异士标格，非常流也。烛神经云：壬子之木，失于优柔，其或扬之，仁而高明。注云：壬子木在水旺之乡，假子中得微阳之气而生，柔脆易折，则自败木也。扬之者，欲得火土之气，益之使敷荣，则仁勇而高明。

- **分字分词释义**：
  - **专位之木**：在专一位置的木。
  - **偏库之木**：在偏库位置的木。
  - **遇死绝则富贵**：遇到死绝反而富贵。
  - **幽阴之木**：幽暗阴冷的木。
  - **阳弱阴盛**：阳气弱而阴气盛。
  - **柔而无立**：柔弱而无法自立。
  - **类仁水德**：类似仁德之水。
  - **水木冲粹**：水木冲和纯粹。
  - **神仙异士标格**：神仙异人的标准格局。
  - **失于优柔**：失误在于过分柔弱。
  - **扬之**：发扬它。
  - **敷荣**：繁荣茂盛。

- **规范化释义（primary_lang_explained）**：
  壬子是专位的木，癸丑是偏库的木，遇到死绝反而富贵，生旺反而贫贱，水多则夭折，金多土盛才好。五行要论说：壬子是幽暗阴冷的木，阳气弱而阴气盛，柔弱而无法自立，类似仁德之水的性质。如果对上丙午水，就成为水木冲和纯粹的德性，类似神仙异人的标准格局，不是寻常人。烛神经说：壬子木，失误在于过分柔弱，如果发扬它，则仁德而高明。注解说：壬子木在水旺之处，借子中微弱的阳气而生，柔脆易折，就是自败之木。发扬它的意思，是希望得到火土之气，帮助它繁荣茂盛，就能仁勇而高明。

- **完整对等诠释（secondary_lang_full）**：
  Renzi is exclusive-position wood, Guichou is partial-storage wood. Encountering dead-extinct then wealth-nobility, born-prosperous then poverty-lowliness. Water abundant then premature-death, Metal abundant Earth prosperous as excellent. Five Elements Essential Discourse says: Renzi is obscure-yin wood, yang-weak yin-prosperous, soft without-standing, resembles benevolence-water virtue. If paired with Bingwu Water, becomes water-wood balanced-pure virtue, resembling immortal-extraordinary-scholar standard-pattern, not ordinary-class. Candle-Spirit Classic says: Renzi Wood, fails at over-gentle, if uplifted, benevolent and elevated-bright. Note says: Renzi Wood at water-prosperous location, borrowing Zi's slight-yang energy generates, soft-brittle easily-broken, thus self-defeated wood. Uplifting it, desires obtaining fire-earth energy, aiding to flourish-prosper, then benevolent-courageous and elevated-bright.

- **核心要点**：
  - 壬子癸丑为桑柘木，专位偏库
  - 遇死绝富贵、生旺贫贱（反常）
  - 水多夭折、金多土盛佳
  - 壬子幽阴木、阳弱阴盛、柔而无立
  - 对丙午水木冲粹、神仙异士格
  - 失于优柔、需火土扬之则仁勇高明

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_241]` `[trigger: 壬子癸丑木性质]` `[factor_trigger: renzi_guichou_obscure_yin_wood AND dead_extinct_wealthy_born_prosperous_poor AND water_wood_balanced_pure_immortal_pattern]` `[role: 主干]` 壬子专位之木，癸丑偏库之木，遇死绝则富贵，生旺则贫贱，水多则夭折，金多土盛为佳。五行要论云：壬子幽阴之木，阳弱阴盛，柔而无立，类仁水德，用事，惟对以丙午水，则为水木冲粹之德，类入神仙异士标格，非常流也。烛神经云：壬子之木，失于优柔，其或扬之，仁而高明。注云：壬子木在水旺之乡，假子中得微阳之气而生，柔脆易折，则自败木也。扬之者，欲得火土之气，益之使敷荣，则仁勇而高明。 → 《三命通会》卷一#壬子癸丑木性质

- **详细解说**：
  此条详论壬子、癸丑（桑柘木）的反常性质。壬子专位木、癸丑偏库木，反常地遇死绝富贵、生旺贫贱（木太柔弱），水多夭折（木漂），金多土盛佳（金土制约）。五行要论指出壬子幽阴木阳弱阴盛，柔而无立，对丙午水则水木冲粹为神仙格。烛神经强调壬子木失于优柔，需火土扬之才能仁勇高明。这是论述柔弱木的反常特性与扶助原理。

- **校勘与字词辨析（双语）**：
  - **中文**："专位"指子为木专位。"幽阴"指阴暗。"冲粹"指冲和纯粹。"扬之"指发扬提升。"敷荣"指繁荣茂盛。
  - **English**: "Exclusive-position" means Zi is wood's exclusive position. "Obscure-yin" means dark and shadowy. "Balanced-pure" means harmonious and pure. "Uplifting" means promoting and elevating. "Flourish-prosper" means thriving and prosperous."""
    normalized_text_zh: str = """"""
    subject: str = "壬子癸丑桑柘木：专位偏库之木"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_壬子癸丑桑柘木_专位偏库之木_001_L1",
    )
    version: str = "1.0.0"
