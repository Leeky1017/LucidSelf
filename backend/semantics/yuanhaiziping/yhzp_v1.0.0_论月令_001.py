"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558705
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
    semantic_id="yhzp_v1.0.0_论月令_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论月令(SemanticEntry):
    """
    - **原文（source_text）**：  
  假令年为本，带官星印绶，则早年有官出自祖宗。月为提纲，带官星印绶，则慷慨聪明、见识高人。时为辅佐，平生操履。若年月日有吉神，则时归生旺之处；若凶神...
    """
    
    original_text: str = """- **原文（source_text）**：  
  假令年为本，带官星印绶，则早年有官出自祖宗。月为提纲，带官星印绶，则慷慨聪明、见识高人。时为辅佐，平生操履。若年月日有吉神，则时归生旺之处；若凶神，则要归时制伏之乡。时上吉凶神，则年月日吉者生之，凶者制之。假令月令有用神，得父母力。年有用神，得祖宗力；时有用神，得子孙力；反此则不得力。

- **分字分词释义**：
  - **月令**：月支当令之气，又称"提纲"，为四柱中决定日主旺衰、格局高低的核心节点。
  - **提纲**：纲领、总领，喻月令对命局的统摄地位，如网之纲、衣之领。
  - **用神**：命局所需的调节平衡之神，为取用判格的关键。
  - **官星**：正官，克我而与我异性者，代表权力、地位。
  - **印绶**：正印，生我而与我异性者，代表学历、庇护、母亲。
  - **吉神**：财官印食等正向十神，利于命局平衡。
  - **凶神**：杀伤枭刃等偏激十神，需制化方可为用。
  - **生旺之处**：五行得生得旺的地支位置。
  - **制伏之乡**：五行受克受制的地支位置。

- **规范化释义（primary_lang_explained）**：月令为提纲，是四柱中最重要的节点。年柱带官印主祖上有功名；月柱带官印主本人聪慧见识高；时柱主晚年操守。吉神宜归生旺之地，凶神宜归制伏之乡。月令有用神得父母之力，年有用神得祖上之力，时有用神得子孙之力。

- **完整对等诠释（secondary_lang_full）**：The Month Command serves as the pivotal guideline, being the most crucial node among the Four Pillars. Year Pillar bearing Officer/Seal indicates ancestral merit; Month Pillar bearing Officer/Seal signifies one's intelligence and superior insight; Hour Pillar governs late-life conduct. Auspicious Gods should reside in prosperous positions; Inauspicious Gods should be placed where controlled. Use-God in Month gains parents' support, in Year gains ancestors' support, in Hour gains children's support.

- **核心要点**：
  - 月令为提纲，是四柱中最重要的判断核心
  - 年月时各有功能定位：年主祖宗、月主本人、时主子孙
  - 吉神宜归生旺之地，凶神宜归制伏之乡
  - 用神在不同柱位得不同人助力

- **详细解说**：  
  本条阐明月令在子平法中的核心地位。"月为提纲"是渊海子平最重要的论断之一，意即月支当令之气决定了命局的基本格局。年柱代表祖上根基，若带官印吉神，主祖上有功名荫庇；月柱代表本人禀赋，带官印主聪明见识过人；时柱代表晚年归宿与子孙缘分。对于吉凶神的安置，本条提出了"吉归生旺、凶归制伏"的原则：吉神应处于得生得旺的位置方能发挥正面作用，凶神应处于受克受制的位置才不为害。用神的力量来源也与柱位相关：月令有用神，得父母之力最强；年柱有用神，得祖宗之力；时柱有用神，得子孙之力。这一论述将四柱、十神、用神三者有机统一，是子平取用定格的基础理论。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_589]` `[trigger: 判断格局]` `[factor_trigger: month_command AND month_command_pattern]` `[role: 主干]` 月为提纲，是四柱中决定命局格局的核心节点。 → 《渊海子平·论月令》
  - `[ns_yhzp_590]` `[trigger: 年柱带官印]` `[factor_trigger: four_pillars_position AND ten_gods]` `[role: 条件分支]` 年带官星印绶，则早年有官出自祖宗。 → 《渊海子平·论月令》
  - `[ns_yhzp_591]` `[trigger: 月柱带官印]` `[factor_trigger: month_command AND ten_gods]` `[role: 条件分支]` 月带官星印绶，则慷慨聪明、见识高人。 → 《渊海子平·论月令》
  - `[ns_yhzp_592]` `[trigger: 吉神定位]` `[factor_trigger: ten_gods AND jixiongshen_dingwei]` `[role: 主干依赖]` 吉神宜归生旺之处，方能发挥正面力量。 → 《渊海子平·论月令》
  - `[ns_yhzp_593]` `[trigger: 凶神定位]` `[factor_trigger: ten_gods]` `[role: 主干依赖]` 凶神宜归制伏之乡，方不为害。 → 《渊海子平·论月令》
  - `[ns_yhzp_594]` `[trigger: 月令用神]` `[factor_trigger: month_command]` `[role: 条件分支]` 月令有用神，得父母之力。 → 《渊海子平·论月令》
  - `[ns_yhzp_595]` `[trigger: 年柱用神]` `[factor_trigger: four_pillars_position]` `[role: 条件分支]` 年有用神，得祖宗之力。 → 《渊海子平·论月令》
  - `[ns_yhzp_596]` `[trigger: 时柱用神]` `[factor_trigger: four_pillars_position AND late_prosperity]` `[role: 条件分支]` 时有用神，得子孙之力。 → 《渊海子平·论月令》
  - `[ns_yhzp_397]` `[trigger: 官运]` `[factor_trigger: officer_luck]` `[role: 条件分支]` 身旺行官运主升迁。 → 《渊海子平·论月令》
  - `[ns_yhzp_398]` `[trigger: 官格]` `[factor_trigger: officer_pattern]` `[role: 条件分支]` 正官格贵显有权。 → 《渊海子平·论月令》
  - `[ns_yhzp_399]` `[trigger: 官禄]` `[factor_trigger: officer_salary]` `[role: 结果]` 官星有气主官禄。 → 《渊海子平·论月令》
  - `[ns_yhzp_400]` `[trigger: 官星当令]` `[factor_trigger: officer_season]` `[role: 条件分支]` 官星当令主贵显。 → 《渊海子平·论月令》
  - `[ns_yhzp_401]` `[trigger: 枭印]` `[factor_trigger: owl_seal]` `[role: 条件分支]` 偏印为枭，枭神夺食主凶。 → 《渊海子平·论月令》
  - `[ns_yhzp_402]` `[trigger: 桃花]` `[factor_trigger: peach_blossom]` `[role: 条件分支]` 桃花主异性缘，多桃花主风流。 → 《渊海子平·论月令》
  - `[ns_yhzp_403]` `[trigger: 桃花煞]` `[factor_trigger: peach_flower]` `[role: 条件分支]` 桃花煞带刑冲主感情波折。 → 《渊海子平·论月令》
  - `[ns_yhzp_404]` `[trigger: 祖上]` `[factor_trigger: predecessors]` `[role: 主干]` 年柱代表祖上根基。 → 《渊海子平·论月令》
  - `[ns_yhzp_405]` `[trigger: 淫乱]` `[factor_trigger: promiscuity]` `[role: 结果]` 多合带桃花主淫乱。 → 《渊海子平·论月令》
  - `[ns_yhzp_406]` `[trigger: 本气官]` `[factor_trigger: proper_qi_officer]` `[role: 条件分支]` 本气正官为真官，主正途显达。 → 《渊海子平·论月令》
  - `[ns_yhzp_407]` `[trigger: 正格]` `[factor_trigger: proper_structure]` `[role: 条件分支]` 正格者八正格也，取月令为用。 → 《渊海子平·论月令》
  - `[ns_yhzp_408]` `[trigger: 旺]` `[factor_trigger: prosperity]` `[role: 条件分支]` 五行当令为旺，旺则有力。 → 《渊海子平·论月令》
  - `[ns_yhzp_409]` `[trigger: 纯格]` `[factor_trigger: pure_pattern]` `[role: 条件分支]` 纯格无破主贵，杂格多破主贱。 → 《渊海子平·论月令》
  - `[ns_yhzp_410]` `[trigger: 去]` `[factor_trigger: removal]` `[role: 条件分支]` 去者制去病神也，去病则吉。 → 《渊海子平·论月令》
  - `[ns_yhzp_411]` `[trigger: 根气]` `[factor_trigger: root_qi]` `[role: 条件分支]` 根气者地支藏干也，有根则力强。 → 《渊海子平·论月令》
  - `[ns_yhzp_412]` `[trigger: 无根]` `[factor_trigger: rootless]` `[role: 条件分支]` 无根者虚浮无力。 → 《渊海子平·论月令》
  - `[ns_yhzp_413]` `[trigger: 禄]` `[factor_trigger: salary]` `[role: 条件分支]` 禄者临官也，主食禄。 → 《渊海子平·论月令》
  - `[ns_yhzp_414]` `[trigger: 禄马]` `[factor_trigger: salary_horse]` `[role: 条件分支]` 禄马交驰主贵显。 → 《渊海子平·论月令》
  - `[ns_yhzp_415]` `[trigger: 印]` `[factor_trigger: seal]` `[role: 条件分支]` 印绶生身主学问、权柄。 → 《渊海子平·论月令》
  - `[ns_yhzp_416]` `[trigger: 印旺]` `[factor_trigger: seal_strong]` `[role: 条件分支]` 印旺有力主学历高。 → 《渊海子平·论月令》
  - `[ns_yhzp_417]` `[trigger: 己]` `[factor_trigger: self]` `[role: 主干]` 日主为己，代表自身。 → 《渊海子平·论月令》
  - `[ns_yhzp_418]` `[trigger: 身旺运]` `[factor_trigger: self_strengthening_luck]` `[role: 条件分支]` 身弱行印比运为身旺运。 → 《渊海子平·论月令》
  - `[ns_yhzp_419]` `[trigger: 身旺]` `[factor_trigger: self_strong]` `[role: 条件分支]` 身旺可任财官。 → 《渊海子平·论月令》
  - `[ns_yhzp_420]` `[trigger: 身弱]` `[factor_trigger: self_weak]` `[role: 条件分支]` 身弱不胜财官。 → 《渊海子平·论月令》"""
    normalized_text_zh: str = """"""
    subject: str = "论月令"
    factor_refs: list = ['month_command', 'use_god']
    
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
        l1_anchor="yhzp_v1.0.0_论月令_001_L1",
    )
    version: str = "1.0.0"
