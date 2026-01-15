"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412776
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
    semantic_id="smth_v1.0.0_墓运与用神入墓_001",
    book_id="sanming",
    engine_id="bazi"
)
class 墓运与用神入墓(SemanticEntry):
    """
    - **原文（source_text）**：

  附论墓运：秘诀云：幼年不宜逢墓库，老年值此却丰隆。又云：旺官旺印与旺财，入墓有祸；伤官食神并身旺，遇库兴灾。又云：旺煞入墓，寿算难延。可见凡官印伤官...
    """
    
    original_text: str = """- **原文（source_text）**：

  附论墓运：秘诀云：幼年不宜逢墓库，老年值此却丰隆。又云：旺官旺印与旺财，入墓有祸；伤官食神并身旺，遇库兴灾。又云：旺煞入墓，寿算难延。可见凡官印伤官七煞为用神者，俱忌行墓库之运，惟晚年行自库地则吉。

- 分字分词释义：

  - **墓库**：四库之地兼具藏与收之象，为气势变化的关键节点。
  - **幼年不宜逢墓库，老年值此却丰隆**：早年行墓运，多为压抑潜力；晚年行墓运，则有“收成”“归藏”之象。

- **规范化释义（primary_lang_explained）**：

  墓运的关键不在“墓”字本身，而在“谁入墓、何时入墓”：

  - 若用神入墓于不当之年，易应挫折、病灾或停滞；
  - 若忌神入墓，则有“藏凶于库”的好处，反而减轻其害。

- 核心要点：

  - 看墓运，先定用神与忌神，后看谁被收、谁被藏。
  - 幼年入墓多为压抑，晚年入墓多为归藏与收束。

- 详细解说：

  对实际人生而言，墓运往往对应：

  - 职业生涯从扩张走向收缩；
  - 健康与精力从外放转向保守与养藏；
  - 人际从广泛交游回归少数核心关系。

- **校勘与字词辨析（双语）**：

  - 原文对“旺煞入墓，寿算难延”一条，本稿在解释时强调“需以煞为用、并结合整体强弱判断”，不作单一死亡预言。
  - **English**：
    - Not interpreted as single death prediction.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_165]` `[trigger: 墓运定义]` `[factor_trigger: muyun_presence AND yongshen_rumu]` `[role: 主干]` 幼年不宜逢墓库，老年值此却丰隆。 → 《三命通会》卷六#附论墓运
  - `[ns_smth_06_166]` `[trigger: 旺官入墓]` `[factor_trigger: wangguan_rumu AND youhuo]` `[role: 主干依赖]` 旺官旺印与旺财，入墓有祸。 → 《三命通会》卷六#附论墓运
  - `[ns_smth_06_167]` `[trigger: 用神忌墓]` `[factor_trigger: yongshen_weiguanyinsha AND ji_muku]` `[role: 条件分支]` 凡官印伤官七煚为用神者，俱忌行墓库之运。 → 《三命通会》卷六#附论墓运
  - `[ns_smth_06_168]` `[trigger: 晚年自库]` `[factor_trigger: wannian_ziku AND ji]` `[role: 总结]` 惟晚年行自库地则吉。 → 《三命通会》卷六#附论墓运"""
    normalized_text_zh: str = """"""
    subject: str = "墓运与用神入墓"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_43', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_yongshen_degree', 'bazi_semantic', 'bazi_state_factor_31', 'bazi_semantic', 'bazi_condition_factor_204', 'bazi_semantic', 'bazi_condition_factor_205', 'bazi_semantic', 'source_ref', 'rel_smth_06_151', 'muyun_ge_presence', 'rel_smth_06_152', 'yongshen_rumu', 'rel_smth_06_153', 'younian_fengmu_risk', 'evi_smth_06_151', 'muyun_ge_presence', 'rule_muyun', 'evi_smth_06_152', 'yongshen_rumu', 'rule_rumu', 'evi_smth_06_153', 'wannian_ziku', 'rule_ziku', 'map_smth_06_101', 'map_smth_06_102']
    
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
        l1_anchor="smth_v1.0.0_墓运与用神入墓_001_L1",
    )
    version: str = "1.0.0"
