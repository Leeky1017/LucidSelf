"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699418
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
    semantic_id="zw_v1.0.0_杨孔目命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 杨孔目命(SemanticEntry):
    """
    - 分字分词释义：

  - **机月同梁**：天机太阴天同天梁四星会合，主作吗人，适合公职。
  - **命垣坐寅申**：命宫坐寅宫或申宫，为机月同梁的典型坐宫。
  - **科禄加会**：化科化禄...
    """
    
    original_text: str = """- 分字分词释义：

  - **机月同梁**：天机太阴天同天梁四星会合，主作吗人，适合公职。
  - **命垣坐寅申**：命宫坐寅宫或申宫，为机月同梁的典型坐宫。
  - **科禄加会**：化科化禄同会命宫，主正途功名。
  - **若无羊刃火铃合照**：若未被擎羊、火星、铃星等重凶冲破，可循正途取得功名。
  - **二限入地网**：大小限同时行入天罗地网之地，主凶险。
  - **铃星太岁到命垣**：铃星与太岁同入命垣，形成多重凶局，主倒寿。
  - **阳男木三局**：杨孔目命盘的五行局数，木三局主生发条理。

- **原文（source_text）**：  
  杨孔目命。阳男木三局。机月同梁，作吏人，命垣坐寅申之地，科禄加会，若无羊刃、火铃合照，乃主正路功名，贵题大小。二限入于地网，怕逢铃星，又且太岁到命垣，故主倒寿。

- **规范化释义（primary_lang_explained）**：  
  此命为阳男木三局，命宫成「机月同梁」之格，本身适合从事吏职、公职，一生以文书、条理与协调见长。命垣坐寅申之地，又得科星、禄星加会，若未被羊刃、火铃等重凶冲破，本可循正途取得功名，由小吏而至清要之职。原文却指出，后期两限行入天罗地网之地，又逢铃星与太岁入命垣，形成多重凶局，使原本清贵安稳的吏人命在寿元上被截短，成为「格局端正而限运倒寿」的典型命例。

- **完整对等诠释（secondary_lang_full）**：  
  This chart belongs to a Yang Wood native with the "Ji‑Moon‑Liang" configuration, a classic pattern for civil and administrative officials. The Life palace lies on the Yin‑Shen axis and is strengthened by Academic and Salary stars: in a quiet form this supports careers built on paperwork, procedure and institutional order, allowing the native to rise step by step through the bureaucracy. As long as harsh stars such as Yang Blade or Fire Bell do not strike the configuration, it represents clean and proper advancement. The text, however, describes a later turn: both major and minor periods move into the Net of Heaven and Earth, and when Fire Bell coincides with Tai Sui entering the Life palace, a dense web of malefics forms. At that point the otherwise upright official faces a shortened lifespan, illustrating how a sound structural pattern can still be cut off by hostile timing.

- **核心要点**：  
  1. 机月同梁与科禄加会，主循规蹈矩、以文书与行政见长的吏人命。  
  2. 若不见羊刃、火铃等重凶，本可成稳健的清贵格。  
  3. 当两限入地网又逢铃星、太岁入命垣时，寿命面临「倒寿」的强烈风险。

- **叙事素材（narrative_snippets）**：
  - **机月同梁吏命**："机月同梁，作吏人，命垣坐寅申之地，科禄加会"，杨孔目命主适合公务体系、以文书条理立身。
  - **正路功名**："若无羊刃、火铃合照，乃主正路功名，贵题大小"，说明格局本可循正途由小吏而升清要。
  - **地网倒寿**："二限入于地网，怕逢铃星，又且太岁到命垣，故主倒寿"，两限入网又遇铃星太岁，为清官早亡的应期结构。
  - **现代应用**：体制内稳健型人士，在事业进入相对稳定阶段时，仍需留意制度巨变或突发事件年份，避免因过度忠诚或加班透支而把寿元赔进体制风险里。"""
    normalized_text_zh: str = """"""
    subject: str = "杨孔目命"
    factor_refs: list = ['pattern_jiyuetongliang', 'position_mingyuan_yinshen', 'pattern_kelu_jiahui', 'malefic_yanghuoling', 'timing_erxian_diwang', 'result_daoshou']
    
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
        l1_anchor="zw_v1.0.0_杨孔目命_001_L1",
    )
    version: str = "1.0.0"
