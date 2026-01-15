"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778539
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
    semantic_id="zw_v1.0.0_补遗骨髓赋注解_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 补遗骨髓赋注解(SemanticEntry):
    """
    #### 4.1 文武庙旺：将相之材

- 原文（断句）：

  文曲、武曲居庙旺处，将相之材。文昌亦同曲也。武曲于辰戌第一，丑未第二，文曲于子宫，为庙旺之地，卯酉次之，若逢左右，为贵格论。

- 分...
    """
    
    original_text: str = """#### 4.1 文武庙旺：将相之材

- 原文（断句）：

  文曲、武曲居庙旺处，将相之材。文昌亦同曲也。武曲于辰戌第一，丑未第二，文曲于子宫，为庙旺之地，卯酉次之，若逢左右，为贵格论。

- 分字分词释义：

  - **文曲武曲**：北斗文星与武星，主科甲功名与财帛权力。
  - **居庙旺处**：星曜处于庙旺有力之地。
  - **将相之材**：具备成为将军或宰相的才干。
  - **武曲辰戌第一**：武曲在辰宫戌宫为最佳庙旺位置。
  - **丑未第二**：武曲在丑宫未宫为次等庙旺。
  - **文曲子宫**：文曲在子宫为庙旺之地。
  - **卯酉次之**：文曲在卯宫酉宫为次等庙旺。
  - **左右同宫**：左辅右弼同守一宫。
  - **披绯衣紫**：穿着绯红与紫色官服，象征高官显贵。
  - **明禄暗禄**：禄存（明禄）与化禄（暗禄）同守命宫。
  - **位至公卿**：官位达到公侯卿相级别。
  - **孤贫则寿**：贫穷孤寒反而长寿。
  - **富贵即夭**：极度富贵反而短命。

- 规范化释义（primary_lang_explained）：

  文曲武曲居庙旺处将相之材。文昌亦同曲也。武曲于辰戌第一丑未第二，文曲于子宫为庙旺之地卯酉次之，若逢左右为贵格论。

- 核心要点：
  - 武曲辰戌为第一，丑未次之
  - 文曲子宫为庙，卯酉次之
  - 文昌同文曲论，逢左右为贵格

#### 4.2 左右同宫：披绯衣紫

- 原文（断句）：

  左右同宫，披绯衣紫。如辰戌安命正月、七月生者，未安命四月生者，丑安命十月生者，卯亥安命八月、十二月生者，巳酉安命二月六月生者，如财官迁移，有左右同宫不系左右同宫格。

- 规范化释义（primary_lang_explained）：

  左右同宫披绯衣紫。如辰戌安命正月七月生者，未安命四月生者，丑安命十月生者，卯亥安命八月十二月生者，巳酉安命二月六月生者，如财官迁移有左右同宫不系左右同宫格。

- 核心要点：
  - 左辅右弼同宫守命，主披绯衣紫
  - 需特定宫位与月份配合
  - 财官迁移有左右不算同宫格

#### 4.3 廉贞未申：富贵声扬

- 原文（断句）：

  廉贞在未并申宫，富贵声扬播远名。无杀，方是加杀平常。

- 规范化释义（primary_lang_explained）：

  廉贞在未并申宫富贵声扬播远名。无杀方是，加杀平常。

- 核心要点：
  - 廉贞未申二宫入庙
  - 无杀主富贵声扬
  - 加杀则平常

#### 4.4 巨机酉上：孤贫则寿，富贵即夭

- 原文（断句）：

  巨机酉上化吉者，便有财官也。不终孤贫则有寿，富贵即夭亡。若太阳坐安迁移，财官之宫化权禄，则横发有时。

- 规范化释义（primary_lang_explained）：

  巨机酉上化吉者便有财官也。不终孤贫则有寿，富贵即夭亡。若太阳坐安迁移财官之宫化权禄则横发有时。

- 核心要点：
  - 巨门天机在酉宫为陷地
  - 化吉虽有财官，但孤贫则寿、富贵则夭
  - 体现"盛极必衰"原理

#### 4.5 明禄暗禄：位至公卿

- 原文（断句）：

  明禄暗禄，位至公卿；命有禄存，又逢化禄是也。如甲生人，命坐禄存在寅，廉贞亦在寅化禄。又戊生人，安命在巳，贪狼化禄；丁己生人，安命在午，太阴化禄。丙己生人为贵格，丁戊生人平常，虽富贵不久。

- 规范化释义（primary_lang_explained）：

  明禄暗禄位至公卿，命有禄存又逢化禄是也。如甲生人命坐禄存在寅廉贞亦在寅化禄，又戊生人安命在巳贪狼化禄，丁己生人安命在午太阴化禄。丙己生人为贵格，丁戊生人平常虽富贵不久。

- 核心要点：
  - 禄存+化禄双禄守命为明禄暗禄
  - 多个生年配合案例
  - 丙己生人为贵格，丁戊生人不久

#### 4.6 历史案例补充

##### 4.6.1 活禄逢迎夫子：文章冠世

- 原文（断句）：

  活禄逢迎夫子，文章冠世。天子安命在子，太阳化禄在午，迁移宫是也。

- 规范化释义（primary_lang_explained）：

  活禄逢迎夫子文章冠世。天子安命在子太阳化禄在午迁移宫是也。

- 核心要点：孔子命例，安命子宫，太阳化禄在午迁移，主文章冠世

##### 4.6.2 西施倾国：命犯擎羊以捐躯

- 原文（断句）：

  西施倾国，命犯擎羊以捐躯；安命在午有羊刃，流年太岁又巡逢，羊陀迭并，故命难逃也。

- 核心要点：（重复骨髓赋案例）擎羊午宫+流年迭并，主凶亡

##### 4.6.3 项羽英雄：限到天空而丧国

- 原文（断句）：

  项羽英雄，限到天空而丧国。生处帝室，或劫空冲照，犹如半天折翅。劫空俱在命犹凶，三方稍轻，只可平常度日。倘有横发、有财禄，必主丧亡。

- 核心要点：（重复骨髓赋案例）限至天空劫空，英雄末路

---

- 完整对等诠释（secondary_lang_full）：

  The supplementary Bone-Marrow verse adds fine-grained specifications on top of the main Bone-Marrow text. Its goal is not to introduce entirely new doctrines, but to sharpen when classic configurations truly qualify as high-grade and how birth year and month adjust their strength.
  It refines civil and military temple-dignity standards, specifying where Wenchang, Wenqu, Wuqu and related stars must stand to produce genuine ministerial or general-level talent. It lists conditions under which Zuofu and Youbi co-guarding the Life palace raise a person into distinguished office, and when the same stars, if misplaced, lose much of their power. Further notes explain Lianzhen in certain Wei or Shen positions, Jumen and Tianji on particular axes, and the famous double-salary patterns where manifest and hidden salary stars combine to support lasting nobility. Historical illustrations using figures like Confucius or Xiang Yu show how the same families of patterns can lead either to stable greatness or to brilliant but short-lived careers, depending on surrounding support.
  A recurring theme is triple coordination: the palace where a pattern appears, the native's birth stem and the relevant month or seasonal context must all line up before the text will grant its highest verdict. The supplement also underlines several dialectical ideas, such as charts in which poverty coincides with long life while extreme wealth coincides with early decline. In this way it trains the reader to look for nuance rather than treating every appearance of a famous configuration as automatically fortunate.

- 叙事素材（narrative_snippets）：

  - **文武庙旺**：文曲、武曲、文昌在庙旺处同度或拱照命身，象征“将相之材”，一生以文武本领立身。
  - **左右同宫披绯衣紫**：左辅右弼同宫守命，又合特定月份与宫位时，易见披绯衣紫、身入权贵之列。
  - **廉贞未申声扬**：廉贞在未并申宫无杀加会时，声名远播，富贵不止一隅。
  - **巨机酉上：孤贫长寿 vs 富贵短命**：巨门天机在酉宫化吉，往往“孤贫则寿，富贵即夭”，以盛极必衰示人。
  - **明禄暗禄位至公卿**：禄存与化禄同守或三合照命，明禄暗禄叠加，主位极人臣、富贵双全。
  - **历史映照**：孔子文章冠世、西施以色殒身、项羽英雄末路，示范同类格局在不同配合下的荣盛与覆灭。"""
    normalized_text_zh: str = """"""
    subject: str = "补遗骨髓赋注解"
    factor_refs: list = ['combo_mingluanlu', 'result_jiangxiangzhicai', 'combo_zuoyoutonggong', 'principle_gupinzeshou', 'principle_fuguijiyao', 'result_pifeiyizi', 'source_ref', 'rel_buyi_001', 'shuanglu_shuangxing', 'rel_buyi_002', 'shengjibishuai', 'rel_buyi_003', 'wenwu_miaowang', 'evi_buyi_001', 'combo_mingluanlu', 'rule_mingluanlu', 'evi_buyi_002', 'result_jiangxiangzhicai', 'rule_wenwumiaowang', 'evi_buyi_003', 'principle_gupinzeshou', 'rule_gupinfugui', 'concept_double_blessing', 'concept_peak_decline', 'concept_precision_match']
    
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
        l1_anchor="zw_v1.0.0_补遗骨髓赋注解_001_L1",
    )
    version: str = "1.0.0"
