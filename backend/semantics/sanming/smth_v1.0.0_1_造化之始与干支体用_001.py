"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066733
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
    semantic_id="smth_v1.0.0_1_造化之始与干支体用_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1造化之始与干支体用(SemanticEntry):
    """
    - 原文（source_text）：
  元一气兮先天，禀清浊兮自然。著三才以成象，播四气以为年。
  以干为禄，向背定其贫富；以支为命，详逆顺以循环。
  运行则一辰十岁，折除乃三日为年。精休旺以为...
    """
    
    original_text: str = """- 原文（source_text）：
  元一气兮先天，禀清浊兮自然。著三才以成象，播四气以为年。
  以干为禄，向背定其贫富；以支为命，详逆顺以循环。
  运行则一辰十岁，折除乃三日为年。精休旺以为妙，穷通变以为玄。
  其为气也，将来者进，成功者退，如蛇在灰，如鳝在尘。
  其为有也，是从无而立有；其为无也，天垂象以示文。
  其为常也，立仁立义；其为事也，或见或闻。

- 分字分词释义：
  - **元一气**：太极元气。
  - **四气**：春夏秋冬。
  - **干为禄**：天干主禄（向背：向禄为富，背禄为贫）。
  - **支为命**：地支主命（逆顺：阴阳顺逆，十二宫循环）。
  - **一辰十岁**：大运一柱管十年。
  - **三日为年**：起运法，三天折算一岁。
  - **将来者进**：进气（如春木）。
  - **成功者退**：退气（如秋木）。
  - **蛇在灰/鳝在尘**：比喻失势（火死于灰，水死于尘，蛇鳝皆属火/水类，失势则困）。

- **规范化释义（primary_lang_explained）**：
  元始的一气是先天的根本，秉承清浊之气自然形成万物。三才（天地人）成象，四时（春夏秋冬）成岁。
  天干代表禄，看向背（向禄、背禄）来定贫富；地支代表命，详察顺逆（十二宫生死）来定循环。
  大运一辰管十年，起运以三日折算一岁。精通五行休旺是妙处，穷究通变之理是玄机。
  气数之道，将来者（进气）进，成功者（旺极）退。如蛇在灰中，鳝在尘中，皆因失势而困顿。
  有生于无，天垂象以示吉凶。
  常道在于仁义，人事在于见闻。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Creation's Beginning and Stem-Branch Substance-Function" from the Xiao-Xi Rhapsody:

  - Original one qi先天, receives clear-turbid自然. Three talents成象, broadcasts four qi为年.
  - Using Stem as Salary, towards-back定贫富; using Branch as Fate, details逆顺循环.
  - Luck travels one辰ten years, fold-remove three days as year.
  - Its being qi: coming ones advance, successful ones retreat; like snake in ash, like eel in dust.
  - Key: Stem represents Salary (career/wealth); Branch represents Fate (life path); advancing qi is auspicious, retreating qi is inauspicious.

- 核心要点：
  - **干支定位**：干禄支命。
  - **起运法**：三日一岁。
  - **进退气**：进气为吉，退气为凶。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_029]` `[trigger: 元一气兮]` `[factor_trigger: yuanyiqi_xi AND bingqingzhuo_ziran]` `[role: 主干]` 元一气兮先天，禀清浊兮自然。著三才以成象，播四气以为年。 → 《三命通会》卷十一#造化之始与干支体用
  - `[ns_smth_11_030]` `[trigger: 干禄支命]` `[factor_trigger: ganlu_zhiming AND xiangbei_dingfu]` `[role: 主干依赖]` 以干为禄，向背定其贫富；以支为命，详逆顺以循环。 → 《三命通会》卷十一#造化之始与干支体用
  - `[ns_smth_11_031]` `[trigger: 蛇灰鳝尘]` `[factor_trigger: shehui_shanchen AND jingtui_zhiqi]` `[role: 条件分支]` 其为气也，将来者进，成功者退，如蛇在灰，如鳝在尘。 → 《三命通会》卷十一#造化之始与干支体用
  - `[ns_smth_11_032]` `[trigger: 有无之道]` `[factor_trigger: youwu_zhidao AND tianchuixiang_shiwen]` `[role: 总结]` 其为有也，是从无而立有；其为无也，天垂象以示文。 → 《三命通会》卷十一#造化之始与干支体用"""
    normalized_text_zh: str = """"""
    subject: str = "1 造化之始与干支体用"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_15', 'bazi_semantic', 'bazi_state_factor_57', 'bazi_semantic', 'bazi_state_factor_58', 'bazi_semantic', 'bazi_state_factor_59', 'bazi_semantic', 'bazi_state_factor_60', 'bazi_semantic', 'bazi_factor_24', 'bazi_semantic', 'source_ref', 'rel_smth_11_022', 'ganlu_zhiming', 'rel_smth_11_023', 'jinqi_shengfa', 'rel_smth_11_024', 'zhechu_qiyun', 'evi_smth_11_022', 'ganlu_zhiming', 'rule_ganlu_zhiming1', 'evi_smth_11_023', 'jinqi_tuiqi', 'rule_jinqi_tuiqi1', 'evi_smth_11_024', 'zhechu_qiyun', 'rule_zhechu_qiyun1', 'map_smth_11_015', 'map_smth_11_016']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_1_造化之始与干支体用_001_L1",
    )
    version: str = "1.0.0"
