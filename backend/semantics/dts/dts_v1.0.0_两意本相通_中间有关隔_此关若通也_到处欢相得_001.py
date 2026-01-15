"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997551
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
    semantic_id="dts_v1.0.0_两意本相通_中间有关隔_此关若通也_到处欢相得_001",
    book_id="dts",
    engine_id="bazi"
)
class 两意本相通中间有关隔此关若通也到处欢相得(SemanticEntry):
    """
    - **原文（source_text）**：
  两意本相通，中间有关隔，此关若通也，到处欢相得。

- 原注（原文注解）：
  　　阴阳之气，欲和合相生……若中间或被间阻、刑冲、劫占，皆为关隔，如局...
    """
    
    original_text: str = """- **原文（source_text）**：
  两意本相通，中间有关隔，此关若通也，到处欢相得。

- 原注（原文注解）：
  　　阴阳之气，欲和合相生……若中间或被间阻、刑冲、劫占，皆为关隔，如局中及岁运，得引用会合之神……乃为通关，关通则满局皆顺。

- 分字分词释义：
  - 两意：两股本可相生、相合之气，如财与官、身与印等；
  - 关隔：被间阻、刑冲、劫占等因素挡在中间；
  - 通关：以第三方之神协调之，使两意重新相通；
  - 欢相得：气机畅通、人事顺遂之象。

- **规范化释义（primary_lang_explained）**：
  通隔之理，就是“打通关节”。原本两意相通，却被中途的刑冲劫占所阻，使之不得相见；若能以会合、通关之神解除阻隔，两意既通，则全局皆顺。所谓“到处欢相得”，不止指某一处，而是整体气路一旦打通，各处皆随之而和。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 通隔 | Connect-Block (Tong-Ge) | 通关与阻隔 | Connecting and blocking | tongge | existing |
| 两意 | Two Intentions (Liang-Yi) | 两股气势 | Two distinct Qi forces | liangyi | new_candidate |
| 关隔 | Obstacle (Guan-Ge) | 阻隔之处 | Blocking point | guange | new_candidate |
| 通关 | Clear the Block (Tong-Guan) | 打通关节 | Clear the passage | tongguan | new_candidate |
| 欢相得 | Joyful Connection | 气畅人和 | Smooth flow and harmony | huanxiangde | new_candidate |
| 中间 | In Between | 阻隔之中介 | The middle blocking agent | zhongjian | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Tong-Ge (Connect-Block) theory: Two intentions (Liang-Yi) are naturally connected (e.g., Resource and Body, Wealth and Official), but blocked by an obstacle (Guan-Ge). If this obstacle is cleared (Tong-Guan), everything flows smoothly (Huan-Xiang-De). The key is identifying the block (e.g., Clash, Robbery) and the mediator."""
    normalized_text_zh: str = """"""
    subject: str = "两意本相通，中间有关隔，此关若通也，到处欢相得。"
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
        l1_anchor="dts_v1.0.0_两意本相通_中间有关隔_此关若通也_到处欢相得_001_L1",
    )
    version: str = "1.0.0"
