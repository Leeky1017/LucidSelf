"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699814
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
    semantic_id="zw_v1.0.0_邓炼之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 邓炼之命(SemanticEntry):
    """
    - 分字分词释义：

  - **昌曲夹贵**：文昌、文曲夹住贵星或命宫，主文名与科第。
  - **左右朝垣**：左辅右彼朝拱命垣，主辅助与贵人扶持。
  - **双禄守照**：双禄星守照命局，主财...
    """
    
    original_text: str = """- 分字分词释义：

  - **昌曲夹贵**：文昌、文曲夹住贵星或命宫，主文名与科第。
  - **左右朝垣**：左辅右彼朝拱命垣，主辅助与贵人扶持。
  - **双禄守照**：双禄星守照命局，主财禄丰厚。
  - **连登科弟**：早年连续登科第取得功名。
  - **地网逢陀忌**：行运入地网并见陀罗化忌，主困局与突发阻截。
  - **擎羊天伤**：擎羊与天伤同临，主突发冲击与伤灾。
  - **倒寿**：原本可更长的寿元因重凶年份被提前截断。
  - **阳男水二局**：邓炼之命盘的五行局数，水二局主智慧文贵。

- **原文（source_text）**：  
  邓炼之命。阳男水二局。昌曲夹贵，左右朝垣，双禄守照，无不富贵。早年连登科弟，位至监察御史，转堕京卿。四十九岁，小限八地网逢陀忌，太岁擎羊、天伤，以致倒寿。

- **规范化释义（primary_lang_explained）**：  
  邓炼之命为阳男水二局，「昌曲夹贵，左右朝垣，双禄守照」，构成文昌、文曲夹命，左右辅弼朝垣，再加双禄守照的高文贵格局，一生多主科名连捷与清显官职。原文说「早年连登科弟」，并位至监察御史、京卿之职，体现典型由科第入仕、渐升京官的路径。  
  然而在四十九岁，小限行至地网之地并逢陀忌，是「地网 + 陀罗化忌」的困厄结构；同年太岁又见擎羊、天伤合击，是外在冲突与伤灾之象。吉格与重凶交会，令寿命被提前截断，形成「富贵而倒寿」的命例——并非寿元本极短，而是在特定年份被强行折减。

- **完整对等诠释（secondary_lang_full）**：  
  Deng Lian’s chart is that of a Yang Water native in the Second Configuration. With Wen Chang and Wen Qu flanking a noble star, Zuo‑You attending the court and a pair of Lu stars guarding, the pattern promises scholarly honours and refined office. The text notes "repeated early success in the examinations," leading to posts as Censor and then a high capital official—an archetypal path from degree‑holder to central government.  
  At forty‑nine, however, the minor period enters a Di‑Net‑type region and meets Tuo‑Ji, while the Annual Tai Sui brings Qing Yang and Tian Shang. This combination—"Earth Net with Tuo‑Ji" plus "Blade and Wound under Tai Sui"—creates a trap of entanglement and harm. Under such converging afflictions, his lifespan is "reversed" or shortened: he dies earlier than the underlying configuration would otherwise allow. The case illustrates a richly endowed literary‑noble chart whose life is cut short by a sharply configured year.

- **核心要点**：  
  1. 昌曲夹贵、左右朝垣、双禄守照，是连登科第、位至京卿的高文贵格。  
  2. 四十九岁小限入地网逢陀忌，太岁擎羊天伤并临，构成困局 + 冲击 + 伤灾的重凶年。  
  3. 命例呈现「富贵成就已立，却因一岁重凶而倒寿」的路径。"""
    normalized_text_zh: str = """"""
    subject: str = "邓炼之命"
    factor_refs: list = ['pattern_changqu_jiagui', 'pattern_zuoyou_chaoyuan', 'pattern_shuanglu_shouzhao', 'malefic_diwang_tuoji', 'malefic_qingyang_tianshang', 'result_daoshou']
    
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
        l1_anchor="zw_v1.0.0_邓炼之命_001_L1",
    )
    version: str = "1.0.0"
