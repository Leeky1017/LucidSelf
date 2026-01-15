"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699891
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
    semantic_id="zw_v1.0.0_胡总制命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 胡总制命(SemanticEntry):
    """
    - 分字分词释义：

  - **科科权权拱命**：多重科星与权星守照命宫，权名并重。
  - **命紫紫府府**：紫微与天府同来守照命宫，主极高尊贵。
  - **朝垣左右加会**：官垣得左右辅彼加...
    """
    
    original_text: str = """- 分字分词释义：

  - **科科权权拱命**：多重科星与权星守照命宫，权名并重。
  - **命紫紫府府**：紫微与天府同来守照命宫，主极高尊贵。
  - **朝垣左右加会**：官垣得左右辅彼加会，主辅佐有力。
  - **羊火**：擎羊与火星同见，主猛烈冲突与事故。
  - **贪廉**：贪狼与廉贞同见，主欲望与刑杀能量叠加。
  - **不得其死**：死法偏离自然寿终，常与战祸或横事相关。
  - **阳男土五局**：胡总制命盘的五行局数，土五局主厚重威武。

- **原文（source_text）**：  
  胡总制命。阳男土五局。科科权权拱命，命紫紫府府，朝垣左右加会，得此四局，宜居威武之职，但见羊火，更命遇贪廉，故终不得其死。

- **规范化释义（primary_lang_explained）**：  
  胡总制命为阳男土五局，「科科权权拱命」指科星、权星多重守照命宫，「命紫紫府府」则说明紫微、天府同来朝拱；再加左右辅弼加会，是集科、权、紫府与左右于一身的重量级权贵格局，宜居总制等威武之职。  
  然而命中也见「羊火」与「贪廉」，意味着擎羊、火星及贪狼、廉贞等星曜形成烈性与偏锋结构。原文言「故终不得其死」，暗示其结局多半非自然寿终，而是战祸、政变或意外横死。此命格因此呈现「权势极重而死法偏烈」的路径：在权位巅峰时，凶星组合改写寿命收束方式。

- **完整对等诠释（secondary_lang_full）**：  
  Hu, the Commander‑in‑Chief, is a Yang Earth native in the Fifth Configuration. Multiple Ke and Quan stars "surround" the Life, while Zi Wei and Tian Fu also attend; Left and Right Assistants complete the picture. These four pillars—academia, authority, imperial favour and close attendants—form a formidable structure suited to supreme military or regional command.  
  Yet Yang Blade and Huo Xing, together with Tan Lang and Lian Zhen, introduce fiery, hungry and transgressive tendencies. The text concludes that "he does not end with a natural death," hinting at violent death in battle, political overthrow or catastrophic incident. The chart thus exemplifies a destiny in which immense command power and resources coexist with an intense, non‑peaceful ending.

- **核心要点**：  
  1. 科权叠拱配紫府与左右，是「总制」级别的重权武职格。  
  2. 羊火与贪廉同见，使得权势与资源被放置在高烈度风险环境中。  
  3. 结局「不得其死」，展示权贵命中「高位易招横祸」的一面。"""
    normalized_text_zh: str = """"""
    subject: str = "胡总制命"
    factor_refs: list = ['pattern_kequan_gongming', 'pattern_ziwei_tianfu_ming', 'pattern_chaoyuan_zuoyou', 'malefic_yanghuo', 'malefic_tanlian', 'result_bude_qisi']
    
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
        l1_anchor="zw_v1.0.0_胡总制命_001_L1",
    )
    version: str = "1.0.0"
