"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578282
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
    semantic_id="qtbj_v1.0.0_2__二月庚金_卯月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2二月庚金卯月(SemanticEntry):
    """
    - **原文（source_text）**：
  二月庚金，柱中自然有乙，当令之乙，见庚必输情于乙，此金有暗强之势，如秋金一理，故二月庚金，专用丁火，借甲引丁，借庚噼甲。无丁用丙者，富贵多出于勉强。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  二月庚金，柱中自然有乙，当令之乙，见庚必输情于乙，此金有暗强之势，如秋金一理，故二月庚金，专用丁火，借甲引丁，借庚噼甲。无丁用丙者，富贵多出于勉强。
  或丁在干，甲透引丁，支下再见一庚制甲，配得中和，必然大贵。如不见庚合者，虽丁甲两透，亦属平人。
  春丁不旺不衰，故用甲为佐丁之物，甲若无庚噼，则不能引丁，乙木虽多，又忌湿乙伤丁，难为丁母，故有丁甲无庚者，常人。有丁庚、甲不出干者、常人。或丁透无庚甲者，可许贡监。无丁有丙者，异路功名。
  或一片甲乙，忌庚出干破才，乃从才格，反主富贵。若见一比，又主孤贫。
  死金嫌盖顶之泥，重见戊土，如人压伏之象，须甲透为妙。

- **分字分词释义**：
  - **二月**：卯月 / 农历二月 / 乙木当令
  - **输情于乙**：庚金与乙木合 / 乙庚合 / 贪合忘克
  - **暗强之势**：隐藏的刚强 / 因合而不弱 / 金性暗旺
  - **借甲引丁**：用甲木生丁火 / 财生官 / 引火之法
  - **借庚噼甲**：用庚金劈甲木 / 比劫制财 / 引火之法
  - **中和**：平衡调和 / 配置得当 / 格局理想
  - **湿乙**：湿润的乙木 / 卯月当令 / 难生火
  - **从才格**：从财格 / 弃命从财 / 木多金弱
  - **盖顶之泥**：土盖住顶 / 戊土压金 / 忌神
  - **压伏**：压制屈服 / 金被土埋 / 凶象

- **规范化释义（primary_lang_explained）**：
  二月（卯月）的庚金，柱中自然有乙木（当令），见庚金必定输送情意给乙木（乙庚合），这庚金有暗强的气势（因贪合而不弱？或指从财？原文“如秋金一理”疑指金木相战或金能克木），所以二月庚金，专用丁火（官/炼金），借甲木引丁（生火），借庚金劈甲（引丁）。没有丁火用丙火者，富贵多出于勉强。
  如果丁火在天干，甲木透出引丁，地支再见一个庚金制甲（劈甲），配合得中和，必然大贵。如果不见庚金（制甲），虽然丁甲两透，也属平人（甲无劈不灵）。
  春天的丁火不旺不衰，所以用甲木作为辅佐丁火之物，甲木如果没有庚金劈，就不能引燃丁火，乙木虽然多，又忌讳湿乙伤丁，难以为丁火之母，所以有丁甲无庚者，常人。有丁庚、甲不出干者，常人。或者丁透无庚甲者，可许贡监。无丁有丙者，异路功名。
  如果一片甲乙木（财），忌讳庚金出干破财，这是“从财格”，反主富贵。如果见到一个比劫，又主孤贫。
  死金（卯月庚金）嫌盖顶之泥（戊土），重见戊土，像人被压伏的象，必须甲木透出（疏土）才妙。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 2nd Month (Rabbit Month): Naturally has Yi in pillars; Yi commands. Meeting Geng, it conveys affection (Yi-Geng combine). This Metal has "Dark Strength" (hidden power via combination or control), similar to Autumn Metal logic. Thus 2nd Month Geng exclusively uses Ding Fire; borrow Jia to ignite Ding, borrow Geng to split Jia. Using Bing without Ding implies forced wealth/nobility.
  If Ding is on stem, Jia reveals to ignite it, and branches see another Geng to control Jia, balanced and harmonized, it is surely great nobility. If Geng is not seen (to split), even with Ding/Jia revealed, one is ordinary.
  Spring Ding is neither prosperous nor weak; thus use Jia to assist. If Jia lacks Geng to split, it cannot ignite Ding. Though Yi is abundant, Wet Yi hurts Ding and cannot be Ding's mother. So with Ding/Jia but no Geng, ordinary. With Ding/Geng but no Jia revealed, ordinary. With Ding revealed but no Geng/Jia, a student. Without Ding but with Bing, alternative fame.
  If there is a slice of Jia/Yi, dread Geng revealing to break Wealth; it is "Follow Wealth", implying wealth/nobility. If one Parallel appears, it implies loneliness/poverty.
  Dead Metal dislikes "Mud covering the top"; seeing heavy Wu Earth is like a person being suppressed; Jia revealing is wondrous.

- **核心要点**：
  - **首要用神**：丁火（炼金）。卯月乙庚合，金有情，喜火炼。
  - **配合**：甲（引丁）、庚（劈甲）。丁甲庚配合，大贵。
  - **从财**：木多无金（比劫），从财贵。
  - **埋金**：忌土多，喜甲疏。

- **详细解说**：
  - 卯月庚金胎地。
  - "乙庚合"是关键。若合化金（需土金运），则身强；若合而不化（木旺），则贪合忘克。
  - 《穷通》主张用丁炼金，认为乙庚合有"暗强"之势，故需火炼成器。
  - 甲木在此处的作用是生丁（官印），庚金劈甲是为了引火，形成循环。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_326]` `[trigger: 庚生卯月]` `[factor_trigger: month_mao AND tiangan_geng AND yi_geng_combine AND dark_strength]` `[role: 主干]` 二月庚金，柱中自然有乙，见庚必输情于乙，此金有暗强之势。 → 《穷通宝鉴·三春庚金》#30.2
  - `[ns_qttbj_327]` `[trigger: 丁甲庚配合]` `[factor_trigger: month_mao AND tiangan_geng AND ding_revealed AND jia_revealed AND geng_in_branch]` `[role: 条件分支]` 或丁在干，甲透引丁，支下再见一庚制甲，配得中和，必然大贵。 → 《穷通宝鉴·三春庚金》#30.2
  - `[ns_qttbj_328]` `[trigger: 从财格]` `[factor_trigger: month_mao AND tiangan_geng AND wood_excessive AND NOT shishen_parallel AND pattern_follow_wealth]` `[role: 条件分支]` 或一片甲乙，忌庚出干破才，乃从才格，反主富贵。 → 《穷通宝鉴·三春庚金》#30.2
  - `[ns_qttbj_329]` `[trigger: 土重埋金]` `[factor_trigger: month_mao AND tiangan_geng AND earth_excessive AND tiangan_jia]` `[role: 例外处理]` 死金嫌盖顶之泥，重见戊土，如人压伏之象，须甲透为妙。 → 《穷通宝鉴·三春庚金》#30.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 二月庚金（卯月）"
    factor_refs: list = ['dark_strength', 'mud_covering_top']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__二月庚金_卯月_001_L1",
    )
    version: str = "1.0.0"
