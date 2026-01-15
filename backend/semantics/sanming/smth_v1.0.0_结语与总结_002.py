"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264282
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
    semantic_id="smth_v1.0.0_结语与总结_002",
    book_id="sanming",
    engine_id="bazi"
)
class 结语与总结(SemanticEntry):
    """
    - **原文（source_text）**：
  以上诸条，皆命理之要法，学者当细心玩味，触类旁通。
  五行生克，变化无穷；神煞吉凶，应验有准。
  要之，以日干为主，月令为纲，岁运为用，神煞为辅。...
    """
    
    original_text: str = """- **原文（source_text）**：
  以上诸条，皆命理之要法，学者当细心玩味，触类旁通。
  五行生克，变化无穷；神煞吉凶，应验有准。
  要之，以日干为主，月令为纲，岁运为用，神煞为辅。
  明得此理，则看命无难矣。

- **核心总结**：
  本卷涵盖了看命口诀、巫咸撮要、玉井奥诀等重要赋文，是《三命通会》实战应用的核心。
  强调了**月令提纲**的重要性，**日主旺衰**的判断，**财官印食**的取用，以及**岁运神煞**的吉凶应期。
  对于**天元地元**、**三元吉凶**、**五行成象**、**纳音交互**等高阶技法也有深入论述。
  掌握这些口诀与心法，是通往命理高手的必经之路。

- 完整对等诠释（secondary_lang_full）：

  This closing section summarizes the essential methods of destiny analysis covered in this volume. The reader is urged to study carefully and draw analogies across cases.

  The five elements generate and control in endless variations; the auspicious and baleful stars manifest with reliable patterns. The core framework is: Day Stem as the subject, Month Branch as the guiding principle, annual and major luck as the operative timing, and spirit-stars as auxiliary markers.

  Once this logic is truly grasped, reading a chart becomes straightforward. The volume's teachings—including the Kan-Ming rhymes, Wu-Xian Cuoyao, and Yuqing Aojue—form the practical core of Sanming Tonghui, covering Month Command priority, Day Master strength assessment, Wealth-Officer-Seal-Food usage, and year-luck spirit-star timing.

  Engineering note: This summary validates the architectural hierarchy: Day Master → Month Command → Luck Timing → Spirit-Stars as the canonical evaluation sequence.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_jieyu2_001]` `[trigger: 日干为主]` `[factor_trigger: rigan_weizhu AND yueling_weigang]` `[role: 主干]` 以日干为主，月令为纲，岁运为用，神煞为辅。 → 《三命通会》卷十#结语与总结
  - `[ns_smth_10_jieyu2_002]` `[trigger: 明得此理]` `[factor_trigger: mingde_cili AND kanming_wunan]` `[role: 总结]` 明得此理，则看命无难矣。 → 《三命通会》卷十#结语与总结"""
    normalized_text_zh: str = """"""
    subject: str = "结语与总结"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_71', 'bazi_semantic', 'bazi_structure_month_command_3', 'bazi_semantic', 'bazi_temporal_factor_7', 'bazi_semantic', 'source_ref', 'rel_smth_10_052', 'rigan_weizhu_kuangjia', 'rel_smth_10_053', 'suiyun_weiyong', 'rel_smth_10_054', 'wuxing_shengke', 'evi_smth_10_052', 'rigan_weizhu_kuangjia', 'rule_kanming_kuangjia1', 'evi_smth_10_053', 'yingqi_panduan', 'rule_suiyun_weiyong1', 'evi_smth_10_054', 'bianhua_wuqiong', 'rule_xuexi_fangfa1', 'map_smth_10_035', 'map_smth_10_036']
    
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
        l1_anchor="smth_v1.0.0_结语与总结_002_L1",
    )
    version: str = "1.0.0"
