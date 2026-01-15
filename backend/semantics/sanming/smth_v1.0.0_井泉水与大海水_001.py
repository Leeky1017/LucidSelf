"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228199
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
    semantic_id="smth_v1.0.0_井泉水与大海水_001",
    book_id="sanming",
    engine_id="bazi"
)
class 井泉水与大海水(SemanticEntry):
    """
    - **原文（source_text）**：
  甲申乙酉，气息安静，子母同位，出而不穷，汲而不竭，乃曰井泉水。壬戌癸亥，天门之地，气归闭塞，水历遍而不趋，势归乎宁谧之位，来之不穷，纳之不溢，乃曰大海...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲申乙酉，气息安静，子母同位，出而不穷，汲而不竭，乃曰井泉水。壬戌癸亥，天门之地，气归闭塞，水历遍而不趋，势归乎宁谧之位，来之不穷，纳之不溢，乃曰大海水也。

- **分字分词释义**：
  - **气息安静**：气息安定平静。
  - **子母同位**：子水母金在同一位置。
  - **出而不穷**：流出而不穷尽。
  - **汲而不竭**：汲取而不枯竭。
  - **天门之地**：天门的位置（戌亥）。
  - **气归闭塞**：气归于闭塞状态。
  - **水历遍而不趋**：水流遍各处而不再前行。
  - **势归乎宁谧之位**：势头归于宁静安谧的位置。
  - **来之不穷纳之不溢**：来的不穷尽纳的不溢出。

- **规范化释义（primary_lang_explained）**：
  甲申乙酉，气息安定平静，子水母金在同一位置，流出而不穷尽，汲取而不枯竭，就叫井泉水。壬戌癸亥，天门的位置，气归于闭塞状态，水流遍各处而不再前行，势头归于宁静安谧的位置，来的不穷尽纳的不溢出，就叫大海水。

- **完整对等诠释（secondary_lang_full）**：
  Jiashen-Yiyou: qi-breath peaceful and quiet, child-Water and mother-Metal in same position, flowing out inexhaustibly, drawing without depletion, thus called Well-Spring Water. Renxu-Guihai: Heaven's Gate position, qi returning to sealed state, water having traversed everywhere no longer rushing forward, momentum returning to serene tranquil position, arriving inexhaustibly yet received without overflow, thus called Great-Ocean Water.

- **核心要点**：
  - 甲申乙酉：井泉水（气息安静，出而不穷）
  - 壬戌癸亥：大海水（天门之地，来之不穷纳之不溢）
  - 井泉水为水的静守涌泉
  - 大海水为水的归宿终极

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_184]` `[trigger: 井泉水与大海水]` `[factor_trigger: well_spring_water AND great_ocean_water AND nayin_water_final]` `[role: 主干]` 甲申乙酉，气息安静，子母同位，出而不穷，汲而不竭，乃曰井泉水。壬戌癸亥，天门之地，水历遍而不趋，势归乎宁谧之位，来之不穷，纳之不溢，乃曰大海水也。 → 《三命通会》卷一#井泉水与大海水

- **详细解说**：
  此条完成水纳音的解释。甲申乙酉为"井泉水"：申酉属金，金生水（子母同位），水在金地安静涌出，如井泉之水，源源不断但不泛滥，汲取不竭，这是水的静守状态。壬戌癸亥为"大海水"：戌亥为天门之地（西北），水气归于闭塞，水流遍天下最终归于大海，不再奔流，来多少容纳多少而不溢出，这是水的终极归宿。六种水纳音：涧下水（潜流）→大溪水（奔流）→长流水（持续）→天河水（高悬）→井泉水（涌泉）→大海水（归海），完整呈现水的一生循环。命理上，井泉水命格清净持久，大海水命格宽广包容。

- **校勘与字词辨析（双语）**：
  - **中文**："井泉水"指井中涌出的泉水。"子母同位"指水（子）与金（母）同在申酉。"天门之地"指戌亥西北方。"来之不穷纳之不溢"形容大海包容。
  - **English**: "Well-Spring Water" refers to spring water welling from wells. "Child-mother same position" means Water (child) and Metal (mother) both at Shen-You. "Heaven's Gate position" refers to Xu-Hai northwest. "Arriving inexhaustibly received without overflow" describes ocean's capacity."""
    normalized_text_zh: str = """"""
    subject: str = "井泉水与大海水"
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
        l1_anchor="smth_v1.0.0_井泉水与大海水_001_L1",
    )
    version: str = "1.0.0"
