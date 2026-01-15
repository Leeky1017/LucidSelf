"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699797
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
    semantic_id="zw_v1.0.0_严介溪命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 严介溪命(SemanticEntry):
    """
    - 分字分词释义：

  - **武曲守垣**：武曲星守命垣，主财帛与决断力。
  - **昌曲朝昭**：文昌文曲朝照命宫，主文采与聪慧。
  - **科权禄夹**：科权禄三星夹命，主大贵格局。
  ...
    """
    
    original_text: str = """- 分字分词释义：

  - **武曲守垣**：武曲星守命垣，主财帛与决断力。
  - **昌曲朝昭**：文昌文曲朝照命宫，主文采与聪慧。
  - **科权禄夹**：科权禄三星夹命，主大贵格局。
  - **三方擎羊天刑廉杀**：三方见擎羊、天刑、廉贞、七杀，主刑杀之气。
  - **子息宫火星天空蛾廉**：子女宫见火星、天空与蛾廉，主子女缘波折与虚耗。
  - **因子破败临终不美**：因子女或家族问题使晚年与身后名声受损。
  - **阳男金四局**：严介溪命盘的五行局数，金四局主刚断清介。

- **原文（source_text）**：  
  严介溪命。阳男金四局。武曲守垣，昌曲朝昭，科权禄夹，宜上大贵。三方擎羊、天刑、廉贞七杀守垣，故寿虽高，而子息宫火星天空，蜚廉为害，故因子破败而临终不得全美也。

- **规范化释义（primary_lang_explained）**：  
  严介溪命为阳男金四局，武曲守垣、昌曲朝昭，科星、权星、禄星夹命，是「武曲 + 昌曲 + 科权禄夹」的上贵结构，一生宜居高位，为人干练刚正。「介溪」之名亦带清介之意。  
  然而三方有擎羊、天刑与廉贞、七杀守垣，使命局带有强烈的刑杀之气，虽寿数尚高，却在子息宫见火星与天空并临，蜚廉为害，象征子女运与家庭晚景中存有爆裂与虚耗之象。最终因子息方面的破败牵连，临终不得全美，晚年心理与名节上留下遗憾。

- **完整对等诠释（secondary_lang_full）**：  
  Yan Jiexian’s chart is that of a Yang Metal native in the Fourth Configuration. Wu Qu guards the Life, Wen Chang/Wen Qu shine upon it, and Ke‑Quan‑Lu flank the palace; this "Wu‑Chang with Ke‑Quan‑Lu" pattern suits high office and resolute, upright character, matching the "Jie" (integrity) in his name.  
  Yet Qing Yang, Tian Xing, Lian Zhen and Qi Sha hold the tri‑palaces, embedding strong punitive and martial energy. Although lifespan is relatively long, the offspring palace hosts Huo Xing and Tian Kong with Fei Lian afflicting it, symbolising volatility, depletion and trouble in descendants or family line. The text notes that "because of ruin through children" he "does not end perfectly," capturing a life of high status shadowed by late‑life familial damage. 

- **核心要点**：  
  1. 武曲、昌曲与科权禄夹命，为高阶武贵与清介之士格。  
  2. 三方擎羊、天刑、廉贞七杀守垣，使命局带刑杀色彩。  
  3. 子息宫火星、天空与蜚廉为害，晚年因子息破败而临终不美，呈现「贵而不圆满」。"""
    normalized_text_zh: str = """"""
    subject: str = "严介溪命"
    factor_refs: list = ['star_wuqu_shouyuan', 'pattern_changqu_chaozhao', 'pattern_kequanlu_jia', 'malefic_sanfang_xingsha', 'malefic_zixi_huokong_feilian', 'result_yinzi_pobai']
    
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
        l1_anchor="zw_v1.0.0_严介溪命_001_L1",
    )
    version: str = "1.0.0"
