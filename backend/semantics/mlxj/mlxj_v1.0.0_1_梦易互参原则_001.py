"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.845115
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
    semantic_id="mlxj_v1.0.0_1_梦易互参原则_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1梦易互参原则(SemanticEntry):
    """
    #### 原文（source_text）

魏咸阳公高伯恭曰：人之祸福，相为倚伏，魂气阖辟，恒兆几微。周家占梦有官，左氏妖梦首纪。然天人召感之际，违应靡常，古法既亡，前贤云逝，岂一涉梦测之以臆，遂能剖...
    """
    
    original_text: str = """#### 原文（source_text）

魏咸阳公高伯恭曰：人之祸福，相为倚伏，魂气阖辟，恒兆几微。周家占梦有官，左氏妖梦首纪。然天人召感之际，违应靡常，古法既亡，前贤云逝，岂一涉梦测之以臆，遂能剖决吉凶，若影之随形，声之答响邪？

是故昔人遇美恶之梦，必占之易，定其卦体，审其爻辞，决其休咎，以梦之兆，准易之象，取易之占，察梦之机。凶袭则凶，吉袭则吉；梦吉筮凶，梦凶筮吉，即本德以观变，庶神魂之动现非虚，祸福之转旋可睹。

#### 规范化释义（primary_lang_explained）

魏咸阳公高伯恭说：人的祸福相互依附，魂气开合之间，恒常显露细微征兆。周朝设有占梦官，《左传》首记妖梦。然而天人感应之际，应验与否并无定规。古法已亡、前贤已逝，岂能仅凭一次梦境就臆测判断吉凶，如影随形、如声应响那样准确？

因此古人遇到好梦或恶梦，必以《易经》占卜：确定卦体、审视爻辞、判断休咎。以梦之兆准于易之象，取易之占察梦之机。凶兆相袭则凶，吉兆相袭则吉；若梦吉而筮凶、或梦凶而筮吉，则应本于德行观察变化，如此才能见到神魂显现并非虚妄、祸福转旋可以预见。

#### 核心要点

- **方法论**：梦易互参
- **操作流程**：遇梦 → 占易 → 定卦体 → 审爻辞 → 决休咎
- **判断规则**：
  - 凶袭凶：梦凶+筮凶 = 凶
  - 吉袭吉：梦吉+筮吉 = 吉
  - 梦吉筮凶/梦凶筮吉：本德以观变

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v27_003]` `[trigger: 梦易互参]` `[factor_trigger: dream_yijing_method]` `[role: 方法论]` 以梦之兆，准易之象，取易之占，察梦之机。凶袭则凶，吉袭则吉。 → 《梦林玄解·卷二十七》#省梦须占易象说"""
    normalized_text_zh: str = """"""
    subject: str = "1 梦易互参原则"
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
        l1_anchor="mlxj_v1.0.0_1_梦易互参原则_001_L1",
    )
    version: str = "1.0.0"
