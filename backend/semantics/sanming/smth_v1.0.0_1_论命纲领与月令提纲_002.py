"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066837
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
    semantic_id="smth_v1.0.0_1_论命纲领与月令提纲_002",
    book_id="sanming",
    engine_id="bazi"
)
class 1论命纲领与月令提纲(SemanticEntry):
    """
    - **原文（source_text）**：
  四柱排定，三才次分。专以日上天元，配合八字支干。有见不见之形，无时不有；神煞相绊，轻重较量。
  若乃时逢七煞，见之未必为凶；月制干强，其煞反为权印。...
    """
    
    original_text: str = """- **原文（source_text）**：
  四柱排定，三才次分。专以日上天元，配合八字支干。有见不见之形，无时不有；神煞相绊，轻重较量。
  若乃时逢七煞，见之未必为凶；月制干强，其煞反为权印。
  财官印绶全备，藏蓄于四季之中。
  官星财气长生，镇居于寅申巳亥。

- **分字分词释义**：
  - **三才**：天干、地支、藏干（或年月日时）。
  - **日上天元**：日干，命之主。
  - **见不见之形**：明见者为有，暗拱、暗夹、遥冲者为不见。
  - **神煞相绊**：贪合忘冲，或吉神凶煞互相牵制。
  - **四季**：辰戌丑未。
  - **寅申巳亥**：四长生之地。

- **白话原意**：
  排好四柱八字，分清天地人三才。专门以日干为主，配合其余七个干支来分析。其中有明见的格局，也有暗拱、暗夹等看不见的格局，无时无刻不存在。神煞之间互相牵绊（如贪合忘冲、合煞留官），需要较量其轻重（看谁更强）。
  如果时柱遇到七煞，未必就是凶（时上一位贵）。如果月令有制（如食神）且日干强旺，七煞反而化为权柄和印信（煞印相生或食制煞）。
  财官印绶如果全备，往往藏在辰戌丑未四季库中（杂气财官格）。
  官星和财气的长生之地，往往镇守在寅申巳亥四长生位。

- **核心要点**：
  - **日干为主**：论命核心。
  - **见不见之形**：重视暗格。
  - **七煞喜忌**：身强有制为权。
  - **四库四生**：财官所藏所生之地。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_059]` `[trigger: 日上天元]` `[factor_trigger: rishang_tianyuan AND bazi_zhigan]` `[role: 主干]` 四柱排定，三才次分。专以日上天元，配合八字支干。 → 《三命通会》卷十一#论命纲领与月令提纲
  - `[ns_smth_11_060]` `[trigger: 见不见之形]` `[factor_trigger: jianbujian_zhixing AND shensha_xiangban]` `[role: 主干依赖]` 有见不见之形，无时不有；神煞相绊，轻重较量。 → 《三命通会》卷十一#论命纲领与月令提纲
  - `[ns_smth_11_061]` `[trigger: 七煞为权]` `[factor_trigger: qisha_weiquan AND yuezhigan_qiang]` `[role: 条件分支]` 若乃时逢七煞，见之未必为凶；月制干强，其煞反为权印。 → 《三命通会》卷十一#论命纲领与月令提纲
  - `[ns_smth_11_062]` `[trigger: 四库四生]` `[factor_trigger: siku_cangcai AND sisheng_zhendi]` `[role: 总结]` 财官印绶全备，藏蓄于四季之中。官星财气长生，镇居于寅申巳亥。 → 《三命通会》卷十一#论命纲领与月令提纲"""
    normalized_text_zh: str = """"""
    subject: str = "1 论命纲领与月令提纲"
    factor_refs: list = ['engine_id', 'bazi_factor_32', 'bazi_semantic', 'bazi_structure_factor_25', 'bazi_semantic', 'bazi_relation_factor_26', 'bazi_semantic', 'bazi_state_huaquan_1', 'bazi_semantic', 'bazi_structure_factor_26', 'bazi_semantic', 'bazi_structure_factor_27', 'bazi_semantic', 'source_ref', 'rel_smth_11_052', 'core_factor', 'rel_smth_11_053', 'cond_factor', 'rel_smth_11_054', 'risk_factor', 'evi_smth_11_052', 'core_factor', 'rule_name52', 'evi_smth_11_053', 'cond_factor', 'rule_name53', 'evi_smth_11_054', 'risk_factor', 'rule_name54', 'map_smth_11_035', 'map_smth_11_036']
    
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
        l1_anchor="smth_v1.0.0_1_论命纲领与月令提纲_002_L1",
    )
    version: str = "1.0.0"
