"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228596
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
    semantic_id="smth_v1.0.0_戊戌平地木_土中之木忌重土_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊戌平地木土中之木忌重土(SemanticEntry):
    """
    - **原文（source_text）**：
  戊戌土中之木，忌重见土，若纳音土多，一生屯蹇，金不能克，盖金气至戌而散，遇金乃能致福利，见水多术盛而为贵格。阎东叟云：戊戌之木，孤根独立，和之以水火旺...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊戌土中之木，忌重见土，若纳音土多，一生屯蹇，金不能克，盖金气至戌而散，遇金乃能致福利，见水多术盛而为贵格。阎东叟云：戊戌之木，孤根独立，和之以水火旺气，则有英明秀实之德，入格则文章进达，福禄始终。然乘天将之气，主备历艰险，节操不移，方见晚福。

- **分字分词释义**：
  - **土中之木**：土中的木。
  - **屯蹇**：艰难困顿。
  - **金气至戌而散**：金气到戌位就分散。
  - **术盛**：道术兴盛。
  - **孤根独立**：孤独的根基独自立着。
  - **英明秀实**：英明秀美充实。
  - **备历艰险**：经历各种艰难险阻。
  - **节操不移**：节操不改变。

- **规范化释义（primary_lang_explained）**：
  戊戌是土中的木，忌讳重见土，如果纳音土多，一生艰难困顿。金不能克制它，因为金气到戌位就分散了，遇金反而能带来福利。如果见水多则道术兴盛而成贵格。阎东叟说：戊戌木孤根独立，如果用水火旺气调和，就有英明秀美充实的德性，入格则文章进达，福禄始终。然而乘天将之气，主要经历各种艰难险阻，节操不改变，才能见到晚年的福气。

- **完整对等诠释（secondary_lang_full）**：
  Wuxu is wood-within-earth, avoids repeatedly seeing earth. If Nayin earth abundant, lifetime difficulty-obstruction. Metal cannot overcome, since metal-energy reaching Xu disperses. Encountering Metal actually brings fortune-benefit. Seeing abundant Water, skills-flourishing becoming noble pattern. Yan Dongsou says: Wuxu Wood solitary-root standing-alone, harmonizing with Water-Fire prosperous energy, then has brilliant-bright excellent-substantial virtue. Entering pattern, literary-works advancing-reaching, blessing-salary beginning-end. However riding Heaven-General energy, mainly experiencing-thoroughly hardship-danger, integrity-principle unchanging, then sees late-blessing.

- **核心要点**：
  - 戊戌为平地木，土中之木
  - 忌重土多土则屯蹇
  - 金不克反致福
  - 见水多术盛贵格
  - 孤根独立、水火和则英明秀实
  - 历艰险而节操不移见晚福

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_232]` `[trigger: 戊戌木性质]` `[factor_trigger: wuxu_wood_within_earth AND solitary_root_standing_alone AND experiencing_hardship_late_blessing]` `[role: 主干]` 戊戌土中之木，忌重见土，若纳音土多，一生屯蹇，金不能克，盖金气至戌而散，遇金乃能致福利，见水多术盛而为贵格。阎东叟云：戊戌之木，孤根独立，和之以水火旺气，则有英明秀实之德，入格则文章进达，福禄始终。然乘天将之气，主备历艰险，节操不移，方见晚福。 → 《三命通会》卷一#戊戌木性质

- **详细解说**：
  此条详论戊戌（平地木）的特殊性质。戊戌是土中的木（戌为土，但纳音为木），最忌重见土（土多木被埋），纳音土多则一生屯蹇。金反而不能克（因金气至戌散），遇金能致福。见水多则术盛为贵（水生木）。阎东叟强调戊戌木孤根独立，需水火调和才能英明秀实，入格文章进达。但需经历艰险，节操不移，才能见晚福。这是论述土木关系与历练成才的原理。

- **校勘与字词辨析（双语）**：
  - **中文**："土中之木"指木埋于土中。"屯蹇"指艰难，典出《易经》屯卦、蹇卦。"孤根独立"形容木在土中孤立。"备历"指全都经历。
  - **English**: "Wood-within-earth" means wood buried in earth. "Difficulty-obstruction" means hardship, from I Ching Zhun and Jian hexagrams. "Solitary-root standing-alone" describes wood isolated in earth. "Experiencing-thoroughly" means experiencing all."""
    normalized_text_zh: str = """"""
    subject: str = "戊戌平地木：土中之木忌重土"
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
        l1_anchor="smth_v1.0.0_戊戌平地木_土中之木忌重土_001_L1",
    )
    version: str = "1.0.0"
