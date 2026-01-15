"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227994
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
    semantic_id="smth_v1.0.0_巳午未支义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 巳午未支义(SemanticEntry):
    """
    - **原文（source_text）**：
  巳者，四月，正阳而无阴也。自子至巳，阳之位，阳于是尽。又巳，起也，物毕尽而起。午者，阳尚未屈，阴始生而为主。又云：午，长也，大也，物至五月皆丰满长大也...
    """
    
    original_text: str = """- **原文（source_text）**：
  巳者，四月，正阳而无阴也。自子至巳，阳之位，阳于是尽。又巳，起也，物毕尽而起。午者，阳尚未屈，阴始生而为主。又云：午，长也，大也，物至五月皆丰满长大也。未，六月，木已种而成矣。又云：未，味也，物成而有味，与辛同意。

- **分字分词释义**：
  - **正阳而无阴**：纯阳而无阴。
  - **阳之位**：阳气的位置。
  - **阳于是尽**：阳气在此达到极致。
  - **物毕尽而起**：万物完全显现而起。
  - **阳尚未屈**：阳气还未屈服。
  - **阴始生而为主**：阴气开始生长并主导。
  - **丰满长大**：丰满高大。
  - **木已种而成**：木已结果成就。
  - **物成而有味**：事物成熟而有味道。

- **规范化释义（primary_lang_explained）**：
  巳是四月，纯阳而无阴。从子到巳是阳气的位置，阳气在此达到极致。又说：巳就是"起"，万物完全显现而兴起。午是阳气还未屈服，阴气开始生长并主导。又说：午就是"长"，也是"大"，万物到五月都丰满高大。未是六月，树木已经结果成就。又说：未就是"味"，事物成熟而有味道，与辛金同意。

- **完整对等诠释（secondary_lang_full）**：
  Si is the fourth month—pure yang with no yin. From Zi to Si is yang's domain; yang reaches its culmination here. Also said: Si means "rising"—myriad things fully manifest and arise. Wu is when yang has not yet yielded; yin begins to generate and dominate. Also said: Wu means "growing" and "great"—by the fifth month all things are plump and tall. Wei is the sixth month—trees have borne fruit and achieved completion. Also said: Wei means "flavor"—things mature and develop taste, sharing the same meaning as Xin Metal.

- **核心要点**：
  - 巳：四月，正阳无阴，阳之位尽，物毕尽而起
  - 午：五月，阳未屈阴始生，物丰满长大
  - 未：六月，木种而成，物成而有味

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_158]` `[trigger: 巳午未支义]` `[factor_trigger: si_branch AND wu_branch AND wei_branch AND summer_season]` `[role: 主干]` 巳者，四月，正阳而无阴也。午者，阳尚未屈，阴始生而为主。未，六月，木已种而成矣。未，味也，物成而有味。 → 《三命通会》卷一#巳午未支义

- **详细解说**：
  此条详解巳午未三支之义。巳对应四月，是纯阳之月，从子（一阳初生）到巳阳气达到顶点，"巳，起也"指万物完全显现兴起。午对应五月，阳气虽达极致但尚未屈服，阴气开始萌生并将主导，是阳极阴生的转折点，万物丰满长大。未对应六月，树木结果成就，"未，味也"指果实成熟有味，与秋季辛金（成熟有辛味）意义相通。巳午未三支完成了从阳极（巳）到阳极阴生（午）到成熟有味（未）的夏季过程。

- **校勘与字词辨析（双语）**：
  - **中文**："正阳"指纯阳。"阳于是尽"指阳气达极致。"与辛同意"指与辛金（成熟）意义相同。
  - **English**: "Pure yang" means completely yang; "yang reaches culmination" means yang qi reaches its peak; "same meaning as Xin" refers to sharing the maturation meaning with Xin Metal."""
    normalized_text_zh: str = """"""
    subject: str = "巳午未支义"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_巳午未支义_001_L1",
    )
    version: str = "1.0.0"
