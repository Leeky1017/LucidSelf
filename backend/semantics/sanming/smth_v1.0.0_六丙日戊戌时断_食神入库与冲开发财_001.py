"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157549
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
    semantic_id="smth_v1.0.0_六丙日戊戌时断_食神入库与冲开发财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日戊戌时断食神入库与冲开发财(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日戊戌时断。

  六丙日生时戊戌，食神入库火明堂；戌冲辰位财官旺，卯未中和福禄长。丙日戊戌时，食神入库，戊土食神，戌上戊土库。若生辰戌丑未月，无冲刑，...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日戊戌时断。

  六丙日生时戊戌，食神入库火明堂；戌冲辰位财官旺，卯未中和福禄长。丙日戊戌时，食神入库，戊土食神，戌上戊土库。若生辰戌丑未月，无冲刑，文章秀发，有冲刑，武职权贵。生身旺月者贵。

  丙子日戊戌时，冲官，怕见巳字。夏秋寒门贵。辰月，财官双美，行水运，贵。亥子申，俱吉。

  丙寅日戊戌时，春金水运，大贵。夏平，秋富，冬贵。

  丙辰日戊戌时，辰戌相冲，生杂气月者贵。年月无壬癸亥，行西运，官至三品。

  丙午日戊戌时，贵。若年月无壬癸亥巳字，天干透印食者，入格。卯月，最贵。寅午戌巳月，火旺，不贵。子丑申酉，富。

  丙申日戊戌时，春富，夏平，秋贵，冬吉。

  丙戌日戊戌时，杂气魁罡。辰月，冲出财官则贵。巳酉丑、申子辰，无破者富贵。

  丙戊相逢遇戌时，食神入库喜相宜；若无冲破福禄厚，有犯刑克损与亏。丙日戊戌时藏，食神入库难当。若还冲动发财官，不冲终为平常。

- 分字分词释义：

  - **食神入库**：戊土食神入戌库，食神有收藏。
  - **冲开发财**：辰冲戌，冲开食神库，财官可用。
  - **杂气魁罡**：戌为杂气之地，又为魁罡位。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，戊戌时」：

  - 戊土食神入戌库，若生辰戌丑未月，食神有根；若辰冲戌，冲开库位，财官可用；
  - 无冲刑者文章秀发，有冲刑者武职权贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Wu-Xu Hour":

  - Wu Earth Food God enters Xu treasury; if born in Chen-Xu-Chou-Wei months, food god has roots; if Chen clashes Xu, treasury opens and wealth-official become usable.
  - Without clash-punishment: literary refinement and elegance; with clash-punishment: military position and authority.

- 核心要点：

  - 本格以「食神入库」为核心，需冲开方能发用。
  - 冲开则财官旺，不冲则平常。
  - 身旺月者更能发挥食神生财的功能。

- 详细解说：

  1. **食神入库的特点**  
     - 戊土食神入戌库，有储藏之象；  
     - 需要辰冲或行运冲开，方能发挥。

  2. **冲与不冲的差异**  
     - 有冲则财官涌出，主武职权贵；  
     - 无冲则储而不发，文章秀发但平稳。

- 校勘与字词辨析：

  - 「火明堂」形容丙火明亮，食神得用。
  - 「卯未中和」指卯未半合木局，调和命局。
  - **English**：
    - Mao-Wei half-wood combination harmonizes the chart.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_137]` `[trigger: 食神入库]` `[factor_trigger: shishen_ruku AND huo_mingtang]` `[role: 主干]` 六丙日生时戊戌，食神入库火明堂。 → 《三命通会》卷八#六丙日戊戌时
  - `[ns_smth_08_138]` `[trigger: 戌冲辰位]` `[factor_trigger: xuchong_chenwei AND caiguan_wang]` `[role: 主干依赖]` 戌冲辰位财官旺，卯未中和福禄长。 → 《三命通会》卷八#六丙日戊戌时
  - `[ns_smth_08_139]` `[trigger: 有冲发财]` `[factor_trigger: youchong_facai AND wu_xingke]` `[role: 条件分支]` 若无冲刑，文章秀发；有冲刑，武职权贵。 → 《三命通会》卷八#六丙日戊戌时
  - `[ns_smth_08_140]` `[trigger: 冲动发官]` `[factor_trigger: chongdong_faguan AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发财官，不冲终为平常。 → 《三命通会》卷八#六丙日戊戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日戊戌时断：食神入库与冲开发财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_shishen_4', 'bazi_semantic', 'bazi_state_factor_211', 'bazi_semantic', 'bazi_state_factor_181', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_103', 'shishen_ruku', 'rel_smth_08_104', 'chongkai_facai', 'rel_smth_08_105', 'youchong_youfa', 'evi_smth_08_103', 'shishen_ruku', 'rule_ruku2', 'evi_smth_08_104', 'chongkai_facai', 'rule_chongkai', 'evi_smth_08_105', 'zaqi_kuigang', 'rule_kuigang', 'map_smth_08_069', 'map_smth_08_070']
    
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
        l1_anchor="smth_v1.0.0_六丙日戊戌时断_食神入库与冲开发财_001_L1",
    )
    version: str = "1.0.0"
