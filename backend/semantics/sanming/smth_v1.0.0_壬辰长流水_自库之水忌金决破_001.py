"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228536
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
    semantic_id="smth_v1.0.0_壬辰长流水_自库之水忌金决破_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬辰长流水自库之水忌金决破(SemanticEntry):
    """
    - **原文（source_text）**：
  壬辰自库之水，若池沼水积之地，忌金来决破。若再见壬辰，是谓自刑，别辰无咎，遇多水皆喜，惟畏壬戌、癸亥、丙子之水，生旺太过，汗漫无归。五行要论云：壬辰水...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬辰自库之水，若池沼水积之地，忌金来决破。若再见壬辰，是谓自刑，别辰无咎，遇多水皆喜，惟畏壬戌、癸亥、丙子之水，生旺太过，汗漫无归。五行要论云：壬辰水为正印，含清明润沃之德。禀之者，含容弘大，心识如镜，春夏得之，作大福慧；秋冬得之，类奸诈涛德。

- **分字分词释义**：
  - **自库之水**：入库的水。
  - **池沼水积**：池塘沼泽积水。
  - **金来决破**：金来决堤破坏。
  - **自刑**：自己刑克自己。
  - **汗漫无归**：泛滥无归宿。
  - **清明润沃之德**：清澈明亮滋润丰沃的德性。
  - **含容弘大**：包容宏大。
  - **心识如镜**：心性明澈如镜。

- **规范化释义（primary_lang_explained）**：
  壬辰是自库的水，如同池塘沼泽积水之地，忌讳金来决堤破坏。如果再见壬辰，叫做自刑，见其他辰则无妨，遇到众多水都喜欢，只怕壬戌、癸亥、丙子的水，生旺太过，就会泛滥无归。五行要论说：壬辰水为正印，包含清澈明亮滋润丰沃的德性。禀受此命的人，包容宏大，心性明澈如镜。春夏得之，成就大福慧；秋冬得之，则类似奸诈败德。

- **完整对等诠释（secondary_lang_full）**：
  Renchen is self-storage water, like pond-marsh water-accumulation place, avoids Metal coming to breach-break. If seeing Renchen again, called self-punishment, other Chen harmless, encountering many Waters all favorable, only fears Renxu, Guihai, Bingzi Water—born-prosperous excessive, flooding without destination. Five Elements Essential Discourse says: Renchen Water as proper seal, contains clear-bright moistening-fertile virtue. Those receiving it possess magnanimous tolerance, mind-consciousness like mirror. Spring-summer obtaining it achieves great blessing-wisdom; autumn-winter obtaining it resembles treacherous-corrupt virtue.

- **核心要点**：
  - 壬辰为长流水，自库之水
  - 如池沼积水，忌金决破
  - 再见壬辰为自刑
  - 喜多水，畏特定水过旺
  - 正印之德，春夏福慧、秋冬败德

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_227]` `[trigger: 壬辰水性质]` `[factor_trigger: renchen_self_storage_water AND avoid_metal_breach AND proper_seal]` `[role: 主干]` 壬辰自库之水，若池沼水积之地，忌金来决破。若再见壬辰，是谓自刑，别辰无咎，遇多水皆喜，惟畏壬戌、癸亥、丙子之水，生旺太过，汗漫无归。五行要论云：壬辰水为正印，含清明润沃之德。禀之者，含容弘大，心识如镜，春夏得之，作大福慧；秋冬得之，类奸诈涛德。 → 《三命通会》卷一#壬辰水性质

- **详细解说**：
  此条详论壬辰（长流水）的性质与格局。壬辰是自库的水（辰为水库），如池沼积水，忌金来决破（金泄水气且破库）。再见壬辰为自刑（库库相刑），见其他辰无妨。喜多水相助，但怕壬戌（大海水）、癸亥（大海水）、丙子（涧下水）等水太旺而泛滥。五行要论指出壬辰为正印，清明润沃，春夏得之福慧，秋冬得之则败德。这是论述水库的平衡与季节格局。

- **校勘与字词辨析（双语）**：
  - **中文**："自库"指辰为水库。"决破"指决堤破坏。"汗漫"指泛滥。"正印"为十神之一，主智慧文化。
  - **English**: "Self-storage" means Chen is water repository. "Breach-break" means breaking dike. "Flooding" means overflowing. "Proper seal" is one of Ten Gods, governing wisdom and culture."""
    normalized_text_zh: str = """"""
    subject: str = "壬辰长流水：自库之水忌金决破"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_壬辰长流水_自库之水忌金决破_001_L1",
    )
    version: str = "1.0.0"
