"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228002
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
    semantic_id="smth_v1.0.0_申酉戌亥支义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 申酉戌亥支义(SemanticEntry):
    """
    - **原文（source_text）**：
  申者，七月之辰，申阳所为，而己阴至于申，则上下通而人始见。白露叶落，乃其候也，可以述阴事以成之。又云：申，身也，言物体皆成。酉者，日入之时，乃阳正中八...
    """
    
    original_text: str = """- **原文（source_text）**：
  申者，七月之辰，申阳所为，而己阴至于申，则上下通而人始见。白露叶落，乃其候也，可以述阴事以成之。又云：申，身也，言物体皆成。酉者，日入之时，乃阳正中八月也。又云：酉，犹也，万物皆缯缩收敛。九月戌，阳未既也，然不能事，潜藏于戌。戌中乃乾位，戌为天门，故也。又云：戌，灭也，万物皆衰灭矣。十月亥，纯阴也。又亥，劾也，言阴气劾杀万物，此地之道也，故以此名月焉。

- **分字分词释义**：
  - **申阳所为**：阳气所作所为。
  - **上下通**：上下贯通。
  - **白露叶落**：白露时节树叶飘落。
  - **述阴事以成之**：记述阴事而成就。
  - **身**：物体。
  - **日入之时**：太阳落下的时刻。
  - **阳正中**：阳气正中。
  - **缯缩**：收缩。
  - **阳未既**：阳气未尽。
  - **不能事**：不能做事。
  - **乾位**：乾卦位置。
  - **天门**：天之门户。
  - **劾杀**：劾核杀灭。

- **规范化释义（primary_lang_explained）**：
  申是七月的时辰，阳气所作所为到此完成，而阴气到申则上下贯通人开始看见。白露节气树叶飘落，是其征候，可以记述阴事来成就。又说：申就是"身"，指万物的形体都已成就。酉是太阳落下的时刻，是阳气正中的八月。又说：酉就是"犹"，万物都收缩收敛。九月戌，阳气未尽，但不能做事，潜藏于戌中。戌中是乾卦的位置，戌为天门，所以如此。又说：戌就是"灭"，万物都衰败灭亡。十月亥，纯阴之月。又说：亥就是"劾"，指阴气劾核杀灭万物，这是地之道，所以用此命名月份。

- **完整对等诠释（secondary_lang_full）**：
  Shen is the seventh month—what yang qi has accomplished completes here, while yin qi reaching Shen penetrates above and below for people to perceive. White Dew with falling leaves marks its season; yin matters can be recorded and completed. Also said: Shen means "body"—all things' physical forms are completed. You is when the sun sets, the eighth month when yang is centered. Also said: You means "hesitating"—myriad things all contract and converge. In the ninth month Xu, yang is not yet exhausted but cannot function, hiding within Xu. Xu contains the Qian position; Xu is Heaven's Gate. Also said: Xu means "extinguishing"—myriad things all decline and perish. The tenth month Hai is pure yin. Also said: Hai means "investigating"—yin qi investigates and kills myriad things. This is Earth's Way, thus months are named accordingly.

- **核心要点**：
  - 申：七月，阴气上下通，白露叶落，物体皆成
  - 酉：八月日入，万物收缩收敛
  - 戌：九月，阳未既但潜藏，乾位天门，万物衰灭
  - 亥：十月纯阴，阴气劾杀万物

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_159]` `[trigger: 申酉戌亥支义]` `[factor_trigger: shen_branch AND you_branch AND xu_branch AND hai_branch AND autumn_winter]` `[role: 主干]` 申，身也，言物体皆成。酉，犹也，万物皆缯缩收敛。戌，灭也，万物皆衰灭矣。亥，劾也，言阴气劾杀万物。 → 《三命通会》卷一#申酉戌亥支义

- **详细解说**：
  此条详解申酉戌亥四支之义。申对应七月，阳气完成使命，阴气上下贯通显现，白露节气标志秋季深入，万物形体成就。酉对应八月酉时（日落时），阳气虽在正中但已开始收敛，万物收缩。戌对应九月，阳气虽未完全消失但已无力作为，潜藏于戌中，戌为乾卦位、天门位，万物衰败灭亡。亥对应十月，纯阴之月，阴气彻底劾核杀灭万物，回归地道。申酉戌亥四支完成了从阴气显现（申）到收敛（酉）到衰灭（戌）到纯阴（亥）的秋冬转换过程，与子丑形成循环。

- **校勘与字词辨析（双语）**：
  - **中文**："白露"为二十四节气之一，在申月。"天门"指戌位为乾卦，乾为天。"劾"有劾核、审查、杀灭之意。
  - **English**: "White Dew" is one of 24 solar terms occurring in Shen month; "Heaven's Gate" refers to Xu position as Qian trigram (Heaven); "劾" (he) means investigating, examining, or killing."""
    normalized_text_zh: str = """"""
    subject: str = "申酉戌亥支义"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_申酉戌亥支义_001_L1",
    )
    version: str = "1.0.0"
