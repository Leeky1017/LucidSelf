"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997656
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
    semantic_id="dts_v1.0.0_君不可抗也_贵乎损上以益下_001",
    book_id="dts",
    engine_id="bazi"
)
class 君不可抗也贵乎损上以益下(SemanticEntry):
    """
    - **原文（source_text）**：
  君不可抗也，贵乎损上以益下。

- 原注（原文注解）：
  　　日主为君，财星为臣。如甲乙日主，满盘是木，内有一二点土，是君盛臣衰，要助其臣：火生之，...
    """
    
    original_text: str = """- **原文（source_text）**：
  君不可抗也，贵乎损上以益下。

- 原注（原文注解）：
  　　日主为君，财星为臣。如甲乙日主，满盘是木，内有一二点土，是君盛臣衰，要助其臣：火生之，土实之，金卫之（官制劫以卫财），其势要多，庶几上全而下安。

- **规范化释义（primary_lang_explained）**：
  君盛臣衰，宜以火土金之序“生→实→卫”扶臣，使上下安。

- 分字分词释义：
  - 君：日主/主位。
  - 不可抗：不宜逆其纲常而强伐。
  - 损上益下：从君侧移资于臣侧（财、辅等）。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 君臣 | Ruler-Subject (Jun-Chen) | 君臣关系 | Ruler-Subject relationship | junchen | existing |
| 损上益下 | Damage Upper Benefit Lower | 损君益臣 | Transfer resources to Subject | sunshang_yixia | new_candidate |
| 庶几 | Hopefully/Almost | 差不多 | Approximating | shuji | new_candidate |
| 上全下安 | Upper Whole Lower Safe | 上下安顿 | Top intact, bottom safe | shangquan_xiaan | new_candidate |
| 卫之 | Defend It (Wei-Zhi) | 护卫财官 | Defend Wealth/Official | weizhi | new_candidate |
| 君不可抗 | Ruler Cannot Be Opposed | 君位尊严 | Ruler position respected | junbukekang | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Jun-Chen (Ruler-Subject) theory: The Ruler (Daymaster) cannot be opposed (Bu-Ke-Kang). Value lies in "Damaging the Upper to Benefit the Lower" (Sun-Shang Yi-Xia). When Ruler is strong and Subject (Wealth/Official) weak, use Fire to generate, Earth to substantiate, and Metal to defend the Subject."""
    normalized_text_zh: str = """"""
    subject: str = "君不可抗也，贵乎损上以益下。"
    factor_refs: list = ['source_ref', 'rel_dts_jc_001', 'junbukekang', 'rel_dts_jc_002', 'sunshang_yixia', 'rel_dts_jc_003', 'weizhi', 'rel_dts_jc_004', 'shangquan_xiaan', 'evi_dts_jc_001', 'rule_junchen_balance', 'evi_dts_jc_002', 'rule_junchen_support', 'evi_dts_jc_003', 'rule_junchen_case_pattern', 'concept_hierarchy', 'concept_redistribution', 'concept_protection', 'engine_id', 'junchen_role_mapping_profile', 'role_profile', 'bazi_calculator', 'junchen_balance_index', 'state_index', 'bazi_semantic', 'junchen_resource_node', 'placement', 'bazi_semantic', 'junchen_support_strategy', 'evaluation', 'bazi_rule_engine', 'junchen_overcorrect_risk', 'risk_indicator', 'bazi_rule_engine', 'junchen_rebalance_window', 'timing', 'bazi_rule_engine', 'junchen_boundary_flag', 'boundary', 'bazi_rule_engine']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_君不可抗也_贵乎损上以益下_001_L1",
    )
    version: str = "1.0.0"
