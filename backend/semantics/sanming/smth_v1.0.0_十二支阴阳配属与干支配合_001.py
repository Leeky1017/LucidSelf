"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228009
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
    semantic_id="smth_v1.0.0_十二支阴阳配属与干支配合_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十二支阴阳配属与干支配合(SemanticEntry):
    """
    - **原文（source_text）**：
  甲之干乃天之五行，以一阴一阳言之。子之支乃地之五行，以地之方隅言之，故子寅午申为阳，卯巳酉亥为阴。土居四维，王在四季之末。土有四，辰戌为阳，丑未为阴，...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲之干乃天之五行，以一阴一阳言之。子之支乃地之五行，以地之方隅言之，故子寅午申为阳，卯巳酉亥为阴。土居四维，王在四季之末。土有四，辰戌为阳，丑未为阴，故其数不同也。合而言之，十配十二，共成六十日，复六六而成岁。故经曰：天以六六之节，以成一岁。此之谓也。

- **分字分词释义**：
  - **天之五行**：天干的五行。
  - **地之方隅**：地支的方位。
  - **四维**：四个角位（东北、东南、西南、西北）。
  - **王在四季之末**：主管在四季末尾。
  - **土有四**：土有四个地支（辰戌丑未）。
  - **十配十二**：十天干配十二地支。
  - **六十日**：六十甲子。
  - **六六之节**：六个六十天的周期。

- **规范化释义（primary_lang_explained）**：
  甲等天干是天的五行，以一阴一阳来说。子等地支是地的五行，以地的方位来说，所以子寅午申为阳支，卯巳酉亥为阴支。土居四个角位，主管四季的末尾。土有四个地支，辰戌为阳土，丑未为阴土，所以其数不同。合并来说，十天干配十二地支，共成六十甲子，六个六十天循环成为一年。所以经书说：天以六个六十天的周期来成就一年。就是这个道理。

- **完整对等诠释（secondary_lang_full）**：
  The Stems like Jia are Heaven's Five Elements, spoken of in terms of one yin and one yang. The Branches like Zi are Earth's Five Elements, spoken of in terms of Earth's directional corners—thus Zi-Yin-Wu-Shen are yang; Mao-Si-You-Hai are yin. Earth occupies the four corners, governing the end of each of the four seasons. There are four Earth Branches: Chen-Xu are yang Earth; Chou-Wei are yin Earth; thus their numbers differ. Combining them: ten paired with twelve form sixty days; six cycles of sixty complete a year. Therefore the classics state: "Heaven uses six sixty-day periods to complete one year." This is the principle.

- **核心要点**：
  - 天干为天之五行（一阴一阳）
  - 地支为地之五行（方位）
  - 阳支：子寅午申（加辰戌阳土）
  - 阴支：卯巳酉亥（加丑未阴土）
  - 土居四维四季末，辰戌阳丑未阴
  - 十配十二成六十甲子
  - 六六之节成一岁（360天）

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_160]` `[trigger: 十二支阴阳配属]` `[factor_trigger: twelve_branches AND yinyang_attribution AND sixty_jiazi]` `[role: 主干]` 子寅午申为阳，卯巳酉亥为阴。土居四维，辰戌为阳，丑未为阴。十配十二，共成六十日。 → 《三命通会》卷一#十二支阴阳配属

- **详细解说**：
  此条总结十二支阴阳配属与干支配合原理。天干以阴阳属性分类，地支以方位分类。地支阴阳配属：子寅午申为四阳支（加辰戌阳土共六阳支），卯巳酉亥为四阴支（加丑未阴土共六阴支）。土特殊，居四个角位（辰东南、戌西北、丑东北、未西南），主管四季末尾，辰戌为阳土，丑未为阴土。十天干与十二地支配合，形成六十甲子循环。六个六十天（360天）为一年的基本周期。这揭示了干支体系的数理基础和时间循环规律。

- **校勘与字词辨析（双语）**：
  - **中文**："四维"指东北、东南、西南、西北四个角位。"六六之节"即360天，接近太阳年。
  - **English**: "Four corners" refers to Northeast, Southeast, Southwest, Northwest; "six sixty-day periods" equals 360 days, approximating a solar year."""
    normalized_text_zh: str = """"""
    subject: str = "十二支阴阳配属与干支配合"
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
        l1_anchor="smth_v1.0.0_十二支阴阳配属与干支配合_001_L1",
    )
    version: str = "1.0.0"
