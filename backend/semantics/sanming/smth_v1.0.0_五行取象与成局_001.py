"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264203
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
    semantic_id="smth_v1.0.0_五行取象与成局_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行取象与成局(SemanticEntry):
    """
    - 原文（source_text）：
  凡五行取象，本象取本象，如甲乙、丙丁、木火象之类；化象取化象，如戊癸、丁壬、亦木火象之类。
  金水象不可见土，谓土杂水混，金自不清。岁运遇土亦滞。惟金水不杂...
    """
    
    original_text: str = """- 原文（source_text）：
  凡五行取象，本象取本象，如甲乙、丙丁、木火象之类；化象取化象，如戊癸、丁壬、亦木火象之类。
  金水象不可见土，谓土杂水混，金自不清。岁运遇土亦滞。惟金水不杂，生于秋月最贵。
  金土象不可见木，谓木克土，则土不能生金，不成象也。土积成金，土多金少，其福厚实。
  金火象不可见水，见水则火灭金沉，不能成器。
  水木象秀而清高，不可见卯巳，以水死绝。
  木火象秀而丰富，不可见金，以木受克。
  水火象成，既济最妙，或未济亦得，不可见土。
  水土象不可见火，土重水轻，秀而不实。
  火土象不可见水，火虚土聚，不成物。

- 分字分词释义：
  - **两气成象**：日主与另一五行力量相当，成两气专旺（如金水、木火）。
  - **本象**：日主本气。
  - **化象**：干支合化之气。
  - **不可见**：指忌神，破坏成像之物。

- **规范化释义（primary_lang_explained）**：
  取象时，可取五行本气（如甲乙木），也可取化气（如丁壬化木）。
  金水成象（金白水清），忌见土，因土混水埋金。生于秋月最贵。
  金土成象（土生金），忌见木，因木克土，土不能生金。
  金火成象（火炼金），忌见水，水灭火，金不成器。
  水木成象（水木清华），忌见损水之物（如土），或水死绝之地（卯巳）。
  木火成象（木火通明），忌见金，金克木。
  水火成象（既济），忌见土，土克水晦火。
  水土成象，忌见火。火土成象，忌见水。

- 核心要点：
  - **两气成象**：喜相生相助，忌克泄杂乱。
  - **顺势而为**：顺应两气之势，不可逆。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_029]` `[trigger: 本象化象]` `[factor_trigger: benxiang_huaxiang AND wuxing_quxiang]` `[role: 主干]` 凡五行取象，本象取本象，如甲乙、丙丁、木火象之类；化象取化象。 → 《三命通会》卷十#五行取象与成局
  - `[ns_smth_10_030]` `[trigger: 金白水清]` `[factor_trigger: jinbai_shuiqing AND qiuyue_zuigui]` `[role: 主干依赖]` 金水象不可见土，谓土杂水浑，金自不清。惟金水不杂，生于秋月最贵。 → 《三命通会》卷十#五行取象与成局
  - `[ns_smth_10_031]` `[trigger: 木火通明]` `[factor_trigger: muhuo_tongming AND xiu_erfengfu]` `[role: 条件分支]` 木火象秀而丰富，不可见金，以木受克。 → 《三命通会》卷十#五行取象与成局
  - `[ns_smth_10_032]` `[trigger: 既济最妙]` `[factor_trigger: jiji_zuimiao AND shuihuo_chengxiang]` `[role: 总结]` 水火象成，既济最妙，或未济亦得，不可见土。 → 《三命通会》卷十#五行取象与成局"""
    normalized_text_zh: str = """"""
    subject: str = "五行取象与成局"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_67', 'bazi_semantic', 'bazi_condition_jishen', 'bazi_semantic', 'bazi_state_metal_water_1', 'bazi_semantic', 'bazi_state_wood_fire', 'bazi_semantic', 'bazi_condition_factor_95', 'bazi_semantic', 'source_ref', 'rel_smth_10_028', 'liangqi_chengxiang', 'rel_smth_10_029', 'jinshui_jiantu', 'rel_smth_10_030', 'muhuo_tongming', 'evi_smth_10_028', 'liangqi_chengxiang', 'rule_liangqi_chengxiang1', 'evi_smth_10_029', 'hunza_buqing', 'rule_jinshui_jiantu1', 'evi_smth_10_030', 'xiu_erfengfu', 'rule_muhuo_tongming1', 'map_smth_10_019', 'map_smth_10_020']
    
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
        l1_anchor="smth_v1.0.0_五行取象与成局_001_L1",
    )
    version: str = "1.0.0"
