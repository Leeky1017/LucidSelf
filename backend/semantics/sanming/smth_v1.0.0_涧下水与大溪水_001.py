"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228179
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
    semantic_id="smth_v1.0.0_涧下水与大溪水_001",
    book_id="sanming",
    engine_id="bazi"
)
class 涧下水与大溪水(SemanticEntry):
    """
    - **原文（source_text）**：
  丙子丁丑，何以取象涧下水？盖气未通济，高段非水流之所，卑湿乃水就之乡，由地中行，故曰涧下水。甲寅乙卯，气出阳明，水势恃源，东流滔注，其势浸大，故曰大溪...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙子丁丑，何以取象涧下水？盖气未通济，高段非水流之所，卑湿乃水就之乡，由地中行，故曰涧下水。甲寅乙卯，气出阳明，水势恃源，东流滔注，其势浸大，故曰大溪水。

- **分字分词释义**：
  - **涧下水**：山涧下的水。
  - **气未通济**：气还未通畅济达。
  - **高段非水流之所**：高处不是水流的地方。
  - **卑湿乃水就之乡**：低湿才是水聚集的地方。
  - **由地中行**：从地下流动。
  - **气出阳明**：气出于阳明之地。
  - **水势恃源**：水势依仗源头。
  - **东流滔注**：向东奔流注入。
  - **其势浸大**：其势渐渐壮大。

- **规范化释义（primary_lang_explained）**：
  丙子丁丑，为什么取象为涧下水？因为气还未通畅济达，高处不是水流的地方，低湿处才是水聚集的地方，从地下流动，所以叫涧下水。甲寅乙卯，气出于阳明之地，水势依仗源头，向东奔流注入，其势渐渐壮大，所以叫大溪水。

- **完整对等诠释（secondary_lang_full）**：
  Bingzi-Dingchou, why symbolize Stream-Beneath Water? Because qi not yet flowing freely, high ground is not where water flows, low dampness is where water gathers, flowing through earth's interior, thus called Stream-Beneath Water. Jiayin-Yimao: qi emerging from yang-bright, water's force relying on source, flowing eastward in torrents, its momentum gradually enlarging, thus called Great-Creek Water.

- **核心要点**：
  - 丙子丁丑：涧下水（气未通济，由地中行）
  - 甲寅乙卯：大溪水（气出阳明，东流滔注）
  - 涧下水为水的初始潜流
  - 大溪水为水的奔腾壮大

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_182]` `[trigger: 涧下水与大溪水]` `[factor_trigger: stream_beneath_water AND great_creek_water AND nayin_water_initial]` `[role: 主干]` 丙子丁丑，何以取象涧下水？盖气未通济，卑湿乃水就之乡，由地中行，故曰涧下水。甲寅乙卯，气出阳明，水势恃源，东流滔注，其势浸大，故曰大溪水。 → 《三命通会》卷一#涧下水与大溪水

- **详细解说**：
  此条开始解释水纳音。丙子丁丑为"涧下水"：子为水旺之地，丑为土旺之地，水气尚未通达，不在高处流淌，而是在低湿的山涧地下潜行，这是水的初始阶段，如地下水、涧流水。甲寅乙卯为"大溪水"：寅卯属木旺之地（春季），水出阳明（春阳），水势得源头之力，向东奔流，势头渐大如溪流，从涧下水（潜流）到大溪水（奔流），体现了水从隐藏到显露、从微弱到壮大的过程。命理上，涧下水命格较弱但有韧性，大溪水命格活跃有力。

- **校勘与字词辨析（双语）**：
  - **中文**："涧下水"指山涧地下之水。"气未通济"指水气未能通达流通。"卑湿"指低洼潮湿之地。"阳明"指春天阳气明朗。"滔注"形容水流汹涌。
  - **English**: "Stream-Beneath Water" refers to underground water in mountain streams. "Qi not flowing freely" means water qi cannot flow smoothly. "Low dampness" refers to low-lying damp areas. "Yang-bright" means spring's bright yang qi. "Torrents" describes surging water flow."""
    normalized_text_zh: str = """"""
    subject: str = "涧下水与大溪水"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_涧下水与大溪水_001_L1",
    )
    version: str = "1.0.0"
