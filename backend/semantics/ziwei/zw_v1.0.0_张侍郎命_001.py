"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.700039
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
    semantic_id="zw_v1.0.0_张侍郎命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 张侍郎命(SemanticEntry):
    """
    - 分字分词释义：

  - **权会巨门**：权星与巨门同会，主威严直言。
  - **威扬果作谏臣**：因权巨同会而敢于直言进谏。
  - **太阴文昌于妻宫蟾宫折桂**：太阴文昌同在妻宫，主科名...
    """
    
    original_text: str = """- 分字分词释义：

  - **权会巨门**：权星与巨门同会，主威严直言。
  - **威扬果作谏臣**：因权巨同会而敢于直言进谏。
  - **太阴文昌于妻宫蟾宫折桂**：太阴文昌同在妻宫，主科名之喜。
  - **太阳文曲于官禄皇殿朝班**：太阳文曲同在官禄宫，主朝堂显赫地位。
  - **癸生人会巨门石巾隐玉格**：癸年生人遇巨门形成的格局，主才华内敛终显。
  - **只兄弟落陷**：唯一不足是兄弟宫落陷，同辈关系欠佳。
  - **阴男金四局**：张侍郎命盘的五行局数，金四局主刚断谏臣。

- **原文（source_text）**：  
  张侍郎命。阴男金四局。权会巨门，威扬果作谏臣。太阴文昌于妻宫，蟾宫折桂；太阳文曲于官禄，皇殿朝班。癸生人会巨门，为石巾隐玉格，信此验矣。只兄弟落陷，果是否不如人矣。

- **规范化释义（primary_lang_explained）**：  
  张侍郎命为阴男金四局，「权会巨门，威扬果作谏臣」，权星与巨门同会，形成敢于直言进谏的威严形象，故为「谏臣」类型的官员。「太阴文昌于妻宫，蟾宫折桂」，太阴与文昌同在妻宫，暗示配偶或自身有科名之喜（「蟾宫折桂」喻中科举）。「太阳文曲于官禄，皇殿朝班」，太阳与文曲同在官禄宫，主在朝堂上有显赫地位。「癸生人会巨门，为石巾隐玉格」，癸年生人遇巨门形成「石巾隐玉」格局，寓意才华内敛而终显。「只兄弟落陷，果是否不如人矣」，唯一不足是兄弟宫落陷，说明同辈关系或手足缘分较差。

- **完整对等诠释（secondary_lang_full）**：  
  Attendant Zhang's chart is that of a Yin Metal male. Quan meeting Ju Men creates the bold remonstrance of a court censor. Tai Yin and Wen Chang in the Spouse palace suggest "plucking cassia on the Moon"—exam success. Tai Yang and Wen Qu in Office signal presence at the imperial court. For someone born in Gui year, Ju Men forms the "Jade Hidden Beneath Stone Cloth" pattern—latent talent eventually revealed. Only the Siblings palace falls, so brotherly relations are weak.

- **核心要点**：  
  1. 权会巨门，威扬果作谏臣，敢于直言。  
  2. 太阴文昌妻宫配太阳文曲官禄，蟾宫折桂与皇殿朝班兼具。  
  3. 癸生人会巨门为石巾隐玉格，唯兄弟落陷不足。"""
    normalized_text_zh: str = """"""
    subject: str = "张侍郎命"
    factor_refs: list = ['pattern_quan_hui_jumen', 'quality_weiyang_jianchen', 'pattern_taiyin_chang_qigong', 'pattern_taiyang_qu_guanlu', 'pattern_shijin_yinyu', 'malefic_xiongdi_luoxian']
    
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
        l1_anchor="zw_v1.0.0_张侍郎命_001_L1",
    )
    version: str = "1.0.0"
