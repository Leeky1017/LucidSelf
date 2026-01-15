"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559292
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
    semantic_id="yhzp_v1.0.0_详解定真论_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 详解定真论(SemanticEntry):
    """
    - **原文（source_text）**：夫生日为主者，行君之令，法运四时。择日之法有三要：以干为天，以支为地，支中所藏者为人元。乃分四柱，以年为根，月为苗，日为花，时为果。干克以为妻财，财多干旺则...
    """
    
    original_text: str = """- **原文（source_text）**：夫生日为主者，行君之令，法运四时。择日之法有三要：以干为天，以支为地，支中所藏者为人元。乃分四柱，以年为根，月为苗，日为花，时为果。干克以为妻财，财多干旺则称意；若干衰则反祸矣！

- **分字分词释义**：
  - **生日为主**：日干为命主代表，称为"日主"或"日元"。
  - **行君之令**：日主如同君主，统领全局。
  - **法运四时**：论命须依据四季时令的阴阳消长规律。
  - **以干为天**：天干代表天，为外在显现。
  - **以支为地**：地支代表地，为内在根基。
  - **支中所藏者为人元**：地支藏干代表人元，为隐含因素。
  - **年为根月为苗日为花时为果**：四柱以植物生长比喻：年为根基、月为苗枝、日为花朵、时为果实。
  - **干克以为妻财**：日主所克者为财星，代表妻与财。
  - **财多干旺则称意**：财星多且日主旺盛，主财运亨通。
  - **财多干衰则反祸**：财星多而日主衰弱，主为财所累反成灾祸。

- **规范化释义（primary_lang_explained）**：日干为主，法运四时阴阳之理。四柱分工：天干为天、地支为地、支藏为人元；年为根、月为苗、日为花、时为果。干克为妻财，财多身旺吉，财多身弱凶。

- **完整对等诠释（secondary_lang_full）**：Day Stem as master follows four seasons' yin-yang principles. Four Pillars division: Heavenly Stems=heaven, Earthly Branches=earth, hidden stems=human element; Year=root, Month=sprout, Day=flower, Hour=fruit. Stem-controlling represents wife-wealth—abundant wealth with strong Stem auspicious, abundant wealth with weak Stem brings calamity.

- **核心要点**：日干为主法四时；四柱分天地人元；年根月苗日花时果；干克为财财多身旺吉身弱凶

- **详细解说**：  《详解定真论》是子平法的基础理论篇章，阐述论命的结构原理与核心法则。"生日为主者，行君之令"确立了日干为命主代表的核心地位，日主如同君主统领全局。"法运四时"则强调论命须遵循四季时令的阴阳消长规律。在结构上，本篇提出"三才"理论：天干为天（外显）、地支为地（根基）、支藏为人元（隐含）。四柱则以植物生长比喻："年为根、月为苗、日为花、时为果"，形象说明四柱各自功能与相互关系。在六亲与财运判断上，"干克以为妻财"确立了财星的推导原则，并提出"财多身旺吉、财多身弱凶"的核心判断标准，即财星多少与日主强弱的配合决定财运吉凶。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_291]` `[trigger: 日主为君]` `[factor_trigger: rigan_weizhu AND junzhi_ling]` `[role: 主干]` 夫生日为主者，行君之令；日干为命主统领全局。 → 《渊海子平·详解定真论》
  - `[ns_yhzp_292]` `[trigger: 三才结构]` `[factor_trigger: sancai AND tiandi_renyuan AND hidden_stem AND human]` `[role: 主干依赖]` 以干为天，以支为地，支中所藏者为人元；天地人三才结构。 → 《渊海子平·详解定真论》
  - `[ns_yhzp_293]` `[trigger: 四柱比喻]` `[factor_trigger: sizhu AND gen_miao_hua_guo AND four_pillars_metaphor]` `[role: 主干依赖]` 以年为根，月为苗，日为花，时为果；四柱生长比喻。 → 《渊海子平·详解定真论》
  - `[ns_yhzp_294]` `[trigger: 财多身旺吉]` `[factor_trigger: caiduo_shenwang AND ji AND chenyi]` `[role: 条件分支]` 财多干旺则称意；财星多且日主旺主财运亨通。 → 《渊海子平·详解定真论》
  - `[ns_yhzp_295]` `[trigger: 财多身弱凶]` `[factor_trigger: caiduo_shenruo AND xiong AND fanhuo]` `[role: 条件分支]` 若干衰则反祸矣！财多身弱主为财所累成灾。 → 《渊海子平·详解定真论》
  - `[ns_yhzp_296]` `[trigger: 定真论纲领]` `[factor_trigger: dingzhen_lun AND lunming_jichu]` `[role: 总结]` 详解定真论以日主为君、三才四柱为结构、财身配合为应用的论命基础理论。 → 《渊海子平·详解定真论》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 三元 | Three Elements | 天干地支人元 | Heavenly Stem, Earthly Branch, Hidden Stem | three_elements | existing |
| 四柱比喻 | Four Pillars Metaphor | 年根月苗日花时果 | Year-root, Month-sprout, Day-flower, Hour-fruit | four_pillars_metaphor | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "详解定真论"
    factor_refs: list = []
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_详解定真论_001_L1",
    )
    version: str = "1.0.0"
