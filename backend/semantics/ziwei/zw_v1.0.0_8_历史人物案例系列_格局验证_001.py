"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778503
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
    semantic_id="zw_v1.0.0_8_历史人物案例系列_格局验证_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 8历史人物案例系列格局验证(SemanticEntry):
    """
    ##### 1.8.1 李广不封：擎羊逢于力士

- 原文（断句）：

  李广不封擎羊逢于力士，二星守命纵吉，多平常之论。加杀最凶。女命不论。

- 分字分词释义：

  - **李广不封**：汉代...
    """
    
    original_text: str = """##### 1.8.1 李广不封：擎羊逢于力士

- 原文（断句）：

  李广不封擎羊逢于力士，二星守命纵吉，多平常之论。加杀最凶。女命不论。

- 分字分词释义：

  - **李广不封**：汉代名将李广，一生功勋卓著却未能封侯，比喻功名难成。
  - **擎羊逢力士**：擎羊与力士二星同宫或相遇。
  - **力士**：斗数中的小星，与擎羊同守则主刑伤克制。
  - **二星守命**：擎羊与力士同守命宫。
  - **纵吉多平常**：即使有吉星相会，也只能算平常之命。
  - **颜回夭折**：孔子最得意弟子，32岁英年早逝，比喻才高命薄。
  - **文昌陷天殇**：文昌星落入天殇凶地。
  - **仲由猛烈**：子路字仲由，性格勇猛刚烈。
  - **廉贞入庙遇将军**：廉贞庙旺且与将军星同宫。
  - **邓通饿死**：汉文帝宠臣，富可敌国却饿死收场。
  - **天罗地网**：辰戌二宫，为困厄之地。

- 规范化释义（primary_lang_explained）：

  李广不封因擎羊逢于力士。二星守命纵有吉星亦多平常之论，加杀最凶。女命不论。

- 案例分析：
  - 人物：李广（汉代名将）
  - 格局：擎羊+力士守命
  - 结局：纵横沙场立功无数，却终身不得封侯
  - 验证：擎羊逢力士，纵有吉星仍为平常，难获高位

##### 1.8.2 颜回夭折：文昌陷于天殇

- 原文（断句）：

  颜回夭折，文昌陷于天殇。如丑生人安命寅宫，其文昌陷于未宫，天殇流年，又遇七杀及羊陀迭并之限，依此断准。

- 规范化释义（primary_lang_explained）：

  颜回夭折因文昌陷于天殇。如丑生人安命寅宫其文昌陷于未宫天殇流年，又遇七杀及羊陀迭并之限依此断准。

- 案例分析：
  - 人物：颜回（孔子最得意弟子）
  - 格局：文昌陷天殇+七杀羊陀迭并
  - 结局：德行第一却英年早逝（32岁）
  - 验证：文昌陷凶地，限遇恶杀，主夭折

##### 1.8.3 仲由猛烈：廉贞入庙，遇将军

- 原文（断句）：

  仲由猛烈，廉贞入庙，遇将军，立命申宫，此二星坐守是也，余仿此。

- 规范化释义（primary_lang_explained）：

  仲由猛烈因廉贞入庙遇将军。立命申宫此二星坐守是也，余仿此。

- 案例分析：
  - 人物：子路（仲由，孔门十哲）
  - 格局：廉贞入庙+将军星守命
  - 性格：性格猛烈，勇武果断
  - 验证：廉贞入庙主果断，将军星主勇武

##### 1.8.4 邓通饿死：运逢大耗之乡

- 原文（断句）：

  邓通饿死，运逢大耗之乡；通命安在子宫二限，行至夹限之地，大耗逢之，更会恶曜是也。

- 案例分析：
  - 人物：邓通（汉文帝宠臣，富可敌国）
  - 格局：限行夹限之地+大耗+恶曜
  - 结局：失宠后家产尽没，竟然饿死
  - 验证：限逢大耗+恶曜，富贵化为乌有

##### 1.8.5 夫子绝粮：限到天殇之内

- 原文（断句）：

  夫子绝粮，限到天殇之内。与上同断。

- 案例分析：
  - 人物：孔子
  - 事件：周游列国时在陈蔡绝粮
  - 格局：限到天殇之地
  - 验证：即使圣人，限运不济亦遭困厄

##### 1.8.6 吕后专权：两重天禄、天马

- 原文（断句）：

  吕后专权，两重天禄、天马，禄存又逢。化禄及天马同守命宫是也。

- 案例分析：
  - 人物：吕后（汉高祖皇后）
  - 格局：禄存+化禄+天马同宫（双禄马）
  - 性格：专权独断，掌控朝政
  - 验证：双禄马守命，主权势与行动力

##### 1.8.7 杨妃好色：三合文曲，文昌

- 原文（断句）：

  杨妃好色，三合文曲，文昌、命宫及财官迁移。昌曲合照，更会太阴、天机，必主淫泆也。

- 案例分析：
  - 人物：杨贵妃
  - 格局：昌曲三合+太阴天机会照
  - 性格：多情好色，倾国倾城
  - 验证：昌曲+太阴天机，主风流淫泆

##### 1.8.8 西施倾国：命犯擎羊以捐躯

- 原文（断句）：

  西施倾国，命犯擎羊以捐躯；安命在午有羊刃，流年太岁又巡逢，羊陀迭并，故命难逃也。

- 案例分析：
  - 人物：西施（春秋四大美女）
  - 格局：命在午宫有羊刃+流年羊陀迭并
  - 结局：倾国倾城却不得善终
  - 验证：羊刃守命+流年迭并，难逃凶厄

##### 1.8.9 项羽英雄：限至天空而丧国

- 原文（断句）：

  项羽英雄，限至天空而丧国。生处帝室，或劫空冲照，犹如半天折翅。劫空俱在命犹凶，三方稍轻，只可平常度日。倘有横发、有财禄，必主丧亡。

- 案例分析：
  - 人物：项羽（西楚霸王）
  - 格局：大小二限俱逢天空
  - 结局：霸业鼎盛却乌江自刎
  - 验证：限至天空，英雄末路

##### 1.8.10 石崇豪富：限行劫地以亡家

- 原文（断句）：

  石崇豪富，限行劫地以亡家。大小二限临于夹陷之地，更遇流陀等杀必凶。

- 案例分析：
  - 人物：石崇（晋代巨富，富可敌国）
  - 格局：限行劫地+夹陷+流年凶杀
  - 结局：家破人亡，爱妾被杀
  - 验证：限行劫地，豪富亦难免亡家

##### 1.8.11 屈原溺水：限至天罗地网

- 原文（断句）：

  限至天罗地网，屈原曾溺水而亡；二限行至辰、戌二宫，逢武曲、贪狼，更有太岁、丧吊、白虎及劫空四杀，或一逢冲照，其限最凶。

- 案例分析：
  - 人物：屈原（楚国忠臣）
  - 格局：限至辰戌（天罗地网）+武曲贪狼+太岁凶杀
  - 结局：怀石投江而死
  - 验证：限至天罗地网+凶杀，主溺水之厄

##### 1.8.12 阮籍贫困：运遇地劫天空

- 原文（断句）：

  运遇地劫天空，阮籍有贫穷之苦。二限十二宫中，但遇劫空二星，虽吉多，亦财来财去。如见流年杀曜凶星，定主贫困。

- 案例分析：
  - 人物：阮籍（竹林七贤）
  - 格局：限遇劫空+流年凶杀

- 完整对等诠释（secondary_lang_full）：

  This series of historical case studies uses famous figures from Chinese history to validate the theoretical principles established in earlier sections. Li Guang, despite his military prowess, never received noble enfeoffment because Qingyang conjoined with Lishi in his chart creates a pattern where even benefic support yields only ordinary outcomes. Yan Hui, Confucius's most gifted disciple, died young because his scholarly star Wenchang fell into the celestial wound position. Zhong You's fierce valor came from Lianzhen in temple dignity meeting the general star, explaining his warrior temperament. Deng Tong, once fabulously wealthy through imperial favor, starved to death when his limits entered the Great Consumption sector. Confucius himself experienced the siege at Chen during his sixty-second year when his minor limit encountered Celestial Wound. Empress Lü's domineering power stemmed from doubled Tianlu and Tianma. Yang Guifei's legendary beauty and passion arose from tripled Wenqu and Wenchang configurations. Xi Shi sacrificed her life because her chart carried Qingyang in a vulnerable position. Xiang Yu lost his kingdom when his limits reached Tiankong. Shi Chong, despite his legendary wealth, lost everything when his limits traversed Robbery Ground. Qu Yuan drowned when his limits reached the Net of Heaven and Earth with malefic convergence. Ruan Ji, one of the Seven Sages of the Bamboo Grove, experienced poverty when his transiting limits encountered Dikong and Tiankong. These twelve cases demonstrate that regardless of talent, status, or historical achievement, all lives remain subject to the immutable laws of pattern and timing.

- 叙事素材（narrative_snippets）：

  - **李广难封**："擎羊遇力士，有官者降职，平人生祸"，李广有羊力同度故不能封侯。
  - **颜回夭寿**："命遇天伤夭寿"，颜回文昌入天伤故夭折。
  - **孔子困陈**："六十二逢天伤困陈"，孔子流年遇凶故有陈蔡之厄。
  - **项羽失江山**："限到天空失江山"，项羽限至天空故失天下。
  - **屈原溺水**："限至天罗地网"，屈原限逢辰戌武贪凶杀故溺水。
  - **现代应用**：本批历史案例可作为"格局应验"的参照——格局定框架，限运定时点，盛极必衰是普遍规律。"""
    normalized_text_zh: str = """"""
    subject: str = "8 历史人物案例系列（格局验证）"
    factor_refs: list = ['case_liguang', 'case_yanhui', 'principle_shengjibishuai', 'position_tianluodiwang', 'theory_gejuxianyun', 'source_ref', 'rel_anli_001', 'anli_geju', 'rel_anli_002', 'xianyun_zhuanzhe', 'rel_anli_003', 'shengjibishuai', 'evi_anli_001', 'case_liguang', 'rule_yangli_bufeng', 'evi_anli_002', 'position_tiankong', 'rule_xiankong_sangguo', 'evi_anli_003', 'position_jiekong', 'rule_xianjie_wangjia', 'concept_historical_validation', 'concept_peak_decline', 'concept_fate_determinism']
    
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
        l1_anchor="zw_v1.0.0_8_历史人物案例系列_格局验证_001_L1",
    )
    version: str = "1.0.0"
