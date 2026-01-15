"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228079
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
    semantic_id="smth_v1.0.0_路史论纳音配合之理_001",
    book_id="sanming",
    engine_id="bazi"
)
class 路史论纳音配合之理(SemanticEntry):
    """
    - **原文（source_text）**：
  又观路史云：甲乙木，丑未土，子水而午火，六者无一金，而风后配合，乃以甲子、乙丑、甲午、乙未为之金。此出乎数者然也。数之所合，变之所由出也。乾为天，坤为...
    """
    
    original_text: str = """- **原文（source_text）**：
  又观路史云：甲乙木，丑未土，子水而午火，六者无一金，而风后配合，乃以甲子、乙丑、甲午、乙未为之金。此出乎数者然也。数之所合，变之所由出也。乾为天，坤为地，乾坤合而为泰，干为君，支为臣，干支合而纳音生。是故甲乙为君，子丑为臣，子丑甲乙合而为金。

- **分字分词释义**：
  - **路史**：宋代罗泌撰历史著作。
  - **六者无一金**：六个元素无一属金。
  - **风后配合**：风后配置组合。
  - **出乎数**：出于数理。
  - **数之所合**：数理的配合。
  - **变之所由出**：变化从此产生。
  - **干为君支为臣**：天干为君地支为臣。

- **规范化释义（primary_lang_explained）**：
  又观看《路史》说：甲乙属木，丑未属土，子属水而午属火，这六个元素没有一个属金，但风后配合，就用甲子、乙丑、甲午、乙未作为金。这是出于数理的规律。数理的配合，就是变化产生的原因。乾为天坤为地，乾坤相合而为泰卦，天干为君地支为臣，干支相合而纳音产生。所以甲乙为君，子丑为臣，子丑甲乙相合而成为金。

- **完整对等诠释（secondary_lang_full）**：
  Observing Lushi (Road History): Jia-Yi are Wood, Chou-Wei are Earth, Zi is Water while Wu is Fire—these six have not one Metal element, yet Fenghou's pairing made Jiazi, Yichou, Jiawu, Yiwei into Metal. This emerges from numerical principles. Where numbers combine, transformations arise. Qian is Heaven, Kun is Earth; Qian-Kun combine to form Tai. Stems are sovereign, Branches are ministers; Stems-Branches combine and Nayin is born. Thus Jia-Yi are sovereign, Zi-Chou are ministers; Zi-Chou with Jia-Yi combine to become Metal.

- **核心要点**：
  - 甲乙木、丑未土、子水午火，六者无金
  - 风后配合成金：甲子乙丑甲午乙未
  - 数之所合，变之所出
  - 乾坤合为泰，干支合生纳音
  - 干为君支为臣，合而为金

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_169]` `[trigger: 《路史》论纳音配合]` `[factor_trigger: lushi AND fenghou AND nayin_pairing AND numbers_transformations]` `[role: 主干]` 甲乙木，丑未土，子水而午火，六者无一金，而风后配合，乃以甲子、乙丑、甲午、乙未为之金。此出乎数者然也。数之所合，变之所由出也。 → 《三命通会》卷一#《路史》论纳音配合之理

- **详细解说**：
  此条引《路史》论纳音配合的数理原理。甲乙本属木，丑未本属土，子本属水，午本属火，这六个元素中没有一个属金，但风后（黄帝时代大臣）将它们配合，甲子、乙丑、甲午、乙未都成为金纳音。为什么？因为"数之所合，变之所由出"——通过数理配合产生新的属性变化。类比乾坤合为泰卦，天干（君）与地支（臣）配合产生纳音五行。这揭示了纳音不是简单的五行叠加，而是通过特殊的数理配合产生的"变"，体现了中国古代数术的深层智慧。

- **校勘与字词辨析（双语）**：
  - **中文**：《路史》为宋代罗泌撰。风后为黄帝时大臣。"数之所合"指数理配合规律。
  - **English**: "Lushi" (Road History) was written by Luo Bi in Song Dynasty; Fenghou was a minister under Yellow Emperor; "where numbers combine" refers to numerical combination principles."""
    normalized_text_zh: str = """"""
    subject: str = "路史论纳音配合之理"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_路史论纳音配合之理_001_L1",
    )
    version: str = "1.0.0"
