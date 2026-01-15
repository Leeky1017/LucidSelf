"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264292
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
    semantic_id="smth_v1.0.0_交运如接木与月令为运元_001",
    book_id="sanming",
    engine_id="bazi"
)
class 交运如接木与月令为运元(SemanticEntry):
    """
    - **原文（source_text）**：  
  吉。又曰：古人以甲子乙丑名支干，六十甲子用花字，是皆以木喻义。若天干地支得时，自然开花结子茂盛。月令者，天元也，今运就月上起，譬之树苗，树之见苗，...
    """
    
    original_text: str = """- **原文（source_text）**：  
  吉。又曰：古人以甲子乙丑名支干，六十甲子用花字，是皆以木喻义。若天干地支得时，自然开花结子茂盛。月令者，天元也，今运就月上起，譬之树苗，树之见苗，则知其名，月之用神，则知其格。故谓交运如同接木，命有根苗花实，正此意也。若出癸入甲，譬反汗之人，多主不吉。

- **规范化释义（primary_lang_explained）**：  
  此段以树木开花结果为喻，说明六十甲子只要「得时」，自然能发挥其应有之用。月令在这里被称为「天元」，实际上是说：大运的起点必系于月令，命局的根苗花实也都以月令为纲。交接大运，好比在已有根苗的树上接入新枝；若新运与月令用神和命局根气同类，则接木得宜，枝叶繁茂；若如「出癸入甲」般从一端骤然跳至另一端，而命局又缺乏中和之力，则好比重病之人强行换阳，多主不吉。

- **完整对等诠释（secondary_lang_full）**：  
  This passage uses the image of a tree blossoming and bearing fruit to explain that the sixty Jiazi flourish naturally when they are "in season." The Month Branch is called the "Heavenly Origin" not in the sense of the natal Year, but as the pivot from which major luck cycles are started. The natal chart already provides roots and sprouts; the Month's useful spirit reveals the pattern. When one luck decade ends and another begins, it is like grafting a new branch onto this living tree: if the incoming luck shares the same quality of qi as the Month and the natal roots, the graft takes and growth continues; if, however, the shift is as abrupt as "leaving Gui and entering Jia"—jumping from one extreme to another without proper adjustment—then it resembles forcing a dramatic yang reversal on someone gravely ill, often leading to misfortune.

- **核心要点**：
  - 月令是大运的起点与纲领，可视为运元。
  - 大运交替如接木，要看新运与原局根苗是否同气。
  - 「出癸入甲」式剧烈转换，如体弱而强行换阳，风险极高。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_065]` `[trigger: 月令为运元]` `[factor_trigger: yueling_weiyunyuan AND yun_jiu_yue_qi]` `[role: 主干]` 月令者，天元也，今运就月上起，譬之树苗。 → 《三命通会》卷十#交运如接木与月令为运元
  - `[ns_smth_10_066]` `[trigger: 交运如接木]` `[factor_trigger: jiaoyun_rujiemu AND mingju_genmiao]` `[role: 主干依赖]` 故谓交运如同接木，命有根苗花实，正此意也。 → 《三命通会》卷十#交运如接木与月令为运元
  - `[ns_smth_10_067]` `[trigger: 出癸入甲]` `[factor_trigger: chugui_rujia AND fanhan_zhiren]` `[role: 条件分支]` 若出癸入甲，譬反汗之人，多主不吉。 → 《三命通会》卷十#交运如接木与月令为运元
  - `[ns_smth_10_068]` `[trigger: 花字得时]` `[factor_trigger: huazi_deshi AND kaihua_jiezi]` `[role: 总结]` 若天干地支得时，自然开花结子茂盛。 → 《三命通会》卷十#交运如接木与月令为运元"""
    normalized_text_zh: str = """"""
    subject: str = "交运如接木与月令为运元"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_交运如接木与月令为运元_001_L1",
    )
    version: str = "1.0.0"
