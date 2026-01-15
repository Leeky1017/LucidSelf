"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523988
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
    semantic_id="zpzq_v1.0.0_变之而善_忌化为喜的两条路径_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 变之而善忌化为喜的两条路径(SemanticEntry):
    """
    - **原文（source_text）**：
  变之而善，其格愈美；变之不善，其格遂坏。何谓变之而善？如辛生寅月，逢丙而化财为官；壬生戌月逢辛而化煞为印。癸生寅月，不专以煞论。此二者，以透出而变化者...
    """
    
    original_text: str = """- **原文（source_text）**：
  变之而善，其格愈美；变之不善，其格遂坏。何谓变之而善？如辛生寅月，逢丙而化财为官；壬生戌月逢辛而化煞为印。癸生寅月，不专以煞论。此二者，以透出而变化者也。癸生寅月，月令伤官秉令，藏甲透丙，会午会戌，则寅午戌三合，伤化为财；加以丙火透出，完全作为财论。即使不透丙而透戊土，亦作财旺生官论，盖寅午戌三合变化在前，不作伤官见官论也。乙生寅月，月劫秉令，会午会戌，则劫化为食伤，透戊则为食伤生财，不作比劫争财论。此二者，因会合而变化者。因变化而忌化为喜，为变之善者。

- 原注（原文注解）：
  　　本段集中说明“变之而善”的两种典型途径：
  - 一是**透干之变**：某藏干透出后，使原本不利之神改头换面，如辛寅化财为官、壬戌化煞为印；
  - 二是**会合之变**：三合、三会等局先行定性，使原本忌神在大局中化身为喜用，如癸寅、乙寅因寅午戌火局而使伤化财、劫化食伤。

- 分字分词释义：
  - 变之而善，其格愈美：
    - 变化方向有利格局，使原有用神体系更完整，格局反而提升。
  - 辛生寅月，逢丙而化财为官：
    - 辛金以寅中丙火本为财，丙透干并得势时，可转而为官，用官制身，财性退居次要。
  - 壬生戌月逢辛而化煞为印：
    - 壬水日主生戌月，戌中辛本为七煞，若辛透而能生壬或配合印局，则煞转为印用。
  - 癸生寅月，不专以煞论：
    - 癸水生寅，寅中甲本为七煞，但作者提醒不必一味以煞论，须看三合会局之后的实际变化.
  - 伤化为财：
    - 原为伤官之神，在三合局中角色转为财，使本局从伤官格转为财格或财官格.
  - 劫化为食伤：
    - 原为比劫之神，在三合局中改为食神或伤官，性质由“争夺”转为“泄秀生财”。

- **规范化释义（primary_lang_explained）**：
  变化不一定都是坏事，有些变化反而令格局更上一层楼。作者把“变之善”分为两大类：

  1）**透干之变**

  - 辛日生于寅月，本以寅中丙火为辛金之财；但若丙火透干有力，其一方面固然仍是财，另一方面却有机会成为辛金之官——尤其当金水不泛滥、火有节度时，“财化官”的结构出现，辛金得其制约而贵格可成；
  - 壬日生于戌月，戌中辛金按常理为七煞；但若辛金透干适度，又能生出壬水或配合印星，则此辛煞反而化为生身之印，用煞生印来护身，格局由偏凶转为清贵.

  2）**会合之变**

  - 癸日生于寅月，表面看是癸水逢寅中甲煞，似乎“煞重可虑”；然若命局中再见午、戌，成寅午戌火局，则寅中伤官之气先化为火财，加之丙火透出，整个格局可以按“财旺生官”来理解，而不必拘泥“伤官见官”；
  - 乙日生于寅月，寅中甲比、丙食、戊财，若再会午戌，同样成火局，则原本的月劫比肩反而化成食伤；若天干透戊，则成“食伤生财”格，而不再是“比劫争财”，由夺转生.

  这类变化的共同点在于：原本令人头疼的忌神（煞、伤、比劫等），通过透干或会合，角色被重新定义，转而承担起生身、生财、成格之功，是典型的"忌化为喜"。

- **完整对等诠释（secondary_lang_full）**：  
  Favourable transformation means that, after change, the overall structure becomes cleaner and more elegant instead of merely “a little less bad”. There are two main pathways by which a harmful star can be turned into a helpful one. 
  The first is **through stems surfacing from the branches**. For example, when Xin Metal is born in Yin month and Bing Fire later appears on the stems, the Wealth represented by Bing can be taken as the new governing star and the pattern shifts toward “Wealth producing Officer”, rather than remaining stuck in its original mixed state. Likewise, when Ren Water is born in Xu month and Xin Metal surfaces, the originally threatening Seven Killings can be reinterpreted as Resource: Metal generates Water and forms a protective chain around the Day Master.
  The second pathway works **through full combinations and elemental bureaus**. When Gui Water is born in Yin month, it would be simplistic to treat the Yin branch only as Killing. If subsequent branches form the complete Yin–Wu–Xu Fire bureau, the Hurting Officer contained in Yin is gathered into the Fire configuration and effectively becomes Wealth. Should Bing Fire also appear on the stems, the chart may be judged as “Wealth flourishing and producing Officer”; even if Bing is absent but Wu Earth surfaces instead, we can still read it as “strong Wealth generating Officer”, because the Fire bureau has already redefined the underlying structure and the pattern can no longer be called “Hurting Officer seeing Officer”.
  A similar logic applies when Yi Wood is born in Yin month and Rob Wealth holds command. If Wu and Xu join to complete the Fire bureau, the Rob Wealth is drawn into the bureau and turns into Food or Hurting Officer; once Wu Earth further appears on the stems, this becomes a clear case of “Food and Hurting producing Wealth”, rather than “Rob Wealth fighting for Wealth”. In all such examples, what used to be a troublesome malefic—Killing, Hurting Officer, or Rob Wealth—is absorbed into a new chain of production and protection, and its function is reassigned from damage to support. This is what the text calls “transforming the inauspicious into the auspicious”.

- 详细解说：
  - “变之而善”并非巧言装饰，而是合局、透干之后**格局中心的真正移动**；
  - 忌神本身并不绝对可恶，关键在于是否有机会被纳入用神链条中，成为“有情”的一环；
  - 从实务角度看，很多命局的高贵，往往正是建立在这种“转祸为福”的变化上.

- 核心要点：
  - 透干变化看三点：
    1) 谁从藏中透出？
    2) 透出后与日主、月令的生克关系是否更合理？
    3) 是否形成官印相生、食财相生等经典链条？
  - 会合变化看两点：
    1) 合局是否真成（支全、得令、有力）？
    2) 合局定性之后，原本的忌神应按新定性重判，不可仍照旧格名.

- 应用推演：
  1) 对原局先作“静态判断”：不看变化，只按原用神体系定格；
  2) 再查透干与会合，评估有无“财化官”“煞化印”“伤化财”“劫化食伤”等变化路径；
  3) 对于找到的变化，判断其是否真成、有力；
  4) 若变化之善足以主导格局，则以新格为主、旧格为辅；
  5) 在岁运推断中，重点观察何时条件具足，使这类“善变”真正落地.

- 反例与边界：
  - 只要看到合局就自动认为“忌化为喜”，不问是否得令、有根；
  - 把“辛逢丙”“壬逢辛”一律当成“化财为官、化煞为印”，忽略日主强弱与全局配合；
  - 对癸寅、乙寅等局，死扣“煞”“比劫”之名，不肯因合局而改变评价.

- 小例（示意）：
  - 一命癸日生寅月，支成寅午戌火局，干透丙、戊，原本的寅中甲煞被火局吸纳，整体表现为“财旺生官”，主财官两美，事业中多有“由压力转成机会”的体验.

- 校勘与字词辨析：
  - “癸生寅月，不专以煞论”：本精校在释义中特别强调此句，视为对“见煞必凶”之俗见的重要纠偏；
  - “不作伤官见官论”“不作比劫争财论”：皆提示读者须以变化后的大局为准，而非以旧格名裁之.

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_294]` `[trigger: 用神纯杂]` `[factor_trigger: (yongshen_chuncu AND geju_gao) OR (yongshen_zaluan AND geju_di)]` `[role: 主干]` 用神纯粹格局高，杂乱则低。 → 《子平真诠》#上卷
  - `[ns_zpzy_295]` `[trigger: 忌神有制]` `[factor_trigger: jishen_youzhi=true AND xiong_hua_wei_ji]` `[role: 主干]` 忌神有制，凶化为吉。 → 《子平真诠》#上卷
  - `[ns_zpzy_296]` `[trigger: 用神有力]` `[factor_trigger: yongshen_youli=true AND result=fugui_keqi]` `[role: 主干]` 用神有力，富贵可期。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "变之而善：忌化为喜的两条路径"
    factor_refs: list = ['tougan_zhibian', 'huihe_zhibian', 'jihuaweixi', 'shanghuaweicai', 'jiehuashishang', 'engine_id', 'jihua_lujing', 'bazi_rule_engine', 'shanbian_wanbei', 'bazi_rule_engine', 'juese_chongzhi', 'bazi_rule_engine', 'bianhua_zhudao', 'bazi_rule_engine', 'wupan_shanbian', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_108', 'tougan_zhibian', 'rel_zpzq_109', 'huihe_zhibian', 'rel_zpzq_110', 'shanbian_wanbei', 'evi_zpzq_101', 'tougan_zhibian', 'rule_caihuaguan', 'evi_zpzq_102', 'huihe_zhibian', 'rule_shanghuacai_huiju', 'concept_transformation', 'concept_upgrade']
    
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
        l1_anchor="zpzq_v1.0.0_变之而善_忌化为喜的两条路径_001_L1",
    )
    version: str = "1.0.0"
