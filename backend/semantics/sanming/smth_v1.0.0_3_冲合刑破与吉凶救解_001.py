"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066666
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
    semantic_id="smth_v1.0.0_3_冲合刑破与吉凶救解_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3冲合刑破与吉凶救解(SemanticEntry):
    """
    - 原文（source_text）：
  不正不冲，不偏不合，不横不刑，不直不破。其为冲也，启六极之岐门；其为合也，辟万物之形迹；其为刑也，变而改正；其为破也，敌而有伤。是以棘地生金，不若蓝田种玉。
...
    """
    
    original_text: str = """- 原文（source_text）：
  不正不冲，不偏不合，不横不刑，不直不破。其为冲也，启六极之岐门；其为合也，辟万物之形迹；其为刑也，变而改正；其为破也，敌而有伤。是以棘地生金，不若蓝田种玉。
  吉神相我，功求相吉之神；凶物伤身，解用伤凶之物。
  五行各得其所者，归聚成福；一局皆失其垣者，流荡无依。

- 分字分词释义：
  - **六极**：凶祸之极。
  - **相我**：帮助我（生我或助我）。
  - **相吉之神**：生助吉神之物（如财生官，印生身）。
  - **伤凶之物**：制伏凶神之物（如食制煞，印化煞）。
  - **各得其所**：财官印食各归禄旺之地。

- **规范化释义（primary_lang_explained）**：
  冲、合、刑、破都有其特定的气势和作用。冲能开启门户（如冲财库），但也可能带来灾祸；合能成就事物，但也可能羁绊；刑是因势而变（如三刑得用）；破是两敌相伤。所以，与其在艰难险阻中求成（棘地生金），不如在顺境中发展（蓝田种玉）。
  如果有吉神（如财官）帮助我，我要寻求能生助吉神的五行（如食伤生财，财生官）。如果有凶神（如七煞）伤害我，我要使用能制伏凶神的五行（如食神制煞，印绶化煞）。
  五行各居其位（禄旺），格局归聚，主富贵。若满盘皆死绝失地，主漂泊无依。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Clash-Combine-Punish-Break and Auspicious-Inauspicious Rescue" from the Qi-Xiang Chapter:

  - Its being clash opens six-extremes gates; its being combine separates myriad things' traces; its being punish changes to correct; its being break enemies mutually wounded.
  - Auspicious God assists me, seek merit from assisting-auspicious gods; fierce thing wounds body, resolve using wound-fierce objects.
  - Five Elements each gains its place, gathering accomplishes fortune; one chart all loses its walls, drifting without reliance.
  - Key: Clash/Combine/Punish/Break all are movement-images; protect auspicious control fierce; each element needs proper position.

- 核心要点：
  - **刑冲合破**：皆为动象，吉凶看喜忌。
  - **护吉制凶**：顺用吉神，逆用凶神。
  - **得地失垣**：五行需通根得地。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_009]` `[trigger: 刑冲合破]` `[factor_trigger: xingchong_hepo AND dongxiang_qishi]` `[role: 主干]` 不正不冲，不偏不合，不横不刑，不直不破。其为冲也，启六极之岐门。 → 《三命通会》卷十一#冲合刑破与吉凶救解
  - `[ns_smth_11_010]` `[trigger: 护吉制凶]` `[factor_trigger: huji_zhixiong AND jishen_xiangwo]` `[role: 主干依赖]` 吉神相我，功求相吉之神；凶物伤身，解用伤凶之物。 → 《三命通会》卷十一#冲合刑破与吉凶救解
  - `[ns_smth_11_011]` `[trigger: 棘地蓝田]` `[factor_trigger: jidi_lantian AND niru_zhongyu]` `[role: 条件分支]` 是以棘地生金，不若蓝田种玉。 → 《三命通会》卷十一#冲合刑破与吉凶救解
  - `[ns_smth_11_012]` `[trigger: 归聚流荡]` `[factor_trigger: guiju_liudang AND wuxing_dedi]` `[role: 总结]` 五行各得其所者，归聚成福；一局皆失其垣者，流荡无依。 → 《三命通会》卷十一#冲合刑破与吉凶救解"""
    normalized_text_zh: str = """"""
    subject: str = "3 冲合刑破与吉凶救解"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_8', 'bazi_semantic', 'bazi_relation_factor_10', 'bazi_semantic', 'bazi_relation_factor_11', 'bazi_semantic', 'bazi_state_factor_48', 'bazi_semantic', 'bazi_state_factor_49', 'bazi_semantic', 'bazi_factor_23', 'bazi_semantic', 'source_ref', 'rel_smth_11_007', 'chonghe_xingpo', 'rel_smth_11_008', 'gede_qisuo', 'rel_smth_11_009', 'jieshi_qiyuan', 'evi_smth_11_007', 'huji_zhixiong', 'rule_huji_zhixiong1', 'evi_smth_11_008', 'gede_qisuo', 'rule_gede_qisuo1', 'evi_smth_11_009', 'liudang_wuyi', 'rule_jieshi_qiyuan1', 'map_smth_11_005', 'map_smth_11_006']
    
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
        l1_anchor="smth_v1.0.0_3_冲合刑破与吉凶救解_001_L1",
    )
    version: str = "1.0.0"
