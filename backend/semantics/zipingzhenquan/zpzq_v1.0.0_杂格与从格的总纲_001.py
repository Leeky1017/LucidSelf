"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492449
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
    semantic_id="zpzq_v1.0.0_杂格与从格的总纲_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 杂格与从格的总纲(SemanticEntry):
    """
    - **原文（source_text）**：
  四十七、论杂格。
  杂格者，月令无用，以外格而用之，其格甚多，故谓之杂。大约要干头无官无煞，方成格，如有官煞，则自有官煞为用，列外格矣。若透财尚可取...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十七、论杂格。
  杂格者，月令无用，以外格而用之，其格甚多，故谓之杂。大约要干头无官无煞，方成格，如有官煞，则自有官煞为用，列外格矣。若透财尚可取格，然财根深，或财透两位，则亦以财为重，不取外格也。

  试以诸格论之，有取五行一方秀气者，取甲乙全亥卯未、寅卯辰，又生春月之类，本是一派劫财，以五行各得其全体，所以成格，喜印露而体纯。如癸亥、乙卯、乙未、壬午，吴相公命是也。运亦喜印绶比劫之乡，财食亦吉，官煞则忌矣。

  有从化取格者，要化出之物，得时乘令，四支局全。如丁壬化木，地支全亥卯未、寅卯辰，而又生于春月，方为大贵。否则，亥未之月亦是木地，次等之贵，如甲戌、丁卯、壬寅、甲辰，一品贵格命也。运喜所化之物，与所化之印绶，财伤亦可，不利官煞。

  有倒冲成格者，以四柱列财官而对面以冲之，要支中字多，方冲得动。譬如以弱主邀强官，主不众则宾不从。如戊午、戊午、戊午、戊午，是冲子财也；甲寅、庚午、丙午、甲午，是冲子官也。运忌填实，余俱可行。

  有朝阳成格者，戊去朝丙，辛日得官，以丙戊同禄于巳，即以引汲之意。要干头无木火，方成其格，盖有火则无待于朝，有木财触戊之怒，而不为我朝。如戊辰、辛酉、戊子，张知县命是也。运喜土金水，木运平平，火则忌矣。

  有合禄成格者，命无官星，借干支以合之。戊日庚申，以庚合乙，因其主而得其偶。如己未、戊辰、戊辰、庚申，蜀王命是也。癸日庚申，以申合巳，因其主而得其朋，如己酉、癸未、癸未、庚申，起丞相命是也。运亦忌填实，不利官煞，理会不宜以火克金，使彼受制而不能合，余则吉矣。

  有弃命保财者，四柱皆财而身无气，舍而从之，格成大贵。若透印则身赖印生而不从，有官煞则亦无从财兼从煞之理，其格不成。如庚申、乙酉、丙申、乙丑，王十万命造也。运喜伤食财乡，不宜身旺。有弃命从煞者，四柱皆煞，而日主无根，舍而从之，格成大贵。若有伤食，则煞受制而不从，有印则印以化煞而不从。如乙酉、乙酉、乙酉、甲申，李侍郎命是也。运喜财官，不宜身旺，食伤则尤忌矣。

  有井拦成格者，庚金生三七月，方用此格。以申子辰冲寅午戌，财官印绶，合而冲之，若透丙丁，有巳午，以现有财官，而无待于冲，乃非井拦之格矣。如戊子、庚申、庚申、庚申，郭统制命也。运喜财，不利填实，余亦吉也。

  有刑合成格者，癸日甲寅时，寅刑巳而得财官，格与合禄相似，但合禄则喜以合之，而刑合则硬以致之也。命有庚申，则木被冲克而不能刑；有戊已字，则现透官煞而无待于刑，非此格矣。如乙未、癸卯、癸卯、甲寅，十二节度使命是也。运忌填实，不利金乡，余则吉矣。

  有遥合成格者，巳与丑会，本同一局，丑多则会巳而辛丑处官，亦合禄之意也。如辛丑、辛丑、辛丑、庚寅，章统制命是也。

  若命是有子字，则丑与子合而不遥，有丙丁戊已，则辛癸之官煞已透，而无待于遥，另有取用，非此格矣。至于甲子遥已，转辗求俣，似觉无情，此格可废，因罗御史命，聊复存之。为甲申、甲戌、甲子、甲子，罗御史命是也。

  若夫拱禄、拱贵、趋乾、归禄、夹戌、鼠贵、骑龙、日贵、日德、富禄、魁罡、食神时墓、两干不杂、干支一气、五行具足之类，一切无理之格，既置勿取。即古人格内，亦有成式，总之意为牵就，硬填人格，百无一是，徒误后学而已。乃若天地双飞，虽富贵亦有自有格，不全赖此。而亦能增重基格，即用神不甚有用，偶有依以为用，亦成美格。然而有用神不吉，即以为凶，不可执也。

  其于伤官伤尽，谓是伤尽，不宜一见官，必尽力以伤之，使之无地容身，现行伤运，便能富贵，不知官有何罪，而恶之如此？

  况见官而伤，则以官非美物，而伤以制之，又何伤官之谓凶神，而见官之为祸百端乎？予用是术以历试，但有贫贱，并无富贵，未轻信也，近亦见有大贵者，不知何故。然要之极贱者多，不得不观其人物以衡之。

- 原注（原文注解）：
  　本章总论“杂格”与若干外格、从格，核心意在纠偏：
  - **第一层**：给出“杂格”的定义——月令无用、须另以外格为用；
  - **第二层**：逐一列举一方秀气、从化、倒冲、朝阳、合禄、弃命从财/从煞、井栏、刑合、遥合等格局；
  - **第三层**：批判大量“无理之格”，并指出“伤官伤尽”等多种成式不可执信。

  几个关键总则：
  1) 杂格成立的前提：
     - 月令本身无法作为用神（“月令无用”）；
     - 干头不得有官煞透出——一有官煞可用，即应以官煞为主，而不取外格；
     - 若财透而根深，则以财格为重，同样不必别立杂格.
  2) 杂格仍不离五行正理：
     - 曲直仁寿（木一方）、炎上（火一方）、从革（金一方）、稼穑（土一方）、润下（水一方）等，皆从“一行偏旺”出发，但仍遵循气势规律；
     - 从化格、从财格、从煞格等从格，也是“气势偏旺到某极值”的特殊形态，而非凭空造格.
  3) 对传统格名的批判：
     - 对拱禄、拱贵、趋乾、归禄、鼠贵、骑龙等多数“名目格”持保留态度，认为多属牵强附会；
     - 特别指出：
       - “伤官伤尽”被过度神秘化，实则应仍回到“伤官制何物、用何神”的结构上来.

- 分字分词释义：
  - 杂格：相对于以月令为主的“正格”，指月令无用、另从外在气势取格的局面；
  - 外格：不循常规财官印食用神链条，而从某一偏旺气势、合化、倒冲等取用的格局；
  - 从格：日主明显无力而“弃命从之”，如从财、从煞等；
  - 一方秀气：某一五行在四支成局、得令得地，气势高度集中；
  - 倒冲：以对冲方式形成“宾主对峙”的局面，如四柱列财官而对面以冲之；
  - 朝阳、合禄等：传统术数中对特定干支组合的命名，本章多做结构化重释.

- **规范化释义（primary_lang_explained）**：
  可以把本章理解为对“特殊格局与名目格”的系统梳理：
  - 一方面承认：
    - 气势偏旺到一定程度，就会出现非常规的“从格、杂格”；
    - 例如从财、从煞、从化、曲直仁寿、炎上、从革、稼穑、润下等，都有其合理性；
  - 另一方面强调整理：
    - 许多后世所传“格名”，只是对某些现象的粗略命名，若离开五行气势与用神结构，便失去意义；
    - 不应为了“凑格名”而牵强附会，从而误导后学.

  文末对“伤官伤尽”的批评，尤其值得注意：
  - 祖师亲自指出，曾用此说法多方试验，所得多为贫贱，并非富贵；
  - 说明若脱离具体结构，只凭“伤尽/官尽”的名词来断吉凶，是极不可靠的.

- **完整对等诠释（secondary_lang_full）**：  
  Miscellaneous and from‑patterns are not mysterious extra categories floating above the system; they are what appears when the regular Month‑Mandate cannot be used and another current of momentum truly dominates the chart. Configurations such as Curved-Straight Benevolence, Blazing Upward, Following-Reform, Harvest-Planting, and Moistening Downward, or following Wealth, following Killing and following transformation, are all cases where a single element or chain has become so strong that the weak Day Master must either submit to it or be read in its shadow. Their legitimacy lies in the real flow of Five‑Element momentum, not in the beauty of their names.

  The author criticises later inventions like Assembly-Nobility, Mouse-Nobility, and Riding-Dragon patterns and the over‑mystification of "Hurting Officer hurting to the end" as examples of pattern-name worship: treating labels as truth while ignoring whether the structure and momentum actually justify them. In his view, miscellaneous patterns are simply extreme parameter regions inside the same framework. The task is always to return to Month-Mandate, stems, roots and dominant momentum, and to ask which force truly runs the board—instead of collecting ever more pattern names and forgetting the underlying logic.

- 详细解说：
  - 杂格篇的真正价值，在于：
    - 把“外格、从格”重新拉回到五行气势与用神逻辑之下；
    - 同时对“格名崇拜”做出批评，提示读者应回到结构与气势本身.
  - 对现代建模而言：
    - 不宜把“从格、杂格”当成完全独立的标签；
    - 更适合将其视作“极端参数区域”的特例，如：
      - 单一五行权重极高；
      - 日主权重极低而从强势一方；
      - 某一合化链条占据绝对主导等.

- **核心要点**：
  - 外格者，非正格也，即外格亦有正理
  - 从格者，日主无根，从其旺神
  - 化格者，天干相合，化为一气

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_585]` `[trigger: 杂格与从格的总纲]` `[role: 主干]` `[factor_trigger: waige_fei_zhengge AND waige_yi_you_zhengli]` 外格者，非正格也，即外格亦有正理 → 《子平真诠》#下卷
  - `[ns_zpzy_586]` `[trigger: 杂格与从格的总纲]` `[role: 条件分支]` `[factor_trigger: congge AND rizhu_wugen AND cong_qi_wangshen]` 从格者，日主无根，从其旺神 → 《子平真诠》#下卷
  - `[ns_zpzy_587]` `[trigger: 杂格与从格的总纲]` `[role: 条件分支]` `[factor_trigger: huage AND tiangan_xianghe AND hua_wei_yiqi]` 化格者，天干相合，化为一气 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 杂格/从格类型     |        | new_candidate | 分型轴     | za_ge / wai_ge / cong_cai_ge / cong_sha_ge / yi_fang_xiu_qi_ge        | 概括本章所列主要类型       |"""
    normalized_text_zh: str = """"""
    subject: str = "杂格与从格的总纲"
    factor_refs: list = ['zage', 'waige', 'congge', 'yifang_xiuqi', 'engine_id', 'zage_leixing', 'bazi_rule_engine', 'rizhu_genqi', 'bazi_rule_engine', 'geming_kekaodu', 'bazi_rule_engine', 'huigui_zhengge', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_150', 'rizhu_genqi', 'rel_zpzq_151', 'geming_kekaodu', 'evi_zpzq_133', 'zage_leixing', 'rule_zage_tiaojian', 'concept_alternative', 'concept_surrender']
    
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
        l1_anchor="zpzq_v1.0.0_杂格与从格的总纲_001_L1",
    )
    version: str = "1.0.0"
