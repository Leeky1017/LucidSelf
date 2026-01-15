"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228303
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
    semantic_id="smth_v1.0.0_丙寅火性质_炉炭之火喜冬及木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙寅火性质炉炭之火喜冬及木(SemanticEntry):
    """
    - **原文（source_text）**：
  丙寅火、为炉炭，喜冬及木，福星禄刑，平头聋哑。

- **分字分词释义**：
  - **炉炭**：炉中炭火。
  - **喜冬及木**：喜欢冬季和木...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙寅火、为炉炭，喜冬及木，福星禄刑，平头聋哑。

- **分字分词释义**：
  - **炉炭**：炉中炭火。
  - **喜冬及木**：喜欢冬季和木。
  - **禄刑**：禄神和刑煞。
  - **聋哑**：聋哑煞，凶煞名。

- **规范化释义（primary_lang_explained）**：
  丙寅火，是炉中炭火，喜欢冬季和木，有福星、禄神则吉，遇刑煞、平头煞、聋哑煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Bingyin Fire is furnace charcoal fire, favoring winter and Wood, auspicious with Fortune Star and Salary Spirit, inauspicious with Punishment sha, Level-Head sha, and Deaf-Mute sha.

- **核心要点**：
  - 丙寅为炉中火，如炉炭
  - 喜冬季（显其功用）、木（生火）
  - 喜福星、禄神
  - 忌刑煞、平头、聋哑

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_197]` `[trigger: 丙寅火性质]` `[factor_trigger: bingyin_fire_charcoal AND favor_winter_wood AND salary_spirit]` `[role: 主干]` 丙寅火、为炉炭，喜冬及木，福星禄刑，平头聋哑。 → 《三命通会》卷一#丙寅火性质

- **详细解说**：
  此条解释丙寅（炉中火）的性质。丙寅纳音为火，在炉中如炭火燃烧，喜欢冬季（冬天需要火的温暖，最能发挥作用），喜欢木（木生火），遇福星、禄神则吉。但忌刑煞、平头煞、聋哑煞等凶神。炉中火需要适当的燃料和环境才能发挥作用。

- **校勘与字词辨析（双语）**：
  - **中文**："炉炭"指炉中炭火。"禄"为禄神，吉神。"刑"为刑煞，凶煞。"聋哑"为聋哑煞，主聋哑残疾。
  - **English**: "Furnace charcoal" refers to charcoal fire in furnace. "Salary" is Salary Spirit, auspicious. "Punishment" is Punishment sha, inauspicious. "Deaf-Mute" is Deaf-Mute sha, indicating deafness and muteness disabilities."""
    normalized_text_zh: str = """"""
    subject: str = "丙寅火性质：炉炭之火喜冬及木"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_丙寅火性质_炉炭之火喜冬及木_001_L1",
    )
    version: str = "1.0.0"
