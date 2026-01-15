"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228150
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
    semantic_id="smth_v1.0.0_剑锋金与钗钏金_001",
    book_id="sanming",
    engine_id="bazi"
)
class 剑锋金与钗钏金(SemanticEntry):
    """
    - **原文（source_text）**：
  壬申癸酉，气盛物极，当施收敛之功，颖脱锋锐之刃。盖申酉金之正位，干值壬癸，金水淬砺，故取象剑锋，而金之功用极矣。至戌亥，则金气藏伏，形体已残，煆炼首饰...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬申癸酉，气盛物极，当施收敛之功，颖脱锋锐之刃。盖申酉金之正位，干值壬癸，金水淬砺，故取象剑锋，而金之功用极矣。至戌亥，则金气藏伏，形体已残，煆炼首饰，已成其状，藏之闺阁，无所施为，而金之功用毕，故曰庚戌辛亥钗钏金。

- **分字分词释义**：
  - **气盛物极**：气盛到极点物质到顶点。
  - **收敛之功**：收敛的功用。
  - **颖脱锋锐之刃**：显露锋利的刀刃。
  - **金之正位**：金的正统位置。
  - **金水淬砺**：金被水淬炼磨砺。
  - **金气藏伏**：金的气藏伏起来。
  - **形体已残**：形体已经残缺。
  - **煆炼首饰**：煅烧炼制首饰。
  - **藏之闺阁**：藏在闺房中。
  - **金之功用毕**：金的功用完毕。

- **规范化释义（primary_lang_explained）**：
  壬申癸酉，气盛到极点物质到顶点，应当发挥收敛的功用，显露锋利的刀刃。因为申酉是金的正统位置，天干遇到壬癸水，金被水淬炼磨砺，所以取象为剑锋，金的功用达到极致了。到了戌亥，金的气藏伏起来，形体已经残缺，煅烧炼制成首饰，已经成为那个样子，藏在闺房中，无所作为，金的功用完结了，所以叫庚戌辛亥钗钏金。

- **完整对等诠释（secondary_lang_full）**：
  Renshen-Guiyou: qi flourishing and substance at peak, should exert restraining function, revealing sharp blade edge. Because Shen-You are Metal's proper positions, Stems encountering Ren-Gui Water, Metal tempered and honed by Water, thus symbolizing sword blade—Metal's function reaching its extreme. Arriving at Xu-Hai, Metal qi conceals and submerges, physical form already deteriorated, forged and refined into jewelry ornaments, already formed into that state, stored in women's chambers, with nothing to accomplish—Metal's function completed. Thus called Gengxu-Xinhai Hairpin-Bracelet Metal.

- **核心要点**：
  - 壬申癸酉：剑锋金（气盛物极，金水淬砺）
  - 庚戌辛亥：钗钏金（金气藏伏，成为首饰）
  - 剑锋金为金的功用极致
  - 钗钏金为金的功用完结

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_178]` `[trigger: 剑锋金与钗钏金]` `[factor_trigger: sword_blade_metal AND hairpin_bracelet_metal AND nayin_metal_cycle]` `[role: 主干]` 壬申癸酉，气盛物极，颖脱锋锐之刃。申酉金之正位，金水淬砺，故取象剑锋，金之功用极矣。至戌亥，则金气藏伏，煘炼首饰，金之功用毕，故曰庚戌辛亥钗钏金。 → 《三命通会》卷一#剑锋金与钗钏金

- **详细解说**：
  此条完成金纳音的解释。壬申癸酉为"剑锋金"：申酉是金的正位（西方属金），天干壬癸属水，金在水中淬炼就像打造宝剑，锋利无比，这是金功用的顶峰。庚戌辛亥为"钗钏金"：戌亥属土水之地，金气藏伏，已被煅炼成首饰（钗是发簪，钏是手镯），虽然精美但藏在闺阁中，不再有实际功用，金的生命周期至此完结。六种金纳音完整展现了金的一生：海中金（孕育）→金泊金（初显）→白镴金（在矿）→沙中金（成物）→剑锋金（极盛）→钗钏金（完结）。命理上，剑锋金最强，钗钏金虽美但力弱。

- **校勘与字词辨析（双语）**：
  - **中文**："剑锋金"因申酉金旺，壬癸水淬，如宝剑锋利。"钗钏金"，钗为发簪，钏为手镯，指金制首饰。"颖脱"指显露出来。"金之功用极矣"指金的作用达到极致。"无所施为"指没有用武之地。
  - **English**: "Sword-Blade Metal" because Shen-You Metal prosperous, Ren-Gui Water tempering, like sharp sword. "Hairpin-Bracelet Metal"—hairpin for hair, bracelet for wrist, refers to gold jewelry. "Ying tuo" means revealed. "Metal's function at extreme" means Metal's utility reaches peak. "Nothing to accomplish" means no place to exert strength."""
    normalized_text_zh: str = """"""
    subject: str = "剑锋金与钗钏金"
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
        l1_anchor="smth_v1.0.0_剑锋金与钗钏金_001_L1",
    )
    version: str = "1.0.0"
