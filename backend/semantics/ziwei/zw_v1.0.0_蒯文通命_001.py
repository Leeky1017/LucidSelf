"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699185
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
    semantic_id="zw_v1.0.0_蒯文通命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 蒯文通命(SemanticEntry):
    """
    - 分字分词释义：

  - **双禄朝垣**：禄存与化禄同时拱照命宫，主善谈兵。
  - **日月左右未宫加会**：太阳太阴左辅右彼在未宫会合，为奇格。
  - **命垣火宿**：命宫坐火性星曜，主...
    """
    
    original_text: str = """- 分字分词释义：

  - **双禄朝垣**：禄存与化禄同时拱照命宫，主善谈兵。
  - **日月左右未宫加会**：太阳太阴左辅右彼在未宫会合，为奇格。
  - **命垣火宿**：命宫坐火性星曜，主胆大敢为。
  - **大岁埋蛇**：大限行至巳宫不利，为凶险之限。
  - **太阴化忌**：乙年太阴星化忌，主凶亡。
  - **善谈兵**：长于兵略谋略，纵横辩论。
  - **阴男木三局**：蒯文通命盘的五行局数，木三局主生发辩才。

- **原文（source_text）**：  
  蒯文通命。阴男木三局。双禄朝垣，又无巨机，对宫相会，最善谈兵。日月左右，未宫加会，最为奇也。但命垣火宿，为人胆大。乙巳年二十五岁，大岁埋蛇。乙年太阴星化忌，故主凶亡。

- **规范化释义（primary_lang_explained）**：  
  蒯文通命属阴男木三局，双禄朝垣、日月左右未宫加会，最善谈兵。命垣火宿主胆大。乙巳年二十五岁，大岁埋蛇，太阴化忌，故凶亡。

- **完整对等诠释（secondary_lang_full）**：  
  Kuai Wentong's Yin male Wood Third chart has Double Salary facing court, Sun‑Moon Left‑Right converge at Wei—superb at military strategy. Life hosts Fire lodging, bold personality. At 25 in yi‑si year, major buries Snake. Taiyin transforms taboo, causing violent death.

- **核心要点**：  
  1. 双禄朝垣、日月左右加会，善谈兵。  
  2. 命垣火宿，主胆大。  
  3. 乙巳年大岁埋蛇、太阴化忌，为凶亡应期。

- **叙事素材（narrative_snippets）**：
  - **谈兵之才**："双禄朝垣，又无巨机，对宫相会，最善谈兵。日月左右，未宫加会，最为奇也"，蒯文通命主纵横辩论、长于兵略。
  - **火宿胆大**："但命垣火宿，为人胆大"，火宿坐命使其行事敢言敢为，亦易冒进。
  - **化忌凶年**："乙巳年二十五岁，大岁埋蛇。乙年太阴星化忌，故主凶亡"，大岁埋蛇配合太阴化忌，为英年早逝关口。
  - **现代应用**：善辩好谋者，在四化化忌与大岁埋蛇的年份，应避免高杠杆博弈与情绪性决策，防止聪明反被聪明误。"""
    normalized_text_zh: str = """"""
    subject: str = "蒯文通命"
    factor_refs: list = ['pattern_shuangluchaoyuan', 'pattern_dasuimaishe', 'sihua_taiyinji', 'source_ref', 'rel_kuaiwentong_001', 'pattern_shuangluchaoyuan', 'rel_kuaiwentong_002', 'pattern_dasuimaishe', 'rel_kuaiwentong_003', 'sihua_taiyinji', 'evi_kuaiwentong_001', 'sihua_taiyinji', 'rule_maishe_taiyinji', 'concept_double_salary', 'concept_taiyin_taboo']
    
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
        l1_anchor="zw_v1.0.0_蒯文通命_001_L1",
    )
    version: str = "1.0.0"
