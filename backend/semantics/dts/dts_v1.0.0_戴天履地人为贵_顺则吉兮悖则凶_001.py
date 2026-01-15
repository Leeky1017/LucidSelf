"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932682
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
    semantic_id="dts_v1.0.0_戴天履地人为贵_顺则吉兮悖则凶_001",
    book_id="dts",
    engine_id="bazi"
)
class 戴天履地人为贵顺则吉兮悖则凶(SemanticEntry):
    """
    - 原文（source_text）：
  戴天履地人为贵，顺则吉兮悖则凶。

- 原注（原文注解）：
  　　凡物莫不得五行，而戴天履地，惟人得五行之全，故为贵，其有吉凶之不一者，以其得于五行之顺与逆...
    """
    
    original_text: str = """- 原文（source_text）：
  戴天履地人为贵，顺则吉兮悖则凶。

- 原注（原文注解）：
  　　凡物莫不得五行，而戴天履地，惟人得五行之全，故为贵，其有吉凶之不一者，以其得于五行之顺与逆也。

- 分字分词释义：
  - 戴：承戴、仰承（承天）。
  - 天：天道、天时。
  - 履：践履、踏着.
  - 地：地道、地气.
  - 人：人道、人的主体.
  - 为贵：为最可贵、为要.
  - 顺：顺应、随顺其理与时.
  - 吉：吉利、顺遂.

- 规范化释义（primary_lang_explained）：
  人贵在承天时、履地气而后立身.顺应天时地利，人事才吉；若违背其理，必见不利.命理断事，首重“顺势而为”。

- **次语种完整诠释（secondary_lang_full）**：  
  Humans are distinguished by wearing Heaven (Dai Tian: receiving celestial timing and seasonal mandate) and treading upon Earth (Lü Di: grounding in terrestrial structure and environmental configuration). Among all beings, only humans receive the full complement of Five Elements, thereby occupying the pivotal position within the Triad of Heaven-Earth-Human. Auspiciousness arises when one acts in accordance (Shun) with the natural order and current momentum of qi; inauspiciousness follows when one contravenes (Bei) this alignment. This principle elevates destiny analysis beyond static chart reading—the same natal structure may yield divergent outcomes depending on whether the individual's choices harmonize with or oppose the timing-structure matrix. Therefore, judgment requires assessing not only the chart's inherent configuration but also the degree to which behavior aligns with favorable pathways.

- **核心要点**：
  - 戴天指承接天时、天道的运行节律
  - 履地指践履地气、立足于地支环境结构
  - 人在三才（天地人）中居于可主动调节的枢纽位置
  - 顺应天时地利则吉，违背结构大势则凶
  - 同一命局因顺逆选择不同可产生截然不同的结果
  - 论命不可只看静态盘面，须结合时势与行为选择

- **详细解说**：
  本条确立"三才定位"与"顺逆框架"两大核心概念。"戴天履地"喻人在天地之间的独特位置：承接天时（节气、历法、岁运），践履地气（地支布局、环境场域），既受天地结构塑造，又能在五行资源间调配取舍。"顺则吉、悖则凶"揭示命理判断的动态性：顺是顺着五行常理与当下气机的方向用神，悖是逆着大势与自身结构硬行。关键在于：判断吉凶不能只看命局一张盘的静态结构，还要看命主的选择是否与天时地利协同。实占时，先判日主与月令的顺逆关系，顺则佐助相生，逆则设制或通关泄化，并结合岁运验证。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_007]` `[trigger: 日主得令得地]` `[factor_trigger: shun_bei_pattern]` `[role: 主干]` 日主得令得地，顺势而行为上策，不宜强制克制。 → 《滴天髓·通天论》#第3条
  - `[ns_dts_008]` `[trigger: 日主失令有救]` `[factor_trigger: shun_bei_pattern]` `[role: 条件分支]` 日主失令而局中有救应时，顺中有逆、逆中有顺，须察情义轻重。 → 《滴天髓·通天论》#第3条
  - `[ns_dts_009]` `[trigger: 三才定位]` `[factor_trigger: sancai_alignment]` `[role: 主干依赖]` 人居天地间，顺天时则吉，悖地利则凶，关键在识别何为当下之"顺"。 → 《滴天髓·通天论》#第3条
  - `[ns_dts_101]` `[trigger: 顺逆与结果]` `[factor_trigger: shun_bei_pattern]` `[role: 主干依赖]` 同一命局因顺逆选择不同，可产生截然不同的结果。 → 《滴天髓·通天论》#第3条
  - `[ns_dts_102]` `[trigger: 静态盘局不足]` `[factor_trigger: sancai_alignment]` `[role: 总结]` 论命不可只看静态盘面，须结合时势与行为选择方能定吉凶。 → 《滴天髓·通天论》#第3条"""
    normalized_text_zh: str = """"""
    subject: str = "戴天履地人为贵，顺则吉兮悖则凶."
    factor_refs: list = ['daitian_alignment', 'ludi_grounding', 'sancai_alignment', 'shun_bei_pattern', 'shun_bei_pattern', 'yongshen']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_戴天履地人为贵_顺则吉兮悖则凶_001_L1",
    )
    version: str = "1.0.0"
