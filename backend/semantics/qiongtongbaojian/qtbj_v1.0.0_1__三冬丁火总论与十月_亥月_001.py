"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596934
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
    semantic_id="qtbj_v1.0.0_1__三冬丁火总论与十月_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三冬丁火总论与十月亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  三冬丁火微寒，耑用庚甲。甲乃庚之良友。凡用甲木，庚不可少，无庚无甲，何能引丁？难云木火通明，冬丁有甲，不怕水多金多。可称上格。甲庚两透，科甲分明。见己...
    """
    
    original_text: str = """- **原文（source_text）**：
  三冬丁火微寒，耑用庚甲。甲乃庚之良友。凡用甲木，庚不可少，无庚无甲，何能引丁？难云木火通明，冬丁有甲，不怕水多金多。可称上格。甲庚两透，科甲分明。见己则否。己多合甲，则为常人。
  或一丙夺丁，必赖支内水救。若有支金发水之源，官拜乌台有准。全无癸水制丙，无用之徒。或有金无水，贫寒之士。有水无金，又主清高。
  或时月二壬争合，取戊破之。有戊稍有富贵。无戊常人。设戊藏得所，不失衣衿。
  或二丙夺丁，得年干有癸，支下带合，金水得所，亦必显达，纳粟奏名，必验。

- **分字分词释义**：
  - **三冬丁火微寒**：冬季三月丁火微弱寒冷 / 亥子丑 / 极弱
  - **甲乃庚之良友**：甲木是庚金的好朋友 / 劈甲引丁 / 配合
  - **官拜乌台**：官职拜授御史台 / 监察官 / 清贵
  - **金发水之源**：金生发水的源头 / 财生官 / 吉象
  - **二壬争合**：两个壬水争合丁火 / 官杀混杂 / 凶象
  - **纳粟奏名**：捐纳粮食获得功名 / 捐官 / 异途

- **规范化释义（primary_lang_explained）**：
  冬季三个月的丁火，微寒，专用庚金和甲木。甲木是庚金的好朋友（劈甲引丁）。凡是用甲木，庚金不可少，没有庚金没有甲木，怎能引燃丁火？难说是“木火通明”。冬天的丁火有甲木（印），就不怕水多（杀）金多（财）。可以称为上格。甲木庚金两透，科甲功名分明。见到己土（合甲）就不行了。己土多合住甲木，就是常人。
  如果一个丙火夺丁火的光，必须依赖地支内的水来救应（制丙）。如果有地支的金发水源（金生水），官拜乌台（御史/监察官）有准。全无癸水制丙，是无用之徒。如果有金无水，贫寒之士。有水无金，又主清高。
  如果时柱月柱两个壬水争合丁火，取戊土破壬（伤官制杀）。有戊土稍有富贵。无戊土常人。假设戊土藏支得所，不失为秀才。
  如果两个丙火夺丁，得到年干有癸水（七杀制劫），地支带合（如戊癸合或支合），金水得地，也必定显达，纳粟奏名，一定灵验。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the Three Winter Months is slightly cold; exclusively use Geng and Jia. Jia is Geng's good friend. Whenever using Jia, Geng cannot be lacking; without Geng/Jia, how to ignite Ding? It's hard to call it "Wood Fire Bright". Winter Ding with Jia fears neither abundant Water nor Metal. It can be called a Superior Pattern. If Jia and Geng are both revealed, Civil Service is clear. Seeing Ji is not good; if Ji is abundant and combines with Jia, one is an ordinary person.
  If one Bing steals Ding's light, one must rely on Water in branches to save it. If there is Metal in branches generating the Water source, official rank in the Censorate (Wutai) is assured. Without any Gui to control Bing, one is useless. Having Metal without Water means poverty. Having Water without Metal implies aloofness.
  If two Rens in Month/Hour compete to combine, take Wu to break them. With Wu, slight wealth/nobility. Without Wu, ordinary. If Wu is hidden and placed well, one maintains a scholar's status.
  If two Bings steal Ding's light, obtaining Gui on Year Stem, with branches combining, and Metal/Water well-placed, one will certainly be prominent; gaining title via donation is verified.

- **核心要点**：
  - **劈甲引丁**：冬丁首重甲庚。
  - **有甲不畏**：有印生身，不畏水（杀）金（财）。
  - **丙夺丁光**：冬月亦忌丙，喜癸（杀）制劫。
  - **争合**：二壬争丁，喜戊制。

- **详细解说**：
  - 亥月丁火，官杀当令。
  - “甲乃庚之良友”：指庚金劈甲，配合有情。
  - “乌台”：御史台，指监察官。水主法，清冷无情，故金水旺多主法家/军警。
  - 己土合甲是冬丁的大忌，因贪合忘生，且己土卑湿不能生火。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_288]` `[trigger: 冬丁火]` `[factor_trigger: season_winter AND tiangan_ding AND tiangan_geng AND tiangan_jia AND winter_ding_cold]` `[role: 主干]` 三冬丁火微寒，耑用庚甲。甲乃庚之良友。凡用甲木，庚不可少，无庚无甲，何能引丁？ → 《穷通宝鉴·三冬丁火》#19.1
  - `[ns_qttbj_289]` `[trigger: 乌台]` `[factor_trigger: season_winter AND tiangan_ding AND dizhi_metal AND dizhi_water AND metal_generate_water]` `[role: 条件分支]` 若有支金发水之源，官拜乌台有准。 → 《穷通宝鉴·三冬丁火》#19.1
  - `[ns_qttbj_290]` `[trigger: 己合甲]` `[factor_trigger: season_winter AND tiangan_ding AND tiangan_ji_multiple AND tiangan_jia AND ji_combines_jia]` `[role: 例外处理]` 见己则否。己多合甲，则为常人。 → 《穷通宝鉴·三冬丁火》#19.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三冬丁火总论与十月（亥月）"
    factor_refs: list = ['wutai', 'donate_title']
    
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
        l1_anchor="qtbj_v1.0.0_1__三冬丁火总论与十月_亥月_001_L1",
    )
    version: str = "1.0.0"
