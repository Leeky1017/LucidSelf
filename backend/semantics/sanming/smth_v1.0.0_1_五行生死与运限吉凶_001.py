"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081110
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
    semantic_id="smth_v1.0.0_1_五行生死与运限吉凶_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1五行生死与运限吉凶(SemanticEntry):
    """
    - 原文（source_text）：
  欲知五行生死诀，容易岂与凡人说。五星只在限为凭，子平专以运中决。
  生知富贵问前程，死时未审如何截。格局只以用神推，用不受伤人不灭。
  运行先布十二宫，看...
    """
    
    original_text: str = """- 原文（source_text）：
  欲知五行生死诀，容易岂与凡人说。五星只在限为凭，子平专以运中决。
  生知富贵问前程，死时未审如何截。格局只以用神推，用不受伤人不灭。
  运行先布十二宫，看于何宫受某节。财官印绶与食神，当知轻重审分明。
  官星怕行七煞运，偏官尤畏正官临。官煞混行当知审，去煞留官仔细评。
  留官去煞莫逢煞，留煞去官官莫逢。官煞受伤人自绝，更看财格定前程。
  日时偏正问何财，又怕干头带煞来。煞运重逢人亦夭，孰知偏正是为灾。
  自专偏正皆为福，兄弟同分是祸媒。运到正财必争竞，各宜偏正两分推。
  有财官运须荣发，官运财乡是福胎。只怕日干元自弱，财多生鬼赶身衰。
  财多身弱行财运，此处方知入泉台。官不受伤财不劫，寿山高耸岂能颓。

- 分字分词释义：
  - **五星**：七政四余（星宗）。
  - **子平**：八字命理。
  - **用不受伤**：用神不被克坏。
  - **兄弟同分**：比劫争财。
  - **泉台**：黄泉。

- **规范化释义（primary_lang_explained）**：  
  本段骨髓歌先从方法论入手，强调“看命以用神为本，以行运为凭”。星宗一派着重大运限度的推断，子平一派则特别重视岁运流转中，用神是否得到保护或打击。判断富贵与寿夭，关键在于：  
  其一，要先定出真正的用神，再看此神在命局与运程中是否受伤。用神安然不受重克，多主人不至夭折；一旦用神在原局或行运中被严重损毁，则有性命之忧。  
  其二，要分清财、官、印、食之间的轻重次序。正官怕行七煞运，七煞又怕行正官运，官煞混杂之时，必须“去煞留官”，取其清纯一方。  
  其三，财星格局须严分偏正。财多而身弱，再行财运，往往是“财多生鬼”，把日主压垮，甚至直指死亡；反之，财为我所专享而不被兄弟比劫分夺，则是福源。  
  其四，若官星一路不受伤，财星又不被劫夺，则身与用神俱安，寿命绵长，可比寿山不倒。整段文字以歌诀形式，将“用神不受伤”“身财平衡”“官煞去留”三大原则压缩为生死富贵的总纲。

- **完整对等诠释（secondary_lang_full）**：  
  This verse lays out a condensed doctrine of life and death in destiny analysis. It insists that one must first identify the true "useful spirit" (yongshen)—the key element or configuration that carries the chart's central mandate—and then track how it is treated across the flow of time. A chart whose yongshen remains intact through natal structure and major cycles is unlikely to end in ruin; when that same core support is repeatedly damaged or exhausted, the person is said to "enter the spring terrace," a metaphor for death.  
  Wealth and Office do not simply add prosperity; they must be weighed against the strength of the Day Master. When Proper Officer and Seven Killings intermingle, they require careful pruning—retaining what represents legitimate authority and trimming away what acts as destructive violence. In wealth-centered patterns, one must distinguish between direct and indirect wealth and be wary whenever fortune cycles repeatedly stimulate aggressive Killings; the same money that promises opportunity can easily turn into the agent of one's downfall. If wealth is enjoyed exclusively by the self and not constantly contested by siblings and peers, it becomes a blessing; if it is shared out in chronic competition, it becomes a source of depletion. When Official stars are not harmed and Wealth stars are not robbed, the text says, longevity rises like an unmoving southern mountain: the interplay of factors supports a long, stable life rather than a brief flare of success.

- 核心要点：
  - **用神为命**：用神受损则死。
  - **身财平衡**：财多身弱死。
  - **官煞去留**：混杂不吉。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_025]` `[trigger: 五行生死]` `[factor_trigger: wuxing_shengsi AND yongshen_weiming]` `[role: 主干]` 欲知五行生死诀，容易岂与凡人说。格局只以用神推，用不受伤人不灭。 → 《三命通会》卷十二#五行生死与运限吉凶
  - `[ns_smth_12_026]` `[trigger: 官煞去留]` `[factor_trigger: guansha_quliu AND hunza_shenji]` `[role: 主干依赖]` 官煞混行当知审，去煞留官仔细评。留官去煞莫逢煞，留煞去官官莫逢。 → 《三命通会》卷十二#五行生死与运限吉凶
  - `[ns_smth_12_027]` `[trigger: 财多身弱]` `[factor_trigger: caiduo_shenruo AND ruyuantai]` `[role: 条件分支]` 只怕日干元自弱，财多生鬼赶身衰。财多身弱行财运，此处方知入泉台。 → 《三命通会》卷十二#五行生死与运限吉凶
  - `[ns_smth_12_028]` `[trigger: 寿山高耸]` `[factor_trigger: shoushan_gaosong AND guanbushang_caibujie]` `[role: 总结]` 官不受伤财不劫，寿山高耸岂能颓。 → 《三命通会》卷十二#五行生死与运限吉凶"""
    normalized_text_zh: str = """"""
    subject: str = "1 五行生死与运限吉凶"
    factor_refs: list = ['engine_id', 'bazi_structure_yongshen_degree', 'bazi_state_relation', 'bazi_factor_38', 'bazi_factor_1', 'bazi_yongshen_1', 'protect_yongshen_first', 'source_ref', 'rel_smth_12_025', 'core_factor', 'rel_smth_12_026', 'cond_factor', 'rel_smth_12_027', 'risk_factor', 'evi_smth_12_025', 'core_factor', 'rule_name25', 'evi_smth_12_026', 'cond_factor', 'rule_name26', 'evi_smth_12_027', 'risk_factor', 'rule_name27', 'map_smth_12_017', 'map_smth_12_018']
    
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
        l1_anchor="smth_v1.0.0_1_五行生死与运限吉凶_001_L1",
    )
    version: str = "1.0.0"
