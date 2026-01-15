"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228360
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
    semantic_id="smth_v1.0.0_癸酉金性质_金之椎凿喜木及寅卯_001",
    book_id="sanming",
    engine_id="bazi"
)
class 癸酉金性质金之椎凿喜木及寅卯(SemanticEntry):
    """
    - **原文（source_text）**：
  癸酉金、金之椎凿，喜木及寅卯伏神，破字聋哑。

- **分字分词释义**：
  - **椎凿**：锤子和凿子。
  - **喜木及寅卯**：喜欢木以及...
    """
    
    original_text: str = """- **原文（source_text）**：
  癸酉金、金之椎凿，喜木及寅卯伏神，破字聋哑。

- **分字分词释义**：
  - **椎凿**：锤子和凿子。
  - **喜木及寅卯**：喜欢木以及寅卯方位。
  - **伏神**：伏神煞。

- **规范化释义（primary_lang_explained）**：
  癸酉金，是金制的锤子和凿子，喜欢木以及寅卯方位，忌讳伏神煞、破字煞、聋哑煞。

- **完整对等诠释（secondary_lang_full）**：
  Guiyou Metal is metal hammer-chisel tools, favoring Wood and Yin-Mao positions, avoiding Concealed-Spirit sha, Broken-Character sha, and Deaf-Mute sha.

- **核心要点**：
  - 癸酉为剑锋金，如椎凿
  - 喜木（有材可用）、寅卯
  - 忌伏神、破字、聋哑

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_204]` `[trigger: 癸酉金性质]` `[factor_trigger: guiyou_metal_tools AND favor_wood_yin_mao AND concealed_spirit]` `[role: 主干]` 癸酉金、金之椎凿，喜木及寅卯伏神，破字聋哑。 → 《三命通会》卷一#癸酉金性质

- **详细解说**：
  此条解释癸酉（剑锋金）的性质。癸酉纳音也是金，如锤子和凿子等工具，喜欢木（金克木，有材料可用），喜欢寅卯方位（木旺之地），但忌伏神煞、破字煞、聋哑煞等凶煞。椎凿之金需要木材才能发挥作用。

- **校勘与字词辨析（双语）**：
  - **中文**："椎凿"为工具，椎是锤子，凿是凿子。"寅卯"属木，为东方。"伏神"指隐伏之神。
  - **English**: "Hammer-chisel" are tools—hammer and chisel. "Yin-Mao" belong to Wood, eastern direction. "Concealed-Spirit" means hidden spirit."""
    normalized_text_zh: str = """"""
    subject: str = "癸酉金性质：金之椎凿喜木及寅卯"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_癸酉金性质_金之椎凿喜木及寅卯_001_L1",
    )
    version: str = "1.0.0"
