"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619797
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
    semantic_id="qtbj_v1.0.0_2__正月甲木_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2正月甲木寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  正月甲木，初春尚有余寒，得丙癸逢，富贵双全。癸藏丙透，名寒木向阳，主大富贵。倘风水不及，亦不失儒林俊秀。如无丙癸，平常人也。

- **分字分词释义*...
    """
    
    original_text: str = """- **原文（source_text）**：
  正月甲木，初春尚有余寒，得丙癸逢，富贵双全。癸藏丙透，名寒木向阳，主大富贵。倘风水不及，亦不失儒林俊秀。如无丙癸，平常人也。

- **分字分词释义**：
  - **正月**：农历一月 / 寅月 / 甲木临官之地
  - **尚有余寒**：还有残余寒气 / 初春气候 / 调候需火
  - **丙癸逢**：丙火与癸水同时出现 / 水火既济 / 富贵配置
  - **癸藏丙透**：癸水藏支、丙火透干 / 最佳配置 / 润根暖身两不误
  - **寒木向阳**：寒冷的木向着太阳 / 格局名称 / 大富贵之象
  - **风水不及**：祖荫环境不足 / 外在条件 / 降格但不失文才
  - **儒林俊秀**：读书人中的杰出者 / 文贵 / 次等富贵

- **规范化释义（primary_lang_explained）**：
  正月（寅月）的甲木，初春还有余寒，如果能得到丙火（太阳）和癸水（雨露）相逢，富贵双全。如果是癸水藏在地支，丙火透出天干，这叫“寒木向阳”格，主大富贵。如果风水（祖荫/环境）不够好，也不失为读书人中的俊秀之才。如果既没有丙火也没有癸水，就是普通人。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 1st Month (Tiger Month): Early Spring still has residual coldness. If it meets both Bing (Fire) and Gui (Water), wealth and nobility are both complete. If Gui is hidden and Bing is revealed, it is called "Cold Wood Facing the Sun", denoting great wealth and nobility. Even if the Feng Shui (background) is lacking, one remains a refined scholar. If there is neither Bing nor Gui, one is an ordinary person.

- **核心要点**：
  - **首要用神**：丙火（调候暖局）。
  - **次要用神**：癸水（滋润木根），但宜藏不宜透（防伤丙）。
  - **格局名称**：寒木向阳（Cold Wood Facing Sun）。

- **详细解说**：
  寅月甲木临官，身旺，但气候寒冷。
  - “寒木向阳”是此月最佳格局，必须丙火高透。
  - 癸水不可少（润根），但如果癸水透干克丙，就叫“不晴不雨”，格局下降。所以“癸藏丙透”最佳。
  - 这里的癸藏通常指丑中癸水或子中癸水。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_077]` `[trigger: 寅月甲木]` `[factor_trigger: month_yin AND tiangan_jia AND tiangan_bing AND tiangan_gui]` `[role: 主干]` 正月甲木，初春尚有余寒，得丙癸逢，富贵双全。 → 《穷通宝鉴·三春甲木》#3.2
  - `[ns_qttbj_078]` `[trigger: 寒木向阳]` `[factor_trigger: pattern_cold_wood_facing_sun AND gui_hidden_bing_revealed]` `[role: 主干依赖]` 癸藏丙透，名寒木向阳，主大富贵。 → 《穷通宝鉴·三春甲木》#3.2
  - `[ns_qttbj_079]` `[trigger: 寅月甲木]` `[factor_trigger: month_yin AND tiangan_jia AND pattern_cold_wood_facing_sun AND external_condition_weak]` `[role: 条件分支]` 倘风水不及，亦不失儒林俊秀。 → 《穷通宝鉴·三春甲木》#3.2
  - `[ns_qttbj_080]` `[trigger: 寅月甲木]` `[factor_trigger: month_yin AND tiangan_jia AND NOT tiangan_bing AND NOT tiangan_gui]` `[role: 例外处理]` 如无丙癸，平常人也。 → 《穷通宝鉴·三春甲木》#3.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 正月甲木（寅月）"
    factor_refs: list = ['pattern_cold_wood_facing_sun', 'bing_revealed', 'gui_hidden', 'refined_scholar']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__正月甲木_寅月_001_L1",
    )
    version: str = "1.0.0"
