"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654100
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
    semantic_id="zw_v1.0.0_安天马星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安天马星诀(SemanticEntry):
    """
    **主题**：论本生年支安天马。

#### 原文（断句）：

寅午戌人马居申，申子辰人马居寅，巳酉丑人马在亥，亥卯未人马在巳。

#### 分字分词释义：

- **寅午戌人**：生年地支为寅、午、...
    """
    
    original_text: str = """**主题**：论本生年支安天马。

#### 原文（断句）：

寅午戌人马居申，申子辰人马居寅，巳酉丑人马在亥，亥卯未人马在巳。

#### 分字分词释义：

- **寅午戌人**：生年地支为寅、午、戌的人，属于火局三合。
- **马居申**：天马安放在申宫。
- **申子辰人**：生年地支为申、子、辰的人，属于水局三合。
- **巳酉丑人**：生年地支为巳、酉、丑的人，属于金局三合。
- **亥卯未人**：生年地支为亥、卯、未的人，属于木局三合。
- **驿马**：古代传递官方文书的马匹，象征奔波、迁移、动态。

#### 安星规则：

- 寅午戌年生：天马在申
- 申子辰年生：天马在寅
- 巳酉丑年生：天马在亥
- 亥卯未年生：天马在巳

#### 口诀：驿马对冲（生年三合局的对宫）

#### 规范化释义（primary_lang_explained）：

寅午戌人马居申申子辰人马居寅巳酉丑人马在亥亥卯未人马在巳。

#### 完整对等诠释（secondary_lang_full·9天马）：

The Tianma rule derives a travelling “post‑horse” star from the birth‑year branch. The twelve branches are grouped into four triads—Yin–Wu–Xu, Shen–Zi–Chen, Si–You–Chou and Hai–Mao–Wei—and in each triad Tianma is placed in the house opposite the group’s main sector. Thus Yin–Wu–Xu years place Tianma in Shen, Shen–Zi–Chen years in Yin, Si–You–Chou years in Hai, and Hai–Mao–Wei years in Si. In every case the star stands across from the native’s year triad like a distant gate that calls for movement.

Tianma symbolises mobility, travel, relocation, running around and making a living through change. Where it falls in the chart shows the life arenas that are stirred up by journeys, transfers, changes of base or restless activity. When it combines well with Lucun, the classic “salary and horse galloping together” pattern appears, describing people who profit precisely by being on the move—through trade, logistics, consulting or itinerant work. When heavily afflicted, the same configuration can manifest as exhausting wandering, repeated uprooting or accidents on the road, so benefic or malefic support needs to be weighed with care.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 天马 | Tianma | 主奔波迁移的驿马星 | Post-horse mobility migration | star_tianma | existing |
| 驿马对冲 | Post-Horse Opposition | 三合局对宫定位法 | Positioning via triad opposition | algo_yimaduichong | new_candidate |
| 禄马交驰 | Salary-Horse Galloping | 禄存天马交会的大吉格 | Supreme wealth Lucun-Tianma | combo_lumajiaochi | existing |
| 动中生财 | Wealth-Through-Movement | 通过动态活动获得财富 | Generating wealth dynamically | concept_dongzhongshengcai | new_candidate |

#### 详细解说：

天马是紫微斗数中主奔波迁移的星曜，依据生年地支的三合局来定位。天马的位置揭示了命主在哪些领域容易有动态变化、远行迁移或频繁奔波。

**算法原理**：
- 十二地支分为四组三合局：寅午戌（火局）、申子辰（水局）、巳酉丑（金局）、亥卯未（木局）
- 天马总是落在三合局的对冲位置，象征"驿马对冲"的动态张力
- 这种对冲关系体现了"静极思动"的哲学思想

**天马的主要象征**：
- **正面象征**：远行发达、动中生财、迁移有利、出差旺运
- **负面象征**：奔波劳碌、居无定所、频繁变动、舟车劳顿

**重要格局**：
- **禄马交驰**：天马与禄存同宫或会照，主动中生财，是大吉格局
- **天马入迁移宫**：主远行发达，适合在外地或异国发展
- **天马逢煞**：主奔波辛苦，或有车祸、舟险等风险

#### 校勘与字词辨析（bilingual）：

- **"马居申"**：天马安放在申宫。英文："Tianma is placed in Shen palace"。
- **"驿马"**：古代传递官方文书的快马，引申为奔波、动态。英文："post-horse, symbolizing travel and mobility"。
- **"对冲"**：相隔六宫，呈180度对立关系。英文："opposition, 180-degree aspect"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："寅午戌马居申，申子辰马在寅，巳酉丑马亥上，亥卯未马在巳。"此口诀是最简洁的天马定位记忆法。
- **禄马交驰**：古人云"禄马交驰，发财如雷轰电掣"，形容禄存与天马同宫时财运迅猛的特点。
- **现代应用**：现代解读中，天马可延伸为出差频繁、异地工作、跨国业务、物流运输等与"动"相关的职业特点。"""
    normalized_text_zh: str = """"""
    subject: str = "安天马星诀"
    factor_refs: list = ['source_ref', 'rel_tianma_001', 'algo_yimaduichong', 'rel_tianma_002', 'star_tianma', 'rel_tianma_003', 'star_tianma', 'evi_tianma_001', 'star_tianma', 'rule_tianma_yinwuxu', 'evi_tianma_002', 'star_tianma', 'rule_tianma_shenzichen', 'concept_mobility', 'concept_dynamic_wealth']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_安天马星诀_001_L1",
    )
    version: str = "1.0.0"
