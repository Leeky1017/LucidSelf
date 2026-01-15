"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042360
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
    semantic_id="smth_v1.0.0_辛金_阴金之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛金阴金之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  辛金继庚之后，为五金之首，八石之元；在天为日月，乃太阴之精，在地为金，金乃山石之矿，谓之阴金。其禄到酉，酉中己土能生辛金，乃阴生阴也，谓之柔金，为太阴...
    """
    
    original_text: str = """- **原文（source_text）**：
  辛金继庚之后，为五金之首，八石之元；在天为日月，乃太阴之精，在地为金，金乃山石之矿，谓之阴金。其禄到酉，酉中己土能生辛金，乃阴生阴也，谓之柔金，为太阴之精。长生于子，子乃坎水之垣，坎中一阳属金，二阴属土，土能生金，子隐母胎，未显其体，得子水荡漾，淘去浮砂，方能出色，此乃水济金辉，色光明莹。至于巳地，巳为炉冶之火，将辛金炼成死器，亦被巳中戊土埋没，其形不能变化，岂能复生？故辛金生于子而死于巳。经云：「土重金埋」，正谓此也。

- **分字分词释义**：
  - **阴金 / 柔金**：偏向饰物、珠宝之类，重在精致与光泽。
  - **水济金辉**：以水洗炼去杂质，使金色鲜明。
  - **土重金埋**：土过重则金被埋没，无以显露。

- **规范化释义（primary_lang_explained）**：
  辛金多象矿藏、珠玉之金，初生时隐于土中，如胎儿在母体，仅在子水长生之地慢慢被水所淘洗而显色。得酉位之禄，则柔金精粹、光辉可见；若火土过盛，在巳地既被锻炼又被埋没，则反丧失变化之机，成为「死器」。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal follows Geng Metal, being first of five metals and origin of eight stones; in heaven as sun-moon being lunar essence, on earth as metal being mountain-stone ore, embodying yin metal. Its official position reaches You where Ji Earth generates Xin Metal being yin-generates-yin, called soft metal as lunar essence. Born in Zi being Kan Water's rampart—Kan's one yang belongs to metal, two yin belong to earth, earth generates metal, child hidden in mother womb not revealing form; obtaining Zi Water washing away floating sand can then shine brilliantly, this being water benefiting metal radiance with bright luster. Reaching Si position as furnace fire, forging Xin Metal into dead tool, also buried by Si's Wu Earth, its form cannot transform—how could longevity extend? Thus Xin Metal born in Zi dies in Si. The classic "heavy earth buries metal" refers precisely to this."""
    normalized_text_zh: str = """"""
    subject: str = "辛金：阴金之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_xin_presence', 'bazi_calculator', 'dizhi_zi_you_si_set', 'bazi_calculator', 'jin_reform_profile', 'bazi_semantic', 'jin_cut_vs_polish_axis', 'bazi_semantic', 'metal_water_earth_balance', 'bazi_calculator', 'season_alignment_score', 'bazi_calculator', 'geng_xin_yun_flag', 'bazi_calculator', 'earth_buries_metal_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_036', 'tiangan_xin_presence', 'rel_smth_02_037', 'water_dominance_score', 'rel_smth_02_038', 'earth_buries_metal_risk', 'evi_smth_02_032', 'water_dominance_score', 'rule_water_polish_xin', 'evi_smth_02_033', 'earth_buries_metal_risk', 'rule_xin_earth_bury', 'evi_smth_02_034', 'tiangan_ji_presence', 'rule_ji_generate_xin', 'map_smth_02_025', 'map_smth_02_026']
    
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
        l1_anchor="smth_v1.0.0_辛金_阴金之生死与象_001_L1",
    )
    version: str = "1.0.0"
