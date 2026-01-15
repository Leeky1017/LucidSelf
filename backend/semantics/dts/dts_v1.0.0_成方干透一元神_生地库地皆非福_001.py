"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997346
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
    semantic_id="dts_v1.0.0_成方干透一元神_生地库地皆非福_001",
    book_id="dts",
    engine_id="bazi"
)
class 成方干透一元神生地库地皆非福(SemanticEntry):
    """
    - **原文（source_text）**：
  成方干透一元神，生地库地皆非福。

- 原注（原文注解）：
  　　如寅卯辰全，而又干透甲乙一元神，复又遇亥之生，未之库，决不发福，方不可混以局也。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  成方干透一元神，生地库地皆非福。

- 原注（原文注解）：
  　　如寅卯辰全，而又干透甲乙一元神，复又遇亥之生，未之库，决不发福，方不可混以局也。

- 分字分词释义：
  - 成方：三会方已成（如寅卯辰东方木）。
  - 干透：天干透出。
  - 一元神：同一五行之神（如甲乙为木之元神）。
  - 生地：五行长生之地（如木之生地亥）。
  - 库地：五行入库之地（如木之库未）。
  - 皆非福：都不利于发福。

- **规范化释义（primary_lang_explained）**：
  方已成而干再透同元神，又遇生地、库地相杂，反致不发。

- **次语种完整诠释（secondary_lang_full）**:  
  Once a directional Fang has been fully established and its primal spirit is already manifest on the stems, piling on yet more of the same element through birth and storage branches does not increase blessing. A pattern such as the eastern Fang Yin–Mao–Chen with Jia or Yi strongly exposed on the stems is already more than sufficient. If, on top of this, Hai as birthplace and Wei as storehouse are added and even a full trinity of the same element appears, the qi is layered so thickly that it becomes blocked rather than lively. What began as a clean, usable structure turns into congestion and delay. This rule warns that after a main direction has enough support, one should stop stacking identical reinforcements and instead leave room for circulation and balance."""
    normalized_text_zh: str = """"""
    subject: str = "成方干透一元神，生地库地皆非福。"
    factor_refs: list = ['chengfang', 'yuanshen_tougan', 'shengdi', 'kudi', 'guozai_zhicheng']
    
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
        l1_anchor="dts_v1.0.0_成方干透一元神_生地库地皆非福_001_L1",
    )
    version: str = "1.0.0"
