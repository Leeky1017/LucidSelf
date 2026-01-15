"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042261
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
    semantic_id="smth_v1.0.0_甲木_阳木之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲木阳木之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  甲木乃十干之首，主宰四时，生育万物；在天为雷为龙，在地为梁为栋，谓之阳木。其禄到寅，寅为离上之木，其根已断，其枝已绝，谓之死木。死木者，刚木也，须仗斧...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲木乃十干之首，主宰四时，生育万物；在天为雷为龙，在地为梁为栋，谓之阳木。其禄到寅，寅为离上之木，其根已断，其枝已绝，谓之死木。死木者，刚木也，须仗斧斤斫削，方成其器。长生于亥，亥为河潭池沼之水，名曰死水，故死木放死水中，虽浸年久，不能朽坏。若离水至岸而遇癸水，癸水者，活水也，为天地间雨露，日晒雨淋，干湿不调，遂成枯朽，则能生火，火旺而木必焚矣。且午属离火，火赖木生，木为火母，火为木子，子旺母衰，焉有不终之理？故甲木死于午。经云：「木不南奔」，正谓此也。

- **分字分词释义**：
  - **阳木**：具开创、直上、承梁之象，偏重「刚木」的一面。
  - **长生于亥，禄到寅，死于午**：以亥水为根，寅为成材之地，午火为气尽之处，构成甲木一生一死的轨迹。
  - **死水 / 活水**：死水指静止之水，可固木而不朽；活水指流动雨露，易致木朽生火。

- **规范化释义（primary_lang_explained）**：
  甲木为十干之首，象征栋梁之材：在天为雷、为龙之动势，在地为屋梁、栋木之承载。其长生在亥水，如木根潜藏水底渐积生机；到寅为禄地，树干挺立成材，却也已「根断枝绝」，进入刚木阶段，宜斫削成器；若再南奔至午火，反因资生之过而致焚，成为「子旺母衰」——火盛而木亡。死水可以固木，使之久而不腐；活水则因干湿不调而促使木朽，终至生火自焚。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood stands as the first of Ten Stems, symbolizing pillar-beam material: in heaven manifesting as thunder and dragon's dynamic force, on earth as roof beam and structural pillar. It finds longevity in Hai water, like roots gathering vitality beneath still waters; reaches official position (Lu) at Yin where the trunk stands mature yet "roots severed branches ended," entering the hardwood phase suitable for cutting and shaping; if continuing south to Wu fire, it suffers from over-resourcing and burns, becoming "child prosperous mother weakened"—fire thriving while wood perishes. Dead water (still water) preserves wood preventing decay; living water (flowing rain-dew) causes wood rot through imbalanced drying-wetting, eventually generating fire leading to self-immolation. This traces the life-death trajectory of Jia Wood from Hai roots through Yin maturation to Wu combustion."""
    normalized_text_zh: str = """"""
    subject: str = "甲木：阳木之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_jia_presence', 'bazi_calculator', 'dizhi_hai_yin_wu_set', 'bazi_calculator', 'jia_root_strength', 'bazi_calculator', 'mu_vitality_vs_control', 'bazi_semantic', 'wood_fire_dominance', 'bazi_calculator', 'spring_season_window', 'bazi_calculator', 'mu_quality_loss_flag', 'bazi_semantic', 'over_resource_drain_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_015', 'tiangan_jia_presence', 'rel_smth_02_016', 'wood_fire_dominance', 'rel_smth_02_017', 'jia_root_strength', 'evi_smth_02_011', 'jia_root_strength', 'rule_jia_hai_root', 'evi_smth_02_012', 'over_resource_drain_risk', 'rule_jia_wu_burn', 'evi_smth_02_013', 'wood_fire_dominance', 'rule_wood_avoid_south', 'map_smth_02_011', 'map_smth_02_012']
    
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
        l1_anchor="smth_v1.0.0_甲木_阳木之生死与象_001_L1",
    )
    version: str = "1.0.0"
