"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699636
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
    semantic_id="zw_v1.0.0_马援之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 马援之命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权禄拱**：科星、权星与禄星同拱命宫，主功名、权位与俸禄并臻。
  - **昌曲加会**：文昌与文曲同会命宫或三方，主文才秀发与科名显达。
  - **贪狼遇铨**...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权禄拱**：科星、权星与禄星同拱命宫，主功名、权位与俸禄并臻。
  - **昌曲加会**：文昌与文曲同会命宫或三方，主文才秀发与科名显达。
  - **贪狼遇铨**：贪狼逢权星，主欲望与开拓力得到权势加持。
  - **武曲同行**：武曲与其他星同宫或同行，主武职与财富气息增强。
  - **威振边夷**：武功势力足以震慑边陲，边将格局。
  - **大限天罗小限夹地**：大限行至天罗、小限巡于夹地，主封锁性格局与劫数难逃。
  - **阳男火六局**：马援命盘的五行局数，火六局主热情执行与边功。

- **原文（source_text）**：  
  马援之命。阳男火六局。科权禄拱，富贵声扬，昌曲加会，文武双全。贪狼遇铨，武曲同行，威振边夷。六十六，大限到于天罗，小限巡于夹地，其数难逃。

- **规范化释义（primary_lang_explained）**：  
  马援命为阳男火六局，命局中科星、权星与禄星同来拱照，再得文昌、文曲加会，为「科权禄拱、昌曲加会」之格，一方面主功名权禄兼具，一方面为文武兼修的将相之命。贪狼遇权、武曲同行，则将此格推向带有强烈武职与边疆开拓色彩的结构，「威振边夷」即形容其武功势力足以震慑边陲。  
  然而，六十六岁时大限行至天罗之地，小限又巡行夹地，罗网与夹困之象层层叠加，为「天罗 + 夹地」的封锁性格局。此时外在局势与内在气数皆被网状凶象所缠绕，进退维谷，原文以「其数难逃」点出劫数难以避免，遂在此年凶亡。命例体现「文武双全、功业显赫，却终折于天罗夹地之运」的轨迹。

- **完整对等诠释（secondary_lang_full）**：  
  Ma Yuan’s chart is that of a Yang Fire native in the Sixth Configuration. With academic Ke, authority Quan and Lu stars all converging on the Life or its triad, and Wen Chang and Wen Qu joining, the pattern "Ke‑Quan‑Lu surrounding with Chang‑Qu assisting" grants both honours and stipends, as well as literary and martial refinement. When Tan Lang meets power and Wu Qu travels alongside, the configuration takes on an explicitly martial and frontier flavour—fitting the image of a general whose might "shakes the border tribes."  
  At sixty‑six, however, the major period reaches the region of Tian Luo, the Celestial Net, while the minor period passes through a "clamped earth" position. Together they form a layered entanglement—nets above and constriction below—symbolising circumstances in which both external situations and internal vitality are tightly bound. The text states that "this tally cannot be escaped," indicating that the convergence of these limiting influences culminates in death that year. The case depicts a life of great civil‑military achievement ultimately cut off by a fatal net of transits.

- **核心要点**：  
  1. 科权禄拱配合昌曲加会，贪狼遇权、武曲同行，是文武双全、威振边陲的将相格。  
  2. 六十六岁大限天罗、小限夹地，形成上网下困的封锁性重凶格局。  
  3. 命例呈现「功勋极盛而终折于天罗夹地」的晚年命轨。

- **叙事素材（narrative_snippets）**：
  - **科权禄拱**："科权禄拱，富贵声扬，昌曲加会，文武双全"，马援命主以科名、权势与文采并重而著称。
  - **贪武边功**："贪狼遇铨，武曲同行，威振边夷"，贪狼逢权与武曲同来，直接点出其以边疆军功立名的性质。
  - **天罗夹地**："六十六，大限到于天罗，小限巡于夹地，其数难逃"，天罗配夹地，使其在晚年陷入上有天网、下有地困的封锁局面。
  - **现代应用**：对承担大型组织或复杂项目的「攻坚型」领导而言，在明显「天罗 + 夹地」年份要学会接受阶段性收官与退场，而不是继续硬撑在一线，以免在系统性压力下把命运压进最后一搏。"""
    normalized_text_zh: str = """"""
    subject: str = "马援之命"
    factor_refs: list = ['pattern_kequanlu_gong', 'pattern_changqu_jiahui', 'pattern_tanlang_yuquan', 'pattern_wuqu_tongxing', 'timing_daxian_tianluo', 'timing_xiaoxian_jiadi']
    
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
        l1_anchor="zw_v1.0.0_马援之命_001_L1",
    )
    version: str = "1.0.0"
