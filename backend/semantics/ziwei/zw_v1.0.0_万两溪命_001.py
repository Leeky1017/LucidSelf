"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699806
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
    semantic_id="zw_v1.0.0_万两溪命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 万两溪命(SemanticEntry):
    """
    - 分字分词释义：

  - **禄权坐守**：禄星与权星同守要宫，主财富与权力基础稳固。
  - **昌曲夹命**：文昌文曲夹命宫，主文采与聪慧。
  - **左右加会**：左辅右彼加会命局，主辅助...
    """
    
    original_text: str = """- 分字分词释义：

  - **禄权坐守**：禄星与权星同守要宫，主财富与权力基础稳固。
  - **昌曲夹命**：文昌文曲夹命宫，主文采与聪慧。
  - **左右加会**：左辅右彼加会命局，主辅助与人脉。
  - **富贵双全福寿有终**：富贵与福寿皆圆满的命局状态。
  - **天罗擎羊之地**：天罗与擎羊同在之地，主网罗困缚下的突发打击。
  - **陀罗夹地**：陀罗夹住地支基础，主根基受挤压与扭曲。
  - **阴男木三局**：万两溪命盘的五行局数，木三局主生发巨富。

- **原文（source_text）**：  
  万两溪命。阴男木三局。此为禄权坐守，昌曲夹命，左右加会，富贵双全，福寿有终。七十六岁，少限到天罗擎羊之地，太岁又遇陀星夹地，是以命亡。

- **规范化释义（primary_lang_explained）**：  
  万两溪命为阴男木三局，「禄权坐守，昌曲夹命，左右加会」，是极重财禄与人脉资源的富贵结构：禄星与权星牢牢守于命财要位，文昌文曲夹命，再加左右辅弼，多主财富丰厚、人脉通达且有清雅风致。「万两」之名点明其巨富之象。原文又言「福寿有终」，说明整体寿数与福报皆较圆满。  
  七十六岁时，小限行至天罗擎羊之地，太岁又遇陀罗夹地，是「天罗 + 擎羊 + 陀罗夹地」的晚年重凶组合：天罗主网罗困缚，擎羊与陀罗主突发打击与硬碰，夹住地支根基。即便是福寿本完的命局，在此岁运中仍完成寿终的收束。

- **完整对等诠释（secondary_lang_full）**：  
  Wan Liangxi’s chart is that of a Yin Wood native in the Third Configuration. With Lu and Quan sitting guard, Wen Chang and Wen Qu flanking the Life and Zuo‑You assisting, the "Lu‑Quan seated, Chang‑Qu encasing, Zuo‑You assisting" pattern indicates abundant wealth, strong networks and cultured refinement—the name "Ten‑Thousand Taels" underlines this. The text notes that "blessings and lifespan reach completion," suggesting a broadly fulfilled life.  
  At seventy‑six, however, the minor period reaches the Tian Luo–Qing Yang region and Tai Sui encounters Tuo Luo forming a clamp. This "net + Blade + Tuo" combination traps the foundations even for a chart otherwise disposed to full term. Death at that point represents a natural closure under relatively heavy affliction. The case illustrates a wealthy, long‑lived pattern whose end still coincides with a strongly configured limiting year.

- **核心要点**：  
  1. 禄权坐守、昌曲夹命、左右加会，是「富贵双全、福寿有终」的富贵长寿格。  
  2. 七十六岁小限到天罗擎羊之地，太岁遇陀罗夹地，为晚年高危年份。  
  3. 命例展现「巨富且寿终圆满，却仍在天罗擎羊陀罗组合年份完成收束」。"""
    normalized_text_zh: str = """"""
    subject: str = "万两溪命"
    factor_refs: list = ['pattern_luquan_zuoshou', 'pattern_changqu_jiaming', 'pattern_zuoyou_jiahui', 'quality_fugui_fushou', 'malefic_tianluo_qingyang', 'malefic_tuoluo_jiadi']
    
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
        l1_anchor="zw_v1.0.0_万两溪命_001_L1",
    )
    version: str = "1.0.0"
