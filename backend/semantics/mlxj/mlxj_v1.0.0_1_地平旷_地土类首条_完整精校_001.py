"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.825943
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
    semantic_id="mlxj_v1.0.0_1_地平旷_地土类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1地平旷地土类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

地平旷大吉。地者，阴土也，平旷广大而深厚也。五方五色土居中央：至哉坤元，万物资始。生生息息，其利无穷。梦此者富厚福泽，通达安平，大吉之占。地者，万物之祖元，...
    """
    
    original_text: str = """#### 原文（source_text）

地平旷大吉。地者，阴土也，平旷广大而深厚也。五方五色土居中央：至哉坤元，万物资始。生生息息，其利无穷。梦此者富厚福泽，通达安平，大吉之占。地者，万物之祖元，气发生也。东至泰远，西至邦国，南至濮铅，北至祝栗。自混蒙之气，重浊者位下成质，而地得以宁。

#### 分字分词释义

- **地**：大地 / 坤卦所主 / 阴土、厚载、根基
- **平旷**：平坦广阔 / 无险阻 / 通达顺畅
- **阴土**：地属阴 / 五行属土 / 承载万物
- **五方五色土**：东青、南赤、西白、北黑、中黄 / 社稷坛五色土 / 王者封土
- **坤元**：坤卦之元 / 《易经》坤卦彖辞 / 地道之始
- **万物资始**：万物赖以生成 / 地生万物 / 母性滋养
- **混蒙**：混沌未开 / 太初之气 / 天地未分
- **重浊**：气之重浊者 / 下沉成地 / 与轻清上升为天相对

#### 规范化释义（primary_lang_explained）

梦见大地平坦广阔，大吉。地是阴土，平旷则广大深厚。五方有五色土，居于中央：「至哉坤元，万物资始」。生生不息，其利无穷。做此梦者，主富厚福泽、通达安平，是大吉之占。

地是万物的祖元，元气从此发生。东至泰远，西至邦国，南至濮铅，北至祝栗。自混沌之气分化，重浊者下沉成质，而大地得以安宁。

#### 完整对等诠释（secondary_lang_full）

Dreaming of flat and expansive land is greatly auspicious. Earth represents Yin-soil, and when flat and vast, it signifies breadth, depth, and solidity. The five directions have five-colored soils centered at the middle: "Supreme is the primal force of Kun (Earth), from which all things derive their birth." Endlessly generating life, its benefits are boundless. The dreamer enjoys abundant blessings, smooth passage, and great fortune.

Earth is the ancestral source of all things, where primordial Qi manifests. From the primordial chaos, the heavy and turbid elements descended to form substance, and thus the Earth became stable.

#### 核心要点

- 地平旷为地理梦象最高吉兆
- 对应《易经》坤卦，「至哉坤元，万物资始」
- 地=阴土/根基/厚载/母性
- 五方五色土=东青南赤西白北黑中黄
- 主富厚福泽——财富丰裕
- 主通达安平——事业顺畅
- 地为万物之祖元——生命根源

#### 详细解说

本条是地理部开篇第一条，以「地平旷」这一最高吉兆统领全部地理类梦象。

地在中国传统宇宙观中与天相对，天为阳、地为阴，天为乾、地为坤。《易经·坤卦》彖辞云：「至哉坤元，万物资生，乃顺承天。坤厚载物，德合无疆。」地的特性是厚德载物、柔顺承天、滋生万物。

梦见地平旷，意味着根基稳固、事业通达、财富充盈。五方五色土（东青、南赤、西白、北黑、中黄）是古代社稷坛的象征，代表王者拥有四方土地。梦见此象，主基业宏大、福泽深厚。

在人事应验上，地平旷分层映射为：
- **事业层**：根基稳固、发展顺畅
- **财富层**：资产丰厚、收益稳定
- **家庭层**：宅基安宁、子孙繁盛
- **心理层**：内心踏实、安全感充足

#### 校勘与字词辨析

- **中文**：「至哉坤元」出自《易经·坤卦》彖辞，「至」通「大」，极致之意。
- **English**："Zhì zāi Kūn yuán" from the Tuan commentary of Kun hexagram; "zhì" means "supreme" or "ultimate."

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v3_001]` `[trigger: 梦地平旷]` `[factor_trigger: dream_di_pingkuang AND yijing_kun AND dream_dishanshuilu AND dream_di_xian AND dream_shui_qing AND dream_shui_zhuo]` `[role: 主干]` 地平旷大吉。地者，阴土也，平旷广大而深厚也。 → 《梦林玄解·卷三》#地平旷
- `[ns_mlxj_v3_002]` `[trigger: 梦地平旷]` `[factor_trigger: dream_di_pingkuang]` `[role: 主干依赖]` 至哉坤元，万物资始。生生息息，其利无穷。梦此者富厚福泽，通达安平。 → 《梦林玄解·卷三》#地平旷
- `[ns_mlxj_v3_003]` `[trigger: 地理论]` `[factor_trigger: dream_dili_theory]` `[role: 理论基础]` 地者，万物之祖元，气发生也。自混蒙之气，重浊者位下成质，而地得以宁。 → 《梦林玄解·卷三》#地平旷
- `[ns_mlxj_v3_004]` `[trigger: 地状梦象]` `[factor_trigger: di_zhuangtai AND dream_dipingkuang AND dream_ditu AND dream_chengshi]` `[role: 地理体系]` 地之状态：平旷、图绘、城市等梦象。 → 《梦林玄解·卷三》#地理
- `[ns_mlxj_v3_005]` `[trigger: 山水梦象]` `[factor_trigger: dream_shanshui AND dream_shanxing AND dream_shangshan_pengri]` `[role: 山水类]` 山水之象：登山捧日大吉，山行得贵。 → 《梦林玄解·卷三》#山水
- `[ns_mlxj_v3_006]` `[trigger: 升迁应验]` `[factor_trigger: career_shengguan AND dream_chengshang_guan AND outcome_fuhou_fuze AND outcome_wo_daquan]` `[role: 主应]` 地理梦象主升官富厚福泽。 → 《梦林玄解·卷三》#主应
- `[ns_mlxj_v3_007]` `[trigger: 地理结构]` `[factor_trigger: dream_cheng_deng AND dream_cheng_hui AND dream_qiao_xin AND dream_qiao_huai AND dream_shan_beng]` `[role: 结构类]` 城登、城毁、桥新、桥坏、山崩等地理结构梦象。 → 《梦林玄解·卷三》#地理结构"""
    normalized_text_zh: str = """"""
    subject: str = "1 地平旷（地土类首条·完整精校）"
    factor_refs: list = ['dream_di_pingkuang', 'yijing_kun', 'yin_tu', 'kun_yuan', 'wuse_tu']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_地平旷_地土类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
