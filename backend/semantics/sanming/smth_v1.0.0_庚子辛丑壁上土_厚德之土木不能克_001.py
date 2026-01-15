"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228612
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
    semantic_id="smth_v1.0.0_庚子辛丑壁上土_厚德之土木不能克_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚子辛丑壁上土厚德之土木不能克(SemanticEntry):
    """
    - **原文（source_text）**：
  庚子厚德之土，能克众水，不忌他木，盖木至子无气，若遇壬申之金，谓之明位禄，其贵必矣。辛丑福聚之土，众木不能克，盖丑为金库，丑中有金，见木何伤。玉霄宝鉴...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚子厚德之土，能克众水，不忌他木，盖木至子无气，若遇壬申之金，谓之明位禄，其贵必矣。辛丑福聚之土，众木不能克，盖丑为金库，丑中有金，见木何伤。玉霄宝鉴云：庚子、辛丑，土爱木而恶水，见木为官，见水不相宜。阎东叟云：辛丑、己酉之土，中含金数厚，德性刚和而不同，济以水火旺气，则威名功烈，见为果敢。

- **分字分词释义**：
  - **厚德之土**：德行深厚的土。
  - **能克众水**：能克制众多的水。
  - **明位禄**：明显的禄位。
  - **福聚之土**：福气聚集的土。
  - **金库**：金的库藏。
  - **土爱木而恶水**：土喜爱木而讨厌水。
  - **中含金数**：内含金的成分。
  - **德性刚和**：德性刚强而和顺。
  - **威名功烈**：威名和功业。

- **规范化释义（primary_lang_explained）**：
  庚子是厚德的土，能克制众多的水，不忌讳其他木，因为木到子位无气。如果遇到壬申的金，叫做明位禄，其贵必定。辛丑是福聚的土，众多木不能克制，因为丑为金库，丑中有金，见木有何妨害。玉霄宝鉴说：庚子、辛丑土喜爱木而讨厌水，见木为官星，见水不相宜。阎东叟说：辛丑、己酉的土，内含金数深厚，德性刚强和顺而各不相同，如果用水火旺气来帮助，就有威名功业，显现果敢。

- **完整对等诠释（secondary_lang_full）**：
  Gengzi is thick-virtue earth, can overcome many Waters, not fearing other Woods, since wood reaching Zi without energy. If encountering Renshen Metal, called evident-position salary, its nobility certain. Xinchou is blessing-gathering earth, many Woods cannot overcome, since Chou is metal-repository, within Chou has Metal, seeing Wood what harm. Jade-Sky Treasure-Mirror says: Gengzi, Xinchou earth loves Wood dislikes Water, seeing Wood as official, seeing Water unsuitable. Yan Dongsou says: Xinchou, Jiyou earth, internally contains Metal-numbers abundant, virtue-nature firm-harmonious yet different, aided by Water-Fire prosperous energy, then mighty-fame achievement-glory, manifesting resolute-courageous.

- **核心要点**：
  - 庚子为壁上土，厚德之土
  - 能克众水、木至子无气不忌
  - 遇壬申金明位禄必贵
  - 辛丑福聚之土，丑中藏金众木不克
  - 土爱木恶水、见木为官
  - 中含金数、德性刚和、水火济则威名功烈

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_234]` `[trigger: 庚子辛丑土性质]` `[factor_trigger: gengzi_xinchou_metal_containing_earth AND thick_virtue_blessing_gathering AND water_fire_aid_mighty_fame_achievement]` `[role: 主干]` 庚子厚德之土，能克众水，不忌他木，盖木至子无气，若遇壬申之金，谓之明位禄，其贵必矣。辛丑福聚之土，众木不能克，盖丑为金库，丑中有金，见木何伤。玉霄宝鉴云：庚子、辛丑，土爱木而恶水，见木为官，见水不相宜。阎东叟云：辛丑、己酉之土，中含金数厚，德性刚和而不同，济以水火旺气，则威名功烈，见为果敢。 → 《三命通会》卷一#庚子辛丑土性质

- **详细解说**：
  此条详论庚子、辛丑（壁上土）的性质。庚子厚德之土能克众水，木至子无气故不忌，遇壬申（剑锋金）为明位禄必贵。辛丑福聚之土，丑为金库藏金，故众木不能克。玉霄宝鉴指出二土爱木恶水，见木为官吉。阎东叟强调辛丑（及己酉）土含金数厚，德性刚和，水火济则威名功烈。这是论述土中藏金、刚柔并济的命理原理。

- **校勘与字词辨析（双语）**：
  - **中文**："厚德"指德行深厚。"明位禄"指明显的禄位。"金库"指丑为金之库。"爱木恶水"，土生木为泄，见木为官星，水克土故恶。
  - **English**: "Thick-virtue" means deep virtue. "Evident-position salary" means clear salary position. "Metal-repository" means Chou is metal's storehouse. "Loves Wood dislikes Water"—earth generates wood (draining), wood as official star, water overcomes earth thus disliked."""
    normalized_text_zh: str = """"""
    subject: str = "庚子辛丑壁上土：厚德之土木不能克"
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
        l1_anchor="smth_v1.0.0_庚子辛丑壁上土_厚德之土木不能克_001_L1",
    )
    version: str = "1.0.0"
