"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619883
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
    semantic_id="qtbj_v1.0.0_2__五六月甲木_午未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2五六月甲木午未月(SemanticEntry):
    """
    - **原文（source_text）**：
  五六月甲木，木性虚焦，一理共推。五月先癸后丁，庚金次之。六月三伏生寒，丁火退气。先丁后庚，无癸亦可。或五月乏癸，用丁亦可，要运行北地为隹。
  总之五...
    """
    
    original_text: str = """- **原文（source_text）**：
  五六月甲木，木性虚焦，一理共推。五月先癸后丁，庚金次之。六月三伏生寒，丁火退气。先丁后庚，无癸亦可。或五月乏癸，用丁亦可，要运行北地为隹。
  总之五六月用丁火，虽运行北地，不致于死。却不利运行火地，号曰木化成灰必死。行西程又不吉，号曰伤官遇杀，不测灾来，惟东方则吉，北方次之。此五六月用丁之说也。

- **分字分词释义**：
  - **木性虚焦**：木的性质虚弱焦枯 / 夏木特征 / 死墓之地
  - **一理共推**：一个道理可以共同推演 / 五六月相近 / 合论
  - **三伏生寒**：三伏天阴气始生 / 夏至后 / 六月特征
  - **丁火退气**：丁火气势减退 / 未月土旺火衰 / 用丁时机
  - **运行北地**：大运走北方水地 / 调候润燥 / 吉运
  - **木化成灰**：木被烧成灰烬 / 火旺无水 / 极凶之象
  - **伤官遇杀**：伤官格遇到七杀 / 火克金又泄身 / 灾祸之象
  - **不测灾来**：不可预测的灾祸来临 / 凶险 / 伤官见杀之患

- **规范化释义（primary_lang_explained）**：
  五月（午月）和六月（未月）的甲木，木性虚弱焦燥，道理可以一起推演。
  五月火旺，先用癸水（润），后用丁火（泄），庚金次之（生水）。
  六月三伏天生起寒气（阴气渐长），丁火退气。先用丁火（炼金/生土），后用庚金（劈甲/制劫），没有癸水也可以（未中乙木有根）。
  如果五月缺乏癸水，单独用丁火也可以（木火伤官），但大运要行北方水地才好（润局）。
  总之五六月用丁火（伤官），虽然运行北方水地，不至于死（有水护身）。但不利于运行南方火地，这叫“木化成灰”必死。运行西方金地也不吉利，这叫“伤官遇杀”，会有不可预测的灾祸，只有东方木地吉利，北方水地次之。这就是五六月用丁火的说法。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 5th and 6th Months (Horse/Goat) is weak and scorched; the principle is deduced together.
  In the 5th Month, first use Gui (Water), then Ding (Fire), with Geng (Metal) as secondary.
  In the 6th Month, the Three Fu Days generate Coldness, and Ding Fire retreats. First use Ding, then Geng; it is acceptable without Gui. If the 5th Month lacks Gui, using Ding is also acceptable, but it is best for Luck to run through the North (Water).
  In summary, using Ding Fire in the 5th/6th Months: Running through the North (Water) luck will not lead to death. However, running through the South (Fire) luck is unfavorable, called "Wood Turning to Ash", implying certain death. Running through the West (Metal) luck is also ominous, called "Hurting Officer Meeting Killing", bringing unpredictable disasters. Only the East (Wood) is auspicious, followed by the North. This is the theory of using Ding in the 5th/6th Months.

- **核心要点**：
  - **五月（午）**：极热，首重癸水调候。无水则木化成灰。
  - **六月（未）**：土旺，三伏生寒，可用丁炼金，不忌无癸。
  - **运势**：喜北（水润）、东（木助）；忌南（火焚）、西（伤官见官/杀）。

- **详细解说**：
  午月甲木死地，必须见水。
  - 若无水而见火（伤官），必须运走北方水地救命。若运走南方火地，火上浇油，木彻底成灰，寿夭。
  - “伤官遇杀”（伤官见官杀）：火克金，且泄身，身弱极，再见杀攻身，必灾。
  - 六月未土，虽然燥，但有乙木余气，且阴气始生，故比午月稍从容，可用丁庚配合（劈甲引丁）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_118]` `[trigger: 午未月甲木]` `[factor_trigger: (month_wu OR month_wei) AND tiangan_jia]` `[role: 主干]` 五六月甲木，木性虚焦，一理共推。 → 《穷通宝鉴·三夏甲木》#4.2
  - `[ns_qttbj_119]` `[trigger: 五月甲木]` `[factor_trigger: month_wu AND tiangan_jia AND tiangan_gui AND tiangan_ding]` `[role: 主干依赖]` 五月先癸后丁，庚金次之。 → 《穷通宝鉴·三夏甲木》#4.2
  - `[ns_qttbj_120]` `[trigger: 六月甲木]` `[factor_trigger: month_wei AND tiangan_jia AND tiangan_ding AND tiangan_geng]` `[role: 条件分支]` 六月三伏生寒，丁火退气，先丁后庚，无癸亦可。 → 《穷通宝鉴·三夏甲木》#4.2
  - `[ns_qttbj_121]` `[trigger: 木化成灰]` `[factor_trigger: (month_wu OR month_wei) AND tiangan_jia AND dayun_south_fire]` `[role: 例外处理]` 运行火地，号曰木化成灰必死。 → 《穷通宝鉴·三夏甲木》#4.2
  - `[ns_qttbj_122]` `[trigger: 伤官遇杀]` `[factor_trigger: (month_wu OR month_wei) AND tiangan_jia AND dayun_west_metal]` `[role: 例外处理]` 行西程又不吉，号曰伤官遇杀，不测灾来。 → 《穷通宝鉴·三夏甲木》#4.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 五六月甲木（午未月）"
    factor_refs: list = ['wood_turning_to_ash', 'hurting_officer_meeting_killing', 'three_fu_generating_cold']
    
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
        l1_anchor="qtbj_v1.0.0_2__五六月甲木_午未月_001_L1",
    )
    version: str = "1.0.0"
