"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523880
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
    semantic_id="zpzq_v1.0.0_八字用神_专求月令_以日干配月令地支_而生克不同_格局分焉_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 八字用神专求月令以日干配月令地支而生克不同格局分焉(SemanticEntry):
    """
    - **原文（source_text）**：
  八字用神，专求月令，以日干配月令地支，而生克不同，格局分焉。财官印食，此用神之善而顺用之者也；煞伤劫刃，用神之不善而逆用之者也。当顺而顺，当逆而逆，配...
    """
    
    original_text: str = """- **原文（source_text）**：
  八字用神，专求月令，以日干配月令地支，而生克不同，格局分焉。财官印食，此用神之善而顺用之者也；煞伤劫刃，用神之不善而逆用之者也。当顺而顺，当逆而逆，配合得宜，皆为贵格。

- 原注（原文注解）：
  　　本段开宗明义：
  - 用神之求，以月令为纲——先看月令藏何神，再以日干配之；
  - 财、官、印、食属于“善神”，顺势而用；
  - 煞、伤、劫、刃属于“恶神”，逆势而用；
  - 能顺则顺、当逆则逆，只要配合得宜，皆可成贵格。

- 分字分词释义：
  - 专求月令：以月令为提纲，用神从月令出发寻找。
  - 日干配月令地支：以日主与月令之关系，判定“用何神”。
  - 格局分焉：由用神不同，分出财格、官格、印格、食格等各种格局。
  - 善而顺用：指顺势而用之神，多为财、官、印、食。
  - 不善而逆用：指逆势而用之神，多为煞、伤、劫、刃。
  - 当顺而顺，当逆而逆：顺则扶助，逆则抑制，各有其法。

- **规范化释义（primary_lang_explained）**：
  论命首先要定"用神"，而用神的根本就在月令。也就是说，要先看出生月份的地支当令何神，再看日干与这一位"月令之神"的生克关系，由此定出到底应当用财、用官、用印、用食，还是用煞、用伤、用劫、用刃。财官印食等大多数被视为"顺用之神"，一般顺势而用；煞伤劫刃则多为"逆用之神"，需要通过制伏或化用的方式用之。命中局势既定，遇到适合顺用的局，就顺着去用；遇到适合逆用的局，就带着制化去用。只要用得其当，哪怕是煞刃伤劫，也可以成格成贵。

- **完整对等诠释（secondary_lang_full）**：  
  In this doctrine the search for the Useful God always begins from the Month branch. We first ask which star actually holds command in the month, then consider how the Day stem stands in the cycle of generation and control with respect to that star. From this pairing we decide whether the chart should be read as using Wealth, Officer, Resource, Food, or instead Killing, Hurting Officer, Rob Wealth or Yang Blade. The first group – Wealth, Officer, Resource and Food – are normally treated as "favourable" gods, applied by following the existing tendency of the qi. The second group – Killing, Hurting Officer, Rob Wealth and Blade – are "adverse" gods that must be handled through control and transformation.

  Once the overall situation of the chart is set, some patterns call for a straightforward supportive use of the favourable gods, while others require us to harness adverse stars in a contrary way. Where a favourable god is central, we feed and protect it; where an adverse god plays the lead, we check and redirect it so that it serves structure rather than destroying it. The same star can thus either lift the pattern or break it, depending on whether it is being used in accordance with its proper role under the Month framework.

- 详细解说：
  - 真正的“用神观”，重在“以月令为纲、以日主为体”，不是随意从某颗喜神中挑一个来叫“用神”。
  - 善神与恶神，只在“顺用/逆用”之别，不在本性绝对善恶；用法得当，皆可为贵。
  - “当顺而顺，当逆而逆”一句，浓缩了后文关于顺格与逆格的全部精神。

- 核心要点：
  - 用神起点：专求月令，以日干配月令地支的生克为纲。
  - 善神四类：财、官、印、食，多顺用；
  - 恶神四类：煞、伤、劫、刃，多逆用；
  - 格局之分，全系于“用何神、如何用”两大问题。

- 应用推演：
  1) 判月令：明确月令当令何神，对日干是财、官、印、食或煞、伤、劫、刃；
  2) 定格局：据此判断是财格、官格、印格、食格，还是煞格、伤官格、刃格、月劫格；
  3) 判顺逆：财官印食为顺，煞伤劫刃为逆，分别确定“扶、制、化”的路线；
  4) 在此基础上，再看四柱透藏与岁运，评估成败高低。

- 反例与边界：
  - 不从月令立用，随意以“命中我喜欢什么”为用神，导致判断完全脱纲。
  - 把煞刃伤劫一概视为“不可用神”，不知逆用亦可成格。

- 小例（示意）：
  - 甲木生于午月，午中丁己为官财，当以官财为用；若日主强，则顺用财官成格；若日主弱，则仍以官财为纲，但需印比扶身。

- 校勘与字词辨析：
  - “财官印食，此用神之善而顺用之者也；煞伤劫刃，用神之不善而逆用之者也”：此处“善/不善”重在“顺/逆”，不宜简单按道德善恶理解。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_272]` `[trigger: 命理要义]` `[factor_trigger: benjie_hexin_mingli AND lunshu_yaodian]` `[role: 主干]` 本节核心命理论述。 → 《子平真诠》#第61节
  - `[ns_zpzy_273]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_274]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_275]` `[trigger: 喜神来助]` `[factor_trigger: xishen_laizhu=true AND result=shishi_shunsui]` `[role: 主干]` 喜神来助，事事顺遂。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "八字用神，专求月令，以日干配月令地支，而生克不同，格局分焉"
    factor_refs: list = ['yueling', 'tigang', 'jianlu', 'yuejie', 'engine_id', 'yueling_zhushen_id', 'bazi_rule_engine', 'rizhu_yueling_rel', 'bazi_rule_engine', 'jianlu_yuejie_flag', 'bazi_rule_engine', 'yongshen_clarity', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_079', 'yueling_zhushen_id', 'rel_zpzq_080', 'rizhu_yueling_rel', 'evi_zpzq_079', 'yueling', 'rule_zhuanqiu_yueling', 'evi_zpzq_080', 'rizhu_yueling_rel', 'rule_geju_fen', 'concept_environment', 'concept_pivot']
    
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
        l1_anchor="zpzq_v1.0.0_八字用神_专求月令_以日干配月令地支_而生克不同_格局分焉_001_L1",
    )
    version: str = "1.0.0"
