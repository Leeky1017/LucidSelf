"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932712
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
    semantic_id="dts_v1.0.0_配合干支仔细详_断人祸福与灾祥_001",
    book_id="dts",
    engine_id="bazi"
)
class 配合干支仔细详断人祸福与灾祥(SemanticEntry):
    """
    - 原文（source_text）：
  配合干支仔细详，断人祸福与灾祥。

- 原注（原文注解）：
  　　干支配合，细详其进退之机.

- 分字分词释义：
  - 配合：匹配与组合（干与支、透与藏...
    """
    
    original_text: str = """- 原文（source_text）：
  配合干支仔细详，断人祸福与灾祥。

- 原注（原文注解）：
  　　干支配合，细详其进退之机.

- 分字分词释义：
  - 配合：匹配与组合（干与支、透与藏）。
  - 干支：天干地支（十干与十二支）。
  - 仔细：细致、逐条不漏.

- 规范化释义（primary_lang_explained）：
  命局之判断必在干支的组合细察：透干与藏干、支神与支局、通根与通关、相生相克之情义.细到每一处气机的进退、根脉与泄制，方能精准断祸福与灾祥.

- **次语种完整诠释（secondary_lang_full）**：  
  Accurate judgment of fortune and misfortune (Huo Fu Yu Zai Xiang) requires meticulous scrutiny (Zi Xi Xiang) of stem-branch combinations (Gan Zhi Pei He). This scrutiny operates across three integrated dimensions: revelation-concealment structure (stems transparent versus roots hidden in branches), assembly-flow structure (how branches form trines, directional gatherings, or conflicting patterns), and affection-conflict dynamics (harmonious generation-combination versus antagonistic control-clash-harm). Heavenly Stems serve as the manifest "banner" displaying function and role, while Earthly Branches provide the foundational "roots" supplying substance and background support. One cannot evaluate destiny by examining stems or branches in isolation—comprehensive assessment of their pairing layouts, flow pathways, and relational sentiments is essential for refined discernment of auspicious and inauspicious outcomes.

- **核心要点**：
  - 干为旗、支为根：天干表现为显露的功能，地支是根基与背景
  - 透与藏：同一五行可透干见用或只藏支中不显，透则显事、藏则潜机
  - 局与路：地支构成三合、方局、刑冲等气路，决定能量流向
  - 情与义：生合为有情、冲克为无情，还须察有无解路、轻重缓急
  - 不可只看天干或只看地支，须综合评估配合结构
  - 同一喜用在不同配合下祸福可大异

- **详细解说**：
  本条强调命局判断的核心在于干支配合的细致审察。天干如同"旗号"，显露功能与角色；地支如同"根脉"，提供根气与背景支撑。判断需从三个维度展开：透藏结构（天干显露还是地支伏藏）、支群结构（地支是否成三合、方局或刑冲）、情义关系（生合有情还是冲克无情）。关键洞见：同一五行在不同配合下表现完全不同，如财星透于用神之干与伏于忌神之支，祸福判断天差地别。实占时，须逐一审察每干的通根状态、每支的局势归属，以及干支之间的情义轻重，方能精准断祸福。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_016]` `[trigger: 干支配合]` `[factor_trigger: ganzhi_pairing_map]` `[role: 主干]` 命局之判断必在干支的组合细察，透干与藏干、支神与支局、通根与通关皆须逐一审明。 → 《滴天髓·通天论》#第6条
  - `[ns_dts_017]` `[trigger: 透藏差异]` `[factor_trigger: gan_reveal_state]` `[role: 主干依赖]` 同一五行透干见用与只藏支中不显，其功用与祸福判然有别。 → 《滴天髓·通天论》#第6条
  - `[ns_dts_018]` `[trigger: 情义判断]` `[factor_trigger: qingyi_relation]` `[role: 条件分支]` 生合为有情、冲克为无情只是粗划，更精细者在于有无解路、是否服务于用神。 → 《滴天髓·通天论》#第6条
  - `[ns_dts_107]` `[trigger: 局与路]` `[factor_trigger: branch_cluster]` `[role: 主干依赖]` 地支三合方局与刑冲破害构成气路，决定能量是在局内循环、外泄还是被阻断。 → 《滴天髓·通天论》#第6条
  - `[ns_dts_108]` `[trigger: 实占细察]` `[factor_trigger: ganzhi_pairing_map]` `[role: 总结]` 实占须逐一审察每干通根、每支局势与干支情义轻重，方能精准断祸福灾祥。 → 《滴天髓·通天论》#第6条"""
    normalized_text_zh: str = """"""
    subject: str = "配合干支仔细详，断人祸福与灾祥。"
    factor_refs: list = ['ganzhi_pairing_map', 'gan_reveal_state', 'cang_hidden_state', 'tonggen', 'qingyi_relation', 'huofu_outcome']
    
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
        l1_anchor="dts_v1.0.0_配合干支仔细详_断人祸福与灾祥_001_L1",
    )
    version: str = "1.0.0"
