"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458321
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
    semantic_id="smth_v1.0.0_时上偏官与晚年权贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 时上偏官与晚年权贵(SemanticEntry):
    """
    - **原文（source_text）**：
  《喜忌篇》云：若乃时逢七煞，见之未必为凶，月制干强，其煞反为权印。经云：时上偏官身要强，阳刃冲刑煞敢当，制多要行煞旺运，煞多制少必为殃。盖时上偏官，要...
    """
    
    original_text: str = """- **原文（source_text）**：
  《喜忌篇》云：若乃时逢七煞，见之未必为凶，月制干强，其煞反为权印。经云：时上偏官身要强，阳刃冲刑煞敢当，制多要行煞旺运，煞多制少必为殃。盖时上偏官，要干上透出，只一位为妙。年月日重见，反主辛苦劳碌。若身旺，煞制太过，喜行煞旺运，或三合煞运，如无制伏，要行制伏运方发。但忌身弱，纵得运扶持发福，运过依旧不济。
  
  又曰：时上偏官，不怕冲刃，为人性重刚直不屈。煞无根，要坐旺宫；有根不宜（财有，煞之根）。若一位七煞，却有两三重制伏，纵文过李、杜，终难显达。《独步》云：时煞无根，煞旺最贵；时煞多根，煞旺不和。《惊神赋》云：时上偏官，有制，晚子英奇。古歌云：时上偏官喜刃冲，身强制伏禄丰隆，正官若也来相混，身弱财多主困穷。又：时上偏官一位强，日辰自旺喜非常，有财有印多财禄，定是天生作栋梁。又：时逢七煞是偏官，有制身强好命者，制过喜行煞旺运，三合得地发何难。又：时逢七煞本无儿，此理人间仔细推，底月时中如有制，定知有子贵而迟。

- 分字分词释义：
  - **时上偏官**：七煞落在时柱天干（且多与日柱形成偏官关系），主晚年境遇、子息与后运中的权煞之象。
  - **月制干强，其煞反为权印**：若月令能制时煞，而日主又健旺，则七煞反成权力与印信的来源。
  - **只一位为妙**：时上偏官以单一一位为贵，年月日再重见则成"煞多"，多主辛劳与是非。
  - **煞无根要坐旺宫，有根不宜**：时煞最好无根而坐旺宫，象征权力来源于职位而非私人纠葛；若煞根深，则煞势难以调和。
  - **晚子英奇**：指晚年及子女方面多有英奇之象，常见于有制之时煞格局。

- **规范化释义（primary_lang_explained）**：
  本节专论"时上一位偏官"。与一般七煞不同，时上偏官多主中晚年及子女层面的权煞之象。《喜忌篇》说：时逢七煞未必为凶，只要月令能够制伏煞气、日主本身又强，则七煞反而可以成为权印，即权力与合法性的来源。理想状态是：时上只一位偏官，日主健旺，有阳刃冲煞、印绶化煞等多重制化，而大运又行煞旺之地，则多主中晚年发迹、掌权，或子女成才。
  
  反之，若身弱而煞重，或时上偏官多根，年月日又重见七煞，则多主辛苦、官非甚至困穷。文中引用《独步》《惊神赋》与多首古歌，反复强调：时上偏官最怕"煞多制少"与"身弱财多"两种情况，而最喜"一位七煞、两三重制伏"这一种：煞有其位而不至泛滥，制有其力而不过其度，于是既有刚强不屈之性，又能在适当时机承载权力。

- **完整对等诠释（secondary_lang_full）**：
  The Joys-and-Taboos chapter says that when the hour pillar holds Seven Killing it is not necessarily inauspicious: if the month can restrain it and the day-master is strong, the Killing can instead become a source of authority and legitimacy. Another verse adds that with a partial official on the hour, the body must be strong, able to face clashes and punishments with a Yang Blade, and that when the controlling stars are many and strong it is best to travel through fortunes where Killing is prosperous; if Killing is many and the control is weak, disaster is almost certain.
  As a rule, an hour-top partial official should appear clearly on the stem and be limited to a single instance; if further officials and Killings repeat in the year, month or day pillars, the result is toil and trouble rather than nobility. When the day-master is strong and the controlling structure somewhat heavy, one actually welcomes fortune cycles that strengthen Killing or gather it through three-harmony formations, so that the controlled Killing can fully function as power. When there is no control at all, later fortunes must first provide the means to restrain the Killing before prosperity can arise. This is the logic behind the so‑called 'one strong Killing on the hour' pattern that brings late-life authority and talented children when handled well.


- 核心要点：
  - 时上偏官主要反映**中晚年与子女层面的权煞结构**，不必一见七煞即断为凶。
  - 贵在"一位七煞、多重制伏"：煞有其位、有其用，而不至于泛滥；制多则煞化为权，制少则煞成祸。
  - 需日主身强，并有月令或他柱印、刃等星制化；否则纵有一时运扶，运过仍旧不济。

- 详细解说：
  时柱为一命之归宿，既主晚年境遇，又主子嗣与后代。七煞若落于时柱，一方面使命主性格多刚直不屈、敢于担当；另一方面也意味着人生后程与子嗣发展，很可能与权力、竞争乃至风险相连。本节强调"时上偏官身要强"，说明只适用于能够承受煞气的人：若日主无根，便如薄体负重，难免折损。
  
  文中"时煞无根，煞旺最贵；时煞多根，煞旺不和"一句，点出了时煞格的微妙之处：时上七煞最好不要在地支多处扎根，而是以职务、位置之"旺"来体现其力量，这样煞气更多表现为职责与权力，而非私人恩怨。再配合"喜刃冲"、"有制"等条件，可以形成一种既有锋芒又有节制的权煞格局，常见于执法、军警、纪检等领域的中高层人物。

- 校勘与字词辨析：
  - 文中括号"（财有，煞之根）"说明财星也是七煞的根源之一，故"有根不宜"意在警惕财煞勾连过深。
  - 多条古歌与引文（如"时上偏官喜刃冲"、"时逢七煞本无儿"）在后世命书中多有引用，现代整理时保留原句，并在白话与释义中加以归纳说明。
  - **English**：
    - Summarized and explained in vernacular and glossary.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_052]` `[trigger: 时上偏官]` `[factor_trigger: shishang_yiwei_gui_presence AND shen_qiang]` `[role: 主干]` 时上偏官身要强，阳刃冲刑煞敢当。 → 《三命通会》卷五#时上偏官
  - `[ns_smth_05_053]` `[trigger: 只一位为妙]` `[factor_trigger: sha_zhi_yi_wei AND gan_shang_tou_chu]` `[role: 主干依赖]` 时上偏官，要干上透出，只一位为妙。 → 《三命通会》卷五#时上偏官
  - `[ns_smth_05_054]` `[trigger: 煞无根贵]` `[factor_trigger: sha_wu_gen AND zuo_wang_gong]` `[role: 条件分支]` 时煞无根，煞旺最贵；时煞多根，煞旺不和。 → 《三命通会》卷五#时上偏官
  - `[ns_smth_05_055]` `[trigger: 晚子英奇]` `[factor_trigger: you_zhi AND wan_zi_yingqi]` `[role: 总结]` 时上偏官，有制，晚子英奇。 → 《三命通会》卷五#时上偏官"""
    normalized_text_zh: str = """"""
    subject: str = "时上偏官与晚年权贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'shishang_yiwei_gui_presence', 'bazi_semantic', 'shisha_genji_config', 'bazi_semantic', 'sha_zhi_pingheng_score', 'bazi_semantic', 'wannian_quangui_score', 'bazi_semantic', 'rizhu_chengsha_condition', 'bazi_semantic', 'zisi_yingqi_flag', 'bazi_semantic', 'source_ref', 'rel_smth_05_040', 'shishang_yiwei_gui_presence', 'rel_smth_05_041', 'sha_zhi_pingheng_score', 'rel_smth_05_042', 'wannian_quangui_score', 'evi_smth_05_040', 'shishang_yiwei_gui_presence', 'rule_yiwei', 'evi_smth_05_041', 'rizhu_chengsha_condition', 'rule_shenqiang', 'evi_smth_05_042', 'zisi_yingqi_flag', 'rule_yingqi', 'map_smth_05_027', 'map_smth_05_028']
    
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
        l1_anchor="smth_v1.0.0_时上偏官与晚年权贵_001_L1",
    )
    version: str = "1.0.0"
