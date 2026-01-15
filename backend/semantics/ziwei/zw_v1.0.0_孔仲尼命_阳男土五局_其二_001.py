"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.698958
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
    semantic_id="zw_v1.0.0_孔仲尼命_阳男土五局_其二_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 孔仲尼命阳男土五局其二(SemanticEntry):
    """
    - 分字分词释义：

  - **重复记载**：此条与第1条内容完全相同，为原书重复收录，可供版本考据。
  - **活禄逢迎**：同第1条，禄存与化禄同临或拱照命宫的极贵格局。
  - **天罗地网...
    """
    
    original_text: str = """- 分字分词释义：

  - **重复记载**：此条与第1条内容完全相同，为原书重复收录，可供版本考据。
  - **活禄逢迎**：同第1条，禄存与化禄同临或拱照命宫的极贵格局。
  - **天罗地网**：同第1条，辰戌两宫形成的束缚格局。
  - **文献价值**：两条命例内容相同，可用于不同底本之间的排比校勘。

- **原文（source_text）**：  
  孔仲尼命。阳男土五局。活禄逢迎，夫子文童冠世。辛亥年六十二岁，在陈绝粮。盖因太岁有劫空，小限逢天伤，七十三岁，小限在天罗，太岁入地网，戌生人有忌，故死。

- **规范化释义（primary_lang_explained）**：  
  此为孔子命例其二，内容与其一相同，为原书重复记载。阳男土五局，活禄逢迎格局，主文名冠世。六十二岁辛亥年困厄，七十三岁因天罗地网与戌忌叠加而寿终。

- **完整对等诠释（secondary_lang_full）**：  
  This is the second version of Confucius's chart, identical in content to the first—likely a duplicate entry in the original text. It reiterates that as a Yang male of Earth Fifth Configuration with the Active Salary Greeting pattern, he enjoyed supreme literary fame. Hardship struck at 62 and death at 73, when the Nets and Xu taboos converged.

- **核心要点**：  
  1. 与其一内容相同，为原书重复记载。  
  2. 可作为文献考据之参考。

- **叙事素材（narrative_snippets）**：
  - **重复命例**：同为「孔仲尼命（阳男土五局）」再记一条，提示原书在圣人命例部分存在重抄或异本并行的可能。
  - **对照校验**：两条命例内容相同，可用于不同底本之间的排比校勘，对比「活禄逢迎」「陈绝粮」「天罗地网」等关键语句是否有文字出入。
  - **现代应用**：实务解读时，可提醒读者区分「命例内容」与「版本差异」——命理判断仍以第一条为主，此条更多承担文献与版本说明的角色。"""
    normalized_text_zh: str = """"""
    subject: str = "孔仲尼命（阳男土五局·其二）"
    factor_refs: list = ['evi_kongzi2_001', 'flag_chongfujizai']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_孔仲尼命_阳男土五局_其二_001_L1",
    )
    version: str = "1.0.0"
