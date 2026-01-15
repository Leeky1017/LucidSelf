"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619862
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
    semantic_id="qtbj_v1.0.0_8__三月甲木的特殊格局_财格与杂气_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 8三月甲木的特殊格局财格与杂气(SemanticEntry):
    """
    - **原文（source_text）**：
  或柱中全无一水，戊己透干，支成土局，又作弃命从才，因人而致富贵，妻子有能。
  或见戊己，及比劫多者，名为杂气夺才，此人劳碌到老，无驭内之权。女命合此...
    """
    
    original_text: str = """- **原文（source_text）**：
  或柱中全无一水，戊己透干，支成土局，又作弃命从才，因人而致富贵，妻子有能。
  或见戊己，及比劫多者，名为杂气夺才，此人劳碌到老，无驭内之权。女命合此，女掌男权，贤能内助，若比劫重见，淫恶不堪。
  或支成金局，方可用丁，不然，三月无用丁之法。惟有先庚后壬取用。
  书曰：甲乙生寅卯，庚辛干上逢，离南推富贵，坎地却为凶。

- **分字分词释义**：
  - **弃命从才**：放弃自身气势顺从财星 / 身弱从财 / 因人致富
  - **因人而致富贵**：因为他人而获得富贵 / 妻财或岳家 / 靠人成事
  - **妻子有能**：妻子很有能力 / 从财格特征 / 妻星有力
  - **杂气夺才**：杂气月比劫争夺财星 / 辰戌丑未月 / 财多身弱
  - **驭内之权**：管理妻子的权力 / 惧内 / 怕老婆
  - **女掌男权**：女人掌握男人的权力 / 女强男弱 / 财旺身弱女命
  - **淫恶不堪**：淫乱邪恶不可收拾 / 比劫太重 / 女命凶象
  - **离南**：南方火运 / 食伤制杀 / 吉运方向
  - **坎地**：北方水运 / 泄杀生身 / 凶运方向

- **规范化释义（primary_lang_explained）**：
  如果柱中全无一点水，戊己土透出天干，地支合成土局，这叫“弃命从财”，因为他人（妻子或岳家）而获得富贵，妻子很有能力。
  如果见到戊己土，但比肩劫财也很多，这叫“杂气夺财”（或比劫争财），此人劳碌到老，没有管理妻子的权力（怕老婆）。女命符合这种情况，是女人掌男人权，能做贤能的内助；但如果比劫重重再见，则淫恶不堪。
  如果地支合成金局，才可以用丁火（制杀），否则，三月没有用丁火的方法（常规不用火）。只有先用庚金后用壬水这一条路。
  古书说：甲乙木生在寅卯月，如果天干遇到庚辛金，行南方火运推断为富贵（食伤制杀），行北方水运却是凶险（泄杀生身太和缓或沉埋）。

- **完整对等诠释（secondary_lang_full）**：
  If there is absolutely no Water in the pillars, and Wu/Ji Earth are revealed with branches forming an Earth frame, it is "Abandon Life Follow Wealth". One achieves wealth and nobility through others (often wife/in-laws), and the wife is capable.
  If Wu/Ji are seen but Parallel/Rob Wealth are also numerous, it is called "Mixed Qi Snatching Wealth". This person toils until old age and has no authority over his wife. For a female life fitting this, she holds the man's power and is a capable helpmate; but if Parallel/Rob Wealth appear repeatedly, she becomes unbearably lewd and wicked.
  Only if branches form a Metal frame can Ding Fire be used (to control Metal); otherwise, there is no method for using Ding in the 3rd Month. The only way is to use Geng first, then Ren.
  The book says: Jia/Yi born in Yin/Mao, meeting Geng/Xin on the stems, infer wealth and nobility in the South (Fire luck), but the North (Water luck) is ominous.

- **核心要点**：
  - **从财格**：土局无水，因妻致富。
  - **财多身弱/比劫争财**：劳碌，惧内。
  - **特殊用丁**：仅在支成金局（杀重）时，用丁制杀。
  - **古诀辨析**：寅卯见金（身旺杀浅），喜南离（伤官制杀/木火通明），忌北坎（水泄杀生身，使杀无力）。

- **详细解说**：
  - 辰月是杂气（土木水），若土气极旺成局且无水木破格，可从财。
  - 若比劫多，则是普通偏财格或杂气财官，此时比劫夺财，主贫劳。
  - “三月无用丁之法”：因为辰月阳气已壮，木气已竭，不再需要火来泄秀或调候（除非金太重需火制）。这与寅卯月不同。
  - 最后的书曰其实是对正二月（寅卯）的补充，强调身旺杀浅宜制（南运），不宜化（北运）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_108]` `[trigger: 辰月从财]` `[factor_trigger: month_chen AND tiangan_jia AND pattern_abandon_life_follow_wealth AND dizhi_earth_frame AND NOT element_water]` `[role: 主干]` 柱中全无一水，戊己透干，支成土局，又作弃命从才，因人而致富贵。 → 《穷通宝鉴·三春甲木》#3.8
  - `[ns_qttbj_109]` `[trigger: 杂气夺财]` `[factor_trigger: month_chen AND tiangan_jia AND element_earth AND shishen_robbery_excessive]` `[role: 条件分支]` 见戊己，及比劫多者，名为杂气夺才，此人劳碌到老，无驭内之权。 → 《穷通宝鉴·三春甲木》#3.8
  - `[ns_qttbj_110]` `[trigger: 女命比劫]` `[factor_trigger: gender_female AND mixed_qi_snatching_wealth AND (shishen_robbery OR shishen_robbery_excessive)]` `[role: 条件分支]` 女命合此，女掌男权，贤能内助，若比劫重见，淫恶不堪。 → 《穷通宝鉴·三春甲木》#3.8
  - `[ns_qttbj_111]` `[trigger: 辰月用丁]` `[factor_trigger: month_chen AND tiangan_jia AND dizhi_metal_frame AND tiangan_ding]` `[role: 例外处理]` 支成金局，方可用丁，不然，三月无用丁之法。 → 《穷通宝鉴·三春甲木》#3.8
  - `[ns_qttbj_112]` `[trigger: 春木运势]` `[factor_trigger: (month_yin OR month_mao) AND element_wood AND (tiangan_geng OR tiangan_xin)]` `[role: 总结]` 甲乙生寅卯，庚辛干上逢，离南推富贵，坎地却为凶。 → 《穷通宝鉴·三春甲木》#3.8"""
    normalized_text_zh: str = """"""
    subject: str = "8. 三月甲木的特殊格局（财格与杂气）"
    factor_refs: list = ['pattern_abandon_life_follow_wealth', 'mixed_qi_snatching_wealth', 'authority_over_wife', 'southern_fire_luck', 'northern_water_luck']
    
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
        l1_anchor="qtbj_v1.0.0_8__三月甲木的特殊格局_财格与杂气_001_L1",
    )
    version: str = "1.0.0"
