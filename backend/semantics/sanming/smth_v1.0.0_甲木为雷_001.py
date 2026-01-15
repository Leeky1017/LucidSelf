"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042561
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
    semantic_id="smth_v1.0.0_甲木为雷_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲木为雷(SemanticEntry):
    """
    - **原文（source_text）**：
  甲木为雷。雷者，阳气之嘘也，甲木属阳，故取象于雷焉。稽诸月令，仲春之月，雷乃发声，甲木旺，即其验也。况雷奋于地，木生于地，其理又无不同者。甲木至申而遂...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲木为雷。雷者，阳气之嘘也，甲木属阳，故取象于雷焉。稽诸月令，仲春之月，雷乃发声，甲木旺，即其验也。况雷奋于地，木生于地，其理又无不同者。甲木至申而遂绝，以雷声至申而渐收也。凡命属甲日，主喜值春天，或类象，或趋干，或遥巳，或拱贵，俱大吉；运不喜西方。经云：「木在春生，处世安然，必寿。」

- **分字分词释义**：
  - **雷者阳气之嘘**：雷为阳气鼓荡于地中而发声，象征阳木勃发之势。
  - **仲春之月雷乃发声**：以惊蛰雷鸣对应甲木在春令得旺。
  - **至申而绝**：雷声到申位渐收，喻甲木气至申而尽。

- **规范化释义（primary_lang_explained）**：
  本段以雷喻甲木：雷由地中阳气鼓荡而出，正如甲木在春令勃然而生。仲春雷动之时，恰是甲木最旺的阶段，所以命中甲日生于春天，多应生机充沛、气象安然。及至申位，雷声渐止，甲木之势亦随之而衰。行运不宜过往西方金地，以免木气过伤。

- **完整对等诠释（secondary_lang_full）**：
  This section likens Jia Wood to thunder: a sudden release of yang that has long been building inside the earth. Thunder bursts from below just as Jia Wood, the upright yang stem of Wood, pushes upward through the ground when spring is fully established. The mid‑spring thunder that shakes the season corresponds to Jia at its peak; by the time the qi moves to Shen, the sound fades and the force disperses. For people born on Jia days, having their main placements rooted in spring‑type branches or structures that echo spring—such as eastern directions, Wood bureaus, or indirect links to noble stars—is especially favourable, as it lets this “thunder qi” show as initiative, courage, and an easy sense of being at home in the world. Repeated movement toward the western Metal regions, by contrast, cuts and dries the Wood so that the same force becomes strain and depletion. The image teaches us to read Jia not only as growth, but as a decisive opening stroke whose success depends on timing and on whether there is soil and rain to receive what the thunder awakens."""
    normalized_text_zh: str = """"""
    subject: str = "甲木为雷"
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
        l1_anchor="smth_v1.0.0_甲木为雷_001_L1",
    )
    version: str = "1.0.0"
