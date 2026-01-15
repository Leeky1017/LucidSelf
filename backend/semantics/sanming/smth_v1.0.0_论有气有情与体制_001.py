"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264272
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
    semantic_id="smth_v1.0.0_论有气有情与体制_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论有气有情与体制(SemanticEntry):
    """
    - 原文（source_text）：
  有气者急，有情者切。有气乃当时也，看八字内外明暗干支，如六月中气大暑节，土金旺相有气之类，此为至急，余则否。有情乃合气也，如甲见己、丙见辛、丁见壬之类，中间干...
    """
    
    original_text: str = """- 原文（source_text）：
  有气者急，有情者切。有气乃当时也，看八字内外明暗干支，如六月中气大暑节，土金旺相有气之类，此为至急，余则否。有情乃合气也，如甲见己、丙见辛、丁见壬之类，中间干支明暗有合，皆取此为最切也。一说非特合气有情，吉神生我克我，亦为有情；虚拱贵气，生我克我，刑我合我，亦无异也。
  体制须广大。凡八字要看气象规模，体势豁达，天地相停，雄健壮实。五气顺克而有力，倒生逆化而有功，贵气往来不杂，必非寻常格调。

- 分字分词释义：
  - **有气**：得月令旺气。
  - **有情**：干支相合，或生克得宜。
  - **体制广大**：气象宏大，格局纯正有力。

- **规范化释义（primary_lang_explained）**：
  五行得令有气，作用最快（急）；干支有情（相合或相生），关系最密切（切）。如生于大暑后，土金旺相，影响力最大。天干五合、地支六合，或吉神生我、克我（官煞），都是有情的表现。
  八字的格局体制要宏大。气象开阔，天地配合得当，五行生克有力，贵气纯正不杂，这才是大富大贵的格局。如果气象狭小、偏枯、混杂，则难成大器。

- 核心要点：
  - **得时得地**：有气为急。
  - **合化生克**：有情为切。
  - **格局气象**：体制广大者贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_061]` `[trigger: 有气者急]` `[factor_trigger: youqi_zheji AND dangshi_wangxiang]` `[role: 主干]` 有气者急，有情者切。有气乃当时也。 → 《三命通会》卷十#论有气有情与体制
  - `[ns_smth_10_062]` `[trigger: 有情者切]` `[factor_trigger: youqing_zheqie AND heqi_xianghe]` `[role: 主干依赖]` 有情乃合气也，如甲见己、丙见辛、丁见壬之类。 → 《三命通会》卷十#论有气有情与体制
  - `[ns_smth_10_063]` `[trigger: 体制广大]` `[factor_trigger: tizhi_guangda AND qixiang_guimo]` `[role: 条件分支]` 体制须广大。凡八字要看气象规模，体势豁达，天地相停，雄健壮实。 → 《三命通会》卷十#论有气有情与体制
  - `[ns_smth_10_064]` `[trigger: 必非寻常]` `[factor_trigger: bifei_xunchang AND wuqi_shunke]` `[role: 总结]` 五气顺克而有力，倒生逆化而有功，贵气往来不杂，必非寻常格调。 → 《三命通会》卷十#论有气有情与体制"""
    normalized_text_zh: str = """"""
    subject: str = "论有气有情与体制"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_temporal_deling', 'bazi_semantic', 'bazi_relation_factor_107', 'bazi_semantic', 'bazi_structure_geju_2', 'bazi_semantic', 'bazi_state_factor_238', 'bazi_semantic', 'source_ref', 'rel_smth_10_049', 'youqi_youqing', 'rel_smth_10_050', 'youqi_zheji', 'rel_smth_10_051', 'youqing_zheqie', 'evi_smth_10_049', 'tizhi_guangda', 'rule_tizhi_guangda1', 'evi_smth_10_050', 'youqi_zheji', 'rule_youqi_zheji1', 'evi_smth_10_051', 'youqing_zheqie', 'rule_youqing_zheqie1', 'map_smth_10_033', 'map_smth_10_034']
    
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
        l1_anchor="smth_v1.0.0_论有气有情与体制_001_L1",
    )
    version: str = "1.0.0"
