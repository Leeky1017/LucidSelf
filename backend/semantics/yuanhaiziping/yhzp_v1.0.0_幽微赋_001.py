"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559438
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
    semantic_id="yhzp_v1.0.0_幽微赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 幽微赋(SemanticEntry):
    """
    - **原文（source_text）**：
  天地阴阳二气，降于春夏秋冬，各生其时；有用者则吉，无用者则凶。是以泄天机之妙理，谈大道之玄微。
  天既生人，人各有命。
  所以，早年富贵，八字运限...
    """
    
    original_text: str = """- **原文（source_text）**：
  天地阴阳二气，降于春夏秋冬，各生其时；有用者则吉，无用者则凶。是以泄天机之妙理，谈大道之玄微。
  天既生人，人各有命。
  所以，早年富贵，八字运限咸和；中主孤单，五行逢死绝败。
  过房入舍，年月中分。
  随母从夫，偏财空而印旺。
  早岁父亡，偏财临死绝杀宫。
  幼岁母离，只为财多印死。
  比肩多，而兄弟无情。
  阳刃多，而妻宫有损。
  官逢死气之方，子招难得。
  若见伤官太盛，子亦难留。
  如遇冲破提纲，定主离于祖业；再见空亡，三番四废。
  印绶逢生，母当贤贵。
  偏官归禄，父必峥嵘。
  官星临禄旺之乡，子当荣显。
  七杀遇长生之位，女招贫夫。
  自身借宫所生，必是依人过活。
  妻星失令，半路抛离；若乃借宫所生，亦是他人义女。
  酒色猖狂，只是桃花带杀。
  慈祥敏慧，天月二德聚来。
  印绶旺，而子少息稀。
  正官旺，而女多男少。
  枭神兴，早年折夭。
  食神旺，老寿而高。
  偏财逢败，父主风流；子曜若临，破家荡产。
  自身逢败，早岁兴衰。
  妻入墓，不得妻财。
  父临库，父当先死。
  比肩逢禄，兄弟名高。
  食神多而好饮食。
  正官旺而受沾滋。
  身临沐浴之年，恐愁水厄。
  生入斗克之年，必逢火灾。
  女带桃花坐杀，定主淫奔。
  伤多而印绶被克，母当淫荡。
  年月冲者，难为祖业。
  日时冲者，妻子招迟。
  若见天元刑战，父母难靠；如遇地支所生，凶中成吉。
  日主弱，水火相战，而招是非。
  甲木衰，逢金旺，而无仁无义。此乃男命之玄机。
  略说女人之奥妙，纯粹在于八字。
  纯有富贵者，一官生旺。
  四柱休囚，必为贵者。
  浊淫者，五行冲旺。
  娼淫者，官杀交叉。
  命主多合，此为不良。
  满柱杀多，不为克制。
  印绶多，而老无子。
  伤官旺，而幼伤夫。
  荒淫之欲，食神太过。
  四柱不见夫星，未为贞洁。
  官星绝，遇休囚，孤孀独宿。
  清洁源流，金猪相遇。
  木虎相见，四柱三夫。
  阳刃重叠、水火逢蛇，夫宫早丧。
  食神一位逢生旺，招子须当拜圣明。
  父母之宫，男命同断。若见此书，藏之如宝，若遇高士，对镜分明；依其此法，万无一失。

- **分字分词释义**：
  - **泄天机之妙理谈大道之玄微**：揭示天机妙理，探讨大道幽微。
  - **过房入舍年月中分**：过继入赘，年月宫位有分离。
  - **随母从夫偏财空而印旺**：随母改嫁，偏财空亡而印星旺。
  - **早岁父亡偏财临死绝杀宫**：年幼丧父，偏财入死绝或七杀之宫。
  - **阳刃多而妻宫有损**：羊刃多主克妻，妻宫有损。
  - **官逢死气之方子招难得**：官星入死气之地，子嗣难得。
  - **桃花带杀喜淫奔**：桃花与七杀同现，主酒色纵欲。
  - **官杀交叉娼淫者**：官杀混杂交战，主情史复杂。
  - **印绶多而老无子**：印星太多克食伤，老来无子。
  - **天月二德聚来慈祥敏慧**：天德月德会聚，主慈祥聪慧。

- **规范化释义（primary_lang_explained）**：
  本篇《幽微赋》从阴阳二气、四时生杀入手，细致论述六亲、出身、婚姻、寿夭等隐秘信息，强调“细处见真章”：
  - **总纲**：天地阴阳二气布于四时，五行有用则吉、无用则凶，命理所论皆是天机与大道的幽微之理。
  - **出身去留**：
    - **过房随母**：年月有分、父母宫被取代，多主过继、寄养。
    - **随母从夫**：偏财空、印旺，多随母改姓或随继父生活。
  - **父母与兄弟**：
    - 偏财临死绝杀宫：父早亡；财多印死：母离散或体弱。
    - 比肩多：兄弟无情；比肩逢禄：兄弟有名望。
  - **夫妻与子息**：
    - 阳刃多：妻宫有损，易克妻。
    - 官星在死气之方：子女难得；伤官太盛：子难留。
    - 妻星入墓：不得妻财；阳刃重叠、水火逢蛇：夫宫早丧（多见于女命）。
  - **女命专论**：
    - 官杀交叉、满柱多合、杀多无制：多主情史复杂、娼淫之象。
    - 印多老无子、伤官旺幼伤夫、食神太过主淫欲，是女命重要判据。
  - **吉凶对照**：
    - 桃花带杀：酒色猖狂。
    - 天月二德聚：慈祥敏慧，可解部分灾祸。
    - 日主弱水火相战：多是非官非；甲木衰逢金旺：少仁少义，为男命凶象。

- **完整对等诠释（secondary_lang_full）**：
  **Subtle Treatise (You Wei Fu)**：
  - **Meta-View**：Heaven–Earth Yin–Yang Qi flows through the four seasons. When the Five Elements are “usable” in a chart, they produce fortune; when “useless”, they generate misfortune. Fate reading is about decoding these subtle patterns.
  - **Origin & Fosterage**：
    - **Adoption / House Transfer**：Split of Year and Month palaces, or replacement of parental stars, points to adoption, fosterage, or moving into another household.
    - **Following Mother and Stepfather**：Empty Indirect Wealth with strong Seal often means following mother and stepfather.
  - **Parents & Siblings**：
    - Indirect Wealth (Father) sitting in death / killing palace → early loss of father.
    - Excess Wealth killing Seal → separation or weakness of mother.
    - Many Parallels → distant / unkind siblings; Parallels meeting Salary → famous brothers.
  - **Marriage & Children**：
    - Many Yang Blades → damage to Wife Palace, spouse easily harmed.
    - Officer in death Qi → hard to have sons; very strong Injuring Officer → hard to keep children.
    - Wife Star in Tomb → no benefit from wife’s wealth; overlapping Blades, Water–Fire–Snake patterns → early death of husband (especially in women’s charts).
  - **Female Charts**：
    - Crossing Officer–Killing, many combinations, Killing without control → complex love life, even prostitution indications.
    - Too many Seals → old age without children; strong Injury early harms husband; excess Food God → strong sensual desires.
    - No visible Husband Star does not automatically mean chaste; need to read the full pattern.
  - **Character & Fortune**：
    - Peach Blossom with Killing → debauchery in wine and sex.
    - Heavenly & Monthly Virtues gathered → kind, smart, softens some misfortune.
    - Weak Day Master with Water–Fire battling → disputes and lawsuits.
    - Jia Wood weak meeting strong Metal → lack of benevolence and righteousness in men.

- **核心要点**：
  - **幽微层级**：通过冲、合、墓、败等细小配置判断六亲与出身的隐秘信息。
  - **女命规则**：官杀交叉、印多无子、伤官旺克夫、食神太过主淫欲，是女命重要判据。
  - **六亲分宫**：偏财、印、官杀在不同宫位与旺衰，决定父母、配偶、子女之吉凶。
  - **德煞救应**：天月二德等吉神能在桃花带杀等凶局中缓和灾祸。

- **详细解说**：  《幽微赋》以"泄天机之妙理，谈大道之玄微"开篇，专论六亲、出身、婚姻等隐秘信息。**出身变动**——"过房入舍，年月中分"主过继寄养；"随母从夫，偏财空而印旺"主随母改嫁。**父母判断**——"早岁父亡，偏财临死绝杀宫"；"幼岁母离，只为财多印死"。**婚姻子嗣**——"阳刃多，而妻宫有损"主克妻；"官逢死气之方，子招难得"主子嗣艰难；"若见伤官太盛，子亦难留"。**女命专论**——"官杀交叉"主娼淫，"印绶多而老无子"，"伤官旺而幼伤夫"，"食神太过"主淫欲。**吉凶对照**——"桃花带杀，喜淫奔"主酒色；"天月二德聚来，慈祥敏慧"主慈善。末句"依其此法，万无一失"强调此赋为论命幽微之要诀。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_727]` `[trigger: 天机幽微]` `[factor_trigger: xie_tianji_miaoli AND dadao_xuanwei AND youwei_fu]` `[role: 主干]` 泄天机之妙理，谈大道之玄微；幽微赋论命总纲。 → 《渊海子平·幽微赋》
  - `[ns_yhzp_728]` `[trigger: 过房随母]` `[factor_trigger: guofang_rushe AND suimu_congfu AND chushen_biandong]` `[role: 条件分支]` 过房入舍年月中分；随母从夫偏财空而印旺；出身变动断法。 → 《渊海子平·幽微赋》
  - `[ns_yhzp_729]` `[trigger: 父母早亡]` `[factor_trigger: piancai_lin_sijue_shagong AND caiduo_yinsi AND caiyin AND caiyin_qing_guansha_zu AND changyin AND fu_zaowang]` `[role: 条件分支]` 早岁父亡偏财临死绝杀宫；幼岁母离只为财多印死。 → 《渊海子平·幽微赋》
  - `[ns_yhzp_730]` `[trigger: 阳刃克妻]` `[factor_trigger: yangren_duo AND qigong_yousun AND keqi]` `[role: 条件分支]` 阳刃多而妻宫有损；羊刃克妻断法。 → 《渊海子平·幽微赋》
  - `[ns_yhzp_731]` `[trigger: 子嗣艰难]` `[factor_trigger: guan_feng_siqi AND shangguan_taisheng AND zi_nande]` `[role: 条件分支]` 官逢死气之方子招难得；若见伤官太盛子亦难留。 → 《渊海子平·幽微赋》
  - `[ns_yhzp_732]` `[trigger: 女命官杀交叉]` `[factor_trigger: nvming AND guansha_jiaocha AND changyin AND caiyin AND caiyin_qing_guansha_zu]` `[role: 条件分支]` 官杀交叉娼淫者；印绶多而老无子；女命专论要点。 → 《渊海子平·幽微赋》
  - `[ns_yhzp_733]` `[trigger: 桃花带杀]` `[factor_trigger: taohua_daisha AND xi_yinben AND tianyue_erde_cixiang AND caiyin AND caiyin_qing_guansha_zu AND changyin AND cixiang_minghui]` `[role: 例外处理]` 桃花带杀喜淫奔；天月二德聚来慈祥敏慧；吉凶对照。 → 《渊海子平·幽微赋》
  - `[ns_yhzp_734]` `[trigger: 幽微赋纲领]` `[factor_trigger: youwei_fu AND liuqin_fengong AND chushen_biandong AND nvming_zhuanlun]` `[role: 总结]` 幽微赋以六亲分宫、出身变动、女命专论为核心，揭示命理幽微之理。 → 《渊海子平·幽微赋》"""
    normalized_text_zh: str = """"""
    subject: str = "幽微赋"
    factor_refs: list = ['adoption_follow_mother', 'follow_mother_stepfather', 'borrowed_palace_birth', 'peach_blossom_killing', 'heavenly_monthly_virtues']
    
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
        l1_anchor="yhzp_v1.0.0_幽微赋_001_L1",
    )
    version: str = "1.0.0"
