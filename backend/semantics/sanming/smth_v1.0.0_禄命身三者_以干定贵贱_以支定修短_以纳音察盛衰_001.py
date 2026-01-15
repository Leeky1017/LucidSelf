"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228274
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
    semantic_id="smth_v1.0.0_禄命身三者_以干定贵贱_以支定修短_以纳音察盛衰_001",
    book_id="sanming",
    engine_id="bazi"
)
class 禄命身三者以干定贵贱以支定修短以纳音察盛衰(SemanticEntry):
    """
    - **原文（source_text）**：
  以干为禄定贵贱，以支为命定修短；以纳音为身察盛衰。人得禄命身俱旺相，三才有气，主快乐长寿；若值死绝休囚，三才无气，必为尘埃困窘之命无疑。

- **分...
    """
    
    original_text: str = """- **原文（source_text）**：
  以干为禄定贵贱，以支为命定修短；以纳音为身察盛衰。人得禄命身俱旺相，三才有气，主快乐长寿；若值死绝休囚，三才无气，必为尘埃困窘之命无疑。

- **分字分词释义**：
  - **以干为禄**：用天干作为禄位。
  - **定贵贱**：确定贵贱高低。
  - **以支为命**：用地支作为命位。
  - **定修短**：确定寿命长短。
  - **以纳音为身**：用纳音作为身体。
  - **察盛衰**：观察盛衰强弱。
  - **俱旺相**：都处于旺盛状态。
  - **三才有气**：天地人三才都有生气。
  - **死绝休囚**：死绝休囚等衰弱状态。

- **规范化释义（primary_lang_explained）**：
  用天干作为禄位来确定贵贱高低，用地支作为命位来确定寿命长短；用纳音作为身体来观察盛衰强弱。人如果得到禄命身都处于旺盛状态，天地人三才都有生气，主快乐长寿；如果遇到死绝休囚等衰弱状态，三才没有生气，必定是尘埃困窘的命无疑。

- **完整对等诠释（secondary_lang_full）**：
  In this view, three different structures are read together when judging a chart. The Heavenly Stem functions as an axis of status and stipend, indicating how high or low a person’s social position can realistically rise. The Earthly Branch functions as an axis of life span, outlining the basic pattern of longevity and vulnerability. The Nayin element functions as an axis of embodiment, describing how full or depleted a person’s life‑force tends to be. When all three are placed in fertile positions and well supported, the three layers of Heaven, Earth and Human are said to be full of vitality and such charts tend toward ease and long years. When all three fall into depleted phases, the three layers lack vitality and life is more likely to feel constrained, overburdened or cut short, unless other strong factors clearly counterbalance the pattern.

- **核心要点**：
  - 天干为禄：定贵贱
  - 地支为命：定修短
  - 纳音为身：察盛衰
  - 三者俱旺：快乐长寿
  - 三者皆衰：困窘短命

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_193]` `[trigger: 禄命身三者]` `[factor_trigger: stems_as_destiny_salary AND branches_as_life AND nayin_as_body]` `[role: 主干]` 以干为禄定贵贱，以支为命定修短；以纳音为身察盛衰。人得禄命身俱旺相，三才有气，主快乐长寿；若值死绝休囚，三才无气，必为尘埃困窘之命无疑。 → 《三命通会》卷一#禄命身三者

- **详细解说**：
  此条阐明命理推断的三大要素：禄、命、身。"禄"看天干，决定一个人的社会地位贵贱；"命"看地支，决定寿命长短；"身"看纳音，观察身体强弱盛衰。这三者如果都处于旺相（生旺之地），天地人三才都有生气，就是快乐长寿的好命；如果都处于死绝休囚（衰弱之地），三才无气，就是贫贱困窘的坏命。这是子平命理中最基本的判断方法，后世发展为"年柱为命、月柱为身、日柱为禄"等更复杂的体系。

- **校勘与字词辨析（双语）**：
  - **中文**："禄"指官禄、俸禄。"命"指生命、寿命。"身"指身体、本体。"旺相"指旺盛状态。"死绝休囚"是五行四种衰弱状态。"三才"指天地人。"尘埃困窘"指贫贱困苦。
  - **English**: "Destiny-Salary" refers to official rank and emolument. "Life" refers to lifespan. "Body" refers to physical body, essence. "Flourishing-thriving" means prosperous state. "Death-extinction-rest-imprisonment" are Four Elements' four weak states. "Three Powers" means Heaven-Earth-Human. "Dusty-困窘" means poor and困苦."""
    normalized_text_zh: str = """"""
    subject: str = "禄命身三者：以干定贵贱、以支定修短、以纳音察盛衰"
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
        l1_anchor="smth_v1.0.0_禄命身三者_以干定贵贱_以支定修短_以纳音察盛衰_001_L1",
    )
    version: str = "1.0.0"
