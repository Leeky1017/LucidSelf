"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066719
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
    semantic_id="smth_v1.0.0_1_富贵贫贱与五行纯杂_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1富贵贫贱与五行纯杂(SemanticEntry):
    """
    - 原文（source_text）：
  富莫富于纯粹，贫莫贫于战争。
  贵莫贵于秀实，贱莫贱于反伤。
  文章锦绣，贵马会于学堂；襟度宏阔，水火合于情性。
  深谋远虑，德星居沉静之宫；术业玄微，...
    """
    
    original_text: str = """- 原文（source_text）：
  富莫富于纯粹，贫莫贫于战争。
  贵莫贵于秀实，贱莫贱于反伤。
  文章锦绣，贵马会于学堂；襟度宏阔，水火合于情性。
  深谋远虑，德星居沉静之宫；术业玄微，帝座守文章之馆。
  魁罡有灵变之机，离坎乃聪明之户。
  贵人禄马宜逢，劫刃空亡可远。
  长生招贵人之可爱，衰败遇小人之憎嫌。
  四宫溃乱兮不仁不义，五行相生兮为孝为忠。
  印禄在刑冲之位，心乱身忙；日时居鬼库之中，忧多乐少。
  日干旺而灾咎寡，财命衰而惆怅多。
  衣食奔波，旺处遭克；利名成败，贵地逢伤。

- 分字分词释义：
  - **纯粹**：五行清纯不杂（如金白水清、木火通明）。
  - **战争**：五行相战（如金木相克，水火相冲）。
  - **秀实**：秀气流行且有根（实）。
  - **反伤**：喜用神受克。
  - **贵马会于学堂**：官星（贵）、财星（马）与长生（学堂）同位。
  - **德星**：指天月二德或印绶。
  - **帝座**：指太岁或帝旺。
  - **鬼库**：七煞库（如甲日见未，乙日见戌？应指官煞库，如甲见丑未，乙见辰戌）。

- **规范化释义（primary_lang_explained）**：
  最富有的命局莫过于五行纯粹有情，最贫穷的莫过于五行战克无情。
  最尊贵的莫过于秀气流行且有根基，最贫贱的莫过于用神受克反伤。
  若贵人、财星会聚于学堂（长生），主文章锦绣。水火既济且得地，主襟怀坦荡。
  德星（印绶）居于沉静之地，主深谋远虑。帝座（太岁）守在文章之馆（学堂），主术业精微。
  魁罡日生人机智灵变，坎离（水火）日生人聪明。
  喜逢贵人禄马，忌见劫财羊刃空亡。
  长生之地招人喜爱，衰败之地遭人憎嫌。
  地支刑冲溃乱，主不仁不义；五行顺生，主忠孝。
  印绶禄神逢刑冲，心忙身乱。日时坐在鬼库（煞库），忧多乐少。
  日干旺相，灾咎少；财星命宫衰弱，惆怅多。
  身旺处遭克，衣食奔波；贵地逢伤，名利成败。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Wealth-Nobility-Poverty-Baseness and Five Elements Pure-Mixed" from the Zeng-Ai Rhapsody:

  - Rich莫rich于Pure; poor莫poor于War. Noble莫noble于Elegant-Solid; base莫base于Reverse-Wound.
  - Literature embroidery, Noble-Horse meets学堂; deep-策far-虑, Virtue-Star居沉静palace.
  - Kui-Gang has spirit-变机; Kan-Li乃clever door.
  - Long Life招lovable; Decay-Defeat遇憎嫌.
  - Day Stem prosperous, disasters few; Wealth-fate weak, melancholy多.
  - Key: Pure (unmixed) brings wealth; War (conflict) brings poverty; Elegant-Solid (rooted) brings nobility; Reverse-Wound (Use God attacked) brings baseness.

- 核心要点：
  - **清纯为贵**：忌战克。
  - **秀实为美**：忌虚浮。
  - **神煞得位**：贵人禄马喜生旺。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_025]` `[trigger: 纯粹战争]` `[factor_trigger: chuncui_zhanzheng AND fugui_pinjian]` `[role: 主干]` 富莫富于纯粹，贫莫贫于战争。贵莫贵于秀实，贱莫贱于反伤。 → 《三命通会》卷十一#富贵贫贱与五行纯杂
  - `[ns_smth_11_026]` `[trigger: 深谋远虑]` `[factor_trigger: shenmou_yuanlv AND dexing_chenjing]` `[role: 主干依赖]` 深谋远虑，德星居沉静之宫；术业玄微，帝座守文章之馆。 → 《三命通会》卷十一#富贵贫贱与五行纯杂
  - `[ns_smth_11_027]` `[trigger: 贵人禄马]` `[factor_trigger: guiren_luma AND yifeng_keyuan]` `[role: 条件分支]` 贵人禄马宜逢，劫刃空亡可远。 → 《三命通会》卷十一#富贵贫贱与五行纯杂
  - `[ns_smth_11_028]` `[trigger: 身旺灾寡]` `[factor_trigger: shenwang_zaigua AND caimingruo_chouzhang]` `[role: 总结]` 日干旺而灾咎寡，财命衰而惆怅多。 → 《三命通会》卷十一#富贵贫贱与五行纯杂"""
    normalized_text_zh: str = """"""
    subject: str = "1 富贵贫贱与五行纯杂"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_13', 'bazi_semantic', 'bazi_structure_factor_14', 'bazi_semantic', 'bazi_state_factor_55', 'bazi_semantic', 'bazi_state_factor_56', 'bazi_semantic', 'bazi_condition_factor_10', 'bazi_semantic', 'bazi_condition_factor_11', 'bazi_semantic', 'source_ref', 'rel_smth_11_019', 'chuncui_zhanzheng', 'rel_smth_11_020', 'xiushi_fanshang', 'rel_smth_11_021', 'guima_xuetang', 'evi_smth_11_019', 'chuncui_zhanzheng', 'rule_chuncui_fu1', 'evi_smth_11_020', 'xiushi_fanshang', 'rule_xiushi_gui1', 'evi_smth_11_021', 'guima_xuetang', 'rule_guima_xuetang1', 'map_smth_11_013', 'map_smth_11_014']
    
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
        l1_anchor="smth_v1.0.0_1_富贵贫贱与五行纯杂_001_L1",
    )
    version: str = "1.0.0"
