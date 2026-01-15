"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264142
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
    semantic_id="smth_v1.0.0_吉凶神之引归与用神得力_001",
    book_id="sanming",
    engine_id="bazi"
)
class 吉凶神之引归与用神得力(SemanticEntry):
    """
    - **原文（source_text）**：
  凡年月日有吉神，要时引归生旺之处；有凶神，要时引归制伏之乡。若时上带吉神或凶神，亦要年月日上吉者生之，凶者制之。
  月上有用神，得祖宗之力；时上有用...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡年月日有吉神，要时引归生旺之处；有凶神，要时引归制伏之乡。若时上带吉神或凶神，亦要年月日上吉者生之，凶者制之。
  月上有用神，得祖宗之力；时上有用神，得子孙之力。反此则否。

- **分字分词释义**：
  - **引归**：将年月日的神煞引至时支看其生旺死绝。
  - **生旺之处**：长生、帝旺、临官等地。
  - **制伏之乡**：死绝、受克之地。

- **白话原意**：
  如果在年、月、日柱上有吉神（如财官印食贵人），最好在时支上处于生旺之地，这样晚年福气绵长。如果有凶神（如七杀羊刃亡劫），最好在时支上处于受制伏或死绝之地，这样晚年无灾。
  反过来，如果时柱上带吉神或凶神，也需要年、月、日柱上的五行来生扶吉神、制约凶神。
  如果用神在月令上有力，主得祖宗父母之力；如果用神在时柱上得力，主得子孙后代之力。如果用神不得力或位置不当，则得不到相应的福荫。

- **核心要点**：
  - **吉凶引归**：吉神宜生旺，凶神宜制伏。
  - **时支归宿**：时支为最终归宿，决定吉凶结局。
  - **宫位六亲**：月主祖父，时主子孙。
  - **English**：
    - "Month governs ancestors, hour governs descendants" — preserved as the guiding principle for pillar correspondences.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_013]` `[trigger: 吉神引归]` `[factor_trigger: jishen_yingui AND shengwang_zhichu]` `[role: 主干]` 凡年月日有吉神，要时引归生旺之处。 → 《三命通会》卷十#吉凶神之引归与用神得力
  - `[ns_smth_10_014]` `[trigger: 凶神制伏]` `[factor_trigger: xiongshen_zhifu AND sijue_zhixiang]` `[role: 主干依赖]` 有凶神，要时引归制伏之乡。 → 《三命通会》卷十#吉凶神之引归与用神得力
  - `[ns_smth_10_015]` `[trigger: 月上用神]` `[factor_trigger: yueshang_yongshen AND de_zuzong_zhili]` `[role: 条件分支]` 月上有用神，得祖宗之力；时上有用神，得子孙之力。 → 《三命通会》卷十#吉凶神之引归与用神得力
  - `[ns_smth_10_016]` `[trigger: 反此则否]` `[factor_trigger: fanci_zefu AND yongshen_shiwu]` `[role: 总结]` 反此则否。 → 《三命通会》卷十#吉凶神之引归与用神得力"""
    normalized_text_zh: str = """"""
    subject: str = "吉凶神之引归与用神得力"
    factor_refs: list = ['engine_id', 'bazi_factor_28', 'bazi_semantic', 'bazi_condition_factor_86', 'bazi_semantic', 'bazi_condition_factor_87', 'bazi_semantic', 'bazi_relation_factor_102', 'bazi_semantic', 'bazi_relation_zi_2', 'bazi_semantic', 'source_ref', 'rel_smth_10_010', 'jishen_yingui', 'rel_smth_10_011', 'xiongshen_zhifu', 'rel_smth_10_012', 'yueshen_youtuo', 'evi_smth_10_010', 'jishen_yingui', 'rule_jishen_yingui1', 'evi_smth_10_011', 'xiongshen_zhifu', 'rule_xiongshen_zhifu1', 'evi_smth_10_012', 'de_zuzong_zhili', 'rule_yueshen_youtuo1', 'map_smth_10_007', 'map_smth_10_008']
    
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
        l1_anchor="smth_v1.0.0_吉凶神之引归与用神得力_001_L1",
    )
    version: str = "1.0.0"
