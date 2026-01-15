"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227949
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
    semantic_id="smth_v1.0.0_庚辛金之义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚辛金之义(SemanticEntry):
    """
    - **原文（source_text）**：
  庚辛其位，金行秋之令，庚乃阴干，阳更而续者也。辛乃阳在下，阴在上，阴于阳极于此。庚更故也，而辛，新也。庚、辛皆金，金味辛物戊而后有味。又云：万物肃然更...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚辛其位，金行秋之令，庚乃阴干，阳更而续者也。辛乃阳在下，阴在上，阴于阳极于此。庚更故也，而辛，新也。庚、辛皆金，金味辛物戊而后有味。又云：万物肃然更改，秀实新成。

- **分字分词释义**：
  - **阴干**：此处指阴气开始主导的天干。
  - **阳更而续**：阳气交替继续。
  - **阳在下阴在上**：阳气在下，阴气在上。
  - **阴于阳极于此**：阴气对阳气的消减在此达到极点。
  - **更故**：更新旧物。
  - **金味辛**：金的味道属辛。
  - **物戊而后有味**：事物成熟后才有味道。
  - **肃然更改**：肃杀而更改。
  - **秀实新成**：果实新成。

- **规范化释义（primary_lang_explained）**：
  庚辛的位置属金，主管秋季的时令。庚是阴气开始主导的天干，阳气在此交替继续。辛是阳气在下阴气在上，阴气对阳气的消减在此达到极点。庚就是"更"，更新旧物；辛就是"新"，新生之意。庚辛都属金，金的味道辛辣，事物成熟后才有味道。又说：万物肃杀而更改，果实新鲜成就。

- **完整对等诠释（secondary_lang_full）**：
  Geng and Xin occupy the Metal position, commanding Autumn's decree. Geng represents the Stem where yin qi begins to dominate, with yang qi alternating and continuing. Xin has yang qi below and yin qi above—yin's elimination of yang reaches its extreme here. Geng means "renewal" or "changing the old"; Xin means "new." Both Geng and Xin are Metal; Metal's taste is acrid, and things develop flavor only after maturing. It is also said: myriad things undergo solemn transformation, with fruits freshly ripening.

- **核心要点**：
  - 庚辛属金，主秋季
  - 庚金：阴干阳续，阳气交替
  - 辛金：阳下阴上，阴消阳极
  - 庚为"更"，辛为"新"
  - 金味辛，物成而有味
  - 万物肃然更改，秀实新成

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_152]` `[trigger: 庚辛金之义]` `[factor_trigger: geng_metal AND xin_metal AND element_metal]` `[role: 主干]` 庚辛其位，金行秋之令。庚更故也，而辛，新也。庚辛皆金，金味辛物戊而后有味。万物肃然更改，秀实新成。 → 《三命通会》卷一#庚辛金之义

- **详细解说**：
  此条详解庚辛金之义。庚金为阳金，秋初之时阴气开始主导但阳气仍在交替继续，象征收敛肃杀的开始。辛金为阴金，阳气居下阴气居上，阴对阳的消减达到极点，象征深秋的彻底肃杀。"庚，更也"指更新旧物、收割成熟；"辛，新也"指虽经肃杀但孕育新生。金味辛辣，对应秋季果实成熟后才显出味道。"肃然更改"描绘秋季万物凋零的景象，"秀实新成"则强调果实虽经肃杀而成熟，体现庚辛金从收敛（庚）到极致（辛）的两个阶段。

- **校勘与字词辨析（双语）**：
  - **中文**："阴干"此处非阴天干之意，而指阴气主导的时期。"物戊"的"戊"通"茂"，指成熟。"秀实"指果实。
  - **English**: "阴干" here doesn't mean yin Stem but rather the period when yin qi dominates; "物戊" means maturation; "秀实" refers to fruits or grains."""
    normalized_text_zh: str = """"""
    subject: str = "庚辛金之义"
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
        l1_anchor="smth_v1.0.0_庚辛金之义_001_L1",
    )
    version: str = "1.0.0"
