"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412795
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
    semantic_id="smth_v1.0.0_食神与福寿之星_001",
    book_id="sanming",
    engine_id="bazi"
)
class 食神与福寿之星(SemanticEntry):
    """
    - **原文（source_text）**：

  食神者，日干所生顺数第三位，乃甲食丙、乙食丁之例。甲生丙为泄气，丙生戊为甲偏财，偏财是天禄自然之财，不劳己之心力，享见成福禄。甲丙有父子之道，如子旺...
    """
    
    original_text: str = """- **原文（source_text）**：

  食神者，日干所生顺数第三位，乃甲食丙、乙食丁之例。甲生丙为泄气，丙生戊为甲偏财，偏财是天禄自然之财，不劳己之心力，享见成福禄。甲丙有父子之道，如子旺相，生起财禄以奉其父母，岂不安享？又甲见庚为煞，见戊为财，其食神丙火能制伏庚煞，使不得克伤甲木，能生戊财，使为甲木所用。凡命遇财煞之地，食神旺相，煞被食制，不敢为祸，财被食生，充裕不竭，故食神一名寿星，一名爵星，良有以也。此格要日主食神俱生旺，无冲破，主人财厚食丰，福量宽弘，肥体肥大，优游自足，有子息，有寿考。四柱见财食在岁月上，祖父荫业丰隆，在日时，妻男获福，怕母子俱衰绝，两皆无成。故经云：“食神宜食生食旺，不可食衰食绝。”又云：“食神生旺，胜似财官”是也。食神大忌偏印为倒食，主为人有始无终，容貌欹邪，身材琐小，心性局促，多愁无成。假如甲见丙为食，柱中有壬作甲木偏印，克制丙火不能生戊土，不能制庚金，使甲木受制退财，岂不窘乎？《元理赋》云：食神制煞，逢枭不贫则夭。《一行》云：阳日食神暗合官星，阴日食神暗合正印，官印不要明显，但得食神纯粹，主贵而有禄，富而有寿，食神只宜一位，不宜太多，恐窃本元之气。经云：“一木叠逢火位，名为散气之父”是也。食多者宜行印运，食少者不宜，是枭神夺食，故食喜旺禄相助，月令建禄最佳，时禄次之，更逢贵人运，行食神生旺之地，大地福禄。忌身衰枭旺，柱中虽喜见财，亦不宜多，多则不清，不过一富翁而已。食神重见，变为伤官，令人少子，纵有，或带破拗性，又不可入墓，即是伤官入墓，主寿难延。大忌空亡，更有官煞显露，为太医师巫术数九流之士，若食神带合、福星贵人之类，另当别论。

- 分字分词释义：

  - **食神者，日干所生顺数第三位**：以日干顺推第三支为食神，如甲食丙、乙食丁，属我所生而较为柔和的气。
  - **偏财是天禄自然之财，不劳己之心力**：由食神所生的偏财，多属顺势而得的福禄，如父母积累、环境所赐等。
  - **食神制煞**：食神能制七煞，使凶煞不致直接伤身，转为可用之力。
  - **一名寿星，一名爵星**：食神与寿命、福量、饮食之丰以及爵位名分皆有关联，故有此二称。
  - **食神大忌偏印为倒食**：偏印克制食神，称为枭神夺食，使食神之福反转为耗损。

- **规范化释义（primary_lang_explained）**：

  食神，是日主所生而又较温和的那一支力量。它既可以生起偏财，为我带来不劳心力的福禄，又可以制伏七煞，使外界的压力、风险不至于直接伤及自身，因此古人称之为“寿星”“爵星”。

  只要日主与食神都生旺而不受冲破，多主：

  - 生活有口福，衣食不缺；
  - 性情宽和、福量宽弘，身体偏丰硕；
  - 有子息，有寿考，人生节奏相对从容。

  但若食神衰绝，或被偏印夺食，则才华、福禄与健康皆难以保全，容易出现有始无终、心性局促、成事不足等情况。

- 核心要点：

  - 食神格重在**福寿与从容之气**，比财官更带一种“有福可享”的意味。
  - 喜食神与日主俱旺、又能生偏财、制七煞；
  - 忌枭神夺食、食神太多或太少，以及入墓、空亡等破格因素。

- 详细解说：

  从结构上看，食神位于“我所生”的一端，却比伤官柔和：伤官偏于锋利、外放，食神则偏于温润、内敛。二者同属才华与表达的一部分，但方向不同：

  - 食神偏向滋养、产出与享受，如饮食、创作、教学、抚育等；
  - 伤官偏向批评、突破与挑战，如改革、辩难、竞争等。

  当命局以食神为用、且结合偏财与七煞时，往往形成“以柔制刚、以福化煞”的格局：

  - 七煞代表压力与挑战，食神制煞，使之不至失控；
  - 偏财由食神所生，则在创造与付出中自然获得报酬。

  若枭神太重，则类似“过度理性或过度顾虑”而压制了食神的自然流动：人虽聪明，却难以放松享受，健康与情绪也易受影响。此时行印运虽能一时护身，却不宜财星过多，以免进一步消耗本元之气。

- **校勘与字词辨析（双语）**：

  - 原文中对“食多者宜行印运，食少者不宜”的说法，本稿理解为：食神过多时需以印收敛其气，食少则不宜再被印夺。
  - “太医师巫术数九流之士”一语，本稿不作职业贬低，而理解为“若食神受损又遇官煞外露，则才华难以正途发挥，易流于边缘与旁门”。
  - 对“食神只宜一位，不宜太多”一句，本稿在白话中解释为“气宜专而不宜散”，以利现代读者理解。
  - **English**：
    - Adapted for modern reader comprehension.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_173]` `[trigger: 食神定义]` `[factor_trigger: shishen_presence AND shengwo_zhiqi]` `[role: 主干]` 食神者，日干所生顺数第三位，乃甲食丙、乙食丁之例。 → 《三命通会》卷六#论食神
  - `[ns_smth_06_174]` `[trigger: 寿星爵星]` `[factor_trigger: shishen_wang AND fushou_zhixiang]` `[role: 主干依赖]` 故食神一名寿星，一名爵星，良有以也。 → 《三命通会》卷六#论食神
  - `[ns_smth_06_175]` `[trigger: 食神制煚]` `[factor_trigger: shishen_zhisha AND sha_bushang]` `[role: 条件分支]` 食神旺相，煚被食制，不敢为祸。 → 《三命通会》卷六#论食神
  - `[ns_smth_06_176]` `[trigger: 食神生旺]` `[factor_trigger: shishen_shengwang AND shengsi_caiguan]` `[role: 总结]` 食神生旺，胜似财官。 → 《三命通会》卷六#论食神"""
    normalized_text_zh: str = """"""
    subject: str = "食神与福寿之星"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_shangguan_marker', 'bazi_semantic', 'bazi_structure_shangguan_1', 'bazi_semantic', 'bazi_state_degree_32', 'bazi_semantic', 'bazi_state_factor_32', 'bazi_semantic', 'bazi_condition_factor_207', 'bazi_semantic', 'bazi_condition_factor_208', 'bazi_semantic', 'source_ref', 'rel_smth_06_157', 'shishen_ge_presence', 'rel_smth_06_158', 'shishen_qiangdu', 'rel_smth_06_159', 'jianguan_risk', 'evi_smth_06_157', 'shishen_ge_presence', 'rule_shishen', 'evi_smth_06_158', 'shencaiyin_wangdu', 'rule_sanwang', 'evi_smth_06_159', 'caiqi_aowu_risk', 'rule_aowu', 'map_smth_06_105', 'map_smth_06_106']
    
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
        l1_anchor="smth_v1.0.0_食神与福寿之星_001_L1",
    )
    version: str = "1.0.0"
