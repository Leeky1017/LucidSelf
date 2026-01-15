"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559392
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
    semantic_id="yhzp_v1.0.0_心镜歌_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 心镜歌(SemanticEntry):
    """
    - **原文（source_text）**：
  人生富贵皆前定，术士须详论；天上星辰有可加，此说更无差。
  时年月建逢命位，正是福元取。
  寿元合处是无真，此说不虚陈。
  官禄贵马见合刑，一举...
    """
    
    original_text: str = """- **原文（source_text）**：
  人生富贵皆前定，术士须详论；天上星辰有可加，此说更无差。
  时年月建逢命位，正是福元取。
  寿元合处是无真，此说不虚陈。
  官禄贵马见合刑，一举便成名。
  日逢贵地见禄马，壮岁登科甲。
  时日若逢禄马位，为官必清贵。
  五行时日无相杂，为官多显达。
  阳刃重重又见杀，大贵登科甲。
  若逢三奇连禄马，名誉满天下。
  日坐食支又合干，九卿三公看。
  甲子己巳有一说，天德得合诀。
  丙子癸巳与前观，官职三公卿。
  木若逢金主不伤，两府坐中堂。
  火若逢水主将权，为将镇戍边。
  金若逢火主大权，方面刺史官。
  水若逢土入金局，宜作侍从下。
  土若逢木为正禄，八座三台福。
  年得月禄不为喜，日贵取为主。
  生逢贵人值孤寡，决定为僧也。
  空亡官禄遇贵人，淡服作高僧。
  五行无气守孤寡，必定作行者。
  空亡刑害又逢囚，为僧及裹头。
  欲知人命主有权，食神旺必全。
  相冲阳刃再杀伤，必主上法场。
  的杀若逢盘足坐，恶鬼死刑狱。
  麦田相逢共帝星，徒流定分明。
  大害当权多夭折，少年逢刃杀。
  日逢官鬼见重刑，恶死甚分明。
  刃神劫煞两头居，早岁梦天衢。
  禄马俱逢行绝地，劳困难逃避。
  月若逢时与刑冲，根基定一空。
  时遇官星生旺位，子孙成行序。
  向禄临财官更期，贵显有家资。
  日月纯官无财位，反主无官贵。
  卯刑子位子刑卯，癸乙相刑贵。
  子来冲午，未刑戌，甲乙逢申显贵名。
  禄马俱绝又发财，人元克出来。
  得一分三缘何议，禄马飞天是。
  岁合时日分两头，切须仔细求；君子若逢主奏对，常人主灾晦。
  心怀悔退成何事，重阳剥官位。
  柱中有禄运逢财，金玉自天来。
  言前能说贵与贱，亦须看大运。
  大凡行运逢禄马，发迹为官也。
  天月二德为救解，百灾不为害。
  向禄临财甚希奇，贵显主官赀。
  命中禄马同贵人，福禄进珠珍。
  贵人君子坐刑煞，名成少年发。
  阴阳贵贱宜消息，熟晓于胸臆；日时身命许多般，一诀通变看。

- **分字分词释义**：
  - **人生富贵皆前定**：富贵贫贱皆命中注定。
  - **福元取**：福气之源，指月令或命宫。
  - **禄马见合刑一举成名**：禄神驿马遇合或刑，主科举成名。
  - **阳刃重重又见杀大贵**：羊刃叠见配七杀，主武职大贵。
  - **三奇连禄马名誉满天下**：乙丙丁三奇配禄马，主声名远播。
  - **五行无气守孤寡**：五行衰弱无气又逢孤寡，主为僧道行者。
  - **相冲阳刃再杀伤必主上法场**：阳刃逢冲又见七杀伤克，主刑死法场。
  - **飞天禄马**：禄马俱绝而暗冲取贵，特殊取官法。
  - **天月二德为救解**：天德月德可化解百灾。
  - **一诀通变看**：以一决通观全局，灵活变化。

- **规范化释义（primary_lang_explained）**：
  本篇《心镜歌》如心头明镜，照出命理吉凶的诸多法则：
  - **总论**：富贵前定，星辰（神煞）可作参考。重在"福元"（命宫/月令）与"寿元"（食神/日主）的合处。
  - **贵格**：
    - **禄马官贵**：日时逢禄马、三奇（财官印/乙丙丁等），主科甲清贵。
    - **杀刃相济**：阳刃重重见七杀，必主大贵（武职）。
    - **五行成器**：木逢金（栋梁）、火逢水（既济）、金逢火（锻炼），皆主掌握大权或位居高官。
  - **僧道孤贫**：贵人逢孤寡、官禄落空亡、五行无气，主为僧道。
  - **凶祸夭亡**：阳刃逢冲战、的杀（的煞）盘根、大耗重逢，主法场刑死或夭折。
  - **特殊格局**：
    - **子卯刑**：癸乙日主见子卯刑反而贵。
    - **飞天禄马**：禄马俱绝而发财，乃因暗冲暗合（如庚子冲午官）。
    - **岁运**：命好还需运扶，行运逢禄马财星，方能发迹。

- **完整对等诠释（secondary_lang_full）**：
  **Heart Mirror Ode**:
  - **Predestination**: Life's riches and nobility are predetermined; star spirits add details. Focus on "Fortune Element" (Month/Life Palace) and "Longevity Element" (Eating God).
  - **Noble Patterns**:
    - **Salary & Horse**: Day/Hour meeting Salary/Horse or "Three Wonders" leads to imperial success and high rank.
    - **Blade & Killing**: Multiple Yang Blades meeting Seven Killings indicates great nobility (often military).
    - **Elemental Interactions**: Wood meeting Metal (Carved into beams), Fire meeting Water (Balance/Authority), Metal meeting Fire (Forged) = High Authority/Ministry positions.
  - **Monastic/Solitary**: Noble meeting Solitary/Widowed stars, or Officer/Salary in Void = Monks or wandering ascetics.
  - **Disaster/Death**: Clashing Yang Blades, Solid "De" Killing, or Great Harm star implies execution, prison, or early death.
  - **Special Cases**:
    - **Zi-Mao Penalty**: For Gui/Yi days, this penalty can indicate nobility (unconventional).
    - **Flying Sky Salary Horse**: Gaining wealth when Salary/Horse are extinct, due to hidden clashing (extracting wealth/officer from opposite branch).
  - **Luck Cycles**: Must examine Great Luck. Meeting Salary/Horse in luck cycles triggers the rise to officialdom.

- **核心要点**：
  - **吉凶两途**：禄马贵人主贵，空亡孤寡主僧，刃杀刑冲主死
  - **五行成器**：金木水火土各得其制（如金得火炼）方成大器
  - **特殊刑冲**：子卯刑、飞天禄马等特殊取贵法
  - **运限参断**：命局为体，运程为用，金玉自天来需运扶

- **详细解说**：  《心镜歌》以心头明镜为喻，照出命理吉凶的诸多法则。开篇"人生富贵皆前定"定调命运之说，随后分述吉凶两途。**贵格**——"禄马见合刑，一举便成名"主科甲显贵；"阳刃重重又见杀"主武职大贵；"若逢三奇连禄马"主声名远播；"木若逢金"、"火若逢水"、"金若逢火"等五行成器之论，揭示制化成材的原理。**僧道**——"贵人值孤寡，决定为僧也"，"空亡官禄遇贵人，淡服作高僧"，揭示出家之命理标志。**凶死**——"相冲阳刃再杀伤，必主上法场"，阳刃逢冲战主刑死；"大害当权多夭折"主少年夭亡。**特殊取贵**——"禄马俱绝又发财"的飞天禄马格，以暗冲取官。末句"一诀通变看"点明论命需灵活变通，不可拘泥。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_367]` `[trigger: 富贵前定]` `[factor_trigger: rensheng_fugui AND qianding AND mingyun AND anchong_qugui AND angui]` `[role: 主干]` 人生富贵皆前定，术士须详论；命运之说总纲。 → 《渊海子平·心镜歌》
  - `[ns_yhzp_680]` `[trigger: 禄马成名]` `[factor_trigger: luma_jianhexing AND yiju_chengming AND kejia AND mingyu]` `[role: 条件分支]` 官禄贵马见合刑，一举便成名；禄马主科甲。 → 《渊海子平·心镜歌》
  - `[ns_yhzp_681]` `[trigger: 刃杀大贵]` `[factor_trigger: yangren_chongchong AND jiansha AND wugui AND anchong_qugui AND angui]` `[role: 条件分支]` 阳刃重重又见杀，大贵登科甲；刃杀相济主武贵。 → 《渊海子平·心镜歌》
  - `[ns_yhzp_682]` `[trigger: 五行成器]` `[factor_trigger: wuxing_chengqi AND zhihua_chengcai AND gui AND anchong_qugui AND angui AND chengqi AND elemental_forging]` `[role: 条件分支]` 木若逢金主不伤两府坐中堂；火若逢水主将权；金若逢火主大权。 → 《渊海子平·心镜歌》
  - `[ns_yhzp_683]` `[trigger: 孤寡为僧]` `[factor_trigger: guiren_zhigua AND kongwang_guanlu AND weiseng AND anchong_qugui AND angui AND huagai_kongwang AND jiujie]` `[role: 条件分支]` 生逢贵人值孤寡，决定为僧也；空亡官禄淡服作高僧。 → 《渊海子平·心镜歌》
  - `[ns_yhzp_684]` `[trigger: 刃杀法场]` `[factor_trigger: xiangchong_yangren AND shashang AND xingsi]` `[role: 例外处理]` 相冲阳刃再杀伤，必主上法场；阳刃冲战主刑死。 → 《渊海子平·心镜歌》
  - `[ns_yhzp_694]` `[trigger: 飞天禄马]` `[factor_trigger: feitian_luma AND anchong_quguan AND flying_sky_salary_horse]` `[role: 条件分支]` 禄马俱绝又发财，人元克出来；飞天禄马暗冲取官。 → 《渊海子平·心镜歌》
  - `[ns_yhzp_695]` `[trigger: 心镜歌纲领]` `[factor_trigger: xinjing_ge AND luma_gui AND kongwang_seng AND renjue_tongbian AND anchong_qugui AND angui]` `[role: 总结]` 心镜歌以禄马贵人为吉，空亡孤寡为僧，刃杀刑冲为死，一诀通变看。 → 《渊海子平·心镜歌》"""
    normalized_text_zh: str = """"""
    subject: str = "心镜歌"
    factor_refs: list = ['heart_mirror_ode', 'fortune_source', 'longevity_element', 'flying_sky_salary_horse', 'yang_blade_wields_killing']
    
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
        l1_anchor="yhzp_v1.0.0_心镜歌_001_L1",
    )
    version: str = "1.0.0"
