"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412508
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
    semantic_id="smth_v1.0.0_福星贵人与真食神之福_001",
    book_id="sanming",
    engine_id="bazi"
)
class 福星贵人与真食神之福(SemanticEntry):
    """
    - **原文（source_text）**：

  福星贵人：乃甲人见丙寅、丙子，乙人见丁亥、丁丑，遁得本旬中真食神，主享受自然，遇者非贵亦富，余倒推。前人作《甲丙相邀入虎乡歌》，是以年论，故有丙寅、...
    """
    
    original_text: str = """- **原文（source_text）**：

  福星贵人：乃甲人见丙寅、丙子，乙人见丁亥、丁丑，遁得本旬中真食神，主享受自然，遇者非贵亦富，余倒推。前人作《甲丙相邀入虎乡歌》，是以年论，故有丙寅、丙子；若以日遁，则非。

- 分字分词释义：

  - **福星贵人**：以真食神为核心，象征先天福厚、享受现成之福禄的格局。
  - **甲人见丙寅、丙子，乙人见丁亥、丁丑**：指甲日以丙火为食神，落在寅、子等位；乙日以丁火为食神，落在亥、丑等位，皆为真食得地之象。
  - **遁得本旬中真食神**：在同一旬空中，食神得其本气与本位，不带偏杂与刑冲。
  - **非贵亦富**：不一定一律登第显官，但大多衣食丰足、福厚而安。

- **规范化释义（primary_lang_explained）**：

  福星贵人格，强调的是“真食神得位”的福厚之象。甲日见丙寅、丙子，乙日见丁亥、丁丑，皆是食神落在对其有利之地位，既得生旺之气，又不受偏印、七煞等破坏。这样的人，多半不必过度挣扎，便能享受较好的生活条件与机缘。

  原文同时提醒，古书有以“年干支”而非“日干支”推此格的说法，本节仅取其结构要点，不拘泥于具体歌诀形式。

- 核心要点：

  - 真食神得本气、本位而不受破损，是福星贵人的关键。
  - 重点在“福厚与享受”，未必一律对应极高官阶，却多主生活从容、难见极端困顿。
  - 需防偏印、七煞夹杂，把食神之福转化为倒食之祸。

- 详细解说：

  在五行用神体系中，食神本就与“福寿、口福、闲适”关系密切；当其又落在对自身最有利的地支，如寅木生丙火、亥水生丁火等时，便容易形成“顺着自身天性而获福”的人生轨迹：

  - 人多性情宽厚、待人和气，不喜争竞；
  - 职业路径常带有一定的稳定性与舒适度，如教职、文职、技术性岗位等；
  - 若再有正财、正印相辅，则“有福可享”而又“不致耽于逸乐”。

  但若局中同时偏印过重，或七煞显露，则食神的柔和之福容易被削弱甚至反转，表现为一方面贪图享受，另一方面又多忧多累，此时虽仍可借“福星”之名，但宜谨慎评估整体结构，不可草率定为高贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_101]` `[trigger: 福星贵人]` `[factor_trigger: fuxing_guiren AND zhen_shishen]` `[role: 主干]` 福星贵人者，甲人见丙寅、丙子，乙人见丁亥、丁丑，遁得本旬中真食神。 → 《三命通会》卷六#福星贵人与真食神之福
  - `[ns_smth_06_102]` `[trigger: 真食神得位]` `[factor_trigger: shishen_dewei AND fuhou_xiangfu]` `[role: 主干依赖]` 真食神得本气、本位而不受破损，主享受自然，非贵亦富。 → 《三命通会》卷六#福星贵人与真食神之福
  - `[ns_smth_06_103]` `[trigger: 偏印破福]` `[factor_trigger: pianyin_guozhong OR qisha_xianlu]` `[role: 条件分支]` 若偏印过重或七煞显露，则食神之福容易被削弱甚至反转。 → 《三命通会》卷六#福星贵人与真食神之福
  - `[ns_smth_06_104]` `[trigger: 福星结论]` `[factor_trigger: fuxing_guiren AND wupo]` `[role: 总结]` 福星贵人多主生活从容、衣食丰足，难见极端困顿。 → 《三命通会》卷六#福星贵人与真食神之福

- **校勘与字词辨析（双语）**：

  - “遁得本旬中真食神”一句，本稿理解为在同一旬空范围内，食神得真气、真位，不夹杂他气。
  - 《甲丙相邀入虎乡歌》原以年干支论，本稿在此不拘于年、日，只取“甲配丙、乙配丁”的结构意涵。
  - “非贵亦富”一语，本稿在白话中解释为“生活条件优越、福厚从容”，不局限于科名仕途。
  - **English**：
    - Key judgment principles are preserved; the detailed explanation emphasizes "leisurely and composed nobility" not limited to examination success or official career."""
    normalized_text_zh: str = """"""
    subject: str = "福星贵人与真食神之福"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_25', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_shishen', 'bazi_semantic', 'bazi_state_degree_8', 'bazi_semantic', 'bazi_condition_pianyin', 'bazi_semantic', 'bazi_condition_factor_165', 'bazi_semantic', 'source_ref', 'rel_smth_06_076', 'fuxing_guiren_presence', 'rel_smth_06_077', 'zhen_shishen_chundu', 'rel_smth_06_078', 'pianyin_guozhong_risk', 'evi_smth_06_076', 'fuxing_guiren_presence', 'rule_fuxing', 'evi_smth_06_077', 'zhen_shishen_chundu', 'rule_zhenshishen', 'evi_smth_06_078', 'caiyin_xiangfu', 'rule_fugui', 'map_smth_06_051', 'map_smth_06_052']
    
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
        l1_anchor="smth_v1.0.0_福星贵人与真食神之福_001_L1",
    )
    version: str = "1.0.0"
