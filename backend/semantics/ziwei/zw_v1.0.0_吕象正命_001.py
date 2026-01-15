"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699694
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
    semantic_id="zw_v1.0.0_吕象正命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 吕象正命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府拱朝**：紫微与天府拱照官垣，主最高等级之尊贵与统摄。
  - **科权双禄夹命**：科星、权星与双禄夹命，主功名权位与财禄极盛。
  - **左右重会**：左辅...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府拱朝**：紫微与天府拱照官垣，主最高等级之尊贵与统摄。
  - **科权双禄夹命**：科星、权星与双禄夹命，主功名权位与财禄极盛。
  - **左右重会**：左辅右彼多重加会，主贵人辅佐层层叠加。
  - **限步未济**：早年限运多阻未能顺利兑现格局之美。
  - **命劫空**：命垣带劫空星，主福报承载时间有限、易虚耗。
  - **小限陷地**：小限行于势弱受制之地，主根基被掘空与环境不利。
  - **阳男水二局**：吕象正命盘的五行局数，水二局主智慧权相。

- **原文（source_text）**：  
  吕象正命。阳男水二局。紫府拱朝，科权禄禄夹夹，左左右右，加加会会，富富贵贵，全全美美。限限步步未济，早年苦困，三十后方及第入相，命劫空，享福不久。大限到于火所天伤之地，小限行于陷地，故寿终焉。

- **规范化释义（primary_lang_explained）**：  
  吕象正命为阳男水二局，「紫府拱朝」加上科星、权星、禄星与双禄夹命，再配合多重左右辅弼，是极高规格的「紫府拱朝、科权双禄夹命、左右重重加会」格局，一生格局之美近乎「富贵全备」。  
  然而原文提到「限限步步未济，早年苦困」，说明早运多阻，虽格局高而现实一时难以承接；至三十岁后方才及第入相，正式登上权力与荣耀的舞台。命垣又带劫空之象，暗示福报虽厚但承载时间有限。晚年大限行至火所天伤之地，小限行于陷地，是「火伤 + 陷地」的组合，最终于此阶段寿终。整体呈现为「极高贵结构 + 早年坎坷 + 中年显贵 + 晚年在火伤陷地自然收束」的路径。

- **完整对等诠释（secondary_lang_full）**：  
  Lü Xiangzheng’s chart is that of a Yang Water native in the Second Configuration. Zi Wei and Tian Fu "beam towards the court," academic Ke, Power and Lu stars gather, Lu appears in double flanking positions, and Left and Right Assistants join repeatedly—"Zifu beaming, Ke‑Quan‑double Lu, Zuo‑You upon Zuo‑You"—forming an exceptionally opulent pattern. In principle it promises comprehensive wealth, status and support.  
  Yet "each step of the periods fails to arrive" in youth, indicating that early cycles are marked by frustration and hardship; only after thirty does he pass the examinations and "enter office as prime minister." With Jie‑Kong signatures at the Life, the enjoyment of such blessings is intrinsically time‑limited. In later life the major period moves into the fiery Tian Shang sector and the minor period into a "pit" or陷地, bringing wounding and undermining influences together. The text concludes that his life ends there, depicting a trajectory of delayed yet dazzling success followed by a relatively early natural closure.  

- **核心要点**：  
  1. 紫府拱朝、科权双禄夹命与多重左右加会，为极高标准的富贵权相格。  
  2. 早年限运未济而苦困，三十后方显格局本色，登堂入相，但因命带劫空而享福不久。  
  3. 晚年大限火所天伤，小限陷地，终以相对自然的寿终收束其富贵人生。"""
    normalized_text_zh: str = """"""
    subject: str = "吕象正命"
    factor_refs: list = ['pattern_zifu_gongchao', 'pattern_kequanlu_jiaming', 'pattern_zuoyou_chonghui', 'timing_xianbu_weiji', 'malefic_ming_jiekong', 'timing_xiaoxian_xiandi']
    
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
        l1_anchor="zw_v1.0.0_吕象正命_001_L1",
    )
    version: str = "1.0.0"
