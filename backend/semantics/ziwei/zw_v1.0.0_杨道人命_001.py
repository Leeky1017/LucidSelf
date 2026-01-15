"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699763
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
    semantic_id="zw_v1.0.0_杨道人命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 杨道人命(SemanticEntry):
    """
    - 分字分词释义：

  - **极居卯地**：命局重心落在卯宫，主表现欲与对外伸展。
  - **权禄加会**：权星与禄星加会命局，主有名望与资源。
  - **刑忌会合**：刑星与忌星会合，主能量...
    """
    
    original_text: str = """- 分字分词释义：

  - **极居卯地**：命局重心落在卯宫，主表现欲与对外伸展。
  - **权禄加会**：权星与禄星加会命局，主有名望与资源。
  - **刑忌会合**：刑星与忌星会合，主能量受限与矛盾。
  - **不过虚名而已**：仅得虚名而缺乏实在权力或成就。
  - **不宜寅申限**：子年生人不宜行寅申之限，主冲击与不顺。
  - **天空擎羊之地**：虚空与擎羊同宫之地，主支撑消失而突遭冲击。
  - **阳男金四局**：杨道人命盘的五行局数，金四局主刚断半出世。

- **原文（source_text）**：  
  杨道人命。阳男金四局。极居卯地，虽有权禄加会，被刑忌会合，不过𮓡名而已。子生人不宜寅申限，小限又入天空擎羊之地，太岁又忌的，主丧命。

- **规范化释义（primary_lang_explained）**：  
  杨道人命为阳男金四局，「极居卯地」说明命局重点落在卯宫，虽有权禄加会，象征有一定名望与资源，但被刑星与忌星会合，导致能量受限，「不过𮓡名而已」提示其名声多浮于表面，不足以支撑实质地位。道人的身份也呼应其半出世、半在俗的状态。  
  对子年生人而言，寅申为不利之限，小限又行到天空擎羊之地，太岁再带忌星相冲，是「不宜之限 + 天空擎羊 + 忌太岁」的高危组合。天空代表虚空与支撑消失，擎羊主突发冲击，忌太岁则放大矛盾与损耗，最终主其丧命。

- **完整对等诠释（secondary_lang_full）**：  
  Yang the Daoist’s chart is that of a Yang Metal native in the Fourth Configuration. Strongly rooted in Mao, it enjoys Power and Lu converging, but these are bound by刑 and Ji‑type stars. The result is some degree of reputation—"a name"—without the full substance of enduring position. His identity as a Daoist fits this in‑between, semi‑worldly role.  
  For a Zi‑year native, Yin and Shen periods are problematic. When the minor period enters the Tian Kong–Qing Yang sector and the Annual Tai Sui carries Ji influence, the pattern "unfavourable limits + void‑Blade sector + malefic Tai Sui" emerges. It suggests that support structures vanish just as sharp conflicts peak. Under this convergence, death is indicated. The case outlines a destiny with modest, somewhat hollow fame that ends under a convergence of void and cutting transits.

- **核心要点**：  
  1. 极居卯地、权禄加会但刑忌会合，形成「有名而难有实」的道人格局。  
  2. 子年生人不宜寅申限，小限入天空擎羊之地，太岁又带忌星，构成高危年份。  
  3. 命例呈现「半出世名士在虚空与冲击并临之年丧命」的命途。"""
    normalized_text_zh: str = """"""
    subject: str = "杨道人命"
    factor_refs: list = ['pattern_ji_ju_mao', 'pattern_quanlu_jiahui', 'malefic_xingji_huihe', 'quality_buguo_xuming', 'timing_buyi_yinshen', 'malefic_tiankong_qingyang']
    
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
        l1_anchor="zw_v1.0.0_杨道人命_001_L1",
    )
    version: str = "1.0.0"
