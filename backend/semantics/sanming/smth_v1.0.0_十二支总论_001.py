"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227970
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
    semantic_id="smth_v1.0.0_十二支总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十二支总论(SemanticEntry):
    """
    - **原文（source_text）**：
  夫清阳为天，五行彰而十干立；浊阴为地，八方定而十二支分。运移气迁，岁岁而盈虚应纪；上升下降，物物而变化可期。所以支干配合，共臻妙用矣。

- **分字...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫清阳为天，五行彰而十干立；浊阴为地，八方定而十二支分。运移气迁，岁岁而盈虚应纪；上升下降，物物而变化可期。所以支干配合，共臻妙用矣。

- **分字分词释义**：
  - **清阳为天**：清轻之阳气为天。
  - **浊阴为地**：浊重之阴气为地。
  - **五行彰**：五行显彰。
  - **八方定**：八个方位确定。
  - **运移气迁**：运转移动，气候变迁。
  - **盈虚应纪**：盈满虚损应合纪律。
  - **上升下降**：天气上升地气下降。
  - **共臻妙用**：共同达到妙用。

- **规范化释义（primary_lang_explained）**：
  清轻的阳气为天，五行显彰而十天干建立；浊重的阴气为地，八个方位确定而十二地支分布。运转移动气候变迁，年年盈满虚损应合纪律；天气上升地气下降，万物变化可以预期。所以天干地支配合，共同达到妙用。

- **完整对等诠释（secondary_lang_full）**：
  Clear yang forms Heaven—the Five Elements manifest and the Ten Stems are established; turbid yin forms Earth—the Eight Directions are fixed and the Twelve Branches are distributed. With cycles shifting and qi transforming, year by year fullness and depletion follow their pattern; with ascent and descent, thing by thing transformations can be anticipated. Thus Stems and Branches combine to achieve wondrous application together.

- **核心要点**：
  - 清阳为天立十干，浊阴为地分十二支
  - 五行彰显，八方确定
  - 运移气迁，盈虚应纪
  - 上升下降，变化可期
  - 干支配合，共臻妙用

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_155]` `[trigger: 十二支总论]` `[factor_trigger: twelve_branches AND heaven_earth_correspondence]` `[role: 主干]` 清阳为天，五行彰而十干立；浊阴为地，八方定而十二支分。支干配合，共臻妙用矣。 → 《三命通会》卷一#十二支总论

- **详细解说**：
  此条为"论十二支名字之义"总论，对应前文"论十干"开篇。清轻的阳气上升为天，五行在天上显彰，形成十天干；浊重的阴气下降为地，八个方位（八卦方位）确定，形成十二地支。天地既分，运转移动不停，气候变迁有序，年年盈虚应合纪律；天气上升地气下降交互作用，万物的变化可以预期。天干地支相互配合，形成完整的干支体系，达到推测天时、预知变化的妙用。这揭示了十二支与十干的对应关系：干属天清阳，支属地浊阴；干彰五行，支定八方。

- **校勘与字词辨析（双语）**：
  - **中文**："清阳"指轻清之阳气，"浊阴"指重浊之阴气。"八方"指八卦八个方位。"盈虚"指盈满与虚损。
  - **English**: "Clear yang" refers to light and clear yang qi; "turbid yin" refers to heavy and turbid yin qi; "Eight Directions" refers to the eight trigram directions; "fullness-depletion" refers to abundance and scarcity."""
    normalized_text_zh: str = """"""
    subject: str = "十二支总论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_十二支总论_001_L1",
    )
    version: str = "1.0.0"
