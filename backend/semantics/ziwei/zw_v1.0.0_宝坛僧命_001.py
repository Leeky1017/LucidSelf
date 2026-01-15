"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699781
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
    semantic_id="zw_v1.0.0_宝坛僧命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 宝坛僧命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权禄拱**：科星、权星、禄星同拱命垣，主功名与俸禄。
  - **左右朝垣**：左辅右彼朝拱命垣，主辅助与贵人扶持。
  - **空劫身命忌会合**：空劫与忌星同会...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权禄拱**：科星、权星、禄星同拱命垣，主功名与俸禄。
  - **左右朝垣**：左辅右彼朝拱命垣，主辅助与贵人扶持。
  - **空劫身命忌会合**：空劫与忌星同会于身命，主俗缘被抽空而导向出世。
  - **主持若泉之名**：以主持道场闻名，有清修与宗教权威之象。
  - **太岁逢铃**：太岁与铃星相逢，主该年突发事件与惊动。
  - **丧门白虎冲并**：丧门与白虎同时冲击命局，主丧事与血光灾祸。
  - **阳男水二局**：宝坛僧命盘的五行局数，水二局主智慧主持。

- **原文（source_text）**：  
  宝坛僧命。阳男水二局。科权禄拱，左右朝垣，本似富贵之命，柰何空劫身命忌呈会合，只宜为僧，有主持若泉之名。五十一岁，太岁逢铃，大小二限俱在天伤之地，丧门、白虎冲并，故死。

- **规范化释义（primary_lang_explained）**：  
  宝坛僧命为阳男水二局，「科权禄拱，左右朝垣」，本是明显的富贵格局：科星、权星、禄星拱照命垣，加之左右辅弼朝拱，一般应在俗世成就功名利禄。然命局同时见空劫、身命忌星会合，形成「空劫 + 忌星」对命身的缠绕，令此格更适合在空门中表现——以「宝坛」之名主持道场，而非在朝堂出仕。  
  五十一岁时，太岁逢铃星，大小二限俱行至天伤之地，且丧门、白虎并起相冲，是「天伤 + 铃星 + 丧门白虎」的重凶组合：既有病损与意外之象，又有丧曜与血光叠加。于是命主在此年死亡，呈现「富贵格转为空门而终于重凶限」的路径。

- **完整对等诠释（secondary_lang_full）**：  
  Bao Tan the monk’s chart is that of a Yang Water native in the Second Configuration. With academic, Power and Lu stars encircling the Life and Left‑Right Assistants facing the court, the "Ke‑Quan‑Lu with Zuo‑You" structure resembles that of a worldly noble. Yet Kong‑Jie and Ji‑type stars converge on the body and Life, binding and hollowing the secular potential. The destiny is "fit only to be a monk," known as an abbot presiding over a "precious altar" rather than a court official.  
  At fifty‑one, Tai Sui meets Ling Xing and both the major and minor periods occupy Tian Shang regions, while Sang Men and Bai Hu冲 the configuration. This blend—"wound stars + bell star + mourning and White Tiger"—signals illness, accidents and bloodshed wrapped in a funerary tone. Death is therefore indicated in that year. The case depicts a chart that transforms noble potential into religious leadership but still faces a sharply afflicted terminal period.

- **核心要点**：  
  1. 科权禄拱配左右朝垣，本为富贵格，却因空劫与身命忌会合而导向出家主持。  
  2. 五十一岁太岁逢铃，大小二限行天伤之地，并见丧门、白虎冲并。  
  3. 命例展现「富贵素质转为空门，终在病伤与丧曜合击之年身亡」。"""
    normalized_text_zh: str = """"""
    subject: str = "宝坛僧命"
    factor_refs: list = ['pattern_kequanlu_gong', 'pattern_zuoyou_chaoyuan', 'malefic_kongjie_shenming_ji', 'quality_zhuchi_ruoquan', 'timing_taisui_fengling', 'malefic_sangmen_baihu_chong']
    
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
        l1_anchor="zw_v1.0.0_宝坛僧命_001_L1",
    )
    version: str = "1.0.0"
