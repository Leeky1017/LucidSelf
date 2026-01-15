"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559117
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
    semantic_id="yhzp_v1.0.0_六亲总篇_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 六亲总篇(SemanticEntry):
    """
    - **原文（source_text）**：  
  夫六亲者：父、母、兄弟、妻财、子、孙是也。用日干为主：正印正母；偏印偏母及祖父也；偏财是父，乃母之夫星也，亦为偏妻；正财为妻；偏财为妾，为父是也；...
    """
    
    original_text: str = """- **原文（source_text）**：  
  夫六亲者：父、母、兄弟、妻财、子、孙是也。用日干为主：正印正母；偏印偏母及祖父也；偏财是父，乃母之夫星也，亦为偏妻；正财为妻；偏财为妾，为父是也；比肩为兄弟姐妹也；七杀是男；正官是女；食神是男孙；伤官是女孙及祖母也。妇人命取六亲，与男命不同：取官星为夫星；七杀是偏夫；食神是男；伤官是女。经云：'男取克干为嗣，女取干生为子息及奴婢也。'年为祖上，月为父母伯叔兄弟门户，日为妻妾己身。

- **分字分词释义**：
  - **六亲**：父母兄弟妻财子孙六种亲属关系。
  - **日干为主**：以日干（日元）为核心参照判断六亲。
  - **正印正母**：正印代表生母（阴阳相异生我者）。
  - **偏印偏母**：偏印代表继母或祖父。
  - **偏财是父**：偏财代表父亲（母亲之夫星）。
  - **正财为妻**：正财代表正妻。
  - **比肩兄弟姐妹**：比劫代表兄弟姐妹。
  - **七杀是男/正官是女**：男命以官杀为子女——杀为子，官为女。
  - **食神男孙/伤官女孙**：食伤代表孙辈——食神男孙，伤官女孙。
  - **年祖上/月父母/日妻妾**：四柱各代表不同六亲位置。

- **规范化释义（primary_lang_explained）**：  
  六亲为父母兄弟妻财子孙。用日干为主：正印正母，偏印偏母及祖父；偏财是父亦为母之夫星；正财为妻；偏财为妾；比肩为兄弟姐妹；七杀是男，正官是女；食神是男孙，伤官是女孙及祖母。女命取六亲与男命不同：官星为夫星，七杀是偏夫，食神是男伤官是女。男取克干为嗣，女取干生为子息。年为祖上，月为父母兄弟，日为妻妾己身。

- **完整对等诠释（secondary_lang_full）**：  
  The Six Relatives refer to father, mother, siblings, wife/wealth, children, and grandchildren. Using the Day Stem as the primary reference: Proper Seal represents the proper mother; Indirect Seal represents the stepmother and grandfather; Indirect Wealth is the father, being the mother's Husband Star, and also represents the concubine/secondary wife; Proper Wealth represents the wife; Parallel represents brothers and sisters; Seven Killings represents the son; Proper Officer represents the daughter; Eating God represents the grandson; Injury Officer represents the granddaughter and grandmother. For women's fate, determining Six Relatives differs from men's fate: Officer Star is the Husband Star; Seven Killings is the indirect/secondary husband; Eating God is the son; Injury Officer is the daughter. The classic says: "Men take what the Stem controls as heirs; women take what the Stem generates as children and servants." Year pillar represents ancestors; Month pillar represents parents, uncles, siblings, and family gate; Day pillar represents wife, concubine, and oneself.

- **核心要点**：
  - 六亲为父母兄弟妻财子孙
  - 以日干为主判断六亲
  - 正印正母，偏印偏母及祖父
  - 偏财是父，正财为妻
  - 比肩为兄弟姐妹
  - 男命：七杀是子，正官是女，食神男孙，伤官女孙
  - 女命：官星为夫星，七杀是偏夫，食神是子，伤官是女
  - 年祖上，月父母兄弟，日妻妾己身

- **详细解说**：  
  本条总论六亲的十神对应体系，是八字论六亲的纲领性条文。六亲包括"父、母、兄弟、妻财、子、孙"六种亲属关系。以日干为核心参照：正印（阴阳相异生我者）代表生母；偏印（阴阳相同生我者）代表继母或祖父；偏财（我克且阴阳相同者）是父亲，因为偏财是正印（母亲）的官星（夫）；正财代表正妻；比肩劫财代表兄弟姐妹。子女的取法男女有别：男命"七杀是男，正官是女"——以官杀为子女；女命"食神是男，伤官是女"——以食伤为子女。孙辈以食伤论："食神是男孙，伤官是女孙"。四柱各代表不同六亲位置："年为祖上，月为父母伯叔兄弟门户，日为妻妾己身"。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_154]` `[trigger: 六亲定义]` `[factor_trigger: liuqin_def]` `[role: 主干]` 夫六亲者：父、母、兄弟、妻财、子、孙是也。 → 《渊海子平·六亲总篇》
  - `[ns_yhzp_155]` `[trigger: 正印正母]` `[factor_trigger: shishen_zhengyin AND liuqin_mu AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干依赖]` 用日干为主：正印正母；偏印偏母及祖父也。 → 《渊海子平·六亲总篇》
  - `[ns_yhzp_156]` `[trigger: 偏财是父]` `[factor_trigger: shishen_piancai AND liuqin_fu]` `[role: 主干依赖]` 偏财是父，乃母之夫星也。 → 《渊海子平·六亲总篇》
  - `[ns_yhzp_157]` `[trigger: 正财为妻]` `[factor_trigger: shishen_zhengcai AND liuqin_qi]` `[role: 主干依赖]` 正财为妻；偏财为妾。 → 《渊海子平·六亲总篇》
  - `[ns_yhzp_158]` `[trigger: 官杀子女]` `[factor_trigger: nanming AND shishen_guansha AND liuqin_zinv]` `[role: 条件分支]` 七杀是男；正官是女。 → 《渊海子平·六亲总篇》
  - `[ns_yhzp_159]` `[trigger: 女命六亲]` `[factor_trigger: nvming AND liuqin_config]` `[role: 条件分支]` 妇人命取六亲，与男命不同：取官星为夫星；七杀是偏夫；食神是男；伤官是女。 → 《渊海子平·六亲总篇》
  - `[ns_yhzp_160]` `[trigger: 四柱六亲]` `[factor_trigger: sizhu_weizhi AND liuqin_mapping]` `[role: 总结]` 年为祖上，月为父母伯叔兄弟门户，日为妻妾己身。 → 《渊海子平·六亲总篇》"""
    normalized_text_zh: str = """"""
    subject: str = "六亲总篇"
    factor_refs: list = ['six_relatives', 'seal_as_mother', 'wealth_as_father']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_六亲总篇_001_L1",
    )
    version: str = "1.0.0"
