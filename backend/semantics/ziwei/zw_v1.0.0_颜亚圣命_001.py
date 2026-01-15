"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.698985
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
    semantic_id="zw_v1.0.0_颜亚圣命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 颜亚圣命(SemanticEntry):
    """
    - 分字分词释义：

  - **魁钺坐命**：天魁天钺贵人星坐守命宫，主贵人扶持。
  - **权禄昌曲**：化权化禄与文昌文曲同会身宫，主显达贵象。
  - **昌曲陷于天伤**：文昌文曲落陷于天...
    """
    
    original_text: str = """- 分字分词释义：

  - **魁钺坐命**：天魁天钺贵人星坐守命宫，主贵人扶持。
  - **权禄昌曲**：化权化禄与文昌文曲同会身宫，主显达贵象。
  - **昌曲陷于天伤**：文昌文曲落陷于天伤之地，福禄不能完全发挥。
  - **七杀重逢**：大限再遇七杀星，为凶险之限。
  - **流羊流陀迭并**：流年擎羊陀罗同时会合命宫，诸凶齐聚主早逝。
  - **英年夷折**：颜回三十二岁早逝，才德卓著却寿命不永。
  - **壬辰年**：颜回寿终之年，太岁带流羊流陀的应期。

- **原文（source_text）**：  
  颜亚圣命。阴男木三局。命坐魁钺，身逢权禄，昌曲，陷于天伤，不能发达，大限七杀重逢。壬辰年太岁流羊、流陀迭并，故死。

- **规范化释义（primary_lang_explained）**：  
  颜回（亚圣）命属阴男木三局，命宫坐魁钺贵人，身宫逢权禄、昌曲诸吉，本应显达。然昌曲陷于天伤之地，福禄不能完全发挥；大限又逢七杀重临。壬辰年，太岁带流羊、流陀迭加命宫，诸凶齐聚，遂于该年早逝，英年夭折，令人惋惜。

- **完整对等诠释（secondary_lang_full）**：  
  Yan Hui, known as the Second Sage, has a chart of Yin male Wood Third Configuration. The Life palace is graced by the Noble Stars Kui and Yue; the Body palace meets Authority, Salary, Changqu and other auspicious stars—all signs of eminence. However, Chang and Qu fall into the Celestial Wound position, preventing full attainment. The major period encounters Seven Killings again. In the ren‑chen year, transiting Yang Blade and Tuo Luo converge with Tai Sui upon the Life palace; under this pile‑up of malefics, he passed away young, a brilliant life cut tragically short.

- **核心要点**：  
  1. 魁钺坐命、权禄昌曲拱身，本为显达之格。  
  2. 昌曲陷天伤，福禄受损；七杀重逢为凶限。  
  3. 流羊流陀迭并，为早逝应期。

- **叙事素材（narrative_snippets）**：
  - **显达之格**："命坐魁钺，身逢权禄昌曲"，颜回命本应显达。
  - **昌曲陷伤**："昌曲陷于天伤，不能发达"，吉星落陷则福禄受损。
  - **英年早逝**："壬辰年流羊流陀迭并，故死"，诸凶齐聚致英年夭折。
  - **现代应用**：吉格亦需看星曜得地与否——昌曲陷地则福禄难全发挥。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j6_014]` `[trigger: 魁钺坐命]` `[factor_trigger: star_tiankui AND star_tianyue AND palace_ming]` `[role: 条件分支]` 魁钺坐命主贵人扶持显达之格。 → 《卷六》颜回命"命坐魁钺"
  - `[ns_zwds_j6_015]` `[trigger: 权禄拱身]` `[factor_trigger: hua_quan AND hua_lu AND palace_shen]` `[role: 条件分支]` 权禄拱身为化权化禄会照身宫的贵格配置。 → 《卷六》"身逢权禄"
  - `[ns_zwds_j6_016]` `[trigger: 昌曲陷地]` `[factor_trigger: star_wenchang AND star_wenqu AND state_xian]` `[role: 条件分支]` 昌曲陷地为文昌文曲落陷的不利配置。 → 《卷六》"昌曲陷于天伤"
  - `[ns_zwds_j6_017]` `[trigger: 七杀重逢]` `[factor_trigger: star_qisha AND daxian_chongfeng]` `[role: 条件分支]` 七杀重逢为大限再遇七杀的凶险配置。 → 《卷六》"大限七杀重逢"
  - `[ns_zwds_j6_018]` `[trigger: 流羊流陀]` `[factor_trigger: liuyang AND liutuo]` `[role: 条件分支]` 流羊流陀为流年擎羊陀罗会合的凶险配置。 → 《卷六》"流羊流陀迭并"
  - `[ns_zwds_j6_019]` `[trigger: 英年早逝]` `[factor_trigger: result_yingnian_zaoshi]` `[role: 结果]` 英年早逝为年轻时夭折的凶险结果。 → 《卷六》"故死""""
    normalized_text_zh: str = """"""
    subject: str = "颜亚圣命"
    factor_refs: list = ['star_kuiyue', 'sihua_quanlu', 'star_changqu', 'pattern_qishachongfeng', 'star_liuyangtuo', 'source_ref', 'rel_yanhui_001', 'star_kuiyue', 'rel_yanhui_002', 'star_changqu', 'rel_yanhui_003', 'star_liuyangtuo', 'evi_yanhui_001', 'star_changqu', 'rule_changqu_xian', 'evi_yanhui_002', 'star_liuyangtuo', 'rule_liuyangtuo_si', 'concept_noble_support', 'concept_star_fallen']
    
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
        l1_anchor="zw_v1.0.0_颜亚圣命_001_L1",
    )
    version: str = "1.0.0"
