"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066860
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
    semantic_id="smth_v1.0.0_3_特殊格局精要_二_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3特殊格局精要二(SemanticEntry):
    """
    - **原文（source_text）**：
  六癸日时逢寅位，岁月怕戊己二方。
  甲子日再逢子时，畏庚辛申酉丑午。
  辛癸日多逢丑地，不喜官星；岁时逢子巳二宫，虚名虚利。
  拱禄拱贵，填实则...
    """
    
    original_text: str = """- **原文（source_text）**：
  六癸日时逢寅位，岁月怕戊己二方。
  甲子日再逢子时，畏庚辛申酉丑午。
  辛癸日多逢丑地，不喜官星；岁时逢子巳二宫，虚名虚利。
  拱禄拱贵，填实则凶。
  时上偏财，别宫忌见。
  六辛日时逢戊子，嫌午位，运喜西方。
  五行遇月支偏官，岁时中亦宜制伏。

- **分字分词释义**：
  - **六癸逢寅**：刑合格（癸亥/癸丑/癸酉见甲寅时，寅刑巳，出官印）。
  - **甲子逢子**：子遥巳格（甲子日甲子时，子遥巳中丙戊，合辛癸）。
  - **辛癸逢丑**：丑遥巳格（辛丑/癸丑日，多丑遥巳，合丙戊）。
  - **拱禄拱贵**：虚拱。
  - **时上偏财**：时上偏财格，忌年离月有财（别宫忌见）。
  - **六辛逢戊子**：六阴朝阳格（辛日戊子时，子动巳，巳动丙官）。

- **白话原意**：
  六癸日生于甲寅时（刑合格），岁月怕见戊己官煞填实。
  甲子日再逢甲子时，叫“子遥巳格”。怕见庚辛申酉（官煞）及丑（合子）、午（冲子），这就破格了。
  辛日或癸日多逢丑地（丑遥巳），不喜见官星（填实）。若岁时遇到子（合丑）、巳（填实），则名利皆虚。
  拱禄、拱贵格，最怕填实或刑冲，主凶。
  时上偏财格，只宜时上一位，别宫（年月）忌见财星混杂。
  六辛日生于戊子时（六阴朝阳），嫌午字冲子。运喜西方金地（助身）。
  五行遇到月支偏官（七煞格），岁运或时柱中应当有制伏（食神）。

- **核心要点**：
  - **遥合倒冲**：皆忌填实、刑冲、官煞混杂。
  - **时上偏财**：一位为贵，多则不奇。
  - **六阴朝阳**：喜金水，忌火土（官煞）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_067]` `[trigger: 刑合格]` `[factor_trigger: xinghe_ge AND guiri_yinshi]` `[role: 主干]` 六癸日时逢寅位，岁月怕戊己二方。 → 《三命通会》卷十一#特殊格局精要（二）
  - `[ns_smth_11_068]` `[trigger: 子遥巳]` `[factor_trigger: ziyao_si AND jiazi_zishi]` `[role: 主干依赖]` 甲子日再逢子时，畏庚辛申酉丑午。 → 《三命通会》卷十一#特殊格局精要（二）
  - `[ns_smth_11_069]` `[trigger: 拱禄拱贵]` `[factor_trigger: gonglu_gonggui AND tianshi_xiong]` `[role: 条件分支]` 拱禄拱贵，填实则凶。 → 《三命通会》卷十一#特殊格局精要（二）
  - `[ns_smth_11_070]` `[trigger: 六阴朝阳]` `[factor_trigger: liuyin_chaoyang AND xinri_wuzishi]` `[role: 条件分支]` 六辛日时逢戊子，嫌午位，运喜西方。 → 《三命通会》卷十一#特殊格局精要（二）"""
    normalized_text_zh: str = """"""
    subject: str = "3 特殊格局精要（二）"
    factor_refs: list = ['engine_id', 'bazi_structure_factor_29', 'bazi_semantic', 'bazi_structure_zi_si', 'bazi_semantic', 'bazi_structure_chou_si', 'bazi_semantic', 'bazi_state_factor_287', 'bazi_semantic', 'bazi_state_factor_78', 'bazi_semantic', 'bazi_condition_factor_20', 'bazi_semantic', 'source_ref', 'rel_smth_11_058', 'core_factor', 'rel_smth_11_059', 'cond_factor', 'rel_smth_11_060', 'risk_factor', 'evi_smth_11_058', 'core_factor', 'rule_name58', 'evi_smth_11_059', 'cond_factor', 'rule_name59', 'evi_smth_11_060', 'risk_factor', 'rule_name60', 'map_smth_11_039', 'map_smth_11_040']
    
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
        l1_anchor="smth_v1.0.0_3_特殊格局精要_二_001_L1",
    )
    version: str = "1.0.0"
