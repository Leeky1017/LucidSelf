"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619927
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
    semantic_id="qtbj_v1.0.0_3__七月甲木补充_丁庚配合_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3七月甲木补充丁庚配合(SemanticEntry):
    """
    - **原文（source_text）**：
  七月甲木，丁火为尊，庚金次之，庚金不可少。火隔水不能镕金，故丁火镕金，必赖甲木引助，方成洪炉。若有癸水阻隔，便灭丁火，壬水无碍，且能合丁，但须见戊土，...
    """
    
    original_text: str = """- **原文（source_text）**：
  七月甲木，丁火为尊，庚金次之，庚金不可少。火隔水不能镕金，故丁火镕金，必赖甲木引助，方成洪炉。若有癸水阻隔，便灭丁火，壬水无碍，且能合丁，但须见戊土，方可制水存火。

- **分字分词释义**：
  - **丁火为尊**：丁火是最尊贵的用神 / 首选 / 炼金之火
  - **庚金不可少**：庚金不能缺少 / 成器原料 / 配合丁火
  - **火隔水**：火被水阻隔 / 水克火 / 炼金失效
  - **镕金**：熔炼金属 / 丁火功能 / 火炼金
  - **甲木引助**：甲木引燃帮助 / 劈甲引丁 / 燃料
  - **洪炉**：旺盛的炉火 / 丁火旺象 / 成器之火
  - **癸水阻隔**：癸水阻挡隔绝 / 雨露灭火 / 大忌
  - **壬水无碍**：壬水没有妨碍 / 江河不灭灯 / 可合化

- **规范化释义（primary_lang_explained）**：
  七月（申月）的甲木，以丁火为至尊（最重要），庚金次之，但庚金也不可少（原材料）。火隔着水就不能熔炼金，所以丁火熔金，必须依赖甲木（劈甲）引火助燃，才能成为洪炉大火。如果有癸水阻隔，便会浇灭丁火；壬水则无大碍（壬合丁化木，或壬水流动不克火），且壬能合丁，但必须见到戊土（堤坝），才能制住水而保存火。

- **完整对等诠释（secondary_lang_full）**：
  For Jia Wood in the 7th Month, Ding Fire is supreme, followed by Geng Metal; yet Geng Metal cannot be lacking. Fire separated by Water cannot melt Metal; therefore, for Ding Fire to melt Metal, it must rely on Jia Wood to ignite and assist, creating a great furnace. If Gui Water obstructs, it extinguishes Ding Fire. Ren Water is not a hindrance and can combine with Ding, but Wu Earth must be seen to control Water and preserve Fire.

- **核心要点**：
  - **尊卑**：丁第一，庚第二。
  - **机制**：甲木引丁（劈甲引丁）。
  - **水的影响**：怕癸（灭火），不怕壬（合化/需戊）。

- **详细解说**：
  - 申月甲木为死木，庚金为顽铁，丁火为炼炉。
  - “劈甲引丁”：死木正好用来生火，火炼金成器，循环有情。
  - 癸水是大忌，因为它是雨露之水，直克丁火（灯烛）。
  - 壬水是江河，丁壬相合化木（在木旺或特定条件下），或者壬水冲奔不直接灭丁，但仍需戊土制衡。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_137]` `[trigger: 丁火为尊]` `[factor_trigger: month_shen AND tiangan_jia AND tiangan_ding AND tiangan_geng]` `[role: 主干]` 七月甲木，丁火为尊，庚金次之，庚金不可少。 → 《穷通宝鉴·三秋甲木》#5.3
  - `[ns_qttbj_138]` `[trigger: 劈甲引丁]` `[factor_trigger: split_jia_ignite_ding AND tiangan_ding AND tiangan_geng]` `[role: 主干依赖]` 丁火镕金，必赖甲木引助，方成洪炉。 → 《穷通宝鉴·三秋甲木》#5.3
  - `[ns_qttbj_139]` `[trigger: 癸灭丁]` `[factor_trigger: tiangan_gui AND tiangan_ding AND gui_extinguish_ding]` `[role: 例外处理]` 若有癸水阻隔，便灭丁火，壬水无碍。 → 《穷通宝鉴·三秋甲木》#5.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 七月甲木补充（丁庚配合）"
    factor_refs: list = ['great_furnace', 'split_jia_ignite_ding', 'fire_separated_by_water']
    
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
        l1_anchor="qtbj_v1.0.0_3__七月甲木补充_丁庚配合_001_L1",
    )
    version: str = "1.0.0"
