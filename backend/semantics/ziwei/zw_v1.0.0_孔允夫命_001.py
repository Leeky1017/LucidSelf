"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699531
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
    semantic_id="zw_v1.0.0_孔允夫命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 孔允夫命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄夹命**：权星、禄星分列命宫两侧，主权势与俸禄环绕命主。
  - **左右加会财官双美**：左辅右彼加会命宫，财帛与官禄二宫皆得吉星会照。
  - **寅申冲照*...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄夹命**：权星、禄星分列命宫两侧，主权势与俸禄环绕命主。
  - **左右加会财官双美**：左辅右彼加会命宫，财帛与官禄二宫皆得吉星会照。
  - **寅申冲照**：大限在寅、太岁在申，寅申二支相冲，主剧烈变动。
  - **蚥廉同并流羊**：冲照蚥廉星同并流年羊刃，主飞祸骤起。
  - **七杀重逢**：限运再遇七杀星，主激烈冲突与权势挑战。
  - **是为凶也**：寅申冲加蚥廉流羊与七杀重逢，为凶险之象。
  - **阴男水二局**：孔允夫命盘的五行局数，水二局主智慧权谋。

- **原文（source_text）**：  
  孔允夫命。阴男水二局。权禄夹命之格，左右加会，财官双美，无不富贵。三十二岁小限，大限在寅，太岁在申，冲照蜚廉同并流羊，又加以七杀重逢，是为凶也。

- **规范化释义（primary_lang_explained）**：  
  孔允夫命为阴男水二局，命宫成「权禄夹命」之格，两侧有权星、禄星夹拱，加之左右同来会合，财官双美，是典型「权禄夹命、左右加会」的清贵权臣或重臣格局，一生多主富贵显达、位臻高秩。此类格局既强调实权与名位，也暗示命主长期置身权力中心。  
  原文指出其关键关口在三十二岁：当时小限行至要害之地，大限在寅，太岁在申，寅申相冲，冲照蜚廉并同流年羊刃，又有七杀重逢，会成「寅申冲 + 蜚廉 + 流羊 + 重煞」等多重凶象。一方面象征权场风云剧烈翻涌，党争、弹劾、兵祸等风险骤增；另一方面亦暗示命主体质与心志在高压之下难以承受，最终于此阶段遭遇严重打击甚至身亡。此命例呈现「高位权臣，在寅申冲与七杀重逢之运中折损」的格局。

- **完整对等诠释（secondary_lang_full）**：  
  Kong Yunfu’s chart is that of a Yin Water native in the Second Configuration. With Authority and Lu stars flanking the Life palace—"power and stipends encircling the self"—and Left and Right Assistants joining in, both Wealth and Office are strong. This "Quan‑Lu flanking Life with Zuo‑You" pattern marks a dignified minister or high official who enjoys real influence and abundant resources, spending much of life in the inner ring of power.  
  The text singles out age thirty‑two as a dangerous turning point. At that time the minor period moves into a critical sector while the major period occupies Yin and the Annual Tai Sui stands in Shen. The clash between Yin and Shen beams onto Fei Lian together with the flowing Yang Blade, and Seven Killing appears again. This combination of branch clash, malefic star and repeated Killing indicates fierce turbulence in the political arena and a heightened risk of downfall or death. The case thus portrays a high‑ranking minister whose privileged position cannot shield him from destruction when severe transits converge on an already intense structure.

- **核心要点**：  
  1. 权禄夹命、左右加会，财官双美，构成典型高位权臣或重臣格局。  
  2. 命主一生深处权力核心，既享富贵也承受高风险。  
  3. 三十二岁小限与大限寅、太岁申相冲，冲照蜚廉、流羊与重逢七杀，为极具摧毁力的高危限运。

- **叙事素材（narrative_snippets）**：
  - **权禄夹命**："权禄夹命之格，左右加会，财官双美，无不富贵"，孔允夫命主两侧权禄夹拱，一生位重财厚。
  - **寅申冲克**："三十二岁小限，大限在寅，太岁在申"，寅申相冲为剧烈变动之象，尤其对权位在身者冲击更大。
  - **蜚廉流羊**："冲照蜚廉同并流羊，又加以七杀重逢，是为凶也"，蜚廉加流羊与七杀重逢，为政治风波与身家险境同时爆发的组合。
  - **现代应用**：身居要职、手握实权者，在形成「寅申冲 + 重煞合击」的年份，应主动降低锋芒、远离权力风暴中心，并重视身体与安全布防，避免在最高位时遭遇最重的跌落。"""
    normalized_text_zh: str = """"""
    subject: str = "孔允夫命"
    factor_refs: list = ['pattern_quanlu_jiaming', 'pattern_zuoyou_jiahui', 'pattern_caiguan_shuangmei', 'timing_yinshen_chong', 'malefic_feilian', 'timing_qisha_chongfeng']
    
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
        l1_anchor="zw_v1.0.0_孔允夫命_001_L1",
    )
    version: str = "1.0.0"
