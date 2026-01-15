"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339518
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
    semantic_id="smth_v1.0.0_六辛日己丑时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日己丑时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时己丑，金土持争势不安。年月财官相救助，免交贫困受饥寒。
  辛日己丑时，金土相争。辛以己为倒食，丑上有明己暗辛。岁月无财官救助者，贫困；得财官运，亦...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时己丑，金土持争势不安。年月财官相救助，免交贫困受饥寒。
  辛日己丑时，金土相争。辛以己为倒食，丑上有明己暗辛。岁月无财官救助者，贫困；得财官运，亦吉。

- 分字分词释义：
  - **金土持争**：丑为金库，己为偏印（倒食），土多金埋，或土金混杂。
  - **倒食**：己土偏印，夺食（癸水）。
  - **暗辛**：丑中藏辛金、己土、癸水。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于己丑时，己土偏印透出，丑中辛金助身，土金混杂相争。若岁月无财官（木火）救助，制土生金（或生官），则主贫困。若行财官运，亦可吉利。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Ji-Chou Hour":

  - Metal-Earth hold struggle, situation unstable—Ji Earth Partial Seal reveals; Chou hides Xin Metal and Ji Earth.
  - If year-month have Wealth-Official mutual rescue, avoids poverty hunger and cold.
  - Without Wealth-Official rescue, indicates poverty; encountering Wealth-Official luck, also auspicious.
  - Key: Earth abundant buries Metal; requires Wood (Wealth) to loosen Earth or Fire (Official) to refine Metal.

- 核心要点：
  - **土多金埋**：己丑重土，辛金易被埋没。
  - **偏印夺食**：己土克丑中癸水。
  - **喜财官**：喜木疏土，火炼金。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_101]` `[trigger: 金土持争]` `[factor_trigger: jintu_chizheng AND shi_bu_an]` `[role: 主干]` 六辛日生时己丑，金土持争势不安。 → 《三命通会》卷九#六辛日己丑时
  - `[ns_smth_09_102]` `[trigger: 财官相救]` `[factor_trigger: caiguan_xiangjiu AND mian_pinkun]` `[role: 主干依赖]` 年月财官相救助，免交贫困受饥寒。 → 《三命通会》卷九#六辛日己丑时
  - `[ns_smth_09_103]` `[trigger: 无财官救]` `[factor_trigger: wu_caiguan_jiu AND pinkun]` `[role: 条件分支]` 岁月无财官救助者，贫困。 → 《三命通会》卷九#六辛日己丑时
  - `[ns_smth_09_104]` `[trigger: 得财官运]` `[factor_trigger: de_caiguan_yun AND yiji]` `[role: 总结]` 得财官运，亦吉。 → 《三命通会》卷九#六辛日己丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日己丑时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_metal_earth', 'bazi_semantic', 'bazi_relation_pianyin_1', 'bazi_semantic', 'bazi_state_factor_289', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_factor_126', 'bazi_semantic', 'source_ref', 'rel_smth_09_076', 'jintu_chizheng', 'rel_smth_09_077', 'jintu_chizheng', 'rel_smth_09_078', 'caiguan_jiuzhu', 'evi_smth_09_076', 'jintu_chizheng', 'rule_jintu_chizheng1', 'evi_smth_09_077', 'pinkun', 'rule_wu_caiguan_jiuzhu1', 'evi_smth_09_078', 'caiguan_jiuzhu', 'rule_caiguan_jiuzhu1', 'map_smth_09_051', 'map_smth_09_052']
    
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
        l1_anchor="smth_v1.0.0_六辛日己丑时_001_L1",
    )
    version: str = "1.0.0"
