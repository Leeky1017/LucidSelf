"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578453
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
    semantic_id="qtbj_v1.0.0_6__二月辛金_卯月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 6二月辛金卯月(SemanticEntry):
    """
    - **原文（source_text）**：
  二月辛金，阳和之际，壬水为尊，见戊己为病。得甲制伏，则辛金不致埋没，壬水不致混浊，合此者必身入玉堂。故二月辛金，有壬甲透者贵显。否则，乡绅。或壬坐亥支...
    """
    
    original_text: str = """- **原文（source_text）**：
  二月辛金，阳和之际，壬水为尊，见戊己为病。得甲制伏，则辛金不致埋没，壬水不致混浊，合此者必身入玉堂。故二月辛金，有壬甲透者贵显。否则，乡绅。或壬坐亥支，不见土出，可能入芥，家亦小康。得申中之壬者，异途名望。无壬者常人。其生克之理，与正月辛金皆同。
  或壬戊透，甲不出干，此为病不遇药，平常之人。得乙破戊，颇有衣衿。但假名假利，刻薄乖张。
  或一派壬水汪洋，名金水淘洗太过，不得中和，略有衣食，全无作为。如壬水重重，得戊反吉。或支成木局，泄尽壬水，有庚富贵，无庚平人。
  或支成火局，名官印相争，金水两伤，下流之格。得二壬出制，富贵反奇。
  辛金生于春季，一派壬水，而无丙火，即能显达，家无宿舂。得壬丙齐透，方许大富大贵。

- **分字分词释义**：
  - **阳和之际**：阳气和煦之时 / 卯月特点 / 春暖
  - **壬水为尊**：壬水最为尊贵 / 用神 / 洗淘
  - **身入玉堂**：进入翰林院 / 壬甲配合 / 大贵
  - **乡绅**：乡里士绅 / 壬甲不透 / 次吉
  - **病不遇药**：有病无药 / 壬戊透无甲 / 凶象
  - **假名假利**：虚假名利 / 乙破戊 / 次凶
  - **金水淘洗太过**：金水冲洗过度 / 壬多无戊 / 凶象
  - **官印相争**：官杀与印绶争夺 / 火局 / 凶象
  - **下流之格**：低下卑贱格局 / 金水两伤 / 凶象
  - **家无宿舂**：家中无隔夜之粮 / 贫穷 / 凶象

- **规范化释义（primary_lang_explained）**：
  二月（卯月）辛金阳和之际壬水为尊见戊己为病。得甲制伏则辛金不致埋没壬水不致混浊合此者必身入玉堂。故二月辛金有壬甲透者贵显否则乡绅。或壬坐亥支不见土出可能入芥家亦小康。得申中之壬者异途名望。无壬者常人。其生克之理与正月辛金皆同。
  或壬戊透甲不出干此为病不遇药平常之人。得乙破戊颇有衣衿但假名假利刻薄乖张。
  或一派壬水汪洋名金水淘洗太过不得中和略有衣食全无作为。如壬水重重得戊反吉。或支成木局泄尽壬水有庚富贵无庚平人。
  或支成火局名官印相争金水两伤下流之格。得二壬出制富贵反奇。
  辛金生于春季一派壬水而无丙火即能显达家无宿舂。得壬丙齐透方许大富大贵。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 2nd Month (Rabbit Month): yang harmony time Ren Water revered見Wu/Ji as病. Gaining Jia制伏 then Xin Metal not buried Ren Water not turbid matching this surely entering Jade-Hall. Therefore 2nd month Xin Metal having Ren/Jia revealing noble-prominent otherwise township-gentry. Or Ren sitting Hai branch not見Earth revealing possibly芥 family also modest-prosperity. Gaining Ren within Shen alternative fame-reputation. Without Ren ordinary. Its生克 principle same as 1st month Xin Metal.
  Or Ren/Wu revealing Jia not revealing this病 not meeting medicine ordinary person. Gaining Yi breaking Wu fairly scholarly but fake-name fake-profit harsh-perverse.
  Or all Ren Water vast name Metal-Water washing too-much not gaining balance slightly food-clothing entirely no-achievement. If Ren Water heavy gaining Wu conversely auspicious. Or branches form Wood Frame draining Ren Water having Geng wealth-nobility without Geng ordinary.
  Or branches form Fire Frame name Officer-Seal争 Metal-Water both-hurt low-class pattern. Gaining two Ren revealing制 wealth-nobility conversely extraordinary.
  Xin Metal born spring season all Ren Water without Bing Fire can prominence family no宿舂. Gaining Ren/Bing齊透 then allowing great-wealth great-nobility.

- **核心要点**：
  - **首要用神**：壬水（为尊）、甲木（制土）
  - **忌神**：戊己埋金浊水
  - **卯月特点**：阳和木旺壬水清洗甲木疏土

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_407]` `[trigger: 辛生卯月]` `[factor_trigger: month_mao AND tiangan_xin AND tiangan_ren AND tiangan_jia]` `[role: 主干]` 二月辛金，阳和之际，壬水为尊，见戊己为病。得甲制伏，则辛金不致埋没。 → 《穷通宝鉴·三春辛金》#34.6
  - `[ns_qttbj_408]` `[trigger: 壬甲两透]` `[factor_trigger: month_mao AND tiangan_xin AND ren_revealed AND jia_revealed]` `[role: 条件分支]` 有壬甲透者贵显，否则乡绅。 → 《穷通宝鉴·三春辛金》#34.6
  - `[ns_qttbj_409]` `[trigger: 金水淘洗太过]` `[factor_trigger: month_mao AND tiangan_xin AND ren_excessive AND metal_water_too_much]` `[role: 例外处理]` 或一派壬水汪洋，名金水淘洗太过，不得中和，略有衣食，全无作为。 → 《穷通宝鉴·三春辛金》#34.6
  - `[ns_qttbj_410]` `[trigger: 官印相争]` `[factor_trigger: month_mao AND tiangan_xin AND dizhi_fire_frame AND officer_seal_contending]` `[role: 例外处理]` 或支成火局，名官印相争，金水两伤，下流之格。 → 《穷通宝鉴·三春辛金》#34.6"""
    normalized_text_zh: str = """"""
    subject: str = "6. 二月辛金（卯月）"
    factor_refs: list = ['entering_jade_hall', 'metal_water_too_much', 'officer_seal_contending']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_6__二月辛金_卯月_001_L1",
    )
    version: str = "1.0.0"
