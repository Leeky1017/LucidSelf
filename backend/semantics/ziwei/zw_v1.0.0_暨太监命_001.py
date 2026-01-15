"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699873
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
    semantic_id="zw_v1.0.0_暨太监命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 暨太监命(SemanticEntry):
    """
    - 分字分词释义：

  - **命坐紫微**：紫微帝星坐守命宫，主至高尊贵。
  - **武曲朝垣**：武曲星朝拱官垣，主武职与财权。
  - **文昌文曲加会天魁天钺**：文昌文曲与天魁天钺同会，...
    """
    
    original_text: str = """- 分字分词释义：

  - **命坐紫微**：紫微帝星坐守命宫，主至高尊贵。
  - **武曲朝垣**：武曲星朝拱官垣，主武职与财权。
  - **文昌文曲加会天魁天钺**：文昌文曲与天魁天钺同会，主文采与贵人扶持。
  - **掌兵权之职**：主掌兵权与军事要职。
  - **地劫疾厄忌星**：地劫与忌星落于疾厄相关宫位，主身体严重损害。
  - **净身之恹**：指阐割或导致生殖机能丧失的疾患。
  - **阳男木三局**：暨太监命盘的五行局数，木三局主生发权臣。

- **原文（source_text）**：  
  暨太监命。阳男木三局。命坐紫微，武曲朝垣，文昌、文曲加会天魁、天钺，酉亥二宫，相会紫微，得文曲扶佐，主掌兵权之职。但地劫疾厄忌星，卯垣合命，故有净身之恙。

- **规范化释义（primary_lang_explained）**：  
  暨太监命为阳男木三局，「命坐紫微，武曲朝垣」主帝星坐命，武曲朝拱，多掌武职与要权；又得文昌、文曲会天魁、天钺，酉亥二宫与紫微相会，形成「紫微 + 武曲 + 文昌文曲 + 魁钺」的强势权贵格，主掌兵权与机密事务，是典型内廷权臣的结构。  
  然而「地劫疾厄忌星，卯垣合命」，说明在疾厄与特定宫位上有地劫与忌星相合，对身体某部分形成不可逆的损伤。古书以「净身之恙」指阉割或相关疾患，命主因此以太监身份出入内廷，在牺牲肉身完整性的前提下取得极高权势——这是「权极而身有缺」的命局样本。

- **完整对等诠释（secondary_lang_full）**：  
  Ji the eunuch’s chart is that of a Yang Wood native in the Third Configuration. Zi Wei sits in the Life palace, Wu Qu faces the court, and Wen Chang/Wen Qu combine with Tian Kui and Tian Yue; You and Hai palaces connect back to Zi Wei with further literary support. This "Zi Wei + Wu Qu + Chang‑Qu + Kui‑Yue" array is typical of powerful inner‑court officials who control military or strategic authority.  
  Yet Di Jie and taboo stars in the illness sector, linked with the Mao branch that combines with the Life palace, mark a severe and irreversible bodily affliction. The phrase "an illness of purification of the body" alludes to castration. The destiny therefore describes someone who, through becoming a eunuch, gains intimate access to the palace and rises to command troops—a life of extreme power purchased at the cost of bodily wholeness.

- **核心要点**：  
  1. 紫微坐命、武曲朝垣并配文昌文曲、魁钺，是典型掌兵权的内廷权臣格。  
  2. 地劫与忌星在疾厄相关宫位合命，象征「净身之恙」，以牺牲身体完整换取路径。  
  3. 命例凸显「权势与身体代价」的交换结构：位极人臣，却为太监之身。"""
    normalized_text_zh: str = """"""
    subject: str = "暨太监命"
    factor_refs: list = ['star_ziwei_shouming', 'star_wuqu_chaoyuan', 'pattern_changqu_kuiyue', 'result_zhangbingquan', 'malefic_dijie_jie_ji', 'affliction_jingshen_zhi_yang']
    
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
        l1_anchor="zw_v1.0.0_暨太监命_001_L1",
    )
    version: str = "1.0.0"
