"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412974
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
    semantic_id="smth_v1.0.0_八专禄旺与专禄纯气_001",
    book_id="sanming",
    engine_id="bazi"
)
class 八专禄旺与专禄纯气(SemanticEntry):
    """
    - **原文（source_text）**：

  八专日见前，或又添丙午、丁巳、戊辰、戊午、己巳、乙丑、壬子，而无丁未。六十甲子，独此干支同类。内甲寅、乙卯、庚申、辛酉四日，自专禄旺为正。甲乙宜亥卯...
    """
    
    original_text: str = """- **原文（source_text）**：

  八专日见前，或又添丙午、丁巳、戊辰、戊午、己巳、乙丑、壬子，而无丁未。六十甲子，独此干支同类。内甲寅、乙卯、庚申、辛酉四日，自专禄旺为正。甲乙宜亥卯未寅月成木局，庚申宜巳酉丑申月成金局，为秀气纯而不杂，主为人聪明有寿，平生少病，多好酒色。柱有官煞，虽身强不畏，但混杂则禄不得专，终为有祸。八字带财印食为福，运行专禄旺乡财印食旺之地，皆发富贵，怕比肩、劫财。柱无财食官印，多孤，或为僧道。经云：“干与支同，损财伤妻。”又云：“身旺无倚，定为僧为道”是也。若只一位禄，运行身旺财食印旺之地，亦主发贵。若并叠三四位禄而无财官，又取冲起对宫财福为用，或月时带官有气，以身旺逢官，尤为贵格。忌冲刑散我旺气，纵贵亦多生病。如朱文公庚戌、丙戌、甲寅、庚午，专禄得火局为食，二庚为煞，居火旺库，木秀得地，化煞为权，宜成大儒。董丞相己巳、辛未、乙卯、丁亥，专禄而得木局，全日干聚生旺秀气，运行东方身旺局，全冲起对宫之禄为权，所以大贵。

- 分字分词释义：

  - **八专日**：前文所列干支同类、禄气专一的一组日柱，日干、日支同气同类。
  - **干支同类，专禄旺**：天干地支同属一气，禄星集中不散，身强而禄旺，故曰“专禄旺”。
  - **秀气纯而不杂**：格局中以本气为主，杂煞与杂气少，故多聪明长寿、少病安稳。
  - **多好酒色**：禄旺身强，享受与欲望的能量也重，容易沉迷酒色享乐，需要后天节制。
  - **怕比肩、劫财**：比劫来分夺禄气，则“专”不再专，易损财伤妻。

- **规范化释义（primary_lang_explained）**：

  八专禄旺格，是就一类“日干日支同气、禄气专一”的日柱而言。此类日柱，禄气高度集中，若再得月令、行运配合，就好像一个人把人生资源集中押在一条主线：若取向正当，则极易成就；若被比劫分夺或引入偏门，则容易在同一主线中遭遇大的起落。

  原文强调：专禄之人多聪明长寿、少病安稳，但也多好酒色，说明禄气既可化为福寿，也可化为享乐与放纵。若命局中同时具备财、印、食等良性配合，并行运于专禄旺乡，则富贵双收；若比肩劫财过多，或禄多而无财官制约，则容易走向孤僧之途，或在婚姻、财务上反覆损耗。

- 核心要点：

  - 以**干支同类、禄气专一**为基础，再视月令与行运是否成木局、金局等纯气之象。
  - 专禄可成大福大贵之基，也可演成好酒色、孤禄或损财伤妻，关键在比劫、财官印食的搭配。
  - 禄多而无财官时，宜取冲起对宫财福或月时带官为用，以身旺逢官为贵。

- 详细解说：

  若从五行结构看，八专禄旺的优势在于“气之纯”：以甲寅、乙卯、庚申、辛酉等为代表，日主与日支同属一气，再得同类月令或三合局时，就形成高度集中的生旺之源。这样的命局，往往在某一领域具有持续投入与深耕的能力，不易半途而废。

  然而，禄气过专也带来风险：一是容易在同一类型的人际关系中反覆纠缠（如同类竞争、同门相争）；二是好酒色、好享受等倾向若得不到节制，容易“福不胜受”。原文以朱熹、董其昌等例说明，当专禄与秀气、财印、用神得宜配合时，能化为学问与权力；反之，若专禄被比劫分夺，又缺乏财官印的正向引导，则禄成孤禄，人易走向清冷或出世之途。

- **校勘与字词辨析（双语）**：

  - 原文对“八专日见前”具体所指的日柱列表，此处不再重抄前文，只在释义中以“干支同类、专禄日柱”统称。
  - “干与支同，损财伤妻”“身旺无倚，定为僧为道”两句，本稿在白话中拆开说明其象意，避免被误读为定命之语。
  - 朱文公、董丞相两造举例，本稿仅以“专禄得局、化煞为权、秀气聚集”概括其结构特征，不逐一推演细节。
  - **English**：
    - Common features extracted; details not individually elaborated.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_233]` `[trigger: 八专禄旺]` `[factor_trigger: bazhuan_luwang AND ganzhitonglei]` `[role: 主干]` 八专日干支同类，自专禄旺为正。 → 《三命通会》卷六#八专禄旺
  - `[ns_smth_06_234]` `[trigger: 秀气纯不杂]` `[factor_trigger: xiuqi_chun AND congming_youshou]` `[role: 主干依赖]` 为秀气纯而不杂，主为人聪明有寿，平生少病。 → 《三命通会》卷六#八专禄旺
  - `[ns_smth_06_235]` `[trigger: 忌比劫]` `[factor_trigger: pa_bijie AND lubudezhuang]` `[role: 条件分支]` 怕比肩、劫财。 → 《三命通会》卷六#八专禄旺
  - `[ns_smth_06_236]` `[trigger: 身旺无倚]` `[factor_trigger: shenwang_wuyi AND sengdao]` `[role: 总结]` 身旺无倚，定为僧为道。 → 《三命通会》卷六#八专禄旺"""
    normalized_text_zh: str = """"""
    subject: str = "八专禄旺与专禄纯气"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_52', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_42', 'bazi_semantic', 'bazi_state_factor_39', 'bazi_semantic', 'bazi_condition_factor_222', 'bazi_semantic', 'bazi_condition_factor_223', 'bazi_semantic', 'source_ref', 'rel_smth_06_202', 'bazhuanluwang_presence', 'rel_smth_06_203', 'luwang_chengdu', 'rel_smth_06_204', 'guansha_hunza_risk', 'evi_smth_06_202', 'bazhuanluwang_presence', 'rule_bazhuan', 'evi_smth_06_203', 'xiuqi_chundu', 'rule_xiuqi', 'evi_smth_06_204', 'gusengdao_risk', 'rule_sengdao', 'map_smth_06_135', 'map_smth_06_136']
    
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
        l1_anchor="smth_v1.0.0_八专禄旺与专禄纯气_001_L1",
    )
    version: str = "1.0.0"
