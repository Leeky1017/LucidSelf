"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228264
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
    semantic_id="smth_v1.0.0_易理与纳音_立天地之道与三才五行_001",
    book_id="sanming",
    engine_id="bazi"
)
class 易理与纳音立天地之道与三才五行(SemanticEntry):
    """
    - **原文（source_text）**：
  易曰：立天之道，阴与阳。日，天道也。十日迭运，而阴阳之义明。立地之道，柔与刚。辰，地道也。自子至亥，十二辰更次，而刚柔之义显。单出为声，而己杂比，然后...
    """
    
    original_text: str = """- **原文（source_text）**：
  易曰：立天之道，阴与阳。日，天道也。十日迭运，而阴阳之义明。立地之道，柔与刚。辰，地道也。自子至亥，十二辰更次，而刚柔之义显。单出为声，而己杂比，然后为音。故以日辰错综纳甲，以成五音，以取六象，于是三才备而五行无余蕴矣。

- **分字分词释义**：
  - **立天之道**：建立天的法则。
  - **十日迭运**：十天干轮流运转。
  - **十二辰更次**：十二地支依次更替。
  - **单出为声**：单独发出为声。
  - **杂比为音**：混杂比配成为音。
  - **日辰错综纳甲**：日干地支交错配合纳入甲子。
  - **三才备**：天地人三才齐备。

- **规范化释义（primary_lang_explained）**：
  《易经》说：建立天的法则，是阴与阳。日（天干），是天道。十天干轮流运转，阴阳的意义就明确了。建立地的法则，是柔与刚。辰（地支），是地道。从子到亥，十二地支依次更替，刚柔的意义就显现了。单独发出为声，混杂比配才成为音。所以用日干地支交错配合纳入甲子，来形成五音，来取得六象，于是天地人三才齐备而五行之理没有遗漏了。

- **完整对等诠释（secondary_lang_full）**：

  The Yijing states that Heaven’s Dao is expressed through the polarity of yin and yang, which in calendrical practice is carried by the ten Heavenly Stems as they cycle in turn. Earth’s Dao is expressed through softness and firmness, carried by the twelve Earthly Branches as they follow one another through the year. A single note uttered alone is only a sound; when different notes are combined in patterned relationships, they become music. In the same way, when stems and branches are interwoven and mapped into the sixty Jiazi, their combinations give rise to the Five musical tones and the sixfold symbolic structure later called Nayin. Read this way, the system is not arbitrary numerology but a way of letting Heaven, Earth and Human—the Three Powers—and the Five Elements all be encoded in one coherent framework.

- **核心要点**：
  - 天道：阴阳（十日迭运）
  - 地道：刚柔（十二辰更次）
  - 声音之理：单为声，杂为音
  - 三才五行：日辰错综，无余蕴

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_192]` `[trigger: 易理与纳音]` `[factor_trigger: yijing_dao AND stems_branches AND three_powers_five_elements]` `[role: 主干]` 易曰：立天之道，阴与阳。日，天道也。十日迭运，而阴阳之义明。立地之道，柔与刚。辰，地道也。十二辰更次，而刚柔之义显。故以日辰错综纳甲，以成五音，于是三才备而五行无余蕴矣。 → 《三命通会》卷一#易理与纳音

- **详细解说**：
  此条引《易经》阐明纳音的易理基础。天道以阴阳为本，十天干（日）轮转体现阴阳运行；地道以刚柔为本，十二地支（辰）更替体现刚柔变化。单独的是"声"，混合比配才是"音"（声音学原理），所以用天干地支交错配合（日辰错综）纳入甲子体系，形成五音（宫商角徵羽），取得六象（六十甲子），这样天地人三才齐备，五行之理完全彰显。这是从《易经》的哲学高度来论证纳音体系的合理性，强调其符合天地自然之道。

- **校勘与字词辨析（双语）**：
  - **中文**："立天之道"出自《易经·说卦传》。"日"指天干。"辰"指地支。"单出为声"，单音为声，复音为音，引《礼记》。"纳甲"指将天干地支配入体系。"三才"指天地人。
  - **English**: "Establishing Heaven's Way" from Yi Jing Explaining Trigrams. "Day" refers to Heavenly Stems. "Branch" refers to Earthly Branches. "Single emission is sound"—single tone is sound, compound tone is music, citing Records of Rites. "納甲" means incorporating Stems-Branches into system. "Three Powers" means Heaven-Earth-Human."""
    normalized_text_zh: str = """"""
    subject: str = "易理与纳音：立天地之道与三才五行"
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
        l1_anchor="smth_v1.0.0_易理与纳音_立天地之道与三才五行_001_L1",
    )
    version: str = "1.0.0"
