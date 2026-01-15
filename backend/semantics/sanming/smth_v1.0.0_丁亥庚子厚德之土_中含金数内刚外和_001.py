"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228510
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
    semantic_id="smth_v1.0.0_丁亥庚子厚德之土_中含金数内刚外和_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丁亥庚子厚德之土中含金数内刚外和(SemanticEntry):
    """
    - **原文（source_text）**：
  五行要论云：丁亥、庚子二土，中含金数，内刚外和，禀之者，得有定力，土下济之以水火旺气，能建功立事，敢为威果之行。

- **分字分词释义**：
  -...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行要论云：丁亥、庚子二土，中含金数，内刚外和，禀之者，得有定力，土下济之以水火旺气，能建功立事，敢为威果之行。

- **分字分词释义**：
  - **中含金数**：内含金的数量。
  - **内刚外和**：内在刚强外在和顺。
  - **禀之者**：禀受此命者。
  - **有定力**：有坚定的力量。
  - **济之以水火旺气**：用水火旺气来帮助。
  - **威果之行**：威武果敢的行为。

- **规范化释义（primary_lang_explained）**：
  五行要论说：丁亥土、庚子土这两种土，内含金的数量，内在刚强而外在和顺，禀受此命的人，能有坚定的力量。如果再得到水火旺气的帮助，就能建功立业，敢于做威武果敢的事情。

- **完整对等诠释（secondary_lang_full）**：
  Five Elements Essential Discourse says: Dinghai Earth and Gengzi Earth, these two earths contain Metal numbers within, internally firm externally harmonious. Those receiving this destiny possess steadfast determination. If further aided by Water-Fire prosperous energy, can establish achievements and undertakings, daring to perform mighty-resolute actions.

- **核心要点**：
  - 丁亥土（屋上土）、庚子土（壁上土）合论
  - 中含金数（土中藏金）
  - 内刚外和的性格
  - 得水火旺气则建功立业

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_224]` `[trigger: 丁亥庚子土性质]` `[factor_trigger: dinghai_gengzi_earth AND contain_metal_numbers AND internal_firm_external_harmonious]` `[role: 主干]` 五行要论云：丁亥、庚子二土，中含金数，内刚外和，禀之者，得有定力，土下济之以水火旺气，能建功立事，敢为威果之行。 → 《三命通会》卷一#丁亥庚子土性质

- **详细解说**：
  此条合论丁亥（屋上土）、庚子（壁上土）的特殊性质。这两种土内含金数（丁亥的亥中有壬水生金，庚子的子中有癸水，庚本身为金），因此具有内刚外和的特性。禀受此命的人有坚定的意志力，如果再得水火旺气的配合（水火既济），就能建功立业，敢作敢为。这是论述土中藏金、刚柔并济的命理原理。

- **校勘与字词辨析（双语）**：
  - **中文**："中含金数"指土中含有金的成分。"内刚外和"指性格刚柔并济。"济之"指帮助。"威果"指威武果敢。
  - **English**: "Contain Metal numbers within" means earth contains Metal components. "Internally firm externally harmonious" means character combining strength and gentleness. "Aided by" means helped by. "Mighty-resolute" means powerful and decisive."""
    normalized_text_zh: str = """"""
    subject: str = "丁亥庚子厚德之土：中含金数内刚外和"
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
        l1_anchor="smth_v1.0.0_丁亥庚子厚德之土_中含金数内刚外和_001_L1",
    )
    version: str = "1.0.0"
