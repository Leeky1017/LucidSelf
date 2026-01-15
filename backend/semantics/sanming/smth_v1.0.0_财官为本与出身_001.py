"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264183
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
    semantic_id="smth_v1.0.0_财官为本与出身_001",
    book_id="sanming",
    engine_id="bazi"
)
class 财官为本与出身(SemanticEntry):
    """
    - **原文（source_text）**：
  凡年干上有日之官星，福气最厚；有日之七煞，终身不可除去。
  官星为禄，财星为马。行官星发官，行财星发财。二者不可缺一，各有所用。
  年月上有财官，...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡年干上有日之官星，福气最厚；有日之七煞，终身不可除去。
  官星为禄，财星为马。行官星发官，行财星发财。二者不可缺一，各有所用。
  年月上有财官，必生富贵之家，祖父根基。少年便行官禄运，多是幼年拜命，早发功名。
  年月无财官，日时有之，则是自己成立。人命以财官为本，柱中但得其一，亦可发福。
  若四柱原无官星，不入他格，年月日时干支财多，又行财旺运，亦能成就功名。以财旺自能生官，须身旺方许。
  年月无财官，幼年又行不好运，多是出身卑微，破祖伤父，无见成之福。
  凡命官煞混杂，伤官合神重，男子犯之，耽迷酒色；女人逢之，不媒自嫁。

- **分字分词释义**：
  - **年干官煞**：年柱代表祖上或早期，年干透官福厚，透煞难除（祖业有瑕或出身压力）。
  - **幼年拜命**：年轻时就获得官职任命。
  - **自己成立**：白手起家。
  - **财旺生官**：无官看财，财旺亦可生官（需身旺）。
  - **不媒自嫁**：私奔或自由恋爱（古指无礼教），多指女命感情混乱。

- **白话原意**：
  若年干透出日主的正官，福气最厚（祖上有官贵）；若透出七煞，则终身带有压力或凶咎，难以摆脱。
  官星是禄，财星是马。运走官乡发官，走财乡发财。财官二者不可缺一（最好兼备），各有用途。
  年月柱（祖父父母宫）有财官，必然生于富贵之家，祖业根基深厚。若少年时期就行官禄运，往往年纪轻轻就受封官职，早发功名。
  若年月无财官，而日时柱有财官，则是白手起家、自己创业之命。人命以财官为根本，八字中只要得其中一样有力，就能发福。
  如果四柱原局没有官星，也不入其他特殊格局，但年月日时财星很旺，又行财旺之运，也能成就功名。因为财旺自然能生官（富而生贵），但前提必须是身旺能任财。
  若年月无财官，幼年又行忌神恶运，多半出身卑微，甚至破败祖业、刑伤父母，没有现成的福气可享。
  凡命局官煞混杂，或者伤官、合神（如天干五合、地支六合）太重，男子犯之，容易沉迷酒色；女子犯之，容易私定终身、不媒自嫁（主作风不正）。

- **核心要点**：
  - **财官位置**：年月主祖荫，日时主自立。
  - **财旺生官**：无官看财，财旺身旺亦贵。
  - **混杂合多**：官煞混、合神多，主酒色淫乱。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_025]` `[trigger: 年干官星]` `[factor_trigger: niangan_guanxing AND fuqi_zuihou]` `[role: 主干]` 凡年干上有日之官星，福气最厚；有日之七煞，终身不可除去。 → 《三命通会》卷十#财官为本与出身
  - `[ns_smth_10_026]` `[trigger: 年月财官]` `[factor_trigger: nianyue_caiguan AND fugui_zhijia]` `[role: 主干依赖]` 年月上有财官，必生富贵之家，祖父根基。 → 《三命通会》卷十#财官为本与出身
  - `[ns_smth_10_027]` `[trigger: 日时自立]` `[factor_trigger: rishi_zili AND ziji_chengli]` `[role: 条件分支]` 年月无财官，日时有之，则是自己成立。 → 《三命通会》卷十#财官为本与出身
  - `[ns_smth_10_028]` `[trigger: 官煞混杂]` `[factor_trigger: guansha_hunza AND danmi_jiuse]` `[role: 总结]` 凡命官煞混杂，伤官合神重，男子犯之，耽迷酒色；女人逢之，不媒自嫁。 → 《三命通会》卷十#财官为本与出身"""
    normalized_text_zh: str = """"""
    subject: str = "财官为本与出身"
    factor_refs: list = ['engine_id', 'bazi_relation_factor_103', 'bazi_semantic', 'bazi_relation_factor_104', 'bazi_semantic', 'bazi_state_factor_299', 'bazi_semantic', 'bazi_state_factor_227', 'bazi_semantic', 'bazi_condition_factor_93', 'bazi_semantic', 'source_ref', 'rel_smth_10_019', 'caiguan_weiben', 'rel_smth_10_020', 'caiwang_shengguan', 'rel_smth_10_021', 'nianyue_wucaiguan', 'evi_smth_10_019', 'nianyue_caiguan', 'rule_nianyue_caiguan1', 'evi_smth_10_020', 'yilu_gongming', 'rule_caiwang_shengguan1', 'evi_smth_10_021', 'chushen_beiwei', 'rule_chushen_beiwei1', 'map_smth_10_013', 'map_smth_10_014']
    
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
        l1_anchor="smth_v1.0.0_财官为本与出身_001_L1",
    )
    version: str = "1.0.0"
