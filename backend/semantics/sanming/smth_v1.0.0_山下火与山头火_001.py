"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228225
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
    semantic_id="smth_v1.0.0_山下火与山头火_001",
    book_id="sanming",
    engine_id="bazi"
)
class 山下火与山头火(SemanticEntry):
    """
    - **原文（source_text）**：
  丙申丁酉，气息形藏，势力韬光，龟缩兑位，力微体弱，明不及远，乃曰山下火也。甲戌乙亥，谓之山头火者，山乃藏形，头乃投光，内明外暗，隐而不显，飞光投乾，归...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙申丁酉，气息形藏，势力韬光，龟缩兑位，力微体弱，明不及远，乃曰山下火也。甲戌乙亥，谓之山头火者，山乃藏形，头乃投光，内明外暗，隐而不显，飞光投乾，归于休息之中，故曰山头火也。

- **分字分词释义**：
  - **气息形藏**：气息形体藏匿。
  - **势力韬光**：势力隐藏光芒。
  - **龟缩兑位**：收缩在兑位（西方）。
  - **力微体弱**：力量微弱体质柔弱。
  - **明不及远**：光明达不到远处。
  - **山乃藏形**：山是藏形的。
  - **头乃投光**：山头投射光芒。
  - **内明外暗**：内部明亮外部昏暗。
  - **隐而不显**：隐藏而不显露。
  - **飞光投乾**：飞散的光投向乾位（西北）。
  - **归于休息之中**：归入休息状态。

- **规范化释义（primary_lang_explained）**：
  丙申丁酉，气息形体藏匿，势力隐藏光芒，收缩在兑位（西方），力量微弱体质柔弱，光明达不到远处，就叫山下火。甲戌乙亥，称为山头火的原因是，山是藏形的，山头投射光芒，内部明亮外部昏暗，隐藏而不显露，飞散的光投向乾位（西北），归入休息状态，所以叫山头火。

- **完整对等诠释（secondary_lang_full）**：
  Bingshen-Dingyou: qi-breath and form concealed, power hiding radiance, contracting at Dui position (west), force weak body feeble, brightness not reaching far, thus called Mountain-Beneath Fire. Jiaxu-Yihai: called Mountain-Peak Fire because mountains conceal form, peaks cast light, internally bright externally dark, hidden not manifest, scattered light casting toward Qian position (northwest), returning to resting state, thus called Mountain-Peak Fire.

- **核心要点**：
  - 丙申丁酉：山下火（势力韬光，明不及远）
  - 甲戌乙亥：山头火（内明外暗，归于休息）
  - 山下火为火的微弱收敛
  - 山头火为火的归藏完结

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_187]` `[trigger: 山下火与山头火]` `[factor_trigger: mountain_beneath_fire AND mountain_peak_fire AND nayin_fire_final]` `[role: 主干]` 丙申丁酉，气息形藏，势力韬光，龟缩兑位，力微体弱，明不及远，乃曰山下火也。甲戌乙亥，内明外暗，隐而不显，飞光投乾，归于休息之中，故曰山头火也。 → 《三命通会》卷一#山下火与山头火

- **详细解说**：
  此条完成火纳音的解释。丙申丁酉为"山下火"：申酉属金旺之地（火克金耗力），火在山下被遮蔽，势力韬光，力微体弱，光明不及远，这是火的衰弱状态。甲戌乙亥为"山头火"：戌亥为秋冬之交（火进入休息），火在山头若隐若现，内明外暗，飞光投向西北（乾位天门），归于休息，这是火的归藏完结。六种火纳音：霹雳火（神异）→炉中火（冶炼）→覆灯火（照明）→天上火（极盛）→山下火（衰弱）→山头火（归藏），完整呈现火的一生。命理上，山下火命格内敛含蓄，山头火命格归隐休息。

- **校勘与字词辨析（双语）**：
  - **中文**："山下火"指山下被遮蔽的火光。"韬光"指隐藏光芒。"兑位"指西方。"山头火"指山顶若隐若现的火光（如夕阳余晖）。"飞光投乾"指光散向西北天门。
  - **English**: "Mountain-Beneath Fire" refers to fire obscured beneath mountains. "Hiding radiance" means concealing light. "Dui position" means west. "Mountain-Peak Fire" refers to fire flickering on mountain peaks (like sunset glow). "Scattered light toward Qian" means light dispersing toward northwest Heaven's Gate."""
    normalized_text_zh: str = """"""
    subject: str = "山下火与山头火"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_山下火与山头火_001_L1",
    )
    version: str = "1.0.0"
