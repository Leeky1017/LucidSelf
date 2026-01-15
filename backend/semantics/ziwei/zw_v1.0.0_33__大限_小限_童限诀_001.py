"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654326
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
    semantic_id="zw_v1.0.0_33__大限_小限_童限诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 33大限小限童限诀(SemanticEntry):
    """
    - 分字分词释义：

  - **大限**：十年一宫的大运周期，决定人生阶段性运势。
  - **小限**：年年一宫的流年运程，决定当年具体运势。
  - **童限**：15岁以下的童年限运，有固定宫...
    """
    
    original_text: str = """- 分字分词释义：

  - **大限**：十年一宫的大运周期，决定人生阶段性运势。
  - **小限**：年年一宫的流年运程，决定当年具体运势。
  - **童限**：15岁以下的童年限运，有固定宫位顺序。
  - **阳男阴女**：阳年生男或阴年生女，大限从命前宫顺数。
  - **阴男阳女**：阴年生男或阳年生女，大限从命后宫逆数。
  - **顺数逆数**：顺时针或逆时针推算宫位。
  - **三合起点**：小限起点按生年支的三合局确定。

#### 大限诀：

- 阳男阴女：从命前一宫（父母宫）起
- 阴男阳女：从命后一宫（兄弟宫）起
- 每宫管10年

#### 小限诀：

- 男命顺数，女命逆数
- 寅午戌人：辰宫起
- 申子辰人：戌宫起
- 巳酉丑人：未宫起
- 亥卯未人：丑宫起

#### 童限诀：

1岁命宫、2岁财帛、3岁疾厄、4岁妻妾、5岁福德、6岁官禄，余年顺流行，15岁回命宫。

#### 完整对等诠释（secondary_lang_full·31-33限运诀）：

  The limit-period system divides life into nested time frames. Daxian (Major Limits) span ten years each. For yang-male and yin-female natives, the first Daxian starts from the palace preceding the Life Palace (Parents Palace) and advances clockwise; for yin-male and yang-female natives, it starts from the palace following the Life Palace (Siblings Palace) and moves counter-clockwise. Xiaoxian (Minor Limits) operate year by year: males count forward, females count backward. The starting palace depends on the native's year-branch trio—Yin-Wu-Xu natives begin from Chen, Shen-Zi-Chen from Xu, Si-You-Chou from Wei, and Hai-Mao-Wei from Chou. Tongxian (Childhood Limits) apply to the first fifteen years of life with a fixed sequence: age one in the Life Palace, age two in Wealth, age three in Health, age four in Spouse, age five in Fortune, age six in Career, then continuing forward until age fifteen returns to the Life Palace. Together these three limit layers allow the astrologer to zoom in from decade-level trends to annual and even childhood-specific influences."""
    normalized_text_zh: str = """"""
    subject: str = "33. 大限、小限、童限诀"
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_33__大限_小限_童限诀_001_L1",
    )
    version: str = "1.0.0"
