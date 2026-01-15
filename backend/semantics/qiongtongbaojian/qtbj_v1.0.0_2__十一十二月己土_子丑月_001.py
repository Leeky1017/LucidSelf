"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597144
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
    semantic_id="qtbj_v1.0.0_2__十一十二月己土_子丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2十一十二月己土子丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  或一派癸，不见比劫，此为从才，反主富贵，虽不科甲，恩误有之。若见比争，平常人物，妻子主事。从才者，木妻、火子。
  或一派戊己，取甲制之，甲透者，富贵...
    """
    
    original_text: str = """- **原文（source_text）**：
  或一派癸，不见比劫，此为从才，反主富贵，虽不科甲，恩误有之。若见比争，平常人物，妻子主事。从才者，木妻、火子。
  或一派戊己，取甲制之，甲透者，富贵。
  或一派辛庚，须用丙火，还须丁火为助。丙藏、富贵奇特之命。

- **分字分词释义**：
  - **从才**：从财格 / 水多无比 / 变格
  - **恩误**：皇帝封赠 / 异途 / 吉象
  - **比争**：比劫争财 / 有比劫 / 凶象
  - **妻子主事**：妻子当家作主 / 财旺身弱 / 凶象
  - **奇特之命**：奇特的命 / 伤官配印 / 吉象

- **规范化释义（primary_lang_explained）**：
  （子丑月同论湿寒，重点在于从格与制化）
  如果一派癸水（财），不见比肩劫财，这是“从财格”，反主富贵，虽然不是科甲出身，也有恩诰（封典/异途）。如果见到比劫争财，是平常人物，妻子主事。从财格的人，木为妻火为子（？从财通常水为妻木为子，此处原文“木妻火子”疑为误，或者指从财后喜行木火运？待考。一般从财以所从之神为妻）。
  如果一派戊己土（比劫），取甲木制约，甲木透出者，富贵（身强用官）。
  如果一派辛庚金（食伤），必须用丙火（制金暖土），还须丁火辅助。丙火藏支，是富贵奇特的命（伤官配印，金水伤官喜见官？土金伤官喜印）。

- **完整对等诠释（secondary_lang_full）**：
  If there is a mass of Gui Water without Parallels/Rob Wealth, it is "Follow Wealth", conversely implying wealth and nobility. Though not Civil Service, one receives honors. If Parallels contend, one is ordinary, wife ruling the house. For Follow Wealth, Wood is Wife, Fire is Child (textual anomaly?).
  If there is a mass of Wu/Ji Earth, take Jia to control. If Jia reveals, wealth and nobility.
  If there is a mass of Xin/Geng Metal, must use Bing, and need Ding to assist. If Bing hides, it is a strangely wealthy and noble life.

- **核心要点**：
  - **从财**：水旺无土，从财贵。
  - **身旺**：土多用甲。
  - **伤官**：金多用丙（佩印）。

- **详细解说**：
  - 子月财旺，易从财。
  - 丑月湿土，金之库，易成金局（食伤），故喜火。
  - 无论何种格局，冬土离不开“丙”字，即使从财，若无暖气，亦恐虽富而寿促或孤寒。"""
    normalized_text_zh: str = """"""
    subject: str = "2. 十一十二月己土（子丑月）"
    factor_refs: list = ['en_gao', 'unique_destiny', 'wife_controls']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__十一十二月己土_子丑月_001_L1",
    )
    version: str = "1.0.0"
