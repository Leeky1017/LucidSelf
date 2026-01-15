"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559520
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
    semantic_id="yhzp_v1.0.0_渊源集说_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 渊源集说(SemanticEntry):
    """
    - **原文（source_text）**：  
  渊源集说。最贵者，官星为命，时得偏正财为福。最凶者，七杀临身，逢天月二德为祥。官星若遇劫财，虽官无贵。七杀如逢资助，其杀愈重。三合六合，运至逢而必...
    """
    
    original_text: str = """- **原文（source_text）**：  
  渊源集说。最贵者，官星为命，时得偏正财为福。最凶者，七杀临身，逢天月二德为祥。官星若遇劫财，虽官无贵。七杀如逢资助，其杀愈重。三合六合，运至逢而必荣。七官八官，月逢官而为喜。四合四刑，合刑当为偏正。七冲七击，冲击喜得会藏。夹贵夹丘为暗会。财库官库要正冲。官星在生旺之方，逢则何须发见。印绶临孟仲之下，见而不见。露形印绶，得劫财为贵。财源喜伤（伤官），贵为奇。伤官要见印绶，贵不可言。归禄若见子孙（食神），禄无限妙。年月立有阴阳阳刃，刑罚重犯。官杀混逢天月德，寿位高迁。飞刃伏刃，会刃多凶。伤官见官，剥官见祸。阳刃若逢印绶，纵贵，有病疾在身。七杀并制，逢官为祸，而寿元不长。三偏三正，贵居一品之尊。四柱四合，福坐众人之上。杀化为印，早擢登科。财旺生官，少年承业。官杀同来，要知扶官扶杀。偏正会合，须知合正合偏。福禄若逢阳刃，世事不明。金神运入水乡，身衰夭折。暗中藏杀，须凭月下刑神。见处无财，必受空中祸患。阳刃兼会七杀，千里徒流。用财若遇劫夺，一生贫困。人生前定，穷富已明，如要识其消长，亦多究其始终；或有前贫后富、或有骤发卒倾、或有白屋之公卿、或有朱门之饿殍、或一生长乐、或一生失所，当视流运之源，要察行年之位。身弱徒然入格，纵发早亡。福转若遇休囚，卒发倾夭。是以，用神不可妄求，形踪自然发见，有福必当用彼，无时必是用身，祸患在于五行，福崇在于运气；福源人所同具，如或伤终困此中。消息阴阳，在我通明理智，荣辱两端，媸妍一断。自古相传，非贤勿授。


- **分字分词释义**：
  - **最贵者官星为命时得偏正财为福**：最贵为官星为命，时柱得财为福。
  - **最凶者七杀临身逢天月二德为祥**：最凶为七杀临身，但逢天月德可转祸为祥。
  - **官星若遇劫财虽官无贵**：官星遇劫财，虽有官亦无贵。
  - **伤官要见印绶贵不可言**：伤官遇印绶，贵不可言。
  - **三偏三正贵居一品之尊**：三偏财或三正官，可至一品高官。
  - **杀化为印早擢登科**：七杀化为印绶，早登科第。
  - **阳刃兼会七杀千里徒流**：阳刃与七杀同会，主千里流放。
  - **用神不可妄求有福用彼无时用身**：用神不可妄求，有福用喜神无福用身。
  - **消息阴阳在我通明理智**：阴阳消息在于我之通明理智。
  - **自古相传非贤勿授**：自古相传，非贤人不授。
- **规范化释义（primary_lang_explained）**：  
  《渊源集说》以警句式汇总财官印杀阳刃天月德伤官劫财等核心神煞的渊源与吉凶要点，是对前文理论的"总结与速查手册"。**官杀与天月德**：最贵为官星为命配偏正财，最凶为七杀临身但逢天月二德可转祸为祥；官星遇劫财虽有官亦无贵，七杀逢资助其杀愈重。**印绶伤官与用神**：露形印绶得劫财反为贵，财源喜伤官为奇，伤官要见印绶贵不可言，归禄若见食神禄无限妙；强调十神组合搭配优于单看一星。**阳刃与刑罚**：年月阴阳阳刃重立多犯刑罚，飞刃伏刃会刃多凶，阳刃兼七杀千里徒流，阳刃逢印绶纵贵亦有病疾，阳刃逢财世事不明。**官杀混配与偏正**：官杀同来要知扶官扶杀，偏正会合须知合正合偏；三偏三正贵居一品，四柱四合福坐众人之上。**运势与用神**：人生穷富前定，消长与流运行年关联；身弱徒然入格纵发早亡；用神不可妄求，有福用彼无时用身；祸患在五行福崇在运气，最终归结为"消息阴阳在我通明理智"。

- **完整对等诠释（secondary_lang_full）**：  
  **Collected Sayings from the Sources**: A compendium of judgment rules for core stars (Officer/Killing/Seal/Wealth/Injury Officer/Rob Wealth/Yang Blade) in concise aphoristic form. **Officer and Killing with Virtues**: The highest nobility is when Officer Star serves as the natal core and the Hour obtains Indirect or Proper Wealth for blessing. The worst danger is when Seven Killings overpower the Body, but meeting Heaven and Moon Two Virtues brings auspiciousness. If Officer Star meets Rob Wealth, even with office there is no nobility. If Seven Killings meet assistance (resources), the Killing becomes even heavier. **Seal and Injury Officer**: Exposed Seal meeting Rob Wealth paradoxically brings nobility; Wealth source favoring Injury Officer is exceptionally auspicious; Injury Officer must meet Seal for true greatness which is beyond words; Returning Salary (Gui Lu) meeting Food God forms infinite blessing. **Yang Blade and Punishment**: Multiple Yang Blades in Year and Month indicate repeated legal punishments; Flying Blade, Hidden Blade, and Combined Blade bring much danger; Yang Blade combined with Seven Killings indicates exile for thousands of miles; Yang Blade meeting Seal, even if noble, brings illness to the body. **Officer–Killing Balance**: When Officer and Killing appear together, one must know whether to bolster Officer or Killing; Three Indirect or Three Proper configurations place one in the supreme rank of first grade; Four Pillars with Four Combinations place blessings above all people. **Timing and Use God**: Human fate's poverty and wealth are predetermined, but to know their waxing and waning, one must investigate the beginning and end; weak body forced into good pattern still results in early death; do not arbitrarily chase Use Gods—if blessing exists use "that", if not use "Body"; disasters and blessings reside in Five Elements; mastery requires deep discernment of Yin-Yang and luck cycles.

- **核心要点**：  
  - 以警句汇总财官印杀阳刃天月德等主要神煞的取舍与吉凶规律  
  - 强调组合优于单星：伤官见印劫财得印杀化为印财旺生官等  
  - 阳刃多与刑狱病疾流放相关，需严格注意其配置  
  - 用神不可妄求，本质是"有福用彼无时用身"，运气与五行决定祸福

- **详细解说**：  《渊源集说》以警句式汇总核心神煞的吉凶要点。**官杀天月德**——"最贵者官星为命，时得偏正财为福"；"最凶者七杀临身，逢天月二德为祥"揭示官杀与德星的配合。**印绶伤官**——"伤官要见印绶，贵不可言"；"归禄若见食神，禄无限妙"强调十神组合优于单星。**阳刃刑罚**——"年月立有阴阳阳刃，刑罚重犯"；"阳刃兼会七杀，千里徒流"揭示阳刃与刑狱的关联。**官杀偏正**——"三偏三正，贵居一品之尊"；"四柱四合，福坐众人之上"阐述特殊配置的贵格。**用神选择**——"用神不可妄求，有福必当用彼，无时必是用身"揭示用神选择之法。末句"消息阴阳，在我通明理智，自古相传，非贤勿授"点明传承之慎重。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_462]` `[trigger: 官杀天月德]` `[factor_trigger: zuigui_guanxing_weiming AND qisha_feng_tianyue_erde AND anchong_qugui AND angui]` `[role: 主干]` 最贵者官星为命时得偏正财为福；最凶者七杀临身逢天月二德为祥。 → 《渊海子平·渊源集说》
  - `[ns_yhzp_463]` `[trigger: 伤官见印]` `[factor_trigger: shangguan_jian_yinshou_gui AND guilu_jian_shishen_miao AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 伤官要见印绶贵不可言；归禄若见食神禄无限妙。 → 《渊海子平·渊源集说》
  - `[ns_yhzp_464]` `[trigger: 阳刃刑狱]` `[factor_trigger: yangren_xingfa_zhongfan AND yangren_hui_qisha_tuliu]` `[role: 条件分支]` 年月立有阴阳阳刃刑罚重犯；阳刃兼会七杀千里徒流。 → 《渊海子平·渊源集说》
  - `[ns_yhzp_465]` `[trigger: 三偏三正]` `[factor_trigger: sanpian_sanzheng_gui_yipin AND sizhu_sihe_fu AND anchong_qugui AND angui]` `[role: 条件分支]` 三偏三正贵居一品之尊；四柱四合福坐众人之上。 → 《渊海子平·渊源集说》
  - `[ns_yhzp_466]` `[trigger: 杀化为印]` `[factor_trigger: sha_huawei_yin_dengke AND caiwang_shengguan_chengye AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 杀化为印早擢登科；财旺生官少年承业。 → 《渊海子平·渊源集说》
  - `[ns_yhzp_467]` `[trigger: 用神选择]` `[factor_trigger: yongshen_buke_wangqiu AND youfu_yongbi AND wushi_yongshen]` `[role: 条件分支]` 用神不可妄求；有福用彼无时用身；祸患在于五行。 → 《渊海子平·渊源集说》
  - `[ns_yhzp_468]` `[trigger: 消息阴阳]` `[factor_trigger: xiaoxi_yinyang AND tongming_lizhi AND feixian_wushou AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 例外处理]` 消息阴阳在我通明理智；自古相传非贤勿授。 → 《渊海子平·渊源集说》
  - `[ns_yhzp_469]` `[trigger: 渊源集说纲领]` `[factor_trigger: yuanyuan_jishuo AND guansha_tianyue AND yinshou_shangguan AND yongshen_xuanze AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 总结]` 渊源集说以官杀天月德、印绶伤官、阳刃刑罚、用神选择为核心，汇总神煞要点。 → 《渊海子平·渊源集说》"""
    normalized_text_zh: str = """"""
    subject: str = "渊源集说"
    factor_refs: list = ['collected_sayings', 'heaven_moon_virtues', 'killing_transforms_seal', 'three_indirect_direct', 'use_god_selection']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_渊源集说_001_L1",
    )
    version: str = "1.0.0"
