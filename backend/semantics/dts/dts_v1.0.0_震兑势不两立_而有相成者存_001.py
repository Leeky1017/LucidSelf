"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997643
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
    semantic_id="dts_v1.0.0_震兑势不两立_而有相成者存_001",
    book_id="dts",
    engine_id="bazi"
)
class 震兑势不两立而有相成者存(SemanticEntry):
    """
    - **原文（source_text）**：
  震兑势不两立，而有相成者存。

- 原注（原文注解）：
  　　震在内，兑在外，月日皆木，年时皆金是也。主之所喜者在震，以兑为敌国，必用火攻；主之所喜...
    """
    
    original_text: str = """- **原文（source_text）**：
  震兑势不两立，而有相成者存。

- 原注（原文注解）：
  　　震在内，兑在外，月日皆木，年时皆金是也。主之所喜者在震，以兑为敌国，必用火攻；主之所喜者在兑，以震为奸宄，备御之而已。兑在内，震在外，月日皆金，年时皆木是也。主之所喜者在兑，以震为游兵，易于灭，然不可党也；主之所喜者在震，以兑为内寇，难于灭，尤不可助也。惟水可为说客，可以相间相解，亦论主之所喜所忌何如……（略）。

- **规范化释义（primary_lang_explained）**：
  金木交争，当以“火攻/水解”权衡，随“主之所喜”立策。相克不必两败，得法可相成。

- 分字分词释义：
  - 震：木势在内。
  - 兑：金势在外。
  - 火攻/水解：以火制金助木/以水和金解争。
  - 主之所喜：体用与喜忌所指。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 震兑 | Thunder-Swamp (Zhen-Dui) | 金木对峙 | Wood and Metal confrontation | zhendui | existing |
| 势不两立 | Irreconcilable Force | 势同水火 | Opposing forces | shibuliangyi | new_candidate |
| 相成 | Mutual Success (Xiang-Cheng) | 反成其功 | Complementary success | xiangcheng | new_candidate |
| 火攻 | Fire Attack (Huo-Gong) | 以火制金 | Control Metal with Fire | huogong | new_candidate |
| 水解 | Water Mediation (Shui-Jie) | 以水通关 | Mediate with Water | shuijie | new_candidate |
| 内寇 | Inner Bandit (Nei-Kou) | 内部隐患 | Internal threat | neikou | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Zhen-Dui (Wood-Metal) theory: Wood (Zhen) Inside, Metal (Dui) Outside (or vice versa). They stand opposed (Shi-Bu-Liang-Li). If Host favors Wood, use Fire Attack (Huo-Gong) to control Metal. If Host favors Metal, use Water Mediation (Shui-Jie) cautiously. Conflict can turn into Mutual Success (Xiang-Cheng) with right strategy."""
    normalized_text_zh: str = """"""
    subject: str = "震兑势不两立，而有相成者存。"
    factor_refs: list = []
    
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
        l1_anchor="dts_v1.0.0_震兑势不两立_而有相成者存_001_L1",
    )
    version: str = "1.0.0"
