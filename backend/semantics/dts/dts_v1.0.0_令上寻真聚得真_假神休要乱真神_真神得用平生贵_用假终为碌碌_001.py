"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997573
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
    semantic_id="dts_v1.0.0_令上寻真聚得真_假神休要乱真神_真神得用平生贵_用假终为碌碌_001",
    book_id="dts",
    engine_id="bazi"
)
class 令上寻真聚得真假神休要乱真神真神得用平生贵用假终为碌碌(SemanticEntry):
    """
    - **原文（source_text）**：
  令上寻真聚得真，假神休要乱真神。真神得用平生贵，用假终为碌碌人。

- 原注（原文注解）：
  　　如木火透者，生寅月聚得真，不要金水乱之，则真神得用...
    """
    
    original_text: str = """- **原文（source_text）**：
  令上寻真聚得真，假神休要乱真神。真神得用平生贵，用假终为碌碌人。

- 原注（原文注解）：
  　　如木火透者，生寅月聚得真，不要金水乱之，则真神得用，不为忌神所害，必然发贵。如金水猖狂，而用金水，是金水不得令，徒与木火不和，乃为碌碌平庸人矣。

- **规范化释义（primary_lang_explained）**：
  “真神”得令得助为上；“假神”搅局则伤。取用先辨真伪。

- 分字分词释义：
  - 令上：月令当权之处。
  - 寻真/聚得真：搜求并聚合真正有用之神。
  - 假神：不当令、不当势而扰局者。
  - 真神得用：得令得势且路径通达。
  - 用假：以假当真、以偏当正。
  - 碌碌人：才力不彰、难有大就。


- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 真假 | True-False (Zhen-Jia) | 真神与假神 | True God and False God | zhenjia | existing |
| 令上寻真 | Seek True in Season | 月令寻真 | Find True God in Month Command | lingshang_xunzhen | new_candidate |
| 聚得真 | Gather True | 真气聚集 | True Qi gathers | judezhen | new_candidate |
| 乱真神 | Confuse True God | 假乱真 | False confuses True | luan_zhenshen | new_candidate |
| 碌碌人 | Mediocre Person | 平庸之人 | Ordinary person | lulu_ren | existing |
| 得用 | In Use | 得力有用 | Effective and useful | deyong | existing |


- **次语种完整诠释（secondary_lang_full）**:  
  Zhen-Jia (True-False) theory: Seek the "True God" (Zhen-Shen) in the Month Command. Do not let "False Gods" (Jia-Shen) confuse the True. If True God is used, nobility follows. Using False God leads to a mediocre life (Lu-Lu Ren). "True" means in season and empowered; "False" means out of season and weak."""
    normalized_text_zh: str = """"""
    subject: str = "令上寻真聚得真，假神休要乱真神，真神得用平生贵，用假终为碌碌人。"
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
        l1_anchor="dts_v1.0.0_令上寻真聚得真_假神休要乱真神_真神得用平生贵_用假终为碌碌_001_L1",
    )
    version: str = "1.0.0"
