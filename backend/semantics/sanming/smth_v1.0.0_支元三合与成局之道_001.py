"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264437
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
    semantic_id="smth_v1.0.0_支元三合与成局之道_001",
    book_id="sanming",
    engine_id="bazi"
)
class 支元三合与成局之道(SemanticEntry):
    """
    - **原文（source_text）**：  
  论支元三合考历家，申子辰初之气，俱起于漏下一刻，巳酉丑初之气，俱起于二十六刻，寅午戌初之气，俱起于五十一刻，亥卯未初之气，俱起于七十六刻，气皆起于...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论支元三合考历家，申子辰初之气，俱起于漏下一刻，巳酉丑初之气，俱起于二十六刻，寅午戌初之气，俱起于五十一刻，亥卯未初之气，俱起于七十六刻，气皆起于同刻，是天地自然之理也，故谓之三合。或以三合者，如人一身之运用也。精乃气之元，气乃神之本，是以精为气之母，神为气之子，子母互相生，精气神全而不散之为合。盖谓支属人元，故以此论之。如申子辰，申乃子之母，辰乃子之子，申乃水生，子乃水旺，辰乃水库，生即产，旺即成，库即收，冇生有成有收，万物得始得终，乃自然之理，故申子辰为水局。若三字缺其一，则化不成局，不可以三合化局论。巳酉丑、寅午戌、亥卯未皆然。五行不言土者，四行皆赖土成局，万物皆归藏于土故也。若辰戌丑未，全自作土局论。凡命有合，要得局为佳……又如丙人见己酉丑，丁人见寅午戌，为三会禄格……

- **规范化释义（primary_lang_explained）**：  
  本段将六合扩展为“三合成局”的概念。历法上，申子辰、巳酉丑、寅午戌、亥卯未四组三合，其“初之气”分别起于同一刻度，因此被视为天地自然赋予的一体化气场。作者又以“精、气、神”的类比说明三合之所以成局：以申子辰为例，申为水之生（母），子为水之旺（成），辰为水之库（收），生—旺—库构成“生有源、旺有极、收有藏”的闭环，才称为真正的水局。其他三合局（火局、金局、木局）亦然。土虽然不入四组三合，却被视为成局的“场地与容器”，所以另以辰戌丑未全聚时自成土局。实务上，“有合要得局为佳”：单支六合只是两点互动，而三合成局才意味着一个五行系统从生到收的完整展开，因此在看格局时，若能构成局，往往较单支之合更为重要。

- **完整对等诠释（secondary_lang_full）**：  
  This section elevates the discussion from simple pairwise harmonies to full "formation of a局" (ju), or configuration. Drawing on calendrical considerations, it notes that in each of the four elemental triads—Shen‑Zi‑Chen (Water), Si‑You‑Chou (Metal), Yin‑Wu‑Xu (Fire), Hai‑Mao‑Wei (Wood)—the initial qi arises at the same clock‑mark, suggesting that these three Branches act as a single extended phase rather than isolated points. To make this intelligible, the author likens the triad to the relation between essence (jing), qi and spirit (shen): in the Water triad, Shen corresponds to birth, Zi to flourishing, Chen to storage; together they ensure that there is a source, a peak and a place of return. If any one is missing, transformation cannot be completed and we must not call it a true Water局. The same reasoning applies to the other elemental triads. Earth, while not included among the four triads, is said to be the medium upon which all局 stand; only when all four Earth Branches—Chen, Xu, Chou, Wei—gather can we speak of an autonomous Earth局. In practice, the presence of a full三合局 in a chart signals that one element has a complete life‑cycle infrastructure, which can support stable talents, careers or life themes in that domain, whereas scattered harmonies without成局 may yield only intermittent benefits.

- **核心要点**：
  - 三合比六合更强调“成局”：必须凑齐三支，才算完成一个五行从生到收的闭环。
  - 申子辰水局、巳酉丑金局、寅午戌火局、亥卯未木局，各自承担“生—旺—库”的分工。
  - 土局（辰戌丑未）虽然不在四组三合之列，却是所有局得以立足与归藏的根基。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_133]` `[trigger: 三合成局]` `[factor_trigger: sanhe_chengju AND shengwangku_bihuan]` `[role: 主干]` 申子辰，申乃子之母，辰乃子之子，申乃水生，子乃水旺，辰乃水库，生即产，旺即成，库即收。 → 《三命通会》卷十#支元三合与成局之道
  - `[ns_smth_10_134]` `[trigger: 精气神全]` `[factor_trigger: jingqishen_quan AND zimu_husheng]` `[role: 主干依赖]` 精乃气之元，气乃神之本，是以精为气之母，神为气之子，子母互相生，精气神全而不散之为合。 → 《三命通会》卷十#支元三合与成局之道
  - `[ns_smth_10_135]` `[trigger: 缺一不成]` `[factor_trigger: queyi_bucheng AND huabuchengju]` `[role: 条件分支]` 若三字缺其一，则化不成局，不可以三合化局论。 → 《三命通会》卷十#支元三合与成局之道
  - `[ns_smth_10_136]` `[trigger: 土为根基]` `[factor_trigger: tu_wei_genji AND wanwu_guicang]` `[role: 总结]` 五行不言土者，四行皆赖土成局，万物皆归藏于土故也。 → 《三命通会》卷十#支元三合与成局之道

- **详细解说**：  
  若将三合视为“系统”，那么六合更像是“系统中两个节点之间的友好通道”。在判断格局时，三合成局往往意味着某一五行在现实中有比较完整的资源链与情境支撑：例如火局完整者，常在表达、自我呈现、权力运用等方面拥有从起势到收束的能力；水局完整者，则在信息流、适应力与隐藏/调节方面有全链路的运作。工程上，可将三合局编码为高权重的结构因子：一旦识别某三支齐备且未被严重刑冲破害，即可将对应五行标记为 high_infrastructure（高基础设施）状态，并在后续推断中，给予相关职业、能力与事件更高的稳定度评分。

- **校勘与字词辨析（双语）**：
  - **中文**：“得一分三，折月中之仙桂”一语，原文用来形容某些三会禄格之妙，本精校在此条只点出其“由一支推及三支”的扩展思路，具体格局另立条目处理。
  - **English**: The metaphor of essence‑qi‑spirit is kept as a structural analogy; in modern usage it can be reframed as source‑process‑outcome within a given elemental domain."""
    normalized_text_zh: str = """"""
    subject: str = "支元三合与成局之道"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_支元三合与成局之道_001_L1",
    )
    version: str = "1.0.0"
