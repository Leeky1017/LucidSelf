"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227893
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
    semantic_id="smth_v1.0.0_风后释纳音与三命术兴起_001",
    book_id="sanming",
    engine_id="bazi"
)
class 风后释纳音与三命术兴起(SemanticEntry):
    """
    - **原文（source_text）**：
  风后释之，以致其用，而三命行矣。彼术家以皇帝定天干十字属河之图，地支十二，属洛之书，以鬼谷子筭成纳音，束方朔解纳音象，皆不得其源而妄云也。

- **...
    """
    
    original_text: str = """- **原文（source_text）**：
  风后释之，以致其用，而三命行矣。彼术家以皇帝定天干十字属河之图，地支十二，属洛之书，以鬼谷子筭成纳音，束方朔解纳音象，皆不得其源而妄云也。

- **分字分词释义**：
  - **风后**：黄帝臣子，释纳音之用。
  - **致其用**：发挥其作用。
  - **三命**：三命术，命理推算之法。
  - **术家**：方技之士。
  - **鬼谷子**：传说中的纵横家。
  - **东方朔**：汉代方士。
  - **不得其源**：不明白根源。

- **规范化释义（primary_lang_explained）**：
  风后解释纳音，使其发挥作用，三命术从此兴起流行。那些术士说黄帝确定的天干十字属于河图，地支十二属于洛书，又说鬼谷子推算出纳音，东方朔解释纳音象征，这些都是不明白根源而胡乱说的。

- **完整对等诠释（secondary_lang_full）**：
  Fenghou interpreted Nayin to bring its applications to fruition, and the Three Fates method arose. Those practitioners claim that the Yellow Emperor assigned the Ten Stems to Hetu and Twelve Branches to Luoshu, that Guiguzi calculated Nayin, and that Dongfang Shuo interpreted Nayin symbolism—all these fail to grasp the true source and speak falsely.

- **核心要点**：
  - 风后解释纳音，发挥其命理作用
  - 三命术（命理推算）由此兴起
  - 批评术家将纳音归功于鬼谷子、东方朔等
  - 强调正统源流为伏羲、黄帝、大挠

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_144]` `[trigger: 风后释纳音三命兴]` `[factor_trigger: fenghou AND sanming AND nayin]` `[role: 主干]` 风后释之，以致其用，而三命行矣。彼术家以鬼谷子筭成纳音，束方朔解纳音象，皆不得其源而妄云也。 → 《三命通会》卷一#风后释纳音与三命术兴起

- **详细解说**：
  此条说明纳音体系的实用化。黄帝命大挠创制纳音后，由臣子风后进行解释和应用，使其成为可操作的命理工具，三命术（以年月日时三命推算人生吉凶的方法）由此兴起。但作者批评后世术士将纳音源头归于鬼谷子（战国纵横家）或东方朔（汉代方士），认为这是不知真正源流而妄言。作者强调纳音的正统谱系是伏羲、黄帝、大挠、风后这一圣王臣子体系，而非后世术士所为。这体现了作者对命理正统性的坚持。

- **校勘与字词辨析（双语）**：
  - **中文**："风后"为黄帝臣子，传说为《风后奇门》作者。"三命"指年命、月命、日命或年月日三柱推命。"东方朔"误作"束方朔"。
  - **English**: "Fenghou" was a minister of the Yellow Emperor, legendary author of "Fenghou Qimen"; "Three Fates" refers to year-month-day pillar divination; "Dongfang Shuo" (Eastern Direction Shuo) was a Han Dynasty court jester and fangshi."""
    normalized_text_zh: str = """"""
    subject: str = "风后释纳音与三命术兴起"
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
        l1_anchor="smth_v1.0.0_风后释纳音与三命术兴起_001_L1",
    )
    version: str = "1.0.0"
