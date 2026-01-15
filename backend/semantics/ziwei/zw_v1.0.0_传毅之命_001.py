"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699347
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
    semantic_id="zw_v1.0.0_传毅之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 传毅之命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄加会**：化权化禄同会命宫，主终身福厚。
  - **擎羊逢力士**：擎羊与力士同宫，凶化吉。
  - **命垣坐火位**：命宫得火位，主心性明朗、气势充盈。
 ...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄加会**：化权化禄同会命宫，主终身福厚。
  - **擎羊逢力士**：擎羊与力士同宫，凶化吉。
  - **命垣坐火位**：命宫得火位，主心性明朗、气势充盈。
  - **大限天使夹地**：大限游于天使又夹地网，主凶险。
  - **天伤天刑**：天伤天刑齐聚，主寿终。
  - **终身福厚**：权禄加会格局的主要效应。
  - **阳男火六局**：传毅命盘的五行局数，火六局主热情学识。

- **原文（source_text）**：  
  传毅之命。阳男火六局。权禄加会，擎羊逢力士，不得十分富贵，亦为终身福厚之论。命垣喜坐火位，皆为吉兆。直到大限游于天使，夹地小限七十一，又逢天伤天刑，故此寿难过。

- **规范化释义（primary_lang_explained）**：  
  传毅命属阳男火六局，权禄加会、擎羊逢力士，虽不十分富贵亦终身福厚。命垣坐火位为吉。大限游于天使、夹地，小限七十一逢天伤天刑，故寿难过而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Fu Yi's Yang male Fire Sixth chart has Authority‑Salary converge, Blade meets Warrior—not extreme wealth but lifelong blessings. Life sits on Fire position, auspicious. Major travels to Envoy, flanks Earth; minor at 71 meets Wound‑Punishment. Lifespan cannot pass.

- **核心要点**：  
  1. 权禄加会、擎羊逢力士，终身福厚。  
  2. 命垣坐火位为吉。  
  3. 大限天使夹地、小限天伤天刑，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **福厚之命**："权禄加会，擎羊逢力士，不得十分富贵，亦为终身福厚之论"，传毅命主虽非极贵，却一生衣食无忧。
  - **火位为吉**："命垣喜坐火位，皆为吉兆"，命宫得火位，象征心性明朗、气势充盈。
  - **天伤天刑**："直到大限游于天使，夹地小限七十一，又逢天伤天刑，故此寿难过"，天伤天刑加夹地，为寿终时间点。
  - **现代应用**：普通而福厚的命局，在晚年遇到天伤天刑之年，应及早安排养老与医疗支持，把有限寿元用在质量而非继续硬撑工作。"""
    normalized_text_zh: str = """"""
    subject: str = "传毅之命"
    factor_refs: list = ['pattern_qingyangfenglishi', 'pattern_tianshijiadi', 'pattern_tianshangtianxing', 'source_ref', 'rel_fuyi_001', 'pattern_quanluge', 'rel_fuyi_002', 'pattern_tianshijiadi', 'rel_fuyi_003', 'pattern_tianshangtianxing', 'evi_fuyi_001', 'pattern_tianshangtianxing', 'rule_tianshi_tianxing', 'concept_blade_warrior', 'concept_wound_punishment']
    
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
        l1_anchor="zw_v1.0.0_传毅之命_001_L1",
    )
    version: str = "1.0.0"
