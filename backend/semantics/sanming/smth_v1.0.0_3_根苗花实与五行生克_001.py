"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066755
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
    semantic_id="smth_v1.0.0_3_根苗花实与五行生克_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3根苗花实与五行生克(SemanticEntry):
    """
    - 原文（source_text）：
  或若生逢休败之地，早岁孤穷；老遇建旺之乡，临年偃蹇。
  若乃初凶后吉，以源浊而流清；始吉终凶，类根甘而裔苦。
  观乎萌兆，察以其原。根在苗先，实从花后。
...
    """
    
    original_text: str = """- 原文（source_text）：
  或若生逢休败之地，早岁孤穷；老遇建旺之乡，临年偃蹇。
  若乃初凶后吉，以源浊而流清；始吉终凶，类根甘而裔苦。
  观乎萌兆，察以其原。根在苗先，实从花后。
  胎生元命，三兽定其门宗；律吕宫商，五虎论其成败。
  无合有合，后学难知；得一分三，前贤不载。
  年虽逢于冠带，尚有余灾；运初至于衰乡，犹披鲜福。

- 分字分词释义：
  - **根苗花实**：胎为根，月为苗，日为花，时为实。
  - **三兽**：生年、生月、生胎之生肖（如子鼠、丑牛等）。
  - **律吕宫商**：纳音五行。
  - **五虎**：五虎遁（年上起月）。
  - **得一分三**：地支三合（如见寅，可合午戌，得一而分三）。

- **规范化释义（primary_lang_explained）**：
  如果八字生在休囚败绝之地，早年孤苦贫穷；晚年运至建禄旺相之乡，却因年老体衰而偃蹇（虽旺无用）。
  如果是初凶后吉，是因为源头浊而流处清（年柱差而日时好，或早运差晚运好）；如果是始吉终凶，好比根甜而果苦（年好时差）。
  看命要观察萌兆，追溯根源。根（胎）在苗（月）之先，实（时）在花（日）之后。
  胎元与元命（年），用三兽（生肖）定其门宗（出身）。用纳音（律吕宫商）和五虎遁（月建）论其成败。
  无合有合（暗合，如寅合亥，柱无亥有壬），后学难以知晓。得一分三（三合局见一字即暗邀其余），前贤未载。
  大运刚交入冠带旺地，可能还有上个运的余灾；运刚交入衰乡，可能还带有上个旺运的余福。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Root-Seedling-Flower-Fruit and Five Elements生克" from the Xiao-Xi Rhapsody:

  - If生meets rest-defeat place, early years孤穷; old遇建旺district, approaching years偃蹇.
  - Initial凶later吉, because source浊while flow清; beginning吉终凶, like root甘while offspring苦.
  - Root在苗先, fruit从花后—Year (Fetal), Month (Seedling), Day (Flower), Hour (Fruit).
  - Without合has合 (hidden combines), later学难知; gain-one分-three (Triple Union暗invites), former贤not载.
  - Key: Root-Seedling-Flower-Fruit metaphor for life stages; hidden combines and Triple Union invitations; luck cycle residual effects.

- 核心要点：
  - **限运吉凶**：根苗花实看一生。
  - **暗合局**：得一分三。
  - **交脱运**：余灾余福。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_030]` `[trigger: 根苗花实]` `[factor_trigger: genmiaohuashi AND xianyun_jixiong]` `[role: 主干]` 根在苗先，实从花后。观乎萌兆，察以其原。 → 《三命通会》卷十一#根苗花实与五行生克
  - `[ns_smth_11_031]` `[trigger: 源浊流清]` `[factor_trigger: yuanzhuo_liuqing AND chuji_houxiong]` `[role: 主干依赖]` 若乃初凶后吉，以源浊而流清；始吉终凶，类根甘而裔苦。 → 《三命通会》卷十一#根苗花实与五行生克
  - `[ns_smth_11_032]` `[trigger: 得一分三]` `[factor_trigger: deyi_fensan AND sanhe_anyao]` `[role: 条件分支]` 无合有合，后学难知；得一分三，前贤不载。 → 《三命通会》卷十一#根苗花实与五行生克
  - `[ns_smth_11_033]` `[trigger: 余灾余福]` `[factor_trigger: yuzai_yufu AND jiaoyin_canyu]` `[role: 总结]` 年虽逢于冠带，尚有余灾；运初至于衰乡，犹披鲜福。 → 《三命通会》卷十一#根苗花实与五行生克"""
    normalized_text_zh: str = """"""
    subject: str = "3 根苗花实与五行生克"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_17', 'bazi_semantic', 'bazi_state_factor_100', 'bazi_semantic', 'bazi_state_factor_65', 'bazi_semantic', 'bazi_relation_factor_17', 'bazi_semantic', 'bazi_state_factor_66', 'bazi_semantic', 'bazi_factor_25', 'bazi_semantic', 'source_ref', 'rel_smth_11_028', 'genmiaohuashi', 'rel_smth_11_029', 'deyi_fensan', 'rel_smth_11_030', 'yuzai_yufu', 'evi_smth_11_028', 'genmiaohuashi', 'rule_genmiaohuashi1', 'evi_smth_11_029', 'deyi_fensan', 'rule_deyi_fensan1', 'evi_smth_11_030', 'yuzai_yufu', 'rule_yuzai_yufu1', 'map_smth_11_019', 'map_smth_11_020']
    
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
        l1_anchor="smth_v1.0.0_3_根苗花实与五行生克_001_L1",
    )
    version: str = "1.0.0"
