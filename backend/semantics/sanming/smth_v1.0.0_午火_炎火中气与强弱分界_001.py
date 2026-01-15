"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042487
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
    semantic_id="smth_v1.0.0_午火_炎火中气与强弱分界_001",
    book_id="sanming",
    engine_id="bazi"
)
class 午火炎火中气与强弱分界(SemanticEntry):
    """
    - **原文（source_text）**：
  午月炎火正，升入中气则一阴生也。庚至此为无用，己至此为归垣；见申子则必战克，见寅戌则越光明。运行东南，正是身强之地，若入西北，则休囚丧形矣。

- *...
    """
    
    original_text: str = """- **原文（source_text）**：
  午月炎火正，升入中气则一阴生也。庚至此为无用，己至此为归垣；见申子则必战克，见寅戌则越光明。运行东南，正是身强之地，若入西北，则休囚丧形矣。

- **分字分词释义**：
  - **炎火正**：午为火王之月，炎热至极。
  - **升入中气、一阴生**：上午火极，转入中气后，一阴始生，预示盛极而衰。
  - **战克 / 越光明**：申子来克午火形成争战；寅戌同类相助，使火光更盛。

- **规范化释义（primary_lang_explained）**：
  午月是火气最盛之时，炎火当权，但火极则阴生，盛中已含衰机。此时庚金难以发挥作用，如铁遇烈焰而被熔；己土反在午地归垣得势。若见申子，则水金来战克午火，多主冲突与消耗；见寅戌，则木火同类相辅，反令火光越发明亮。大运行东南木火之方，有助身强；一旦入西北金水之地，则火力休囚，形势转弱。"""
    normalized_text_zh: str = """"""
    subject: str = "午火：炎火中气与强弱分界"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_wu_presence', 'bazi_calculator', 'yin_wu_xu_combo', 'bazi_calculator', 'zi_wu_chong', 'bazi_calculator', 'seasonal_phase', 'summer', 'fire_peak_intensity', 'bazi_calculator', 'load_bearing_capacity', 'bazi_semantic', 'bing_ding_yun_flag', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_063', 'dizhi_wu_presence', 'rel_smth_02_064', 'zi_wu_chong', 'rel_smth_02_065', 'fire_peak_intensity', 'evi_smth_02_059', 'yin_wu_xu_combo', 'rule_yin_wu_xu_fire', 'evi_smth_02_060', 'zi_wu_chong', 'rule_zi_wu_clash', 'evi_smth_02_061', 'fire_peak_intensity', 'rule_wu_peak_decline', 'map_smth_02_043', 'map_smth_02_044']
    
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
        l1_anchor="smth_v1.0.0_午火_炎火中气与强弱分界_001_L1",
    )
    version: str = "1.0.0"
