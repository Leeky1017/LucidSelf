"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699755
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
    semantic_id="zw_v1.0.0_和尚之命_阴男金四局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 和尚之命阴男金四局(SemanticEntry):
    """
    - 分字分词释义：

  - **极居酉地**：紫微等极星落于酉宫，主命局重心在酉。
  - **权禄扶持**：权星与禄星扶持命局，主有权位与财禄基础。
  - **杀破空劫巳酉会合**：杀、破、空、...
    """
    
    original_text: str = """- 分字分词释义：

  - **极居酉地**：紫微等极星落于酉宫，主命局重心在酉。
  - **权禄扶持**：权星与禄星扶持命局，主有权位与财禄基础。
  - **杀破空劫巳酉会合**：杀、破、空、劫等星在巳酉会合，主脱俗与刚烈气质。
  - **脱俗之僧**：以僧人身份脱离俗世，承载命局能量。
  - **空劫陀罗**：空劫与陀罗同会，主抽空与割裂。
  - **丧门天哭**：丧礼与哀伤相关星曜，主悲事与精神打击。
  - **阴男金四局**：此和尚命盘的五行局数，金四局主刚断出家。

- **原文（source_text）**：  
  和尚之命。阴男金四局。极居酉地，权禄扶持，杀破空劫，巳酉相会合，多为脱俗之僧。大限到本身，又加空劫陀罗，小限四十三，丧门、天哭、太岁大限相冲，是为不美，故死于是年。

- **规范化释义（primary_lang_explained）**：  
  此命为阴男金四局，「极居酉地」暗示命局重心落在酉宫，权星、禄星扶持，加上杀破空劫等星在巳酉会合，既带武职与决断性，又明显指向脱俗之僧。「多为脱俗之僧」表明其以僧人角色承载这些能量。  
  大限行到本命之地，再加空劫与陀罗同会，是原有结构被抽空与割裂之象；四十三岁小限又逢丧门、天哭并与太岁、大限相冲，是「空劫陀罗 + 丧门天哭 + 太岁冲限」的多重重凶。此时既有外界冲击，也有内心悲苦与能量流失，故于四十三岁死亡。

- **完整对等诠释（secondary_lang_full）**：  
  This second monk’s chart is that of a Yin Metal native in the Fourth Configuration. Centered in the You branch with Power and Lu supporting, and with martial, disruptive and void stars (Sha, Po, Kong, Jie) meeting between Si and You, the pattern is forceful yet detached from ordinary life; the text notes that such charts "often belong to monks who have left the world."  
  When the major period returns to the natal sector and emptiness with Tuo Luo join, the base is cut and hollowed. At forty‑three, the minor period meets Sang Men and Tian Ku, while Tai Sui and the major period form冲 aspects, layering grief, loss and collision—"Kong‑Tuo plus Sang‑Ku with Tai Sui striking the limits." Under this convergence the native dies. The example shows a renunciant whose strong, even harsh energies find expression in monastic life but are ultimately overwhelmed by a heavily afflicted year.

- **核心要点**：  
  1. 权禄扶持、杀破空劫巳酉会合，是具武性与决断力的出家僧格。  
  2. 大限回本命并加空劫陀罗，小限四十三逢丧门、天哭与太岁冲击，为多重重凶。  
  3. 命例呈现「脱俗僧人在重凶交加之年身亡」的路径。"""
    normalized_text_zh: str = """"""
    subject: str = "和尚之命（阴男金四局）"
    factor_refs: list = ['pattern_ji_ju_you', 'pattern_quanlu_fuchi', 'pattern_shapo_kongjie_siyou', 'quality_tuosu_zhiseng', 'malefic_kongjie_tuoluo', 'malefic_sangmen_tianku']
    
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
        l1_anchor="zw_v1.0.0_和尚之命_阴男金四局_001_L1",
    )
    version: str = "1.0.0"
