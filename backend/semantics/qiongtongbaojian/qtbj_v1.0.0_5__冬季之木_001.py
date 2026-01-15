"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619775
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
    semantic_id="qtbj_v1.0.0_5__冬季之木_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 5冬季之木(SemanticEntry):
    """
    - **原文（source_text）**：
  冬月之木，盘屈在地，欲土多而培养。恶水盛而忘形。金总多不能克伐。火重见温暖有功。归根复命之时。木病安能辅助，须忌死绝之地，只宜生旺之方。

- **分...
    """
    
    original_text: str = """- **原文（source_text）**：
  冬月之木，盘屈在地，欲土多而培养。恶水盛而忘形。金总多不能克伐。火重见温暖有功。归根复命之时。木病安能辅助，须忌死绝之地，只宜生旺之方。

- **分字分词释义**：
  - **盘屈在地**：盘绕蜷缩在地下 / 冬木潜藏 / 冬眠之象
  - **培养**：培育保护 / 土的护根功能 / 冬木需土
  - **忘形**：失去形态 / 水多木漂或腐 / 冬木大忌
  - **金总多不能克伐**：金虽多也不能有效克木 / 金寒水冷反增寒 / 冬金无用
  - **温暖有功**：带来温暖是有功劳的 / 火为第一喜用 / 寒木向阳
  - **归根复命**：回归根本恢复生命 / 冬木内敛积蓄 / 等待来春
  - **木病**：木处于病位 / 亥子丑为木之病死墓 / 衰弱之极
  - **死绝之地**：金水之方（西北） / 加重寒气 / 运忌西北
  - **生旺之方**：木火之方（东南） / 温暖生发 / 运喜东南

- **规范化释义（primary_lang_explained）**：
  冬天的木，盘屈蜷缩在地下，希望能有厚土来培养保护根基。厌恶水太盛，水盛则木会忘失形态（漂流或腐烂）。金虽然多，但因为金生水、水生木（且金寒水冷），所以金不能有效地克伐木（反而增寒）。火重出现，带来温暖是有功劳的。此时是木归根复命（潜藏等待来春）的时候。木在病位（亥子丑为木之病死墓），怎能辅助呢？必须忌讳去往死绝的地方（再见金水），只适宜去往生旺的方向（东南木火方）。

- **完整对等诠释（secondary_lang_full）**：
  Wood in Winter is coiled underground; it desires abundant Earth for cultivation and protection. It detests abundant Water, which makes it lose its form. Even if Metal is plentiful, it cannot effectively prune (as Metal generates cold Water). Seeing heavy Fire brings warmth and merit. This is the time of "Returning to the Root and Restoring Life". Since Wood is in the "Sickness" stage, how can it assist? It must avoid places of Death and Extinction (Metal/Water lands) and is only suitable for directions of Birth and Prosperity (Wood/Fire lands).

- **核心要点**：
  - 首要：火（暖局、解冻）。
  - 次要：土（止水、培根）。
  - 大忌：水盛（冻木、漂木）。
  - 金无用：金生水增寒，不能克木。
  - 运势：宜东南生旺，忌西北死绝。

- **详细解说**：
  冬木（亥子丑月）完全进入冬眠状态。
  - 关键是“保暖”和“防涝”。
  - 水在冬天是忌神（除非极少量的亥水作为长生），因为水冷木冻。
  - 土非常重要，不仅培根，更能挡住大水。
  - 火是唯一的生机，所谓“寒木向阳”。
  - “归根复命”指木气内敛，外形枯槁但内在积蓄生机。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_064]` `[trigger: 冬木状态]` `[factor_trigger: season_winter AND element_wood AND element_earth]` `[role: 主干]` 冬月之木，盘屈在地，欲土多而培养。 → 《穷通宝鉴·论木》#2.5
  - `[ns_qttbj_065]` `[trigger: 冬木忌水]` `[factor_trigger: season_winter AND element_wood AND water_excessive]` `[role: 例外处理]` 恶水盛而忘形，水多则木漂或腐。 → 《穷通宝鉴·论木》#2.5
  - `[ns_qttbj_066]` `[trigger: 冬金无用]` `[factor_trigger: season_winter AND element_wood AND element_metal]` `[role: 总结]` 金总多不能克伐，金寒水冷反增寒。 → 《穷通宝鉴·论木》#2.5
  - `[ns_qttbj_067]` `[trigger: 冬木喜火]` `[factor_trigger: season_winter AND element_wood AND wood_winter_likes_fire]` `[role: 主干依赖]` 火重见温暖有功，寒木向阳。 → 《穷通宝鉴·论木》#2.5
  - `[ns_qttbj_068]` `[trigger: 归根复命]` `[factor_trigger: season_winter AND element_wood AND pattern_return_to_root]` `[role: 条件分支]` 归根复命之时，木气内敛积蓄生机。 → 《穷通宝鉴·论木》#2.5
  - `[ns_qttbj_069]` `[trigger: 冬木方位]` `[factor_trigger: season_winter AND element_wood AND direction_east_south]` `[role: 总结]` 须忌死绝之地，只宜生旺之方，运喜东南。 → 《穷通宝鉴·论木》#2.5"""
    normalized_text_zh: str = """"""
    subject: str = "5. 冬季之木"
    factor_refs: list = ['roots_hidden_underground', 'return_to_root', 'lose_form', 'pattern_cold_wood_facing_sun']
    
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
        l1_anchor="qtbj_v1.0.0_5__冬季之木_001_L1",
    )
    version: str = "1.0.0"
