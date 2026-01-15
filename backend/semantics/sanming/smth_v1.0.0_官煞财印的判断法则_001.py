"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264118
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
    semantic_id="smth_v1.0.0_官煞财印的判断法则_001",
    book_id="sanming",
    engine_id="bazi"
)
class 官煞财印的判断法则(SemanticEntry):
    """
    - 原文（source_text）：
  凡正官一位，乃君子贵人，笃厚纯粹，刚直廉明，年时有印尤妙，多则反主成败。四位纯官，仕宦虚名。
  凡七煞一位，聪明伶俐，二位、三位，先清后浊。四柱纯煞，有制贵...
    """
    
    original_text: str = """- 原文（source_text）：
  凡正官一位，乃君子贵人，笃厚纯粹，刚直廉明，年时有印尤妙，多则反主成败。四位纯官，仕宦虚名。
  凡七煞一位，聪明伶俐，二位、三位，先清后浊。四柱纯煞，有制贵，无制贫。
  凡财一位，务要得时，富贵成家。为人性燥紧急，二位性气减半；三位、四位，耗气身衰。若身旺甚，则可成立，弱则劳苦生受。
  凡印不论一位、二位、四位都好，格中不宜见财破印。

- 分字分词释义：
  - **一位**：指天干透出一个，或地支一位有力。
  - **四位纯官**：四柱天干地支皆见官星，官多变鬼，或官重身轻。
  - **得时**：生于财旺之月。
  - **耗气身衰**：财多耗身（财为我克，克者耗我气）。

- **规范化释义（primary_lang_explained）**：
  正官只有一位且清纯，主君子贵人，性格敦厚纯粹，刚直廉明。若年干或时干有印绶护官生身，更加美妙。若官星太多，反而成败无常。若四柱全是正官，不仅不贵，反主虚名（官多无官）。
  七煞只有一位，主聪明伶俐（有制）。若见二位、三位，先清后浊（杂乱）。若四柱纯煞（杀重身轻或从杀），有制伏主贵，无制伏主贫贱。
  财星一位，必须得时（旺相），主富贵成家。性格多急躁。若见二位财星，急躁之气减半。若见三位、四位财星，财多耗身，日主衰弱。若日主极旺，尚可成立；若日主弱，则终身劳苦受累（富屋贫人）。
  印绶不论一位、二位还是四位，通常都好（印生身，多多益善，但不可太过）。最忌格局中见财星破印。

- 核心要点：
  - **官煞贵清**：官煞皆喜一位清纯，忌多而杂。
  - **财多身弱**：财喜身旺，忌身弱财多。
  - **印绶护身**：印绶忌财破。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_005]` `[trigger: 正官一位]` `[factor_trigger: zhengguan_yiwei AND junzi_guiren]` `[role: 主干]` 凡正官一位，乃君子贵人，笃厚纯粹，刚直廉明。 → 《三命通会》卷十#官煞财印的判断法则
  - `[ns_smth_10_006]` `[trigger: 七煞一位]` `[factor_trigger: qisha_yiwei AND congming_lingli]` `[role: 主干依赖]` 凡七煞一位，聪明伶俐，二位、三位，先清后浊。 → 《三命通会》卷十#官煞财印的判断法则
  - `[ns_smth_10_007]` `[trigger: 财一位]` `[factor_trigger: cai_yiwei AND deshi_fugui]` `[role: 条件分支]` 凡财一位，务要得时，富贵成家。三位、四位，耗气身衰。 → 《三命通会》卷十#官煞财印的判断法则
  - `[ns_smth_10_008]` `[trigger: 印不宜见财]` `[factor_trigger: yin_buyi_jiancai AND gezhong_poyin]` `[role: 总结]` 凡印不论一位、二位、四位都好，格中不宜见财破印。 → 《三命通会》卷十#官煞财印的判断法则"""
    normalized_text_zh: str = """"""
    subject: str = "官煞财印的判断法则"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_condition_factor_82', 'bazi_semantic', 'bazi_state_factor_219', 'bazi_semantic', 'bazi_state_factor_220', 'bazi_semantic', 'bazi_relation_factor_100', 'bazi_semantic', 'bazi_condition_factor_83', 'bazi_semantic', 'source_ref', 'rel_smth_10_004', 'yiwei_qingchun', 'rel_smth_10_005', 'guanduo_wuguan', 'rel_smth_10_006', 'caiduo_shenruo', 'evi_smth_10_004', 'yiwei_qingchun', 'rule_yiwei_qingchun1', 'evi_smth_10_005', 'xuming_wushi', 'rule_guanduo_wuguan1', 'evi_smth_10_006', 'zhongshen_laoku', 'rule_caiduo_shenruo1', 'map_smth_10_003', 'map_smth_10_004']
    
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
        l1_anchor="smth_v1.0.0_官煞财印的判断法则_001_L1",
    )
    version: str = "1.0.0"
