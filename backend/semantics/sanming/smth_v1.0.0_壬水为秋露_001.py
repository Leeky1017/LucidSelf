"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042613
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
    semantic_id="smth_v1.0.0_壬水为秋露_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬水为秋露(SemanticEntry):
    """
    - **原文（source_text）**：
  壬水为秋露。春亦有露，何独拟之以秋？盖春露为雨露既濡之露，秋露为霜露既降之露也。露一也，春主生，秋主杀，功用不同有如此。然吾以壬为秋露也，盖露属水，而...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬水为秋露。春亦有露，何独拟之以秋？盖春露为雨露既濡之露，秋露为霜露既降之露也。露一也，春主生，秋主杀，功用不同有如此。然吾以壬为秋露也，盖露属水，而壬水生于申，水本能生木者，水既然在此而生，木何由于此而绝？故知壬之为露，秋露也。如壬日生秋，见丁火最显，丁为星河，壬为秋露，一洗炎蒸，象纬昭然矣。

- **分字分词释义**：
  - **秋露与春露**：同为露水，功能一生一杀，侧重点不同。
  - **壬为秋露**：壬水生于申，偏应秋季肃杀之露。
  - **一洗炎蒸、象纬昭然**：露与星河相映，清凉而显文采。

- **规范化释义（primary_lang_explained）**：
  壬水被拟为秋露：露水属水，春露偏向滋生，秋露偏向收敛与肃杀。壬水生于申金，位置上更接近秋露之象，因此取「秋露」而非「春露」。壬日生于秋令，若命局见丁火，如秋夜星河映露，可洗去夏日炎蒸，使格局清朗、文章星象分明。

- **完整对等诠释（secondary_lang_full）**：
  Ren Water is here narrowed from oceans and great rivers to the image of autumn dew. Dew in spring nourishes new life; in autumn it accompanies decline and killing. Both are water, but their functions differ. Because Ren is born in Shen Metal, close to the autumn sector, the text assigns it to this latter image: cool droplets that appear after heat, signalling contraction and review. For a Ren‑day person born in autumn, the presence of Ding Fire is especially prized, like a clear Milky Way mirrored in beads of dew: together they “wash away the steaming heat”, making the pattern bright, articulate, and refined. In practical reading this points to Ren as the phase of cooling down, taking stock, and clarifying structures after intense activity, rather than a symbol of lifelong coldness; the risk is only when cooling becomes permanent frost and no new movement follows."""
    normalized_text_zh: str = """"""
    subject: str = "壬水为秋露"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_壬水为秋露_001_L1",
    )
    version: str = "1.0.0"
