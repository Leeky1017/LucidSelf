"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699710
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
    semantic_id="zw_v1.0.0_杭宽之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 杭宽之命(SemanticEntry):
    """
    - 分字分词释义：

  - **命不主财**：命局整体对财富支撑力弱，财运难以成为主轴。
  - **禄主缠于陷地**：禄星落于陷地而受困，主财路阻塞与机会落空。
  - **空劫冲照**：空星与劫...
    """
    
    original_text: str = """- 分字分词释义：

  - **命不主财**：命局整体对财富支撑力弱，财运难以成为主轴。
  - **禄主缠于陷地**：禄星落于陷地而受困，主财路阻塞与机会落空。
  - **空劫冲照**：空星与劫星冲照命宫或财帛，主虚耗与损失。
  - **擎羊天使之地**：擎羊与天使并临之宫位，主硬碰与制度性打击。
  - **天哭地劫**：与哀伤、根基被夺相关的组合，主精神打击与现实损失并存。
  - **终身不得发达**：一生难以真正发达，财禄始终受困。
  - **阴男水二局**：杭宽命盘的五行局数，水二局主智慧财困。

- **原文（source_text）**：  
  杭宽之命。阴男水二局。命不主财，禄主缠于陷地，空劫冲照，终身不得发达。大限到于擎羊天使之地，小限临命垣天哭地劫之位，何能得生，必主命亡，故死于五十一而巳。

- **规范化释义（primary_lang_explained）**：  
  杭宽命为阴男水二局，原文明言「命不主财」，禄星落在陷地而受困，又逢空劫冲照，象征财路常被虚耗、机会落空，一生难以真正发达。宽字本带宽厚之意，但命理上却呈现「财禄被困、空劫冲耗」的长期紧绷。  
  当大限行至擎羊与天使同在之地，小限又临命垣的天哭与地劫之位，是「擎羊 + 天使 + 天哭 + 地劫」的重凶组合，既指突发打击与制度性压力，也象征哀伤与根基被掏空。原文以「何能得生，必主命亡」点明其断灭性，命主遂于五十一岁死亡。

- **完整对等诠释（secondary_lang_full）**：  
  Hang Kuan’s chart is that of a Yin Water native in the Second Configuration. The text explicitly states that "the chart does not govern wealth": the Lu star is trapped in a fallen position and bombarded by Kong and Jie, so that financial avenues are constrained and opportunities dissipate. The name "Kuan" (broad, generous) contrasts with a life pattern of constrained resources and repeated depletion.  
  When the major period reaches the region of Qing Yang and a "Heavenly Office" star, and the minor period meets Tian Ku and Di Jie at the Life sector, the combination of Qing Yang, institutional pressure, grief and earth‑robbery—"Yang + Heavenly Office + Ku + Di Jie"—forms an intensely malefic pattern. The text concludes that under such conditions "there is no way to survive" and records death at fifty‑one. The case typifies a chart with chronically constrained wealth that ends in a heavily afflicted year.

- **核心要点**：  
  1. 命不主财，禄星陷地并受空劫冲照，一生财路多被困与虚耗。  
  2. 五十一岁大限行擎羊天使之地，小限临天哭地劫，构成打击 + 悲伤 + 根基流失的重凶年。  
  3. 命例呈现「财禄难开、一生不得大展且终结于重凶限」的轨迹。"""
    normalized_text_zh: str = """"""
    subject: str = "杭宽之命"
    factor_refs: list = ['quality_ming_buzhucai', 'malefic_lu_xiandi', 'malefic_kongjie_chongzhao', 'timing_qingyang_tianshi', 'malefic_tianku_dijie', 'quality_zhongshen_buda']
    
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
        l1_anchor="zw_v1.0.0_杭宽之命_001_L1",
    )
    version: str = "1.0.0"
