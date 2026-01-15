"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227544
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
    semantic_id="smth_v1.0.0_甲乙_春木生发之名义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲乙春木生发之名义(SemanticEntry):
    """
    - **原文（source_text）**：
  是以东方甲乙，南方丙丁，西方庚辛，牝方壬癸，中央戊巳，五行之位也。盖甲乙其位木，得春之令，甲乃阳内而阴尚包之。乙者，阳过中，然未得正方。

- 分字分...
    """
    
    original_text: str = """- **原文（source_text）**：
  是以东方甲乙，南方丙丁，西方庚辛，牝方壬癸，中央戊巳，五行之位也。盖甲乙其位木，得春之令，甲乃阳内而阴尚包之。乙者，阳过中，然未得正方。

- 分字分词释义：
  - **东方甲乙**：甲乙配东方与春令，主木气初生与渐长。
  - **甲乃阳内而阴尚包之**：甲像刚出土的芽，阳气在内，外面尚被阴包裹。
  - **乙者，阳过中，未得正方**：乙为弯曲之木，阳气已偏强，却尚未端正定方。

- **规范化释义（primary_lang_explained）**：
  甲乙安在东方，主春木之气。甲像破土而出的第一茎嫩芽，阳气在内鼓动，外表尚柔弱；乙则像已经抽长而略带弯曲的柔枝，阳气已显，但尚未端直定型。二者一刚一柔，共同描画了春木从萌芽到初长的阶段。

- **完整对等诠释（secondary_lang_full）**：

  Jia and Yi are placed in the East and govern the Qi of spring Wood. Jia Wood is like the very first shoot breaking through the soil: Yang force is gathering inside while the outside still appears soft and wrapped in Yin. Yi Wood is like the branch that has already grown out and begun to bend: Yang has passed the midpoint and is visible, yet has not fully straightened and set its direction. One is firm, the other supple; together they sketch the passage from germination to early extension in spring growth. In charts this allows us to distinguish between an initiating, spearhead type of Wood Qi (Jia Wood) and a harmonising, adaptive type (Yi Wood) instead of treating all Wood as a single undifferentiated tendency."""
    normalized_text_zh: str = """"""
    subject: str = "甲乙：春木生发之名义"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_甲乙_春木生发之名义_001_L1",
    )
    version: str = "1.0.0"
