"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699540
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
    semantic_id="zw_v1.0.0_郭子仪命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 郭子仪命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄夹命昌曲加会**：权星禄星夹拱命宫，文昌文曲同来会照，主无不富贵。
  - **太岁并限于地劫**：太岁与大限同行至地劫所在宫位，主晚年结构性承压。
  - **...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄夹命昌曲加会**：权星禄星夹拱命宫，文昌文曲同来会照，主无不富贵。
  - **太岁并限于地劫**：太岁与大限同行至地劫所在宫位，主晚年结构性承压。
  - **小限擎羊忌宿**：小限行经擎羊与忌宿同宫，主刚烈冲撞与晦暗之气。
  - **酉人有忌**：生于酉支者于特定限运逢忌，较他支更易显凶。
  - **终寿于此年**：寿数大致走完整程，于高龄自然终结而非横死。
  - **快德承压**：厉重功业与权禄结构对寿命的承压能力。
  - **阴男水二局**：郭子仪命盘的五行局数，水二局主智慧谋略。

- **原文（source_text）**：  
  郭子仪命。阴男水二局。权禄夹命之格，又兼昌曲加会，无不富贵之论。八十五岁，太岁并限于地劫，小限又行擎羊忌宿，酉人有忌，故终寿于此年。

- **规范化释义（primary_lang_explained）**：  
  郭子仪命为阴男水二局，命宫成「权禄夹命」之格，两侧有权星、禄星夹拱，再兼文昌、昌曲加会，为典型富贵权臣结构，一生多主权高位重、功业显赫。原文以「无不富贵之论」点出其富贵之厚，并以八十五岁寿终于此年，说明此权禄格不仅不折寿，反而支撑其高龄终寿。  
  八十五岁时，太岁并大限行至地劫之地，小限又行擎羊与忌宿等重凶组合，且「酉人有忌」，在理气上已然构成高度危险的限运。然而命局根基厚重、权禄格局稳固，终在此年「终寿」而非横死，从案例角度呈现的是「高位权臣在重凶限运下，仍以自然终寿收官」的形态。

- **完整对等诠释（secondary_lang_full）**：  
  Guo Ziyi’s chart is that of a Yin Water native in the Second Configuration. Authority and Lu stars flank the Life palace while Wen Chang and Wen Qu join in, forming a classic "Quan‑Lu flanking Life with scholarly support" pattern. This is a structure of great honour and power, suitable for a minister of high rank whose achievements and standing are widely recognised. The text emphasises that "there is no argument against his wealth and nobility," underscoring the depth of his fortune.  
  At the age of eighty‑five, both the Annual Tai Sui and the major period move into the sector of Di Jie, while the minor period passes through the region of Qing Yang and Ji‑宿, a heavy configuration especially inauspicious for natives of the You branch. By ordinary standards this would be a highly dangerous combination, suggesting sharp risks to life and status. Yet in this case the robust foundation—anchored by the Quan‑Lu pattern—allows the native to reach a full lifespan and die a natural death. The example thus illustrates a type of high ministerial chart that, despite severe transits, closes with a dignified and complete old age.

- **核心要点**：  
  1. 权禄夹命加昌曲拱照，构成极高权势与富贵的重臣格局。  
  2. 虽在八十五岁逢太岁并大限于地劫、小限擎羊忌宿等重凶组合，仍以自然终寿收场。  
  3. 呈现「高位权臣 + 重凶限运」却不致横死，而是善终的对照命例。

- **叙事素材（narrative_snippets）**：
  - **权禄重臣**："权禄夹命之格，又兼昌曲加会，无不富贵之论"，郭子仪命主权禄环身、文采加持，为开国重臣典型。
  - **高龄重凶**："八十五岁，太岁并限于地劫，小限又行擎羊忌宿，酉人有忌，故终寿于此年"，晚年虽逢地劫、擎羊与忌宿重凶，仍在高龄自然终寿。
  - **厚德承压**：同为权禄夹命，与前面折损命例相比，此局以功勋与格局厚重，展现出更强的承压能力。
  - **现代应用**：处在高压岗位多年、又积累深厚人望与结构优势的人，在重凶岁运中若能主动减负与养生，往往可以把原本可能的"大祸"化为"顺势退场"，以善终代替折寿。"""
    normalized_text_zh: str = """"""
    subject: str = "郭子仪命"
    factor_refs: list = ['pattern_quanlu_jiaming', 'pattern_changqu_jiahui', 'timing_taisui_dijie', 'malefic_qingyang_jisu', 'condition_youren_youji', 'result_zhongshou']
    
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
        l1_anchor="zw_v1.0.0_郭子仪命_001_L1",
    )
    version: str = "1.0.0"
