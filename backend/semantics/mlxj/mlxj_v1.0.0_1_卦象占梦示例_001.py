"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.845123
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
    semantic_id="mlxj_v1.0.0_1_卦象占梦示例_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1卦象占梦示例(SemanticEntry):
    """
    #### 乾卦

**乾为天，属金**。六龙御天之卦，广大包容之象。

判曰：乾者，健也。大哉乾元，荫覆无偏。元运造化，万物资始。云行雨施，变化不言。东西任意，南北安然。

爻辞要点：
- 初九：潜龙...
    """
    
    original_text: str = """#### 乾卦

**乾为天，属金**。六龙御天之卦，广大包容之象。

判曰：乾者，健也。大哉乾元，荫覆无偏。元运造化，万物资始。云行雨施，变化不言。东西任意，南北安然。

爻辞要点：
- 初九：潜龙勿用
- 九二：见龙在田，利见大人
- 九三：君子终日乾乾，夕惕若，厉，无咎
- 九四：或跃在渊，无咎
- 九五：飞龙在天，利见大人
- 上九：亢龙有悔
- 用九：见群龙无首，吉

#### 坤卦

**坤为地，属土**。生载万物之卦，博厚无疆之象。

判曰：坤者，顺也，乃顺成天，万物资生。用动则浊，用静则清。所作有顺，万物皆成。

#### 坎卦

**坎为水，属水**。船渡重难之卦，外虚中实之象。

判曰：坎者，陷也。逢流则注，遇坎则止。出入艰险，随坎不已。阴愁伏慝，共相谋计，千里辞家，始免迍否。

#### 离卦

**离为火，属火**。天官赐福之卦，光明显贵之象。

判曰：离者，丽也，光明美丽，不利出师。二鸟同飞，雄失其雌，婚姻未合，易起官非，口舌柏尚，财散人离。"""
    normalized_text_zh: str = """"""
    subject: str = "1 卦象占梦示例"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="mlxj_v1.0.0_1_卦象占梦示例_001_L1",
    )
    version: str = "1.0.0"
