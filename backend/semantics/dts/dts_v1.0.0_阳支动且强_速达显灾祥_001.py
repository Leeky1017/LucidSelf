"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997145
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
    semantic_id="dts_v1.0.0_阳支动且强_速达显灾祥_001",
    book_id="dts",
    engine_id="bazi"
)
class 阳支动且强速达显灾祥(SemanticEntry):
    """
    - **原文（source_text）**：
  阳支动且强，速达显灾祥。

- 原注（原文注解）：
  　　子，寅，辰，午，申，戌，阳也，其性动，其势强，其发至速，其灾祥至显。

- 分字分词释义：...
    """
    
    original_text: str = """- **原文（source_text）**：
  阳支动且强，速达显灾祥。

- 原注（原文注解）：
  　　子，寅，辰，午，申，戌，阳也，其性动，其势强，其发至速，其灾祥至显。

- 分字分词释义：
  - 阳支：地支之阳者（子、寅、辰、午、申、戌）。
  - 动：性动、主动、易感发。
  - 强：势强、有力道。
  - 速达：应期来得快，反应迅疾。
  - 显：明显、显著。
  - 灾祥：灾与祥（凶与吉）。

- **规范化释义（primary_lang_explained）**：
  阳性地支性质主动而强劲，故事象来得快，吉也快显、凶也快见。断运、断流年时，阳支位的冲会刑合，往往呈现为速发速应的表现。



- **次语种完整诠释（secondary_lang_full）**:  
  Yang branches are the six active Earthly Branches (Zi, Yin, Chen, Wu, Shen, Xu). They represent strongly dynamic qi that moves quickly and shows its effects on the surface. When these branches are stirred, both auspicious and inauspicious events tend to manifest fast, often within the same year or even within a few months. In timing work, clashes, combinations, punishments and meetings that involve Yang branches should therefore be treated as fast-response triggers, in sharp contrast to Yin branches, whose effects usually build up slowly over longer cycles.

- **核心要点**：
  - 阳支六位：子、寅、辰、午、申、戌，性动势强
  - 速达显灾祥：阳支应事快、吉凶迹象来得迅速明显
  - 断应期：遇冲合刑会于阳支，多以"速达"推断应期
  - 取用策略：阳支旺时宜顺势或设制，避免硬逆

- **详细解说**：
  阳支是地支中主动外向、力道强劲的六位（子寅辰午申戌）。其特质在"动且强"：不守静待，易感发、易冲突、易展现。应事快、反应快，吉凶迹象来得明显且迅速。断运断流年时，阳支位的冲会刑合往往呈现速发速应的表现。关键在识别阳支位置与岁运交互，据此推算应期，以月日为准而非年。阳支过旺时需考虑是否设制或顺势。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_055]` `[trigger: 阳支被岁运冲动]` `[factor_trigger: yangzhi_trigger==被岁运冲合刑 AND event_speed_index==以月季计]` `[role: 主干]` 阳支主动主变，逢冲逢会则速发，吉凶立见。 → 《滴天髓·地支论》#阳支
  - `[ns_dts_056]` `[trigger: 流年大运冲阳支]` `[factor_trigger: yangzhi_trigger==被岁运冲合刑 AND event_speed_index==以月季计]` `[role: 主干依赖]` 大运流年冲动阳支时，应期宜以月日为准，速达显应。 → 《滴天髓·地支论》#阳支
  - `[ns_dts_057]` `[trigger: 阳支动势强]` `[factor_trigger: yangzhi_momentum==强动 AND event_speed_index==以月季计]` `[role: 条件分支]` 阳支动而有力，灾祥显现迅捷，需及时应对不可迟疑。 → 《滴天髓·地支论》#阳支
  - `[ns_dts_133]` `[trigger: 阳支旺极无制]` `[factor_trigger: yangzhi_control_need==高 AND yangzhi_momentum==强动]` `[role: 例外处理]` 阳支过旺而无制时，速达之应或成过激之动，须防失控。 → 《滴天髓·地支论》#阳支
  - `[ns_dts_134]` `[trigger: 断阳支应期]` `[factor_trigger: event_speed_index==以月季计 AND yangzhi_trigger==被岁运冲合刑]` `[role: 总结]` 阳支断事以速为主，冲会刑合之应期宜取月日，不宜年论。 → 《滴天髓·地支论》#阳支"""
    normalized_text_zh: str = """"""
    subject: str = "阳支动且强，速达显灾祥。"
    factor_refs: list = ['dizhi_yangzhi_group', 'yangzhi_dong_qiang', 'suda_yingqi', 'xian_zaixiang']
    
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
        l1_anchor="dts_v1.0.0_阳支动且强_速达显灾祥_001_L1",
    )
    version: str = "1.0.0"
