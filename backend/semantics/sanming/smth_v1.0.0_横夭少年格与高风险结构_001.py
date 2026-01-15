"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436545
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
    semantic_id="smth_v1.0.0_横夭少年格与高风险结构_001",
    book_id="sanming",
    engine_id="bazi"
)
class 横夭少年格与高风险结构(SemanticEntry):
    """
    - 原文（source_text）：

  横夭少年。

  夫横夭少年者，造化之穷绝，格局之变异也。有悬梁溺水、血产少亡、被人杀死，若此者何？乃身弱而遇煞重，煞多克身，又带刑冲破败之类；或命中元有官...
    """
    
    original_text: str = """- 原文（source_text）：

  横夭少年。

  夫横夭少年者，造化之穷绝，格局之变异也。有悬梁溺水、血产少亡、被人杀死，若此者何？乃身弱而遇煞重，煞多克身，又带刑冲破败之类；或命中元有官星受伤，行运复遇官乡；或无官见伤，运复临官之类；或带刃无制，运行合刃之地，及亡神劫煞等类，此皆横夭类也。不独女命有之，男命亦同。如一命：丁卯、癸丑、庚辰、丙子，庚用丁为官，被癸水子辰伤官叠遇，克之太重，水多金沉。一交丁巳运，伤官见官，又会丙煞克身，故溺水之害。

- 分字分词释义：

  - **横夭少年**：横，指横遭之祸；夭，早逝。概指意外、突发风险集中于少年时期。
  - **身弱煞重、刑冲破败**：日主气弱，而七煞、刑、冲、破、败等凶神过多，象征环境压力远超自我承受力。
  - **官星受伤 / 无官见伤**：夫星或权力象受损，或本无官星却反复遇伤官之运，皆主秩序与保护机制不足。
  - **带刃无制、亡神劫煞**：羊刃、亡神、劫煞等多而无制，象征高危险行为或环境。

- **规范化释义（primary_lang_explained）**：

  本节所谓“横夭少年格”，描述的是一种**风险高度聚集、守护机制薄弱**的结构：

  - 身弱煞重，好比个人的“安全防护”不足，而外界压力与危险因素过多；
  - 加上刑冲破败等组合，使突发事故、意外伤害的可能性增大；
  - 原例以庚金身弱、水煞过重、伤官见官的结构，说明溺水之害的象征逻辑。

  今人阅读，应将此视为“命局显示需高度重视安全与健康风险”的提醒，而不是对早亡的预言。

- 核心要点：

  - 身弱而煞重、刑冲破败成群，是横夭格的主要结构特征。
  - 官星、印星等“保护机制”若受损或缺失，风险更易聚集。
  - 现代解读应着重于安全教育、健康管理与环境选择上的谨慎，而非宿命论。

- 详细解说：

  1. **风险聚集的结构逻辑**  
     - 日主弱、煞星多，象征个体在高压、高风险环境中承载力不足；  
     - 刑、冲、破、败等象征突变与断裂，易与事故、冲突、极端情绪相应。

  2. **官星与印星的保护作用**  
     - 官星、印星适当时，可视为秩序、制度、家庭与社会支持；  
     - 当这些星位受损，命主可能缺乏稳定的规则与照护网络，更需后天弥补。

  3. **从“预言不幸”到“预防风险”**  
     - 与其死记“横夭少年”，不如据此提高对少年期身心安全、情绪健康、行动边界的重视；  
     - 当命局有类似结构时，可通过教育、环境选择、心理支持等方式，把潜在风险转化为警觉与自我照顾能力。

- 校勘与字词辨析：

  - “悬梁溺水、血产少亡、被人杀死”等语，本稿保留于原文段落中，但在白话与解说部分不作具体灾象扩展，仅作为古人列举的极端风险示例。
  - “横夭少年”在本稿中统摄为“高风险结构”，着重提醒防范，而非作定数之断。
  - **English**：
    - Reminder for prevention; not fixed-fate judgment.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_057]` `[trigger: 横夭少年定义]` `[factor_trigger: hengyao_shaonian_ge]` `[role: 主干]` 横夭少年。 → 《三命通会》卷七#横夭少年
  - `[ns_smth_07_058]` `[trigger: 造化穷绝]` `[factor_trigger: zaohua_qiongjue AND geju_bianyi]` `[role: 主干依赖]` 造化之穷绝，格局之变异也。 → 《三命通会》卷七#横夭少年
  - `[ns_smth_07_059]` `[trigger: 身弱煞重]` `[factor_trigger: shen_ruo_sha_zhong AND xingchong_pobai]` `[role: 条件分支]` 乃身弱而遇煞重，煞多克身，又带刑冲破败之类。 → 《三命通会》卷七#横夭少年
  - `[ns_smth_07_060]` `[trigger: 横夭类]` `[factor_trigger: hengyao_lei]` `[role: 总结]` 此皆横夭类也。不独女命有之，男命亦同。 → 《三命通会》卷七#横夭少年"""
    normalized_text_zh: str = """"""
    subject: str = "横夭少年格与高风险结构"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_100', 'bazi_semantic', 'bazi_structure_factor_101', 'bazi_semantic', 'bazi_state_factor_355', 'bazi_semantic', 'bazi_factor_12', 'bazi_semantic', 'source_ref', 'rel_smth_07_040', 'shensha_liliang', 'rel_smth_07_041', 'xingchong_miji', 'rel_smth_07_042', 'zhongdian_fanghu', 'evi_smth_07_040', 'shensha_liliang', 'rule_hengyao', 'evi_smth_07_041', 'xingchong_miji', 'rule_xingchong', 'evi_smth_07_042', 'zhongdian_fanghu', 'rule_fanghu', 'map_smth_07_027', 'map_smth_07_028']
    
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
        l1_anchor="smth_v1.0.0_横夭少年格与高风险结构_001_L1",
    )
    version: str = "1.0.0"
