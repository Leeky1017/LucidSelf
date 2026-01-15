"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134340
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
    semantic_id="tis_v1.0.0_symbol_reading__learning_the_l_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class SymbolReadingLearningTheL(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Symbol reading | Art of weaving sign-house-planet meanings | Core skill |
| Phrase-book astrology | Stock interpretations looked up mechanically | What to avoid |
| Language learning | Grasping vocabulary and grammar to form sentences | Proper approach |
| Wholeness | Seeing chart as integrated system, not isolated bits | First law |

**Source Text**:
The birthchart is a remarkable tool. But to use that tool you must learn a lost art. You must become a symbol reader.
Interpretation is not a scientific procedure, not something to be memorized. It is not mechanical. The element of creativity, of inspiration, of intuition, is the vital spark at the core of the system.
The mind is a living creature. If our Mercury hurts, then that imbalance is reflected in one of our signs and houses too. We must learn to grasp the birthchart as a whole, just as a good doctor learns to see the body as an interacting system. That is the first law of interpretation: to see wholeness.
Most astrological texts are like phrase books. They contain stock interpretations of each "bit." Have Saturn in Virgo? Turn to page 39. That kind of phrase-book astrology produces fast results but bad ones. There is no life in them.
Learning the language really is not hard to do. As languages go, astrology is an easy one. There are ten planets, twelve signs, and twelve houses. Only thirty-four words. Grasp them and it is as if you were off to Paris with an A in high school French.

**English Paraphrase (Primary Language)**:
Forrest distinguishes two approaches to interpretation: **phrase-book astrology** (looking up stock meanings) versus **language learning** (grasping vocabulary and grammar to form original sentences).

Phrase-book astrology is fast but produces lifeless, contradictory results. It treats each planetary placement as an isolated "bit" to be looked up separately, then awkwardly combines these disconnected paragraphs. The results have no organic unity and often contradict each other.

True interpretation requires **symbol reading**—the art of weaving together sign, house, and planet messages. This involves creativity, intuition, and the ability to see **wholeness**. Just as a doctor sees the body as an interacting system (a headache may connect to stomach issues, both relieved by a neck massage), the astrologer must see the birthchart as an integrated whole where all parts influence each other.

The good news: astrology's vocabulary is small—only 34 words (10 planets, 12 signs, 12 houses). Learning these words and their grammar is manageable. The challenge is not memorization but synthesis.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 区分了两种解读方法：**短语手册式占星**（查找现成含义）与**语言学习**（掌握词汇和语法以形成原创句子）。

短语手册式占星很快但产生无生命、相互矛盾的结果。它把每个行星配置当作独立的"碎片"分别查找，然后笨拙地组合这些断开的段落。结果缺乏有机统一性，常常自相矛盾。

真正的解读需要**符号阅读**——编织星座、宫位、行星信息的艺术。这涉及创造力、直觉和看到**整体性**的能力。正如医生把身体看作互动系统（头痛可能与胃部问题相连，两者都可通过颈部按摩缓解），占星师必须把命盘看作所有部分相互影响的整合整体。

好消息是：占星词汇量很小——仅34个词（10行星、12星座、12宫位）。学习这些词汇及其语法是可管理的。挑战不在于记忆而在于综合。

**Core Points**:
- Phrase-book astrology = fast but lifeless, contradictory
- Language learning = slower but organic, coherent
- First law of interpretation: see wholeness
- Chart is an interacting system like the body
- Only 34 words to learn; challenge is synthesis

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The Paris/French analogy positions astrology as a learnable language rather than an esoteric mystery. The phrase-book critique targets cookbook-style texts that dominated popular astrology.
- **中文**: 巴黎/法语类比将占星定位为可学习的语言而非神秘学。短语手册批评针对主导流行占星的食谱式文本。

**Narrative Snippets**:
- `[ns_innersky_053]` `[trigger: cookbook_astrology]` `[factor_trigger: astro_interpretation AND astro_criticism AND phrase_book_antipattern]` `[role: 主干]` Phrase-book astrology produces fast results but bad ones—there is no life in them. → Source Text
- `[ns_innersky_054]` `[trigger: learning_astrology]` `[factor_trigger: astro_language AND astro_vocabulary]` `[role: 主干依赖]` Learning the language is not hard; as languages go, astrology is an easy one—only 34 words. → Source Text
- `[ns_innersky_055]` `[trigger: holistic_reading]` `[factor_trigger: wholeness_principle AND symbol_reading_method]` `[role: 条件分支]` We must learn to grasp the birthchart as a whole, just as a doctor sees the body as an interacting system. → Source Text
- `[ns_innersky_056]` `[trigger: creative_interpretation]` `[factor_trigger: astro_interpretation AND astro_intuition]` `[role: 总结]` Interpretation is not mechanical; creativity, inspiration, and intuition are the vital spark at the core. → Source Text
- `[ns_innersky_057]` `[trigger: symbol_reading]` `[factor_trigger: astro_symbol AND astro_art AND basic_vocabulary_size]` `[role: 主干]` To use the birthchart you must learn a lost art—you must become a symbol reader. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "Symbol Reading: Learning the Language vs. Memorizing Phrases"
    factor_refs: list = ['source_ref', 'rel_inner_sky_symbol_001', 'symbol_reading_method', 'evi_inner_sky_symbol_001', 'rule_wholeness_first', 'concept_holistic_interpretation', 'mingli_zhengtixing', 'dream_gestalt']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_symbol_reading__learning_the_l_001_L1",
    )
    version: str = "1.0.0"
