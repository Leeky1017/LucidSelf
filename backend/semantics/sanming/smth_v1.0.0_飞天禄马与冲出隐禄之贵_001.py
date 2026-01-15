"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412487
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
    semantic_id="smth_v1.0.0_飞天禄马与冲出隐禄之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 飞天禄马与冲出隐禄之贵(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：若逢伤官月建，如凶处未必为凶，内有倒禄飞冲。忌官星，亦嫌羁绊。此格唯有四日：庚子、壬子、辛亥、癸亥。生十月、十一月，冬水纯阴，柱无财官...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：若逢伤官月建，如凶处未必为凶，内有倒禄飞冲。忌官星，亦嫌羁绊。此格唯有四日：庚子、壬子、辛亥、癸亥。生十月、十一月，冬水纯阴，柱无财官，方用。又须月、时或年与日同支，方能并冲。忌官星显露，禄难飞冲；合神羁绊，不能飞冲。要柱中有一字合住禄马，方不走了贵气。喜伤官、食神及干支本运。假令庚子日，庚以丁火为官，在子月生，是伤官月建，可谓凶处；若子字多，冲出午中丁火，则庚日得官星，未可便以凶论。柱要有未或寅、戌，但得一字合午为妙；若有丑羁绊，子去贪合，不能冲午中之禄，见丁字为官露、丙为煞显、午字填实、戊吞啖，则减分数，岁运同。壬子日，壬以己土为官，要柱中子字多，冲午中己土，则壬日得官星，其喜忌与庚子日同。辛亥日，辛用丙火为官；癸亥日，癸用戊土为官，俱要四柱亥字多，冲出巳中丙、戊，则辛、癸得官星。柱有申或酉、丑，但得一字作合为妙，多则不中；有寅羁绊，则亥贪合，不能冲巳中之禄，见丙、戊、己为官星露，减分数，岁运同。

- 分字分词释义：

  - **飞天禄马**：以冲合之力，将伏藏于对宫或他支的禄马位置“飞出”显现，使日主得官得禄。
  - **伤官月建，如凶处未必为凶**：表面是伤官当令之“凶月”，但若能借冲合飞出禄马，反成贵格。
  - **庚子、壬子、辛亥、癸亥四日**：仅限四个日柱，在冬水纯阴之月（亥子月）方可成格。
  - **柱无财官，方用**：原局不宜另有明透之官星、财星，以免与飞出之官禄相冲杂。
  - **合神羁绊、官星显露则减分**：冲禄之神若被合住或为他物所牵制，官星又提前露出，则飞天之妙大减。

- **规范化释义（primary_lang_explained）**：

  飞天禄马格，是在“伤官月建”的表面凶象中，寻找“冲出隐伏官禄”的机会。庚子、壬子、辛亥、癸亥四日，若生于十月、十一月，水气纯阴，原局不见明露财官，而地支又多见子或亥来成势，便有可能通过子午、亥巳对冲，把午、巳中的官禄之气从暗处冲出，使本来“无官可用”的日主，一举得官得禄。

  关键在于：

  - 冲出之官禄必须原本伏藏、不曾显露；
  - 冲禄之支要有力而不被羁绊；
  - 再配合一二合神，既能收住禄马，又不致把冲力全部抵销。

- 核心要点：

  - 飞天禄马属于**冲出伏禄型高格**，仅限庚子、壬子、辛亥、癸亥四日，且以冬月为正。
  - 要求原局无明露财官，官禄藏于午、巳等处，由多子或多亥来飞冲而出。
  - 喜伤官、食神月建与行运呼应，使“凶处逢生”；忌官星提前明露、合神羁绊过多。

- 详细解说：

  可以把飞天禄马理解为“远程起官”的一类格局：

  1. 日主本身在当令之月并无显眼官星，却在对宫或三合局中暗藏官禄（午中丁己、巳中丙戊等）；
  2. 借助子、亥等强力冲支，将这些伏藏的官禄“冲出”原位，使之飞临干头或成合局；
  3. 若同时有一两支未、寅、戌、申、酉、丑等作合，既能收住飞出的官禄，又不致使冲力全失，就能化“伤官月建”为贵格。

  实务判断时，既要看到“飞天”之妙，也要警惕其风险：一旦冲神被其他刑、合、害牵制，或原局中官煞已然显露，飞出的官禄就会变成争合、混煞之源，贵气大减。行运若再以官煞显露、土火填实午巳为主，则容易从“飞天贵格”滑向“官煞是非”，仅主一时虚名。

- **校勘与字词辨析（双语）**：

  - “倒禄飞冲”与后文“飞天禄马”同属一系，本稿统一理解为通过冲合把伏禄冲出的格局。
  - 文中多处“填实”“羁绊”等术语，本稿在释义中以“冲力被削弱、官禄被固定难飞出”解释，不作额外术语扩展。
  - 古歌数首仅作格局条件与层次高低的补充，本稿择其要点收于白话与核心要点，不逐句硬译。
  - **English**：
    - The term "Inverted-Salary Flying-Clash" belongs to the same series as "Flying-Heaven Salary-Horse"; this edition uniformly understands it as a pattern that clashes out hidden salary through combination.
    - Phrases like "filling solid" and "clashing broken" are extracted into vernacular and key points without line-by-line literal translation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_093]` `[trigger: 飞天禄马定义]` `[factor_trigger: feitian_luma_presence]` `[role: 主干]` 若逢伤官月建，如凶处未必为凶，内有倒禄飞冲。 → 《三命通会》卷六#飞天禄马
  - `[ns_smth_06_094]` `[trigger: 四日限定]` `[factor_trigger: feitian_siri]` `[role: 主干依赖]` 此格唯有四日：庚子、壬子、辛亥、癸亥。生十月、十一月，冬水纯阴，柱无财官，方用。 → 《三命通会》卷六#飞天禄马
  - `[ns_smth_06_095]` `[trigger: 忌官露合绊]` `[factor_trigger: ji_guan_xianlu OR heshen_jiban]` `[role: 条件分支]` 忌官星显露，禄难飞冲；合神羁绊，不能飞冲。 → 《三命通会》卷六#飞天禄马
  - `[ns_smth_06_096]` `[trigger: 合住贵气]` `[factor_trigger: hezhu_luma_guiqi]` `[role: 总结]` 要柱中有一字合住禄马，方不走了贵气。 → 《三命通会》卷六#飞天禄马"""
    normalized_text_zh: str = """"""
    subject: str = "飞天禄马与冲出隐禄之贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_23', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_5', 'bazi_semantic', 'bazi_state_degree_7', 'bazi_semantic', 'bazi_condition_factor_161', 'bazi_semantic', 'bazi_condition_factor_162', 'bazi_semantic', 'source_ref', 'rel_smth_06_070', 'feitian_luma_presence', 'rel_smth_06_071', 'bingchong_lidu_feichi', 'rel_smth_06_072', 'guanxing_xianlu_risk', 'evi_smth_06_070', 'feitian_luma_presence', 'rule_feitian', 'evi_smth_06_071', 'hezhu_luma', 'rule_hezhu', 'evi_smth_06_072', 'heshen_jiban_risk', 'rule_jiban', 'map_smth_06_047', 'map_smth_06_048']
    
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
        l1_anchor="smth_v1.0.0_飞天禄马与冲出隐禄之贵_001_L1",
    )
    version: str = "1.0.0"
