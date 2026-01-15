"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042378
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
    semantic_id="smth_v1.0.0_壬水_阳水之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬水阳水之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  壬水喜阳土而为堤岸之助，畏阴木而为盗气之忧；在天为云，在地为泽，谓之阳水。其禄在亥，亥为池沼存留之水，谓之死水。死水者，刚水也，赖庚金而生，庚禄到申，...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬水喜阳土而为堤岸之助，畏阴木而为盗气之忧；在天为云，在地为泽，谓之阳水。其禄在亥，亥为池沼存留之水，谓之死水。死水者，刚水也，赖庚金而生，庚禄到申，能生壬水，乃五行转养之气。至于卯地，卯乃花叶树木，木旺于卯则能克土，土虚则崩，故堤岸崩颓，而壬水走泄，散漫四野，流而不返，又被阴木盗气，岂得存活？故壬水生于申而死于卯。经云：「死水横流」，正谓此也。

- **分字分词释义**：
  - **阳水 / 刚水**：多象江河湖海之水，力量大、流势强。
  - **喜阳土、畏阴木**：堤岸以阳土为固，阴木太盛则坏堤。
  - **死水横流**：形容水失束缚、泛滥成灾。

- **规范化释义（primary_lang_explained）**：
  壬水如江河大水，喜有高堤厚岸来节制其势，怕阴木过旺破坏土堤。长生于申金，得金生而源远流长；禄在亥池，为蓄水之所；至卯木旺地，木克土、土破堤，壬水失其节制，便四处漫流而难收束，成为「死水横流」。

- **完整对等诠释（secondary_lang_full）**：
  Ren Water delights in yang earth as embankment assistance, fears yin wood as qi-stealing worry; in heaven as clouds, on earth as marshes, embodying yang water. Its official position reaches Hai being pond-swamp retained water, called stagnant water. Stagnant water being hard water relies on Geng Metal for birth; Geng's official position reaches Shen generating Ren Water being five-elements' rotating nourishment qi. Reaching Mao position as flowers-leaves-trees, wood prosperous in Mao can control earth; earth hollow then collapses causing embankment crumbling, Ren Water leaks scattering four fields, flowing without return, also stolen by yin wood qi—how could survival extend? Thus Ren Water born in Shen dies in Mao. The classic "stagnant water flows horizontally" refers precisely to this."""
    normalized_text_zh: str = """"""
    subject: str = "壬水：阳水之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_ren_presence', 'bazi_calculator', 'dizhi_shen_hai_mao_set', 'bazi_calculator', 'shui_role_profile', 'bazi_semantic', 'shui_outer_vs_inner_axis', 'bazi_semantic', 'water_earth_wood_balance', 'bazi_calculator', 'season_alignment_score', 'bazi_calculator', 'ren_gui_winter_window', 'bazi_calculator', 'stagnant_water_floods_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_039', 'tiangan_ren_presence', 'rel_smth_02_040', 'tiangan_geng_presence', 'rel_smth_02_041', 'stagnant_water_floods_risk', 'evi_smth_02_035', 'tiangan_geng_presence', 'rule_geng_generate_ren', 'evi_smth_02_036', 'stagnant_water_floods_risk', 'rule_ren_mao_flood', 'evi_smth_02_037', 'tiangan_wu_presence', 'rule_wu_bank_ren', 'map_smth_02_027', 'map_smth_02_028']
    
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
        l1_anchor="smth_v1.0.0_壬水_阳水之生死与象_001_L1",
    )
    version: str = "1.0.0"
