"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228726
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
    semantic_id="smth_v1.0.0_戊子丙午水火既济_水中火火中水贵格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊子丙午水火既济水中火火中水贵格(SemanticEntry):
    """
    - **原文（source_text）**：
  戊子支干旺于北方，乃水之位，纳音属火，乃水中之火，非神龙不能有之。丙午支干旺于南方，乃火之位，纳音属水，乃火中之水，非天河不能有之。戊子人得丙午，或丙...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊子支干旺于北方，乃水之位，纳音属火，乃水中之火，非神龙不能有之。丙午支干旺于南方，乃火之位，纳音属水，乃火中之水，非天河不能有之。戊子人得丙午，或丙午人得戊子，无不贵。盖火中出水，水中藏火，水火既济，精神运动，必灵异于人矣。李虚中云：丙午天上之水，银汉有之，即十二辰之天后也。得之者，高明豁达，颖异不凡。

- **分字分词释义**：
  - **支干旺于北方**：天干地支的气势都在北方旺盛。
  - **水之位**：属水的方位与气场。
  - **纳音属火/属水**：纳音五行分别属火、属水。
  - **水中之火/火中之水**：在水位之中的火、在火位之中的水。
  - **非神龙不能有之**：只有“神龙”格局才能承载这种火。
  - **非天河不能有之**：只有“天河”之水才能承载这种水。
  - **水火既济**：《易》卦名，比喻水火相济、对立而和。
  - **精神运动**：精神与气机流动灵活。
  - **天后**：天上的尊神，此处喻指特尊之贵神格局。

- **规范化释义（primary_lang_explained）**：
  戊子这个干支，在北方水位上支干都旺，是属水的方位，但它的纳音却属火，所以称为“水中之火”，只有“神龙”一类的格局才能承载这种火。丙午这个干支，在南方火位上支干都旺，是属火的方位，但它的纳音却属水，所以称为“火中之水”，只有“天河”那样的水才能承载这种水。戊子日主遇到丙午，或者丙午日主遇到戊子，没有不主大贵的。因为火中透出水、水中藏着火，形成水火既济的格局，精神与气机都非常灵动，自然比常人更灵异不凡。李虚中说：丙午是天上的水，在银河中才有，是十二辰中的“天后”之象，得此格局的人，高明豁达，颖悟不凡。

- **完整对等诠释（secondary_lang_full）**：
  Wuzi, with stem and branch flourishing in the North, occupies the Water position, yet its Nayin belongs to Fire, thus it is Fire-within-Water, which only Dragon-of-Spirit patterns can possess. Bingwu, with stem and branch flourishing in the South, occupies the Fire position, yet its Nayin belongs to Water, thus it is Water-within-Fire, which only Celestial-River (Milky Way) can possess. When a Wuzi native encounters Bingwu, or a Bingwu native encounters Wuzi, there is without exception nobility. Because from within Fire emerges Water, and within Water is hidden Fire; Water and Fire mutually completed, spirit and qi move dynamically, and the person is necessarily extraordinary and beyond the common run. Li Xuzhong says: Bingwu is water in Heaven, found in the Silver River, being the “Heavenly Empress” among the twelve branches. Those who obtain it are bright and open‑minded, remarkably gifted and outstanding.

- **核心要点**：
  - 戊子为水位而纳音属火，是“水中之火”
  - 丙午为火位而纳音属水，是“火中之水”
  - 戊子与丙午互见，多主大贵，为水火既济格
  - 精神气机灵动异常，性格高明豁达、颖悟不凡

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_248]` `[trigger: 水火既济格局]` `[factor_trigger: wuzi_fire_in_water AND bingwu_water_in_fire AND water_fire_jiji_noble_pattern]` `[role: 主干]` 戊子支干旺于北方，乃水之位，纳音属火，乃水中之火，非神龙不能有之。丙午支干旺于南方，乃火之位，纳音属水，乃火中之水，非天河不能有之。戊子人得丙午，或丙午人得戊子，无不贵。盖火中出水，水中藏火，水火既济，精神运动，必灵异于人矣。李虚中云：丙午天上之水，银汉有之，即十二辰之天后也。得之者，高明豁达，颖异不凡。 → 《三命通会》卷一#水火既济格局

- **详细解说**：
  本条总论戊子、丙午这组“水中火、火中水”的特殊格局。按方位，戊子居北方坎水之地，却纳音属火，故名“水中之火”；丙午居南方离火之地，却纳音属水，故名“火中之水”。水火本为相克之性，这里却互藏互济，成为《易》所说“既济”之象。命局中，若日主为戊子而岁运逢丙午，或日主为丙午而岁运逢戊子，往往有精神敏锐、反应灵动、悟性超常之象，多主贵显、有卓绝之功。李虚中以“天上水”“银汉天后”来形容丙午，说明其既高又清、既贵且明，与一般火水对冲不同，是水火在高层次上的圆融与互济。

- **校勘与字词辨析（双语）**：
  - **中文**：“水中之火”“火中之水”是以纳音与方位相反来立象，并非字面意思；“天后”原指尊位女神，此处为贵格比喻。
  - **English**: “Fire‑within‑Water” and “Water‑within‑Fire” are symbolic, based on conflict between Nayin element and spatial position, not literal physical fire in water; “Heavenly Empress” is a metaphor for an especially noble configuration."""
    normalized_text_zh: str = """"""
    subject: str = "戊子丙午水火既济：水中火火中水贵格"
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
        l1_anchor="smth_v1.0.0_戊子丙午水火既济_水中火火中水贵格_001_L1",
    )
    version: str = "1.0.0"
