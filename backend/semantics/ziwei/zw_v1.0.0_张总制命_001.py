"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699899
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
    semantic_id="zw_v1.0.0_张总制命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 张总制命(SemanticEntry):
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
  - **同格异人**：相同命理结构在不同人物身上重复出现。
  - **内廷兵权**：由内廷或近臣掌握的军队指挥权。
  - **净身之恹**：指阔割或导致生殖机能丧失的疾患。
  - **阴男木三局**：张总制命盘的五行局数，木三局主生发权臣。

- **原文（source_text）**：  
  张总制命。阴男木三局。命坐紫微，武曲朝垣，文昌、文曲。加会天魁、天钺，酉亥二宫，相会紫微，得文曲扶佐，主掌兵权之职。但地劫疾厄忌星，卯垣合命，故有净身之恙。

- **规范化释义（primary_lang_explained）**：  
  张总制命为阴男木三局，原文给出的星曜结构与「暨太监命」完全相同：紫微坐命，武曲朝垣，文昌、文曲会魁钺，酉亥与紫微相会，主掌兵权之职；同时疾厄宫有地劫与忌星在卯垣合命，形成「净身之恙」的象征。不同在于称呼为「总制」，强调其在军政体系中的正式职衔与封号。  
  这体现出同一类强势格局可以在现实中投射为不同人物：既可以是以宦官身份掌兵的太监，也可以是受封总制的外廷武官，但二者都与内廷权力、兵权、以及身体代价高度纠缠。此命例由此补充了「同格异人」的观察维度。

- **完整对等诠释（secondary_lang_full）**：  
  Zhang, the Commander‑in‑Chief, has a Yin Wood chart whose configuration is textually identical to that of Ji the eunuch: Zi Wei in the Life palace, Wu Qu facing the court, Wen Chang/Wen Qu together with Kui‑Yue, and the You/Hai palaces linking back to Zi Wei, all indicating control of military power. Di Jie and taboo stars in the illness sector, tied to Mao and combining with the Life, again signal "an illness of bodily purification."  
  The difference lies in naming and social framing: here he appears as a formally titled "Zongzhi"—a high‑ranking commander—rather than explicitly as a eunuch. The case highlights how the same underlying pattern can manifest through different institutional roles, yet still revolve around inner‑court authority, military command and bodily sacrifice.

- **核心要点**：  
  1. 星曜结构与「暨太监命」同型，皆为紫微武曲魁钺掌兵权之格。  
  2. 疾厄宫地劫与忌星合命，同样指向「净身之恙」或身体重大代价。  
  3. 命例强调「同格异人」：制度角色不同，但权势与代价模式相近。"""
    normalized_text_zh: str = """"""
    subject: str = "张总制命"
    factor_refs: list = ['star_ziwei_shouming', 'star_wuqu_chaoyuan', 'pattern_changqu_kuiyue', 'principle_tongge_yiren', 'quality_neiting_bingquan', 'affliction_jingshen_zhi_yang']
    
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
        l1_anchor="zw_v1.0.0_张总制命_001_L1",
    )
    version: str = "1.0.0"
