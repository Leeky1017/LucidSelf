"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.842848
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
    semantic_id="mlxj_v1.0.0_1_登帝王之位_帝王类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1登帝王之位帝王类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

登帝王之位吉。凡此之梦，非平人所当能，当此者必帝王之种，有德有功之人也。宜详其何位，兆于何人，以定吉凶。如身居王位者，大为不祥。其在常人，或大象而小应，或贵...
    """
    
    original_text: str = """#### 原文（source_text）

登帝王之位吉。凡此之梦，非平人所当能，当此者必帝王之种，有德有功之人也。宜详其何位，兆于何人，以定吉凶。如身居王位者，大为不祥。其在常人，或大象而小应，或贵兆而贱征，或阳人而冥职，当随时随分，以占之。

#### 分字分词释义

- **登**：攀登 / 登临 / 即位 / 升迁
- **帝王之位**：九五之尊 / 天子之位 / 至高权位
- **帝王之种**：帝王血脉 / 龙种凤裔 / 有王气者
- **有德有功**：德行高尚 / 功业卓著 / 天命所归
- **大象小应**：梦象宏大而应验较小 / 降格应验
- **贵兆贱征**：梦兆尊贵而应验卑贱 / 反向应验
- **阳人冥职**：活人得阴司官职 / 死后受封 / 冥界应验

#### 规范化释义（primary_lang_explained）

梦见登上帝王之位，吉。凡是这样的梦，不是普通人所能应验的，能够当此梦者必是帝王之后裔，或有德有功之人。应当详细分辨梦见的是什么官位，应验在什么人身上，以此判定吉凶。

如果已经身居王位者梦此，则大为不祥。对于普通人而言，可能是「大象小应」（梦象宏大而应验较小），或「贵兆贱征」（梦兆尊贵而应验卑贱），或「阳人冥职」（活人得阴间官职），应当根据时势和身份来占断。

#### 完整对等诠释（secondary_lang_full）

Dreaming of ascending to the throne of an emperor is auspicious. Such a dream cannot be fulfilled by ordinary people—only those of imperial lineage or those with great virtue and merit can bear this portent. One should carefully examine what position was seen and to whom it applies to determine fortune or misfortune.

If one who already holds royal position dreams this, it is greatly inauspicious. For commoners, the dream may manifest as "grand symbol with minor fulfillment" (the dream is grand but the result is modest), "noble omen with humble verification" (the portent is noble but manifests humbly), or "living person receiving underworld office" (receiving a position in the realm of the dead). Interpretation should follow the circumstances and status of the dreamer.

#### 核心要点

- 登帝王位为人物梦象最高吉兆（限特定身份）
- **身份分化**：帝王种→大应，有德功者→中应，常人→小应或冥应
- **反向法则**：已居王位者梦此反为不祥
- **三种降格应验**：
  - 大象小应：梦象宏大，应验缩小
  - 贵兆贱征：梦兆尊贵，应验卑微
  - 阳人冥职：活人得阴间官职
- 核心原则：「随时随分」——因人因时因势而占

#### 详细解说

本条是人物部开篇第一条，以最尊贵的「登帝王之位」统领全部人物类梦象。

人物梦象的核心是「同气相感」——梦者的身份、德行、时势与所梦人物相匹配时，应验最大；反之则降格或反向应验。此条明确提出三种降格应验模式，为后续解梦提供了重要的方法论：

1. **大象小应**：梦见登帝位，常人可能只是升小官、得小利
2. **贵兆贱征**：梦见尊贵之象，可能应验在卑微之事
3. **阳人冥职**：活人梦得官位，可能是死后才受封

这体现了梦学的辩证思维——同一梦象，因人而异，不可执一而论。

#### 典故

- **宋元公梦**：宋元公梦太子栾即位于庙，己与平公服而相之。旦召六卿告之，后果卒于曲棘之地。此为「已居王位者梦此不祥」之验。

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v4_001]` `[trigger: 梦登帝位]` `[factor_trigger: dream_deng_diwang AND dream_dengdiwang AND dream_diwang AND diwang_dexing]` `[role: 主干]` 登帝王之位吉。凡此之梦，非平人所当能，当此者必帝王之种，有德有功之人也。 → 《梦林玄解·卷四》#登帝王之位
- `[ns_mlxj_v4_002]` `[trigger: 梦登帝位]` `[factor_trigger: dream_deng_diwang]` `[role: 条件约束]` 如身居王位者，大为不祥。其在常人，或大象而小应，或贵兆而贱征，或阳人而冥职。 → 《梦林玄解·卷四》#登帝王之位
- `[ns_mlxj_v4_003]` `[trigger: 宋元公梦]` `[factor_trigger: dream_deng_diwang]` `[role: 典故]` 宋元公梦太子栖即位于庙，己与平公服而相之，后果卒于曲棘。 → 《梦林玄解·卷四》#登帝王之位
- `[ns_mlxj_v4_004]` `[trigger: 圣贤梦象]` `[factor_trigger: dream_kongzi AND dream_shengxian AND jiemeng_jiangge]` `[role: 圣贤类]` 梦孔子、圣贤、借梦讲格等梦象。 → 《梦林玄解·卷四》#圣贤"""
    normalized_text_zh: str = """"""
    subject: str = "1 登帝王之位（帝王类首条·完整精校）"
    factor_refs: list = ['dream_deng_diwang', 'jiemeng_daxiaoxiaoying', 'jiemeng_guizhaojianzhen', 'jiemeng_yangren_mingzhi']
    
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
        l1_anchor="mlxj_v1.0.0_1_登帝王之位_帝王类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
