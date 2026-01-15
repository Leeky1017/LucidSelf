"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227860
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
    semantic_id="smth_v1.0.0_三皇与干支配置的完善_001",
    book_id="sanming",
    engine_id="bazi"
)
class 三皇与干支配置的完善(SemanticEntry):
    """
    - **原文（source_text）**：
  谓之天皇氏者，取其天开于子之义也。谓之地皇氏者，取其地辟于丑之义也。谓之人皇氏者，取其人生于寅之义也。故干支之名，在天皇时始制。而地皇氏则爰定三辰，道...
    """
    
    original_text: str = """- **原文（source_text）**：
  谓之天皇氏者，取其天开于子之义也。谓之地皇氏者，取其地辟于丑之义也。谓之人皇氏者，取其人生于寅之义也。故干支之名，在天皇时始制。而地皇氏则爰定三辰，道分昼夜，以三十日为一月，而干支始各有所配。人皇氏者，王不虚土，臣不虚贵，政教君臣所自起，饮食男女所自始，始得天地阴阳之气，而有子母之分，于是干支始各有所属焉。

- **分字分词释义**：
  - **天开于子**：天在子时开辟。
  - **地辟于丑**：地在丑时开辟。
  - **人生于寅**：人在寅时诞生。
  - **爰定三辰**：确定日月星三辰。
  - **道分昼夜**：划分白天黑夜。
  - **王不虚土**：君王不虚占土地。
  - **臣不虚贵**：臣子不虚享贵位。
  - **子母之分**：子辈母辈的区分。

- **规范化释义（primary_lang_explained）**：
  称为"天皇氏"，是取天在子时开辟的意义。称为"地皇氏"，是取地在丑时开辟的意义。称为"人皇氏"，是取人在寅时诞生的意义。所以干支名称，在天皇氏时开始创制。到了地皇氏，就确定了日月星三辰，划分了昼夜，以三十天为一个月，干支开始各有配置。到了人皇氏，君王不虚占土地，臣子不虚享贵位，政治教化和君臣关系由此建立，饮食男女之事由此开始，初步获得天地阴阳之气，有了子母之分，于是干支开始各有所属。

- **完整对等诠释（secondary_lang_full）**：
  The Celestial Sovereign is so named because heaven opened at the Zi hour. The Terrestrial Sovereign is so named because earth opened at the Chou hour. The Human Sovereign is so named because humanity was born at the Yin hour. Thus the names of stems and branches were first created during the Celestial Sovereign's time. During the Terrestrial Sovereign's reign, the three celestial bodies (sun, moon, stars) were established, day and night were differentiated, thirty days formed one month, and stems and branches began to have specific pairings. During the Human Sovereign's reign, rulers did not occupy land in vain, ministers did not hold noble positions in vain, political governance and ruler-minister relationships originated, matters of food and marriage began, heaven-earth yin-yang qi were first obtained, parent-child distinctions emerged, and thus stems and branches began to have specific attributions.

- **核心要点**：
  - 三皇分别对应子丑寅三时：天开于子，地辟于丑，人生于寅
  - 天皇氏创制干支名称
  - 地皇氏确定三辰，划分昼夜，配置干支
  - 人皇氏建立政教，明确干支所属关系

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_140]` `[trigger: 三皇配置干支]` `[factor_trigger: three_sovereigns AND ganzhi_attribution]` `[role: 主干]` 谓之天皇氏者，取其天开于子之义也。地皇氏则爰定三辰，而干支始各有所配。人皇氏始得天地阴阳之气，而有子母之分。 → 《三命通会》卷一#三皇与干支配置的完善

- **详细解说**：
  此条详述三皇与干支体系完善的关系。天皇氏对应子时（天开于子），地皇氏对应丑时（地辟于丑），人皇氏对应寅时（人生于寅），体现了天地人三才递次生成的宇宙观。天皇氏首创干支名称，地皇氏确定天文历法（三辰、昼夜、月份），使干支有了具体配置。人皇氏建立人类社会秩序（君臣、政教、饮食男女），获得天地阴阳之气，明确了干支的子母归属关系。这个演进过程体现了从宇宙创生到历法建立，再到社会秩序确立的完整谱系。

- **校勘与字词辨析（双语）**：
  - **中文**："爰"，于是、乃。"三辰"指日月星。"子母之分"指干支之间的生克关系，天干为母，地支为子。
  - **English**: "爰" means "thereupon"; "三辰" (three celestial bodies) refers to sun, moon, and stars; "parent-child distinction" alludes to generation relationships between stems and branches."""
    normalized_text_zh: str = """"""
    subject: str = "三皇与干支配置的完善"
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
        l1_anchor="smth_v1.0.0_三皇与干支配置的完善_001_L1",
    )
    version: str = "1.0.0"
