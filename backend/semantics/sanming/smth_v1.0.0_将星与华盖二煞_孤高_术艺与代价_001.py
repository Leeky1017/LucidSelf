"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264446
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
    semantic_id="smth_v1.0.0_将星与华盖二煞_孤高_术艺与代价_001",
    book_id="sanming",
    engine_id="bazi"
)
class 将星与华盖二煞孤高术艺与代价(SemanticEntry):
    """
    - **原文（source_text）**：  
  论将星华盖二煞皆三合中取，故附于后。将星者，如将札中军也，故以三合中位，谓之将星。华盖者，喻如宝盖。天有此星，其形如盖，常覆乎大帝之座，故以三合底...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论将星华盖二煞皆三合中取，故附于后。将星者，如将札中军也，故以三合中位，谓之将星。华盖者，喻如宝盖。天有此星，其形如盖，常覆乎大帝之座，故以三合底处得库，谓之华盖。洞玄经云：将星处乎中军，华盖张乎库土是也。凡将星常欲吉星相扶，贵煞加临，乃为吉庆。理愚歌云：将星若用亡神临，为国栋梁臣。言吉助之为贵。更夹贵库墓，纯粹而不杂者，出将入相之格也。带华盖正印而不夹库，两府之格也。只带库墓而不带正印，止有华盖，常调之禄也，带华印而不带墓，又不带正印，止有华盖，常调之禄也……凡人命得华盖，多主孤寡，总贵，亦不免孤独，作僧道，艺术论。壶中子云：华盖为术艺星。理愚歌云：华盖虽吉亦有妨，或为㜍子或孤孀。填房入赘多阙口，𬬻钳顶笠披缁黄。

- **规范化释义（primary_lang_explained）**：  
  将星与华盖同取自三合局，但指向的气质不同。将星位居三合中宫，如军中主将，象征统筹调度与实际指挥权；若与吉星、贵人、库墓相夹而纯粹，则有“出将入相”的潜能，多主掌权用兵、敢当重任。华盖则取自三合底处之库，像覆盖天帝的宝盖，象征超然、内向、自成一界的精神空间。命带华盖而又得正印相扶，多主文采清奇、术艺有成，甚至出入两府；但若只见华盖而无正印、无库墓配合，则多为“常调之禄”——有才而不至显赫。古人又多以华盖论孤寡：命有华盖者，往往性情孤高、清冷寡欲，不利婚姻，却宜僧道、术艺、学术等路径。整段文字反复强调：这两颗“煞”并非单纯凶星，而是“高位、高格局、高代价”的组合，需要看与贵人、印绶、库墓等吉神如何搭配，才能判断趋向。

- **完整对等诠释（secondary_lang_full）**：  
  This passage treats General Star (Jiangxing) and Canopy Star (Huagai) as two special configurations derived from the三合局. General Star occupies the central position of a triad, like the commander in the middle of an army, and symbolizes the ability to coordinate, direct and take responsibility. When it is accompanied by benefic stars, noble lords and supportive墓/库 positions, it can mark people who literally "rise as generals and ministers"—those suited to wield military or administrative power. Canopy Star, by contrast, is drawn from the storage branch of a triad and likened to a canopy over the throne: it suggests withdrawal from the crowd, contemplative depth and a life oriented toward study, religion or the arts. Charts with Huagai often signal talent and refinement but also loneliness; individuals may become monks, Daoist adepts or professional craftsmen and artists, sometimes at the cost of conventional family life. The text is careful to note that these stars are not purely lucky or unlucky: without the right support they lead to eccentricity, isolation and missed opportunities, but with proper backing they become signatures of high, if solitary, distinction.


- **校勘与字词辨析（双语）**：
  - **中文**：“术艺星”在古文中包括星命、医卜、书画、工艺等广义技艺，本精校在释义中不局限于占术。
  - **English**: The term "arts" here is broad, covering learned and craft skills alike; Huagai is not only about occult practice but about any field that invites seclusion and specialization.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_jiangxing_huagai_001]` `[trigger: 将星如将]` `[factor_trigger: jiangxing_rujun AND sanhe_zhongwei]` `[role: 主干]` 将星者，如将札中军也，故以三合中位，谓之将星。 → 《三命通会》卷十#将星与华盖
  - `[ns_smth_10_jiangxing_huagai_002]` `[trigger: 华盖如盖]` `[factor_trigger: huagai_rugai AND sanhe_kucang]` `[role: 主干依赖]` 华盖者，喻如宝盖，常覆乎大帝之座，故以三合底处得库，谓之华盖。 → 《三命通会》卷十#将星与华盖
  - `[ns_smth_10_jiangxing_huagai_003]` `[trigger: 术艺星]` `[factor_trigger: shuyi_xing AND gugu_gudao]` `[role: 条件分支]` 壶中子云：华盖为术艺星。凡人命得华盖，多主孤寡。 → 《三命通会》卷十#将星与华盖
  - `[ns_smth_10_jiangxing_huagai_004]` `[trigger: 出将入相]` `[factor_trigger: chujiang_ruxiang AND guisha_jiadian]` `[role: 总结]` 更夹贵库墓，纯粹而不杂者，出将入相之格也。 → 《三命通会》卷十#将星与华盖"""
    normalized_text_zh: str = """"""
    subject: str = "将星与华盖二煞：孤高、术艺与代价"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_将星与华盖二煞_孤高_术艺与代价_001_L1",
    )
    version: str = "1.0.0"
