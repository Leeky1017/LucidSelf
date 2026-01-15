"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066766
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
    semantic_id="smth_v1.0.0_4_阴阳顺逆与神煞灾福_001",
    book_id="sanming",
    engine_id="bazi"
)
class 4阴阳顺逆与神煞灾福(SemanticEntry):
    """
    - 原文（source_text）：
  大段天元羸弱，宫吉不及以为荣；中下兴隆，卦凶不能成其咎。
  若遇尊凶卑吉，救疗无功；尊吉卑凶，逢灾自愈。
  禄有三会，灾有五期。
  凶多吉少，类大过之初...
    """
    
    original_text: str = """- 原文（source_text）：
  大段天元羸弱，宫吉不及以为荣；中下兴隆，卦凶不能成其咎。
  若遇尊凶卑吉，救疗无功；尊吉卑凶，逢灾自愈。
  禄有三会，灾有五期。
  凶多吉少，类大过之初爻；福浅祸深，喻同人之九五。
  闻喜不喜，是六甲之亏盈；当忧不忧，赖五行之救助。
  八孤临于五墓，戌未东行；六虚下于空亡，自乾南首。
  天元一气，定侯伯之迁荣；支作人元，运商徒而得失。

- 分字分词释义：
  - **天元羸弱**：日干衰弱。
  - **宫吉**：坐下财官印吉。
  - **中下兴隆**：地支与纳音旺相。
  - **尊卑**：年为尊，日时为卑；或天干为尊，地支为卑。
  - **禄有三会**：长生、帝旺、库。
  - **灾有五期**：衰、病、死、败、绝。
  - **八孤五墓**：神煞（孤辰寡宿、墓库）。

- **规范化释义（primary_lang_explained）**：
  大体上，若天干（日主）羸弱，即使地支宫位吉利（财官），也难以享受荣耀（身弱不胜财官）。若地支与纳音兴隆（身旺），即使卦象（神煞）有凶，也不能构成大害。
  若尊位（年/干）凶而卑位（日时/支）吉，救疗无功（根基坏了）；若尊位吉而卑位凶，逢灾自愈（根基稳固）。
  禄有三会（生旺库），灾有五期（衰病死败绝）。
  凶多吉少，像《大过》卦初爻，宜慎重；福浅祸深，像《同人》卦九五，先号啕而后笑（先难后易）。
  闻喜不喜，是因为六甲气数亏缺（空亡或失令）；当忧不忧，是因为有五行救助（有制化）。
  八孤（孤辰寡宿）临于五墓（辰戌丑未），六虚（空亡对冲）下于空亡，皆为凶煞。
  天元一气（干支一气或天干纯粹），定侯伯之贵；地支作人元（藏干），定商贾之利。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Yin-Yang顺逆 and Spirit-Killings Disaster-Fortune" from the Xiao-Xi Rhapsody:

  - Major天元weak, palace吉not及for荣; middle-lower兴隆, hexagram凶cannot成咎.
  - If遇尊凶卑吉, rescue-療no功; 尊吉卑凶, meet灾self-heals.
  - Salary has三会 (Long Life, Prosperous, Treasury); disaster has五期 (Decay, Sick, Dead, Defeat, Extinct).
  - Hear喜not喜, is六甲亏盈; should忧not忧, relies五行救助.
  - Key: Day Master strength is foundation; Superior position determines root stability; Five Elements rescue can resolve disasters.

- 核心要点：
  - **身旺为本**：天元不可弱。
  - **尊卑有序**：年柱/天干为重。
  - **神煞与五行**：五行救助可解神煞之凶。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_034]` `[trigger: 天元羸弱]` `[factor_trigger: tianyuan_leiruo AND gongjili_wuyi]` `[role: 主干]` 大段天元羸弱，宫吉不及以为荣；中下兴隆，卦凶不能成其咎。 → 《三命通会》卷十一#阴阳顺逆与神煞灾福
  - `[ns_smth_11_035]` `[trigger: 尊卑吉凶]` `[factor_trigger: zunbei_jixiong AND jiuzhi_youxu]` `[role: 主干依赖]` 若遇尊凶卑吉，救疗无功；尊吉卑凶，逢灾自愈。 → 《三命通会》卷十一#阴阳顺逆与神煞灾福
  - `[ns_smth_11_036]` `[trigger: 禄灾五期]` `[factor_trigger: luyou_sanhui AND zaiyou_wuqi]` `[role: 条件分支]` 禄有三会，灾有五期。 → 《三命通会》卷十一#阴阳顺逆与神煞灾福
  - `[ns_smth_11_037]` `[trigger: 五行救助]` `[factor_trigger: wuxing_jiuzhu AND dangyu_buyou]` `[role: 条件分支]` 闻喜不喜，是六甲之亏盈；当忧不忧，赖五行之救助。 → 《三命通会》卷十一#阴阳顺逆与神煞灾福
  - `[ns_smth_11_038]` `[trigger: 天元一气]` `[factor_trigger: tianyuan_yiqi AND dinghoubo_qianrong]` `[role: 总结]` 天元一气，定侯伯之迁荣；支作人元，运商徒而得失。 → 《三命通会》卷十一#阴阳顺逆与神煞灾福"""
    normalized_text_zh: str = """"""
    subject: str = "4 阴阳顺逆与神煞灾福"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_18', 'bazi_semantic', 'bazi_state_factor_72', 'bazi_semantic', 'bazi_state_factor_68', 'bazi_semantic', 'bazi_state_factor_69', 'bazi_semantic', 'bazi_relation_wuxing', 'bazi_semantic', 'bazi_condition_factor_12', 'bazi_semantic', 'source_ref', 'rel_smth_11_031', 'core_factor', 'rel_smth_11_032', 'cond_factor', 'rel_smth_11_033', 'risk_factor', 'evi_smth_11_031', 'core_factor', 'rule_name31', 'evi_smth_11_032', 'cond_factor', 'rule_name32', 'evi_smth_11_033', 'risk_factor', 'rule_name33', 'map_smth_11_021', 'map_smth_11_022']
    
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
        l1_anchor="smth_v1.0.0_4_阴阳顺逆与神煞灾福_001_L1",
    )
    version: str = "1.0.0"
