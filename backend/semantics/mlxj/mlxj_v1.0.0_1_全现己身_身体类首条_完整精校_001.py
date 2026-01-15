"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.782212
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
    semantic_id="mlxj_v1.0.0_1_全现己身_身体类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1全现己身身体类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

全现己身，大吉。人之相貌，谁能自知？自知之明，征祥备矣。君子得之荣显，小人得之康健，当默识之。顾虎头名恺之，尝梦自己面目肌发，睆然如鉴，其详之曰：反照其体肤...
    """
    
    original_text: str = """#### 原文（source_text）

全现己身，大吉。人之相貌，谁能自知？自知之明，征祥备矣。君子得之荣显，小人得之康健，当默识之。顾虎头名恺之，尝梦自己面目肌发，睆然如鉴，其详之曰：反照其体肤，此自知之妙。后果名重天下。

#### 分字分词释义

- **全现己身**：梦中完整看见自己的身体 / 自我观照 / 自知之明
- **自知之明**：能够认识自己 / 知人者智，自知者明
- **征祥备矣**：吉祥之征都具备了
- **睆然如鉴**：明亮如镜 / 清晰明澈
- **反照**：反观 / 自我观照

#### 规范化释义（primary_lang_explained）

梦见完整看见自己的身体，大吉。人的相貌，谁能自知？能够自知之明，则吉祥之征都具备了。君子得此梦则荣显，小人得此梦则康健，应当默默记住。

顾恺之尝梦见自己面目肌发，明亮如镜，他详细解释道：「反照其体肤，此自知之妙。」后来果然名重天下。

#### 完整对等诠释（secondary_lang_full）

Dreaming of seeing one's entire body is greatly auspicious. Who can truly know their own appearance? Self-knowledge is the perfection of auspicious signs. When a virtuous person dreams this, they gain glory; when a common person dreams this, they gain health—remember this well.

Gu Kaizhi once dreamed of seeing his own face and body, bright and clear as a mirror. He interpreted it saying: "Reflecting upon one's own form—this is the wonder of self-knowledge." Later he indeed became renowned throughout the realm.

#### 核心要点

- 全现己身=自知之明=大吉
- **身份分化**：君子→荣显，小人→康健
- 自知之明是征祥之本——能自观者必有成就
- 顾恺之典故：梦中自观如镜，后名重天下

#### 详细解说

「全现己身」是身体类梦象的首条，也是形貌部的总纲。其核心思想是「自知之明」——能够在梦中看清自己的人，必然具备自我认知的能力，这是成功的基础。

顾恺之（字虎头）是东晋著名画家，被称为「画绝」。他在梦中看见自己「睆然如鉴」（明亮如镜），这种自我观照的能力，正是他后来能够成为一代宗师的内在基础。

从心理学角度看，梦中能够看见完整的自己，意味着自我意识的完整和清醒，这是心理健康的重要标志。

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v7_001]` `[trigger: 梦见己身]` `[factor_trigger: dream_quan_xian_jishen AND dream_quanxianjishen AND zizhi_zhiming]` `[role: 主干]` 全现己身，大吉。人之相貌，谁能自知？自知之明，征祥备矣。 → 《梦林玄解·卷七》#全现己身
- `[ns_mlxj_v7_002]` `[trigger: 梦见己身]` `[factor_trigger: dream_quan_xian_jishen]` `[role: 典故]` 顾虎头梦自己面目肌发，睆然如鉴，后果名重天下。 → 《梦林玄解·卷七》#全现己身
- `[ns_mlxj_v7_003]` `[trigger: 形貌梦象]` `[factor_trigger: dream_shenti AND dream_toulu AND tou_xiangzheng AND dream_meaning]` `[role: 形貌体系]` 身体头颅等形貌梦象，头为诸阳之首。 → 《梦林玄解·卷七》#形貌"""
    normalized_text_zh: str = """"""
    subject: str = "1 全现己身（身体类首条·完整精校）"
    factor_refs: list = ['dream_quanxian_jishen', 'zizhi_zhiming', 'fanzh']
    
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
        l1_anchor="mlxj_v1.0.0_1_全现己身_身体类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
