"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228037
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
    semantic_id="smth_v1.0.0_纳音在风水命理中的应用_001",
    book_id="sanming",
    engine_id="bazi"
)
class 纳音在风水命理中的应用(SemanticEntry):
    """
    - **原文（source_text）**：
  圣人推之以入用，以分金六十位，定布于二十四位，以正五行为各宫之主，以六甲大五行为纬，察其分金胎养衰死之气，定其孤虚旺相之卦。内有戊己黛龟甲空亡，甲乙为...
    """
    
    original_text: str = """- **原文（source_text）**：
  圣人推之以入用，以分金六十位，定布于二十四位，以正五行为各宫之主，以六甲大五行为纬，察其分金胎养衰死之气，定其孤虚旺相之卦。内有戊己黛龟甲空亡，甲乙为补接之空，以是消息阴阳。凡立葬乘气、定命纳音，皆宗乎此。

- **分字分词释义**：
  - **分金六十位**：分金六十个方位。
  - **二十四位**：二十四山向。
  - **正五行**：天干地支本身的五行。
  - **六甲大五行**：六十甲子纳音五行。
  - **为纬**：作为经纬。
  - **分金胎养衰死**：方位上的胎养衰死状态。
  - **孤虚旺相**：孤虚旺相的卦象。
  - **空亡**：空亡位。
  - **补接之空**：补接空亡。
  - **消息阴阳**：推测阴阳变化。
  - **立葬乘气**：风水立向乘气。
  - **定命纳音**：命理定纳音。

- **规范化释义（primary_lang_explained）**：
  圣人将纳音推演用于实践，用分金六十个方位，确定布置于二十四个山向，以正五行作为各宫的主导，以六十甲子纳音五行作为经纬，观察其分金上胎养衰死的气，确定其孤虚旺相的卦象。其中有戊己旬的空亡，甲乙为补接的空亡，由此推测阴阳变化。凡是风水立向乘气、命理确定纳音，都以此为宗。

- **完整对等诠释（secondary_lang_full）**：
  Sages extended this into practical application, using sixty directional divisions, establishing arrangements across twenty-four mountains, taking the proper Five Elements as masters of each palace, using Sixty Jiazi Nayin Five Elements as warp and weft, examining the qi of gestation-nurturing-decline-death in directional divisions, determining hexagrams of isolation-emptiness-prosperity-phase. Within are Wu-Ji decade's void positions, with Jia-Yi as supplementary voids, thus investigating yin-yang transformations. All feng shui orientation and qi-riding, fate determination through Nayin, all take this as foundation.

- **核心要点**：
  - 纳音应用于实践：风水和命理
  - 分金六十位布于二十四山向
  - 正五行为主，纳音五行为纬
  - 察分金胎养衰死之气
  - 定孤虚旺相之卦
  - 空亡与补接

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_164]` `[trigger: 纳音在风水命理中应用]` `[factor_trigger: nayin_fengshui AND twenty_four_mountains AND directional_divisions]` `[role: 主干]` 圣人推之以入用，以分金六十位，定布于二十四位，以正五行为各宫之主，以六甲大五行为纬。 → 《三命通会》卷一#纳音在风水命理中的应用
  - 风水立葬、命理定命皆宗此

- **详细解说**：
  此条说明纳音理论的实际应用。圣人将六十甲子纳音推演到实践中：在风水学中，将六十个分金方位分布到二十四山向上，以天干地支本身的五行为主导，以纳音五行为辅助经纬，观察每个方位上的胎养衰死状态（生命周期），确定孤虚旺相的卦象（吉凶状态）。特别要注意空亡位（戊己旬的空亡）和补接空亡（甲乙的补接），由此推测阴阳消长变化。无论是风水学的立向乘气，还是命理学的定命纳音，都以此纳音体系为根本依据。这体现了纳音从理论到实践的完整应用体系。

- **校勘与字词辨析（双语）**：
  - **中文**："分金"是风水术语，指罗盘上的精确方位。"二十四位"即二十四山向。"空亡"指旬中无对应地支的空位。
  - **English**: "分金" (dividing gold) is a feng shui term for precise compass directions; "twenty-four positions" refers to twenty-four mountains; "void" (空亡) refers to empty positions in a decade without corresponding Branches."""
    normalized_text_zh: str = """"""
    subject: str = "纳音在风水命理中的应用"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_纳音在风水命理中的应用_001_L1",
    )
    version: str = "1.0.0"
