"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339690
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
    semantic_id="smth_v1.0.0_六癸日庚申时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日庚申时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时庚申，官星印旺在其支。柱中无己丙寅巳，自有荣华富贵时。
  癸日庚申时，作专印合禄。癸以戊为正官，庚为正印，申上庚旺戊生，以申合巳中戊丙，癸日得财官...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时庚申，官星印旺在其支。柱中无己丙寅巳，自有荣华富贵时。
  癸日庚申时，作专印合禄。癸以戊为正官，庚为正印，申上庚旺戊生，以申合巳中戊丙，癸日得财官，若有倚托，柱中无财及破害刑冲官印，主贵；柱中有财，行财运，反复进退，少贵。

- 分字分词释义：
  - **专印合禄**：庚金正印得禄于申，申合巳（戊丙），合来财官。
  - **忌丙寅巳**：丙坏印，寅冲申，巳填实（合禄忌填实）。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于庚申时，正印庚金坐禄，印旺。申金合出巳中戊土正官、丙火正财。若日主有倚托，且柱中无丙火（坏印）、寅木（冲申）、巳火（填实），主荣华富贵。若见财星破坏印绶，或刑冲破害，则贵气减损。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Geng-Shen Hour":

  - Official star Seal prosperous in its branch—Geng Metal Direct Seal at Shen is at Prosperity position; Shen combines Si getting Wealth-Official.
  - If pillars have no Ji-Bing-Yin-Si, naturally has glorious-splendor wealthy-noble time.
  - Making Exclusive-Seal Combined-禄; Geng prosperous Wu generates; with support and no Wealth or break-harm-punish-clash, noble.
  - Key: Combined-禄 pattern fears filling in (Si) and clashing (Yin); Wealth damages Seal should be avoided.

- 核心要点：
  - **合禄格**：申合巳。
  - **正印格**：庚申印旺。
  - **忌财**：财坏印。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_gui_gengshen_001]` `[trigger: 专印合禄]` `[factor_trigger: gui_gengshen AND zhuanyin_helu]` `[role: 主干]` 癸日庚申时，作专印合禄，庚为正印，申上庚旺戊生。 → 《三命通会》卷九#六癸日庚申时
  - `[ns_smth_09_gui_gengshen_002]` `[trigger: 官星印旺]` `[factor_trigger: guanxing_yinwang AND zhizhong]` `[role: 主干依赖]` 官星印旺在其支，以申合巳中戊丙，癸日得财官。 → 《三命通会》卷九#六癸日庚申时
  - `[ns_smth_09_gui_gengshen_003]` `[trigger: 无丙寅巳]` `[factor_trigger: wu_bing_yin_si AND chengge_guanjian]` `[role: 条件分支]` 柱中无己丙寅巳，自有荣华富贵时。 → 《三命通会》卷九#六癸日庚申时
  - `[ns_smth_09_gui_gengshen_004]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND helu_deyong]` `[role: 总结]` 若有倔托，柱中无财及破害刑冲官印，主贵。 → 《三命通会》卷九#六癸日庚申时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日庚申时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_321', 'bazi_semantic', 'bazi_relation_factor_131', 'bazi_semantic', 'bazi_state_factor_334', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_bing_yin_si', 'bazi_semantic', 'source_ref', 'rel_smth_09_169', 'zhuanyin_helu', 'rel_smth_09_170', 'wu_bing_yin_si', 'rel_smth_09_171', 'caixin_poyin', 'evi_smth_09_169', 'yinwang_shengshen', 'rule_yinwang_shengshen1', 'evi_smth_09_170', 'ronghua_fugui', 'rule_ronghua_fugui1', 'evi_smth_09_171', 'fanfu_jintui', 'rule_fanfu_jintui1', 'map_smth_09_113', 'map_smth_09_114']
    
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
        l1_anchor="smth_v1.0.0_六癸日庚申时_001_L1",
    )
    version: str = "1.0.0"
