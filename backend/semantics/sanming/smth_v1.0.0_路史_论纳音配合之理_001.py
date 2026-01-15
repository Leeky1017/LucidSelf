"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227885
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
    semantic_id="smth_v1.0.0_路史_论纳音配合之理_001",
    book_id="sanming",
    engine_id="bazi"
)
class 路史论纳音配合之理(SemanticEntry):
    """
    - **原文（source_text）**：
  路史云：伏羲命潜龙氏筮之，乃迎日推策，相刚建造甲子，以命岁时。配天为干，配地为枝，枝干配类，以纲维乎四象，故情伪相感，而星辰以顺则。至黄帝命大挠探五行...
    """
    
    original_text: str = """- **原文（source_text）**：
  路史云：伏羲命潜龙氏筮之，乃迎日推策，相刚建造甲子，以命岁时。配天为干，配地为枝，枝干配类，以纲维乎四象，故情伪相感，而星辰以顺则。至黄帝命大挠探五行之情，考天书三式，以十干十二支衍而成六十甲子纳音，声而定之为纳音，即甲子、乙丑、海中金之类是也。

- **分字分词释义**：
  - **潜龙氏**：伏羲臣子。
  - **迎日推策**：观日推算筮法。
  - **相刚建**：观察刚柔配置。
  - **纲维乎四象**：统领四象（四时四方）。
  - **情伪相感**：真情与虚伪相互感应。
  - **天书三式**：太乙、六壬、奇门三式。
  - **衍而成**：推演而成。

- **规范化释义（primary_lang_explained）**：
  《路史》说：伏羲命令潜龙氏占筮，迎着太阳推算策数，观察刚柔建立甲子，用来命定岁时。配天的称为干，配地的称为支，干支相配成类，用来统领四象，所以真情与虚伪相互感应，星辰因此顺应规律。到了黄帝时，命大挠探究五行的性情，考察天书三式（太乙、六壬、奇门），用十天干十二地支推演而成六十甲子纳音，通过声音确定，称为纳音，如甲子乙丑海中金之类就是。

- **完整对等诠释（secondary_lang_full）**：
  The "Lushi" (Path History) states: Fuxi commanded Qianlong (Hidden Dragon) to divine, observing the sun and calculating with counting rods, examining hardness and softness to establish Jiazi for determining years and seasons. What matches heaven is called Stems; what matches earth is called Branches. Stems and branches pair by category to govern the Four Symbols, thus genuine and false interact, and celestial bodies follow their proper order. By the time of the Yellow Emperor, he commanded Da Nao to explore the natures of the Five Elements, examine the Three Celestial Arts (Taiyi, Liuren, Qimen), and extend the Ten Stems and Twelve Branches to form the Sixty Jiazi Nayin system. This was determined through tonal qualities and called Nayin, such as Jiazi-Yichou being Haijin (Sea Metal).

- **核心要点**：
  - 引《路史》详述干支纳音起源
  - 伏羲命潜龙氏筮法推算，建造甲子
  - 干配天、支配地，统领四象
  - 黄帝命大挠考察三式，衍成纳音
  - 纳音通过声音（音律）确定五行属性

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_143]` `[trigger: 路史论纳音]` `[factor_trigger: lushi AND nayin AND sanshi]` `[role: 主干]` 路史云：伏羲命潜龙氏筮之，相刚建造甲子。配天为干，配地为枝。至黄帝命大挠考天书三式，以十干十二支衍而成六十甲子纳音。 → 《三命通会》卷一#《路史》论纳音配合之理

- **详细解说**：
  此条引用《路史》详细论述纳音配合的原理。伏羲时代，命潜龙氏通过占筮、观日、推策，观察刚柔阴阳的配置，建立甲子以定岁时。干配天、支配地的设定，使干支体系能够统领四象（四时四方），真情虚伪相感应，星辰顺应规律运行。到黄帝时，大挠在此基础上深入探究五行性情，考察天书三式（太乙、六壬、奇门这三种占卜术），用十干十二支推演出六十甲子配纳音体系。纳音通过音律（声音的五行属性）来确定，如甲子乙丑配海中金。这套体系将天文、五行、音律、占卜融为一体。

- **校勘与字词辨析（双语）**：
  - **中文**：《路史》为南宋罗泌所著史书。"三式"指太乙、六壬、奇门三大占卜术。"声而定之"指通过音律五行确定纳音属性。
  - **English**: "Lushi" is a history by Luo Bi (Southern Song); "Three Celestial Arts" are Taiyi, Liuren, and Qimen divination systems; "determined through tones" refers to assigning Five Elements through musical tones."""
    normalized_text_zh: str = """"""
    subject: str = "《路史》论纳音配合之理"
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
        l1_anchor="smth_v1.0.0_路史_论纳音配合之理_001_L1",
    )
    version: str = "1.0.0"
