"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482410
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
    semantic_id="iod_v1.0.0_source_text_006",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "A portion of the symbolism of the dream is part of the common property of all mankind, and indeed i...
    """
    
    original_text: str = """"A portion of the symbolism of the dream is part of the common property of all mankind, and indeed in an even wider sense: for similar symbols are to be found in legends, myths, folk-lore, popular customs, idioms, proverbs, and jokes, and we find them more complete there than in dreams. The dream makes use of this symbolism in order to give a disguised representation to its latent thoughts."

#### English Paraphrase (Primary Language)

Symbolization is the dream-work mechanism whereby latent thoughts are represented through universal or culturally shared symbols rather than personal associations. Unlike condensation and displacement which are purely individual, symbols carry relatively fixed meanings across individuals and cultures. The dream employs symbolic representation for its most primitive, fundamental, and forbidden content—especially sexual and aggressive wishes. Common symbols include houses/rooms for bodies/genitals, journeys for life/death, stairs for sexual intercourse, weapons for male genitalia, containers for female genitalia. These symbols appear not only in dreams but throughout human cultural expression—myths, folklore, jokes, idioms—suggesting they represent archaic, pre-linguistic modes of thought inherited from humanity's collective past.

#### Complete Chinese Interpretation

在梦的工作诸机制中，**象征化**与凝缩、移置不同，它不只是个体私人的联想游戏，而是调动了整个人类文化共享的一套符号库。弗洛伊德指出，许多梦中形象之所以反复出现，是因为它们在神话、民间故事、宗教仪式、俗语笑话中早已被反复使用，形成了相对稳定的**普遍象征意义**——尤其用来承载最原始、最难以直接承认的性与攻击性愿望。

典型例子包括：房屋与房间象征身体与性器（窗户是眼睛，门是开口，房间是子宫或女性身体）；上下楼梯或穿越桥梁象征性行为；锋利的刀剑、矛枪、手枪象征男性生殖器；箱子、器皿、洞穴、封闭空间象征女性生殖器；旅行与乘船象征生命历程与死亡过渡；水中浮沉、穿过狭道象征分娩过程。这些意象同时存在于梦境与神话宗教图像之中，说明它们并非个体偶然的联想，而是沿着人类极早期的思维模式沉积下来的“集体遗产”。

象征化尤其服务于两大需求：一是为**最禁忌的内容提供伪装**——当性欲与攻击冲动无法以直白形式出现时，借由房子、武器、道路等形象绕道表达，梦者在清醒时往往不会意识到它们的真正指向；二是为**最原始的思维方式保留出口**——无意识倾向于用形象而非抽象概念来处理经验，象征正是这种前语言、前逻辑思维的自然外衣。

不过，弗洛伊德也提醒不能把象征学变成僵硬“解梦字典”：同一符号在不同人、不同语境中依然需要通过个人联想加以验证。所谓“普遍象征”是出发点而不是终点——分析者既要尊重文化中高度重复的象征模式，也要聆听梦者自己如何讲述这些形象在他生命史中的独特意义。

#### Core Points

- **Universal symbols**: Shared across individuals and cultures (houses, journeys, stairs, weapons)
- **Fixed meanings**: More stable than individual associations (sexual and aggressive content primarily)
- **Cultural presence**: Appear in myths, folklore, jokes, idioms, not just dreams
- **Archaic thinking**: Represents primitive, pre-linguistic cognitive mode
- **Primary disguise**: Especially for most forbidden content (sexuality, aggression)

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Symbolization | Universal symbols for taboos | Third major mechanism |
| Universal Symbols | Cross-cultural fixed meanings | House/stairs/weapons |
| Archaic Thinking | Pre-linguistic cognition | Collective heritage |
| Sexual Symbolism | Body parts, acts | Most common content |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Symbolization uses universal symbols (house=body, stairs=intercourse, weapons=phallus). Archaic pre-linguistic thinking. Cultural presence in myths/folklore.
- **中文**: 象征化使用普遍象征(房子=身体,楼梯=性行为,武器=阳具)。古老前语言思维。文化存在于神话/民间故事。

**Narrative Snippets**:
- `[ns_freud_021]` `[trigger: universal_symbols]` `[factor_trigger: dream_symbol AND dream_universal]` `[role: 主干]` A portion of dream symbolism is common property of all mankind—similar symbols found in legends, myths, folk-lore, and jokes. → Source Text
- `[ns_freud_022]` `[trigger: disguised_representation]` `[factor_trigger: dream_symbolism AND dream_disguise]` `[role: 主干依赖]` The dream makes use of this symbolism in order to give a disguised representation to its latent thoughts. → Source Text
- `[ns_freud_023]` `[trigger: symbol_examples]` `[factor_trigger: dream_symbol AND dream_examples]` `[role: 条件分支]` Common symbols: houses for bodies, journeys for life/death, stairs for sexual intercourse, weapons for male genitalia, containers for female. → English Paraphrase
- `[ns_freud_024]` `[trigger: archaic_thinking]` `[factor_trigger: dream_archaic AND dream_collective]` `[role: 总结]` Symbols represent archaic, pre-linguistic modes of thought inherited from humanity's collective past. → English Paraphrase

#### Detailed Explanation

Symbolization differs fundamentally from condensation and displacement. While those mechanisms operate through purely individual associations unique to each dreamer, symbols carry relatively constant meanings across individuals and cultures. This universality distinguishes symbolic representation from other dream-work processes.

**Universal symbols** appear with remarkable consistency. A house frequently represents the human body, with windows as eyes, doors as bodily orifices, facades as the external appearance. Rooms often symbolize women or the womb. Ascending/descending stairs represents sexual intercourse (the rhythmic movement). Sharp weapons (swords, knives, guns) symbolize male genitalia, while containers (boxes, chests, rooms, caves) represent female genitalia. Journeys symbolize death; births are represented by emergence from water.

These symbols are not arbitrary but grounded in analogical resemblances and archaic modes of thought. The similarity is often visual (elongated for phallus, hollow for womb), functional (penetrating for sexual act), or based on linguistic connections (idioms linking sexuality and architectural terms).

Crucially, symbols appear throughout human cultural expression—not just dreams but myths, fairy tales, jokes, slang, poetic metaphors, and religious imagery. This suggests symbolization accesses a collective, archaic layer of human cognition predating individual experience. Symbols may represent humanity's original pre-linguistic thinking—a mode where abstract concepts were necessarily represented through concrete bodily and sensory imagery.

**The dream prefers symbolic representation for its most primitive and tabooed content**—especially sexuality. This is partly because symbols provide ready-made disguise (the dreamer genuinely doesn't recognize the house as body or stairs as intercourse), and partly because the archaic nature of symbols matches the primitive, infantile character of unconscious wishes.

Freud was cautious about over-applying symbolic interpretation. Symbols provide a useful starting point but must be validated through individual associations. A cigar may sometimes be just a cigar. The danger of purely symbolic interpretation is imposing fixed meanings without checking whether they apply to the specific dreamer's personal context.

---"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
    factor_refs: list = []
    
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_source_text_006_L1",
    )
    version: str = "1.0.0"
