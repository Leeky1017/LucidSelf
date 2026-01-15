"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228755
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
    semantic_id="smth_v1.0.0_海中金吉凶宜忌_蛤蚌珠藏空冲成器_001",
    book_id="sanming",
    engine_id="bazi"
)
class 海中金吉凶宜忌蛤蚌珠藏空冲成器(SemanticEntry):
    """
    - **原文（source_text）**：
  甲子、乙丑，海中金。海中金者，宝藏龙宫，珠孕蛟室，出现虽假于空冲，成器无藉乎火力。故东方朔以蛤蚌名之，良有理也。妙选有珠藏渊海格，以甲子见癸亥，是不用...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲子、乙丑，海中金。海中金者，宝藏龙宫，珠孕蛟室，出现虽假于空冲，成器无藉乎火力。故东方朔以蛤蚌名之，良有理也。妙选有珠藏渊海格，以甲子见癸亥，是不用火逢空，有蚌珠照月格，以甲子见巳未，是欲合化互贵。盖以海金无形，非空冲则不能出现，而乙丑金库，非旺火则不能陶铸故也。如甲子见戊寅、庚午，是土生金，乙丑见丙寅、丁卯，是火制金，又天干逢三奇，此等格局，无有不贵。

- **规范化释义（primary_lang_explained）**：
  甲子、乙丑是海中金纳音。海中金，是宝藏在龙宫、珠孕于蛟室的金，出现虽要靠空冲之力，但成器却不需要火力锻炼。所以东方朔用蛤蚌来比喻它，确实有道理。妙选中有"珠藏渊海格"，是甲子见癸亥，不用火而逢空；有"蚌珠照月格"，是甲子见巳未，想要合化互贵。因为海金本无形体，不经空冲就不能出现，而乙丑是金库，不经旺火就不能陶铸成器。如甲子见戊寅、庚午，是土生金；乙丑见丙寅、丁卯，是火制金，又天干逢三奇（乙丙丁或甲戊庚），这些格局没有不贵的。

- **完整对等诠释（secondary_lang_full）**：
  Jiazi and Yichou are Sea-Center Metal Nayin. Sea-Center Metal is treasure stored in Dragon-Palace, pearl gestating in Flood-Dragon chamber; its emergence relies on void-clash, yet its vessel-forming requires no fire-power. Therefore Dongfang Shuo named it clam-shell, truly reasonable. In Wonderful-Selection there is Pearl-Hidden-Deep-Sea pattern: Jiazi meeting Guihai, not using fire yet meeting void. There is Clam-Pearl-Illuminates-Moon pattern: Jiazi meeting Si-Wei, desiring mutual transformation and reciprocal nobility. Because Sea-Metal has no form, without void-clash it cannot emerge; and Yichou is Metal-repository, without vigorous fire it cannot be cast. For example, Jiazi meeting Wuyin or Gengwu is Earth generating Metal; Yichou meeting Bingyin or Dingmao is Fire controlling Metal; moreover heavenly-stems meeting Three-Wonders (Yi-Bing-Ding or Jia-Wu-Geng)—such patterns are without exception noble.

- **核心要点**：
  - 海中金：宝藏龙宫、珠孕蛟室
  - 出现靠空冲、成器不需火
  - 贵格：珠藏渊海（甲子癸亥）、蚌珠照月（甲子巳未）
  - 甲子喜土生、乙丑喜火制加三奇

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_100]` `[trigger: 海中金吉凶]` `[factor_trigger: haizhong_jin AND jiazi_yichou]` `[role: 主干]` 海中金者，宝藏龙宫，珠孕蛟室，出现虽假于空冲，成器无藉乎火力。故东方朔以蛤蚌名之，良有理也。 → 《三命通会》卷一#海中金吉凶宜忌

- **详细解说**：
  本条详论甲子乙丑海中金的性质与吉凶。海中金象征深藏海底的宝珠，需要"空冲"才能出现（如甲子遇癸亥为空），但成器不依赖火力锻造。东方朔以蛤蚌比喻，点出其藏珠之象。贵格包括"珠藏渊海"（甲子癸亥，不用火）和"蚌珠照月"（甲子巳未，合化互贵）。甲子无形需空冲显现，乙丑为金库需火炼成器。具体配置：甲子喜见戊寅庚午（土生金），乙丑喜见丙寅丁卯（火制金），天干再逢三奇（乙丙丁或甲戊庚）则贵。这是纳音相互关系论的开篇，建立了海中金独特的成器逻辑。

- **校勘与字词辨析（双语）**：
  - **中文**："海中金"为六十甲子纳音之首，象征潜藏待显。"空冲"指地支相冲带来的显现力量。"三奇"有多种组合，此处指天干乙丙丁或甲戊庚的特殊配置。
  - **English**: "Sea-Center Metal" is first of sixty Jiazi Nayin, symbolizing hidden-awaiting-manifestation. "Void-clash" means manifestation power from branch-clashing. "Three-Wonders" has multiple combinations, here referring to stems Yi-Bing-Ding or Jia-Wu-Geng special configurations."""
    normalized_text_zh: str = """"""
    subject: str = "海中金吉凶宜忌：蛤蚌珠藏空冲成器"
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
        l1_anchor="smth_v1.0.0_海中金吉凶宜忌_蛤蚌珠藏空冲成器_001_L1",
    )
    version: str = "1.0.0"
