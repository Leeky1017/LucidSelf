"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042744
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
    semantic_id="smth_v1.0.0_上半年长生与下半年生成_001",
    book_id="sanming",
    engine_id="bazi"
)
class 上半年长生与下半年生成(SemanticEntry):
    """
    - **原文（source_text）**：
  大抵合而言之，上半年主长生，曰雨、曰雷、曰风，皆生之气；下半年主生成，曰露、曰霜、曰雪，皆成之气。下半年言天时，不言农时：农时莫急于春夏也。

- *...
    """
    
    original_text: str = """- **原文（source_text）**：
  大抵合而言之，上半年主长生，曰雨、曰雷、曰风，皆生之气；下半年主生成，曰露、曰霜、曰雪，皆成之气。下半年言天时，不言农时：农时莫急于春夏也。

- **分字分词释义**：
  - **长生 / 生成**：长生偏向萌芽、生发；生成偏向成熟、定型。
  - **雨雷风 / 露霜雪**：前者属阳动之气，后者属阴收之气，分别标志气机的升与降。
  - **天时 / 农时**：天时指自然气候的变化，农时指农业作业的关键时段。

- **规范化释义（primary_lang_explained）**：
  作者在节气细分之后，总结出一个简明的大图景：一年上半年以长生为主，雨、雷、风等现象，都在为万物萌芽、成长提供动力；下半年以生成为主，露、霜、雪等现象，则在帮助万物收敛、成熟、定形。下半年所言，多关乎天时与气机收束，而真正关系到农作物存亡的农时，主要集中在春夏上半年。

- **完整对等诠释（secondary_lang_full）**：
  After detailing the individual solar terms, the author steps back to sketch a simple macro‑picture. The first half of the year is dominated by “long life”: rain, thunder and wind are all outward‑moving yang phenomena that awaken and drive growth. The second half is dominated by “formation”: dew, frost and snow are yin manifestations that help things contract, ripen and settle into their final forms. Much of what is said about the latter half concerns Heaven’s timing and the gathering of qi; the truly critical windows for agriculture—sowing, rooting, early growth—cluster in spring and summer. For fate analysis this suggests that, beyond exact term, we should note whether a birth or an event falls in the expansive half of the yearly rhythm or the contracting half, and adjust our expectations of growth versus consolidation accordingly.

- **核心要点**：
  - 对命理调候来说，判断一个命局是否「得时」，关键不只在具体节气，而在其所处大半年是「长生段」还是「生成段」。
  - 许多经典断语围绕「春夏生者宜顺生长之势，秋冬生者宜顺收藏之机」展开，本段给出了气候学上的根基。
  - 在应用中，可将「上半年/下半年」作为一个粗粒度标签，与具体节气和真实气象数据一同使用，避免只靠24节气文句做生硬判断。

- **详细解说**：
  1) 在时间特征中增加「半年段」标签：以立春或立冬为起点，将上半年标记为「长生期」、下半年标记为「生成期」，与节气坐标一并输入；
  2) 推盘时，将上半年出生者整体倾向于「顺势生长」，在用神与格局解释中强调发展空间；下半年出生者则偏向「生成收敛」，强调整合、沉淀与收束；
  3) 行运分析中，可将每年的上半年视为该年「起势段」，下半年视为「定形段」，结合命局结构判断哪些年份的哪一半更值得发力；
  4) 工程实现时，将「半年段」视为介于节气与季节之间的中尺度特征，有助于缓和因节气边界所带来的跳变效应。

- 反例与边界：
  - 不宜仅凭「上半年/下半年」就粗暴下结论，如「上半年生就好、下半年生就差」，违背中和原则；
  - 不能把半年段标签当作替代节气的粗糙指标，而应该与节气与气象数据叠加校正；
  - 工程上若只用半年段而不用节气，会导致时间刻度过于粗糙，无法还原许多关键调候细节；
  - 反向误区是过于迷信节气细分，而完全忽略「半年节奏」这种宏观韵律，使模型失去对大势起伏的把握。 

- 小例（示意）：
  - 某命局火土偏旺而生于上半年，系统可解释为「上半年长生段中火土易被放大」，在用神策略上更强调水木调衡，并在运程建议中提醒上半年更宜谨慎扩张；
  - 另一命局金水偏寒而生于下半年，系统则提示其「生成段偏寒收敛」，适合在下半年更多做整理、复盘与结构调整，而将突破与开局安排在上半年有利年份。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_02_bannian_001]` `[trigger: 上半年长生]` `[factor_trigger: shangbannian_zhangsheng AND yu_lei_feng]` `[role: 主干]` 上半年主长生，曰雨、曰雷、曰风，皆生之气。 → 《三命通会》卷二#上半年长生
  - `[ns_smth_02_bannian_002]` `[trigger: 下半年生成]` `[factor_trigger: xiabannian_shengcheng AND lu_shuang_xue]` `[role: 主干依赖]` 下半年主生成，曰露、曰霜、曰雪，皆成之气。 → 《三命通会》卷二#上半年长生
  - `[ns_smth_02_bannian_003]` `[trigger: 农时春夏]` `[factor_trigger: nongshi_chunxia AND jishi_zhongyao]` `[role: 条件分支]` 下半年言天时，不言农时：农时莫急于春夏也。 → 《三命通会》卷二#上半年长生
  - `[ns_smth_02_bannian_004]` `[trigger: 半年节奏]` `[factor_trigger: bannian_jiezou AND honguan_yunlv]` `[role: 总结]` 判断命局是否得时，关键在其所处大半年是长生段还是生成段。 → 《三命通会》卷二#上半年长生

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 时间类 | 半年段标签 | bazi_temporal_factor_1 | existing | 大尺度节律 | 长生段/生成段 | bazi_semantic | 上半年主生下半年主成 |
| 条件类 | 得时判断 | bazi_condition_factor_5 | existing | 调候基础 | 长生期/生成期 | bazi_semantic | 与节气叠加使用 |
<!-- FACTOR_END -->"""
    normalized_text_zh: str = """"""
    subject: str = "上半年长生与下半年生成"
    factor_refs: list = []
    
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
        l1_anchor="smth_v1.0.0_上半年长生与下半年生成_001_L1",
    )
    version: str = "1.0.0"
