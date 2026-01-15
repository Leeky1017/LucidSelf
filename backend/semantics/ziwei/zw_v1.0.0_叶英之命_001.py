"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699435
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
    semantic_id="zw_v1.0.0_叶英之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 叶英之命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫相昌曲相逢加会**：紫微、天相与文昌文曲同会，主清贵文名。
  - **文星逢廉贞化忌**：文昌文曲与廉贞化忌同见，才华反成招灾之源。
  - **丧命夭寿**：秘...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫相昌曲相逢加会**：紫微、天相与文昌文曲同会，主清贵文名。
  - **文星逢廉贞化忌**：文昌文曲与廉贞化忌同见，才华反成招灾之源。
  - **丧命夭寿**：秘传文星逢廉贞主丧命与夭寿。
  - **本作美论**：紫相昌曲格局本为清贵双全的美格。
  - **卑二岁夭折**：约在三十出头因结构被激发而早亡。
  - **才高命薄**：文名甚高而寿命甚短的结构。
  - **阳男水二局**：叶英命盘的五行局数，水二局主智慧才情。

- **原文（source_text）**：  
  叶英之命。阳男水二局。紫相昌曲相逢加会，本作美论，柰嫌昌曲，不宜见廉贞化忌。秘云：文曲文昌逢廉贞，丧命，夭寿之人，故死。千二十二岁。

- **规范化释义（primary_lang_explained）**：  
  叶英命局为阳男水二局，命宫得紫微、天相与昌曲相逢加会，原本是极佳的清贵与文誉格局：紫微、天相主权柄与清望，昌曲主文名与才情，三者会合，本应成就「文武兼资而品行端正」的一生。然原文指出关键隐患在于「昌曲不宜见廉贞化忌」——当文昌、文曲遇上廉贞化忌时，才华与名气反而可能成为招灾之源。秘传更直言「文曲文昌逢廉贞，丧命，夭寿之人」，说明此组合在某些结构下，会把本可成名之才推向早夭之途。  
  原文末句「千二十二岁」应为「卅二岁」或近似写法，可理解为命主在三十出头时因上述结构被限运激发而夭折。整体来看，此命例展示了「高文名 + 凶曜纠缠」如何将本应长成的才华压缩在短暂的一生之内。

- **完整对等诠释（secondary_lang_full）**：  
  Ye Ying’s chart is a Yang Water pattern in which Zi Wei, Tian Xiang and the literary pair Wen Chang and Wen Qu come together. In theory this is a superb configuration: Zi Wei and Tian Xiang speak of dignity, fairness and administrative talent, while the literary stars promise reputation based on real ability. Combined, they sketch the outline of a cultivated official whose merit is widely acknowledged. The text, however, calls out a hidden flaw: Wen Chang and Wen Qu "should not meet Lian Zhen transformed to Ji." When the literary stars fall under the shadow of a tabooed Lian Zhen, talent and fame can turn into points of vulnerability. A secret transmission bluntly states that when the writing stars meet Lian Zhen in this way, the result is often death and short life.  
  The final note that he dies at "qian‑er‑shi‑er" is very likely a scribal form of "thirty‑two," suggesting an early death in the early thirties when this fraught combination is triggered by periods and years. As a case, it illustrates how a chart rich in culture and honour can nonetheless be compressed into a brief lifespan once malefic entanglements are activated.

- **核心要点**：  
  1. 紫微、天相与昌曲同会，构成高文名、高品行的清贵格局。  
  2. 文昌、文曲遇廉贞化忌时，才华与名气可能反转为招灾因子。  
  3. 叶英命例呈现「文名甚高而寿命甚短」的结构，约在三十出头即遭夭折。

- **叙事素材（narrative_snippets）**：
  - **紫相昌曲**："紫相昌曲相逢加会，本作美论"，叶英命主本是品行端正、文名在外的典型清贵之才。
  - **文星遇廉**："柰嫌昌曲，不宜见廉贞化忌。秘云：文曲文昌逢廉贞，丧命，夭寿之人"，文星逢廉贞化忌，使才华与声望反成折寿之因。
  - **三十出头夭折**：原文记「千二十二岁」可作卅二岁理解，指示其在三十出头即因结构被激发而早亡。
  - **现代应用**：对学者、文人或高曝光知识型职业而言，须警惕在名声与期待高压之下的心理与身体负荷，必要时主动减压与设立边界，避免“文名太盛而命承受不起”。"""
    normalized_text_zh: str = """"""
    subject: str = "叶英之命"
    factor_refs: list = ['pattern_zixiang_changqu', 'star_wenchang_wenqu', 'malefic_lianzhen_huaji', 'malefic_wenxing_fenglian', 'result_yaoshou']
    
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
        l1_anchor="zw_v1.0.0_叶英之命_001_L1",
    )
    version: str = "1.0.0"
