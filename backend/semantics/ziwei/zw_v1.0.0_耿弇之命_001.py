"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699177
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
    semantic_id="zw_v1.0.0_耿弇之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 耿弇之命(SemanticEntry):
    """
    - 分字分词释义：

  - **破军子午宫**：破军星在子或午宫，主官至三公。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，主文武双全。
  - **大限天伤**：大限行至天伤星宫位，有...
    """
    
    original_text: str = """- 分字分词释义：

  - **破军子午宫**：破军星在子或午宫，主官至三公。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，主文武双全。
  - **大限天伤**：大限行至天伤星宫位，有巨门之嫌。
  - **沉马**：太岁到午宫为沉马，主行军险阻。
  - **流羊当头**：流年擎羊直冲命宫，主血光灾祸。
  - **小限冲太岁**：小限与太岁相冲，为命亡应期。
  - **阴男金四局**：耕弇命盘的五行局数，金四局主刚断决绝。

- **原文（source_text）**：  
  耕弇之命。阴男金四局。破军若在子午宫，官资清题至三公，又兼左右昌曲加会，文武双全。富贵之命，大限到于天伤，有嫌巨门。太岁到午，谓之沉马，流羊当头，小限冲太岁凶，故死。

- **规范化释义（primary_lang_explained）**：  
  耿弇命属阴男金四局，破军在子午宫，主官资清显至三公，左右昌曲加会，文武双全。大限到天伤有巨门之嫌，太岁到午为沉马，流羊当头，小限冲太岁，诸凶叠加而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Geng Yan's Yin male Metal Fourth chart has Po Jun in Zi‑Wu palace—official rank rising to Three Dukes. Left‑Right Chang‑Qu converge, dual civil‑martial talents. Major reaches Celestial Wound with Jumen concern. Tai Sui at Wu is Sinking Horse; transiting Blade strikes head; minor clashes Tai Sui. Malefics cause death.

- **核心要点**：  
  1. 破军子午宫，主官至三公。  
  2. 大限天伤有巨门，太岁沉马流羊当头。  
  3. 小限冲太岁，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **三公之命**："破军若在子午宫，官资清题至三公，又兼左右昌曲加会"，耿弇命主武功显赫、位列三公。
  - **沉马流羊**："大限到于天伤，有嫌巨门。太岁到午，谓之沉马，流羊当头"，沉马加流羊，主行军险阻与血光灾祸。
  - **小限冲岁**："小限冲太岁凶，故死"，小限与太岁相冲，为具体殒命触发点。
  - **现代应用**：从军从警或高危行业者，遇沉马+流羊+小限冲太岁的组合年份，应严控出勤与危险任务配置。"""
    normalized_text_zh: str = """"""
    subject: str = "耿弇之命"
    factor_refs: list = ['pattern_pojunziwu', 'pattern_liuyangdangtou', 'pattern_xiaoxianchongtaisui', 'source_ref', 'rel_gengyan_001', 'pattern_pojunziwu', 'rel_gengyan_002', 'star_chenma', 'rel_gengyan_003', 'pattern_xiaoxianchongtaisui', 'evi_gengyan_001', 'pattern_xiaoxianchongtaisui', 'rule_chenma_liuyang', 'concept_pojun_noble', 'concept_blade_head']
    
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
        l1_anchor="zw_v1.0.0_耿弇之命_001_L1",
    )
    version: str = "1.0.0"
