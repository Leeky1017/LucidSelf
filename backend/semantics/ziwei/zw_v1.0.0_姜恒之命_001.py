"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699373
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
    semantic_id="zw_v1.0.0_姜恒之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 姜恒之命(SemanticEntry):
    """
    - 分字分词释义：

  - **双禄加会**：禄存与化禄同会命宫，主富贵。
  - **左右同宫**：左辅右彼同在一宫，主终身福厚。
  - **空劫身命**：地劫天空在身命，主寿年难长。
  - ...
    """
    
    original_text: str = """- 分字分词释义：

  - **双禄加会**：禄存与化禄同会命宫，主富贵。
  - **左右同宫**：左辅右彼同在一宫，主终身福厚。
  - **空劫身命**：地劫天空在身命，主寿年难长。
  - **天伤夹地**：天伤星夹守地网，主凶险。
  - **病耗相临**：病符大耗同临，主疾病耗损。
  - **子生忌寅限**：子年生人不宜寅岁限。
  - **阳男土五局**：姜恒命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  姜恒之命。阳男土五局。双禄加会，无不富贵，左右同宫，终身福厚。空劫身命，寿年难长。大限入于天伤夹地，小限相冲。丙寅年太岁病耗相临，且子生人不宜寅岁限，故死于是年。

- **规范化释义（primary_lang_explained）**：  
  姜恒命属阳男土五局，双禄加会、左右同宫，主富贵福厚。然空劫在身命，寿年难长。大限入天伤夹地，小限相冲，丙寅年太岁病耗相临，子生人不宜寅岁限，故死于是年。

- **完整对等诠释（secondary_lang_full）**：  
  Jiang Heng's Yang male Earth Fifth chart has Double Salary converge, Left‑Right same palace—wealth and lifelong blessings. But Void‑Robbery at Body‑Life, short lifespan. Major at Wound flanks Earth, minor clashes. Bing‑yin year Tai Sui with Illness‑Depletion; Zi natives shouldn't have Yin periods. Death that year.

- **核心要点**：  
  1. 双禄加会、左右同宫，主富贵福厚。  
  2. 空劫身命，寿年难长。  
  3. 天伤夹地、子生忌寅限，为死亡应期。

- **叙事素材（narrative_snippets）**：
  - **双禄左右**："双禄加会，无不富贵，左右同宫，终身福厚"，姜恒命主衣食丰足、出身不凡。
  - **空劫折寿**："空劫身命，寿年难长"，身命同带空劫，预示福厚而短寿的结构缺陷。
  - **病耗岁限**："大限入于天伤夹地，小限相冲。丙寅年太岁病耗相临，且子生人不宜寅岁限"，病耗加寅岁忌限，为具体死亡年份。
  - **现代应用**：富贵而体质薄弱的命局，在病耗与生年忌限叠加时，更要重视体检与慢病管理，不宜在该年承担高风险项目。"""
    normalized_text_zh: str = """"""
    subject: str = "姜恒之命"
    factor_refs: list = ['pattern_kongjieshenming', 'pattern_binghaoxianglin', 'taboo_zishengyinxian', 'source_ref', 'rel_jiangheng_001', 'pattern_shuangluzuoyou', 'rel_jiangheng_002', 'pattern_kongjieshenming', 'rel_jiangheng_003', 'taboo_zishengyinxian', 'evi_jiangheng_001', 'taboo_zishengyinxian', 'rule_kongjie_yinxian', 'concept_double_salary', 'concept_void_body_life']
    
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
        l1_anchor="zw_v1.0.0_姜恒之命_001_L1",
    )
    version: str = "1.0.0"
