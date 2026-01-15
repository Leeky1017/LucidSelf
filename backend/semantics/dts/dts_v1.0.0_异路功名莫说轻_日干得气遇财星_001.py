"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997776
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
    semantic_id="dts_v1.0.0_异路功名莫说轻_日干得气遇财星_001",
    book_id="dts",
    engine_id="bazi"
)
class 异路功名莫说轻日干得气遇财星(SemanticEntry):
    """
    - **原文（source_text）**：
  异路功名莫说轻，日干得气遇财星。

- 分字分词释义：
  - 异路：非正途、非科举之路径。
  - 功名：成就与名位。
  - 莫说轻：不可轻视。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  异路功名莫说轻，日干得气遇财星。

- 分字分词释义：
  - 异路：非正途、非科举之路径。
  - 功名：成就与名位。
  - 莫说轻：不可轻视。
  - 日干得气：日主有根气、身强能任。
  - 遇财星：逢遇清旺之财星。

- 原注（原文注解）：
 
- 规范化释义（primary_lang_explained）：
  本句指出，非常规路径的功名不可轻视，其成就往往来自“日干得气、财星成门户”的组合——身有根气，又遇清旺之财，财能通官，便能在商贾、技艺、专业等异路上立身成名。

- **核心要点**：
  - 异路功名以“清+气+财”为本：清气不浊、日主得气、财星通路；
  - 财星须成门户、通官而不与官相拗；
  - 不可一味贬低非常规出身与路径。

- 详细解说：
  与前几句偏重科第、秀才等正途功名不同，此句强调：即便不走科举或官场，只要财星清旺、有门户可依，并能通官生印，同样可以在异路上取得不轻的名位。这里的“异路”可指经商、专业技术、艺能等路径，关键仍在格局是否清纯、承载是否稳固，而不在形式是否合乎传统标准。

- 校勘与字词辨析：
  - “异路”：指相对于科举正途的其他成名道路，并非旁门邪道。

- 原注（原文注解）：
  　　财星成门户、通官有清旺之气者，得异路功名；反之官财相拗则难。

- 白话综解（总论）：
  出身之辨，贵在“清+静+承+路”。清静安顿，方可立名；有路有承，方能发科与异路功名。

- 分字分词释义（总论）：
  - 科第/黄榜：科举取第、正途功名。
  - 元机：暗中之关键机括。
  - 异路功名：非常规路径之成名。

- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 出身 | Origin/Status (Chu-Shen) | 出身背景 | Family background/Status | chushen_origin_status | new_candidate |
| 科第 | Examination Success (Ke-Di) | 科举功名 | Academic success | kedi | new_candidate |
| 元机 | Hidden Mechanism (Yuan-Ji) | 玄机 | Subtle mechanism | yuanji | new_candidate |
| 黄榜 | Yellow List (Success) | 金榜题名 | Honor roll | keju_rank | new_candidate |
| 异路功名 | Irregular Path Success | 非正途功名 | Alternative success | alternate_achievement | new_candidate |
| 门户 | Gate/Household (Men-Hu) | 立身之地 | Established foundation | menhu_foundation | new_candidate |

- **次语种完整诠释（secondary_lang_full）**:  
  Chu-Shen (Origin/Status) theory: "Examination Success" (Ke-Di) requires "Clear Qi" (Qing-Qi) and "Hidden Mechanism" (Yuan-Ji). Even with "Turbid Qi" (Zhuo-Qi), if "Settled Quietly" (Qing-De-Jing-Shi), one can succeed. Irregular Path (Yi-Lu) requires Wealth creating a "Gate" (Men-Hu) and connecting to Official."""
    normalized_text_zh: str = """"""
    subject: str = "异路功名莫说轻，日干得气遇财星。"
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_异路功名莫说轻_日干得气遇财星_001_L1",
    )
    version: str = "1.0.0"
