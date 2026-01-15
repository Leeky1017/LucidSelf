"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066848
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
    semantic_id="smth_v1.0.0_2_特殊格局精要_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2特殊格局精要(SemanticEntry):
    """
    - **原文（source_text）**：
  庚申时逢戊日，名食神干旺之方；岁月犯甲丙卯寅，此乃遇而不遇。
  月生日干无天财，乃印绶之名。
  日禄归时没官星，号青云得路。
  阳水叠逢辰位，是...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚申时逢戊日，名食神干旺之方；岁月犯甲丙卯寅，此乃遇而不遇。
  月生日干无天财，乃印绶之名。
  日禄归时没官星，号青云得路。
  阳水叠逢辰位，是壬骑龙背之乡。
  阴木独遇子时，为六乙鼠贵之地。
  庚日全逢润下，忌壬癸巳午之方；时遇子申，其福减半。若逢伤官月建，如凶处未必为凶；内有正倒禄飞，忌官星亦嫌羁绊。

- **分字分词释义**：
  - **食神干旺**：戊日见庚申时（庚为戊食神，申为庚禄，食神得禄）。
  - **遇而不遇**：见甲（煞）、丙（枭）、寅（煞/枭长生）、卯（官），则破格。
  - **月生日干**：印绶格。
  - **日禄归时**：时支为日干之禄（如甲见寅时）。没官星：忌见官杀填实。
  - **壬骑龙背**：壬辰日，柱多见辰（辰为龙，又冲戌财库）。
  - **六乙鼠贵**：乙日生子时（子为乙贵人，又子遥巳，巳动丙戊，丙合辛官，戊合癸印）。
  - **庚日润下**：井栏叉格（庚申庚子庚辰全，冲寅午戌官印）。

- **白话原意**：
  戊日生于庚申时，叫“食神干旺之方”（专食合禄格），食神有力。若年月见到甲（煞）、丙（枭）、寅卯（官煞地），则食神受损，叫“遇而不遇”（破格）。
  月令生于日干（如甲生子月），天干无财星坏印，这就是正宗的“印绶格”。
  日主之禄归于时支（如甲见寅时），且柱中没有官星填实，叫“青云得路”（日禄归时格）。
  壬水日主叠见辰字（壬辰日），叫“壬骑龙背”，多辰冲戌中财官。
  乙木日主独遇子时（乙生子时），叫“六乙鼠贵”，子水贵人遥合巳中财官。
  庚日地支全逢申子辰水局（润下），忌见壬癸（透出则泄气过甚？或指忌官煞？）及巳午官煞方。若时支遇子或申（归时？），福气减半（填实？）。若月令是伤官（子月），看似凶，其实未必（井栏叉即伤官局）。内有正冲（冲官）、倒冲（倒冲禄）、飞天禄马等格，都忌讳官星填实或被合绊。

- **核心要点**：
  - **专食合禄**：忌枭煞。
  - **日禄归时**：忌官星。
  - **特殊贵格**：壬骑龙背、六乙鼠贵、井栏叉（皆忌填实）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_063]` `[trigger: 食神干旺]` `[factor_trigger: shishen_ganwang AND wuri_gengshenshi]` `[role: 主干]` 庚申时逢戊日，名食神干旺之方；岁月犯甲丙卯寅，此乃遇而不遇。 → 《三命通会》卷十一#特殊格局精要
  - `[ns_smth_11_064]` `[trigger: 日禄归时]` `[factor_trigger: rilu_guishi AND qingyun_delu]` `[role: 主干依赖]` 日禄归时没官星，号青云得路。 → 《三命通会》卷十一#特殊格局精要
  - `[ns_smth_11_065]` `[trigger: 壬骑龙背]` `[factor_trigger: renqi_longbei AND yangshui_diefeng_chen]` `[role: 条件分支]` 阳水叠逢辰位，是壬骑龙背之乡。 → 《三命通会》卷十一#特殊格局精要
  - `[ns_smth_11_066]` `[trigger: 六乙鼠贵]` `[factor_trigger: liuyi_shugui AND yinmu_duyu_zishi]` `[role: 条件分支]` 阴木独遇子时，为六乙鼠贵之地。 → 《三命通会》卷十一#特殊格局精要"""
    normalized_text_zh: str = """"""
    subject: str = "2 特殊格局精要"
    factor_refs: list = ['engine_id', 'bazi_state_shishen_8', 'bazi_semantic', 'bazi_state_ren', 'bazi_semantic', 'bazi_structure_yi_1', 'bazi_semantic', 'bazi_structure_factor_28', 'bazi_semantic', 'bazi_state_factor_77', 'bazi_semantic', 'bazi_state_factor_346', 'bazi_semantic', 'source_ref', 'rel_smth_11_055', 'core_factor', 'rel_smth_11_056', 'cond_factor', 'rel_smth_11_057', 'risk_factor', 'evi_smth_11_055', 'core_factor', 'rule_name55', 'evi_smth_11_056', 'cond_factor', 'rule_name56', 'evi_smth_11_057', 'risk_factor', 'rule_name57', 'map_smth_11_037', 'map_smth_11_038']
    
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
        l1_anchor="smth_v1.0.0_2_特殊格局精要_001_L1",
    )
    version: str = "1.0.0"
