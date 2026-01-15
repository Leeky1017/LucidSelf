"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559489
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
    semantic_id="yhzp_v1.0.0_爱憎赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 爱憎赋(SemanticEntry):
    """
    - **原文（source_text）**：  
  爱憎赋。  
  富莫富于纯粹，贫莫贫于战争；贵莫贵于秀实，贱莫贱于反伤。  
  文辞称辨，贵马会于学堂。  
  锦绣文章，火木合于性情。  ...
    """
    
    original_text: str = """- **原文（source_text）**：  
  爱憎赋。  
  富莫富于纯粹，贫莫贫于战争；贵莫贵于秀实，贱莫贱于反伤。  
  文辞称辨，贵马会于学堂。  
  锦绣文章，火木合于性情。  
  深谋远虑，德性居沉静之宫。  
  术业精微，帝座守文章之馆。  
  吉福生旺禄马，全要精神。  
  魁罡有灵变之机。  
  离（火）坎（水）乃聪明之户。  
  贵人禄马，宜逢劫刃，空亡奇远。  
  长生，招君子之可爱。  
  衰败，遇小人之憎嫌。  
  四柱斗乱兮，不仁不义。  
  五行相生兮，为孝为忠。  
  印绶在刑冲之内，心乱身忘。  
  日时居墓库之中，忧多乐少。  
  日干旺，而灾咎寡。  
  财命衰，而惆怅多。  
  衣食奔波，旺处遭刑。  
  利名成败，贵地逢伤。  
  平生祸福，赖于一时；一世吉凶，凭于气运。  
  福有气而变通陞迁。  
  岁克运凶，无气而人离散。  
  大运凶，而生百祸。  
  流年吉，而除千殃。  
  无绝至绝，财命危倾。  
  本主得生，利名称遂。  
  三合六合，逢之吉重祸轻。  
  七杀四凶，遇之祸深福浅。  
  加官进职，定因禄会之年。  
  广置根基，必是合财之地。  
  岁君冲压主凶灾。  
  大运受伤殊少吉。  
  岁宜生运，运喜生身；三位相生，一年称意。  
  财官俱旺，应显达于仕途。  
  财食均萦，岂淹留于白屋。  
  禄入聚生之地，富贵可知。  
  马奔禄旺之乡，荣华可断。  
  欲取交关利息，须寻六合相扶。  
  财官带禄朝元，定主安然获福。  
  月衰时旺，早岁丰肥。  
  木重土轻，终身漂荡。  
  惯取市廛之利，必因旺处逢财。  
  忽然显达成家，定是刑冲见贵。  
  主本当时，得女以扶持。  
  贵禄有情，因男子而升吉。  
  南商北旅，定因马道之通；东贩西驰，必是车运之利。  
  日干困弱，伯牛敢怨苍穹。  
  禄马衰微，颜子难逃短命。  
  凶，莫凶于劫刃。  
  吉，莫吉于刚强。  
  官微马劣，男逃女走。  
  天罗地网，非横之灾。  
  脱命夭亡，遇之必不得实而死。  
  穷途逢劫，危疑必犯于自刑。  
  绝处逢财，妻子应难谐老。  
  大耗小耗，多因博戏亡家。  
  官符死符，必主狱讼时有。  
  或，行四柱遇绝，三命刑伤，未免徒绞之刑，难逃黥面之苦。  
  若逢五鬼，雷伤虎咬无疑，更值群凶，恶殃横死定断；女多淫贱，男必猖狂。  
  或问人之情性，贤愚善恶，先推贵贱旺相之由，衰败方究机巧灵变。心高者，魁罡为祸；性顺者，六合为祥。  
  观幽闲潇洒之人，遇华盖孤虚之位。  
  好恃势倚霸之辈，犯偏官劫刃之权。  
  劫刃生鄙吝之悭，更出机关之险。  
  谋略大因于壬癸。  
  威风气猛于丙丁。  
  孤囚遇之，无精神。  
  破败遇之，多疏坦。  
  甲乙顺而仁慈大量。  
  庚辛亏而果断气刚。  
  燥败火盛须疑。  
  隐忍金多定论。  
  刑战者，愚顽。  
  安静者，贤俊。  
  金木司令而相生，火土逢时而相助，不劳心而衣食自足，不费力而家计自成；更若得神扶持，定是权尊乡里。  
  禄贵拱位者，台省扬名。  
  其所忧者福不福，其所虑者成不成。福不福者，吉处遭凶；成不成者，格局见破。  
  伤其格者，则伤。  
  破其格者，则祸。  
  譬若，苗逢秋旱，而冬廪空虚；花被春霜，而夏果无成。  
  智谋思虑，措用无成，纵有回天转轴之机，而无建功立业之遂；岂不见郦生烹鼎，范生甑尘，渊明东归，子美西去，孟轲不遇，冯衍空回，买臣负薪而行歌，江革苦寒而坐泣。盖苗而不秀者有之，秀而不实者有之，更值伤败太过，一福不过刍荛；纵有百艺多能，难免饥寒苦疾，困于沟壑，命使其然尔，淹滞无成，何劳叹嗟！  
  欲问富贵，全仗财官。  
  朕何由得之？大莫大于镃基，奇莫奇于秀异。达圣达贤者，无时不有；至富至贵者，自古皆然。  
  或生生月之中，文高武显。  
  或居冠带之下，业大财奇。  
  若此玄妙，何如推测？先论学堂之内，三奇四福，次察格局之外，一吉二宜。  
  若，己未见甲午为祥，壬申见丁巳为瑞。  
  壬子丙午，主光风儒雅之人。  
  辛酉丙申，长俊秀荣华之士。  
  阴阳全凭纯美。  
  造化最喜相生。  
  难辨者日精月华，莫测者金堂玉匮，得之者荣，遇之者贵。若遇贤愚显晦，无非造化钧陶，物既荣枯，为人岂无成败；假若凤生于雉，蛇化为龙，芳兰不断蓬蒿，枯木犹生于山野。  
  少贵老贱，初迍后亨；盖由大运之衰旺，以致富贵之更变。  
  格局纯而反杂，惆怅残春。  
  运行老而得时，优游晚景。  
  防不测运之艰危，是以时有春秋，月圆有缺。尝观资荫之子，亲一丧定无聊；复见田井钓之人，运一通而殊显。多年爵禄，一旦俱休；时运至者，片时相遇。值生旺者，未必为凶；有情者通，无情者滞；有合者吉，有冲者凶。  
  官印岁临，仕途定知进擢。  
  食财运遇，庶民亦喜荣昌。  
  或有少依祖父之荣，长借儿孙之贵；又有垂髫难苦，至老无依；盖因四柱之旺衰，所由大运之亨否。  
  岂不见枯槁之木，纵逢春而不荣；茂盛之标，虽凌霜而不败。  
  论日更亏年月，定无下稍。  
  生时旺气朝元，必有晚福。  
  古有琢磨之玉，值价连城；世有正直之人，自成家计；如烹炼之馀而不朽，如岁寒之后而不凋。消息妙在变通，祸福当察衰旺，庶几君子，共鉴是幸！

- **分字分词释义**：
  - **富莫富于纯粹贫莫贫于战争**：最富在于格局纯粹，最贫在于刑冲战争。
  - **贵莫贵于秀实贱莫贱于反伤**：最贵在于秀气充实，最贱在于反克伤损。
  - **四柱斗乱兮不仁不义**：四柱刑冲战乱，主不仁不义。
  - **五行相生兮为孝为忠**：五行相生有情，主孝顺忠诚。
  - **大运凶而生百祸流年吉而除千殃**：大运凶生百祸，流年吉除千殃。
  - **心高者魁罡为祸性顺者六合为祥**：心高者魁罡反为祸，性顺者六合为吉。
  - **甲乙顺而仁慈大量庚辛亏而果断气刚**：甲乙仁慈宽大，庚辛果断刚强。
  - **有情者通无情者滞**：干支有情则通达，无情则滞涩。
  - **消息妙在变通祸福当察衰旺**：变通为妙，祸福看衰旺。
  - **欲问富贵全仗财官**：欲问富贵，全靠财官。

- **规范化释义（primary_lang_explained）**：  
  《爱憎赋》并不是简单讲“喜欢/讨厌谁”，而是从**格局纯粹/驳杂、喜神/忌神、运势高低**三个维度，说明命理上“应当所爱”与“必须所憎”的对象：  
  - **格局与纯粹**：
    - 富莫富于纯粹：格局清纯、五行相生、财官印食分明者，最易成大富贵。  
    - 贫莫贫于战争：刑冲克害杂战、劫刃横行、官杀混乱者，多主贫困动荡。  
  - **福神与祸神**：
    - 财官印绶、学堂、贵人、禄马、天月德等，是应当“爱”的福神——助人科名、家业、品行。  
    - 劫刃、七杀四凶、天罗地网、大耗小耗、官符死符、五鬼等，是应当“憎”的祸神——多主官非、横死、赌博亡家。  
  - **性情与格局的对应**：
    - 心高者，魁罡为祸；性顺者，六合为祥。  
    - 甲乙顺而仁慈，庚辛亏而果断；火盛多躁、金多多忍，金木司令相生则为忠孝之人。  
  - **运势与吉凶翻转**：
    - 一生祸福赖一时，一世吉凶凭气运：大运凶而百祸并生，流年吉则可除千殃。  
    - 值生旺者未必为凶，有情者通，无情者滞；有合者吉，有冲者凶——提示要看“气有无情”。  
  - **富贵的取得方式**：
    - 欲问富贵，全仗财官；先看学堂三奇四福，再察格局一吉二宜。  
    - 资荫子弟丧亲而失依，田井钓者一运通便显达，都体现“运至则遇，运去则休”的基调。  

- **完整对等诠释（secondary_lang_full）**：  
  **Treatise on Love and Aversion (Ai Zeng Fu)**:  
  - **Purity vs. Conflict**: The highest wealth comes from pure, well-formed patterns; the worst poverty from charts full of internal wars—clashes, punishments, and conflicting stars. True nobility lies in real talent and substance, while the lowest status appears when benefic patterns are repeatedly damaged.  
  - **Whom to Love, Whom to Hate**: One should "love" supportive gods—Wealth, Officer, Seal, Noblemen, Study Hall, Horses, Virtue stars—because they bring learning, rank, and stability. One must "hate" robbing Blades, Seven Killings without control, entangling nets like Tian Luo Di Wang, major and minor Loss stars, and lawsuit stars, as they correlate with ruin, prison, and even violent death.  
  - **Character and Temperament**: Charts rich in Canopy and Study Hall indicate solitary scholars; strong Rob Wealth and Blades breed greed and scheming; Ren and Gui emphasize strategy, Bing and Ding emphasize force and presence. Gentle charts match harmonious combinations; harsh charts resonate with conflictual stars.  
  - **Role of Luck Cycles**: A person’s lifetime fortune depends heavily on timing. Auspicious natal patterns can be broken by harsh luck, while modest charts can rise through well-timed years. Combinations of year, decade luck, and pillars that mutually generate bring a year "where everything flows"; severe clashes can turn good foundations into hardship.  
  - **Wealth and Rank in Reality**: Stories of historical figures illustrate how even talented people fail when their patterns are repeatedly harmed, while some with ordinary origins rise because their charts and luck cooperate. The ode concludes that one must observe change and waxing–waning carefully—fortune is the result of both inherent pattern and evolving qi.  

- **核心要点**：  
  - 爱：格局清纯、喜神得位、财官印食有情、学堂贵人禄马成局。  
  - 憎：刑冲克害杂战、劫刃横行、七杀四凶、大耗官符等反复破格。  
  - 性情与五行、神煞高度对应，魁罡、华盖、学堂、桃花等各有心性偏向。  
  - 运势可把好命拖坏，也能把弱局托起，必须联合命局和大运岁运同看。  

- **详细解说**：  《爱憎赋》以"富莫富于纯粹，贫莫贫于战争；贵莫贵于秀实，贱莫贱于反伤"开篇，阐述命局中应爱与当憎的对象。**格局纯粹**——"五行相生兮，为孝为忠"；"四柱斗乱兮，不仁不义"揭示格局清浊与性情的关系。**福神祸神**——"吉福生旺禄马，全要精神"；"凶莫凶于劫刃"揭示福神祸神的区分。**性情对应**——"心高者魁罡为祸，性顺者六合为祥"；"甲乙顺而仁慈大量，庚辛亏而果断气刚"揭示五行与性情的对应。**运势翻转**——"大运凶而生百祸，流年吉而除千殃"；"有情者通，无情者滞；有合者吉，有冲者凶"揭示运势与吉凶的交互。**富贵取法**——"欲问富贵，全仗财官"；"禄入聚生之地，富贵可知"为取富贵之法。末句"消息妙在变通，祸福当察衰旺"点明爱憎之法的核心。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_759]` `[trigger: 纯粹战争]` `[factor_trigger: fu_yu_chuncui AND pin_yu_zhanzheng AND gui_yu_xiushi AND anchong_qugui AND angui]` `[role: 主干]` 富莫富于纯粹贫莫贫于战争；贵莫贵于秀实贱莫贱于反伤。 → 《渊海子平·爱憎赋》
  - `[ns_yhzp_760]` `[trigger: 五行性情]` `[factor_trigger: wuxing_xiangsheng_xiao_zhong AND sizhu_douluan_buren_buyi AND burenbuyi]` `[role: 条件分支]` 五行相生兮为孝为忠；四柱斗乱兮不仁不义。 → 《渊海子平·爱憎赋》
  - `[ns_yhzp_761]` `[trigger: 福神祸神]` `[factor_trigger: jifu_shengwang_luma AND xiong_yu_jieren]` `[role: 条件分支]` 吉福生旺禄马全要精神；凶莫凶于劫刃。 → 《渊海子平·爱憎赋》
  - `[ns_yhzp_762]` `[trigger: 魁罡六合]` `[factor_trigger: xingao_kuigang_weihuo AND xingshun_liuhe_weixiang]` `[role: 条件分支]` 心高者魁罡为祸；性顺者六合为祥；性情与神煞对应。 → 《渊海子平·爱憎赋》
  - `[ns_yhzp_763]` `[trigger: 甲乙庚辛]` `[factor_trigger: jiayi_shun_renci AND gengxin_kui_guoduan AND jiayi_shun]` `[role: 条件分支]` 甲乙顺而仁慈大量；庚辛亏而果断气刚；天干与性情。 → 《渊海子平·爱憎赋》
  - `[ns_yhzp_764]` `[trigger: 运势吉凶]` `[factor_trigger: dayun_xiong_baihuo AND liunian_ji_chuyang]` `[role: 条件分支]` 大运凶而生百祸；流年吉而除千殃；运势翻转之理。 → 《渊海子平·爱憎赋》
  - `[ns_yhzp_444]` `[trigger: 有情无情]` `[factor_trigger: youqing_tong AND wuqing_zhi AND youhe_ji AND youchong_xiong]` `[role: 例外处理]` 有情者通无情者滞；有合者吉有冲者凶；干支有情无情。 → 《渊海子平·爱憎赋》
  - `[ns_yhzp_445]` `[trigger: 爱憎赋纲领]` `[factor_trigger: aizeng_fu AND chuncui_zhanzheng AND fushen_huoshen AND yunshi_fanzhuan AND huofu]` `[role: 总结]` 爱憎赋以纯粹战争、福神祸神、性情对应、运势翻转为核心，阐述命局爱憎之理。 → 《渊海子平·爱憎赋》"""
    normalized_text_zh: str = """"""
    subject: str = "爱憎赋"
    factor_refs: list = ['pure_pattern', 'warring_pattern', 'auspicious_deities', 'malefic_deities', 'harmonious_ruthless']
    
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
        l1_anchor="yhzp_v1.0.0_爱憎赋_001_L1",
    )
    version: str = "1.0.0"
