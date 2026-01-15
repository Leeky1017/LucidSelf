"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523932
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
    semantic_id="zpzq_v1.0.0_用神专寻月令_以四柱配之_必有成败_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 用神专寻月令以四柱配之必有成败(SemanticEntry):
    """
    - **原文（source_text）**：
  用神专寻月令，以四柱配之，必有成败。何谓成？如官逢财印，又无刑冲破害，官格成也。财生官旺，或财逢食生而身强带比，或财格透印而位置妥贴，两不相克，财格成...
    """
    
    original_text: str = """- **原文（source_text）**：
  用神专寻月令，以四柱配之，必有成败。何谓成？如官逢财印，又无刑冲破害，官格成也。财生官旺，或财逢食生而身强带比，或财格透印而位置妥贴，两不相克，财格成也。印轻逢煞，或官印双全，或身印两旺而用食伤泄气，或印多逢财而财透根轻，印格成也。食神生财，或食带煞而无财，弃食就煞而透印，食格成也。身强七煞逢制，煞格成也。伤官生财，或伤官佩印而伤官旺，印有根，或伤官旺、身主弱而透煞印，或伤官带煞而无财，伤官格成也。阳刃透官煞而露财印，不见伤官，阳刃格成也。建禄月劫，透官而逢财印，透财而逢食伤，透煞而遇制伏，建禄月劫之格成也。

- 原注（原文注解）：
  　　本段论“成格”的种种情形，核心在于：
  - 用神得位、得力，又不受刑冲破害；
  - 各类格局（官、财、印、食、煞、伤、刃、建禄月劫）都有其“成格条件”；
  - 关键看“主神有根、用神得辅、忌神受制”。

- 分字分词释义：
  - 成格：用神与格局条件相符，且生克得宜，能发挥其应有之功。
  - 官逢财印：官星有财生、有印护。
  - 财生官旺：财既生官，又不损身；
  - 印轻逢煞：煞生印而印不重压日主；
  - 弃食就煞而透印：在食神生财与煞印结构之间择一而从。
  - 身强七煞逢制：日主强有力，七煞既有力又受制。
  - 伤官佩印：伤官与印同时存在，印能制伤，伤不至于反客为主。
  - 阳刃透官煞而露财印：刃旺但有官煞制之，财印辅之，而不见伤官破局。
  - 透官逢财印 / 透财逢食伤 / 透煞遇制伏：建禄月劫格中官财印食煞的适度搭配与制衡。

- **规范化释义（primary_lang_explained）**：
  这里作者以“成格”为主线，把各类格局的“成格条件”逐一列出。大意可以归纳为：
  - 官格：官星有财来生，有印来护，又不受刑冲破害；
  - 财格：财星既能生官，又不被比劫抢夺，或财透印而位置恰当，两不相克；
  - 印格：印星虽轻，却有煞生、有官印双全，身印两旺而用食伤泄气，或印多逢财而财透根轻；
  - 食格：食神能生财，或食带煞而无财时，干脆弃食就煞、透出印星成煞印格；
  - 煞格：身强七煞有制，煞为我所用；
  - 伤官格：伤官生财，或伤官佩印而伤官有力、印有根，或伤官旺而身弱、透煞印，或伤官带煞而无财，此类皆为可成之格；
  - 阳刃格：刃旺而有官煞透出制之，又有财印辅佐，不见伤官破格；
  - 建禄月劫格：透官逢财印，透财逢食伤，透煞遇制伏，皆为成格之象。

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph sets out what it really means for a pattern to be "complete". A chart is not complete merely because it can be named "Officer pattern" or "Wealth pattern"; it is complete only when the chief star has roots, the Useful God is properly assisted, and harmful stars are either absent or firmly controlled.
  In an Officer pattern, the Officer star must be supported by Wealth and protected by Resource, and must not be injured by Hurting Officer, punishment, clash or other forms of disruption. In a Wealth pattern, Wealth has to be strong enough to generate Officer and yet not be robbed away by Companions; or Wealth appears together with Resource in such positions that the two can cooperate without mutual damage. In a Resource pattern, Resource may be light, yet is enlivened by Killings, backed by Officer and Resource together, or shared by both Day Master and Resource so that Food and Hurting can be used to vent the surplus; even when much Resource meets Wealth, the exposed Wealth must be light so that the seal is not emptied. A Food-God pattern is complete when Food can safely generate Wealth; when Food coexists with Killings and Wealth is absent, one simply abandons the Food-God approach and instead follows Killing and Resource, turning it into a Killing–Resource structure. A Seven-Killings pattern is only usable when the Day Master is strong and Killings are present with proper restraint, so that harsh power can be harnessed instead of feared.
  Hurting-Officer patterns are complete when Hurting is able to give birth to Wealth, or when Hurting "wears a seal" and Resource is rooted, or when Hurting is strong, the body somewhat weak, and Killings and Resource both appear to tie the structure together, or when Hurting and Killings appear without Wealth so that the pattern remains internally consistent. Yang-Blade patterns require a powerful Blade that is checked by exposed Officer or Killings, with Wealth and Resource assisting and no Hurting-Officer to spoil the configuration. In Establishment-and-Robbery patterns, when the stems show Officer, Wealth or Killings, each must be matched with the appropriate helpers—Officer with Wealth and Resource, Wealth with Food-God and Hurting-Officer, Killings with control and transformation—so that the overall qi flow is coherent. All these are specific illustrations of one principle: the chief significator must be rooted, the Useful God must be helped, and the malefic stars must be held in check.

- 详细解说：
  - 每一类格局都有自己的“理想配置”：谁为主神、谁为辅神、谁为护神、谁为制神，必须搭配得宜。
  - “成格”并非只看一种神强，而在于整体气机是否协调：有生有护、有制有化。
  - 识别成格，是后面谈成败、救应的基础。

- 核心要点：
  - 成格三问：
    1) 主神是否得令有根？
    2) 用神是否得生得护？
    3) 忌神是否受制或不致妨害？
  - 官财印食煞伤刃建禄月劫八类格局，各有其“成格模板”。

- 应用推演：
  1) 先定本局属于哪一类格局（官、财、印、食、煞、伤、刃、建禄月劫）；
  2) 对照本段条目，看其是否满足成格条件；
  3) 若主神有根、用神得辅、忌神有制，则可判为“成格”；
  4) 再进一步看成格高低与岁运配合。

- 反例与边界：
  - 一见“官星透、财星透”便言官格成，不看印与伤；
  - 见七煞便言凶，不看是否身强、有食制、有印护。"""
    normalized_text_zh: str = """"""
    subject: str = "用神专寻月令，以四柱配之，必有成败"
    factor_refs: list = ['chengge_tiaojian', 'guange_cheng', 'caige_cheng', 'yinge_cheng', 'shage_cheng', 'engine_id', 'bage_chengge_moban', 'bazi_rule_engine', 'zhushen_yougen', 'bazi_rule_engine', 'yongshen_defu', 'bazi_rule_engine', 'jishen_shouzhi', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_091', 'zhushen_yougen', 'rel_zpzq_092', 'yongshen_defu', 'rel_zpzq_093', 'jishen_shouzhi', 'evi_zpzq_090', 'guange_cheng', 'rule_guange_cheng', 'evi_zpzq_091', 'shage_cheng', 'rule_shage_cheng', 'concept_ideal_structure', 'concept_balance']
    
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
        l1_anchor="zpzq_v1.0.0_用神专寻月令_以四柱配之_必有成败_001_L1",
    )
    version: str = "1.0.0"
