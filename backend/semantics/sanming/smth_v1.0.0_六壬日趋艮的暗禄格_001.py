"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412386
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
    semantic_id="smth_v1.0.0_六壬日趋艮的暗禄格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日趋艮的暗禄格(SemanticEntry):
    """
    - **原文（source_text）**：

  此格乃六壬日见甲寅时，合出亥中壬禄，即暗禄格。经云：明禄不如暗禄是也。忌亥字填实，怕冲刑克破。壬寅、壬辰二日为正，见寅字多者大富，以寅中甲木食神生丙...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格乃六壬日见甲寅时，合出亥中壬禄，即暗禄格。经云：明禄不如暗禄是也。忌亥字填实，怕冲刑克破。壬寅、壬辰二日为正，见寅字多者大富，以寅中甲木食神生丙火长生之财，财旺生官，故美。忌官煞损身，申庚伤甲，不能生财，为凶。又曰：壬日多见寅字，用寅中甲木暗邀己土为壬官星，寅中丙火暗邀辛金为壬印绶，怕午合申冲，忌财官填实，喜身旺地，岁运同。口诀云：六壬趋艮，逢亥月必贫。《相心赋》云：六壬趋艮，智足多仁。《真宝赋》云：六壬趋艮，透财印为奇，官煞来侵，反为贫穷下贱。

- 分字分词释义：

  - **六壬日见甲寅时**：指六个壬日（壬子、壬寅、壬辰、壬午、壬申、壬戌）见甲寅时，寅居东北艮位，故名“趋艮”。
  - **合出亥中壬禄，即暗禄格**：通过寅、亥之间的合引，将亥中壬水之禄暗中引出，为“暗禄”，区别于日支明见禄位的“明禄”。
  - **明禄不如暗禄**：暗藏之禄经结构牵引而起，更具机缘性与隐蔽性，被视为优于直接坐禄。
  - **忌亥字填实，怕冲刑克破**：亥位若被过多支神填实或遭刑冲克害，则暗禄之位被占或被破，格局难成。
  - **壬寅、壬辰二日为正，见寅字多者大富**：以壬寅、壬辰二日为正格日，命局寅多则以寅中甲木生丙火之财，财旺生官，富贵之象更显。
  - **寅中甲木暗邀己土为官，丙火暗邀辛金为印**：以寅中甲木引出己土作壬之官星，以寅中丙火引出辛金作壬之印绶，皆属“暗邀”之象。
  - **怕午合申冲，忌财官填实**：午火合申、冲亥等，会破坏寅亥间的暗合结构；财官填实亥寅之位，则暗禄转为明官财，格局失其妙。
  - **六壬趋艮，逢亥月必贫**：提示若再逢亥月，亥水过重，反使暗禄失衡，易应贫薄之象。

- **规范化释义（primary_lang_explained）**：

  六壬趋艮格，是六个壬日在甲寅时形成的一种“暗禄格”。壬水之禄在亥，若通过寅亥之间的合引，把亥中的壬禄暗暗牵出，则日主获得一份不明露的禄位与贵气。古人以“明禄不如暗禄”称之，认为这种通过结构暗起的禄，比单纯日坐禄地更灵动、更有机缘。
  
  经典中以壬寅、壬辰二日为正格：寅中藏甲、丙、戊，甲为食神、生丙火之财，财旺再生官；同时又以寅中甲木暗邀己土为官星、以丙火暗邀辛金为印绶，使壬水日主在“趋艮”的结构中，同时获得财、官、印三重资源。但这一切都建立在暗局不被破坏的前提上：亥不可填实、不可多遭刑冲，午申等支若合冲过度，则暗禄被扰，反成贫薄之象。

- 核心要点：

  - 本格以**六壬日 + 甲寅时**为基础条件，属于壬日专用格。
  - 通过寅亥结构合出亥中壬禄，构成“暗禄”，强调“明禄不如暗禄”。
  - 壬寅、壬辰为尤佳之日，多寅则食神生财、财生官，成富贵之象。
  - 忌亥位填实、亥寅遭刑冲，忌午申等破局；同时须防官煞过重损身。

- 详细解说：

  若从结构线路来解读，可以分三层：
  
  1. **禄层**：壬禄在亥，通过寅亥之间的隐合，壬禄由“隐”转“显”，但仍不以日支直坐的形式出现；
  2. **财官层**：寅中甲木为食神，生丙火为财，财旺生官，使壬水在趋艮之局中同时兼得财与官；
  3. **印层**：寅中丙火又可暗邀辛金为印，使壬水既得财官，又有印绶调和克泄生制。
  
  由于这些关系多在地支藏干中完成，表现为“暗邀”“暗禄”，所以格局一方面颇具灵动弹性，另一方面也更怕外来冲合。亥若被填实或再逢亥月、水局成泛，原本精微的暗禄格所依赖的张力被冲淡，便容易由“智足多仁”的美象，滑向“逢亥月必贫”的反面。

- **校勘与字词辨析（双语）**：

  - 原文中“合出亥中壬禄，即暗禄格。经云：明禄不如暗禄是也”一句，本稿据底本保留，并在释义中将“暗禄格”与一般“坐禄”加以区分。
  - “用寅中甲木暗邀己土为壬官星，寅中丙火暗邀辛金为壬印绶”中的“暗邀”，本稿理解为“通过藏干引出”的技术用语，在白话中以“暗中牵引”解释。
  - “六壬趋艮，逢亥月必贫”一句，本稿视为对亥水过重破坏暗禄平衡的警示，而非一见亥月必然贫困的绝对论断。
  - **English**：
    - The sentence "combining to bring out Ren salary in Hai, this is the Hidden-Salary pattern; classics say 'visible salary is not as good as hidden salary'" is preserved; this edition distinguishes "hidden salary" from general "sitting on salary."
    - The term "secretly inviting" in "using Jia wood in Yin to secretly invite Ji earth as Ren's official" is understood as a technical term meaning "drawing out through hidden stems"; explained in vernacular as "secretly attracting."
    - The sentence "Six Ren Approaching Gen, meeting Hai month is surely poor" is treated as a warning about excessive Hai water disrupting the hidden-salary balance, not an absolute prediction.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_057]` `[trigger: 六壬趋艮定义]` `[factor_trigger: liuren_qugen_presence]` `[role: 主干]` 此格乃六壬日见甲寅时，合出亥中壬禄，即暗禄格。 → 《三命通会》卷六#六壬趋艮
  - `[ns_smth_06_058]` `[trigger: 明禄不如暗禄]` `[factor_trigger: ming_lu_bu_ru_an_lu]` `[role: 主干依赖]` 经云：明禄不如暗禄是也。 → 《三命通会》卷六#六壬趋艮
  - `[ns_smth_06_059]` `[trigger: 忌亥填实]` `[factor_trigger: ji_hai_tianshi OR pa_chongxing]` `[role: 条件分支]` 忌亥字填实，怕冲刑克破。壬寅、壬辰二日为正，见寅字多者大富。 → 《三命通会》卷六#六壬趋艮
  - `[ns_smth_06_060]` `[trigger: 智足多仁]` `[factor_trigger: zhi_zu_duo_ren]` `[role: 总结]` 《相心赋》云：六壬趋艮，智足多仁。 → 《三命通会》卷六#六壬趋艮

- **完整对等诠释（secondary_lang_full）**：
  The "Six Ren Approaching Gen" pattern is a hidden-salary configuration for all six Ren days born at Jia-Yin hour. Yin occupies the Gen (Northeast) sector, hence "approaching Gen". Through the Yin-Hai combination, Ren's salary hidden in Hai is drawn out indirectly—this is the "hidden salary" principle, considered superior to openly sitting on one's salary branch. The classics say "open salary is not as good as hidden salary" because the hidden form carries more serendipity and subtlety.
  
  The pattern operates on three interlocking layers: (1) Salary layer—Yin-Hai combination pulls out Ren's salary from Hai; (2) Wealth layer—Jia wood (Eating God) inside Yin produces Bing fire (Ren's wealth at long-life position), and wealth in turn generates official; (3) Seal layer—Bing fire inside Yin can further invite Xin metal as Seal, giving Ren both wealth-official support and Seal harmony. Because these linkages occur through hidden stems, the pattern is nimble but also fragile: if Hai is filled by another branch or if Hai-month flooding dilutes the tension, the delicate balance collapses.
  
  The ideal native is "wise and benevolent" (zhi zu duo ren). Revealing wealth and Seal transparently on the stems is auspicious; however, if official-and-Killer invade and the body is weak, the same structure becomes a source of poverty and lowliness. When Shen-Geng metal injures Jia wood, the food-god-to-wealth chain breaks and misfortune follows. Thus the pattern demands a strong body and careful avoidance of excessive Hai water or hostile metal clashing the hour."""
    normalized_text_zh: str = """"""
    subject: str = "六壬日趋艮的暗禄格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_ren_gen_marker', 'bazi_semantic', 'bazi_structure_factor_79', 'bazi_semantic', 'bazi_state_factor_11', 'bazi_semantic', 'bazi_state_degree_1', 'bazi_semantic', 'bazi_condition_hai', 'bazi_semantic', 'bazi_condition_hai_water', 'bazi_semantic', 'source_ref', 'rel_smth_06_043', 'liuren_qugen_presence', 'rel_smth_06_044', 'sanceng_jiegou_wanzheng', 'rel_smth_06_045', 'haizi_tianshi_risk', 'evi_smth_06_043', 'anlu_hechu_lujing', 'rule_qugen', 'evi_smth_06_044', 'sanceng_jiegou_wanzheng', 'rule_anlu', 'evi_smth_06_045', 'haiyue_shuiju_fanlan', 'rule_haiyue', 'map_smth_06_029', 'map_smth_06_030']
    
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
        l1_anchor="smth_v1.0.0_六壬日趋艮的暗禄格_001_L1",
    )
    version: str = "1.0.0"
