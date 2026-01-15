"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436414
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
    semantic_id="smth_v1.0.0_清格与财官印绶之洁净_001",
    book_id="sanming",
    engine_id="bazi"
)
class 清格与财官印绶之洁净(SemanticEntry):
    """
    - 原文（source_text）：

  清者洁净之称.女命或一官一煞，不相混杂，谓之清.要夫星得时，柱有财生官，有印助身，无一点混浊之气，方为清贵.如已未、壬申、乙未、甲申，乙以庚为夫，庚禄到申；...
    """
    
    original_text: str = """- 原文（source_text）：

  清者洁净之称.女命或一官一煞，不相混杂，谓之清.要夫星得时，柱有财生官，有印助身，无一点混浊之气，方为清贵.如已未、壬申、乙未、甲申，乙以庚为夫，庚禄到申；以丁为子，丁旺于未；以壬为印，壬生于申.又坐下支神为乙木之财，财旺则能生官，四柱无刑冲破败.经云：财官印绶三般物，女命逢之必旺夫.故为夫人之命.

- 分字分词释义：

  - **清者洁净之称**：清，指结构不杂乱、组合有条理.
  - **一官一煞，不相混杂**：女命中官、煞位置分明，各守其位，不互相争合、混乱.
  - **财生官、印助身**：财星能生官星，印星能资日主，是经典的财官印配合模式.
  - **无刑冲破败**：四柱之间少刑冲穿破，使得格局清爽而不受损.

- **规范化释义（primary_lang_explained）**：

  “清格”是在“纯、和”基础上，再加上财官印三者搭配得宜、结构井然：

  - 官、煞各守其位，不互相混乱；
  - 财星向官星流，印星护身，使得日主既能旺夫、亦能自立；
  - 四柱少刑冲破败，整体呈现一种“干干净净”的格局.

  原例己未、壬申、乙未、甲申：乙木以庚金为夫，庚禄在申；以丁火为子，丁旺于未；以壬水为印，壬生申金.乙木下坐之支又为财，财旺生官，且无冲破，因此被视为“清贵”之象.

 - **完整对等诠释（secondary_lang_full）**：

   The "Clear" pattern describes not only a single, well-defined spouse axis, but also a tidy circulation of resources and protection around it. Officer and, where present, Seven Killings each keep to their own place without overlapping or competing; Wealth naturally flows toward the Officer, and Seal supports the Day Master from behind. With few clashes or destructive combinations, the overall feeling is that the chart is "clean": relationships are structured, obligations are clear, and help arrives through regular, visible channels rather than through chaotic twists of fate.

   In the example, Yi Wood Day Master takes Geng Metal as the spouse star, and Geng sits in its Lu at Shen, signifying a partner with solid standing. Ding Fire acts as the child star and is strong in Wei, giving the child line warmth and vitality. Ren Water serves as Seal, being born in Shen as well, so that understanding, learning, and inner support gather around both self and spouse. The branch beneath Yi also functions as Wealth, which in turn feeds Geng the Officer. With no serious clashes or breakages among the Four Pillars, this becomes a textbook case of "Wealth generates Officer, Seal supports self" wrapped in a clean structure.

   From a modern perspective, a Clear pattern often corresponds to a life in which family roles, financial flows, and expectations are relatively straightforward. The native is able to support her spouse without losing her own education, taste, or integrity; the home functions in an orderly way; and social perception tends toward "refined, self-possessed, and reliable" rather than dramatic or scandalous.

- 核心要点：

  - 官煞分明、财官印配合得宜，是“清格”的核心.
  - 少刑冲、少破败，使得福力能持续运行，而不易被中途折断.
  - 对女命而言，多主旺夫而不失自身气质与品位.

- 详细解说：

  1. **财官印三者的协同**  
     - 财生官，使伴侣与婚姻有现实支撑；  
     - 印助身，使本人有理解、承载与调和的能力；  
     - 三者若各得其所，就形成“内外兼修”的配置.

  2. **清与浊的分界**  
     - 清：官煞不混、刑冲不重、财印不滥；  
     - 浊：官煞杂乱、刑冲横生、财印失衡.两者更多指结构与能量流向的不同，而非道德评判.

  3. **现实层面的表现**  
     - 常见为性情自持、礼数得体、能照顾家庭与自身成长的命主；  
     - 在婚姻中，既能成就伴侣，也能保持一定的独立感与判断力.

- 校勘与字词辨析：

  - “财官印绶三般物，女命逢之必旺夫”一句，本稿理解为结构上的助力，而非简单鼓励以旺夫为唯一价值.
  - “夫人之命”在古代指高阶命妇，本稿在白话中以“位置较高、能旺夫自立”概括之.
  - **English**：
    - Spirit-star (shensha) terms demystified; fortune cycle descriptions treated as developmental tendencies.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_017]` `[trigger: 清格定义]` `[factor_trigger: qing_ge_jiejing]` `[role: 主干]` 清者洁净之称。 → 《三命通会》卷七#清格
  - `[ns_smth_07_018]` `[trigger: 官煞不混]` `[factor_trigger: yi_guan_yi_sha AND bu_xiang_hunza]` `[role: 主干依赖]` 女命或一官一煞，不相混杂，谓之清。 → 《三命通会》卷七#清格
  - `[ns_smth_07_019]` `[trigger: 财生官印助身]` `[factor_trigger: cai_sheng_guan AND yin_zhu_shen]` `[role: 条件分支]` 要夫星得时，柱有财生官，有印助身，无一点混浊之气，方为清贵。 → 《三命通会》卷七#清格
  - `[ns_smth_07_020]` `[trigger: 三般物旺夫]` `[factor_trigger: cai_guan_yin_sanbanwu]` `[role: 总结]` 财官印绶三般物，女命逢之必旺夫。 → 《三命通会》卷七#清格"""
    normalized_text_zh: str = """"""
    subject: str = "清格与财官印绶之洁净"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_92', 'bazi_semantic', 'bazi_structure_factor_93', 'bazi_semantic', 'bazi_state_unnamed_3', 'bazi_semantic', 'bazi_degree', 'bazi_semantic', 'source_ref', 'rel_smth_07_010', 'guansha_fenming', 'rel_smth_07_011', 'caiguanyin_xietong', 'rel_smth_07_012', 'jiegou_qingzhuo', 'evi_smth_07_010', 'guansha_fenming', 'rule_qingge', 'evi_smth_07_011', 'caiguanyin_xietong', 'rule_sanbawu', 'evi_smth_07_012', 'jiegou_qingzhuo', 'rule_qinggui', 'map_smth_07_007', 'map_smth_07_008']
    
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
        l1_anchor="smth_v1.0.0_清格与财官印绶之洁净_001_L1",
    )
    version: str = "1.0.0"
