"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227906
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
    semantic_id="smth_v1.0.0_王氏进一步质疑历法源头_001",
    book_id="sanming",
    engine_id="bazi"
)
class 王氏进一步质疑历法源头(SemanticEntry):
    """
    - **原文（source_text）**：
  天地之运，如环无端，运周一元，磨硙之转，独不再始乎？日周十二时，天之运独不再子乎？一元之上，安知其不有一元耶？况历元之度，牛斗之变，岁差远矣，后世之历...
    """
    
    original_text: str = """- **原文（source_text）**：
  天地之运，如环无端，运周一元，磨硙之转，独不再始乎？日周十二时，天之运独不再子乎？一元之上，安知其不有一元耶？况历元之度，牛斗之变，岁差远矣，后世之历，各自为据，以求合时尔。古历之法，随世亡矣，安能筭而合之？

- **分字分词释义**：
  - **如环无端**：像圆环没有端点。
  - **一元**：一个大周期（129600年）。
  - **磨硙之转**：磨盘的旋转。
  - **再子**：再次回到子时。
  - **牛斗之变**：牛宿斗宿位置的变化。
  - **岁差**：天文岁差，星辰位置的变化。
  - **各自为据**：各自设定依据。

- **规范化释义（primary_lang_explained）**：
  天地运行就像圆环没有端点，运转完一个大周期（一元），就像磨盘转动，难道不会再次开始吗？日行十二时辰周而复始，天的运行难道不会再次回到子时吗？一元之上，怎么知道没有另一个更大的元呢？何况历法元年的设定、牛宿斗宿的位置变化，岁差相距已经很远，后世的历法各自设定依据，只是为了符合当时罢了。古代历法已经随着时代失传，怎么能推算并符合呢？

- **完整对等诠释（secondary_lang_full）**：
  The operation of heaven and earth is like a ring without end. After completing one Great Cycle (Yuan), like a millstone's rotation, would it not begin again? The day cycles through twelve hours repeatedly; would heaven's operation not return to Zi again? Above one Yuan, how can we know there is not another Yuan? Moreover, regarding calendar epoch calculations and the shifts of Ox and Dipper constellations, the precession has progressed far. Later calendars each establish their own basis merely to fit their times. Ancient calendar methods have been lost with their ages—how can we calculate and match them?

- **核心要点**：
  - 天地运行如环无端，循环往复
  - 一元之上可能还有更大的元
  - 天文岁差使古今星位变化巨大
  - 后世历法各自为据，无法还原古法
  - 古历已失传，无法精确考证

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_146]` `[trigger: 王氏质疑历法源头]` `[factor_trigger: cyclic_time AND precession AND ancient_methods_lost]` `[role: 主干]` 天地之运，如环无端。一元之上，安知其不有一元耶？历元之度，牵斗之变，岁差远矣。古历之法，随世亡矣。 → 《三命通会》卷一#王氏进一步质疑历法源头

- **详细解说**：
  王洙继续深化质疑，提出循环往复的时间观。天地运行像圆环无端，一元（大周期）结束后会再次开始，如同磨盘转动、日行十二时般周而复始。更重要的是，一元之上可能还有更大的元，时间起点无法确定。他提出天文观测问题：牛斗等星宿的位置因岁差（地轴进动）已发生巨大变化，古今星象不同，后世历法各自设定起点以符合当时，但古代历法已失传，无法精确还原和考证。这是更深层的怀疑论：既然时间循环无端、星象变迁、古法失传，如何确定甲子的真正起源？

- **校勘与字词辨析（双语）**：
  - **中文**："一元"为邵雍元会运世说中的大周期（129600年）。"岁差"指地轴进动导致的星位变化，约72年移动1度。
  - **English**: "One Yuan" is a Great Cycle of 129,600 years in Shao Yong's system; "precession" refers to the shift in star positions due to axial precession, approximately 1 degree per 72 years."""
    normalized_text_zh: str = """"""
    subject: str = "王氏进一步质疑历法源头"
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
        l1_anchor="smth_v1.0.0_王氏进一步质疑历法源头_001_L1",
    )
    version: str = "1.0.0"
