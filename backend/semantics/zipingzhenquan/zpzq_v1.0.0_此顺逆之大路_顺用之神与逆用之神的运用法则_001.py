"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523894
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
    semantic_id="zpzq_v1.0.0_此顺逆之大路_顺用之神与逆用之神的运用法则_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 此顺逆之大路顺用之神与逆用之神的运用法则(SemanticEntry):
    """
    - **原文（source_text）**：
  是以善而顺用之，则财喜食神以相生，生官以护财；官喜透财以相生，生印以护官；印喜官煞以相生，劫财以护印；食喜身旺以相生，生财以护食。不善而逆用之，则七煞...
    """
    
    original_text: str = """- **原文（source_text）**：
  是以善而顺用之，则财喜食神以相生，生官以护财；官喜透财以相生，生印以护官；印喜官煞以相生，劫财以护印；食喜身旺以相生，生财以护食。不善而逆用之，则七煞喜食神以制伏，忌财印以资扶；伤官喜佩印以制伏，生财以化伤；阳刃喜官煞以制伏，忌官煞之俱无；月劫喜透官以制伏，利用财而透食以化劫。此顺逆之大路也。

- 原注（原文注解）：
  　　本段具体列出顺用与逆用的基本配合法则，可视为“用神运用纲要”：
  - 财格：以食生财，以官护财；
  - 官格：以财生官，以印护官；
  - 印格：以官煞生印，以劫财护印；
  - 食格：以旺身生食，以财护食；
  - 煞格：以食神制服煞，忌财印去扶煞；
  - 伤官格：以印制伤，以财化伤；
  - 阳刃格：喜官煞制刃，忌刃失制；
  - 月劫格：喜官制劫，用财配食化劫。

- 分字分词释义：
  - 护财/护官/护印/护食：用另一喜神来保护主用神不受克泄破坏。
  - 制伏：通过克制来制服忌神，使其不致为害。
  - 化伤：通过财星等，把伤官的克性转化为有用的生克关系。
  - 化劫：用官制劫，用财食引导劫财之力，使之参与正向结构。

- **规范化释义（primary_lang_explained）**：
  作者在这里把顺格与逆格的基本用法用极简的几句话概括出来。大意是：
  - 顺用之神：
    - 财格：喜见食神来生财，再以官星来保护财（防止财被过分劫耗）；
    - 官格：喜透财来生官，再以印星护官（防止官星过弱或被伤）；
    - 印格：喜官煞来生印，再以劫财护印（防止印星被财所损）；
    - 食格：喜日主有力以生食，再用财星护食（防止食神受克或虚浮）。
  - 逆用之神：
    - 煞格：喜食神制服七煞，忌财印来扶煞；
    - 伤官格：喜佩印以制伤，再以财来化伤；
    - 阳刃格：喜官煞制刃，最忌刃而无官煞制伏；
    - 月劫格：喜官来制月劫，再借财与食把劫财之力引导出去。

-  这些看似简短的板书，其实是用神运用的大纲。后文所有关于用神成败、救应的细细展开，都是在这些原则的基础上做具体变化。

- **完整对等诠释（secondary_lang_full）**：  
  This compressed passage sketches the main operating rules for each type of pattern. For the "favourable" group, the principle is that what is used must both be nourished and guarded. In a Wealth pattern, Food God should generate Wealth and Officer should stand guard over it so that it is not stripped away. In an Officer pattern, Wealth is expected to feed Officer, while Resource protects Officer from being damaged. In a Resource pattern, Officer or Killing are allowed to generate Resource, but Rob Wealth must be present to shield Resource from being drained by ordinary Wealth. In a Food pattern, a strong Day Master produces Food, and Wealth in turn protects that Food from control or dispersion.

  For the "adverse" group, the core idea is control and transformation. In a Killing pattern, Food God must be present to restrain Killing, and we must beware of Wealth or Resource that would instead strengthen the Killing. In a Hurting Officer pattern, Resource is needed to subdue Hurting Officer, while Wealth can channel its sharp, attacking nature into productive uses. In a Blade pattern, Officer and Killing should check the Blade; what is feared is a Blade that runs unrestrained. In a Month Rob pattern, Officer must control Rob, and Wealth together with Food can draw off Rob's energy into more constructive channels. All later discussions of success, failure and rescue of the Useful God are elaborations on this basic map of "who should feed whom, who should protect whom, and who must keep whom in check".

- 详细解说：
  - 顺神要“生而有护”，不能只有生、不设护；逆神要“制而能化”，不能只有制、不设化。
  - 财官印食的相生相护，是传统“中正格局”的基础；煞伤劫刃的制化则是“偏格成贵”的关键。
  - 用神体系本质上是一个“能量流动与保护机制”的设计，不是孤立的几颗星。

- 核心要点：
  - 财格：食生财、官护财；
  - 官格：财生官、印护官；
  - 印格：官煞生印、劫护印；
  - 食格：身生食、财护食；
  - 煞格：食制煞、忌财印扶煞；
  - 伤官格：印制伤、财化伤；
  - 刃格：官煞制刃、忌刃失制；
  - 月劫格：官制劫、财食化劫。

- 应用推演：
  1) 认清本局属于哪一类格局（财官印食煞伤劫刃）；
  2) 检查“生与护”是否齐备，或“制与化”是否齐备；
  3) 看岁运是否强化了“护神/制神”，还是反而增强了忌神；
  4) 由此判断格局是否由顺入逆、由逆成顺，或成败之间如何摇摆。

- 反例与边界：
  - 只看“见财、见官”便喜，不看有无护神与制神；
  - 把煞、伤、刃一概视为破局，不考虑其是否已得食印官财之制化。

- 小例（示意）：
  - 一命财格，得食神生财、官星护财，岁运再逢财生官，多主财官两美；
  - 一命煞格，身强煞重而不见食印，运再见财印扶煞，多主祸患。

- 校勘与字词辨析：
  - “劫才”原文作“劫才”，即“劫财”，本精校在释义中统一为“劫财”。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_276]` `[trigger: 命理要义]` `[factor_trigger: benjie_hexin_mingli AND lunshu_yaodian]` `[role: 主干]` 本节核心命理论述。 → 《子平真诠》#第64节
  - `[ns_zpzy_277]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_278]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_279]` `[trigger: 忌神来犯]` `[factor_trigger: jishen_laifan=true AND result=zaihuo_nanmian]` `[role: 主干]` 忌神来犯，灾祸难免。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "此顺逆之大路：顺用之神与逆用之神的运用法则"
    factor_refs: list = ['shunyong_zhishen', 'niyong_zhishen', 'hushen', 'zhishen', 'huashen', 'engine_id', 'geju_zhenying', 'bazi_rule_engine', 'shenghu_liandao', 'bazi_rule_engine', 'zhihua_liandao', 'bazi_rule_engine', 'suiyun_hushen_effect', 'bazi_rule_engine', 'shunni_zhuanhuan', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_081', 'shenghu_liandao', 'rel_zpzq_082', 'zhihua_liandao', 'rel_zpzq_083', 'suiyun_hushen_effect', 'evi_zpzq_081', 'shenghu_liandao', 'rule_caige_shenghu', 'evi_zpzq_082', 'zhihua_liandao', 'rule_shage_zhihua', 'evi_zpzq_083', 'shunni_zhuanhuan', 'rule_shunni_dalu', 'concept_supply_chain', 'concept_control_transform']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_此顺逆之大路_顺用之神与逆用之神的运用法则_001_L1",
    )
    version: str = "1.0.0"
