"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997481
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
    semantic_id="dts_v1.0.0_能知衰旺之真机_其于立命之奥_思过半矣_001",
    book_id="dts",
    engine_id="bazi"
)
class 能知衰旺之真机其于立命之奥思过半矣(SemanticEntry):
    """
    - **原文（source_text）**：
  能知衰旺之真机，其于立命之奥，思过半矣。

- 原注（原文注解）：
  　　旺则宜泄宜伤，衰则喜帮喜助，子平之理也，然旺中有衰者存，不可损也。衰中有旺...
    """
    
    original_text: str = """- **原文（source_text）**：
  能知衰旺之真机，其于立命之奥，思过半矣。

- 原注（原文注解）：
  　　旺则宜泄宜伤，衰则喜帮喜助，子平之理也，然旺中有衰者存，不可损也。衰中有旺者存，不可益也。旺之极者不可损，以损在其中矣，衰之极者不可益，以在其中矣。至于所当损者而损之反凶，所当益者而益之反害，此中真机皆能知之，何难于立命之微奥乎。

- 分字分词释义：
  - 衰旺：五行强弱之度，不仅看数量，更看令、根、助、制；
  - 真机：表象之下的真实运作机制；
  - 宜泄宜伤：对旺者以泄、以伤以去其过；
  - 喜帮喜助：对衰者以帮、以生以补其不足。

- **规范化释义（primary_lang_explained）**：
  “衰旺论”的关键在“不执死法”：日主或某用神虽旺，一味泄伤未必吉；虽衰，一味帮扶亦未必利。要看“旺中有衰”“衰中有旺”的内里：极旺者本身已具自损之机，再损即反伤；极衰者反而内藏一线元气，再助则爆裂。能识此等微妙，立命之奥理已明其大半。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 衰旺 | Decline-Prosperity (Shuai-Wang) | 强弱之度 | Degree of strength/weakness | shuaiwang | existing |
| 真机 | True Mechanism | 内在运作机理 | Inner operational logic | zhenji | new_candidate |
| 宜泄宜伤 | Suitable to Drain/Hurt | 旺者宜制 | Prosperous should be controlled | yi_xie_yi_shang | new_candidate |
| 喜帮喜助 | Joy to Help/Assist | 衰者喜扶 | Declining likes support | xi_bang_xi_zhu | new_candidate |
| 旺中有衰 | Prosperous containing Decline | 旺而虚 | Prosperous but hollow | wang_zhong_shuai | new_candidate |
| 衰中有旺 | Declining containing Prosperity | 衰而有根 | Declining but rooted | shuai_zhong_wang | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Shuai-Wang (Decline-Prosperity) true mechanism: not just surface strength. Prosperous (Wang) usually needs draining (Xie/Shang), Declining (Shuai) usually needs helping (Bang/Zhu). BUT: Wang-contains-Shuai (don't drain), Shuai-contains-Wang (don't help), Extreme-Wang (don't drain), Extreme-Shuai (don't help). Knowing when to act contrary to the rule is the secret (真机)."""
    normalized_text_zh: str = """"""
    subject: str = "能知衰旺之真机，其于立命之奥，思过半矣。"
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
        l1_anchor="dts_v1.0.0_能知衰旺之真机_其于立命之奥_思过半矣_001_L1",
    )
    version: str = "1.0.0"
