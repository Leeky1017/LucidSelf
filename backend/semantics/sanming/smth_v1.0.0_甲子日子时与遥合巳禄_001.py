"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412214
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
    semantic_id="smth_v1.0.0_甲子日子时与遥合巳禄_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲子日子时与遥合巳禄(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：甲子日再遇子时，畏庚辛申酉丑午。此格以甲子日、甲子时，甲以辛为官，二子中癸水能遥合巳中戊土，戊来合癸，畏子上甲木克制，不敢来合。戊与丙...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：甲子日再遇子时，畏庚辛申酉丑午。此格以甲子日、甲子时，甲以辛为官，二子中癸水能遥合巳中戊土，戊来合癸，畏子上甲木克制，不敢来合。戊与丙同居巳宫，丙戊为父子，戊动丙亦动，丙却与酉中辛相合来克甲木，甲日得官星，戊方得合癸，是谓巳酉丑三合会起官星局。年月大怕有午冲子、丑绊子，不能遥矣。
  
  又曰：此格以二子中癸水遥合巳中戊土为甲之财，丙戊禄同在巳，丙是甲之爵星，戊是丙之爵星；戊动丙亦动，丙见子，戊贪合癸妻为印绶，丙却合起辛金为甲之官，如人有子继其后，传其家，以成父道之尊贵。喜生壬癸亥子月印旺，卯寅月身旺，行官旺乡，必主登科食禄，权贵浊富。忌见庚辛丙字明露，申酉巳字破格，如有制化，亦不为害。柱有丑午绊冲，则减分数，岁运同。若生酉丑月，只作正官格，取虚露庚字，亦主富贵，全看月令何如，或可煞生印助。若成此格，须忌尤怕南方运。如樊继祖尚书：庚子、己卯、甲子、甲子，真此格也。经云：甲子逢合禄，终身须富足。诗曰：甲子日逢甲子时，遥合官禄贵无疑，丑绊子冲官煞显，福不为祥禄亦迟。又：子来遥巳细沉吟，甲子还将甲子寻，癸向巳中邀戊土，丙来酉上合辛金；暗忻申酉三六合，明怕庚辛二癸侵，丑午不逢高格论，登科及第宴琼林。

- 分字分词释义：

  - **甲子日再遇子时**：日干甲、日支子，时柱亦甲子，形成“日时同干支”的结构，子水为甲木之临官禄地。
  - **子遥巳禄**：子中癸水遥合巳中戊土；巳为甲之禄地，巳中藏丙戊，二者动则禄与官俱动，故名“遥巳禄”。
  - **癸合巳中戊土**：以癸水合戊土，构成财印关系，既为甲之财源，又为丙戊体系提供根基。
  - **巳酉丑三合会起官星局**：巳酉丑会金局，酉中辛金为甲官星，经由丙、戊之动而显现。
  - **畏庚辛申酉丑午**：庚辛辛金明露、申酉金局与丑午绊冲，皆可能破坏“遥”与“暗合”的微妙平衡。
  - **爵星**：这里以丙、戊为“爵星”，象征爵禄与官职之源。
  - **浊富**：富贵中带有辛劳、是非或世俗气较重，非清贵雅士之类。

- **规范化释义（primary_lang_explained）**：

  子遥巳禄格，是专为甲子日、甲子时而设的遥合官禄之格。甲日以辛金为官，辛藏于酉；而甲子日、甲子时的两个子水中，各伏癸水。癸水一方面为甲之印，一方面又能在地支结构中“遥合”巳中戊土：戊土为丙火之子，丙戊同居巳宫，丙为甲之爵星、戊为丙之爵星。戊土一动，丙火亦动；丙火动，则去酉中辛金而成官星克甲，甲日因此得官。整个路径是：
  
  子中癸 → 遥合巳中戊 → 动丙火 → 合酉中辛 → 辛为甲官。甲子日本身又以子为禄地，故名“子遥巳禄”。若再得巳、酉、丑三合金局配合，则官星之力更显。
  
  此格喜身旺、印旺，以承载官星之重：壬癸亥子月印绶旺，或卯寅木旺月身强，配合行官旺之运，往往主登科食禄、权贵之命。反之，若庚辛辛金明露、巳申酉过多、或丑午绊冲子水，则“遥合”的微妙结构被破坏，只能按普通正官格或平常财官格论，不可强扯为子遥巳禄。

- **完整对等诠释（secondary_lang_full）**：
  The "Zi Remote-Si Salary" pattern is a remote salary-and-official configuration designed specifically for Jia-Zi day born at Jia-Zi hour. Jia Wood takes Xin metal as its Proper Official, and Xin is hidden in You. In this layout there are two Zi branches, each containing Gui Water. Gui at once acts as Seal for Jia and as the agent that reaches across to combine with Wu earth in Si. Wu is the salary star for Bing fire, and Bing itself is the noble star for Jia; both share their salary seat in Si. When Gui in Zi combines with Wu in Si, it moves Wu and therefore stirs Bing; Bing then travels to You and combines with the hidden Xin metal there, which is Jia's official star. The official star thus does not stand close to the day-stem, but is raised from a distance through the chain Zi → Si → You, in the way that children and descendants extend a parent's rank and honour.
  
  This configuration therefore emphasises remoteness, concealment and subtle activation rather than loud, exposed officials. It works best when the two Zi branches are clean salary positions for Jia, Gui Water is well rooted and not excessively clashed, and the metal trine of Si–You–Chou can genuinely form so that Xin official has a stable body. The text especially favours months where Seals and the body are strong—Hai and Zi months for abundant Gui Water, or Yin and Mao months for vigorous Jia—so that the native can bear the responsibilities brought by this remote chain of officials. It warns against Geng and Xin metals shining too brightly on the stems, against an overabundance of Si, Shen and You that spoils the delicate balance, and against branches such as Chou and Wu that tangle or clash with Zi and cut off the remote link. When the structure holds and fortune cycles travel through territories that strengthen official and Seal, this pattern often produces examination success and office stipends with a somewhat worldly, "turbid wealth" flavour rather than pure, detached nobility.

- 核心要点：

  - 子遥巳禄以**甲子日、甲子时、癸合戊、丙合辛**这一套遥合路径为核心，是一种“暗中起官”的格局。
  - 身旺、印旺为前提，方能承受遥合而来的官禄；庚辛明露、巳申酉过多则易破格。
  - 巳酉丑三合若全，则格局更高，多主登科、权职之贵；若只见部分或受冲绊，则贵气减损。

- 详细解说：

  与卷六中其他禄马格类似，子遥巳禄强调“远处起用”的结构美学：官星辛金并非直接坐在日时旁边，而是藏于酉中，由丙戊体系牵动而显；巳中的丙戊又要靠子中癸水的遥合才能被激活。整个过程看似迂回，实则体现古人对气机路径的细致体察：
  
  1. 甲子日时，子水为甲木之禄；
  2. 子中癸水遥合巳中戊土，戊土为丙之子；
  3. 戊动丙亦动，丙火再去合酉中辛金；
  4. 辛金为甲之正官，于是官星由遥处而来。
  
  这种结构下，甲木并非直接“背负官星”，而是通过子、巳、酉等多重关系承接权力，因而古书用“如人有子继其后，传其家，以成父道之尊贵”来比附：子孙与后代（丙戊）承载父辈（甲）的官禄，使其家道久长。
  
  实务判断时，可以按以下次第：
  1. 确认日时确为甲子、甲子，且子中癸水位置得力；
  2. 察看巳酉丑局是否完整、有无午冲子、丑绊子等破格因素。
  若仅有甲子日，而时不在子，或局中巳酉丑不真成局，则不足以按子遥巳禄论贵，多只能视作官星根基较佳的正官格。

- **校勘与字词辨析（双语）**：
  - **中文**：
    - 原文中“甲子日再遇子时，畏庚辛申酉丑午”一句，概括了本格喜忌，特别点出庚辛、申酉与丑午对“遥合”结构的破坏，本稿据底本保留。
    - “爵星”一词在古命书用法不一，此处按上下文理解为“禄、官之星”，并在释义与白话中统一为“爵禄与官职之源”。
    - “浊富”原文用以形容富贵中带杂浊之气，本稿保留原语，在白话中释为“权贵浊富”。
  - **English**：
    - The phrase "Jia-Zi day meeting Zi hour again fears Geng, Xin, Shen, You, Chou, Wu" summarizes the likes and dislikes of this pattern; this edition preserves the original.
    - The term "Noble Star" (爵星) varies in usage across classical texts; here it is interpreted as "star of rank and office."
    - The phrase "turbid wealth" (浊富) describes nobility tinged with impurity; this edition keeps the original wording.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_005]` `[trigger: 子遥巳禄定义]` `[factor_trigger: zi_yao_si_lu_presence]` `[role: 主干]` 甲子日再遇子时，畏庚辛申酉丑午。 → 《三命通会》卷六#子遥巳禄
  - `[ns_smth_06_006]` `[trigger: 癸遥合戊]` `[factor_trigger: gui_yao_he_wu AND wu_dong_bing]` `[role: 主干依赖]` 二子中癸水能遥合巳中戊土，戊来合癸。 → 《三命通会》卷六#子遥巳禄
  - `[ns_smth_06_007]` `[trigger: 丙合辛官]` `[factor_trigger: bing_he_xin AND jia_de_guan]` `[role: 条件分支]` 戊动丙亦动，丙却与酉中辛相合来克甲木，甲日得官星。 → 《三命通会》卷六#子遥巳禄
  - `[ns_smth_06_008]` `[trigger: 终身富足]` `[factor_trigger: jia_zi_feng_he_lu]` `[role: 总结]` 甲子逢合禄，终身须富足。 → 《三命通会》卷六#子遥巳禄"""
    normalized_text_zh: str = """"""
    subject: str = "甲子日子时与遥合巳禄"
    factor_refs: list = ['engine_id', 'bazi_structure_zi_si_marker', 'bazi_structure_gui_wu_bing_xin', 'bazi_state_strength_1', 'bazi_state_factor_5', 'bazi_condition_si_you_chou_sanhe_condition', 'bazi_condition_geng_xin_si_shen_you', 'source_ref', 'rel_smth_06_004', 'ziyao_silu_presence', 'rel_smth_06_005', 'yaone_qiguan_score', 'rel_smth_06_006', 'gengxin_minglu_risk', 'evi_smth_06_004', 'gui_he_wu_lujing', 'rule_yaohe', 'evi_smth_06_005', 'yaone_qiguan_score', 'rule_qiguan', 'evi_smth_06_006', 'gengxin_minglu_risk', 'rule_minglu', 'map_smth_06_003', 'map_smth_06_004']
    
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
        l1_anchor="smth_v1.0.0_甲子日子时与遥合巳禄_001_L1",
    )
    version: str = "1.0.0"
